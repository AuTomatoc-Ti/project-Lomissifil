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

**BUILT-IN SELF-TEST:** `python3 tools/check_roots.py --src ../reference/example.md` audits the real
lexicon, which is known-good by construction, so it must report **0 breaking A1 layer 1 and 0 breaking
R-b**; anything else is a bug in this checker (two such bugs were found this way on 2026-10-14: `t`
inside the fricative `th`, and the P6 hard spellings `mp np mt nt mk nk`).
"""

import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import syllabify as S                      # noqa: E402

FORM_RE = re.compile(r"^[a-z]{1,12}$")     # a hand-written file contains prose too: ignore it

VOWELS = set("aeiouy")
AREA_FINALS = ("f", "w", "h", "s", "m", "r")   # A1 layer 1 after R4 (`s`) and R6 (`m`, `r`)
PROPOSED_FINALS = ("n", "l")               # still illegal as bare-root finals: nothing has asked for
                                           # them, and R6's class map gives them no job yet
HARD = set("ptk")


def parse(path):
    """-> [(form, gloss, section)]. A hand-written file contains prose: only real word lines are
    taken, and the current `# section` is remembered so a *function word* can be judged by R5's
    rule instead of A1's bare-root rule."""
    out = []
    section = ""
    for ln in open(path, encoding="utf-8"):
        if ln[:1] in (" ", "\t"):
            continue                        # wrapped continuation lines are INDENTED; entries start
        s = ln.strip()                      # at column 0 (this is what keeps prose out)
        if not s:
            continue
        if s.startswith("#"):
            section = s.lstrip("# ").strip()
            continue
        if s.startswith("- "):
            s = s[2:].strip()
        if "," in s:
            form, gloss = s.split(",", 1)
            form, gloss = form.strip().lower(), gloss.strip()
            if FORM_RE.match(form):
                out.append((form, gloss, section))
                continue
            # a comma inside the GLOSS (`basdo (—; author wrote basto, voiced)`) must not eat the
            # line -- fall through to the token regex instead of dropping it
        m = re.match(r"^([a-z]{1,12})(.*)$", s)
        if not m:
            continue
        form, rest = m.group(1), m.group(2).strip()
        if rest == "" or rest.startswith(("(", "\u2014", "-")):   # `lafi (birth)` or a bare token
            out.append((form, rest, section))
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
    """Per-form verdicts + a summary. Function words (R5) are judged by A1's 'any word' layer."""
    stats = {"n": 0, "legal": 0, "a1": 0, "rb": 0, "en": 0, "s": 0}
    for form, gloss, section in forms:
        stats["n"] += 1
        is_func = "function word" in section.lower()
        is_name = "name" in section.lower()
        an = S.analyse(form)
        notes = []
        if not an["syllables"]:
            notes.append("**ILLEGAL spelling** (phonotactics)")
        last = form[-1]
        if is_name:
            notes.append("proper name (**C2 exemption**): the voicing knob does not apply, and a name "
                         "is a word, not a bare root -- so no A1 layer-1 constraint either")
        elif is_func:
            notes.append("function word (**R5**): it takes no suffixes, so the bare-root final rule "
                         "has no purpose for it -- A1's 'any word' layer applies")
        elif last in PROPOSED_FINALS:
            stats["a1"] += 1
            notes.append("**breaks A1 layer 1**: a bare root may not end in `%s` (allowed since R4: "
                         "a vowel, `f`, `w`, `h`, `s`) -- the DEFERRED part of the author's note 1 "
                         "(03-open-questions.md section 0 item 28)" % last)
        elif last not in VOWELS and last not in AREA_FINALS:
            stats["a1"] += 1
            notes.append("**breaks A1 layer 1**: ends in `%s`" % last)
        if last == "s":
            stats["s"] += 1
            notes.append("`s`-final: **R4 is USAGE-LIMITED** -- the branch is reserved, so an "
                         "`s`-final root should be a deliberate, rare pick")
        if last in ("m", "r"):
            toks = S.tokenize(form) or []
            nuces = [t[1] for t in toks if t[0] == "V"]
            ln = nuces[-1] if nuces else "?"
            if last == "m" and ln not in ("i", "e", "y"):
                notes.append("soft rule **R6**: `-m` is meant for roots whose last vowel is a "
                             "non-open FRONT vowel (i / e / y); this one ends in `%s`" % ln)
            if last == "r" and not is_func:
                notes.append("soft rule **R6**: `-r` is meant for FUNCTION WORDS; a content root in "
                             "`-r` is a deliberate, rare exception")
        # R-b: no hard stop letter (p t k) in a base form -- but `th` is the FRICATIVE /T/ (one
        # phoneme, not a stop), and a nasal+stop is P6's REQUIRED hard spelling (`nk` = coda n +
        # /g/). Both must be masked before scanning, or the check reports false positives.
        scan = form.replace("th", "@").replace("sh", "#")
        for p6 in ("mp", "np", "mt", "nt", "mk", "nk"):
            scan = scan.replace(p6, "@@")
        for ch in ("ptk" if not is_name else ""):
            if ch in scan:
                i = scan.index(ch)
                stats["rb"] += 1
                notes.append("**breaks R-b**: base forms are voiced -- write `%s`"
                             % (form[:i] + {"p": "b", "t": "d", "k": "g"}[ch] + form[i + 1:]))
                break
        if "ng" in form[1:]:
            notes.append("P6: `ng` reads as /N/ (ONE phoneme) -- if you meant n+g, spell it `nk`")
        if words is not None and form in words:
            stats["en"] += 1
            notes.append("**IS an English word** (-2 in the menu's ranking)")
        if not notes:
            stats["legal"] += 1
        syl = "-".join(an["syllables"]) if an["syllables"] else "-"
        st = an["stressed"] or "-"
        b = base_of(form)
        sibs = [b + f for f in AREA_FINALS] + [b]
        d1 = [p for p in pool if lev_at_most(form, p, 1)]
        print("### `%s`%s%s" % (form, ("  -- *%s*" % gloss) if gloss else "",
                                "   [function word]" if is_func else ""))
        print("  syllables %-14s stress %-14s   siblings: %s" % (syl, st, " ".join(sibs)))
        print("  in the pool right now: %s" % ("YES" if form in pool else "no"))
        print("  distance-1 neighbours in the pool: %d%s"
              % (len(d1), ("  e.g. " + " ".join(d1[:6])) if d1 else ""))
        print("  %s" % ("; ".join(notes) if notes else "passes every locked rule checked here"))
        print()
    n = float(stats["n"]) or 1.0
    print("# summary")
    print("  forms checked           : %d" % stats["n"])
    print("  clean (no note at all)  : %d (%.1f%%)" % (stats["legal"], 100.0 * stats["legal"] / n))
    print("  breaking A1 layer 1     : %d" % stats["a1"])
    print("  breaking R-b            : %d" % stats["rb"])
    print("  English-word collision  : %d   (soft warning)" % stats["en"])
    print("  s-final (R4, keep rare) : %d (%.1f%%)" % (stats["s"], 100.0 * stats["s"] / n))
    print("  NOTE on the stress column: it is the analyser's BARE-ROOT default. For a SUFFIXED form the")
    print("  stress must be counted from the ROOT (P4c), which `tools/seam.py` does correctly -- e.g. a")
    print("  1-syllable root keeps its own stress (`sym`+`-as` is `SYmas`, NOT `syMas`).")



def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default="lists/proposed.md")
    ap.add_argument("--pool", default="lists/roots-bases-current.txt")
    ap.add_argument("--forms", default=None, help="check these instead (comma separated)")
    a = ap.parse_args()
    if a.forms:
        forms = [(f.strip(), "", "ad-hoc") for f in a.forms.split(",") if f.strip()]
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
