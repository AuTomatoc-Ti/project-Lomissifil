# 06 — Neutrality: the donor ledger

Goal 2 (`.clinerules/colang.md`): *"the language should be neutral (can be inspired from different
languages), but must ensure its word and grammar not like other language too much (avoid loan words
from other language)"*.

Until 2026-10-14 this goal had **no mechanism at all** — only the goal statement (`draft/handoff.md`,
`03-open-questions.md` §F). This file is that mechanism, in the form the author asked for: measure
**not only the sound, but also the grammar and the word-building**.

## What this document is (and how it is used)

1. **A ledger.** Every designed sub-area, on three axes — **A. Sound**, **B. Grammar**,
   **C. Word-building** — gets one row: what WE decided, which single natural language is the
   *closest* donor (if any), how strong that resemblance is, and where it is recorded.
2. **A dominance check.** If one language is the closest donor in too many rows, the language *is*
   that language's clone with extra steps. Strength labels used below:
   **same pattern** (a natural language does essentially the same) · **close** (very similar, a
   detail differs by our own choice) · **loose** (the same *idea*, materially different constraint) ·
   **no donor** (original; nothing in the reference set does this).
3. **A living rule (the important part).** **Every future decision adds its row(s) here in the same
   turn it is locked.** A ledger that stops being updated is worse than none: the system could drift
   into one donor while this document still claims balance. Rows still **missing** today — they
   belong to decisions not made yet: **M5, M5a, M4b, M6, M7, rhyme, prosody↔melody, negation scope**.
4. **Not a beauty filter.** Precedence is fixed by the goals file: **beauty outranks neutrality**.
   This ledger produces *warnings and design pressure*, never silent deletions.

> ⚠️ **Honesty about the method.** This is a **judgement table** (classification), not a
> measurement — built from public typological facts and from what the decision log already declares
> (e.g. C3 itself says "German-style"). Loose analogies are marked **loose**. A *statistical* sound
> measurement is a separate, still-unbuilt tool (see "What this does NOT cover").

## A. Sound — inventory, phonotactics, stress, spelling

| # | our decision (where) | closest single donor | strength | note |
|---|---|---|---|---|
| A1 | 7 vowels `a ae e o i u y` (`01-phonology` §2, V1–V3) | **Finnish** | close | Finnish has the same `/y/` + `/æ/`, but also `/ø/`, which V1 deliberately omits |
| A2 | no `/ø/`; lone `/y/` as the signature (V1) | none | no donor | a *restriction* chosen for minimalism |
| A3 | diphthongs = non-high nucleus `{a,ae,e,o}` + off-glide `{i,u}` (V7–V9) | Finnish / Germanic | loose | the *rule* is a designed generalisation; Finnish has more diphthongs and no such restriction |
| A4 | the hiatus "leap" set `iu yu ia ya` — a deliberate 2×2 front-high × extreme-back | none | no donor | no language designates a systematic "leap" set |
| A5 | 16-phoneme inventory incl. `/θ/`, and no `/z ð ʒ/` (C1, A2) | none (each member has donors; the *set* does not) | no donor | `/θ/` is rare (English, Icelandic, Greek, Castilian); the combination is idiosyncratic |
| A6 | stop voicing is **phonation** — `p t k` are free realisations, base forms voiced-only (C2/C2b, **P6**) | Finnish (no voicing contrast) | loose | the "hard/soft knob" and its P6 exception are invented |
| A7 | `/v/` written `w` (C3) | German / Polish | same pattern | |
| A8 | `sh` = /ʃ/, `th` = /θ/ (C1) | English / Albanian | same pattern | |
| A9 | `c` = /tʃ/ in every position; `j` = /j/ (C1) | `j`: German/Polish/Finnish · `c`: Italian *only before i/e* | loose | no language matches `c` = /tʃ/ everywhere |
| A10 | `ae` spells `/æ/` (V10) | Old English / Latin *letter tradition* | loose | a modern ASCII workaround; Icelandic `æ` = /ai/ |
| A11 | geminates `ss nn ll mm rr ww`, **intervocalic only**, never word-final (C1) | Italian / Japanese | close | the *whitelist of 6* and the position rule are designed |
| A12 | onset clusters only `pr br tr dr kr gr` | Slavic / Latin / Italian (inside a **much larger** set) | loose | a whitelist approach, not a copy |
| A13 | VCV-only clusters `fm fn hm hn wm wn jm jn` | none | no donor | near-unattested |
| A14 | coda `m n l r s` (P3) | Finnish | close | Finnish codas are `n l r s t` (+ `m` before `p`) — same spirit, one member differs |
| A15 | word-final **area rule**: bare roots end in `∅ / f / v / h`; any word may also end in `m n l r s` (R1, A1) | none | no donor | a designed class-marking device |
| A16 | stress = **2nd syllable of the ROOT**, affixes never move it (P4/P4c) | Polish (penultimate) | loose | Polish counts from the end; ours is root-relative and length-independent |
| A17 | notation: CAPITAL = stress only, doubled vowel = length, `v` = vibrato (V5/V6, N1) | none | no donor | no natural orthography does this; proper nouns unmarked = Chinese-style (V6) |
| A18 | no tone / no pitch (V4 + the terminology warning) | most European languages | same pattern | not distinctive either way |

