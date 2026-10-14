#!/usr/bin/env python3
"""Goal-2 instrument 2: the SOUND-axis fingerprint (see decision/06-neutrality.md).

The donor ledger (06-neutrality.md) is qualitative and it concluded that the exposure sits on the
sound axis, especially the SPELLING. This script puts numbers on that axis. Three modes:

  --profile    fully MEASURED structural profile of our candidate material (no external data):
               syllables per form, open-syllable rate, cluster rate, digraph + P6 rates, word-final
               distribution, vowel ratio, and how much of the locked inventory the pool actually uses.
  --english    coincidence with a REAL English dictionary (/usr/share/dict/words, Webster's 2nd):
               exact matches (listed) and 1-substitution matches, each against a baseline of
               same-length random strings. Caveat printed with the result -- the uniform-letter
               baseline is a WEAK null (any vowel-rich string beats it).
  --similarity our rule-derived typological vector vs 16 HAND-CODED reference languages, with a
               Jaccard ranking and the "distinctive matches" (features we share with a language but
               NOT with the average language).

Languages (author's ruling 2026-10-14): donors = Finnish, Turkish, Japanese, German, Polish, Latin,
Italian, English, Albanian, Old English; non-donors (accidental-resemblance risk) = Mandarin
(pinyin), Cantonese (Jyutping), Indonesian/Malay, Maori, Hawaiian, Quechua.

⚠️ HONESTY: the reference vectors below are HAND-CODED from well-known typology, not corpus data.
A wrong cell only changes that language's score; `?` cells are excluded from the comparison.
"""

import argparse
import random
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import syllabify as S                      # noqa: E402

# feature order (15): y th sh tc gem ini fin finf tone case aggl free dig vlen diph
FEATURES = ("front-rounded /y/", "/th/ = /T/", "/sh/ = /S/", "/tc/ = /tS/", "geminates",
            "word-initial clusters", "word-final consonants", "word-final fricatives",
            "lexical pitch/tone", "case marking", "agglutinative", "free word order",
            "digraphs for one sound", "contrastive vowel length", "diphthongs")

