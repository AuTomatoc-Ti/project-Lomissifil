# Handoff — background for the next session/agent

## What this is

- A **constructed language**. **"Lomissifil" is only the PROJECT name**; the language
  itself is unnamed.
- Layout (after the **2026-10-15 tidy-up**): `docs/decisions` = locked design + open questions,
  `docs/draft` = scratch, `data/` = generated + hand-written data, `reference/example.md` = the only
  words allowed in examples, `tools` = the scripts, `archive/` = retired material. `textbook/` is a
  location convention (**FINAL, publication-ready docs only**; working notes go in `docs/draft`,
  author convention 2026-10-14) — the folder does not exist yet. **The full map is the repo-root
  `README.md`.**
- The repo **is** a git repo (branch `main`, remote `origin`).

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
  record it in `docs/decisions`.
- Decisions are numbered in the order they were asked: `V*` = vowels, `C*` = consonants,
  `P*` = phonotactics/stress, `N1` = notation. See `docs/decisions/00-README.md` for the log.

## Hard constraints (do not violate)

- **NO tone/pitch exists in this language, and it never *sounds* chords.** "tonic / subdominant /
  dominant" are **metaphors** for three relational **vowel-colour** classes. Never write or reason as
  if the grammar produces audible harmony — see the terminology warning at the top of
  `docs/decisions/00-README.md`.
- **ASCII letters only, no custom symbols**, anywhere (goal 3).
- Examples may **only** use words already in `reference/example.md` — which is **no longer a blocker**:
  it holds 2 names + 3 function words + **36 roots** = **41 words** (batches 1–2, the author's own list,
  checked by `../../tools/check_roots.py`), and the first integrated clauses already run — see
  `01-first-lines.md`. Still missing for teaching: the case/number slots (M4b), tense/aspect/mood (M5a),
  pronouns/questions (M6) and the function-word grammar (H5).
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
  - the `audio/` folder is **gone**: the `.wav` files were **never committed** (`*.wav` is git-ignored)
    and it arrived empty at the 2026-10-15 tidy-up. The retired-audition history now lives in
    `../../archive/README.md`; `tools/archive/audition_m1.py` / `tools/archive/audition_roots.py` are
    **historical — do not re-run**.
  - The **M1 full re-test** (real suffixed vs prefixed words, `../decisions/03-open-questions.md` §A.2)
    can **no longer** be done from WAVs — it must be done **live** (author reads / sings the written
    forms).
  - **A replacement method for judging beauty is OPEN** (`../decisions/03-open-questions.md` §0 item 19). Until it
    exists, goal i ("beautiful to hear") cannot be tested at all.
- `say`, `ffmpeg`, `python3` are present. The audition `.wav` files are git-ignored (`*.wav`);
  `/tmp/lomissifil-audition/` is **not** canonical.
- **Root legality, syllables + stress:** `python3 tools/syllabify.py --check` (verifies the splitter
  against the reference words), `--sheet` (writes `../../data/generated/picks-sheet.md`), `--stats` (histogram of a
  pool: syllable counts, digraph-stress rate, P6 hard spellings, P6-illegal forms).
- **Goal-2 measurement:** `python3 tools/fingerprint.py --profile | --similarity | --english` — the
  measured half of `../decisions/06-neutrality.md`: structural profile of the candidate material,
  Jaccard similarity against **16 hand-coded reference languages**, and coincidence with the real
  English dictionary `/usr/share/dict/words`. ⚠️ The reference vectors are hand-coded; audit them in
  the tool (`REF`).
- **Coining menu:** `python3 tools/menu.py > ../../data/generated/menu.md` — the candidate pool grouped by initial
  onset and first vowel, **ranked by an auditable bias** (+2 for the un-donated features: area-rule
  final, the `fm`-class cluster, a hiatus leap; +1 for an onset cluster; −2 if the form is a real
  English word). `--group th --per 6` browses one sound in depth. Weights: `score()` in the tool.
- **M3a seam, read aloud:** `python3 tools/seam.py > ../../data/generated/seam-sheet.md` — a root + all 9 suffixes
  with the seam tier that fired and the root-based stress. This is the **audition method that replaced
  the synthesiser** (the author reads the written forms aloud): tier 3 is dormant for the current
  suffix set, and the within-branch alternatives collide in GEN/INS/OBL/V1 — which is why `../../data/hand/picks.md`'s
  "at most 2 roots per base" rule is correctness, not style.

## Where it stands / exact next step

- ⚠️ **2026-10-15 — START HERE. The bullets BELOW this one are the earlier state, and several are now
  OUT OF DATE** (they are kept as history; this bullet is authoritative). The **verb is complete** and
  the tooling changed.