## B. Grammar — the machinery of the clause

| # | our decision (where) | closest single donor | strength | note |
|---|---|---|---|---|
| B1 | case marking, 7-case working set `NOM ACC GEN DAT LOC INS OBL` (M4) | **Latin / Slavic** | close | LOC + INS together are especially Slavic; **OBL** (a dedicated "else" case) has **no donor** |
| B2 | what carries case identity: **consonant = category, vowel = relational grade** (M2c, H2–H4) | none | no donor | V2 reusing ACC's `n` with a different grade is designed |
| B3 | the **grade / chord system**: suffix vowels stand in tonic–subdominant–dominant contrast to the root's last nucleus, so **word order is a chord progression** (H1–H8) | none | no donor | inspired by functional harmony (music), not by a language — the language's centre of gravity |
| B4 | case marking **plus free word order** (S2) | Latin / Sanskrit / Russian | close | Finnish is free-ish but SVO-default |
| B5 | **verb-final default** (S2) | Latin / Sanskrit | close | Turkish/Japanese are stricter SOV |
| B6 | negation = a **postposed particle on the negated constituent**, `mei` (S1) | Turkish `değil` | close | constituent (not sentence) negation is the designed part |
| B7 | no articles | Latin, Russian, Finnish, Japanese, Chinese… | same pattern | too widespread to be a donor |
| B8 | **article & VOC are an emotional VOWEL WORD** (H8) | none | no donor | |
| B9 | VOC is **not** a case (H8) | none | no donor | Latin has a vocative case |
| B10 | no gender, no agreement | English-ish / Japanese-ish | same pattern | not distinctive |
| B11 | …questions, pronouns, tense/aspect/mood | **not designed yet** (M5, M5a, M6) | — | **rows to be added when decided** |

## C. Word-building — how a word is put together

| # | our decision (where) | closest single donor | strength | note |
|---|---|---|---|---|
| C1 | **suffixation, agglutinative** (M1, still PROVISIONAL) | Turkish / Finnish / Japanese | same pattern | |
| C2 | ordering principle: near the root = lexical, far = syntactic (M2) | Turkish / Finnish | loose | a generalisation of agglutinative layering |
| C3 | every affix is one syllable `C V (C)`, identity budget **30 shapes** (M3b) | none | no donor | a designed constraint |
| C4 | the **outermost** suffix decides the word's chord (M2c) | none | no donor | |
| C5 | affixes never move the root stress (P4c) | Turkish / Finnish | loose | those languages have *fixed* stress, not root-relative |
| C6 | compound stress: only the LAST root keeps stress (P4d, PROVISIONAL) | Japanese (head-final) | loose | German would keep the FIRST element's stress — so not German |
| C7 | the **area-rule sibling class**: every base yields exactly 2 roots differing by one segment, marking a grammatical class (R1, R3) | none | no donor | the author's own analogy was "like a derivational affix in English", but the mechanism is invented |
| C8 | the **M3a seam**: a 3-tier repair (`CC` group → syncope → copied vowel) for roots ending in `f/v/h` before a suffix | none | no donor | |
| C9 | the concrete case shapes `-na -sa -me -ner -ser -le` (M4a) | none | no donor | the *concept* of case suffixes is Latin's; the shapes are invented |
| C10 | the class marker is **lexical, not productive** (R3) | none | no donor | agglutinative languages are typically productive — ours deliberately is not |

