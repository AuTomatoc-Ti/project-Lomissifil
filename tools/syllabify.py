#!/usr/bin/env python3
"""Syllabify spelled forms + mark the DEFAULT stress (P4/N1). Read-only helper.

WHY THIS EXISTS
    The synthesiser is rejected (decision/03-open-questions.md section F item 19), so the
    audition signal is now the WRITTEN form. Judging a written form needs its syllable
    boundaries and its stress position, which the raw index (audio/roots-index.txt) does not
    show -- reading it off by eye is exactly where a wrong judgement comes from.

RULES IMPLEMENTED (all already locked; nothing new is invented here)
    shape      (C)V(C)
    onsets     1 consonant | pr br tr dr kr gr (any position)
               | fm fn hm hn wm wn jm jn (VCV only: never word-initial, and only after an
                 OPEN syllable)
    codas      m n l r s; word-final also f / w / h (the area rule)
    nuclei     a e o i u y | ae | diphthongs ai au ei eu oi ou aei aeu (ONE syllable)
               | hiatus iu yu ia ya (TWO syllables)
    stress     P4: 2nd syllable of the root; a 1-syllable root carries it on itself
    mark       N1: CAPITAL on the FIRST letter of the stressed syllable
    split      maximal onset (the longest legal onset wins). It reproduces every split the
               docs state: se-li, los-do, ar-gon-na, aus-ta-reus.
    Anything that does not split legally is reported as an ERROR / 'illegal' -- the inputs are
    supposed to be legal, so a failure means a bug HERE, not a bad word (fail loud).

READING (P6, author's ruling 2026-10-14)
    Medial `sh` and `ng` are ALWAYS ONE phoneme: /S/ and /N/. The sequence **coda `n` + onset
    /g/** is written **`nk`** (the hard letter). That `k` is not free texture: `/g/` after a coda
    `n` is **obligatorily [k]** (P6, the language's first conditioned process), so the soft/hard
    knob does not apply there. `nk` is NOT a cluster: coda `n` + onset `k`, read exactly as P5
    reads `st`. Because the coda+onset reading of `sh` is gone, **/s/ + /h/ has no spelling
    at all** and is illegal by ruling. (`th` was never ambiguous -- a coda can never be `t`;
    `ae` is not either -- adjacent nuclei are illegal.)

USAGE
    python3 tools/syllabify.py --check                  # verify against the reference words
    python3 tools/syllabify.py --sheet > lists/picks-sheet.md
"""

import argparse
import random
import sys

VOWELS = set("aeiouy")
CONSONANTS = set("bcdfghjklmnpqrstvwxyz")
# longest match first: aei/aeu before ae, and every 2-char nucleus before the bare vowel
NUCLEI = ("aei", "aeu", "ai", "au", "ei", "eu", "oi", "ou",
          "iu", "yu", "ia", "ya",
          "ae", "a", "e", "o", "i", "u", "y")
HIATUS = {"iu", "yu", "ia", "ya"}
CONS_DIGRAPHS = ("sh", "th", "ng")
ONSET1 = {"b", "d", "g", "p", "t", "k", "m", "n", "l", "r", "f", "w", "s", "h", "c", "j",
          "sh", "th", "ng"}
ONSET_CLUSTER = {"pr", "br", "tr", "dr", "kr", "gr"}
ONSET_VCV = {"fm", "fn", "hm", "hn", "wm", "wn", "jm", "jn"}
CODA = set("mnlrs")
WORD_FINAL = CODA | {"f", "w", "h"}


def tokenize(word):
    """-> [('C', text) | ('V', text)] or None if some letter sequence is not readable.

    `sh` / `th` / `ng` are read as ONE consonant (P6): a digraph, never C + C.
    """
    toks, i = [], 0
    while i < len(word):
        hit = None
        for d in CONS_DIGRAPHS:
            if word.startswith(d, i):
                hit = d
                break
        if hit:
            toks.append(("C", hit))
            i += len(hit)
            continue
        ch = word[i]
        if ch in VOWELS:
            hit = None
            for n in NUCLEI:
                if word.startswith(n, i):
                    hit = n
                    break
            if hit is None:
                return None
            toks.append(("V", hit))
            i += len(hit)
            continue
        if ch in CONSONANTS:
            toks.append(("C", ch))
            i += 1
            continue
        return None
    return toks


