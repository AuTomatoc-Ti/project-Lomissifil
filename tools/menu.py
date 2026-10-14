#!/usr/bin/env python3
"""The coining MENU: browse the candidate pool by sound, ranked to favour what is OURS.

Author's ruling 2026-10-14: the menu is deliberately BIASED, because
`tools/fingerprint.py` measured which parts of our sound profile are un-donated
(decision/06-neutrality.md -> "Measurement"):

    +2   an AREA-RULE word-final f / w / h       (A15 -- no donor at all)
    +2   a VCV-only cluster fm fn hm hn wm wn jm jn   (A13 -- near-unattested)
    +2   a HIATUS "leap" iu yu ia ya             (A4  -- a designed 2x2, no donor)
    +1   an onset cluster pr br tr dr kr gr      (A12 -- a whitelist, not a copy)
    -2   the form IS an English word             (measured: 143 of 105,936 forms are)

Every point is printed with its reason, so the ranking can be audited and the weights changed in
one place (score() below). This biases the SHORTLIST, never the language: the pool is unchanged.

USAGE
    python3 tools/menu.py > lists/menu.md
    python3 tools/menu.py --group th --per 6      # browse one sound in depth
    python3 tools/menu.py --top 20 --per 3
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import syllabify as S                      # noqa: E402

AREA_FINALS = ("f", "w", "h")                                    # +2  (A15)
VCV_CLUSTERS = ("fm", "fn", "hm", "hn", "wm", "wn", "jm", "jn")  # +2  (A13)
LEAPS = ("iu", "yu", "ia", "ya")                                 # +2  (A4)
ONSET_CLUSTERS = ("pr", "br", "tr", "dr", "kr", "gr")            # +1  (A12)
ENGLISH_DICT = "/usr/share/dict/words"


def load_english():
    """-> set of English words, or None when the machine has no dictionary."""
    if not os.path.exists(ENGLISH_DICT):
        return None
    out = set()
    for ln in open(ENGLISH_DICT, encoding="utf-8", errors="ignore"):
        w = ln.strip().lower()
        if w.isalpha() and len(w) >= 2:
            out.add(w)
    return out


def score(form, words):
    """-> (score, [reasons]). Auditable: every point names its source (see the docstring)."""
    why, sc = [], 0
    if form[-1] in AREA_FINALS:
        sc += 2
        why.append("area-rule final (+2)")
    if form[-1] == "s":
        sc -= 1            # R4 is USAGE-LIMITED by the author: the `s` branch is reserved, so an
        why.append("`s`-final: reserved branch, meant to be RARE (-1)")   # s-final root is a
                                                                          # deliberate, unusual pick
    for c in VCV_CLUSTERS:
        if c in form:            # legal ONLY intervocalically (P2), so a hit is always the cluster
            sc += 2
            why.append("un-donated cluster %s (+2)" % c)
            break
    for l in LEAPS:
        if l in form:            # a leap pair is ALWAYS a hiatus (V7-V9), never a diphthong
            sc += 2
            why.append("hiatus leap %s (+2)" % l)
            break
    for c in ONSET_CLUSTERS:
        if c in form:
            sc += 1
            why.append("onset cluster %s (+1)" % c)
            break
    if words is not None and form in words:
        sc -= 2
        why.append("IS an English word (-2)")
    return sc, why


HEADER = """\
# lists/menu.md - GENERATED coining menu. DO NOT ANNOTATE HERE.

Regenerate with:

```
python3 tools/menu.py > lists/menu.md
```

**Picks go in `lists/picks.md`** - record the FORM TEXT, not just a number. Any note written in this
file is lost on regeneration.

## The ranking is deliberate (author's ruling 2026-10-14)

`tools/fingerprint.py` measured which parts of our sound profile are **un-donated** (see
`../decision/06-neutrality.md` -> "Measurement"). This menu pushes those to the top:

