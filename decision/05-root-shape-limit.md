# 05 — Root capacity under the tighter shape rule (pairwise distance >= 2)

> **Scope note (author):** every count in this file is over the **2-syllable core** of the
> shape policy. Root length by frequency: **1 syllable frequent** (`roi`), **2 syllables the
> core**, **3 syllables rare** (`argonna`). The 1- and 3-syllable classes are **not** in these
> counts, so these totals are **lower bounds** for the real space.

**Author's tighter rule (as interpreted — please confirm):**

- Bare roots may only be **VCV / CVCV**;
- **plus VCCV / CVCCV** when the medial `CC`'s **first C (the coda) is a sonorant**
  (`m n l r`; `/s/` excluded because it is not a sonorant);
- target lexicon: **1000–3000 bare words**, with **distance >= 2 between "most" roots**.

## Computed results

| Metric | Value |
|---|---|
| valid roots (plain enumeration, monophthong nuclei) | 48,020 |
| valid roots if diphthong nuclei are also allowed in roots | 220,500 |
| neighbours within distance <= 1 (avg / min / max) | 43.5 / 42 / 55 |
| **max roots with pairwise distance >= 2** | **~3,010 (greedy) … ~3,430 (upper bound)** |

### Upper bound (projection bound)

Two words at distance >= 2 must not agree in all-but-one coordinate, so the projection
onto any L-1 coordinates is injective; take the tightest (drop the largest coordinate):

| shape | coordinate sizes | bound |
|---|---|---|
| VCV | 7 · 14 · 7 | 49 |
| CVCV | 13 · 7 · 14 · 7 | 637 |
| VCCV | 7 · 4 · 14 · 7 | 196 |
| CVCCV | 13 · 7 · 4 · 14 · 7 | 2,548 |
| **TOTAL** | | **3,430** |

Without the coda shapes entirely: 49 + 637 = **686**.

## Conclusions

1. **1000–3000 fits — but the top of the range is essentially the hard limit.**
   Greedy reached 3,010, the ceiling is 3,430. **There is no headroom for growth.**
2. **The sonorant-coda exception is load-bearing.** Without VCCV/CVCCV the ceiling drops to
   ~686, i.e. *below the 1,000 minimum*. So the "unless coda 用響音" clause is what makes
   the target achievable at all.
3. The author said **"most" roots**, not all: releasing the strictness on a few pairs buys
   real slack (a near-code of ~2.5–3k is comfortable).
4. **The metric matters.** The numbers above count distance **per segment** (Levenshtein).
   If distance were counted **per phonetic feature**, it would usually be *stricter*
   (fewer roots) — this should be pinned down before coining roots.
5. Raw space is NOT the issue: 48,020 (or 220,500) forms exist; the binding constraint is
   keeping them apart.

## If more capacity is ever needed

- allow `/s/` as a coda as well (5th coda) → ceiling rises to ~4,116;
- allow diphthong nuclei inside roots (raw space 220,500) — recheck the ceiling;
- relax the shape list (e.g. allow the whitelisted clusters `pr/tr/...` inside roots).

---

## UPDATE — author then accepted BOTH: diphthong nuclei **and** `s` as a coda

Recomputed with the same method:

| Metric | Value |
|---|---|
| valid roots | **264,600** |
| neighbours within distance <= 1 (avg / min / max) | 49.4 / 43 / 88 |
| **max roots with pairwise segment-distance >= 2** | **>= 16,108** (greedy; 12 seeds gave 16,034–16,108) |

**Validation:** the same enumeration + greedy code, run on the PREVIOUS configuration
(monophthongs only, coda `m n l r`), reproduced **3,006** — consistent with the earlier
3,010, so the machinery (and therefore the new number) is trustworthy.

Interpretation:

- Headroom over the 3,000 target is now **~5.4x** → **comfortable**.
- Why the big jump: (a) raw space x5.5 (48,020 → 264,600); (b) words get **longer**
  (up to 7 segments with diphthongs) and longer words differ in more positions, so
  "distance >= 2" is much easier to satisfy.