def is_onset(toks, after_open):
    if len(toks) == 1:
        return toks[0] in ONSET1
    if len(toks) == 2:
        j = "".join(toks)
        if j in ONSET_CLUSTER:
            return True
        return j in ONSET_VCV and after_open
    return False


def split_run(run):
    """(coda, onset) for the consonant run between two nuclei; maximal onset wins."""
    best = None
    for k in range(len(run) + 1):
        coda, onset = run[:k], run[k:]
        if any(c not in CODA for c in coda):
            continue
        if onset and not is_onset(onset, after_open=(k == 0)):
            continue
        if best is None or len(onset) > len(best[1]):
            best = (coda, onset)
    return best


def parse(word):
    """-> list of syllables, or None when the form does not split legally."""
    toks = tokenize(word)
    if toks is None:
        return None
    i = 0
    initial = []
    while i < len(toks) and toks[i][0] == "C":
        initial.append(toks[i][1])
        i += 1
    if i == len(toks):
        return None                                  # no nucleus at all
    if initial and not is_onset(initial, after_open=False):
        return None                                  # illegal word-initial onset
    groups = []                                      # [(nucleus, consonant run after it)]
    while i < len(toks):
        if toks[i][0] != "V":
            return None
        nuc = toks[i][1]
        i += 1
        run = []
        while i < len(toks) and toks[i][0] == "C":
            run.append(toks[i][1])
            i += 1
        if nuc in HIATUS:                            # a hiatus is TWO syllables, no C between
            groups.append((nuc[0], []))
            groups.append((nuc[1], run))
        else:
            groups.append((nuc, run))
    fin = groups[-1][1]                              # the word-final coda
    if fin and (len(fin) != 1 or fin[0] not in WORD_FINAL):
        return None
    sylls = ["".join(initial) + groups[0][0]]
    for gi in range(1, len(groups)):
        sp = split_run(groups[gi - 1][1])
        if sp is None:
            return None
        coda, onset = sp
        sylls[-1] += "".join(coda)
        sylls.append("".join(onset) + groups[gi][0])
    sylls[-1] += "".join(fin)
    if "".join(sylls) != word:                       # fail loud: the split must rebuild the word
        return None
    return sylls


def analyse(word):
    """-> dict(syllables, stressed, stress_syllable, p6, illegal).

    `p6` marks the P6 sequence `nk` (= coda `n` + the /g/ phoneme). Worth showing on a sheet:
    that `k` is a spelling rule, not the performance voicing knob.
    """
    sylls = parse(word)
    if sylls is None:
        return {"syllables": None, "stressed": None, "stress_syllable": None,
                "p6": False, "illegal": True}
    si = 0 if len(sylls) == 1 else 1                 # P4: 2nd syllable of the root
    out = list(sylls)
    out[si] = out[si][0].upper() + out[si][1:]       # N1: capital on the syllable's 1st letter
    return {"syllables": sylls, "stressed": "".join(out), "stress_syllable": si,
            "p6": "nk" in word, "illegal": False}


def note_for(an):
    notes = []
    if an["syllables"] and an["syllables"][an["stress_syllable"]].startswith(
            ("sh", "th", "ng", "ae")):
        notes.append("stress capital lands on a DIGRAPH (convention OPEN: 03 section C)")
    if an["p6"]:
        notes.append("`nk` = coda n + /g/, obligatorily [k] (P6: the soft/hard knob does not apply here)")
    return "; ".join(notes)


REFERENCE = [                                        # every split the docs state explicitly
    ("seli", "se-li"),                               # 02-notation.md worked example
    ("losdo", "los-do"),                             # P5
    ("roi", "roi"),                                  # R1: 1 syllable, a diphthong
    ("argonna", "ar-gon-na"),                        # 02-notation.md worked example
    ("austareus", "aus-ta-reus"),                    # 03-open-questions.md section C
]
REFERENCE_NO_EXPECTATION = ["aurorius"]              # a name; no split is documented
PROBES = ["shia", "nga", "songa", "thas", "iufa", "pra", "afmara", "asma", "fmara",
          "manka", "asha", "sangka"]


