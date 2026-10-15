#!/usr/bin/env python3
"""Root-capacity enumerator for the Lomissifil conlang.

Recomputes the numbers in docs/decisions/05-root-shape-limit.md FROM THE LOCKED
PHONOLOGY (docs/decisions/01-phonology.md) instead of by hand.  Action item 4 in
docs/decisions/00-README.md asks for exactly this.

Rule set actually implemented (printed on every run, never assumed):

  nuclei   7 monophthongs  a ae e o i u y      +  8 diphthongs  ai au ei eu oi ou aei aeu
  cons     16 distinctive consonants, canonical (soft) spelling:
           b d g m n r l f w s sh th h c j  +  ng (onset only, never initial)
  coda     P3: m n l r s
  clusters NONE inside roots (R2, the tight shape rule).  A coda may only
           precede a SINGLE onset.  (P2's clusters need an OPEN syllable
           before them, so they can never sit after a coda.)
  shapes   VCV, CVCV, VCCV, CVCCV      (2-syllable core)
  finals   the word-final area rule (empty / f / v / h, "<= 2 roots per base")
           is NOT part of a base count, exactly as in 05.

Note on onsets: "--legacy-onsets" reproduces 05's own counts, which use
13 initial / 14 medial onsets = the current 15/16 MINUS the two consonants
added later (`c`, `j`).  05's figures were therefore computed on a pre-`c`/`j`
inventory and understate the space in the current locked phonology.

Usage:
  python3 tools/enumerate_roots.py --report
  python3 tools/enumerate_roots.py --pack --config current
  python3 tools/enumerate_roots.py --pack --config legacy-core --emit /tmp/roots.txt
"""

import argparse
import random
import sys
import time

MONO = ("a", "ae", "e", "o", "i", "u", "y")
DIPH = ("ai", "au", "ei", "eu", "oi", "ou", "aei", "aeu")
NUCLEI = MONO + DIPH                      # 15
HIATUS = ("iu", "yu", "ia", "ya")         # the 4 "leaps": two syllables, no consonant between
CONS = ("b", "d", "g", "m", "n", "r", "l", "f", "w", "s", "sh", "th", "h", "c", "j")
NG = "ng"
CODA4 = ("m", "n", "l", "r")
CODA5 = ("m", "n", "l", "r", "s")
ADDED_LATER = ("c", "j")
STOP_R = ("br", "dr", "gr")               # distinctive stop+/r/ clusters (canonical voiced form)
NONSTOP = ("fm", "fn", "hm", "hn", "wm", "wn", "jm", "jn")   # VCV-only (no stop involved)
ALPHA = NUCLEI + CONS + (NG,)                # what a base form itself may contain (R-b: voiced)
HARD_STOP = ("p", "t", "k")                  # P6-2: legal in a base form after a nasal coda only
ALPHA_DIST = ALPHA + HARD_STOP               # ... but the DISTANCE alphabet must know them, or a
                                             # pair differing by b~p after a nasal would look >= 2
P6_MAP = {"b": "p", "d": "t", "g": "k"}      # P6-2: the hard letter of each stop phoneme


def onset_sets(legacy, clusters=False):
    """Return (O1 initial, O2 after an open vowel, O2c after a coda).

    P2: `pr br tr dr kr gr` may sit in ANY onset position but must **never touch another
    consonant**, so after a coda only a SINGLE onset is legal; `fm fn hm hn wm wn jm jn`
    are VCV-only.  R1 (author's ruling 2026-10-14, choice A): clusters inside a bare root
    ARE legal, so O1 AND O2 grow.  `legacy` (and `clusters=False`) keep them out, which is
    what reproduces 05's figures.
    """
    ini = tuple(c for c in CONS if not (legacy and c in ADDED_LATER))
    med = tuple(c for c in CONS + (NG,) if not (legacy and c in ADDED_LATER))
    if legacy or not clusters:
        return ini, med, med
    return ini + STOP_R, med + STOP_R + NONSTOP, med


