#!/usr/bin/env python3
"""Neutrality-ledger recount: derive the donor counts from `06-neutrality.md` itself.

Why this exists: the ledger's headline figures ("counted rows 38, Finnish 8/38, original 42%") are
**hand-counted** -- the file says so ("the rules of the count are stated so it can be audited"). Every
new design row silently invalidates them, and `B13` (DAT-possession, 2026-10-15) already did: the file
carries a dated note saying the figures are stale. So this tool derives the count mechanically, states
its rules, and compares its result with the figures the file claims.

USAGE
    python3 tools/neutrality.py                # the recount + the two thresholds + the headroom
    python3 tools/neutrality.py --rows         # one line per row: id / derived class / donors / strength
    python3 tools/neutrality.py --selftest     # pin today's derivation

RULES (stated so the result can be audited, and so disagreements can be argued with)
  * a table row `| id | feature | donor | strength | note |` is COUNTED unless the donor cell says
    "not designed yet" (e.g. `B11`, which the file excludes);
  * a **language** is read out of the donor cell by matching a whitelist, so prose like
    "Finnish (no voicing contrast)" or "Turkish `degil`" counts as ONE language;
  * **no-donor row**  = no whitelisted language, and the cell says none / nothing / no language;
  * **universal row** = languages are named only as a GROUP or "widespread" phrase (a phrase like
    "most European languages" or "too widespread to be one") -> no single donor;
  * **donor row**     = >= 1 named language; **single-donor row** = exactly one named language;
  * thresholds (the author's, as printed in the ledger): the top donor must stay <= 1/3 of the counted
    rows, and the no-donor share must stay >= 1/4.

This is a MEASUREMENT tool: it does not decide whether a row *should* name a donor -- it prints what
the table says, and flags every row where the derived class disagrees with the row's own `strength`
cell, so the author can rule.
"""

import argparse
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.normpath(os.path.join(HERE, "..", "docs", "decisions", "06-neutrality.md"))

ROW_RE = re.compile(r"^\|\s*([ABC]\d+)\s*\|(.*?)\|(.*?)\|(.*?)\|(.*?)\|\s*$")

# longest first, so `Old English` wins over `English`
LANGUAGES = ("Old English", "Castilian", "Icelandic", "Albanian", "Sanskrit", "Bulgarian", "Tibetan",
             "Finnish", "Turkish", "Japanese", "Chinese", "Vietnamese", "Korean", "Italian",
             "Polish", "Germanic", "Slavic", "German", "English", "Hebrew", "Arabic", "Quechua",
             "Tuyuca", "Greek", "Latin", "Thai", "Russian", "Amazigh", "Hungarian", "Estonian")
VAGUE = ("most european", "widespread", "too widespread", "many languages", "a quarter of",
         "no single donor", "not distinctive")
NO_DONOR = ("none", "no donor", "nothing in the reference")


