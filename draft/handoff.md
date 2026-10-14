# Handoff — background for the next session/agent

## What this is

- A **constructed language**. **"Lomissifil" is only the PROJECT name**; the language
  itself is unnamed.
- Layout: `decision/` = locked design + open questions, `draft/` = scratch,
  `reference/example.md` = the only words allowed in examples, `textbook/` = future,
  `tools/` = scripts (`enumerate_roots.py` = counts + distance>=2 packer + root emitter;
  `audition_m1.py` = the M1 A/B WAVs).
- The repo **is** a git repo (branch `main`, remote `origin`); one commit so far (`62960c8`).

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

- **~~Auditioning by synthesiser~~ — REJECTED (author, 2026-10-14).** `espeak-ng -v fi` was the
  engine used for the M1 test and the roots audition, but the author judges its output **rough and
  unneutral** (it imposes a Finnish voice on the language), so: **no further WAVs are to be
  generated — this round or in future.** The old recipe is kept only as history:
  `espeak-ng -v fi -s 130 -w /tmp/out.wav "le li ly lä la lo lu"` (Finnish maps almost 1:1 onto the
  vowel system; the IPA path `"[[...]]"` never worked with `-v fi`).
- **Consequences — do not lose these:**
  - `audio/` is now a **frozen historical record**: its `roots-*.wav` and `01`–`05` predate the
    rejection. `tools/audition_m1.py` / `tools/audition_roots.py` are **historical — do not re-run**.
  - The **M1 full re-test** (real suffixed vs prefixed words, `../decision/03-open-questions.md` §A.2)
    can **no longer** be done from WAVs — it must be done **live** (author reads / sings the written
    forms).
  - **A replacement method for judging beauty is OPEN** (`03-open-questions.md` §0 item 19). Until it
    exists, goal i ("beautiful to hear") cannot be tested at all.
- `say`, `ffmpeg`, `python3` are present. The audition `.wav` files are git-ignored (`*.wav`);
  `/tmp/lomissifil-audition/` is **not** canonical.

## Where it stands / exact next step

- Phonology, notation and the **vowel-colour ("grade") system** are in place; morphology and the
  opening of syntax are done.
- **⚠️ Read first:** the terminology warning at the top of `decision/00-README.md` (no tone/pitch —
  "chords" are metaphors) and **`03-open-questions.md` §0 — the canonical pending list**.
- **`M1` is DECIDED but PROVISIONAL = SUFFIXES** (author's call, risk accepted). The
  earlier "head-final hint" argument for it was **circular** — the hint *is* P4d, which
  is itself provisional. **P4d is PROVISIONAL too.** ✅ **2026-10-14: the M1 smoke test PASSED
  by ear** (author listened to `tools/audition_m1.py`'s WAVs and judged the suffix direction good).
  M1 therefore now HAS independent evidence — but only early perceptual evidence; the **full
  re-test** (real suffixed vs prefixed words, once M2–M5 exist) is **still pending**.
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
  INS IV · `s`+`r` / OBL IV · `l`; verbs V1 I · `r`, V2 I · `n`. **23 of 30 identity shapes are still
  free** (7 skeletons used: `n s m nr sr l r`; NOM's *zero* suffix is not one of the 30) — this file
  previously said "24", an off-by-one, now corrected against `00-README.md` M4a and `03` §0 item 14.
- **➡️ PATH CHANGED, 2026-10-14 (this session): do NOT jump straight to M4b.** The agreed order is
  0) the **M1 re-test** by ear, 1) the `05` recompute (**DONE** — see `05`'s UPDATE section),
  2) two author rulings (below), 3) the **first coining + audition round**, 4) *then* M4b — and M4b
  must be asked as a **slot-budget** question, not one label at a time: 30 suffix identities have to
  cover number / person / tense / aspect / mood, and that may already be too few (`03` §0 item 6).
- **Only ONE ruling still gates step 3:** is the coining distance **per segment** (Levenshtein —
  what the script uses) or **per phonetic feature** (`05` conclusion 4, still open)?