def make_config(nuclei, codas, legacy, clusters=False, p6=False, mono=False):
    o1, o2, oc = onset_sets(legacy, clusters)
    return {"nuclei": nuclei, "codas": codas,
            "initial": o1, "after_open": o2, "after_coda": oc,
            "medial": o2,                      # kept as an alias for older call sites
            # `p6` = model the 2026-10-14 rulings (hard spelling after a nasal coda, and the
            # unspellable /s/+/h/ fill excluded).  OFF for the legacy/singles configs on purpose:
            # those exist to reproduce 05's published figures, so they must keep its arithmetic.
            "p6": p6,
            # `mono` = ALSO enumerate the 1-syllable roots (R1: "1 syllable = frequent", `roi`).
            # They were counted but never packed until 2026-10-14; OFF for legacy/singles so their
            # cross-checks keep matching.
            "mono": mono}


CONFIGS = {
    # 05's own validated figures (tight shape rule, pre-c/j onsets, NO clusters)
    "legacy-mono4": make_config(MONO, CODA4, True),        # 05: 48,020
    "legacy-diph4": make_config(NUCLEI, CODA4, True),      # 05: 220,500
    "legacy-core": make_config(NUCLEI, CODA5, True),       # 05: 264,600
    # locked inventory, single onsets only (what this file reported before 2026-10-14)
    "singles-mono4": make_config(MONO, CODA4, False),
    "singles-diph4": make_config(NUCLEI, CODA4, False),
    "singles-core": make_config(NUCLEI, CODA5, False),     # 345,600
    # locked inventory + clusters in roots (author's ruling A) + P6 + 1-syllable roots <-- CURRENT RULE
    "current-mono4": make_config(MONO, CODA4, False, clusters=True, p6=True, mono=True),
    "current-diph4": make_config(NUCLEI, CODA4, False, clusters=True, p6=True, mono=True),
    "current": make_config(NUCLEI, CODA5, False, clusters=True, p6=True, mono=True),
}


def formula(cfg):
    n = len(cfg["nuclei"])
    o1 = len(cfg["initial"])
    o2 = len(cfg["after_open"])
    oc = len(cfg["after_coda"])
    # P6: a coda + onset fill only counts if it HAS a spelling. `/s/` + `/h/` has none
    # (`sh` is always /ʃ/), so that one fill is excluded on the P6 configs only -- it is the
    # 4,275 difference the enumerated cross-check used to report as MISMATCH.
    excl = 1 if (cfg.get("p6") and "s" in cfg["codas"] and "h" in cfg["after_coda"]) else 0
    cc = len(cfg["codas"]) * oc - excl
    # 1-syllable roots (R1: frequent): (optional word-initial onset) x nucleus.
    mono = (1 + o1) * n if cfg.get("mono") else 0
    vcv = n * o2 * n
    cvcv = o1 * n * o2 * n
    vccv = n * cc * n
    cvccv = o1 * n * cc * n
    cvv = o1 * len(HIATUS)                 # the 4 leaps WITH an onset = 05's CVV row
    vv = len(HIATUS)                       # onset-less leaps (05 never counted these)
    return {"VCV": vcv, "CVCV": cvcv, "VCCV": vccv, "CVCCV": cvccv,
            "CVV": cvv, "VV": vv, "MONO": mono,
            "|CC|": cc, "total": vcv + cvcv + vccv + cvccv,
            "total_all": vcv + cvcv + vccv + cvccv + cvv + vv + mono,
            "|nuclei|": n, "|ini|": o1, "|med|": o2, "|oc|": oc,
            "|codas|": len(cfg["codas"])}


def p6_respell(coda, onset):
    """P6-2 (author's ruling 2026-10-14): a stop /b d g/ after a nasal coda /m/ or /n/ is
    obligatorily [p t k] AND is written with the HARD letter, so `man-ga` can never be coined --
    only `man-ka`. A cluster counts by its first element (`bra` -> `pra`). Non-nasal codas
    (`l r s`) are untouched, and `ng` is unaffected (it is the phoneme /N/, not n + g).
    """
    if coda in ("m", "n") and onset[0] in P6_MAP:
        return P6_MAP[onset[0]] + onset[1:]
    return onset


