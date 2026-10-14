#!/usr/bin/env python3
"""M1 direction smoke-test: SUFFIXES vs PREFIXES.

M1 (affix direction) is DECIDED but PROVISIONAL, and its reversal cost is the
highest in the project (draft/handoff.md; decision/03-open-questions.md section A).
Section A states that a direction smoke-test is possible *now* with
non-semantic sound-strings -- which 02-notation.md explicitly allows.

This script builds the SAME morpheme content twice, once AFTER the root and once
BEFORE it, so the author can hear the difference.  Morphemes = the M4a case table,
shaped by M3b (one syllable C V (C)), with the suffix vowel derived from the
root's last-syllable nucleus by H3/H4.

Nothing here is a sentence and no meaning is claimed.

Output: /tmp/lomissifil-audition/*.wav  (espeak-ng -v fi, the engine verified in
draft/handoff.md) + a printed listening guide.
"""

import os
import subprocess
import sys

OUT = "/tmp/lomissifil-audition"
ESPEAK = "espeak-ng"

VOWEL_CLASS = {"i": "front", "e": "front", "y": "front", "ae": "front",
               "a": "back", "o": "back", "u": "back"}
CENTRAL = {"front": "e", "back": "o"}
OPPOSITE_POLE = {"front": "a", "back": "i"}

# bare roots (reference/example.md) + their H4 trigger (last-syllable nucleus)
ROOTS = [
    ("seli",    "se-li",     "i", "birth"),
    ("losdo",   "los-do",    "o", "happy"),
    ("roi",     "roi",       "o", "day"),
    ("argonna", "ar-gon-na", "a", "love"),
]

# M4a case table -> (onset, coda, grade label)   I = tonic, IV = subdominant, V = dominant
CASES = [
    ("NOM", None, None, None),
    ("ACC", "n", None, "V"),
    ("GEN", "s", None, "V"),
    ("DAT", "m", None, "IV"),
    ("LOC", "n", "r", "IV"),
    ("INS", "s", "r", "IV"),
    ("OBL", "l", None, "IV"),
]


def grade_vowel(trigger, label):
    """H3: tonic = the same vowel, subdominant = the class's central vowel,
    dominant = the opposite pole."""
    cls = VOWEL_CLASS[trigger]
    if label == "I":
        return trigger
    if label == "IV":
        return CENTRAL[cls]
    return OPPOSITE_POLE[cls]


def morpheme(onset, coda, vowel):
    return "" if onset is None else onset + vowel + (coda or "")


def stressed(root, syll, pre="", suf=""):
    """P4/N1: stress on the 2nd syllable OF THE ROOT (mono root = on itself)."""
    parts = syll.split("-")
    idx = 1 if len(parts) > 1 else 0
    off = len("".join(parts[:idx]))
    word = pre + root + suf
    at = len(pre) + off
    return word[:at] + word[at].upper() + word[at + 1:]


def forms_for(root, syll, trig, pre=False):
    out = []
    for cname, onset, coda, label in CASES:
        if label is None:
            out.append((cname, stressed(root, syll)))
            continue
        v = grade_vowel(trig, label)
        m = morpheme(onset, coda, v)
        out.append((cname, stressed(root, syll, m, "") if pre else stressed(root, syll, "", m)))
    return out


def legal_adjacency(root, pre):
    """The prefix seam: a vowel-final prefix + a vowel-initial root breaks the
    'no adjacent vowels' phonotactic (01-phonology.md section 5)."""
    if not pre:
        return True
    return not (root[0] in "aeiouy" and pre[-1] in "aeiouy")


def say(fname, text):
    path = os.path.join(OUT, fname)
    subprocess.run([ESPEAK, "-v", "fi", "-s", "130", "-w", path, text], check=True)
    return path