- Distance is counted on **segments**, so a diphthong counts as 2
  (`tara` vs `taira` = distance 1) — this is the strict/honest reading.
- Greedy is *constructive*, so 16,108 is a **guaranteed achievable** count; the true
  maximum is at least that.

**Still to pin down:** whether "distance >= 2" is measured per *segment* (used here) or
per *phonetic feature* (usually stricter).

---

## FINAL RESOLUTION (this thread) — the "distance" rule is a SOFT GUIDELINE

The author decided (rule **D**): the "differ by only one consonant" limitation is a
**creation guideline, not a hard ban** — a larger difference between two bare roots is
*suggested*, but a near-minimal pair such as `latif` / `latiw` is **totally acceptable**
if the author wants it.

Consequences:

1. **There is no hard distance constraint.** The effective capacity is therefore the
   raw form space.
2. **Updated raw form space** (after the new shape policy
   `VCV(C) / CVCV(C) / VCCV(C) / CVCCV(C) / CVV(C)`, optional word-final `(C)` assumed to
   be `∅ / f / v(w) / h`):

   | shape | forms |
   |---|---|
   | VCV | 3,600 |
   | CVCV | 54,000 |
   | VCCV | 20,025 |
   | CVCCV | 300,375 |
   | CVV | 60 |
   | subtotal (no final) | 378,060 |
   | **with optional final x4** | **1,512,240** |

3. **Target 1,000–3,000 = ~0.2% of the space** → capacity is no longer a concern at all.
4. The area rules (`{f,v}`, `{h,∅}`) and the `j`-vs-hiatus note (`ria`/`rija`) are the
   **same kind of soft quality guideline** (the author explicitly rated `ria`/`rija` as
   "highly not suggested by distance, so no conflict issue").
5. **Still open:** the exact spec of the optional word-final `(C)` (assumed `f / v / h`),
   and whether those area rules are guidelines or bans.

---

## UPDATE 2 — the word-final area rule is HARD; clusters may be word-initial

Two further author revisions:

1. **The word-final area rule is HARD, not a guideline.** "Strictly 2 choose 1 from the
   same area": for every base at most one of `{f, v}` may be used, and at most one of
   `{h, no-final}`. So a base yields **1–2** roots (instead of 4).
2. **Clusters may occupy an onset slot, word-initially too.** Revised shapes:
   `VCV(C) / {C}CVCV(C) / VCCV(C) / {C}CVCCV(C) / CVV(C)`, where `{C}C` = a single
   consonant **or** a permitted cluster (2 places). The earlier stop+`r` clusters
   (`pr br tr dr kr gr`) are **back in** the permitted set.

   Permitted clusters counted distinctively (stop voicing is non-distinctive, so
   `pr`/`br` collapse): `pr tr kr` (3) + `st fm fn hm hn vm vn jm jn` (9) = **12**.
   Medial `CC` options = (coda `m n l r s` + single onset) + clusters = `5x16 + 12 = 92`.

Recomputed raw space:

| reading | base forms (no final) | with final (<=2 per base) |
|---|---|---|
| clusters CAN be word-initial (new revision) | **680,508** | **<= 1,361,016** |
| clusters medial-only (earlier rule) | 388,860 | <= 777,720 |

Either way the 1,000–3,000 target is ~0.2% of the space — capacity remains a non-issue.

**RESOLVED (author picked B):** only the **stop+`r`** clusters (`pr br tr dr kr gr`) may be
word-initial. `st` and `fm fn hm hn wm wn jm jn` are **VCV-only** — they may only sit
between two vowels, never word-initially (they still count in the medial `CC`).
*(⚠️ The `st` half of this is outdated: see the P5 update below.)*