def mono_forms(cfg):
    """The 1-syllable roots (R1: "1 syllable = frequent"): (optional WORD-INITIAL onset) x nucleus.
    No coda (a bare root ends in a vowel or f/w/h, and the area-rule final is added downstream).
    ⚠️ These are EXEMPT from the distance >= 2 guideline: that guideline is SOFT (R2), and for
    2-3 letter forms it would admit only ~15 of the 285 candidates."""
    if not cfg.get("mono"):
        return []
    out = []
    for o1 in ("",) + tuple(cfg["initial"]):
        for v1 in cfg["nuclei"]:
            out.append((o1, v1) if o1 else (v1,))
    return out


def iter_forms(cfg):
    nuc = cfg["nuclei"]
    ini = cfg["initial"]
    opn = cfg["after_open"]
    oc = cfg["after_coda"]
    codas = cfg["codas"]
    for v1 in nuc:
        for o2 in opn:
            for v2 in nuc:
                yield (v1, o2, v2)                                  # VCV
    for o1 in ini:
        for v1 in nuc:
            for o2 in opn:
                for v2 in nuc:
                    yield (o1, v1, o2, v2)                      # CVCV
    for v1 in nuc:
        for c1 in codas:
            for o2 in oc:
                if cfg.get("p6") and c1 == "s" and o2 == "h":
                    continue            # P6: /s/ + /h/ has no spelling (`sh` is always /S/)
                for v2 in nuc:
                    yield (v1, c1, p6_respell(c1, o2), v2)      # VCCV (P6-2 hard spelling)
    for o1 in ini:
        for v1 in nuc:
            for c1 in codas:
                for o2 in oc:
                    if cfg.get("p6") and c1 == "s" and o2 == "h":
                        continue        # P6: unspellable -> not a legal form
                    for v2 in nuc:
                        yield (o1, v1, c1, p6_respell(c1, o2), v2)   # CVCCV (P6-2)
    for o1 in ini:
        for h in HIATUS:
            yield (o1, h[0], h[1])                              # CVV -- a "leap"
    for h in HIATUS:
        yield (h[0], h[1])                                      # VV  -- onset-less leap
    if cfg.get("mono"):
        for t in mono_forms(cfg):
            yield t                                             # the 1-syllable class (R1)


def dist1(t):
    """Every sequence at Levenshtein distance exactly 1 from tuple t."""
    out = []
    L = len(t)
    for i in range(L):
        head, tail = t[:i], t[i + 1:]
        for a in ALPHA_DIST:
            if a != t[i]:
                out.append(head + (a,) + tail)
    for i in range(L + 1):
        for a in ALPHA_DIST:
            out.append(t[:i] + (a,) + t[i:])
    for i in range(L):
        out.append(t[:i] + t[i + 1:])
    return out


def neigbour_counts(space, sample):
    return [sum(1 for g in dist1(f) if g in space) for f in sample]


def greedy_pack(space_set, order):
    """Max subset with pairwise segment-distance >= 2 (greedy over `order`)."""
    forbidden = set()
    chosen = []
    for f in order:
        if f in forbidden:
            continue
        chosen.append(f)
        for g in dist1(f):
            if g in space_set:
                forbidden.add(g)
    return chosen



def fmt(t):
    return "".join(t)


def one_syllable(cfg):
    """A 1-syllable BARE ROOT = (optional single onset) x nucleus x final.
    R1 (author's ruling 2026-10-14): a bare root ends in a vowel or f/v/h -- it may
    NOT end in the coda set m n l r s (that set is word-final, not bare-root-final)."""
    finals = ("", "f", "v", "h")
    n = len(cfg["nuclei"])
    ini = len(cfg["initial"])
    return {"no-coda": (1 + ini) * n,
            "with-coda": (1 + ini) * n * len(finals),
            "formula": "(1 + |ini|) x |nuclei| x (1 + |{f,v,h}|)"}


def three_syllable_formula(cfg):
    """CVCVCV lower bound: not materialised (3-syllable roots are 'rare')."""
    n = len(cfg["nuclei"])
    ini, med = len(cfg["initial"]), len(cfg["medial"])
    return {"CVCVCV (no codas)": ini * n * med * n * med * n,
            "formula": "|ini| x |nuclei| x |med| x |nuclei| x |med| x |nuclei| "
                       "(+ coda variants, uncounted)"}