def clean(cell):
    """Strip markdown emphasis / backticks / parentheticals so the words can be read."""
    s = cell.replace("**", "").replace("`", "")
    s = re.sub(r"\([^)]*\)", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def parse(path=LEDGER):
    """-> [ {id, feature, donor, strength, note, raw_feature, raw_donor, raw_strength} ]."""
    rows = []
    for ln in open(path, encoding="utf-8"):
        m = ROW_RE.match(ln.rstrip("\n"))
        if not m:
            continue
        rid = m.group(1)
        if not re.match(r"^[ABC]\d+$", rid):
            continue
        rows.append({"id": rid,
                     "feature": clean(m.group(2)), "donor": clean(m.group(3)),
                     "strength": clean(m.group(4)), "note": clean(m.group(5)),
                     # raw cells: `clean()` deletes parentheticals, and "not (yet) designed" often
                     # lives inside one -- so the skip test must read the untouched text
                     "raw_feature": m.group(2).lower(), "raw_donor": m.group(3).lower(),
                     "raw_strength": m.group(4).lower()})
    return rows


def classify(row):
    """-> (kind, [languages]). kind in {counted-donor, single-donor, universal, no-donor, skip}."""
    if any(re.search(r"not (yet )?designed", row[k]) for k in ("raw_feature", "raw_donor",
                                                               "raw_strength")):
        return ("skip", [])
    donor, note, strength = row["donor"].lower(), row["note"].lower(), row["strength"].lower()
    langs = []
    for name in LANGUAGES:                       # LANGUAGES is longest-first
        low = name.lower()
        if low in donor and not any(low in got.lower() for got in langs):
            langs.append(name)
    vague = any(v in donor or v in note or v in strength for v in VAGUE)
    if langs and not vague:
        return (("single-donor" if len(langs) == 1 else "counted-donor"), langs)
    if langs or vague:
        return ("universal", langs)
    return ("no-donor", [])


def recount(path=LEDGER):
    """-> {rows, kinds, langs, counted, no_donor, universal, single, donor_rows, counts, top}."""
    rows = parse(path)
    kinds, langs = {}, {}
    for r in rows:
        kinds[r["id"]], langs[r["id"]] = classify(r)
    counted = [r for r in rows if kinds[r["id"]] != "skip"]
    counts = {}
    for r in counted:
        if kinds[r["id"]] in ("counted-donor", "single-donor"):
            for _l in langs[r["id"]]:
                counts[_l] = counts.get(_l, 0) + 1
    return {
        "rows": rows, "kinds": kinds, "langs": langs, "counted": len(counted),
        "no_donor": [r["id"] for r in counted if kinds[r["id"]] == "no-donor"],
        "universal": [r["id"] for r in counted if kinds[r["id"]] == "universal"],
        "single": [r["id"] for r in counted if kinds[r["id"]] == "single-donor"],
        "donor_rows": [r["id"] for r in counted
                       if kinds[r["id"]] in ("counted-donor", "single-donor")],
        "counts": counts, "top": sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))}


