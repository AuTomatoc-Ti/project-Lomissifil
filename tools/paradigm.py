#!/usr/bin/env python3
"""Verb-paradigm sheet: FINITE x ASPECT x EVIDENTIAL, written out to be READ ALOUD.

The verb morphology as of 2026-10-15 -- `M4a` (finite endings) + `M4c` (4 aspects, carried by the
finite syllable's CODA) + `M5f` (4 evidentials, an OUTER syllable ending in the one licensed stop) --
written for one REAL lexicon root per trigger class, so the grade vowels can be read and compared.

Structure (locked):
    root + (r|n) + V(aspect grade) + aspect coda(empty|s|m) + evidential(onset + SUBDOMINANT V + stop)
  * no aspect        -> the vowel is the FINITE grade (tonic)
  * PROGRESSIVE (I)  -> coda `s` + DOMINANT      * PERFECT (II) -> coda `m` + TONIC
  * III              -> coda `m` + DOMINANT
  * evidential       -> `witnessed -seg/-sog` / `inferred -med/-mod` / `surmised -neg/-nog` /
                        `reported -leb/-lob` (the value differs in ONSET and in CODA; the vowel is the
                        class SUBDOMINANT = chord IV BY DEFAULT, and HARMONISES to dominant when the
                        preceding aspect is dominant -- `M5f`, amended 2026-10-15)
  * `V0` (a bare root) takes an EVIDENTIAL but NO aspect (the aspect requires the finite ending).

Every surface is built from `grades.py`'s GRADE table (one source of truth) and checked with
`syllabify.analyse` -- the sheet ends by reporting how many forms there are and whether any is illegal.

USAGE
    python3 tools/paradigm.py                     # the sheet on stdout
    python3 tools/paradigm.py > data/generated/verb-paradigm.md
    python3 tools/paradigm.py --check             # verify only: count + list any illegal form
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import syllabify as S        # noqa: E402
import seam as SEAM          # noqa: E402
import grades as G           # noqa: E402

# one real lexicon root per trigger class (the 6th class, `ae`, has no root yet -- reported below)
ROOTS = [("a", "thyma", "think, class I"), ("e", "res", "be, class II"),
         ("i,y", "seli", "birth, class D"), ("o", "os", "have, class I"),
         ("u", "hu", "wind, class II*")]
ASPECTS = [("simple", "", "tonic"), ("progressive", "s", "dom"),
           ("perfect", "m", "tonic"), ("III", "m", "dom")]
EVIDENTIALS = [("witnessed", "s", "g"), ("inferred", "m", "d"),
               ("surmised", "n", "g"), ("reported", "l", "b")]
FINITE = [("V0", ""), ("V1", "r"), ("V2", "n")]


PINS = [   # known values, pinned so a refactor cannot silently change the morphology
    ("thyma", "V1", "simple", None, "thymara"),
    ("thyma", "V1", "progressive", "witnessed", "thymarissig"),      # harmonised (dominant asks dom)
    ("thyma", "V1", "perfect", "witnessed", "thymaramsog"),          # IV (subdominant) default
    ("thyma", "V0", "simple", "reported", "thymalob"),               # the evidential on a bare root
    ("res", "V2", "perfect", "surmised", "resnemneg"),
    ("res", "V1", "progressive", "witnessed", "resrassag"),          # e-class dominant = `a`
    ("seli", "V2", "III", "inferred", "selinammad"),
]
MOOD_PINS = [   # M5g: the imperative is the outermost syllable, always dominant, `-lVn`
    ("thyma", "V1", "simple", "imperative", "thymaralin"),
    ("thyma", "V0", "simple", "imperative", "thymalin"),
    ("res", "V1", "simple", "imperative", "resrelan"),
    ("res", "V2", "progressive", "imperative", "resnaslan"),
    ("os", "V1", "simple", "imperative", "osrolin"),
]


def check_tables():
    """The display rows below must agree with the single source of truth in `grades.py` (M4c / M5f /
    M5g), and a few known forms are PINNED (a refactor that changes them fails loudly)."""
    assert set(a[0] for a in ASPECTS) == set(G.ASPECT), "paradigm.ASPECTS drifted from grades.ASPECT"
    assert set(e[0] for e in EVIDENTIALS) == set(G.EVIDENTIAL), "EVIDENTIALS drifted from grades"
    assert set(G.MOOD) == {"imperative"}, "grades.MOOD changed shape (M5g)"
    bad = ["%s+%s+%s got %s" % (r, f, a, G.verb(r, f, a, e)[0]) for r, f, a, e, want in PINS
           if G.verb(r, f, a, e)[0] != want]
    bad += ["%s+%s+%s+mood got %s" % (r, f, a, G.verb(r, f, a, None, m)[0])
            for r, f, a, m, want in MOOD_PINS if G.verb(r, f, a, None, m)[0] != want]
    assert not bad, "pinned verb forms changed: %s" % bad


def surface(root, cons, aspect, evid, mood=None):
    """Thin wrapper over the ONE implementation, `grades.verb()` (M4a finite + M4c aspect + M5f evid +
    M5g mood). The grade vowel, the harmony, the exclusivity and the seam all live there."""
    return G.verb(root, {v: k for k, v in G.FINITE_CONSONANT.items()}[cons],
                  aspect[0] if aspect else "simple", evid[0] if evid else None, mood)[0]


def rows_for(root):
    """-> [(environment label, {None: form, evidential-name: form, mood-name: form}), ...]."""
    check_tables()
    out = []
    for vname, cons in FINITE:
        if not cons:                        # V0: the bare root, plus evidentials OR a mood (M5f/M5g)
            row = {None: surface(root, "", None, None)}
            for e in EVIDENTIALS:
                row[e[0]] = surface(root, "", None, e)
            for m in G.MOOD:
                row[m] = surface(root, "", None, None, m)
            out.append(("V0 (bare root)", row))
            continue
        for aname, coda, grade in ASPECTS:
            asp = None if aname == "simple" else (aname, coda, grade)
            row = {None: surface(root, cons, asp, None)}
            for e in EVIDENTIALS:
                row[e[0]] = surface(root, cons, asp, e)
            for m in G.MOOD:
                row[m] = surface(root, cons, asp, None, m)
            out.append(("%s + %s" % (vname, aname), row))
    return out


def build(check_only=False):
    lines = ["# data/generated/verb-paradigm.md - GENERATED: the verb paradigm, to be READ ALOUD",
             "",
             "Regenerate with `python3 tools/paradigm.py > data/generated/verb-paradigm.md`.",
             "**No annotations here** (they are lost on regeneration) - notes belong in `../hand/`.",
             "",
             "`root + (r|n) + V(aspect grade) + aspect coda(empty|s|m) + evidential(onset + sub + stop)`.",
             "Aspect: simple (no coda, tonic) - progressive (`s`, dominant) - perfect (`m`, tonic) -",
             "III (`m`, dominant). Evidential: witnessed `-sVg` - inferred `-mVd` - surmised `-nVg` -",
             "reported `-lVb`, where `V` is the class SUBDOMINANT (front `e` / back `o`) = chord IV.",
             "`V0` takes an evidential but no aspect (the aspect requires the finite ending).",
             "**Mood (`M5g`): the imperative is an outer syllable, always DOMINANT = chord V**, and it is",
             "**mutually exclusive with an evidential** (a command is not reported); `V0` may carry it too.",
             ""]
    cols = [None] + [e[0] for e in EVIDENTIALS] + list(G.MOOD)
    total, illegal = 0, []
    for cls, root, gloss in ROOTS:
        lines.append("## `%s` (`%s`; %s) - tonic `%s` / sub `%s` / dom `%s`"
                     % (root, cls, gloss, *G.GRADE[cls]))
        lines.append("")
        lines.append("| environment | " + " | ".join(c or "(no evidential)" for c in cols) + " |")
        lines.append("|" + "---|" * (len(cols) + 1))
        for label, row in rows_for(root):
            cells = []
            for c in cols:
                f = row[c]
                total += 1
                if S.analyse(f)["illegal"]:
                    illegal.append(f)
                    cells.append("**ILLEGAL** `%s`" % f)
                else:
                    cells.append("`%s`" % f)
            lines.append("| %s | %s |" % (label, " | ".join(cells)))
        lines.append("")
    if not check_only:
        print("\n".join(lines))
    print("## summary")
    print("")
    print("- roots: %d, one per trigger class (**`ae` has no lexicon root yet**, so it is not shown)"
          % len(ROOTS))
    print("- forms: **%d** (5 roots x {V0, V1, V2} x {no aspect, 3 aspects} x "
          "({no evidential} + 4 evidentials + the imperative, which excludes the evidentials))" % total)
    print("- illegal: **%d**%s" % (len(illegal), (" -> " + ", ".join(illegal)) if illegal else ""))
    return 1 if illegal else 0


def main(argv=None):
    args = sys.argv[1:] if argv is None else argv
    return build(check_only="--check" in args)


if __name__ == "__main__":
    sys.exit(main())
