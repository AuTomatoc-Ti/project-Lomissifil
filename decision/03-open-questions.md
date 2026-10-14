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
    (c) ✅ **RESOLVED (author, 2026-10-14): the replacement method is the author READING THE WRITTEN
    FORMS ALOUD** (the orthography is 1:1, so spelling -> sound needs no engine). First application:
    `../lists/seam-sheet.md`, the M3a seam sheet (`tools/seam.py`). No synthesiser, ever again.
20. **`lists/picks.md`** is the hand-written home for audition picks (the `.txt` files must stay
    machine-generated — `lists/00-README.md`). ⚠️ The **M3a seam** is not covered by the bare-root
    round — but it now has its own material: ✅ **`../lists/seam-sheet.md`** (`tools/seam.py`), which
    the author reads aloud (item 19c). Two things that tool **verified** while generating it:
    (a) **tier 3 (the copied vowel) NEVER fires** for the current 9 suffixes — all of them start with
    `m n l r s` and tiers 1-2 cover all 15 combinations — so M3a is **fully determined today**, and
    tier 3 is future-proofing for suffixes that do not exist yet;
    (b) ⚠️ **the two alternatives inside one branch collide**: `+f` vs `+w` (and `+h` vs bare) become
    **identical in GEN, INS, OBL and V1** (`thaeumtof` / `thaeumtow` → both `thaeumtossa`), because
    tier 2 syncs `f`/`w` into `ss`/`rr`/`ll` and drops `h`. Cross-branch pairs stay distinct in all 9
    forms. ⇒ the "**at most 2 roots per base**" rule in `picks.md` is a **CORRECTNESS requirement**,
    not a style preference: coining both members of one branch would make the paradigm ambiguous.

