# 03 — Open Questions / TODO

## 0. OPEN ITEMS — canonical list (start here; everything else in this file is detail)

Last consolidated: after the M4a case table. Sections A–G below hold the history/detail;
**this list is the single place to check what is still pending.**

**A. Small rulings the author should confirm (low stakes, but blocking small things)**
1. **`l` seam row — adopted by necessity.** Because OBL = `-le` exists, the missing M3a row is applied
   as `{f,v}`+`l` → `ll`, `h`+`l` → `l`. *Veto if wrong.*
2. **tier-3 `y` copy.** When the root's last vowel is `y` and tier 3 inserts a copied vowel, does it come
   out as `y` (putting `y` outside a root, against H3) or as `i`?
3. **`NOM = zero suffix`** (the demo implies it; never explicitly confirmed).
4. **One-letter capital rule (H8).** A one-letter vowel word with a capital is read as **VOC**, not as a
   stress mark — confirm.
5. **Emotional vowel table (H8)** is still an *example* list, not a locked one — confirm or revise.

**B. Grammar decisions still open**
6. **M4b — grade labels for the inner/non-role categories** (number, tense, aspect, mood, person).
   **Currently unanswered** (the author deferred it). Sub-question: **is NUMBER suffixed at all?**
7. **M5a — the verb's outermost suffix.** Does tense/aspect/mood decide a verb's chord, or does the
   class/finite ending stay outermost so verbs remain permanently tonic? (M2c makes this unavoidable.)
8. **Negation scope.** `X mei` is *constituent* negation; sentence negation must be defined explicitly so
   "I do not love you" and "it is not you I love" cannot collide. Also outstanding: the **separate
   mechanism for "from" / "towards (go-to)"** the author promised (ABL was dropped in favour of it).
9. **How free is "free" scrambling?** (May the verb move to the middle? May a negator's host move
   independently of it?)
10. **M5 verb morphology, M6 (pronouns? questions?), M7 compounding** — not started.

