# Name
- aurorius
- austareus


# bare root
- seli (birth)
- losdo (happy)
- roi (day)
- argonna (love)

# NOTE (2026-10-14): entries below are NOUNS unless their gloss says otherwise. `os` / `res` are
# VERB-related (R6), `ar` / `mer` / `mei` are FUNCTION WORDS (R5). An **adjective** has no audible
# shape of its own in NOM (item 29): a vowel-final adjective is coined as an **`h`-class root**
# (`hosda`→`hosdah` "certain") and takes the agreeing `-Vs` ending when it modifies a case-marked
# head (`hosdahas sefmehna`). ⚠️ The case suffix on the adjective is a KNOB (author's refinement,
# 2026-10-14): it is NOT written in the default order and is added only when the order is mixed
# (`hosdahasna sefmehna`), where it re-links the adjective to its noun. So a lexicon entry needs a
# PART OF SPEECH, and this file should grow one.

# function word (class: takes NO suffixes — R5; shape = A1's "any word" layer)
- ar (from) — ⚠️ **`ar` stands IN FRONT of the noun: `ar X` = "from X"** (the R5 mechanism that replaced
  ABL). ✅ **The "is this a one-off?" question was RULED the same day (2026-10-15, `S5`): relational
  function words PREPOSE, operators POSTPOSE** — so `ar` is not an exception but the pattern's first
  instance (the old "postposed by default" note in this file was wrong and is withdrawn).
- mer (with) — ⚠️ **PREPOSED (`S5`): `mer X` = "with X"** — relational, so it stands in FRONT of its host
  (`ar` · `mer` · a future `towards`), while **operator** words stand AFTER (`mei`, and any future
  tense/aspect particle). (A NUMBER word was considered for `M4b` on 2026-10-15 and then **dropped in the
  same session** — number is zero-marked; see `../docs/decisions/00-README.md` `M4b`.)
- mei (not; negator — postposed to what it negates, S1)

# bare root — batch 2 (released by R4 / R5 / R6, 2026-10-14)
- esgim (foot) — R6: `-m` for a front non-open vowel (i / e / y) ✓ this root ends in `i`
- aldem (face) — author wrote `altem`; voiced per C2 (R-b). R6: `-m` ✓ ends in `e`
- sym (god) — R6: `-m` ✓ ends in `y`; stays ONE syllable (a chant word)
- os (have) — R6: an `-s` root for a 1-syllable VERB-related word
- res (be) — same class as `os` (1-syllable, verb-related). ⚠️ the old note said their verb class
  (V1 `-ri` / V2 `-ni`) "is not decided yet" — **the shape of the answer is RULED (2026-10-15)**:
  V1 = "there IS an instigator", V2 = "there is NO instigator", so V1/V2 are two forms of the SAME
  root (a mediopassive alternation), not classes a root belongs to — and the bare root (`V0`) is the
  unmarked form whose reading comes from the **PARTICIPANT'S CASE** (NOM ⇒ implied V1, ACC ⇒ implied
  V2), which is what makes `V1`/`V2` optional. **RULED 2026-10-15 — the two roots differ after all:**
  `res` (be) is **class II** (`orGina res` / `orGina Resne` = "the heart is"; `orGina Symme res` =
  "the heart is to god" = DAT possession), while `os` (have) is **class I** (two participants ⇒ the
  agentive side): `orGi sefMehna os` = "the heart has the world", and **`Osno` (the V2 form of `os`)
  is not a legal use**. See the class section at the bottom of this file. The alignment is
  **active–stative (split-S)**: NOM (zero suffix) = the agent-like case (AG), ACC (`n` + dominant) =
  the patient-like case (PT). Verified forms: `orgi` / `orgina` / `res` / `resne` / `os` / `osro`;
  contrast the `V1` clause `orGi thyMara` ("the heart thinks" = heart-AG + think-V1). Checked with
  `../tools/check_roots.py` and `../tools/clause.py` (`--selftest`).