def report(cfg, name):
    c = formula(cfg)
    print("=" * 78)
    print("config: %s" % name)
    print("  nuclei=%d  O1(initial)=%d  O2(after a vowel)=%d  O2c(after a coda)=%d  codas=%s"
          % (c["|nuclei|"], c["|ini|"], c["|med|"], c["|oc|"], ",".join(cfg["codas"])))
    print("  |CC| (medial 'CC' fill; P6 excludes the unspellable /s/+/h/) = %d" % c["|CC|"])
    print("  VCV   = |V|x|O2|x|V|         = %10s" % format(c["VCV"], ","))
    print("  CVCV  = |O1|x|V|x|O2|x|V|    = %10s" % format(c["CVCV"], ","))
    print("  VCCV  = |V|x|CC|x|V|         = %10s" % format(c["VCCV"], ","))
    print("  CVCCV = |O1|x|V|x|CC|x|V|    = %10s" % format(c["CVCCV"], ","))
    print("  CVV   = |O1| x 4 leaps       = %10s   (+%s onset-less VV)"
          % (format(c["CVV"], ","), c["VV"]))
    print("  TOTAL (4 main shapes)        = %10s" % format(c["total"], ","))
    print("  TOTAL + leaps (2-syllable)   = %10s" % format(c["total_all"] - c["MONO"], ","))
    print("  1-syllable bases %s = %10s   (R1: '1 syllable = frequent')"
          % ("IN the enumeration " if c["MONO"] else "counted, not enumerated", format(c["MONO"], ",")))
    print("  TOTAL + leaps + 1-syllable   = %10s   <- what the pack is drawn from"
          % format(c["total_all"], ","))
    # enumerated cross-check
    t0 = time.time()
    n = sum(1 for _ in iter_forms(cfg))
    print("  enumerated cross-check        = %10s  (%.1fs)  %s"
          % (format(n, ","), time.time() - t0, "MATCH" if n == c["total_all"] else "*** MISMATCH ***"))
    o = one_syllable(cfg)
    print("  1-syllable  vowel-final        = %10s" % format(o["no-coda"], ","))
    print("  1-syllable  raw, 4 finals      = %10s   %s" % (format(o["with-coda"], ","), o["formula"]))
    for k, v in three_syllable_formula(cfg).items():
        if k != "formula":
            print("  3-syllable  %-18s = %10s" % (k, format(v, ",")))
    # R1 area rule (author's ruling 2026-10-14): two INDEPENDENT binary choices --
    # a fricative from {f,v}, and {h, nothing} -- so a base yields exactly 2 bare roots.
    print("  area rule: raw finals space = 6 x bases = %s ;  COINED roots = 2 x bases = %s"
          % (format(4 * c["total_all"], ","), format(2 * c["total_all"], ",")))
    print()
    return c


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--report", action="store_true", help="counts only (fast)")
    ap.add_argument("--pack", action="store_true", help="also run the distance>=2 greedy pack")
    ap.add_argument("--config", default=None, help="config name, or 'all' (default: all for --report)")
    ap.add_argument("--seeds", type=int, default=3, help="random orders to try in --pack")
    ap.add_argument("--stats", type=int, default=0, help="neighbour stats over N sampled forms")
    ap.add_argument("--emit", default=None, help="write the packed root list here")
    ap.add_argument("--limit", type=int, default=0, help="cap the packing input (debug)")
    ap.add_argument("--pairs", type=int, default=0,
                    help="step 3: print N packed bases with their 4 area-rule sibling forms")
    ap.add_argument("--src", default="data/generated/roots-bases-current.txt",
                    help="packed-base list used by --pairs (the committed canonical list; "
                         "the old /tmp default was wiped on reboot)")
    a = ap.parse_args()
    random.seed(20261014)

    if a.pairs:
        with open(a.src, encoding="utf-8") as fh:
            bases = [ln.strip() for ln in fh if ln.strip()]
        pick = sorted(random.sample(bases, min(a.pairs, len(bases))))
        print("=" * 78)
        print("area-rule siblings: %d packed bases sampled from %d in %s"
              % (len(pick), len(bases), a.src))
        print("  base        {f,/v/} branch                    {h,s,empty} branch")
        for b in pick:
            # SPELLING: the /v/ member is written `w` -- `v` is the VIBRATO mark, not a
            # letter (02-notation.md), so a /v/-final root is `...w` (e.g. `lafiw`), never `...v`.
            # R4 (2026-10-14) added `s` to the second branch; it is RESERVED for a future job.
            print("  %-11s %-11s %-11s %-11s %-11s %-11s"
                  % (b, b + "f", b + "w", b + "h", b + "s", b))
        print("  -> exactly TWO of the six become roots: ONE from {f,v}, ONE from {h,s,empty}")
        return

    names = list(CONFIGS) if (a.config in (None, "all")) else [a.config]
    if a.config in (None, "all") and a.pack:
        names = ["legacy-core"]
    results = {}
    for nm in names:
        cfg = CONFIGS[nm]
        results[nm] = report(cfg, nm)
        if a.pack:
            forms = list(iter_forms(cfg))
            # The 1-syllable class is appended AFTER the pack instead of competing inside it:
            # pairwise distance >= 2 is a SOFT guideline (R2) and it would keep only ~15 of the 285.
            mono = mono_forms(cfg)
            mono_set = set(mono)
            if mono:
                forms = [t for t in forms if t not in mono_set]
            if a.limit:
                forms = forms[:a.limit]
            space = set(forms)
            if a.stats:
                sample = random.sample(forms, min(a.stats, len(forms)))
                ns = neigbour_counts(space, sample)
                print("  neighbours within distance <= 1 : avg %.1f  min %d  max %d  (n=%d)"
                      % (sum(ns) / len(ns), min(ns), max(ns), len(ns)))
            best, best_order = 0, None
            for s in range(a.seeds):
                order = list(forms)
                if s:
                    random.shuffle(order)
                t0 = time.time()
                chosen = greedy_pack(space, order)
                print("  pack seed %d: %6s roots   (%.1fs)" % (s, format(len(chosen), ","), time.time() - t0))
                if len(chosen) > best:
                    best, best_order = len(chosen), sorted(chosen)
            print("  BEST over %d seeds: %s roots" % (a.seeds, format(best, ",")))
            if mono and best_order:
                already = set(best_order)
                extra = [t for t in mono if t not in already]
                best, best_order = best + len(extra), sorted(list(best_order) + extra)
                near = sum(1 for t in extra
                           if any(g in already for g in dist1(t)))
                print("  + %d one-syllable roots appended (exempt from the SOFT distance>=2 rule)"
                      % len(extra))
                print("    of those, %d have a distance-1 neighbour in the pack (all pairs involve a "
                      "1-syllable root)" % near)
                print("  FINAL: %s roots" % format(best, ","))
            if a.emit and best_order:
                with open(a.emit, "w", encoding="utf-8") as fh:
                    for t in best_order:
                        fh.write(fmt(t) + "\n")
                print("  wrote %s roots to %s" % (format(len(best_order), ","), a.emit))
            print()

    if len(results) > 1:
        print("=" * 78)
        print("SUMMARY (2-syllable base forms)")
        for nm in results:
            print("  %-14s %12s" % (nm, format(results[nm]["total"], ",")))
        print()
        print("05's disputed rows (formula family, |CC|):")
        print("  VCCV  = 15 x |CC| x 15   -> %s with |CC|=91, %s with |CC|=92"
              % (format(15 * 91 * 15, ","), format(15 * 92 * 15, ",")))
        print("  CVCCV = 18 x 15 x |CC| x 15 -> %s with |CC|=91, %s with |CC|=92"
              % (format(18 * 15 * 91 * 15, ","), format(18 * 15 * 92 * 15, ",")))
        print("  family totals: %s (|CC|=91)  vs  %s (|CC|=92)"
              % (format(3600 + 64800 + 20475 + 368550 + 72, ","),
                 format(3600 + 64800 + 20700 + 372600 + 72, ",")))
        print("  P5 rules the 92 out (it double-counts 'st'), so the 91 / 457,485 family is the right one.")


if __name__ == "__main__":
    main()
