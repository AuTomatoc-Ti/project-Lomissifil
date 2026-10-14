#!/usr/bin/env python3
"""The M3a SEAM sheet: root-final f/w/h + a suffix, written out to be READ ALOUD.

Why: the seam is the one layer left unjudged (03-open-questions.md section 0 item 20), it fires for
**3 of every 4** coined roots, and it lands **unstressed** -- exactly where sung intelligibility dies
(section F). The synthesiser was rejected (item 19), so the author's ruling 2026-10-14 is that the
test method is **reading the written forms aloud**. This tool produces exactly that material.

M3a (locked). A root ending in f / w / h meets a suffix whose onset is m n l r s:
    tier 1  the pair is one of the legal VCV clusters fm fn hm hn wm wn jm jn -> NOTHING changes,
            the two consonants simply become one onset of the next syllable (`lafif` + `-na` ->
            la-fi-fna)
    tier 2  otherwise SYNC (the root-final consonant disappears into a geminate / single)
            {f,w}+s -> ss · {f,w}+r -> rr · {f,w}+l -> ll · h+s -> s · h+r -> r · h+l -> l
            (`lafif`+`-sa` -> lafissa · `lafih`+`-le` -> lafile)
    tier 3  anything else would insert a vowel copied from the root's last nucleus -- this tool
            REPORTS when tier 3 fires, and with the current M3b suffix set it never does (all 9
            suffixes start with m n l r s, and tiers 1-2 cover all 15 combinations).
The tool also prints, for every pair of siblings, whether their suffixed forms stay distinct: the
coining rule "**exactly 2 roots per base, one per branch**" is what keeps them apart, so violating
the at-most-two rule of `lists/picks.md` would create homophones in GEN/INS/V1/OBL.

Reading a row: `syllables` uses `-` between syllables; the CAPITAL sits on the first letter of the
stressed syllable, and the stress is counted **from the ROOT** (P4c: affixes never move it) -- which
is why a one-syllable root keeps its stress on its own syllable while a two-syllable root stresses
its second.

USAGE
    python3 tools/seam.py > lists/seam-sheet.md
    python3 tools/seam.py --bases 12 --seed 7
"""

import argparse
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import syllabify as S                      # noqa: E402

# M4a (nouns) + the two verb classes. NOM is the zero suffix.
SUFFIXES = [("NOM", "zero", ""), ("ACC", "dominant", "na"), ("GEN", "dominant", "sa"),
            ("DAT", "subdominant", "me"), ("LOC", "subdominant", "ner"),
            ("INS", "subdominant", "ser"), ("OBL", "subdominant", "le"),
            ("V1", "tonic", "ri"), ("V2", "tonic", "ni")]
FINALS = ("f", "w", "h", "s", "m", "r")    # R4 added `s`; R6 added `m` and `r` -- all are codas,
                                           # so none of them needs an M3a repair
TIER1_ONSETS = ("m", "n")                  # + f/w/h = fm fn hm hn wm wn (the VCV-only clusters)
TIER2 = {("f", "s"): "ss", ("w", "s"): "ss", ("h", "s"): "s",
         ("f", "r"): "rr", ("w", "r"): "rr", ("h", "r"): "r",
         ("f", "l"): "ll", ("w", "l"): "ll", ("h", "l"): "l"}


def last_nucleus(word):
    toks = S.tokenize(word) or []
    nucs = [t[1] for t in toks if t[0] == "V"]
    return nucs[-1] if nucs else "a"


def seam(root, suf):
    """-> (spelling, tier, note). `suf` is the suffix body without the dash (`na`, `ner`, ...)."""
    if not suf:
        return root, 0, "NOM = zero suffix"
    fin = root[-1]
    if fin not in FINALS:
        return root + suf, 0, "vowel-final root: nothing to repair"
    onset = suf[0]
    if onset in TIER1_ONSETS:
        return root + suf, 1, "tier 1: `%s%s` is a legal VCV cluster" % (fin, onset)
    if (fin, onset) in TIER2:
        rep = TIER2[(fin, onset)]
        return root[:-1] + rep + suf[1:], 2, "tier 2 sync: %s+%s -> %s" % (fin, onset, rep)
    v = last_nucleus(root)
    return root + v + suf, 3, "tier 3: copied vowel `%s` inserted" % v