# bare root — batch 1 (author's own roots, 2026-10-14; checked by `../tools/check_roots.py`)
# ⚠️ Spelling follows C2/R-b: the DICTIONARY form uses the VOICED stop, so a hard realisation is
# written `basdo` here and may still be sung `basto` (the voicing knob). Glosses are PROVISIONAL
# until the loanword check runs (docs/decisions/03-open-questions.md §0 item 26).
- aba (seed)
- asdo (knowledge)
- basdo (—; author wrote `basto`, voiced per C2)
- cou (autumn)
- eli (life)
- esa (the all)
- ima (present / now) — ⚠️ **TIME is expressed with this word, because the language has NO TENSE** (ruled
  2026-10-15, `M5a`). Use it as a **MODIFIER** (`H9` / item 29: `root(+h) + V + s`, head-coloured ⇒
  `iMahes` before a front head, `iMahos` before a back one) and let **POSITION set its scope**:
  `ima Noun Verb` (or `Noun ima Verb`) — and the author's **default is clause-initial ⇒ it frames the
  whole sentence** (e.g. `imahes orGi sefMehna thyMAra` = IV–I–V–I). ⚠️ The vowel comes from the head's
  ROOT CLASS (`H9` / `H4`: front ⇒ `-hes`, back ⇒ `-hos`) and **the head is the word immediately after the
  modifier** (`item 29`: a modifier stands directly before its head) — so here the head is `orgi` (front)
  ⇒ `-hes`, while the *sentence-scope* reading is a pragmatic default laid on top of that syntax. This
  also **closes §0 item 34** (a NOM head is no exception: the head's root class decides). ⚠️ **GAP:** `ima` is the ONLY time
  word — past/future need words (§0 item 6), unless perfective aspect carries "already happened".
- foih (ice)
- fumi (flower)
- hu (wind)
- hosda (certain)
- boih (—; author wrote `poih`, voiced per C2)
- bosga (place; author wrote `posga`, voiced per C2)
- ila (the stop)
- onla (the leave)
- orgi (heart)
- noih (emptiness)
- sefmeh (world)
- sinkoi (solitude) — author's choice 2026-10-14: /sin.goi/, so the spelling MUST be `sinkoi`
  (P6: `ng` is one phoneme /N/; `singoi` would read /si.ŋoi/)
- desa (the making; author wrote `tesa`, voiced per C2)
- thyma (think)
- walu (wood)
- winah (eye)
- hinah (ear)
- brega (—)
- drera (thunder)
- gridi (the promise)

# class & POS — RULED 2026-10-15 (the ruling is logged in `../../docs/decisions/00-README.md`)
# Format: `- root | pos | class | verb sense`, read by `../../tools/clause.py`
# (`pos` = n / v / adj; `class` = I / II / D / II*; `-` in the sense column = no verb sense recorded).
#   I   agentive   — there IS an instigator (a willed act / making / perception / speech)
#   II  patientive — there is NONE (a state, a property, a natural process)
#   D   dual       — BOTH framings are natural (a causative / anticausative pair): never warned
#   II*            — no verb sense yet -> the NOUN DEFAULT "be / become N": never warned
# The class is ADVISORY: it is the natural reading a checker warns against, never a hard rule. And a
# `V0` (bare) clause reads its agentivity OFF THE PARTICIPANT'S CASE (NOM ⇒ implied V1, ACC ⇒ V2),
# which is what makes `V1`/`V2` optional rather than required.
# ⚠️ Still PROPOSALS awaiting the author's veto (`../../data/hand/class-proposal.md`): the classes of
# `argonna` (I), `onla` (I), `roi` (II), `asdo` (II), `eli` (II), `noih` (II). Everything else is ruled.
- aba | n | D | sprout (intr.) / sow (tr.)
- aldem | n | II* | -
- argonna | n | I | to love
- asdo | n | II | to know
- basdo | n | II* | -
- boih | n | II* | -
- bosga | n | II* | -
- brega | n | II* | -
- cou | n | II* | -
- desa | n | I | to make
- drera | n | II | to thunder
- eli | n | II | to live
- esa | n | II* | -
- esgim | n | II* | -
- foih | n | II | to freeze
- fumi | n | II | to bloom
- gridi | n | D | be promised / promise
- hinah | n | II* | -
- hosda | adj | II | to be certain
- hu | n | II | to blow (of wind)
- ila | n | D | stop (intr.) / stop (tr.)
- ima | n | II* | -
- losdo | adj | II | to be happy
- noih | n | II | to be empty
- onla | n | I | to leave
- orgi | n | II* | -
- os | v | I | to have
- res | v | II | to be
- roi | n | II | to dawn
- sefmeh | n | II* | -
- seli | n | D | be born / give birth
- sinkoi | n | II | to be alone
- sym | n | II* | -
- thyma | v | I | to think
- walu | n | II* | -
- winah | n | II* | -

