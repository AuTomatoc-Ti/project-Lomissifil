#!/usr/bin/env python3
"""Suffix-inventory collision check: H3's grade table x M4a's skeletons.

For every root-final nucleus (H4's trigger) the script computes the SURFACE string of every
morpheme, then reports:

  (1) two roles producing the SAME string **for the same root**  -> a REAL ambiguity.
      H3's coining rule forbids this. The borderline case is *tonic vs subdominant*:
      H3 makes them coincide for `e`-final and `o`-final roots.
  (2) the same string shared **across trigger classes**          -> normal allomorphy:
      the listener knows the root's last nucleus (H4), so nothing needs repairing.

Run it after ANY change to the suffix inventory.

  python3 tools/check_suffixes.py            # V2 = l + tonic            (author, 2026-10-14)
  python3 tools/check_suffixes.py --v2-coda  # V2 = l + tonic + coda r   (proposed fix)
"""
import sys

# H3 (FINAL): trigger -> (tonic, subdominant, dominant)
T = {
    "i,y": ("i", "e", "a"),
    "e":   ("e", "e", "a"),
    "ae":  ("ae", "e", "a"),
    "u":   ("u", "o", "i"),
    "o":   ("o", "o", "i"),
    "a":   ("a", "o", "i"),
}


def inventory(v2_coda, v2_onset="l"):
    """role -> (onset or None, grade or None, coda)."""
    return {
        "NOM": (None, None, ""),      # zero suffix
        "V0":  (None, None, ""),      # bare verb (author's ruling, 2026-10-14)
        "ACC": ("n", "dom", ""),
        "GEN": ("s", "dom", ""),
        "DAT": ("m", "sub", ""),
        "LOC": ("n", "sub", "r"),
        "INS": ("s", "sub", "r"),
        "OBL": ("l", "sub", ""),
        "V1":  ("r", "tonic", ""),
        "V2":  (v2_onset, "tonic", "r" if v2_coda else ""),
    }


def surface(onset, grade, coda, trio):
    if onset is None:
        return ""
    tonic, sub, dom = trio
    v = {"tonic": tonic, "sub": sub, "dom": dom}[grade]
    return "-" + onset + v + coda


def main():
    v2_coda = "--v2-coda" in sys.argv[1:]; v2_onset = next((x.split("=",1)[1] for x in sys.argv[1:] if x.startswith("--v2-onset=")), "l")
    inv = inventory(v2_coda, v2_onset)
    print("V2 = " + v2_onset + " + tonic" + (" + coda r" if v2_coda else "") + "\n")
    header = f"{'trigger':6} | " + " | ".join(f"{r:>5}" for r in inv)
    print(header)
    print("-" * len(header))

    rows = {}
    for trig, trio in T.items():
        strs = {r: surface(*inv[r], trio) for r in inv}
        rows[trig] = strs
        print(f"{trig:6} | " + " | ".join(f"{strs[r]:>5}" for r in inv))

    print("\n(1) SAME string, DIFFERENT roles, one root  -> REAL ambiguity:")
    found = False
    for trig, strs in rows.items():
        seen = {}
        for role, s in strs.items():
            seen.setdefault(s, []).append(role)
        for s, roles in seen.items():
            if len(roles) > 1:
                found = True
                print(f"   {trig:6} {s or '(zero)':>8} : {', '.join(roles)}")
    if not found:
        print("   NONE")

    print("\n(2) strings shared ACROSS trigger classes (normal allomorphy; H4 resolves it):")
    owner = {}
    for trig, strs in rows.items():
        for role, s in strs.items():
            owner.setdefault(s, set()).add(role)
    shared = {s: r for s, r in owner.items() if len(r) > 1}
    if shared:
        for s, roles in sorted(shared.items()):
            print(f"   {s or '(zero)':>8} : {', '.join(sorted(roles))}")
    else:
        print("   NONE")


if __name__ == "__main__":
    main()