**C. Documentation / data debt**
11. ~~**Capacity recompute by script** (`05`)~~ — **DONE** (`tools/enumerate_roots.py`, 2026-10-14);
    full findings in `05`'s UPDATE section. In short: `|CC| = 91` is confirmed but is a
    *letter-pattern* count (the syllable reading is 80); the last inconsistency is the `CVV` row
    (60 vs 72 → family total 457,485 vs 457,497, so `R2`'s "461,760" is the rejected `92` family);
    **every count in `05` used a pre-`c`/`j` onset set (13/14)**, so on the locked inventory the
    figures rise 264,600 → 345,600 (single onsets) → **457,425** (clusters allowed, same-day
    ruling A); greedy 16,108 → 20,025 → **26,751**; the 1- and 3-syllable classes are now counted
    (1-syllable bare root: **285** vowel-final / **1,140** with an area-rule final —
    the earlier 1,350 used the *coda* set, which the author's 2026-10-14 ruling excludes; 3-syllable
    `CVCVCV`: 44,286,750 lower bound, clusters allowed). **Still open inside item 11:** `05`
    conclusion 4 — per-segment vs per-feature distance.
12. ~~**`A1` vs `R1`/`05` contradiction**~~ — **RESOLVED (author's ruling, 2026-10-14): they are
    TWO LAYERS, not a contradiction.** A **bare root** may end in `∅` (a vowel) or `f`/`v`/`h`
    (that is `R1`'s area rule) and may **not** end in `m n l r s`; **any word** (every
    suffixed/derived form) may end in `∅`, `f`, `v`, `h` **or** `m n l r s`. So `los` is not a
    legal bare root but `laf` is, and `-ner` / `-ser` are legal because they are *word*-final.
    **Consequences:** M3a stays **load-bearing** (bare roots really do end in `f/v/h`), so items 1
    and 2 above **stay open**; and the bare-root coining rule for the first batch is
    **vowel-final, or `f`/`v`/`h`-final**. `01-phonology.md` §5 now states this explicitly.
13. **Notation edge cases still open** (§C): length on a diphthong, `rr` as a trill, capital on the `ae`
    digraph, multiple capitals in a word, whether stress marks are allowed in the poetry register.
14. **Lexicon is still only 6 items** (`reference/example.md`) → real sentences are impossible, which
    blocks the textbook. Coining rules to obey: R1/R2 shapes, R5-area finals, H3's coining rule
    (never distinguish two morphemes by tonic-vs-subdominant alone), and the identity budget (**23 of 30**
    suffix shapes still free: 7 used). **NEW (2026-10-14, after the area-rule mechanism was pinned):** what do
    the **two siblings of an area-rule pair** mean to each other? The pair differs by **one segment
    only**, so if their meanings are unrelated the lexicon acquires near-minimal pairs *by
    construction* — which is exactly what the distance-`>= 2` guideline exists to avoid (it is
    "soft", and the area rule is "hard", so the collision is deliberate — but the **semantics** of a
    pair: ⏸️ **PARKED BY THE AUTHOR (2026-10-14).** The author's direction is **C — the branches carry
    grammatical meaning** (`00-README.md` **R3**), but the content question was then **explicitly
    dropped**: *"skip this first, drop it as open question"*. So R3 is **decided in shape, OPEN in
    content, and must not be built on**. **Practical consequence for step 3 (important):** provisional
    coinage stays **SOUND-ONLY — assign no pair semantics yet** (exactly what `tools/audition_roots.py`
    does). Two costs already recorded under R3: the class is **lexical, not productive** (it cannot
    behave like an English derivational suffix), and once the content *is* fixed, coining happens
    **in pairs** (1,000–3,000 roots ≈ 500–1,500 bases × 2).

**D. Big areas not started (material now exists for two of them)**
15. **Prosody ↔ melody mapping.** Now has real input: the grade system (H1–H7), the composer/listener
    split, and the rule that a mapping must use **contrast relative to each word's own centre**, never
    absolute colour. **Not started.**
16. **Rhyme (押韻)** — one of the author's stated goals and **still undesigned**. Known tension: if
    suffix vowels are grade-determined, word endings rhyme by rule (mechanical); rhyming on the
    *stressed* vowel (inside the root, hence lexical) is the alternative.
17. **The language has no name yet** (Lomissifil is only the project).

**E. Reserved contingency (decided, not active)**
18. Keep the case grades at **1·2·4**; if future corpus/music work shows too many IV in a clause, the
    one-line fix is **INS → dominant** (yields 1·3·3).

**F. Tooling / process (decided)**
19. **Synthesiser auditioning is REJECTED (author, 2026-10-14) — and it leaves a REAL GAP.**
    `espeak-ng -v fi` output is judged **rough and unneutral** (it forces a Finnish voice onto the
    language), so **no further WAVs are to be generated — this round or in future**. `audio/` is now a
    **frozen historical record**, and `tools/audition_m1.py` / `tools/audition_roots.py` are
    **historical — do not re-run** (see `draft/handoff.md`, tooling section). Consequences:
    (a) **M1's full re-test** ("real suffixed vs prefixed words", §A.2) can **no longer** be done from
    WAVs — it must be done **live** (the author reads / sings the written forms);
    (b) the roots audition's evidence is now the **written list** (`audio/roots-index.txt`), not the
    WAVs — picks go to `lists/picks.md`;
    (c) ⚠️ **a replacement method for judging beauty is OPEN.** Until it exists, **goal i ("beautiful
    to hear") cannot be tested at all**, which arguably makes this the most blocking open item in this
    file. Candidate methods: the author **reads the written forms aloud** (the orthography is 1:1, so
    spelling -> sound needs no engine), a single **hand-picked human speaker**, or **print-only**
    judgement (no audio at all).
20. **`lists/picks.md`** is the hand-written home for audition picks (the `.txt` files must stay
    machine-generated — `lists/00-README.md`). ⚠️ Picks from the existing material are **bare roots
    only**: the **M3a seam** (root-final `f`/`v`/`h` + a case suffix, always *unstressed*) is **not**
    covered by that round, so it stays unjudged by ear.

## A. M1 — affix direction (DECIDED, **PROVISIONAL**)

**M1 = SUFFIXES** (agglutinative, Turkish/Finnish/Japanese style). Recorded as a
**working assumption to build M2–M7 on**, not as a settled fact.

- ⚠️ **The original rationale was circular.** `draft/handoff.md` recommended suffixes
  because they "match the head-final hint" — but that hint *is* P4d, which is itself
  provisional. So M1 has **no independent evidence** yet.
- ⚠️ **Reversal cost is asymmetric.** P4d is cheap to reverse (notation/performance layer
  only — no word form changes); M1 is expensive (M2 order, M3 epenthesis, affix shapes,
  M4–M7, textbook, lexicon cards). Do **not** treat the two as one risk.
- The author explicitly **accepts the risk** of a full rebuild from this point.
- A **"position-neutral affix shape" insurance policy** (morphemes shaped so they work as
  either prefix or suffix) was **considered and rejected** — the author chose to assume
  suffixes rather than pay that design cost.
- **Re-test trigger:** once M2–M5 give enough material to audition real suffixed words
  against prefixed ones. ⚠️ The 2026-10-14 recipe (`espeak-ng -v fi`) is **no longer usable** — the
  engine is rejected (§0 item 19) — so this re-test must now be **live**. Note that a direction
  smoke-test *is* possible with non-semantic sound-strings; it was run — see §A.1/§A.2.

### A.1 RE-TEST EVIDENCE — the M1 audition, run 2026-10-14

Tool: `tools/audition_m1.py` (recipe `espeak-ng -v fi -s 130`) — ⚠️ that engine was **later rejected**
as rough and unneutral (§0 item 19), so the script is now **historical: do not re-run**. The WAVs it
produced are kept in `../audio/` (`01`–`05`). Method: the SAME M4a case morphemes (M3b shape, H3/H4
grade vowels) placed once AFTER the root and once BEFORE it — non-semantic sound-strings.

**STATUS: the author LISTENED on 2026-10-14 and judged it good → §A.2 (M1 stays SUFFIXES).** The
files were `01` suffix chain · `02` prefix chain · `03` an A/B alternation on `seli` · `04` the rhyme
probes · `05` the vowel-initial seam. The two hard facts below are what the script proves *without*
ears:

1. **Prefixing has its own seam, and it is not obviously cheaper.** A prefix is vowel-final (coda
   `∅`) or `V`+`C`, so with a **vowel-initial root** the four vowel-final morphemes break the
   "no adjacent vowels" rule: `niarGonna · siarGonna · moarGonna · loarGonna` are **illegal**; only
   the two `C`-final ones survive (`norarGonna · sorarGonna`). Scale: vowel-initial roots are
   `VCV + VCCV = 21,600 / 345,600` base forms ≈ **6.3%**, but they lose **4 of the 6** case
   morphemes. Suffixing's seam (M3a) is the mirror image: it hits `f/v/h`-final roots (which exist
   only under the word-final area rule) but is **already solved**, with three tiers.
2. **Where the weight sits.** Suffixes keep the root's stress at the front (`seLi-na`) and end in an
   unstressed tail; prefixes push the stressed root later (`na-seLi`). Since rhyme lives at the
   END, that is the axis the ear is judging: a suffix tail carries the rhyme vowel **by rule**; a
   prefix tail carries the root's own vowel (**lexical**).
3. **The rhyme consequence is class-local, not global** (feeds §0 item 16): ACC across classes =
   `seLina · losDoni · Roini · arGonnani` → front roots take `-na`, back roots `-ni`; DAT =
   `seLime · losDomo · Roimo · arGonnamo`. So "suffix vowels make rhyme automatic" holds only
   *within one root class* — which turns the root's class into a **rhyming device**. (Observation,
   not a decision.)

### A.2 SMOKE-TEST RESULT (2026-10-14): **PASSED — M1 stays SUFFIXES**

The author listened to the audition (`tools/audition_m1.py`; the six WAVs in
`/tmp/lomissifil-audition/`) and judged it **good**, so the suffix direction survives its first
perceptual test. ⚠️ **Do not overread the strength:** this is an *early* test on **non-semantic
sound-strings**, so it clears the **direction itself**, not the morphological system that gets built
on it. Section A's own **re-test trigger stands** — once M2–M5 supply enough material, real suffixed
words must be auditioned against real prefixed ones.

Two things that listening did **not** settle, and the author has not commented on either:

- the **prefix-side seam** (`niarGonna · siarGonna · moarGonna · loarGonna` are illegal; §A.1 item 1);
- the **class-local rhyme** (same case does not rhyme across root classes; §A.1 item 3).

> ⚠️ **Caveat added 2026-10-14:** the engine used for this test (`espeak-ng`) was **later rejected** as
> rough and unneutral (§0 item 19). The *direction* verdict is a coarse A/B comparison, which such an
> engine can still carry — but this evidence is **weaker than "PASSED" suggests**, and the **live
> re-test** (§0 item 19a) is what actually settles M1.

## B. Morphology queue (after M1)

- ~~**M2 — morpheme order**~~ — **DECIDED, PRINCIPLE ONLY** (author's choice D): *closer to the
  root = more lexical, farther = more syntactic; agreement/case-like slots last.* The **density**
  (how many slots one word may carry) and the concrete slot inventory are **deferred to the
  syntax phase**. ⚠️ Interacts with §G: if vowel harmony lands on suffixes, the suffix vowel
  becomes predictable and **meaning rides on consonants alone** (~16 distinctive affix
  consonants) — an argument for keeping the slot count low.
- **M3 — vowel-adjacency / epenthesis (⚠️ forced by phonology).** The phonology forbids
  adjacent vowels except the 8 diphthongs and the 4 hiatus pairs, so any affix that
  would create an illegal vowel sequence must be handled: insert an epenthetic
  consonant (which one? `n`? `r`? a glide-like `y`/`w`?), or drop/shorten a vowel.
  This must be decided together with affix shapes.
- **M2b — which suffix carries the word's harmonic function?** — **DECIDED = M2c (author's choice A):
  the outermost (rightmost) suffix decides the word's chord.** Inner suffixes' grade vowels still
  appear, **as redundant cues** (deliberately: they are the answer to the §F sung-intelligibility
  risk). The author's clarification: the colour is **relational** — the contrast between the suffix
  vowel and the **root's last vowel** — so the same suffix vowel can be *tonic* in one word and
  *dominant* in another. In a noun, the outermost slot is the case, so a noun's chord = its case's
  function.
- **M4 — the case inventory: DECIDED + table complete (M4a).** **NOM** I · zero · `lati` / **ACC** V · `n` ·
  `-na` / **GEN** V · `s` · `-sa` / **DAT** IV · `m` · `-me` / **LOC** IV · `n`+`r` · `-ner` / **INS** IV ·
  `s`+`r` · `-ser` / **OBL** IV · `l` · `-le`. Verbs: **V1** I · `r` · `-ri` / **V2** I · `n` · `-ni` (same
  skeleton as ACC — distinguished by grade alone, which H3's coining rule allows). **7 of 30 identities used** (the 6 noun cases + V1`r`; V2 re-uses ACC's `n`). ⚠️ The OBL choice forces the **`l` row of the M3a seam** (`{f,v}`+`l` → `ll`, `h`+`l` → `l`) —
  adopted by necessity. ⚠️ **Grade balance — CORRECTED (author's challenge):** 1·2·4 (I·V·IV), and the
  agent's "OBL is high-frequency" claim is **withdrawn** — with six cases covering the normal roles, the
  else-case is plausibly low-frequency; and the *frequent* cases (NOM/ACC/GEN) already carry the I-vs-V
  contrast. Remaining mild point: an all-oblique line is colour-uniform — possibly fixed by M4b's inner
  suffix grades. **RESERVED CONTINGENCY (author):** keep 1·2·4, but hold **"move INS → dominant"** in
  reserve if future work shows too many IV (one-line change; yields 1·3·3).
- **H8 — VOC & the article by vowel colour: RESOLVED.** The device is a **lone vowel word**: **lowercase
  = article** (`a`/`e`/`o`/`i`/`u`/`ae`/`y`), **initial capital = VOC** (`A`/`E`/`Ae`/`Y`…), and the vowel
  chosen = the **emotion**. Plain ASCII (the agent's "small caps" objection was a misreading —
  withdrawn). A residual rule is needed: **a one-letter word with a capital is read as VOC, not stress.**
  The emotional vowel lives on **its own word**, so it never touches the root's identity or a suffix's
  grade.
- **M5a — the verb's OUTERMOST suffix (⚠️ raised by M2c, needs an answer).** Under M2's ordering
  principle (near root = lexical, far = syntactic) the verb's slots would be *class (inner) → tense /
  aspect / mood (outer)*, so **a verb's chord would be decided by its tense/aspect/mood**, not by the
  verb class the demo fixed as tonic. Consequence: the default-order perfect cadence (I-V-I) only holds
  if the **default narrative form (present/indicative) is assigned tonic**. Option ① embraces this
  (tense colours the chord — future/irrealis = maximum contrast = unresolved, which is musically apt);
  option ② puts the **class/finite ending outermost** so verbs stay permanently tonic (tense then only
  supplies colour inside the word).
- **M4b — grade labels for non-role categories (⚠️ forced).** Every suffix's vowel must come from
  somewhere, so **number, tense, aspect, mood, negation, person** all need a grade label too, even
  though only the outermost suffix is the word's chord (M2c). What principle assigns them?
- **M5 — verb morphology** (tense, aspect, mood, person, …).
- **M6 — pronouns, negation, questions.**
- **M7 — compounding rules** (root order, head direction; and how geminates behave at the new
  word edges the morphology creates — geminates are intervocalic-only, so a suffix/prefix can
  break the environment. `st`'s old VCV-only clause is gone since **P5**: `st` is simply coda
  `s` + onset `t`/`d`).
- **M3 pre-work — the CONSONANT side (⚠️ found while recording §G: this is not only a vowel
  problem).** The word-final **area rule** lets roots end in `f`/`v`/`h`, which are **not in the
  coda set** `m n l r s`. As soon as a suffix follows, that consonant has to fit a **medial**
  pattern:
  - `f`/`v`/`h` + a **vowel-initial** suffix → **fine** (the consonant becomes the onset of the
    next syllable);
  - `f`/`v`/`h` + a **consonant-initial** suffix → `ft`, `fk`, `hs`… are **illegal**; only
    `fm fn hm hn wm wn` exist in the cluster list, so **such roots can only take suffixes that
    begin with `m` or `n`** — a severe, non-obvious constraint, unless a sandhi rule (drop or
    change the final consonant) is added;
  - roots ending in `m n l r s` are safe: coda + any single onset is a legal medial `CC`.
  - ⚠️ **Unresolved contradiction to settle here too:** `01-phonology.md` A1 says the word-final
    set is `m n l r s`, while `R1` and `05` say the word-final `(C)` is `∅ / f / v / h`. They
    cannot both be the full truth.
  - ⚠️ **Scale: this is NOT an edge case.** The word-final area rule means a large share of the
    lexicon (up to half or more) ends in `f`/`v`/`h`, so the seam rule is main-street.
  - ⚠️ **"Just drop the final" is NOT safe.** The area rule deliberately creates pairs such as `X` /
    `Xf` from one base. Dropping the final before a suffix would make those two roots **identical in
    every suffixed form** — the distinction would survive only in the unsuffixed (NOM) form, which
    defeats the purpose of the rule.
  - **ADDRESSED = M3a (decided):** see the M3a row in `00-README.md`. Three tiers: (1) group as a CC
    (`fm fn hm hn wm wn`), (2) else sync (`{f,v}`+`s`→`ss`, `{f,v}`+`r`→`rr`, `h`+`s`→`s`,
    `h`+`r`→`r`), (3) else insert a vowel **copied from the root's last vowel**. ⚠️ Two follow-ups:
    (i) the list has **no `l`** entry — proposed `{f,v}`+`l`→`ll`, `h`+`l`→`l` (pending);
    (ii) if the root's last vowel is `y`, does the copied vowel come out as `y` (putting `y` outside
    a root, against H3) or as `i`?
  - **M3b — suffix shape: DECIDED (author's choice A).** **One syllable `C V (C)`**: onset ∈
    `{m,n,l,r,s}`, then the grade vowel, then an optional coda ∈ `{∅,m,n,l,r,s}` → **identity space
    5 x 6 = 30**. (a) one suffix = one syllable = one note; (b) suffix chains can never break
    phonotactics (a suffix's coda + the next suffix's onset = a legal medial CC); (c) the grade vowel
    is a cue, not extra identity. **30 shapes is the budget for M4–M6.** Still open here: the missing
    `l` seam rules, the `y`-copy question, and `NOM = zero suffix`.

## C. Notation edge cases (need rules)

- ~~Capital in an `st`-initial syllable~~ — **RESOLVED by P5.** No syllable begins with
  `st` any more (`s` is a coda), so the question is moot: `losdo` = `los-do` → `losDo`.
  The general rule stays N1 (capital on the first letter of the stressed syllable).
- ~~Voicing knob inside a cluster~~ — **RESOLVED by P5 + P2.** The knob now only ever
  applies to a **single-consonant onset** or to a **stop+`r`** cluster (`tr`~`dr`);
  `fm fn hm hn wm wn jm jn` contain no stop at all, so nothing is left ambiguous.
- ~~`sd` / `st` conflict~~ — **RESOLVED = P5** (author's choice): `st` is **not** a
  cluster, it is coda `s` + onset `t`/`d`, so `losdo` is plainly legal and the voicing knob
  applies normally. P2 loses the `st` entry; `01-phonology.md` §5/§7 updated. Chosen over
  "`st` is a cluster, permanently voiceless" (which would have made `losdo` illegal, made
  that root **knob-inert**, and required an exception rule for a single cluster).
- ~~`e|u` in `austareus`~~ — **RESOLVED (author chose A):** it is simply the **diphthong
  `eu`** — `austareus` = **`aus-ta-reus`** (3 syllables, **no leap**). The earlier
  `Au-sta-re-us` syllabification was a wrong split added by a previous session; the
  reference file needed no change. Design consequence: the leap (hiatus) stays a
  **4-member set** `iu yu ia ya`, and the reason is now explicit — **a pair that can be
  read as a diphthong (`e|u` and friends) can never be a hiatus**, because the spelling
  could not disambiguate it.
- **Length on a diphthong.** "Repeat the last letter" gives `ai` → `aii`, `aei` →
  `aeii`. Is lengthening a glide even meaningful?
- **Vibrato before a coda.** Marking vibrato on the vowel of `gon` yields `govn…`
  (`arGovnna`), which looks like an illegal cluster though `v` is not a phoneme.
  Where exactly does the `v` go?
- **Multiple capitals in one word.** Compound stress keeps only the last root's stress
  by default, but a composer may want more stresses — is more than one capital allowed?
- **Capital on the `ae` digraph** → `Ae`? (which letter is capitalized?)
- **Poetry register.** May stress marks appear in poetry, or only in lyric notation?

## D. Data / reference action items

1. ~~Citation-form review of `reference/example.md`~~ — **DONE** (`losdo`, `aurorius`,
   `austareus`). Both side effects are settled (the `sd`/`st` clash by **P5**, the `e|u` split as the
   diphthong `eu`). **All six reference words are sound.**
2. **Lexicon seeds.** Only 6 items exist; the reference must grow before real examples,
   poetry or a textbook are possible.

## E. Pending confirmations (currently assumed)

- **A1** word-final consonants = the coda set `m n l r s` — ⚠️ **CONTRADICTED** by `R1`/`05`
  (word-final `(C)` = `∅ / f / v / h`), and M3a's seam rules assume the `f/v/h` finals. **See §0 item 12.**
- **A2** fricative asymmetry kept (only `/v/` is voiced; no `/z ð ʒ/`).
- Punctuation is still used in plain text (only the *performance marks* are letters-only).
- The cluster whitelist is *extensible* per the author ("add any good-sounding one").

## F. Larger areas not started

- **Syntax — OPENED (S2 decided):** free scrambling + a preferred **verb-final default order** (prose
  uses the default → a plain declarative is I-V-I = a perfect cadence; poetry permutes freely).
  Particles stay adjacent to their host (`mei` follows the word it negates). ⚠️ Still open here:
  (i) the **scope of negation** — `X mei` is *constituent* negation, so sentence negation has to negate
  the verb; needs an explicit rule so "I do not love you" and "it is not you that I love" cannot
  collide; (ii) how much scrambling is legal (may the verb move to the middle? may a negator's host
  move independently?).
- **Remaining risk to keep alive:** free order is decodable only if the listener *hears each word's
  case suffix* — and case suffixes are (a) **unstressed**, (b) **one syllable**, (c) frequently **one
  vowel apart** (`-na` / `-ni` / `-no`). In singing, unstressed word-final syllables are where
  intelligibility dies first. Mitigations already available: the grade vowel is a **redundant cue**;
  the consonant shape (`n` / `s` / `m` / `nr` / `sr` / `l`) carries identity; the notation register can mark
  **length** if the composer wants a suffix sustained.

- **Lexicon generation strategy + a neutrality check** (avoid loanwords / not too much like any one
  language) — goal 2 still has **no mechanism**. ⚠️ Only **6 reference words** exist, which now blocks
  the textbook.
- **Prosody ↔ melody mapping** — *material now exists*: the grade system (H1–H7) plus the
  composer/listener split. Hard rule it must respect: map **contrast relative to each word's own
  centre**, never absolute colour.
- **Rhyme (押韻)** — a stated design goal and **still undesigned**; the automatic-rhyme tension
  (grade-determined endings rhyme by rule) is noted in H3/H6.
- ~~An auditioning workflow for real listening~~ — **first attempt DONE, then REJECTED** (author,
  2026-10-14): the `espeak-ng -v fi` recipe works mechanically but sounds rough and **unneutral**, so
  it is **no longer the method** — see §0 item 19 (the replacement is still open).

## G. The vowel-colour ("grade") system — raised by the author

> **⚠️ TERMINOLOGY — read first.** The language has **NO tone/pitch** and **never sounds chords**.
> "tonic / subdominant / dominant" ("I / IV / V") are **metaphors**, borrowed from music theory, for
> three **grammar-level labels** over three relational **vowel-colour** classes. Physically there is
> only: (a) each vowel's **colour** (bright↔dark) and (b) the **contrast** between a suffix's vowel and
> the root's last vowel (operational: same vowel / the class's central vowel / the opposite pole).
> ⚠️ **Consequence that matters:** since the value is *relational*, the **absolute colour of a grade
> flips with the root's class** — "dominant" is dark `a` after a front root but bright `i` after a back
> root. So only the **degree of contrast** is stable; any future prosody↔melody mapping must be built on
> contrast relative to the word's own centre, never on absolute colour. Details + the correction of an
> agent overstatement: `../draft/brainstorm.md` §2 warning block.

Full record: `../draft/brainstorm.md` (marked RAW). Summary:

1. **Divide the vowels into front / back.** *(The division already exists — `01-phonology.md`
   §2 bright/dark palette. The new part is presumably to give it a **grammatical** job.)*
2. **Emphasise rhyme** (押韻).
3. **Vowel harmony / "oppositeness"** — ~~to be explained later~~ → **explained: it is the grade
   system** (see the STATUS block below and `00-README.md` H1–H8).

**STATUS — the *scope* is decided (H1):** harmony applies to **suffixes only; roots stay
internally free** (author's choice A). No locked asset is invalidated (all 8 diphthongs and all
6 reference words survive). Two sub-decisions remain, and both must be answered **before M3**,
because they fix what a suffix's vowel is:

- **(i) allomorph strategy** — two front/back variants per suffix (Finnish/Turkish style), or
  one fixed **"grammar vowel"** shared by all suffixes, or a mix (core grammar suffixes
  harmonic, derivational ones fixed)?
  - ⚠️ **A concrete proposal is on the table (RAW):** THREE grades per suffix,
    **tonic / subdominant / dominant**, inspired by functional harmony — tonic = the same vowel
    as the trigger, subdominant = same group but a different vowel, dominant = the opposite
    group. This gives **suffix = consonant (category) x vowel (grade)** ≈ 16 x 3 ≈ 48 shapes, and
    it **repairs** the "meaning rides on consonants alone" problem. Full write-up + the six
    parameters that must be pinned: `../draft/brainstorm.md` §3. **Not decided.**
- **(ii) trigger vowel** — the root's **last nucleus** (adjacency; the standard), or its
  **stressed** vowel (the melodic peak — musically appealing, but non-standard)? (Also decides
  what happens with a diphthong-final or mixed-vowel root.)
- ⚠️ **The author then explained the full picture** (agent's notes + open items:
  `../draft/brainstorm.md` §4): a **case system borrowed from the Indo-European pattern**, where the
  **consonant** carries the grammatical identity and the **vowel** realises the harmonic grade —
  NOM = I (bare root), ACC/GEN = V, DAT/LOC = IV, verbs = I — so that **word order alone determines
  the chord progression of a clause** (`lati latina latiri` = I-V-I). Consequences to settle:
  (a) ~~whether the grade is **fixed per category** or a **clause-level mode**~~ — **DECIDED = H2:
  bound to the CATEGORY.** Word order alone therefore sets the progression (free word order becomes
  load-bearing), and a clause with no dominant-category word can never end on V (accepted);
  (b) ~~what questions / negation / non-final clauses get~~ — **DECIDED = H5:** a set of freestanding
  **function words assigned the dominant grade (V)**; they take no suffixes, so any clause can end on V
  and a statement can cadence on its tonic verb. This introduces a **second word class** that the
  lexicon must list separately. **Grade audibility — DECIDED = H6:** a particle does **not** sound its
  grade; its shape is fixed and realizing the chord is the composer's job (so the language has two
  tiers: a suffix always exposes a colour-contrast marker, a particle exposes none). **S1 (negation):** the negator **`mei`**
  is **postposed to the word it negates**, so any negative clause automatically contains a V chord
  (mid-clause for constituent negation, final for predicate negation);
  (c) it commits the language to **case marking + free word order** (see §F — syntax not started);
  (d) it collides with the root-final `f`/`v`/`h` rule (see M3 pre-work above).
- **Grade table — pinned since (details `../draft/brainstorm.md` §4c):** `y` **counts as `i`** for the
  grade system (so `y` never appears in suffix vowels — it stays a root-only signature sound), and
  **`dominant` is always one of the two poles `i` / `a`** (front trigger → `a`, back trigger → `i`).
  **Grade table — DECIDED (H3):** subdominant = the class's central vowel **unconditionally**
  (front `e`, back `o`); so for `e`/`o`-final roots the tonic and subdominant vowels **coincide**
  (I/IV is not audibly distinct there — accepted, no grammatical ambiguity). It implies a **coining
  rule: never distinguish two morphemes by tonic-vs-subdominant alone.**
  **Trigger — DECIDED (H4):** the root's **last syllable nucleus** (a diphthong triggers on its
  nucleus, so `roi` → `o`). Identical to the stressed vowel for 1-/2-syllable roots; it only bites
  3-syllable roots (`argonna` → `a`). Chosen partly because it cannot be destabilised by performance
  stress rewriting (P4). **Still unconfirmed: `NOM = zero suffix`.** Remaining open item in §G:
  **case marking + free word order is now a hard requirement** (§F — syntax not started).

**Conflicts to settle when the mechanic is explained** (details in `../draft/brainstorm.md`):

- **Scope matters enormously.** Harmony *inside roots* hits locked assets — under the strictest
  reading 4 of the 8 diphthongs (`ai eu oi aeu`) cross the divide, and `roi`, `aurorius`,
  `austareus` cross with them. Two sub-parameters decide this: (a) does the diphthong's
  **off-glide** count, or only the nucleus? (b) are **`i`/`e` neutral** (Turkish/Finnish
  solution)? With "nucleus only" + "`i`,`e` neutral", **nothing breaks**.
- **Harmony + the voicing knob (C2b)** ⇒ a suffix vowel is predictable ⇒ suffix meaning rides on
  **consonants alone** ⇒ a ~16-consonant effective affix alphabet, i.e. a cap on morphological
  richness.
- **Rhyme may become automatic** (suffix vowels are harmony-determined and sit at word ends) —
  a device that fires by rule can start to feel mechanical; rhyming on the **stressed** vowel
  (inside the root, hence lexical) is the alternative.
- **Harmony vs the leap.** The 4 hiatus leaps (`iu yu ia ya`) jump front-high → extreme-back
  **on purpose**, i.e. they are structurally anti-harmonic. Harmony (unity) and the leap
  (contrast) must be given **different jobs**, not merged.
