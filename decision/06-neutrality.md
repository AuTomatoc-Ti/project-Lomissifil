# 06 — Neutrality: the donor ledger

Goal 2 (`.clinerules/colang.md`): *"the language should be neutral (can be inspired from different
languages), but must ensure its word and grammar not like other language too much (avoid loan words
from other language)"*.

Until 2026-10-14 this goal had **no mechanism at all** — only the goal statement (`draft/handoff.md`,
`03-open-questions.md` §F). This file is that mechanism, in the form the author asked for: measure
**not only the sound, but also the grammar and the word-building**.

## What this document is (and how it is used)

1. **A ledger.** Every designed sub-area, on three axes — **A. Sound** (18 rows), **B. Grammar**
   (11 rows), **C. Word-building** (10 rows) = **39 rows** — gets one row: what WE decided, which
   single natural language is the *closest* donor (if any), how strong that resemblance is, and where
   it is recorded.
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
| B10 | no gender, no **grammatical** agreement | English-ish / Japanese-ish | same pattern | not distinctive. ⚠️ **UPDATED 2026-10-14 (item 29):** the language now HAS agreement — but of a kind no reference language has: an **adjective copies the vowel of its head's outermost suffix** (colour agreement). Gender/number agreement is still absent |
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
| C11 | the **agreeing adjective ending** `-Vs` (item 29, author's design 2026-10-14) | Latin / Slavic | loose | inflectional **agreement** has donors everywhere in IE; what does **not** is agreement in **vowel COLOUR (grade)** — the mechanism borrows the *idea* of agreement and the *payload* is entirely ours (`H3`). ⚠️ This is also the row where the B and C axes interact most: a suffix whose vowel comes from **outside its own word** |
| B12 | **information structure / topic** (raised by the author 2026-10-14, not yet designed) | — | — | ⚠️ **The author's point is measured and correct:** the B axis's donors are 3 rows of Latin/IE + 1 Turkish (`B1`, `B4`, `B5`), so the clause axis IS IE-heavy. Their proposal: make the language **topic-prominent**. Finding to weigh: "topic-driven order + pro-drop + case marking" is **exactly Russian/Slavic** — which is *already* the B4 donor — so full topic-prominence would **strengthen an existing donor** rather than add a no-donor subsystem. What would be genuinely un-donated: (a) topic-prominence **as a structural type** (no IE language is one, though Slavic *uses* topic-comment), and (b) **H8's emotion-vowel article doubling as the topic marker** (zero new morphemes, no donor). ⚠️ **CORRECTED the same session (the author challenged the agent, and was right): subject OMISSION IS ALREADY LEGAL.** `S2` calls the verb-final NOM-ACC-V order a "**PREFERRED** default", not a requirement; no rule requires an explicit subject; and with **no agreement** nothing forces one. So `sefMehna thyMAri` ("…thinks the world") is a legal clause **today** — the language is **already pro-drop / topic-friendly by construction**, which is exactly the Finnish situation the author pointed at (case marking + free order + no agreement ⇒ omission resolved by inference). ⇒ what a full topic-prominence move would actually *add* is much smaller than first claimed: (i) the **convention** that the leading slot is the topic, (ii) the optional **marker**. ⚠️ The remaining gap is **convention, not permission**: what an omitted argument refers to (proposal: the previous clause's topic/subject) — it must be written down before the textbook can teach it |

## The dominance check

**Counted rows: 38** (39 sub-areas minus **B11**, which is not designed yet). The rules of the count
are stated so it can be audited:

- **donor row** = at least one natural language is named as its closest donor (**19** rows:
  A1 A3 A6 A7 A8 A9 A10 A11 A12 A14 A16 B1 B4 B5 B6 C1 C2 C5 C6);
- **single-donor row** = exactly one language is the *closest* (**9** of those: A1 A3 A6 A10 A11 A14
  A16 B6 C6) — the other 10 are ties;
- **universal row** = no single donor because the pattern is too widespread to be one (**3**:
  A18 B7 B10);
- **no-donor row** = original; nothing in the reference set does this (**16**:
  A2 A4 A5 A13 A15 A17 B2 B3 B8 B9 C3 C4 C7 C8 C9 C10).

