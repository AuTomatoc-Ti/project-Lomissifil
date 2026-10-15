# 02 — Orthography & Expressive Notation (LOCKED)

## Two registers

1. **Plain text** — prose, dictionary, novels.
   - **Lowercase only.** Capitals are reserved for the stress mark, so they are
     **not** used for sentence-initial letters or proper nouns (V6). Proper nouns are
     simply unmarked (Chinese-name style); grammar/context disambiguate.
     **One exception (H8):** a **one-letter vowel word** written with its initial capital is a **VOC**
     marker, not a stress mark (see the article/VOC section below).
   - No performance marks.
   - Punctuation for sentence/clause boundaries is *assumed* to still be used
     (assumption — to be confirmed).
2. **Notation text** — lyrics / performance.
   - Same base spelling, plus the three marks below.

## The three marks — letters only, no custom symbols

| Technique | Mark | Example |
|---|---|---|
| **Stress** | CAPITAL on the **last onset letter before the stressed nucleus** (N1, **amended 2026-10-15**: the capital marks the ROOT's stressed syllable, so a consonant the `M3a` seam moved into it is not capitalised) | `argonna` → `arGonna` (syllable `gon`); `sefmehna` → `sefMehna` (stressed syll. `fme`, the seam-moved `h` is in the next one) |
| **Length / sustain** | double the **last letter of the vowel grapheme** | `a`→`aa`, `ae`→`aee`, `o`→`oo`, `i`→`ii` |
| **Vibrato** | `v` immediately after the vowel | `a` → `av` |

Nothing outside A–Z is ever required → satisfies goal 3 ("typable, no custom symbols").
This is deliberate: the author's model is *composers writing down how to sing it*.

## The "voicing knob" (C2 / C2b)

- The **dictionary (citation) form uses the VOICED stop** `b d g`.
- **Phonation, not phonology (clarified).** The stops are **3 phonemes** `/b d g/`, each with a free
  voiceless realisation `[p t k]` — the knob is a **voice-quality (phonation)** setting, so it may
  be **free and unconditioned** (compare *whispering*, where every stop is voiceless and no word is
  lost). `w` (=/v/) is a real phoneme and must **never** be hardened. Full rules: `01-phonology.md` §1.
- **Register boundary (R-c).** Plain text and the dictionary are voiced **only**; hard spellings
  belong to notation/performance text and to singing — so a lookup never misses (`losdo` is the
  headword, `losto` its hard realisation).
- A composer may swap to the **VOICELESS** stop `p t k` for a harder texture —
  **the meaning does not change**, only the texture. This is the language's built-in
  "hard <-> soft" control, aimed at the power-metal vs post-rock/folk contrast.
- Voicing and stress are **decoupled** — all four combinations exist:

| | unstressed | stressed (capital) |
|---|---|---|
| **soft (voiced)** | `g` (default) | `G` |
| **hard (voiceless)** | `k` — legal, but *marked/rare* (e.g. off-beat punch) | `K` |

Because the capital sits on the syllable's first letter, one capital can show both
at once: `arGonna` = stressed + soft ; `arKonna` = stressed + hard.

## The article / VOC — an emotional vowel WORD (H8)

A separate device, spelled with a **lone vowel word** whose vowel carries an **emotion**
(so it is also the language's article):

| written | meaning |
|---|---|
| `a` · `e` · `o` · `i` · `u` · `ae` · `y` (lowercase, alone) | **article** (a / an / the) |
| `A` · `E` · `O` · `I` · `U` · `Ae` · `Y` (same word, initial capital) | **VOC** (address) |

- **One-letter-capital rule:** a one-letter vowel word written with a capital is read as **VOC**, never
  as a stress mark (otherwise `A` would be an "emphasized article").
- The vowel is chosen **emotionally** (author's example list — **not yet locked**):

| vowel | emotion |
|---|---|
| `a` | angry / brave / energetic |
| `ae` | disgust / hate |
| `o` | surprise / awe |
| `e` | joy / searching / pride |
| `i` | sad / depression / lonely |
| `u` | calm / mercy |
| `y` | fear / mysterious / confusing |

- Because the emotion lives on **this separate word**, it never collides with the root's identity or with
  a suffix's grade vowel (H3) — the two layers cannot fight.
- **Intensity** is not in the table: use the existing performance marks (length `aa`, stressed CAPITAL,
  vibrato `v`) → together they give a two-axis emotion system (which emotion × how strongly).

## Reminders

- `v` is **not** a normal letter → the sound /v/ is written `w`.
- `y` is a **vowel** (/y/), not a glide.
- `/j/` **does** exist (letter `j`) but is **onset-only** — it can never be a coda — so
  the off-glide in `ai ei oi` is still written with the vowel `i` (`tai` = diphthong,
  `taj` = illegal). *(Corrected: an earlier draft said `/j/` did not exist; `/j/` was
  added later — see `01-phonology.md` §1.)*

## Worked examples (reference words only)

| Base | Stressed (default) | + length | + vibrato |
|---|---|---|---|
| `seli` (birth) `se-li` | `seLi` | `seLii` | `seLiv` |
| `argonna` (love) `ar-gon-na` | `arGonna` | `arGoonna` | `arGovnna`* |

\* The vibrato case shows a known edge case (the mark lands before the coda `n`);
see `03-open-questions.md`.

## Example-making rule (from `.clinerules/colang.md`)

Examples for **decisions and the textbook** may **only** use words that already exist
in `reference/example.md`. Today that is 2 names + 3 function words + 36 roots = **41 words**, so
real sentences **are** possible — the first integrated clauses are in `../draft/01-first-lines.md`;
use clearly-labelled *non-semantic sound-strings* only for phonology demos.