> **UPDATE — P5 (later):** `st` is **no longer a cluster at all**; it is the ordinary
> sequence coda `s` + onset `t`/`d`. It therefore never occupies a cluster slot, and its
> "VCV-only" restriction is now **automatic** rather than stipulated. **The capacity
> counts below are unchanged by this**, because `st` was already counted as a coda+onset
> fill (see the `|CC| = 5x16 + 11` line, where `st` is deliberately *excluded* from the 11
> "extra" clusters precisely because it is already inside the `5x16`).

**Final figure (hybrid reading):**

| shape | forms |
|---|---|
| VCV | 3,600 |
| CVCV | 64,800 |
| VCCV | 20,700 |
| CVCCV | 372,600 |
| CVV | 60 |
| **base forms (no final)** | **461,760** |
| **with final (hard rule, <=2/base)** | **<= 923,520** |

Initial onset options = 15 single consonants + 3 distinctive stop+`r` clusters = 18;
medial `CC` fills = **91** = (5 codas x 16 onsets) + 11 extra clusters (`st` is already
one of the coda+onset fills). Target 1,000–3,000 is ~0.3% of the space.

---

## Capacity under TWO strictness levels (requested)

Symbols: `|V|` = 15 nuclei; `|C|` = 16 distinctive consonants (initial singles = 15, as
`ng` is not word-initial); `|Ci|` = 18 initial onsets (15 singles + 3 stop+`r` clusters);
`|CC|` = 91 medial CC fills; `|H|` = 4 hiatus pairs.

### (i) Current rules — no hard consonant-distance rule

```
N_base = |V|·|C|·|V|            (VCV)
       + |Ci|·|V|·|C|·|V|       (CVCV / cluster-initial CCVCV)
       + |V|·|CC|·|V|           (VCCV)
       + |Ci|·|V|·|CC|·|V|      (CVCCV / CCVCCV)
       + |Ci|·|H|               (CVV)

N_base = 3,600 + 64,800 + 20,475 + 368,550 + 60 = **457,485**
N(i)  <= 2 x N_base = **<= 914,970**   (hard word-final area rule: <=2 roots per base)
```

### (ii) + hard consonant distance

Rule: two roots of the same length/pattern that differ in **exactly one consonant
position** may not coexist (so `lafi`/`lawi` banned, `lafi`/`lefi` fine).

```
N(ii) = SUM over cells (length x C/V pattern x vowel assignment)
             of (max consonant code in that cell)
```

Result (greedy, best of several orders — a constructive lower bound):

| shape | raw | packed (ii) | ratio |
|---|---|---|---|
| VCV | 3,600 | 225 | 6.2% |
| CVCV | 54,000 | 3,375 | 6.2% |
| CCVCV | 10,800 | 675 | 6.2% |
| VCCV | 20,475 | 1,800 | 8.8% |
| CVCCV | 307,125 | 19,350 | 6.3% |
| CCVCCV | 61,425 | 5,400 | 8.8% |
| CVV | 60 | 4 | 6.7% |
| **total** | **457,485** | **30,829** | **6.7%** |

- (ii) keeps **~10.3x** headroom over the 3,000 target.
- The word-final variants (`f/v/h`) would add a further layer of similar size (same
  conflict structure plus the hard area rule).
- For reference, an even stricter rule (ban ANY single-segment difference, not just
  consonant ones) gave ~16,000 under the earlier shape policy.

> ⚠️ **Observed inconsistency in this file (needs a recompute script, not hand
> arithmetic).** The tables are not mutually consistent even for the *same* rule set:
> `VCCV` 20,475 (section "i") vs 20,700 ("hybrid reading"), `CVCCV` 368,550 vs 372,600,
> `CVV` 60 vs what the formula `|Ci|·|H| = 18·4` gives (72), i.e. `|CC| = 91` vs `92` and
> `|Ci| = 18` vs `15`. The `92` variant counts `st` **twice** (once as a cluster, once
> inside "coda + onset"). **P5 confirms the `91` / **457,485** family**, so the headline
> **461,760** quoted in `00-README.md` is probably too high. The *conclusion* (the lexicon
> target is a tiny fraction of the space) holds either way.