def check():
    bad = 0
    for word, exp in REFERENCE:
        an = analyse(word)
        got = "-".join(an["syllables"]) if an["syllables"] else "ILLEGAL"
        ok = got == exp
        bad += 0 if ok else 1
        print("%-4s %-12s got %-14s expected %-14s %s"
              % ("PASS" if ok else "FAIL", word, got, exp, note_for(an)))
    for word in REFERENCE_NO_EXPECTATION:
        an = analyse(word)
        got = "-".join(an["syllables"]) if an["syllables"] else "ILLEGAL"
        print("%-4s %-12s got %-14s (no documented expectation) %s"
              % ("----", word, got, note_for(an)))
    for word in PROBES:                              # edge cases, eyeball these
        an = analyse(word)
        got = "-".join(an["syllables"]) if an["syllables"] else "ILLEGAL"
        print("%-4s %-12s got %-14s probe %s" % ("----", word, got, note_for(an)))
    print()
    print("FAILURES: %d" % bad)
    return 1 if bad else 0


SHEET_HEADER = """\
# lists/picks-sheet.md - GENERATED audition sheet. DO NOT ANNOTATE HERE.

Regenerate with:

```
python3 tools/syllabify.py --sheet > lists/picks-sheet.md
```

Any annotation written in this file is **lost** on regeneration. **Picks go in `lists/picks.md`.**
The row numbers are the same as `../audio/roots-index.txt` (same seed, same sample), so a pick can
be recorded as a number in either file.

## How to read a row

| column | meaning |
|---|---|
| `form` | the citation form, plain lowercase (P4: the dictionary form is unstressed) |
| `syllables` | the syllable split, `-` between syllables |
| `stress` | where the **default** stress falls (P4/N1): 2nd syllable of the root, CAPITAL on the first letter of that syllable |

Reading it aloud needs no engine and no IPA - only these letter values:

`a` = the dark open vowel of *father* · `ae` = the bright vowel of *cat* · `e` = close-mid front ·
`o` = close-mid back · `i` = /i/ · `u` = /u/ · `y` = French *u* / German *ue* ·
`w` = /v/ · `sh` = the *sh* of *ship* · `th` = the *th* of *thin* · `c` = the *ch* of *church* ·
`j` = the *y* of *yes* · `r` = a single tap · a doubled letter (`ss nn ll mm rr ww`) = a long sound ·
a diphthong (`ai au ei eu oi ou aei aeu`) is ONE syllable, a hiatus (`iu yu ia ya`) is TWO.

## Rules for the pick (R1/R3)

Every group of 4 rows is ONE base: `+f` | `+w` (= /v/) | `+h` | bare. A base yields **exactly 2**
roots, so pick **at most one** from the `{+f, +w}` pair and **at most one** from the
`{+h, bare}` pair.

> Sound-only. R3 is PARKED, so assign **no meanings** (decision/03-open-questions.md section 0
> item 14). A pick is not a word; `../reference/example.md` stays the only source for examples.

## Reading rule (P6) - and the one flag left

**`sh` and `ng` are ALWAYS one phoneme** (`sh` = the *sh* of *ship*, `ng` = the *ng* of *sing*) - that
is `P6`, ruled 2026-10-14. So a row containing `ng` never means "n then g": the sequence **coda `n` +
/g/** is written **`nk`** instead, and nothing below needs a guess.

The one flag left is **`stress capital lands on a DIGRAPH`**: the stressed syllable starts with
`sh` / `th` / `ng` / `ae` - one sound written with two letters - and N1 has no rule for that case yet
(it is an open item). The `stress` column capitalises the first letter; treat it as provisional.

Also: `stress` is only the DEFAULT (P4). A composer may overwrite it in notation - that is
performance, not a different word.

---

"""

SHEET_FOOTER = """
---

## What this sheet does NOT do

- It does not cover the **M3a seam** (a root-final `f` / `w` / `h` in front of a case suffix,
  always unstressed) - that layer is unjudged, see `../decision/03-open-questions.md` section 0
  item 20.
- It cannot show the **/n/ + /g/ (`nk`) class** of candidates: the pool was packed before `P6`
  existed and contains no `nk` spelling at all (`03-open-questions.md` section 0 item 24).
- It does not say which form is a good word. That is the pick, and it is yours to make.
"""