# Our vector is DERIVED FROM THE LOCKED RULES (see the cell comments), not guessed.
# street order: y th sh tc gem ini fin finf tone case aggl free dig vlen diph
OURS = [  # 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
    "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "N", "Y", "Y", "Y", "Y", "N", "Y"]
#    |    |    |    |    |    |    |    |    |    |    |    |    |    |    +- diph: 8 diphthongs (V7)
#    |    |    |    |    |    |    |    |    |    |    |    |    |    +------ vlen: V4 -- length is NOT phonemic
#    |    |    |    |    |    |    |    |    |    |    |    |    +----------- dig:  sh / th / ng / ae
#    |    |    |    |    |    |    |    |    |    |    |    +---------------- free: S2 (free scrambling)
#    |    |    |    |    |    |    |    |    |    |    +--------------------- aggl: M1 (PROVISIONAL)
#    |    |    |    |    |    |    |    |    |    +-------------------------- case: M4
#    |    |    |    |    |    |    |    |    +------------------------------- tone: NONE (V4 + terminology warning)
#    |    |    |    |    |    |    |    +------------------------------------ finf: A1 (f / w / h)
#    |    |    |    |    |    |    +----------------------------------------- fin:  A1 layer 2 (any word)
#    |    |    |    |    |    +---------------------------------------------- ini:  R1 ruling A (pr br tr dr kr gr)
#    |    |    |    |    +--------------------------------------------------- gem:  C1 (ss nn ll mm rr ww)
#    |    |    |    +-------------------------------------------------------- tc:   C1 (`c` = /tS/)
#    |    |    +------------------------------------------------------------- sh:   C1
#    |    +------------------------------------------------------------------ th:   C1
#    +----------------------------------------------------------------------- y:    V1 (lone /y/)

REF = {   # y th sh tc gem ini fin finf tone case aggl free dig vlen diph   (Y/N only; '?' = unknown)
    # ---- DONORS (the 10 named in the ledger) ----
    "Finnish":     ["Y", "N", "Y", "N", "Y", "N", "Y", "Y", "N", "Y", "Y", "Y", "N", "Y", "Y"],
    "Turkish":     ["Y", "N", "Y", "Y", "Y", "N", "Y", "Y", "N", "Y", "Y", "Y", "N", "N", "N"],
    "Japanese":    ["N", "N", "Y", "Y", "Y", "N", "N", "N", "Y", "N", "Y", "Y", "Y", "Y", "N"],
    "German":      ["Y", "N", "Y", "Y", "N", "Y", "Y", "Y", "N", "Y", "N", "Y", "Y", "Y", "Y"],
    "Polish":      ["N", "N", "Y", "Y", "N", "Y", "Y", "Y", "N", "Y", "N", "Y", "Y", "N", "N"],
    "Latin":       ["N", "N", "N", "N", "Y", "Y", "Y", "Y", "N", "Y", "N", "Y", "Y", "Y", "Y"],
    "Italian":     ["N", "N", "Y", "Y", "Y", "Y", "Y", "N", "N", "N", "N", "Y", "Y", "N", "Y"],
    "English":     ["N", "Y", "Y", "Y", "N", "Y", "Y", "Y", "N", "N", "N", "N", "Y", "N", "Y"],
    "Albanian":    ["Y", "Y", "Y", "Y", "N", "Y", "Y", "Y", "N", "Y", "N", "Y", "Y", "N", "Y"],
    "Old English": ["Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "N", "Y", "N", "Y", "Y", "Y", "Y"],
    # ---- NON-DONORS: did we land near something we never borrowed from? ----
    "Mandarin":    ["Y", "N", "Y", "Y", "N", "N", "N", "N", "Y", "N", "N", "N", "Y", "N", "Y"],
    "Cantonese":   ["Y", "N", "N", "N", "N", "N", "Y", "N", "Y", "N", "N", "N", "Y", "Y", "Y"],
    "Indonesian":  ["N", "N", "Y", "Y", "N", "Y", "Y", "Y", "N", "N", "Y", "N", "Y", "N", "Y"],
    "Maori":       ["N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "Y", "Y", "Y"],
    "Hawaiian":    ["N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "N", "Y", "Y"],
    "Quechua":     ["N", "N", "Y", "Y", "N", "N", "Y", "N", "N", "Y", "Y", "Y", "Y", "N", "Y"],
}


def similarity():
    """Jaccard vs the 16 hand-coded reference languages + the 'distinctive matches'."""
    _validate()
    n = len(FEATURES)
    majority = []
    for i in range(n):
        yes = sum(1 for v in REF.values() if v[i] == "Y")
        majority.append("Y" if yes * 2 > len(REF) else "N")
    print("feature order (15):")
    for i, f in enumerate(FEATURES):
        print("   %2d  %s" % (i + 1, f))
    print()
    print("OURS            : %s" % " ".join(OURS))
    print("majority of the 16: %s" % " ".join(majority))
    print()
    rows = []
    for nm, v in sorted(REF.items()):
        inter = sum(1 for i in range(n) if OURS[i] == "Y" and v[i] == "Y")
        union = sum(1 for i in range(n) if OURS[i] == "Y" or v[i] == "Y")
        j = inter / float(union) if union else 0.0
        agree = [i for i in range(n) if OURS[i] == v[i]]
        # a "distinctive match" = we agree with this language where we differ from the majority
        dist = [FEATURES[i] for i in range(n) if OURS[i] == v[i] and OURS[i] != majority[i]]
        rows.append((j, nm, agree, dist))
    rows.sort(key=lambda r: (-r[0], r[1]))
    mean = sum(r[0] for r in rows) / float(len(rows))
    var = sum((r[0] - mean) ** 2 for r in rows) / float(len(rows))
    sd = var ** 0.5
    print("Jaccard similarity to OUR rule-derived vector (higher = more similar):")
    for j, nm, agree, dist in rows:
        flag = "  <-- above mean+1sd" if j > mean + sd else ""
        print("  %-13s %.3f   %2d/15 features agree%s" % (nm, j, len(agree), flag))
    print()
    print("mean %.3f   sd %.3f   max %.3f (%s)   min %.3f (%s)"
          % (mean, sd, rows[0][0], rows[0][1], rows[-1][0], rows[-1][1]))
    print()
    print("DISTINCTIVE matches (we agree with the language where we differ from the average):")
    for j, nm, agree, dist in rows:
        if dist:
            print("  %-13s %s" % (nm, " | ".join(dist)))


def _split_syl(s):
    """-> (onset, nucleus, coda) of one syllable string, or None."""
    toks = S.tokenize(s)
    if not toks:
        return None
    i = 0
    on = []
    while i < len(toks) and toks[i][0] == "C":
        on.append(toks[i][1])
        i += 1
    if i >= len(toks):
        return None
    nuc = toks[i][1]
    i += 1
    cod = []
    while i < len(toks) and toks[i][0] == "C":
        cod.append(toks[i][1])
        i += 1
    return "".join(on), nuc, "".join(cod)


def profile(src):
    """Fully measured structural profile of the candidate material (all 4 sibling forms)."""
    bases = [ln.strip() for ln in open(src, encoding="utf-8")
             if ln.strip() and not ln.startswith("#")]
    forms = []
    for b in bases:
        forms += [b + "f", b + "w", b + "h", b]
    n = len(forms)
    syl_hist, finals = {}, {}
    open_n = closed = 0
    onset_cl = 0
    dig = hard = viol = bad = 0
    nuc_len = 0
    onsets, nuclei, codas = set(), set(), set()
    extras = set()
    for f in forms:
        an = S.analyse(f)
        if not an["syllables"]:
            bad += 1
            continue
        syl_hist[len(an["syllables"])] = syl_hist.get(len(an["syllables"]), 0) + 1
        last = f[-1]
        key = ("vowel" if last in "aeiouy" else
               "f/w/h (area rule)" if last in "fwh" else "coda " + last)
        finals[key] = finals.get(key, 0) + 1
        if "sh" in f or "th" in f or "ng" in f:
            dig += 1
        if an["p6"]:
            hard += 1
        if an["p6_illegal"]:
            viol += 1
        for s in an["syllables"]:
            sp = _split_syl(s)
            if not sp:
                continue
            on, nuc, cod = sp
            nuc_len += len(nuc)
            if on:
                onsets.add(on)
                if len(S.tokenize(on)) > 1:
                    onset_cl += 1
            nuclei.add(nuc)
            if cod:
                closed += 1
                if cod in ("m", "n", "l", "r", "s"):
                    codas.add(cod)          # the P3 coda set
                else:
                    extras.add(cod)         # word-final f / w / h = the area rule (R1)
            else:
                open_n += 1
    tot_syl = open_n + closed
    print("forms: %d  (4 per base; bases: %d)" % (n, len(bases)))
    print("mean length %.2f letters   vowel letters %d/%d = %.1f%%"
          % (sum(len(f) for f in forms) / float(n), nuc_len, sum(len(f) for f in forms),
             100.0 * nuc_len / sum(len(f) for f in forms)))
    print("syllables per form: %s"
          % ", ".join("%d->%d (%.1f%%)" % (k, v, 100.0 * v / n)
                      for k, v in sorted(syl_hist.items())))
    print("OPEN-syllable rate: %d/%d = %.1f%%   (closed %d)"
          % (open_n, tot_syl, 100.0 * open_n / tot_syl, closed))
    print("onset clusters: %d occurrences (%.1f%% of forms contain one)"
          % (onset_cl, 100.0 * sum(1 for f in forms if any(c in f for c in
              ("pr", "br", "tr", "dr", "kr", "gr", "fm", "fn", "hm", "hn", "wm", "wn", "jm", "jn"))) / n))
    print("word-final: %s" % ", ".join("%s %d (%.1f%%)" % (k, v, 100.0 * v / n)
                                       for k, v in sorted(finals.items())))
    print("digraph spelling (sh/th/ng): %d (%.1f%%)   P6 hard spelling: %d (%.1f%%)"
          % (dig, 100.0 * dig / n, hard, 100.0 * hard / n))
    print("P6-illegal forms: %d   unreadable forms: %d" % (viol, bad))
    print("INVENTORY COVERAGE — distinct onsets used: %d %s" % (len(onsets), sorted(onsets)))
    print("                      distinct nuclei used: %d/15 %s"
          % (len(nuclei), sorted(nuclei)))
    print("                      distinct codas used (P3 set): %d/5 %s"
          % (len(codas), sorted(codas)))
    print("                      word-final extras (R1 area rule): %s" % sorted(extras))


def _validate():
    """Fail loud: a wrong-length vector would silently distort every comparison."""
    bad = []
    if len(OURS) != len(FEATURES):
        bad.append("OURS")
    for nm, v in REF.items():
        if len(v) != len(FEATURES) or any(c not in "YN?" for c in v):
            bad.append("%s (%d cells)" % (nm, len(v)))
    if bad:
        raise SystemExit("FATAL: bad feature vectors: %s -- expected %d cells of Y/N/?"
                         % (", ".join(bad), len(FEATURES)))


ENGLISH_DICT = "/usr/share/dict/words"


def _neigh(f):
    yield f
    for i in range(len(f)):
        for c in "abcdefghijklmnopqrstuvwxyz":
            if c != f[i]:
                yield f[:i] + c + f[i + 1:]


def english(src, sample):
    """Coincidence with a REAL English dictionary, against a same-length random baseline."""
    if not os.path.exists(ENGLISH_DICT):
        raise SystemExit("FATAL: no dictionary at %s -- this mode cannot run here" % ENGLISH_DICT)
    words = set()
    for ln in open(ENGLISH_DICT, encoding="utf-8", errors="ignore"):
        w = ln.strip().lower()
        if w.isalpha() and len(w) >= 2:
            words.add(w)
    bases = [ln.strip() for ln in open(src, encoding="utf-8")
             if ln.strip() and not ln.startswith("#")]
    forms = []
    for b in bases:
        forms += [b + "f", b + "w", b + "h", b]
    print("dictionary: %s (%d entries, lowercased)" % (ENGLISH_DICT, len(words)))
    print("forms tested: %d" % len(forms))
    exact = [f for f in forms if f in words]
    print("EXACT matches (our form IS an English word): %d  (%.3f%%)"
          % (len(exact), 100.0 * len(exact) / len(forms)))
    if exact:
        print("  the list (candidates to avoid on THIS channel):")
        print("  " + " ".join(exact[:200]))
        if len(exact) > 200:
            print("  ... and %d more" % (len(exact) - 200))
    random.seed(20261014)
    samp = random.sample(forms, min(sample, len(forms)))
    n = len(samp)
    one = [f for f in samp if f not in words and any(g in words for g in _neigh(f))]
    rand = ["".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(len(f)))
            for f in samp]
    rone = [f for f in rand if f not in words and any(g in words for g in _neigh(f))]
    rex = [f for f in rand if f in words]
    print("SAMPLE %d real forms : exact %d (%.3f%%)   1-substitution %d (%.2f%%)"
          % (n, len([f for f in samp if f in words]), 100.0 * len([f for f in samp if f in words]) / n,
             len(one), 100.0 * len(one) / n))
    print("SAME-LENGTH random   : exact %d (%.3f%%)   1-substitution %d (%.2f%%)"
          % (len(rex), 100.0 * len(rex) / n, len(rone), 100.0 * len(rone) / n))
    print()
    print("CAVEAT -- do not overread the 1-substitution number: the uniform-random baseline is a")
    print("WEAK null. Real languages are vowel-rich, so ANY vowel-rich string sits closer to an")
    print("English dictionary than a uniform random string does. The number to act on is the")
    print("EXACT list above; the ratio only says 'our strings are word-like, not letter-soup'.")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--profile", action="store_true", help="measured structure of the material")
    ap.add_argument("--english", action="store_true", help="coincidence with an English dictionary")
    ap.add_argument("--similarity", action="store_true", help="Jaccard vs 16 reference languages")
    ap.add_argument("--src", default="lists/roots-bases-current.txt")
    ap.add_argument("--sample", type=int, default=4000)
    a = ap.parse_args()
    ran = False
    if a.profile:
        ran = True
        profile(a.src)
    if a.english:
        ran = True
        english(a.src, a.sample)
    if a.similarity:
        ran = True
        similarity()
    if not ran:
        ap.print_help()


if __name__ == "__main__":
    main()