- **The SEVEN decisions of the 2026-10-15 session** (logged in `../decisions/00-README.md`; the ONLY
  pending list is still `../decisions/03-open-questions.md` §0):
  - **`M4b` — NUMBER: zero morphology.** No plural suffix at all; when number must be explicit the route
    is **lexical** (the root `esa` "the all", or numerals if they are ever designed — the lexicon has
    **no numerals**). ⇒ the language marks **neither person (`M5b`) nor number**.
  - **`M4c` — the ASPECT paradigm, 4 values, carried by the finite syllable's CODA**:
    **`0 simple`** (no coda, tonic) · **`I progressive`** (`s`, dominant) · **`II perfect`** (`m`,
    tonic) · **`III`** (`m`, dominant — the author's own category: *"complete at a reference moment
    that is never now, so the contrary holds now"*, i.e. a **discontinuous** aspect, both directions;
    the closest documented thing is Plungian's *discontinuous past*).
  - **`M5a` — TENSE IS CANCELLED** ("avoid too close to Indo-European"). Time is a **modifier word**
    (`ima`, positional scope, clause-initial by default ⇒ it frames the sentence) ⇒ the verb's
    morphology is **aspect + evidential** only, and `H2`'s "verbs are always tonic" is now conditional.
  - **`M5e` — the `V0` reading rule + the root CLASS system `I`/`II`/`D`** (plus the noun default
    `II*`): a bare `V0` verb claims nothing and the agentivity is read **off the participant's case**;
    the class is **advisory** and lives in `reference/example.md`'s **CLASS & POS section** (36 roots).
  - **`M5f` — EVIDENTIALITY, 4 values, an OUTER syllable ending in the one licensed stop**:
    `witnessed` `-sVg` · `inferred` `-mVd` · `surmised` `-nVg` · `reported` `-lVb`. The vowel is **`IV`**
    (subdominant) **by default and HARMONISES to dominant after a dominant aspect**; a bare `V0` root
    may carry one too (aspect may not); a word-final stop exists **only** here (`A1`/`P3`'s one
    exception). The **interrogative shift** (statement → the speaker's evidence, question → the
    hearer's) is typologically real (*egophoricity*) and is **person-free** here — needs pronouns (`M6`).
  - **`M5g` — MOOD: the IMPERATIVE is the only mood SUFFIX (`-lVn`, always DOMINANT = chord `V`), and it is mutually exclusive with the evidential; every other attitude rides `H8`'s lone VOWEL WORD** — its 7 colours (`A` anger/bravery · `AE` disgust · `O` awe/surprise = the mirative · `E` joy/searching · `I` grief/loneliness · `U` calm/mercy · `Y` fear/mystery) cost ZERO morphemes and split themselves along the bright/dark texture knob. **Prohibitive** = imperative + `mei`; **interrogative is NOT a mood** (`M6`); subjunctive/hortative deferred.
  - **`S5` — function-word POSITION is a principle:** relational words PREPOSE (`ar` "from", `mer`
    "with"), operators POSTPOSE (`mei`; any future tense/aspect particle).
  - Also: **`N1` AMENDED** (the stress capital marks the ROOT's stressed syllable ⇒ `sefMehna`, not
    `seFmehna`; `data/generated/seam-sheet.md` regenerated), and §0 items **31** (clause tool), **35**,
    **36**.
- **Identity budget — CURRENT (this is now the binding constraint):** by `(onset, coda)` **15 of the 30
  are used** (7 nominal/finite + the aspect's `(r,s) (r,m) (n,s) (n,m)` + the evidentials' `(s,g) (m,d)
  (n,g) (l,b)`); by **triples** (a triple = onset + coda + GRADE, and the harmony gives each evidential
  two variants) **≈22 of 30 are spoken for ⇒ only ~8 triples are free**. **⇒ the "23 of 30 free" claim
  further down is OUT OF DATE**: the next category (MOOD) must be planned against the **triples**.
  (Counting is not automated yet — a `tools/` addition would be welcome.)
- **New tools this session (each with `--selftest` / `--check`, all green):** `tools/clause.py` (a whole
  clause: cases, chords, class warnings, 8 N1 pins) · `tools/neutrality.py` (recounts the donor ledger
  from the table itself, prints the thresholds and the headroom — **top donor Finnish 8/43 = 18.6%**,
  original 39.5%, headroom +9 / +21) · `tools/paradigm.py` (the **270-form verb paradigm** (finite x aspect x evidential OR mood) →
  `data/generated/verb-paradigm.md`). Plus **bug fixes** in `tools/seam.py` (suffix vowels were
  hard-coded for one trigger class; a vowel was inserted after `s`/`m`/`r`-final roots, which ARE codas
  ⇒ `res`+`-sog` was `reseseg`, now `resseg`) and `tools/syllabify.py` (`WORD_FINAL` accepts the
  evidential's stop).
- **Still open (short list):** the **time vocabulary** (only `ima`;
  a future word could double as §0 item 8's missing *towards*) · the **irregular-aspect policy** (must
  become a closed whitelist) · the **`§F` read-aloud test** (the author's method; the paradigm sheet is
  the material) · the **`ae` trigger class has NO lexicon root** · `tools/clause.py` still needs the
  **stop-final** and **harmony** checks · `tools/check_roots.py` needs a `--word` mode (it judges
  suffixed forms as bare roots) · **`split_run()` in `tools/syllabify.py` accepts multi-consonant codas
  (`resr-sa`), which P5 forbids** · the 6 classes awaiting the author's veto · `forah` (burn) is
  uncoined.

- Phonology, notation and the **vowel-colour ("grade") system** are in place; morphology and the
  opening of syntax are done.
- **⚠️ Read first:** the terminology warning at the top of `docs/decisions/00-README.md` (no tone/pitch —
  "chords" are metaphors) and **`../decisions/03-open-questions.md` §0 — the canonical pending list**.
- **`M1` is DECIDED but PROVISIONAL = SUFFIXES** (author's call, risk accepted). The
  earlier "head-final hint" argument for it was **circular** — the hint *is* P4d, which
  is itself provisional. **P4d is PROVISIONAL too.** ✅ **2026-10-14: the M1 smoke test PASSED
  by ear** (author listened to `tools/archive/audition_m1.py`'s WAVs and judged the suffix direction good).
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
  previously said "24", an off-by-one, now corrected against `../decisions/00-README.md` M4a and `03` §0 item 14.
- ~~**➡️ PATH CHANGED, 2026-10-14 (this session): do NOT jump straight to M4b.**~~ — ⚠️ **DONE
  2026-10-15: M4b AND M4c AND M5a AND M5e AND M5f were all ruled in one session** (see the START HERE
  bullet at the top of this section), and the "slot-budget question" was asked and answered: the aspect
  and the evidential spent the budget (~8 triples left). ~~The agreed order is
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
  Direction = **C** (the branches carry grammatical meaning → `../decisions/00-README.md` R3), but the author then
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
  legal-root emitter; `--emit` writes 20,025 mutually-far roots) and `tools/archive/audition_m1.py`
  (writes the M1 A/B WAVs to `/tmp/lomissifil-audition/`).
- **Step 3 material is now READABLE without audio** (2026-10-14): three generated files, all from the
  same pool — `data/generated/menu.md` (the biased, auditable coining menu: `tools/menu.py`),
  `data/generated/picks-sheet.md` (48 bases x 7 forms with syllables + default stress: `tools/syllabify.py`),
  `data/generated/seam-sheet.md` (a root + all 9 suffixes, to be **read aloud** — the audition method that
  replaced the synthesiser: `tools/seam.py`). Picks go in `data/hand/picks.md`.
  ✅ The pool was **re-emitted after P6 AND now includes the 1-syllable class**: **26,769 bases =
  26,484 two-syllable + 285 one-syllable** (§0 items 22 and 24 both closed), 0 duplicates, 0 illegal
  spellings. ⚠️ The 1-syllable class is **exempt from the soft distance ≥ 2 rule** (it would keep only
  15 of 285 — measured); the 2-syllable core keeps the guarantee exactly.
  Still open: §0 item 20 (the seam sheet exists, the author reads it) and item 14 (R3 semantics).
- **Reserve:** keep the case grades at 1·2·4; if too many IV show up later, `INS → dominant` is the
  one-line fix (yields 1·3·3).
- ⚠️ **Sung-intelligibility risk to keep alive:** free word order is decodable only if the listener
  *hears* each word's case suffix, and case suffixes are unstressed, one syllable, and often one vowel
  apart (`-na` / `-ni` / `-no`). Mitigations already in place: the grade vowel is a redundant cue; the
  consonant shape carries identity; the notation can mark length on a suffix. See
  `../decisions/03-open-questions.md` §F.

## Glossary of the author's own terms

- **"type 1"** = the single vowels; **"type 2"** = diphthongs (one syllable);
  **"type 3"** = adjacent vowels split across two syllables (hiatus) = the "leaps".
- **硬 / 軟** = *hard* (voiceless stop `p t k`) / *soft* (voiced stop `b d g`), chosen
  freely by the performer via the voicing knob.

## Location convention (author, 2026-10-14)

- **`textbook/` = FINAL, publication-ready documentation only** — a **location convention for now**; the folder does not exist yet (working notes live in `docs/draft`).
- **Working / integration-test material lives in `docs/draft`** — e.g. `docs/draft/01-first-lines.md` (the integration test: Lines 1–6 plus the split-S pair).
- ⚠️ **Process correction (agent, same day):** two agent commits (e.g. `d5feae9`) carry a PROCESS NOTE claiming the integration-test file was never committed and was then overwritten — **that was wrong and is withdrawn.** The file had simply been moved to `docs/draft` by the author, so the agent's edit was a *creation at the vacated path*. **No content was ever lost.** The lesson that does stand: after a file moves, check its tracked state with `git ls-files` / `git status`; and prefer python or insert_line edits (they fail loudly) over blind whole-file replaces.
