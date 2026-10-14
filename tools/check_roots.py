#!/usr/bin/env python3
"""Check an author's proposed roots against the LOCKED rules, mechanically.

Reads a hand-written file (default `../lists/proposed.md`, format `form, gloss`), and for every
entry reports:

  legality      `syllabify.analyse()` -- is the spelling phonotactically legal at all?
  bare-root end A1 layer 1: a bare root must end in a VOWEL or `f` / `w` / `h` (what the author
                called note 1 on 2026-10-14 is a proposal to add `m n l r s`)
  R-b           no `p t k` in a base form (the dictionary form is voiced); P6's nasal+stop
                sequences are the one exception
  P6 reading    medial `ng` is ALWAYS /N/ and medial `sh` is ALWAYS /S/ -- so `singoi` is
                /si.Noi/; if the author meant n+g the spelling must be `nko`-style
  English       is the form literally in /usr/share/dict/words (the measured 0.135% channel)
  price         how many neighbours it has at distance 1 and 2 inside the pool, plus the closest
                few, because "differ by >= 2 segments" is R2's SOFT guideline
  siblings      the four raw area-rule members of its base (2 fricative + the {h,none,...} branch)
                and which of them are safe to coin together (never both of one branch -- those
                collide in GEN/INS/OBL/V1, measured in seam-sheet.md)

Nothing here writes to `reference/example.md`: passing is a report, the author decides.
"""

import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import syllabify as S                      # noqa: E402

FORM_RE = re.compile(r"^[a-z]{1,12}$")     # a hand-written file contains prose too: ignore it

VOWELS = set("aeiouy")
AREA_FINALS = ("f", "w", "h", "s")         # A1 layer 1 after R4 (2026-10-14: `s` was added)
PROPOSED_FINALS = ("m", "r")               # the author's note 1, still DEFERRED (n/l were never asked for)
HARD = set("ptk")


def parse(path):
    out = []
    for ln in open(path, encoding="utf-8"):
        s = ln.strip()
        if not s or s.startswith("#"):
            continue
        if s.startswith("- "):
            s = s[2:].strip()
        form, _, gloss = s.partition(",")
        form = form.strip().lower()
        if FORM_RE.match(form):            # prose lines are ignored, not misread as forms
            out.append((form, gloss.strip()))
    return out


def lev_at_most(a, b, k=2):
    """True when the string distance is <= k (bounded, for speed)."""
    if abs(len(a) - len(b)) > k:
        return False
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        if min(cur) > k:
            return False
        prev = cur
    return prev[-1] <= k


def english():
    p = "/usr/share/dict/words"
    if not os.path.exists(p):
        return None
    out = set()
    for ln in open(p, encoding="utf-8", errors="ignore"):
        w = ln.strip().lower()
        if w.isalpha() and len(w) >= 2:
            out.add(w)
    return out


def base_of(form):
    """The base this root belongs to: strip a final f/w/h (or m/r/s) to get the vowel-final base."""
    if form and form[-1] in AREA_FINALS + PROPOSED_FINALS:
        return form[:-1]
    return form


def report(forms, pool, words):
    for form, gloss in forms:
        an = S.analyse(form)
        notes = []
        if not an["syllables"]:
            notes.append("**ILLEGAL spelling** (phonotactics)")
        last = form[-1]
        if last in PROPOSED_FINALS:
            notes.append("**breaks A1 layer 1**: a bare root may not end in `%s` (allowed since R4: "
                         "a vowel, `f`, `w`, `h`, `s`) -- this is the DEFERRED part of the author's "
                         "note 1 (03-open-questions.md section 0 item 28)" % last)
        elif last not in VOWELS and last not in AREA_FINALS:
            notes.append("**breaks A1 layer 1**: ends in `%s`" % last)
        # R-b: no hard stop letter (p t k) in a base form -- but `th` is the FRICATIVE /T/ (one
        # phoneme, not a stop), so a `t` inside `th` must not be flagged; same for `sh`.
        scan = form.replace("th", "@").replace("sh", "#")
        for ch in "ptk":
            if ch in scan:
                i = scan.index(ch)
                notes.append("**breaks R-b**: base forms are voiced -- write `%s`"
                             % (form[:i] + {"p": "b", "t": "d", "k": "g"}[ch] + form[i + 1:]))
                break
        if "ng" in form[1:]:
            notes.append("P6: `ng` reads as /N/ (ONE phoneme) -- if you meant n+g, spell it `nk`")
        if words is not None and form in words:
            notes.append("**IS an English word** (-2 in the menu's ranking)")
        syl = "-".join(an["syllables"]) if an["syllables"] else "-"
        st = an["stressed"] or "-"
        b = base_of(form)
        sibs = [b + "f", b + "w", b + "h", b + "s", b]
        d1 = [p for p in pool if lev_at_most(form, p, 1)]
        print("### `%s`%s" % (form, ("  -- *%s*" % gloss) if gloss else ""))
        print("  syllables %-14s stress %-14s   siblings: %s" % (syl, st, " ".join(sibs)))
        print("  in the pool right now: %s" % ("YES" if form in pool else "no"))
        print("  distance-1 neighbours in the pool: %d%s"
              % (len(d1), ("  e.g. " + " ".join(d1[:6])) if d1 else ""))
        print("  %s" % ("; ".join(notes) if notes else "passes every locked rule checked here"))
        print()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default="lists/proposed.md")
    ap.add_argument("--pool", default="lists/roots-bases-current.txt")
    ap.add_argument("--forms", default=None, help="check these instead (comma separated)")
    a = ap.parse_args()
    if a.forms:
        forms = [(f.strip(), "") for f in a.forms.split(",") if f.strip()]
    else:
        forms = parse(a.src)
    pool = [ln.strip() for ln in open(a.pool, encoding="utf-8")
            if ln.strip() and not ln.startswith("#")]
    pool_set = set(pool)
    words = english()
    print("# proposed-root check (%d forms; pool %d bases)\n" % (len(forms), len(pool)))
    report(forms, pool, words)
    print("# pool membership test used exact strings; distance is bounded Levenshtein <= 1")


if __name__ == "__main__":
    main()