## The dominance check

Counting the rows above (35 sub-areas; a row may name more than one donor):

| donor | rows where it is the closest single donor | share |
|---|---|---|
| **Finnish** | A1, A3(loose), A6(loose), A14, C1, C2(loose), C5(loose) | ~7 (20%) |
| **Latin / IE** | A12(loose), B1, B4, B5, B7 | ~5 (14%) |
| **Turkish** | C1, C2(loose), C5(loose), B6 | ~4 (11%) |
| **Japanese** | C1, C6(loose), B7, B10 | ~4 (11%) |
| **German** | A7, A9(loose) | ~2 (6%) |
| **Polish** | A7, A16(loose) | ~2 (6%) |
| English / Italian / Albanian / Old English / Chinese | A8, A11, A9, A10, A17 | ≤2 each |
| **no donor (original)** | A2, A4, A5, A13, A15, A17, B2, B3, B8, B9, + OBL in B1, C3, C4, C7, C8, C9, C10 | **~17 (≈48%)** |

**Proposed thresholds (the author may reset them):** no single language may be the closest donor in
more than **1/3** of the rows, and the **original share should stay ≥ 1/4**.

**Current result: PASS on both, comfortably.** The top donor is Finnish at ~20%; about **half of the
sub-areas have no donor at all**; and the mechanism that carries the grammar (B2 + B3, the grade and
chord system) is entirely original. Put plainly: this is a pastiche whose *centre* is invented.

**Where the exposure actually is: the SOUND axis — and especially the SPELLING.** Grammar and
word-building are balanced; the sound is where one language (Finnish vowels + a Germanic/English
orthography: `y`, `ae`, `w`, `sh`, `th`, `oi/au`) can take over a listener's or reader's first guess.
The fix is **not** to remove those letters — it is to **break the pattern early**: put the
un-donated material (the `/θ/` + `c` + geminate profile, the `fm`-class clusters, the hiatus leaps,
the area-rule `-f/-w/-h` finals) into the **first example sentences and lyrics**, so that no single
guess sticks. That is a usable instruction for the textbook and for the first verse.

## What this ledger does NOT cover (and who owns each gap)

- **Loanwords — the word level.** A word is only a "loanword" *relative to a meaning*, and coining is
  currently **sound-only** (R3 parked), so **this check cannot run yet**. It must be *specified* now
  and *executed* in the **meaning-assignment step**, which does not exist yet. Sketch to refine:
  **hard reject** = a coined word whose meaning coincides with a natural-language word within one
  edit (*beauty outranks neutrality* does **not** protect these — they would *feel* borrowed);
  **soft warn** = homophony with an unrelated meaning (record it, never reject).
  ⚠️ Unscheduled; it blocks nothing today, but it must not be forgotten when meanings arrive.
- **A statistical sound fingerprint.** This ledger is qualitative. A *measured* profile of the coined
  set (phoneme frequency, syllable shapes, cluster rate, word length) compared against a
  reference-language list would police the one axis where the exposure is real — but it needs one
  input only the author can give: **which languages count as "others"**. Until that list exists there
  is nothing to compare against.
- **Grammatical drift.** Rows B11 and the "not designed yet" decisions (M5, M5a, M4b, M6, M7, rhyme,
  prosody↔melody) are the ledger's *future work*: **each decision must add its rows**, or the balance
  recorded here silently stops being true.