- **`A1` vs `R1` is RESOLVED, not open** (author's ruling, 2026-10-14): they are **two layers** —
  a **bare root** ends in `∅` (a vowel) or `f`/`v`/`h` (R1's area rule) and may **not** end in
  `m n l r s`, while **any word** (incl. every suffixed form) may end in `∅`, `f`, `v`, `h` **or**
  `m n l r s`. ⇒ M3a stays **load-bearing** (M3a fires for **3 of every 4 coined roots**), so `03` §0
  items 1 and 2 **stay open**. The **area-rule mechanism** was then pinned by the same ruling
  (option B): **two independent binary choices** — a fricative from `{f,v}`, and **`h` or nothing** —
  so every base yields **exactly 2** bare roots (one per branch). ⇒ the coining unit for step 3 is a
  **base + its 2 siblings**, and the `20,025` mutually-far bases ⇒ **~40,050 coined roots**.
- ⏸️ **PARKED by the author (2026-10-14):** what do the two siblings of a pair **mean** to each other?
  Direction = **C** (the branches carry grammatical meaning → `00-README.md` R3), but the author then
  **dropped** the content question (*"skip this first"*). ⇒ **coinage stays SOUND-ONLY** for now: do
  not assign pair semantics and do not build on R3. See `03` §0 item 14.
- ~~**Small inconsistency left over (not blocking):** R1 also allows a **word-initial stop+`r`
  cluster** in a bare root, but every capacity count in `05` (and therefore this session's script
  model) uses single initial onsets only. Worth one ruling later; it is a ×1.2 on the root space.~~
  — **RESOLVED (author's ruling A, 2026-10-14): clusters inside a bare root ARE legal** — word-initial,
  and as the 2nd syllable's onset when the 1st syllable is **open**; never after a coda (P2). The
  script now models three onset sets (O1 / O2 / O2c); `05`'s UPDATE **§6** holds the recomputed
  figures, and **the first candidate batch was regenerated** because the earlier 20,025-base menu
  contained **no clusters at all** (so `pra / tri / kro` were silently absent from the audition).
- **Two areas are still empty, and material is now waiting for both:** prosody ↔ melody (must map
  **contrast relative to each word's own centre**, never absolute colour) and **rhyme/押韻** (undesigned).
  *New (2026-10-14): the audition's `04-rhyme-*.wav` shows the suffix tails rhyme **only inside one
  root class** (`seLina` = `-na`, front vs `losDoni` = `-ni`, back) — so "automatic" rhyme is
  class-local, and choosing a clause's root classes becomes a rhyming device.*
- ~~Bookkeeping: recompute `05`'s capacity numbers by script; write the 1-/3-syllable root enumerations.~~
  — **DONE** (`tools/enumerate_roots.py`: all three of `05`'s figures reproduce exactly; 1-syllable
  bare root = **960** with an `f`/`v`/`h` final (240 vowel-final — the coda set does **not** apply to
  a bare root, per the 2026-10-14 ruling); 3-syllable `CVCVCV` = 12,960,000 lower bound — all on the
  locked inventory).
- **New artefacts this session:** `tools/enumerate_roots.py` (counts + distance >= 2 packer +
  legal-root emitter; `--emit` writes 20,025 mutually-far roots) and `tools/audition_m1.py`
  (writes the M1 A/B WAVs to `/tmp/lomissifil-audition/`).
- **Step 3 material is now READABLE without audio** (2026-10-14): `lists/picks-sheet.md` — 48 bases x 4
  forms with the **syllable split and the default stress**, generated by `tools/syllabify.py`
  (`--check` verifies the splitter; `--stats` histograms the pool). Picks go in `lists/picks.md`.
  ✅ The pool was **re-emitted after P6** (26,484 bases, 0 duplicates, 0 illegal spellings — §0 item 24),
  so the sheet's numbering is its own; `audio/roots-index.txt` is a frozen pre-P6 record. Still open:
  §0 item 21 (P6 itself is decided; the sheet now shows 20 rows with a P6 hard spelling) and item 22
  (**the batch is 100% two-syllable** — no short root, although R1 calls them frequent).
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
