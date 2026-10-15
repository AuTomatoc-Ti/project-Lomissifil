#!/usr/bin/env python3
"""Grade calculator: root + morpheme -> the correct SURFACE suffix + its chord.

Implements the locked rules:
  H3   grade vowel table (tonic / subdominant / dominant, per trigger class)
  H4   the trigger is the ROOT's LAST SYLLABLE nucleus (a diphthong triggers on its
       nucleus; `ae` is its own class)
  M4a  the skeleton table (onsets / optional codas)
  H9   a MODIFIER is IV-grade, and a modifier word is a HEAD-COLOURED ISLAND: every
       suffix in it (including a CASE suffix on a displaced modifier) takes its vowel
       class from the HEAD, not from the modifier's own root (author, 2026-10-14)
  H2   the chord is bound to the CATEGORY:
         NOM / V0 / V1 / V2  -> I      ACC / GEN -> V
         DAT / LOC / INS / OBL -> IV   MOD       -> IV

Usage:
  python3 tools/grades.py thyma V1                     -> thymara  (V1, I)
  python3 tools/grades.py sefmeh ACC                   -> sefmehna (ACC, V)
  python3 tools/grades.py hosda MOD --head=sefmeh      -> hosdahes (MOD, IV)
  python3 tools/grades.py hosda MOD,ACC --head=sefmeh  -> hosdahesna (MOD IV + ACC V)
  python3 tools/grades.py --selftest                   -> reproduce the known-good forms

Limits (honest): the script CONCATENATES; it does not implement M3a's seam spellings
(root-final f/v/h + l) or the M3b cluster whitelist, so a hand check is still needed
for consonant-final roots in the seam cases.
"""
import sys

# H3 (FINAL): trigger class -> (tonic, subdominant, dominant)
GRADE = {
    "i,y": ("i", "e", "a"),
    "e":   ("e", "e", "a"),
    "ae":  ("ae", "e", "a"),
    "u":   ("u", "o", "i"),
    "o":   ("o", "o", "i"),
    "a":   ("a", "o", "i"),
}
FRONT = set("iey")          # first element decides, except `ae`
VOWELS = "aeiouy"
DIPHTHONGS = ("ae", "ei", "ou", "ai", "au", "oi", "ui", "eu", "io", "ua")

SKEL = {
    "NOM": (None, None, ""),
    "V0":  (None, None, ""),
    "ACC": ("n", "dom", ""),
    "GEN": ("s", "dom", ""),
    "DAT": ("m", "sub", ""),
    "LOC": ("n", "sub", "r"),
    "INS": ("s", "sub", "r"),
    "OBL": ("l", "sub", "r"),
    "MOD": ("h", "sub", "s"),
    "V1":  ("r", "tonic", ""),
    "V2":  ("n", "tonic", ""),
}
CHORD = {"NOM": "I", "V0": "I", "V1": "I", "V2": "I",
         "ACC": "V", "GEN": "V", "MOD": "IV",
         "DAT": "IV", "LOC": "IV", "INS": "IV", "OBL": "IV"}


def last_nucleus(root):
    """The root's last syllable nucleus, as H4 defines it (grapheme level)."""
    r = root.lower()
    i = len(r) - 1
    while i >= 0 and r[i] not in VOWELS and r[i] != "y":
        i -= 1
    if i < 0:
        return None
    # a diphthong: look one letter further left
    if i > 0 and r[i - 1] + r[i] in DIPHTHONGS:
        return r[i - 1] + r[i]
    if i + 1 < len(r) and r[i] + r[i + 1] in DIPHTHONGS:
        return r[i] + r[i + 1]
    return r[i]


def trigger_class(root):
    n = last_nucleus(root)
    if n == "ae":
        return "ae"                      # its own class (H3)
    if n == "y" or (n and n[0] == "y"):
        return "i,y"
    if n in ("i", "e") or (n and n[0] in ("i", "e")):
        return "e" if n[0] == "e" else "i,y"
    if n in ("u", "o", "a"):
        return n
    if n and n[0] in ("u", "o", "a"):
        return n[0]
    return None


def suffix(morpheme, cls):
    onset, grade, coda = SKEL[morpheme]
    if onset is None:
        return ""
    tonic, sub, dom = GRADE[cls]
    v = {"tonic": tonic, "sub": sub, "dom": dom}[grade]
    return "-" + onset + v + coda


def build(root, morphemes, head=None):
    """Return (surface, [(morpheme, suffix, chord), ...])."""
    own_cls = trigger_class(root)
    mod_cls = trigger_class(head) if head else own_cls   # H9: head-coloured island
    out = root
    parts = []
    for m in morphemes:
        cls = mod_cls if head else own_cls
        sfx = suffix(m, cls)
        if m == "MOD" and root[-1] not in VOWELS:      # R6: only a vowel-final root keeps the h
            sfx = sfx[:1] + sfx[2:]   # drop the h onset, keep the leading -
        out += sfx.replace("-", "")
        parts.append((m, sfx, CHORD[m]))
    return out, parts


SELFTEST = [   # (root, morphemes, head, expected)
    ("orgi",    ["NOM"],        None,      "orgi"),
    ("orgi",    ["ACC"],        None,      "orgina"),
    ("sefmeh",  ["ACC"],        None,      "sefmehna"),
    ("thyma",   ["V1"],         None,      "thymara"),
    ("res",     ["V2"],         None,      "resne"),
    ("hosda",   ["MOD"],        "sefmeh",  "hosdahes"),
    ("sefmeh",  ["MOD"],        "orgi",    "sefmehes"),
    ("hosda",   ["MOD", "ACC"], "sefmeh",  "hosdahesna"),
]


def main():
    if "--selftest" in sys.argv[1:]:
        bad = 0
        for root, ms, head, want in SELFTEST:
            got, parts = build(root, ms, head)
            ok = "OK " if got == want else "FAIL"
            if got != want:
                bad += 1
            print(f"{ok} {root}+{'+'.join(ms)}"
                  + (f" (+head {head})" if head else "")
                  + f" -> {got}   expected {want}   "
                  + " ".join(f"[{m} {s} {c}]" for m, s, c in parts))
        print("\nself-test:", "ALL PASS" if not bad else f"{bad} FAILURE(S)")
        return 0 if not bad else 1

    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    head = next((a.split("=", 1)[1] for a in sys.argv[1:] if a.startswith("--head=")), None)
    if len(args) < 2:
        print(__doc__)
        return 1
    root, ms = args[0], args[1].split(",")
    for m in ms:
        if m not in SKEL:
            print(f"unknown morpheme: {m}")
            return 1
    surf, parts = build(root, ms, head)
    print(f"{root} + {'+'.join(ms)}" + (f"  (head: {head})" if head else ""))
    print(f"  trigger class : {trigger_class(head) if head else trigger_class(root)}"
          + ("  <- the HEAD, because a modifier is head-coloured (H9)" if head else ""))
    for m, s, c in parts:
        print(f"  {m:4} {s or '(zero)':7} chord {c}")
    print(f"  surface       : {surf}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
