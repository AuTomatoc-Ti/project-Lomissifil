# Handoff — background for the next session/agent

## What this is

- A **constructed language**. **"Lomissifil" is only the PROJECT name**; the language
  itself is unnamed.
- Layout: `decision/` = locked design + open questions, `draft/` = scratch,
  `reference/example.md` = the only words allowed in examples, `textbook/` = future.
- The repo is **not** a git repo.

## The author's brief

The language must sound beautiful specifically in:
**epic/powerful power metal · emotionally delicate post-rock · resonant symphonic
vocals · ethereal nostalgic folk**. Standing priority order (from `.clinerules/colang.md`):
1) beauty, 2) neutrality (no loanwords / not too much like any one language),
3) typable on an English keyboard with **no custom symbols**.

## How the design sessions work

- The conversation runs in a **"grill" style: one fine question at a time**, each
  with an explanation, concrete options, and the risks/limitations the author may have
  missed. Do **not** batch many questions.
- Per topic the pattern is: gather evidence from existing material -> propose->
  **surface conflicts instead of averaging them** -> the author chooses -> lock it and
  record it in `decision/`.
- Decisions are numbered in the order they were asked: `V*` = vowels, `C*` = consonants,
  `P*` = phonotactics/stress, `N1` = notation. See `decision/00-README.md` for the log.

## Hard constraints (do not violate)

- **NO tone/pitch exists in this language, and it never *sounds* chords.** "tonic / subdominant /
  dominant" are **metaphors** for three relational **vowel-colour** classes. Never write or reason as
  if the grammar produces audible harmony — see the terminology warning at the top of
  `decision/00-README.md`.
- **ASCII letters only, no custom symbols**, anywhere (goal 3).
- Examples may **only** use words already in `reference/example.md` (currently just
  2 names + 4 roots) — so real sentences are not possible yet.
- Goal 2: avoid loanwords; do not let the language resemble any single natural language
  too closely.

## Tooling verified on this machine (macOS)

- **Auditioning:** `espeak-ng -v fi` is a good approximation engine, because Finnish
  orthography maps almost 1:1 onto the vowel system —
  `y`=/y/, `ä`=/æ/ (our `ae`), `a`=/ɑ/, `o`=/o/, `u`=/u/, `e`=/e/, `i`=/i/.
  - Recipe: `espeak-ng -v fi -s 130 -w /tmp/out.wav "le li ly lä la lo lu"`
    then open `/tmp/out.wav`.
  - `-v fi` even reads `t`, `s`, `n`, `l`, `r`, geminates and clusters reasonably.
- The IPA-phoneme input path (`espeak-ng ... "[[...]]"`) did **not** work with `-v fi`
  — do not rely on it.
- `say`, `ffmpeg`, `python3` are also present. WAVs were written to `/tmp` only.

## Where it stands / exact next step

- Phonology, notation and the **vowel-colour ("grade") system** are in place; morphology and the
  opening of syntax are done.
- **⚠️ Read first:** the terminology warning at the top of `decision/00-README.md` (no tone/pitch —
  "chords" are metaphors) and **`03-open-questions.md` §0 — the canonical pending list**.
- **`M1` is DECIDED but PROVISIONAL = SUFFIXES** (author's call, risk accepted). The
  earlier "head-final hint" argument for it was **circular** — the hint *is* P4d, which
  is itself provisional. **P4d is PROVISIONAL too.**
- Settled along the way: **P5** (`st` = coda `s` + onset `t`/`d`; `losdo` legal, knob applies),
  **`austareus` = `aus-ta-reus`** (all six reference words are now sound), **M2** (ordering principle
  only; density deferred), **M3a** (the `f/v/h` seam), **M3b** (suffix = one syllable `C V (C)`,
  identity space 5x6 = 30), **M4/M4a** (the case table), **H1–H8** (the grade system),
  **S1/S2** (negator `mei` postposed; free scrambling + verb-final default).
- **The grade system in one paragraph.** A suffix's vowel "grade" is the **contrast** against the root's
  last syllable nucleus (H4): same vowel = *tonic*, the class's central vowel (`e`/`o`) = *subdominant*,
  the opposite pole (`a`/`i`) = *dominant* (H3). The grade is fixed by the grammatical category (H2);
  the **outermost** suffix decides the word's chord label (M2c), inner ones stay as **redundant cues**.
  Particles carry **no** colour marker (H6). Questions / negation / non-final clauses use dominant-grade
  function words (H5), and `mei` is postposed to what it negates (S1). Because word order is free (S2),
  **the order of a clause is its chord progression**.
- **The case table (M4a):** NOM I · zero / ACC V · `n` / GEN V · `s` / DAT IV · `m` / LOC IV · `n`+`r` /
  INS IV · `s`+`r` / OBL IV · `l`; verbs V1 I · `r`, V2 I · `n`. **24 of 30 identity shapes are still free.**
- **➡️ NEXT: M4b — grade labels for the inner/non-role categories** (number, tense, aspect, mood,
  person); sub-question: is NUMBER suffixed at all? Then **M5a** (the verb's outermost suffix — it decides
  whether verbs stay permanently tonic), then M5–M7 and the rest of syntax.
- **Two areas are still empty, and material is now waiting for both:** prosody ↔ melody (must map
  **contrast relative to each word's own centre**, never absolute colour) and **rhyme/押韻** (undesigned).
- Bookkeeping: recompute `05`'s capacity numbers by script; write the 1-/3-syllable root enumerations.
- **Reserve:** keep the case grades at 1·2·4; if too many IV show up later, `INS → dominant` is the
  one-line fix (yields 1·3·3).
- ⚠️ **Sung-intelligibility risk to keep alive:** free word order is decodable only if the listener
  *hears* each word's case suffix, and case suffixes are unstressed, one syllable, and often one vowel
  apart (`-na` / `-ni` / `-no`). Mitigations already in place: the grade vowel is a redundant cue; the
  consonant shape carries identity; the notation can mark length on a suffix. See
  `03-open-questions.md` §F.

## Glossary of the author's own terms

- **"type 1"** = the single vowels; **"type 2"** = diphthongs (one syllable);
  **"type 3"** = adjacent vowels split across two syllables (hiatus) = the "leaps".
- **硬 / 軟** = *hard* (voiceless stop `p t k`) / *soft* (voiced stop `b d g`), chosen
  freely by the performer via the voicing knob.