def main():
    os.makedirs(OUT, exist_ok=True)
    print("espeak-ng:", subprocess.run([ESPEAK, "--version"], capture_output=True, text=True)
          .stdout.strip().splitlines()[0])
    print("out:", OUT)
    print()

    # --- derived suffix vowels (H3/H4) -------------------------------------
    print("derived suffix vowels per root (H3/H4):")
    print("  %-9s %-8s %-6s %-4s %-4s %-4s   %s"
          % ("root", "syll", "trig", "I", "IV", "V", "class"))
    for name, syll, trig, gloss in ROOTS:
        print("  %-9s %-8s %-6s %-4s %-4s %-4s   %s (%s)"
              % (name, syll, trig, grade_vowel(trig, "I"), grade_vowel(trig, "IV"),
                 grade_vowel(trig, "V"), VOWEL_CLASS[trig], gloss))
    print()

    # --- 01 suffix chain ---------------------------------------------------
    lines = []
    for name, syll, trig, gloss in ROOTS:
        fs = forms_for(name, syll, trig, pre=False)
        lines.append("%s: %s" % (gloss, "  ".join(w for _, w in fs)))
        print("  01 suffix  %-8s -> %s" % (name, " ".join(w for _, w in fs)))
    say("01-suffix-chain.wav", " , ".join(l.split(": ", 1)[1] for l in lines))
    print()

    # --- 02 prefix chain ---------------------------------------------------
    lines, bad = [], []
    for name, syll, trig, gloss in ROOTS:
        fs = forms_for(name, syll, trig, pre=True)
        ok = [w for _, w in fs if w == name or legal_adjacency(name, w[:len(w) - len(name)])]
        for _, w in fs:
            if w != name and not legal_adjacency(name, w[:len(w) - len(name)]):
                bad.append((name, w))
        lines.append("%s: %s" % (gloss, "  ".join(ok)))
        print("  02 prefix  %-8s -> %s" % (name, " ".join(ok)))
    say("02-prefix-chain.wav", " , ".join(l.split(": ", 1)[1] for l in lines))
    print("     illegal (vowel-final prefix + vowel-initial root):",
          ", ".join(w for _, w in bad))
    print()

    # --- 03 same content, both directions (A/B) ----------------------------
    name, syll, trig, gloss = ROOTS[0]
    ab = []
    for cname, onset, coda, label in CASES:
        if label is None:
            ab.append(stressed(name, syll))
            continue
        v = grade_vowel(trig, label)
        m = morpheme(onset, coda, v)
        ab.append(stressed(name, syll, "", m))
        ab.append(stressed(name, syll, m, ""))
    say("03-ab-both-ways-seli.wav", " , ".join(ab))
    print("  03 A/B (suffix then prefix, root = seli):")
    print("     " + "  ".join(ab))
    print()

    # --- 04 rhyme probe ----------------------------------------------------
    for want in ("ACC", "DAT"):
        words = []
        for name, syll, trig, gloss in ROOTS:
            for cname, w in forms_for(name, syll, trig, pre=False):
                if cname == want:
                    words.append(w)
        say("04-rhyme-%s.wav" % want.lower(), " , ".join(words))
        print("  04 rhyme  %s: %s" % (want, " ".join(words)))
    print("     (front-class roots end -na/-me, back-class roots -ni/-mo:")
    print("      same case -> same tail ONLY inside one root class)")
    print()

    # --- 05 the vowel-initial seam ----------------------------------------
    name, syll, trig, gloss = ROOTS[3]
    pref = [w for _, w in forms_for(name, syll, trig, pre=True) if w != name]
    suf = [w for _, w in forms_for(name, syll, trig, pre=False) if w != name]
    say("05-seam-vinitial.wav", " , ".join(pref + suf))
    print("  05 seam, root = argonna (vowel-initial):")
    print("     prefix (ILLEGAL vowel contact): %s" % " ".join(pref))
    print("     suffix (legal):                %s" % " ".join(suf))
    print()
    print("Listening guide: play 01 vs 02 for direction, 03 for a direct A/B,")
    print("04 for the rhyme consequence, 05 for the seam cost of prefixing.")


if __name__ == "__main__":
    main()