**G. NEW — raised by running the first audition material (2026-10-14, needs a ruling)**
21. ~~**`sh` and `ng` are HOMOGRAPHIC and both readings are legal.**~~ — **DECIDED = `P6` (author,
    2026-10-14): fix the reading.** Medial `sh`/`ng` are **always one phoneme** (`/ʃ/`, `/ŋ/`), and a
    wanted **coda `n` + onset `/g/`** sequence **must be written `nk`**. Full row + consequences:
    `00-README.md` P6 (bijective spelling again; `/s/`+`/h/` becomes unspellable; `nk` = coda `n` +
    onset `k`, **not** a cluster; **R-b/R-c amended**; no locked asset affected — none of the six
    reference words contains `sh`/`ng`, and no suffix onset is `h` or `g`, so neither affected
    sequence can ever arise in morphology). **The sub-question that was left open:** is the `k` of `nk`
    **spelling-only** (the soft/hard knob stays free there) or a real **conditioned devoicing**?
    → **SETTLED (author, 2026-10-14): a REAL conditioned devoicing.** `/g/` after a coda `n` is
    obligatorily `[k]`, so C2b's "free and unconditioned" knob is **blocked in that one environment**
    (the language's first genuine phonological process). ⚠️ Its **scope** for `/b/` and `/d/` after a
    nasal coda is the next question (item 25), and it blocks the pool regeneration (item 24).
    ⚠️ **Data consequence (do not miss):** the current pack (`lists/roots-bases-current.txt`) contains
    **no `nk` spelling at all**, so the `/n/`+`/g/` sequences P6 legalises are **absent from the
    candidate pool**, and its 1,071 `ng` strings now all mean `/ŋ/`. Regenerating the pool (the sha in
    `lists/00-README.md` and the sheet's sample both change) is a follow-up — see §0 item 24.
22. ~~**The first coining batch contains NO 1-syllable root — and R1 says 1-syllable roots are
    frequent.**~~ — ✅ **FIXED (2026-10-14, author's ruling ①).** The emitter now enumerates the
    **1-syllable class** (`mono_forms()`; (optional word-initial onset) × nucleus = **285** vowel-final
    bases) and the pack contains **all 285**. Verified: `--stats` shows **1 syllable: 285 (1.1%) /
    2 syllables: 26,484 (98.9%)**, 0 illegal, 0 duplicates; the space becomes **453,511**
    (453,226 + 285) and the script's cross-check says **MATCH**.
    ⚠️ **The mono class is EXEMPT from the pairwise distance ≥ 2 guideline** — and that was measured,
    not assumed: inside the greedy pack only **15 of the 285** survive that rule, because 2-3 letter
    forms differ by one segment almost by definition. R2 calls the guideline *soft* (only the area
    rule is *hard*), so the 2-syllable core keeps its exact ≥ 2 guarantee (26,484, unchanged) and the
    short class is appended. Honest cost: **256 of the 285** have a distance-1 neighbour in the pack
    (all such pairs involve a 1-syllable root). **Author may veto** — the alternative is losing 95% of
    the short roots.
    Consequence for the menu: short roots no longer vanish behind the higher-scoring 2-syllable bases —
    `lists/menu.md` has a dedicated `roi`-class section **and** guarantees one short root inside every
    by-sound group (`--mono N` controls the section size).
23. **New tooling (not a decision):** `tools/syllabify.py` computes the syllable split + default
    stress for any spelling, with `--check` (verified against `se-li` / `los-do` / `roi` /
    `ar-gon-na` / `aus-ta-reus`), `--sheet` (the audition sheet) and `--stats`. It reproduces every
    split the docs state; the one bug it caught was an onset set missing the hard spellings
    `p t k` (needed because `austareus` is C2-exempt).
24. **Pool regeneration after P6** — ✅ **DONE: re-emitted 2026-10-14** (`--pack --config current
    --seeds 4`, run *before* the pick round because the author chose "re-emit first, then pick"):
    **26,484 bases**, sha1 `f532e58e…`, **0 duplicate lines, 0 P6-illegal spellings, 2,142 (8.1%) P6
    hard spellings**, and the sheet was regenerated from it. The count equals the **unique** line count
    of the pre-P6 file (26,751 − 267) — confirming the only real change was de-duplication +
    respelling. What `enumerate_roots.py` does on the P6 configs (and only there: `legacy-*` /
    `singles-*` keep `p6=False`, so they still reproduce `05`'s 48,020 / 220,500 / 264,600):
    (i) a **nasal coda + stop is emitted with the HARD letter** (`mb`→`mp`, `nb`→`np`, `md`→`mt`,
    `nd`→`nt`, `mg`→`mk`, `ng`→`nk`); (ii) the **`/s/` + `/h/` fill is excluded** (no spelling exists);
    (iii) `dist1` uses a distance alphabet that **includes `p t k`**, or a pair differing by `b`~`p`
    after a nasal would still look like distance ≥ 2.
    **Verified:** 453,226 forms = 453,226 distinct spellings (**injective**), 34,200 hard spellings,
    **0 violations**, and the script's own cross-check now says **MATCH** for all five configs (it used
    to print a 4,275 MISMATCH). Space: 457,501 → **453,226**; `|CC|` 80 → 79 (`05`'s P6 UPDATE).
    ⚠️ **A REAL DEFECT FOUND IN THE COMMITTED PACK:** it contains **267 duplicate lines** — two
    different phoneme sequences that shared one spelling (`manga` was both /maŋa/ and /man.ga/), i.e.
    **pairs at distance 0** in a pack that advertises pairwise distance ≥ 2, plus **1,338 (5.0%)**
    P6-illegal spellings. Both vanish on re-emission.
    ⚠️ **Timing — already respected:** the re-emission changed the sheet's 48-base sample, so it was
    run **before** the pick round started, exactly as required. The old numbering is gone;
    `../audio/roots-index.txt` is a separate, **frozen** record of the pre-P6 pool and its numbers do
    not map onto the new sheet.

**H. Neutrality (goal 2) — the donor ledger and its two remaining halves**

The design-level mechanism now exists: **`06-neutrality.md`** (three axes — sound / grammar /
word-building — one row per sub-area, each mapped to its closest single donor or marked *no donor*,
plus a **dominance check**). Result: **PASS** — top donor Finnish at 8/38 rows (21%) inclusive, 4/38
(11%) strict, so **no language comes near the 1/3 ceiling**; **42% of the counted rows have no donor
at all**; and the grammar's centre (the grade/chord system) is entirely original. ⚠️ **Living rule:**
every future decision must add its rows. Two halves are still open:
26. **The loanword mechanism (word level)** — **partially RUNNABLE since 2026-10-14, because the author
    started assigning meanings** (`../reference/example.md` batch 1, 31 roots). Spec: **hard reject** =
    a coined word whose meaning coincides with a natural-language word within one edit distance
    (*beauty outranks neutrality* does **not** protect those — they would *feel* borrowed);
    **soft warn** = homophony with an unrelated meaning (record, never reject).
    ✅ **The English channel has RUN** (`/usr/share/dict/words`, 234,428 entries) on batch 1: 7 of the
    27 roots are literally English words (`aba`, `basto`→`basdo`, `eli`, `ima`, `hu`, `ila`), all with
    *unrelated* meanings ⇒ **soft warnings, kept** (results in `../lists/proposed.md`).
    ⚠️ **Still missing:** the **multilingual** reference word list — the author must name which
    languages count as "others" (the same list the sound fingerprint would use; `06-neutrality.md`
    already names 16 for the *sound* side, but a word list is a different input).
    **Owner:** ongoing — run it whenever a batch of meanings is assigned.
28. **The 5 held words + the deferred `m`/`r` question (author's ruling ③, 2026-10-14).** `R4` legalised
    `s`-final bare roots, which **immediately released `os` (have) and `res` (be)**. Still **held**
    (they need `m`/`r` finals, which stay illegal): **`ar` (from) · `mer` (with) · `esgim` (foot) ·
    `altem` (face) · `sym` (god)** — recorded in `../lists/proposed.md`. Two clean ways to admit them,
    **not yet chosen**:
    (a) **a function-word carve-out** — `H5` already says function words are a **separate class that
    takes NO suffixes**, and the bare-root final rule exists *because* bare roots must host suffixes ⇒
    for a suffixless class the constraint has no purpose. This would admit **`ar` / `mer`** immediately
    and gives `H5`'s class its first two members. (The three nouns cannot use it — they take case
    suffixes.)
    (b) **the `m`/`r` extension** (the earlier options ①/②: add `m`/`r`, or the whole coda set
    `m n l r s`) — deferred by the author, but note it is **mechanically cheap** for the same reason
    `s` was: `m`, `r`, `n`, `l` are all codas (P3), so **no M3a repair** is needed. Its real cost is
    goal i (word-final `m`/`r`/`s` are among the commonest finals world-wide ⇒ the "signature" flavour
    of our endings dilutes). ⚠️ If (b) is ever taken, the **donor ledger** should get a
    "word-final consonants" row updated, and the fingerprint re-measured.
    A third route for the three nouns: a **+vowel respelling** (`esgima`, `aldema`, `syma`), which keeps
    them legal today at the cost of their sound. ✅ **RESOLVED the same day: the author chose the
    extension (`m` + `r`), and `R6` records the class semantics** — the three nouns are now legal (see
    item 29 for the one mechanism `R6` opened).
29. **The ADJECTIVE / ADVERB mechanism `root(+h) + V + s` — NEW, and it needs a ruling before any
    adjective can exist** (author's design, 2026-10-14, tied to `R6`). Their examples:
    `onlah` + `is`/`as`/`es`/`os` → `onlahis` / `onlahas` / `onlahes` / `onlahos`, where **the vowel
    agrees with the case/verb suffix of the word it modifies**. Three collisions, deliberately **not**
    averaged:
    (a) ⚠️ **`M3b` says a suffix is one syllable `C V (C)`, onset ∈ `{m,n,l,r,s}`** — `-V s` is
    **vowel-initial** ✗ ⇒ M3b must be amended, or a separate **derivational-ending** shape class
    created;
    (b) ⚠️ **the no-adjacent-vowels rule** forbids a vowel-initial ending after a vowel-final root —
    which is exactly why the author writes `onla(h)`: **`h` is a BUFFER**. So `R6`'s `h` rule is not
    only a class marker but a **morphological device** ✅ (it also implies: a vowel-final root *must*
    take `h` before `-Vs`, and any later vowel-initial ending will need the same trick);
    (c) ⚠️ **`H2` binds a suffix's grade to its own category**; here the vowel is decided by
    **agreement with another word** ⇒ this is a **new principle** (and arguably the payoff of the whole
    colour system: colour agreement). State it as an explicit exception to H2, or reword H2.
    ⚠️ **Unexamined and unverified:** whether `-Vs` can collide with a case suffix on the same root —
    GEN is `-sa` (`s` + vowel) and the adjective is `-Vs` (vowel + `s`), which *look* distinct, but the
    **`h` buffer plus tier-2 sync** could bring them together (`onlah`+GEN → `onlasa`: compare
    `onla`+`-s`+`a`?). **A mechanical check is needed and does not exist yet.**
    ⚠️ Also open: is `-Vs` an **affix** or a **separate particle** (`H5`-style)? A particle would avoid
    (a) and (b) entirely, at the cost of one more free word per modification.
    ✅ **DECIDED by the author (2026-10-14): the AFFIX `-Vs`.** The draft below is the agent's proposal
    built from their note 1; the two cells marked ⚠️ are what still needs their word.
    **DRAFT — the mechanism, verified legal through `tools/check_roots.py` (`--forms`):**
    *Shape*: adjective/adverb = `root` + **`h`** (only if the root is vowel-final — the buffer) +
    **[agreeing vowel]** + **`s`**. Verified: `onla`→`onlahis/onlahas/onlahes/onlahos` ·
    `hosda`→`hosdahas` · `sym`→`symas` · `esgim`→`esgimis` · `sefmeh`→`sefmehis` — every one passes the
    locked rules. ⚠️ **NOTE (agent error found by that check):** a **1-syllable root keeps its own
    stress** (P4c), so `sym`+`-as` is `SYmas`, not `syMas` — `syllabify.py`'s stress column is only the
    *bare-root* default, and `seam.py` is the tool that counts from the root.
    *The agreeing vowel*: it copies **the vowel of the WORD's outermost suffix that the adjective
    modifies** (the author's note 1), which — because every suffix vowel is a grade relative to its own
    host — yields exactly the author's four vowels:

    | the modified word's outer suffix | its vowel | adjective ending |
    |---|---|---|
    | ACC / GEN (grade V, dominant) | `a` if the host root is front, `i` if back | `-as` / `-is` |
    | DAT / LOC / INS / OBL (grade IV) | `e` if front, `o` if back | `-es` / `-os` |
    | verb V1 / V2 (grade I, tonic) | the verb root's own last vowel (any of the 7) | that vowel + `s` |
    | **NOM (zero suffix)** ⚠️ | **no vowel exists to copy** | ⚠️ **the open cell** — three candidates: (i) copy the modified ROOT's own last vowel, (ii) a fixed default (`e`), (iii) **take no ending at all**, i.e. the `h`-class root itself is the NOM form (this is what `R6`'s `h` rule already implies, and it would explain the author's `onla(h)` notation) |
    | **declension** ⚠️ | — | **A: the adjective never takes a case suffix** (`hosdahas sefmehna`) — short; its chord would be inherited from the host, so a phrase still sounds as one chord. **B: the adjective also takes the case** (`hosdahasna sefmehna`) — the case cue is DOUBLED, which is what the sung-intelligibility risk (§F) wants; the case consonant agrees while the vowel is computed from the adjective's own root |

    ✅ **RESOLVED (author, 2026-10-14): (iii) + B.** The two cells become:
    - **NOM: no ending.** The bare root itself is the adjective's NOM form — so a **vowel-final
      adjective is simply an `h`-class root** (`hosdah` = "certain", `onlah` = "leaving"), which is what
      the author's `onla(h)` notation meant, and it gives `R6`'s `h` rule a grammatical meaning: **the
      `h` class IS the adjective's unagreed form.** A consonant-final root (`sym`) is its own NOM form
      too (`sym` = "divine").
    - **Declension: YES.** The adjective takes the agreement ending **and then the same case suffix as
      its head**: `hosdahasna sefmehna` = "the certain-ACC world-ACC". Consequences: (a) the **case cue
      is doubled** — exactly what the §F sung-intelligibility risk asks for; (b) M2c (outermost suffix
      = the word's chord) makes **the whole noun phrase one chord**: both words carry the same grade
      label, though their vowels may differ when their root classes differ — the **case consonant** is
      what agrees.
    **Implied by this ruling, with proposed defaults (author may veto any):**
    (i) **adjective position = BEFORE its noun** (`hosdah sefmeh`), following the modifier-head /
    head-final tendency of S2/P4d;
    ✅ **REFINED by the author (2026-10-14, same session): the adjective's CASE SUFFIX IS OPTIONAL — a
    KNOB, not a requirement.** In the default order (adjective immediately before its head) the
    adjective carries **only the agreeing ending**, never a case suffix: `orGi hosDahas sefMehna
    thyMAri` = "the heart thinks the certain world". The case suffix appears on the adjective **only
    when the order is mixed** (a poetic scrambling), where it is what lets the listener re-pair the
    words: `sefMehna hosDahasna thyMAri orGi`. Reasons given by the author: case on the adjective is
    **too redundant for poetry and music**. Why this is *better* than plain B: (1) it turns **free word
    order into an economy** — mark only what the order does not already say; (2) it is the **second
    "knob"** in the language, exactly parallel to C2's voicing knob (a canonical dictionary form + a
    free performance variant); (3) the *audible* effect the mechanism exists for (colour agreement) is
    carried by the **vowel**, not by the case consonant, so nothing is lost; (4) its only cost is a
    **local ambiguity** in scrambled orders, which is the poet's own choice. ⚠️ Consequence to keep in
    view: the chord label is *relational to each word's own root* (the standing caveat in `00-README`),
    so a phrase is **audibly** one colour while the analytic labels stay per-word;
    ✅ **SETTLED from the author's own wording: the cased form is REQUIRED when the adjective is
    separated from its head** ("only need adding when sequence is mixed"), and freely available
    otherwise as a stylistic choice (veto allowed);
    (ii) the **lexicon gains a part-of-speech field**, because a NOM adjective and a NOM noun are
    shape-identical — word class is a lexical fact here (as in Latin), not an audible shape;
    (iii) two locked rules are **amended**: **`M3b`** gains a second sanctioned suffix shape —
    the **derivational ending `V s`** (vowel first), because `-sV` would collide with GEN's `-sa`;
    **`H2`** gains an explicit **agreement exception** (the adjective ending's vowel is copied from its
    head, not computed from its own category).

**I. Raised by the FIRST INTEGRATION TEST (2026-10-14) — see `../textbook/01-first-lines.md`**

Five clauses were assembled from the 42-word lexicon and **every form was checked mechanically**. The
test did **not** fail: case marking, the grade/chord progression, the `M3a` seam, adjective agreement
and negation all worked as designed (line 2 lands the signature **I–V–I**; line 5 ends on **V** because
`H5` gives function words the dominant grade). What it exposed is the **shape of what is missing** — a
10-row gap list lives in the textbook file. Most gaps already have owners (`M4b` number = item 6,
`M5a`/tense = item 7, the copula and verb valency = `M5`, pronouns/questions = `M6`, "towards" and
negation scope = item 8). **Two gaps had no owner at all:**
30. **Do FUNCTION WORDS carry a performance STRESS?** `P4` speaks only of *roots*; `H5`/`H6` say a
    particle's grade is a label that is not sounded. So `mei` (one syllable) has **no defined stress** —
    small, but it appears in every negative clause. Options: stress it like a root (the 2nd-syllable
    rule is meaningless for a one-syllable word), never stress it, or leave it to the composer.
31. **There is no CLAUSE-LEVEL tool.** The five lines of the integration test were assembled **by hand**
    and verified word by word; nothing composes a clause, checks its chord progression (`I–V–I`), or
    verifies agreement across words. A `tools/clause.py` would be the natural next tool — and it is what
    would let the author write **hundreds** of demo lines instead of five.
32. **CASE ALIGNMENT (格配列) — never explicitly decided; the design is de facto NOMINATIVE–ACCUSATIVE.**
    Raised by the author 2026-10-14 ("what is our language using? what if we use 南島型?"). **Evidence for the
    status quo:** in `M4a` NOM is the **zero** suffix and ACC is `-na`; the S of an intransitive and the A of a
    transitive both take NOM (`orgi thyMAri` / `orgi sefmehna thyMAri`), and only P takes ACC ⇒ S = A ≠ P =
    **accusative**. Because `M5b` forbids person marking, alignment rides **only on the case suffix** (the
    Japanese profile). ⚠️ **Settling this also settles item 3** (`NOM = zero suffix`), since zero-NOM is what
    *makes* the system accusative.
    ⚠️ **Why it is not a side detail here:** `H2` binds the grade to the category (NOM → tonic I; ACC & GEN →
    dominant V; DAT/LOC/INS/OBL → IV) ⇒ **the I–V–I signature cadence IS the accusative alignment made
    audible.** Changing alignment changes what the signature *means*.
    **Three alternatives, with measured costs:**
    - **(a) Philippine-type / "Austronesian" symmetric voice** (Tagalog: actor / patient / locative voice, a
      **pivot** in the `ang`-case, the non-pivot core argument in the **genitive**, the rest oblique). Our
      *inventory* already fits (pivot = NOM ✓, non-pivot core = GEN ✓, oblique = OBL ✓) and voice affixes are
      affordable (one syllable each; 23 skeletons free per `M4a`) — **but**: (i) the ACC/GEN contrast, the
      commonest I-vs-V pair, would collapse into a single genitive; (ii) the typical Austronesian order is
      **verb-initial**, and since `H2` makes verbs tonic, a verb-initial clause can no longer **end on I** ⇒
      **I–V–I dies**; (iii) if we keep verb-final instead, the listener hears the voice affix *after* both
      nouns ⇒ **retroactive decoding** at song speed (§F). So this option trades the signature cadence for
      the machinery.
    - **(b) Active–stative (split-S)** — also an Austronesian pattern (Acehnese). **Cheapest: zero new
      morphemes.** Intransitive subjects split by the verb's class: an agentive S takes NOM, a
      patientive/stative S takes ACC ⇒ i.e. **`V1` vs `V2` stops being a free-floating class and *becomes*
      the alignment** — which is exactly the choice `reference/example.md` still lists as open ("⚠️ their
      verb class (V1 `-ri` / V2 `-ni`) is not decided yet", for `os` / `res`). Harmonic payoff: a stative
      clause opens on the dominant (the ACC-marked subject) and ends on the tonic verb ⇒ a **V–I** perfect
      cadence *without* the opening tonic.
    - **(c) Ergative** — equally cheap: keep zero for S/P and re-point `-na` from P to A. `H2`'s chord
      mapping survives untouched, and the *meaning of the dominant chord flips*: the **doer** becomes the
      tension (apt for epic / power metal), not the affected thing.
    **Agent's recommendation:** keep NOM-ACC (it *is* the cadence) and take the Austronesian idea in its cheap
    form — (b) to settle `V1`/`V2`, or a **single** patient-promoting suffix (one syllable) if a morphological
    "spotlight any argument" is wanted; note that `S3`'s topic slot plus free order **already provide that
    function pragmatically, at zero cost**. **Author decision needed.**
    ⚠️ **UPDATE (same session): the author's own `V1`/`V2` design — "V1 = there IS an instigator, V2 = there is
    NO instigator" (Georgian-inspired) — is recorded as `M5c`, and it IS this item's option (b) or the safe
    voice reading.** What remains to rule is therefore narrow: **in a V2 clause, does the participant keep NOM
    (plain accusative) or take ACC (split-S)?**
27. ~~**A statistical sound fingerprint**~~ — ✅ **DONE (2026-10-14): `tools/fingerprint.py`**
    (`--profile` / `--similarity` / `--english`), with the reference set **decided** by the author =
    the 10 ledger donors **plus Mandarin, Cantonese, Indonesian/Malay, Māori, Hawaiian and Quechua**
    as the non-donor group. Full results: `06-neutrality.md` → "Measurement (2026-10-14)". Headlines:
    (a) the **closest** matches are **Old English 0.857 and Albanian 0.846** — i.e. the profile reads
    "archaic European" and **no familiar language owns our sound** (German 0.714, Turkish 0.692,
    Finnish 0.643 sit mid-pack); (b) the feared accidental CV-only resemblance is **refuted** —
    Māori 0.143, Hawaiian 0.071, Cantonese 0.267, Mandarin 0.357, with the 26.2% open-syllable rate
    and 25.2% cluster rate as the separating evidence; (c) **143 of 105,936 forms (0.135%) are
    literally English words** (Webster's 2nd, 234,428 entries) — the ~28 recognisable ones are listed
    as a blocklist for the meaning step. ⚠️ The 16 reference vectors are **hand-coded**, not corpus
    data: audit or correct them in `tools/fingerprint.py` (`REF`).
25. ~~**Scope of the P6 devoicing**~~ — **DECIDED (author, 2026-10-14): the full natural class.**
    Any stop `/b d g/` after a **nasal coda** `/m/` or `/n/` is obligatorily `[p t k]`, and **the
    spelling shows it**: `mb`→`mp`, `nb`→`np`, `md`→`mt`, `nd`→`nt`, `mg`→`mk`, `ng`→`nk`. Chosen over
    the `/g/`-only reading because it is consistent and teachable, and because it keeps R-c's promise
    that the spelling always predicts the sound. **Cost, measured and accepted:** the composer loses the
    hard/soft knob in those **6 of the 90 medial (coda × onset) combinations (~7%)** — and nasal + stop
    is a *frequent* cluster, so the main genre control (power-metal hard vs post-rock soft) is weaker
    exactly there. **Effect on the pool (item 24):** the *voiced* spellings `mb nb md nd mg` are now
    **illegal for coining**, and `/n/`+`/g/` gains `nk` — so regeneration both respells and **enlarges**
    the candidate space: a string like `manga` was previously doing double duty for /maŋa/ and /man.ga/,
    and after P6 those are **two** bases (`manga`, `manka`).

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
  language) — ~~goal 2 has no mechanism~~ → **the design-level mechanism now EXISTS (2026-10-14):
  `06-neutrality.md`, the donor ledger** (three axes — sound / grammar / word-building — one row per
  sub-area, + a dominance check; result: PASS — top donor Finnish 8/38 rows inclusive / 4/38 strict,
  **42% of the rows have no donor**). Two halves remain open and are listed as §0 items 26–27: **loanwords** (needs meanings;
  spec written, execution scheduled) and a **statistical sound fingerprint** (needs the author's
  reference-language list). ⚠️ Only **6 reference words** exist, which still blocks the textbook.
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
