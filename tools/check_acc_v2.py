#!/usr/bin/env python3
"""Does V2 ever collide with ACC for the SAME root?

H3's grade table (decision/00-README.md, FINAL):  per trigger vowel -> (tonic, subdominant, dominant)

    i,y -> (i, e, a)      u -> (u, o, i)
    e   -> (e, e, a)      o -> (o, o, i)
    ae  -> (ae,e, a)      a -> (a, o, i)

M4a's skeletons:  ACC = n + dominant   (grade V)
                  V2  = n + tonic      (grade I)
                  V1  = r + tonic      LOC = n + subdominant + r
                  DAT = m + subdominant            GEN/INS = s (+dominant / +sub+r)
                  OBL = l + subdominant
This script answers two different questions, and they must not be confused:

  (1) WITHIN one root: can the ACC string equal the V2 string?  (a real ambiguity)
  (2) ACROSS roots:    which strings carry two readings?        (normal allomorphy:
                       the listener computes the grade from the root's last nucleus, H4)
"""
T = {
    "i,y": ("i", "e", "a"),
    "e":   ("e", "e", "a"),
    "ae":  ("ae", "e", "a"),
    "u":   ("u", "o", "i"),
    "o":   ("o", "o", "i"),
    "a":   ("a", "o", "i"),
}

hdr = f"{'trigger':6} | {'ACC(n+dom)':11} | {'V2(n+ton)':10} | {'V1(r+ton)':10} | {'LOC':9} | {'DAT':7} | {'GEN':7} | {'OBL':7} | same?"
print(hdr)
print("-" * len(hdr))
within = []
for trig, (ton, sub, dom) in T.items():
    acc, v2, v1 = "n" + dom, "n" + ton, "r" + ton
    loc, dat, gen, obl = "n" + sub + "r", "m" + sub, "s" + dom, "l" + sub
    same = "COLLISION" if acc == v2 else "ok"
    if acc == v2:
        within.append(trig)
    print(f"{trig:6} | -{acc:10} | -{v2:9} | -{v1:9} | -{loc:8} | -{dat:6} | -{gen:6} | -{obl:6} | {same}")

print()
print("Q1 WITHIN a root, ACC vs V2 collisions:", within if within else "NONE")
print("       (reason: ACC uses the DOMINANT vowel, V2 the TONIC; H3 guarantees they differ)")
print("       also check: does dominant ever equal tonic anywhere?",
      [t for t, (ton, sub, dom) in T.items() if ton == dom] or "no")

from collections import defaultdict

owner = defaultdict(list)
for trig, (ton, sub, dom) in T.items():
    owner["n" + dom].append(f"ACC<{trig}>")
    owner["n" + ton].append(f"V2<{trig}>")
amb = {k: v for k, v in owner.items() if len(v) > 1}
print()
print("Q2 ACROSS roots, strings with two readings (normal allomorphy, resolved by H4):")
for k, v in sorted(amb.items()):
    print(f"   -{k}: {', '.join(v)}")