def headroom(n, top_count):
    """How many MORE rows could be added before a threshold breaks?

    top donor:    (top + r) <= (n + r)/3   ->  r <= (n - 3*top) / 2
    a NEW donor:  (0 + r)   <= (n + r)/3   ->  r <= n / 2
    """
    return max(0, (n - 3 * top_count) // 2), max(0, n // 2)


def report(path=LEDGER, show_rows=False):
    d = recount(path)
    n = d["counted"]
    print("# neutrality recount - derived from %s" % os.path.basename(path))
    print("parsed table rows       : %d  (%d counted, %d skipped as 'not designed yet')"
          % (len(d["rows"]), n, len(d["rows"]) - n))
    print("  donor rows            : %2d  (%s)" % (len(d["donor_rows"]), " ".join(d["donor_rows"])))
    print("  single-donor rows     : %2d  (%s)" % (len(d["single"]), " ".join(d["single"])))
    print("  universal rows        : %2d  (%s)" % (len(d["universal"]), " ".join(d["universal"])))
    print("  no-donor (original)   : %2d  (%s)" % (len(d["no_donor"]), " ".join(d["no_donor"])))
    print("\ntop donors (rows where the language is one of the closest donors):")
    for lang, c in d["top"][:8]:
        print("  %-14s %2d  %5.1f%%" % (lang, c, 100.0 * c / n))
    top_lang, top_c = d["top"][0] if d["top"] else ("-", 0)
    print("\nthresholds (the author's, as printed in the ledger):")
    print("  top donor <= 1/3 of the counted rows : %s   (%s has %d/%d = %.1f%%)"
          % ("PASS" if 3 * top_c <= n else "FAIL", top_lang, top_c, n, 100.0 * top_c / n))
    print("  original  >= 1/4 of the counted rows : %s   (%d/%d = %.1f%%)"
          % ("PASS" if 4 * len(d["no_donor"]) >= n else "FAIL",
             len(d["no_donor"]), n, 100.0 * len(d["no_donor"]) / n))
    r_top, r_new = headroom(n, top_c)
    print("  HEADROOM: %s may gain %d more row(s); a BRAND-NEW donor could appear in up to %d row(s)"
          % (top_lang, r_top, r_new))
    mism = [r["id"] for r in d["rows"]
            if d["kinds"][r["id"]] != "skip"
            and (("no donor" in r["strength"].lower()) != (d["kinds"][r["id"]] == "no-donor"))]
    if mism:
        print("\nAUDIT  derived class disagrees with the row's OWN strength cell: %s" % " ".join(mism))
    if show_rows:
        print("\nper row (id / derived class / languages read / the row's strength cell):")
        for r in d["rows"]:
            print("  %-4s %-14s %-26s %s" % (r["id"], d["kinds"][r["id"]],
                                             ", ".join(d["langs"][r["id"]]) or "-", r["strength"]))
    return d


PRINTED = {      # the ledger's hand count of 2026-10-14, as printed in the file
    "donor_rows": "A1 A3 A6 A7 A8 A9 A10 A11 A12 A14 A16 B1 B4 B5 B6 C1 C2 C5 C6".split(),
    "single": "A1 A3 A6 A10 A11 A14 A16 B6 C6".split(),
    "universal": "A18 B7 B10".split(),
    "no_donor": "A2 A4 A5 A13 A15 A17 B2 B3 B8 B9 C3 C4 C7 C8 C9 C10".split(),
    "counted": 38, "top": ("Finnish", 8),
}
ADDED_SINCE = {                      # rows added AFTER the printed hand count (2026-10-14)
    "donor_rows": ["C11"],                  # the agreeing adjective ending
    "universal": ["B13", "B14", "B15"],     # DAT-possession; evidentiality; the interrogative shift
    "no_donor": ["B16"],                    # the evidential x chord integration
}
# rows the printed count calls single-donor (= exactly one language is CLOSEST -- a judgement) while
# the table's cell names two languages. The tool cannot judge closeness, so it reports them as ties.
SINGLE_BY_JUDGEMENT = "A3 A10 A11".split()


def selftest(path=LEDGER):
    d = recount(path)
    der = {"donor_rows": d["donor_rows"], "single": d["single"], "universal": d["universal"],
           "no_donor": d["no_donor"]}
    bad = 0
    print("self-test - the derivation vs the figures the ledger PRINTS (hand count 2026-10-14):")
    for k in ("donor_rows", "single", "universal", "no_donor"):
        want = PRINTED[k] + ADDED_SINCE.get(k, [])
        extra = sorted(set(der[k]) - set(want))
        missing = sorted(set(want) - set(der[k]))
        ok = not extra and not missing
        if k == "single":
            ok = sorted(set(PRINTED["single"]) - set(der["single"])) == sorted(SINGLE_BY_JUDGEMENT)
            extra, missing = [], []          # explained by the rule difference below, not an error
        bad += 0 if ok else 1
        print("  %-11s %2d row(s)  %s%s" % (k, len(der[k]), "OK" if ok else "DIFF",
                                            "" if ok else "  extra=%s missing=%s" % (extra, missing)))
    print("  (single-donor: the printed count judges CLOSENESS and calls %s single; the table's cells"
          % " ".join(SINGLE_BY_JUDGEMENT))
    print("   name two languages, so this tool reports them as ties -- a RULE difference, pinned.)")
    for k in ("counted", "top"):
        if k == "counted":
            added = sum(len(v) for v in ADDED_SINCE.values())
            got, want = d["counted"], PRINTED["counted"] + added
        else:
            got = d["top"][0] if d["top"] else ("-", 0)
            want = PRINTED["top"]
        ok = got == want
        bad += 0 if ok else 1
        print("  %-11s %-20s expected %-16s %s" % (k, got, want, "OK" if ok else "DIFF"))
    print("self-test:", "ALL PASS" if not bad else "%d DIFF(S)" % bad)
    return 0 if not bad else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description="Recount the neutrality ledger from the table itself.")
    ap.add_argument("--ledger", default=LEDGER)
    ap.add_argument("--rows", action="store_true", help="print one line per table row")
    ap.add_argument("--selftest", action="store_true", help="compare with the printed figures")
    args = ap.parse_args(argv)
    if args.selftest:
        return selftest(args.ledger)
    report(args.ledger, args.rows)
    return 0


if __name__ == "__main__":
    sys.exit(main())
