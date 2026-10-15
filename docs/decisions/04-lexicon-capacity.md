# 04 — Lexicon capacity (2-syllable bare roots)

> **Status: historical / superseded by `05-root-shape-limit.md`.** The conclusion (the
> phonology allows vastly more roots than the 1,000–3,000 target) still holds, but the
> method paragraph below reflects an **older cluster set** (it lists `st` as a VCV-only
> cluster — since **P5**, `st` is coda `s` + onset `t`/`d`, not a cluster at all) and the
> counts have been recomputed in `05`. Keep this file for the *reasoning*, not the numbers.
> **Also note the root-length policy (author):** **1-syllable roots are frequent** (`roi`),
> 2-syllable roots are the **core**, 3-syllable roots are **rare** (`argonna`). This file
> (see its title) counts the **2-syllable** class only, so all totals here are **partial**.

**Question asked by the author:** is the current inventory enough to coin 2-syllable
bare roots, without the language needing super-long words?

**Answer: yes, by several orders of magnitude.**

## Counts (enumerated under the locked phonology)

| Inventory | onsets (init / non-init) | 2-syllable words |
|---|---|---|
| Spelling (17 consonants) | 23 / 25 | 3,540,252 |
| **Distinctive** (14, because stop voicing is NOT distinctive — C2b) | 17 / 19 | **2,134,758** |

- Single-syllable forms: ~**1,530** (word-initial) / ~**1,710** (non-initial) — already
  enough for a core vocabulary (cf. Chinese, which runs on ~1,300 syllables).
- Headroom for a **10,000-root** lexicon: ~**213x**. For a 2,000-root lexicon: ~**1067x**.

**Method** (script, not guesswork): enumerate `(C)V(C)` syllables with onset clusters
`{pr br tr dr kr gr}` (any onset) + `{st}` (VCV only); nuclei = 7 monophthongs +
8 diphthongs; codas `{m n l r s}`; word-initial excludes `ng` and `st`; a cluster onset
requires the previous syllable to be open; vowel contact limited to the 4 hiatus pairs.

## The real constraint is NOT space

- **Perceptual distinctiveness while singing** — consonants weaken in song, and voicing
  is non-distinctive anyway, so the risk is *near-minimal-pairs*, not running out.
- **Memory / learnability** — a few thousand roots is the practical core; longer concepts
  should be compounds (normal for an agglutinative language).
- **Beauty + neutrality pruning** (goals 1–2) will discard most of the raw space.

## Recommendation

1. Cap bare roots at **2 syllables**; more is never needed for basic vocabulary.
2. Adopt a **root-shape policy** for beauty (e.g. prefer sonorant-coda `CVCV`, avoid
   overloading a single template).
3. Add a **minimum-distance rule** when coining roots (a new root must differ from
   existing roots by at least 2 features) — this is where the real design work is.
4. Let long word-forms arise only from **compounding**.

## Edge cases surfaced by this enumeration

- `ww` (/vː/) would require `w` as a coda, but the coda set is `m n l r s` → `ww` is an
  exception and needs an explicit rule.
- Whether the "no adjacent vowels" rule applies **across** syllable boundaries (this
  count assumed yes, allowing only the 4 hiatus pairs). If it applies only inside a
  syllable, the count is larger still.