def stress_index(root):
    """P4c: the stress is the 2nd syllable OF THE ROOT (1st if the root is one syllable)."""
    syl = S.parse(root)
    return 1 if syl and len(syl) >= 2 else 0


def mark(form, root):
    an = S.analyse(form)
    if not an["syllables"]:
        return None
    syls = list(an["syllables"])
    i = min(stress_index(root), len(syls) - 1)
    syls[i] = syls[i][0].upper() + syls[i][1:]
    return syls, "-".join(an["syllables"]), "".join(syls)


HEADER = """\
# lists/seam-sheet.md - GENERATED: the M3a seam, written out to be READ ALOUD.

Regenerate with:

```
python3 tools/seam.py > lists/seam-sheet.md
```

**No annotations here** (they are lost on regeneration). Notes and verdicts belong in `picks.md` or in
the decision log.

## Why this sheet exists

- the **M3a seam** (a root ending in `f`/`w`/`h` meeting a suffix) fires for **3 of every 4** coined
  roots;
- it lands **unstressed** -- the place where sung intelligibility dies first
  (`../decision/03-open-questions.md` section F);
- it has **never been judged by ear**, and the synthesiser was rejected (section 0 item 19), so the
  author's method (2026-10-14) is: **read the written forms aloud**.

## What M3a does (locked)

| tier | when | what happens | example |
|---|---|---|---|
| **1** | the suffix starts with `m` / `n` | nothing changes: the two consonants become the **onset** of the next syllable (a legal VCV cluster `fm fn hm hn wm wn`) | `lafif` + `-na` -> `la-fi-fna` |
| **2** | otherwise (`l` / `r` / `s`) | **sync**: the final disappears into a geminate / single | `lafif`+`-sa` -> `lafissa` · `lafih`+`-le` -> `lafile` |
| **3** | anything else | insert a vowel copied from the root's last nucleus -- **reported below if it ever fires** | (dormant for all 9 current suffixes) |

## What to listen for while reading aloud

1. **tier 1** (`la-fi-fna`): does it still sound like the same root, or does the final feel *eaten*?
2. **tier 2** (`lafissa`, `larri`, `lalle`, `lasa`): the root's final **vanishes**. Is the root still
   recognisable after `-sa` / `-ser` / `-ri` / `-le`?
3. **the unstressed tail**: the case vowel is never stressed (P4c). Can you still hear
   `-na` vs `-sa` vs `-me` vs `-ner`?
4. **the class siblings side by side** (the `+f`/`+w` row vs the `+h`/bare row): do they stay apart,
   or do they blur into each other?

## Reading a row

`syllables` uses `-` between syllables; the CAPITAL sits on the first letter of the stressed
syllable, counted **from the ROOT** (P4c: affixes never move the stress). The `seam` column names the
tier. Sound values: `a` dark *father* · `ae` bright *cat* · `e`/`o` close-mid · `i` `u` `y` as usual
(`y` = French *u*) · `w` = /v/ · `sh` = *ship* · `th` = *thin* · `c` = *church* · `j` = *yes* ·
doubled letters = long · a diphthong is ONE syllable, a hiatus (`iu yu ia ya`) is TWO.

> ⚠️ **The "at most 2 roots per base" rule of `picks.md` is a CORRECTNESS rule, not a nicety.**
> Within one branch you may pick either `+f` **or** `+w` (and either `+h`, `+s` **or** bare) -- never
> both. (`+s` is new in **R4**: `s` is RESERVED for a future adjective/adverb/exceptional-case job, so a
> `+s` root is ordinary in sound but its meaning slot is held.)
> The last section of this file shows, for every base on the sheet, exactly which case forms would
> collide. Sound-only: assign **no meanings** (R3 parked).

---
"""