def stats(src):
    """Histogram over a whole list: syllable counts + the two flags. Read-only."""
    with open(src, encoding="utf-8") as fh:
        words = [ln.strip() for ln in fh if ln.strip() and not ln.startswith("#")]
    hist, illegal, dig, nk, reads = {}, 0, 0, 0, 0
    for w in words:
        an = analyse(w)
        if an["illegal"]:
            illegal += 1
            continue
        k = len(an["syllables"])
        hist[k] = hist.get(k, 0) + 1
        if an["syllables"][an["stress_syllable"]].startswith(("sh", "th", "ng", "ae")):
            dig += 1
        if an["p6"]:
            nk += 1
        if "sh" in w[1:] or "ng" in w[1:]:
            reads += 1
    n = float(len(words)) or 1.0
    print("forms: %d   (%s)" % (len(words), src))
    for k in sorted(hist):
        print("  %d syllable(s) %8d  %5.1f%%" % (k, hist[k], 100.0 * hist[k] / n))
    print("  illegal                            %8d" % illegal)
    print("  stress on a digraph                %8d  %5.1f%%" % (dig, 100.0 * dig / n))
    print("  reads as ONE phoneme (sh/ng, P6)   %8d  %5.1f%%" % (reads, 100.0 * reads / n))
    print("  `nk` spellings (coda n + /g/, P6)  %8d  %5.1f%%   <- 0 = pool predates P6 (03 item 24)"
          % (nk, 100.0 * nk / n))
    return 1 if illegal else 0


def sheet(src, bases_n, per_file, seed):
    with open(src, encoding="utf-8") as fh:
        all_bases = [ln.strip() for ln in fh if ln.strip() and not ln.startswith("#")]
    bases = random.Random(seed).sample(all_bases, min(bases_n, len(all_bases)))
    out = [SHEET_HEADER]
    out.append("Source: `%s` (%d packed bases); sample %d bases, seed %d - the SAME sample as\n"
               "`../audio/roots-index.txt`.\n\n" % (src, len(all_bases), len(bases), seed))
    n = 0
    bad = 0
    for fi in range(0, len(bases), per_file):
        chunk = bases[fi:fi + per_file]
        first = n + 1
        out.append("## roots-%02d.wav  (numbered %d-%d)\n\n"
                   % (fi // per_file + 1, first, first + 4 * len(chunk) - 1))
        out.append("| # | base | form | syllables | stress (P4/N1) | note |\n"
                   "|---|---|---|---|---|---|\n")
        for b in chunk:
            for form in (b + "f", b + "w", b + "h", b):
                n += 1
                an = analyse(form)
                if an["illegal"]:
                    bad += 1
                    syll, st, note = "**ILLEGAL**", "-", "ERROR: does not split legally"
                else:
                    syll = "-".join(an["syllables"])
                    st = an["stressed"]
                    note = note_for(an)
                    if len(an["syllables"]) == 1:
                        note = (note + "; " if note else "") + "1 syllable (stress on itself)"
                out.append("| %d | %s | %s | %s | %s | %s |\n" % (n, b, form, syll, st, note))
        out.append("\n")
    out.append(SHEET_FOOTER)
    if bad:
        sys.stderr.write("WARNING: %d form(s) did not split legally - see ILLEGAL rows\n" % bad)
    return "".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true",
                    help="verify the splitter against the reference words and a few probes")
    ap.add_argument("--sheet", action="store_true", help="print the markdown audition sheet")
    ap.add_argument("--stats", action="store_true",
                    help="histogram the whole --src list (syllable counts + the two flags)")
    ap.add_argument("--src", default="lists/roots-bases-current.txt",
                    help="packed base list (the committed canonical one)")
    ap.add_argument("--bases", type=int, default=48, help="bases to sample (audition run: 48)")
    ap.add_argument("--per-file", type=int, default=8, help="bases per file section")
    ap.add_argument("--seed", type=int, default=20261014, help="must match audition_roots.py")
    a = ap.parse_args()
    if a.check:
        sys.exit(check())
    if a.sheet:
        sys.stdout.write(sheet(a.src, a.bases, a.per_file, a.seed))
        return
    if a.stats:
        sys.exit(stats(a.src))
    ap.print_help()


if __name__ == "__main__":
    main()