| points | what triggers it | why it counts as ours |
|---|---|---|
| **+2** | word-final `f` / `w` / `h` | the **area rule** (A15) - no language in the reference set does this |
| **+2** | an intervocalic cluster `fm fn hm hn wm wn jm jn` | A13 - near-unattested |
| **+2** | a hiatus "leap" `iu yu ia ya` | A4 - a designed 2x2, no donor |
| **+1** | an onset cluster `pr br tr dr kr gr` | A12 - a whitelist, not a copy of any language |
| **-1** | an `s`-final form | **R4**: the `s` branch is RESERVED for a future adjective / adverb job, so `s`-final roots are meant to be **RARE** (author's ruling) |
| **-2** | the form **IS an English word** | measured: 421 of 133,845 forms (0.315%) are in Webster's 2nd |

Every row shows **why** it scored. The weights live in one place: `tools/menu.py`, `score()`.

⚠️ This biases the *shortlist*, never the language: the pool is untouched, and a low score is not a
verdict - it only means "this form is built from material that many languages share".

## How to read a row

`#` is this menu's own numbering. `syllables` and `stress` come from `tools/syllabify.py` (default
stress = the 2nd syllable of the root, P4/N1; the capital lands on the *first letter* of the stressed
syllable). **A group of seven rows is ONE base**, in the fixed order
`+f | +w (/v/) | +h | +s | +m | +r | bare`, and a base yields exactly **2** roots - so pick **at most
one** from the `{+f, +w}` pair and **at most one** from the `{+h, +s, +m, +r, bare}` group. (`+s` is
reserved for adjective/adverb duty, `+m` suits front-vowel roots, `+r` is for function words -- see
**R4**/**R6** in the decision log; the menu prints a soft-rule note when a form breaks one.)

> Sound-only: R3 is PARKED, so assign **no meanings** (`../decision/03-open-questions.md` section 0
> item 14). A pick is not a word; `../reference/example.md` stays the only source for examples.

---
"""

FOOTER = """
---

## What the menu does NOT do

- It cannot tell you what sounds *beautiful* - that is the part only you can supply.
- It contains **no 1-syllable (`roi`-class) root**: the pool is the 2-syllable core
  (`../decision/03-open-questions.md` section 0 item 22). Wanting short roots in this round means
  extending that pool FIRST - which changes the numbering here.
- It does not test the **M3a seam** (root-final `f`/`w`/`h` + a case suffix, always unstressed) -
  still unjudged (section 0 item 20), and it fires for 3 of every 4 coined roots.
"""


def _syl_parts(s):
    """-> (onset, nucleus, coda) of one syllable string, or None."""
    toks = S.tokenize(s)
    if not toks:
        return None
    i = 0
    on = []
    while i < len(toks) and toks[i][0] == "C":
        on.append(toks[i][1])
        i += 1
    if i >= len(toks):
        return None
    nuc = toks[i][1]
    i += 1
    cod = []
    while i < len(toks) and toks[i][0] == "C":
        cod.append(toks[i][1])
        i += 1
    return "".join(on), nuc, "".join(cod)


def menu(src, top, per, max_en, group=None, mono_top=12):
    words = load_english()
    bases = [ln.strip() for ln in open(src, encoding="utf-8")
             if ln.strip() and not ln.startswith("#")]
    data = []
    for b in bases:
        rows = []
        for form in (b + "f", b + "w", b + "h", b + "s", b + "m", b + "r", b):
            an = S.analyse(form)
            sc, why = score(form, words)
            rows.append((form,
                         "-".join(an["syllables"]) if an["syllables"] else "ILLEGAL",
                         an["stressed"] or "-", sc, "; ".join(why) if why else "-"))
        on = nuc = "(none)"
        is_mono = False
        syl = S.analyse(b)["syllables"]
        if syl:
            is_mono = len(syl) == 1
            sp = _syl_parts(syl[0])
            if sp:
                on, nuc = sp[0] or "(none)", sp[1]
        data.append({"base": b, "rows": rows, "best": max(r[3] for r in rows),
                     "on": on, "nuc": nuc, "mono": is_mono})
    counter = [0]

    def section(title, items):
        out.append("## %s\n\n" % title)
        out.append("| # | base | form | syllables | stress | score | why |\n"
                   "|---|---|---|---|---|---|---|\n")
        for d in items:
            for form, syl, st, sc, why in d["rows"]:
                counter[0] += 1
                out.append("| %d | %s | %s | %s | %s | %+d | %s |\n"
                           % (counter[0], d["base"], form, syl, st, sc, why))
        out.append("\n")

    def rank(items):
        return sorted(items, key=lambda d: (-d["best"], d["base"]))

    out = [HEADER]
    if group:
        sel = [d for d in data if d["on"] == group or d["nuc"] == group]
        section("`%s` (%d bases; top %d)" % (group, len(sel), per), rank(sel)[:per])
    else:
        section('Top %d bases - the most "ours" material' % top, rank(data)[:top])
        monos = rank([d for d in data if d["mono"]])
        section("one-syllable roots (the `roi` class): top %d of %d - they are EXEMPT from the soft "
                "distance>=2 rule, so they resemble each other by nature" % (mono_top, len(monos)),
                monos[:mono_top])
        for g in sorted(set(d["on"] for d in data)):
            items = [d for d in data if d["on"] == g]
            sel = rank(items)[:per]
            for d in rank([x for x in items if x["mono"]])[:1]:      # guarantee one short root
                if d not in sel:
                    sel.append(d)
            section("bases starting with `%s`" % g, sel)
        for g in sorted(set(d["nuc"] for d in data)):
            items = [d for d in data if d["nuc"] == g]
            sel = rank(items)[:per]
            for d in rank([x for x in items if x["mono"]])[:1]:
                if d not in sel:
                    sel.append(d)
            section("bases whose first vowel is `%s`" % g, sel)
    hits = [f for d in data for (f, _, _, _, why) in d["rows"] if "IS an English word" in why]
    out.append("## English collisions (measured - avoid or accept knowingly)\n\n")
    out.append("%d forms are literally in `/usr/share/dict/words`, so a pick can never hit one by "
               "accident:\n\n" % len(hits))
    out.append("```\n%s\n```\n\n" % " ".join(hits[:max_en]))
    if len(hits) > max_en:
        out.append("(... and %d more; raise --max-en)\n\n" % (len(hits) - max_en))
    out.append(FOOTER)
    sys.stdout.write("".join(out))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default="lists/roots-bases-current.txt")
    ap.add_argument("--top", type=int, default=20, help="bases in the 'most ours' section")
    ap.add_argument("--per", type=int, default=1, help="bases per group in the by-sound sections")
    ap.add_argument("--max-en", type=int, default=200, help="cap on the English-collision list")
    ap.add_argument("--group", default=None,
                    help="print only this group, in depth (an initial onset like `th`, or a vowel)")
    ap.add_argument("--mono", type=int, default=12,
                    help="bases in the one-syllable (roi-class) section")
    a = ap.parse_args()
    menu(a.src, a.top, a.per, a.max_en, a.group, a.mono)


if __name__ == "__main__":
    main()