FOOTER = """
---

## What this sheet does NOT cover

- **suffix chains** (suffix + suffix): M3b guarantees the result is a legal medial `CC`, but nobody
  has read one aloud yet;
- **compounds** (M7): compound stress is PROVISIONAL (P4d) and untested;
- **1-syllable roots**: the pool is the 2-syllable core (section 0 item 22), so no `roi`-class root is
  shown -- the stress code handles them if such roots are added;
- **meanings**: none exist yet, so nothing here is a word.
"""


def distinctness(roots):
    """For each pair of the 4 raw roots of one base, name the suffixes where the forms collide."""
    joined = {}
    for r in roots:
        joined[r] = {}
        for name, grade, body in SUFFIXES:
            joined[r][name] = seam(r, body)[0]
    out = []
    for i in range(len(roots)):
        for j in range(i + 1, len(roots)):
            clash = [name for name, _, _ in SUFFIXES
                     if joined[roots[i]][name] == joined[roots[j]][name]]
            out.append((roots[i], roots[j], clash))
    return out


def sheet(src, n_bases, seed):
    bases = [ln.strip() for ln in open(src, encoding="utf-8")
             if ln.strip() and not ln.startswith("#")]
    samp = random.Random(seed).sample(bases, min(n_bases, len(bases)))
    out = [HEADER]
    tier3 = []
    for b in samp:
        roots = [b + f for f in FINALS] + [b]
        out.append("## base `%s`\n\n" % b)
        out.append("| root | suffix | form | syllables | stress | seam |\n"
                   "|---|---|---|---|---|---|\n")
        for r in roots:
            for name, grade, body in SUFFIXES:
                form, tier, note = seam(r, body)
                mk = mark(form, r)
                if tier == 3:
                    tier3.append((b, r, name, form))
                if mk is None:
                    out.append("| `%s` | %s `-%s` | `%s` | **UNREADABLE** | - | %s |\n"
                               % (r, name, body, form, note))
                    continue
                _, syl, st = mk
                out.append("| `%s` | %s `-%s` (%s) | `%s` | %s | %s | %s |\n"
                           % (r, name, body, grade, form, syl, st, note))
        out.append("\n")
    out.append("## Do the siblings stay distinct? (why the `<=2 per base` rule is correctness)\n\n")
    for b in samp:
        roots = [b + f for f in FINALS] + [b]
        out.append("**base `%s`**\n\n" % b)
        for r1, r2, clash in distinctness(roots):
            if clash:
                out.append("- `%s` vs `%s` -> **COLLIDE in %s** (e.g. both become `%s`)\n"
                           % (r1, r2, ", ".join(clash), seam(r1, "sa")[0]))
            else:
                out.append("- `%s` vs `%s` -> distinct in all 9 forms\n" % (r1, r2))
        out.append("\n")
    if tier3:
        out.append("**tier 3 (copied vowel) fired %d time(s):** %s\n\n"
                   % (len(tier3), ", ".join("%s+%s" % (r, n) for _, r, n, _ in tier3[:8])))
    else:
        out.append("**tier 3 (copied vowel) never fired** -- M3a is fully determined by tiers 1-2 for "
                   "the current suffix set (all 9 start with `m n l r s`).\n\n")
    out.append(FOOTER)
    sys.stdout.write("".join(out))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default="lists/roots-bases-current.txt")
    ap.add_argument("--bases", type=int, default=6, help="bases to write out (4 roots each)")
    ap.add_argument("--seed", type=int, default=20261014)
    a = ap.parse_args()
    sheet(a.src, a.bases, a.seed)


if __name__ == "__main__":
    main()