| donor | rows where it is one of the closest donors | share of 38 |
|---|---|---|
| **Finnish** | A1 A3 A6 A9 A14 C1 C2 C5 | 8 (21%) |
| **Latin / IE** | A12 B1 B4 B5 | 4 (11%) |
| **Turkish** | B6 C1 C2 C5 | 4 (11%) |
| **Japanese** | A11 C1 C6 | 3 (8%) |
| **Italian** | A9 A11 A12 | 3 (8%) |
| **Polish** | A7 A9 A16 | 3 (8%) |
| **German** | A7 A9 | 2 (5%) |
| English · Albanian · Old English | A8 · A8 · A10 | ≤1 each |
| **no donor (original)** | the 16 rows above | **16 (42%)** |
| **no single donor (universal)** | the 3 rows above | 3 (8%) |

**Strict reading (only the single closest donor per row counts): the maximum is Finnish at 4/38
(≈11%)**, and **9 rows have a unique closest donor at all**.

**Proposed thresholds (the author may reset them):** no single language may be one of the closest
donors in more than **1/3** of the rows, and the **original share should stay ≥ 1/4**.

**Current result: PASS, comfortably, on every reading.** Top donor Finnish at 8/38 (21%) inclusive or
4/38 (11%) strict; the original share is **42%**; and the mechanism that carries the grammar
(B2 + B3, the grade and chord system) is entirely original. Put plainly: this is a pastiche whose
*centre* is invented.

**Where the exposure actually is: the SOUND axis — and especially the SPELLING.** Grammar and
word-building are balanced; the sound is where one language (Finnish vowels + a Germanic/English
orthography: `y`, `ae`, `w`, `sh`, `th`, `oi/au`) can take over a listener's or reader's first guess.
The fix is **not** to remove those letters — it is to **break the pattern early**: put the
un-donated material (the `/θ/` + `c` + geminate profile, the `fm`-class clusters, the hiatus leaps,
the area-rule `-f/-w/-h` finals) into the **first example sentences and lyrics**, so that no single
guess sticks. That is a usable instruction for the textbook and for the first verse.

## Measurement (2026-10-14): the sound axis, checked — `tools/fingerprint.py`

The ledger above is qualitative. This section is the **measured** half, produced by
`python3 tools/fingerprint.py --profile | --similarity | --english` on
`lists/roots-bases-current.txt` (all **five** area-rule sibling forms per base — `+f`, `+w`, `+h`,
`+s`, bare — i.e. 133,845 forms, re-measured after **R4** added the `s` branch).

### The reference set (author's ruling, 2026-10-14)

- **donors (10):** Finnish · Turkish · Japanese · German · Polish · Latin · Italian · English ·
  Albanian · Old English
- **non-donors (6), the "did we accidentally land near something we never borrowed from?" set:**
  **Mandarin (pinyin) · Cantonese (Jyutping)** · Indonesian/Malay · Māori · Hawaiian · Quechua

### Measured structural profile (no external data involved)

| measure | value (5 forms per base, **after R4**) | reads as |
|---|---|---|
| mean length | **7.43** letters | long-ish (the area-rule finals add a letter) |
| vowel letters | **46.4%** | vowel-rich (Romance-ish; English ≈ 39%) |
| syllables per word | 98.9% two, 1.1% one | the pool is the 2-syllable core + the 285 short roots (§0 item 22, closed) |
| **open-syllable rate** | **23.7%** (closed 76.3%) | **low** — decisively not a CV-only language |
| forms containing an onset cluster | **25.1%** | clusters are a *mainstream* feature here, not a garnish |
| word-final | **60.0% `f`/`w`/`h`**, **20.0% `s`** (R4), 20.0% vowel | the area rule dominates word endings; R4 added the `s` slice |
| digraph spelling (`sh`/`th`/`ng`) | **23.9%** | a quarter of all candidates |
| P6 hard spelling (`mp np mt nt mk nk`) | **8.0%** | matches the 6-of-90-fills estimate |
| inventory actually used | onsets **30** · nuclei **15/15** · codas **5/5** (+`f/w/h` finals) | nothing in the locked palette is starved; `k`/`p`/`t` appear **only** as P6 hard spellings |

### Similarity to the 16 reference languages (Jaccard over 15 typological features)

Order: `Old English 0.857 > Albanian 0.846` (both above mean+1sd) `> German 0.714 > Turkish 0.692 >
Finnish 0.643 > English · Indonesian · Italian · Polish · Quechua 0.615 > Latin 0.571 > Japanese 0.400
> Mandarin 0.357 > Cantonese 0.267 > Māori 0.143 > Hawaiian 0.071` (mean 0.540, sd 0.223).

Three things follow, and the first one is the surprise:

1. **The fingerprint and the ledger measure DIFFERENT things, and disagree on purpose.** The ledger
   weighs *anatomy* (where the vowel system, the agglutination and the case inventory came from) and
   names Finnish/Turkish/Latin. The fingerprint weighs the **phonological + spelling profile** and
   names **Old English and Albanian** — both of which the ledger lists as *minor* donors at best.
   Neither is wrong; together they say: *we borrowed our machinery from Finnish/Turkish/Latin, but we
   SOUND like an archaic European language.* For a fantasy project that is the **good** outcome: the
   closest match is a **dead or unfamiliar** language, not a recognisable one — nobody hears a song
   and says "that is Albanian". The recognisable donors (German 0.714, Turkish 0.692, Finnish 0.643)
   sit mid-pack, i.e. no *familiar* language owns our sound.
2. **The accidental-resemblance fear about CV-only languages is REFUTED by measurement.** The worry
   was that our vowel-rich, `ng`/`sh`/`ae` spelling would read as Japanese-romanisation / Indonesian.
   Measured: **Māori 0.143 · Hawaiian 0.071 · Cantonese 0.267 · Mandarin 0.357** — the four lowest in
   the set. The **26.2% open-syllable rate and 25.2% cluster rate** are what separate us: they are
   impossible for a CV-only language. Only **Indonesian (0.615)** sits mid-pack (it shares word-final
   consonants, initial clusters and agglutination) — a mild flag, not a dominance.
3. **"Distinctive matches" are the actionable column** (a Jaccard number compresses because many
   features are shared by almost everyone): we match Old English on `y` + `/θ/` + geminates + initial
   clusters + case marking; Albanian on `y` + `/θ/` + initial clusters + case; Finnish/Turkish on `y` +
   geminates + case + agglutination. Those are exactly the ledger's A1/A2/C1/M1/M4 rows — the two
   instruments agree about **which** levers create the resemblance, and disagree only about which
   language is "closest".

### Coincidence with a real English dictionary (`/usr/share/dict/words`, 234,428 entries)

- **exact matches: 421 of 133,845 (0.315%)** — ⚠️ **this more than DOUBLED when `R4` added the `s`
  branch** (before R4: 143 of 105,936 = 0.135%), because `+s` produces many plural-looking strings.
  That is a **measurable neutrality cost of R4** and worth remembering if the `m`/`r` extension is ever
  considered (§0 item 28). Most hits are archaic/technical because Webster's 2nd
  is huge (`aba`, `agrah`, `branta`, `brolga`, `cothy`, `cumshaw`, `gade`, `galga`, `inro`, `lemna`,
  `mabi`, `nummi`, `rompu`, `thonga`…). The ones that a listener would actually recognise as English
  words — `age · bounce · carry · dine · dome · elbow · fishy · follow · geisha · granny · grassy ·
  holly · horse · hurrah · lady · louse · lube · male · mainly · mana · more · none · ode · only ·
  onto · rude · silly · wince` — are worth a **blocklist** when meanings are assigned (per the
  precedence rule: a collision with a *different* meaning is a soft warning; the same meaning is a
  hard reject — §0 item 26).
- **1-substitution: 3.38% vs a 0.72% same-length random baseline.** ⚠️ **Do not overread this ratio:**
  the uniform-letter baseline is a **weak null** (any vowel-rich string beats it), so 3.38% only says
  "our strings are word-like, not letter-soup". The number to act on is the exact list above.

### This measurement ranks the coining menu

`tools/menu.py` (output: `lists/menu.md`) orders the candidate pool by exactly the un-donated
features this section measured: **+2** for an area-rule final (A15), an `fm`-class cluster (A13) or a
hiatus leap (A4), **+1** for an onset cluster (A12), and **−2** if the form is a real English word.
So the shortlist the author browses is biased toward material that no reference language has — the
measurement is not just a report, it is the menu's ranking function (`score()` in the tool).

### Caveats that must travel with these numbers

- the 16 reference vectors are **hand-coded** from well-known typology, not corpus data; a wrong cell
  changes only that language's score, and the table is deliberately compact so the author can audit
  and correct it (`tools/fingerprint.py`, `REF`);
- Jaccard over booleans is a **coarse** similarity; the *distinctive matches* list is the substantive
  output;
- the English dictionary is a **spelling** test, not a sound test (our orthography ≠ IPA);
- this checks **sound + spelling only** — the word-level loanword question still belongs to §0
  item 26 and needs meanings.


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


