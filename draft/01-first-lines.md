# draft/01-first-lines.md — the first lines (integration test, 2026-10-14)

**What this is.** The first *integrated* test of the locked layers: NOM/ACC case marking (`M4a`), the
grade/chord system (`H1`–`H8`), the `M3a` seam, the `M2b`/`M2c` suffix rules, adjective agreement
(item 29), the topic slot (`S3`) and negation (`S1`). Every clause below uses **only** words from
`../reference/example.md` (the project's rule), and **every FORM was checked mechanically** with
`python3 ../tools/check_roots.py --forms …` — all of them pass the locked rules (none needed a repair
except the seam, which is by design).

⚠️ **Stress is counted from the ROOT** (`P4c`), so a suffix never steals it and a **one-syllable root
keeps its own stress**. The checker prints the *bare-root* default and says so; the marks below are the
root-based ones (`sefmehna` → `sefMehna`, `res`+`-ri` → `Resri`).

## Line 1 — the minimal clause (chord I–I)

    orGi thyMAra
    heart think-V1
    "the heart thinks"

| word | syllables | how it is built |
|---|---|---|
| `orgi` (heart) | or-gi | **NOM = zero suffix** (`M4a`) |
| `thymara` | thy-ma-ri | **V1** = `r` + the grade vowel. The trigger is the root's **last syllable** nucleus: `thyma` = `thy-ma` ⇒ **`a`** (back) ⇒ tonic = `a` ⇒ **`ra`**. ⚠️ An earlier version of this file read the trigger as the `y`; **the author caught the error (2026-10-14)**. The surface vowel changed; the chord did **not** (V1 is tonic = I either way). |

Chords: NOM = **I**, V1 = **I** ⇒ **I–I**. `H2` predicts that a clause with **no dominant-category
word cannot half-cadence** — this line is exactly that case, and it is musically apt: "the heart
thinks" does not resolve anywhere.

## Line 2 — the design's signature cadence (I–V–I)

    orGi sefMehna thyMAra
    heart world-ACC think-V1
    "the heart thinks the world"

| form | syllables | what happens |
|---|---|---|
| `sefmehna` | se-fme-**hna** | **the `M3a` seam, tier 1**: `sefmeh` (an `h`-final root) + `-na` ⇒ the `hn` **VCV cluster**: the two consonants become ONE onset — no repair, no extra vowel |
| `thymara` | thy-ma-ri | V1, tonic, as above |

Chords: I → **V** (ACC = dominant) → I ⇒ **I–V–I, the perfect cadence** the whole design was aimed at
(`S2` + `H2`). Note the stress: `orGi` · `sefMehna` · `thyMAra` — the root's syllable always wins.

## Line 3 — an adjective, default order (a modifier is IV: the pre-dominant)

    orGi hosDahes sefMehna thyMAra
    heart certain-MOD world-ACC think-V1
    "the heart thinks the certain world"

Chords: NOM **I** + modifier **IV** + ACC **V** + V1 **I** ⇒ **I–IV–V–I** — the complete classical progression, reached by adding one adjective (`H9`). (Line 2, without the adjective, was a bare **I–V–I**.)

- `hosdah` is a **vowel-final adjective**, so it is coined as an **`h`-class root** (`hosda` → `hosdah`,
  `R6`); in NOM it would simply be `hosdah`, with no ending at all (item 29, cell (iii)).
- ⚠️ **CLARIFIED by the author (2026-10-14): POSITION decides — not case marking, and not clause order.** A modifier (adjective *or* adverb) standing **immediately before its head** needs **no CASE ending**, in any clause order (SVO / SOV / scrambled), and in a **chain** (`adj1-adj2-N`) neither modifier needs a case suffix (the `-s` ending is still there). So the ending here is **`hosDahes`**: the `-s` is ALWAYS there, and its vowel is the **subdominant** of the head's class (`sefmeh` is front ⇒ `e`), i.e. a modifier is always **IV** (`H9`). What is positional is the **CASE** suffix.
- The modifier ending (`-V s`, its vowel the head's class subdominant's outermost suffix) is **always present**; the **case suffix** appears only when the modifier is **displaced** from its head — and there it may also take the **case suffix** (`hosDahasna sefMehna`), which is exactly Line 4's job. The rule is therefore **local adjacency**, not a global order type.
- ✅ **`H9` also closes item 34:** because `V` is no longer copied from the head's *suffix* vowel, a **NOM** head is no problem (`hosDahes orGi` = "the certain heart") — only the head's front/back class matters. ⚠️ Micro-choice: taken from the head's **root** (recommended, `H4`) or from its whole word (item 34).

## Line 4 — the same content, scrambled (the displaced modifier)

    sefMehna hosDahesna thyMAra orGi
    world-ACC certain-MOD-ACC think-V1 heart

Chords: **V–V–I–I** — `M2c` says the **outermost** suffix sounds a word's chord, so once the displaced modifier also takes its CASE suffix its chord is the case's (**V** for ACC), not its own IV.
    "the world — the certain one — the heart thinks" (the same statement, poetically re-ordered)

Both the noun and the adjective now carry ACC, so the listener can **re-pair** them across the scramble.
This is the author's own pattern `a b-na A B-na`: marking appears exactly where the order stops carrying
the information. ⚠️ Cost, stated honestly: in a heavily scrambled line the pairing can stay locally
ambiguous — that is the poet's choice, not a defect.

## Line 5 — negation (chord I–I–V, deliberately unresolved)

    orGi thyMAra mei
    heart think-V1 not
    "the heart does not think"

`mei` is **postposed to what it negates** (`S1`). `H5` gives function words the **dominant** grade, so a
negative clause always **ends on V** — it cannot sound finished, which is exactly what negation means
musically. (Whether a *function word* carries a performance stress at all is **undefined** — see gap 9.)

## Line 6 — the topic slot (`S3`) and the absent person (`M5b`), ruled 2026-10-14

    a orGi sefMehna thyMAra
    (article, colour `a`) heart world-ACC think-V1
    "as for the heart — it thinks the world" (colour `a` = brave / energetic / angry)

`H8`'s emotion-vowel article doubles as an **optional topic marker**: it costs no new morpheme, and the
colour it carries shades the whole clause. The topic **keeps its case** (NOM here) — we deliberately do
not copy the Japanese behaviour where the topic particle *replaces* the case, because the case suffix is
our only decoder (§F).

Two things this line shows about what is **not** needed:

- a **subjectless** clause such as `sefMehna thyMAra` ("…thinks the world") was **always legal** —
  `S2`'s verb-final order is a *preferred* default, not a requirement, and with no verb agreement
  nothing forces a subject to be spoken. `S3` rule (2) merely writes down what an omitted argument
  refers to;
- per **`M5b`** the verb will **never** carry person, so *who does it* is never on the verb: it is a
  **pronoun**'s job (`M6`) or the **topic convention**'s. That is exactly the Japanese/Chinese profile —
  and it is why pronouns are now the most urgent missing piece.

## Line 7 — the split-S pair (`M5c` + `S4`, ruled 2026-10-14)

    orgi thyMAra                 heart-AG think-V1        "the heart thinks"
    orgina Resne                 heart-PT be-V2           "the heart is"

The **same noun in two different cases**, because the **verb form** says whether there is an
instigator: `V1` (`-ri`) = there IS one, `V2` (`-ne`, since `res` is `e`-final) = there is NONE. So
`orgi` is the **AG**(ent) and `orgina` the **PT**(atient) — active–stative, **split-S** (`S4`). Both
forms pass `tools/check_roots.py` (`--forms orgi,orgina,resne,thymara`), and stress is root-based:
`orGi` · `ORgina` · `thyMAra` · `RESle` (a one-syllable root keeps its own stress).

⚠️ **This is not a grammar curiosity — it is a chord choice.** `H2` makes the AG/NOM word **tonic
(I)** and the PT/ACC word **dominant (V)**, so:

| the poet writes | the clause sounds |
|---|---|
| `orgi thyMAra` (V1) | **I–I** — no dominant anywhere, so it cannot half-cadence |
| `orgina Resne` (V2) | **V–I** — it *opens* on the tension and resolves; a perfect cadence with no opening tonic |
| `orGi sefMehna thyMAra` (V1, transitive) | **I–V–I** — the signature cadence |

✅ **Settled (`M5d`, same day):** `V2` stays `n` + tonic, so there is no OBL clash (`OBL` moved to `-ler`/`-lor` instead). The verb form here is **`RESne`**.

Picking `-ri` or `-ne`/`-ni` is therefore picking how the line **starts** harmonically — the cheapest
expressive tool in the language, and it costs **one suffix the language already owns**.

## What this test EXPOSED (the honest gap list)

| # | gap | why the demo hit it | owner |
|---|---|---|---|
| 1 | **pronouns** — `I` / `you` / `it` | the most song-useful sentence ("I love you") is currently **impossible** — and since `M5b` forbids person marking on the verb, pronouns are now the **only** way to name a participant | `M6` (open) |
| 2 | **number** (singular/plural) | "hearts" / "worlds" have no marking at all | `M4b` (open — and now **smaller**, because `M5b` removed person from the budget) |
| 3 | **tense / aspect** | every line above is present/imperfect only; `ima` (now) is a root, but there is **no tense morphology** | `M5`/`M5a` (open) |
| 4 | **noun predicate / copula** | "the world is certain" — `res` (be) exists as a root, but how a predicate is built is undefined (`Resri`? a bare noun?) | `M5`/`M6` (open) |
| 5 | **questions** | nothing exists yet | `M6` (open) |
| 6 | **verb valency** | line 1 uses `thymara` intransitively, line 2 transitively; *partly* answered by `M5c`/`S4` (`V1` = agentive, may be transitive; `V2` = patientive, no A) - but **which roots may appear in which form** is still open | `M5` (open) |
| 7 | **"towards / go-to"** | `ar` (from) exists; the other half of `03` §0 item 8 has no word | §0 item 8 (half open) |
| 8 | **negation scope** | "does not think" ✓ vs "it is not the heart that thinks" ✗ | §0 item 8 (open) |
| 9 | **stress on function words** | `mei` is one syllable and `P4` speaks only of *roots*, so a particle's stress is undefined | §0 item 30 |
| 10 | **a clause tool** | these lines were assembled **by hand** (word-by-word verified); nothing composes or checks whole clauses yet | §0 item 31 |

## What this test does NOT say

It is a **grammatical** demonstration, not an aesthetic verdict. **Nobody has heard any of it**: the
synthesiser was rejected (`03` §0 item 19) and the audition method is the author **reading the written
forms aloud**. So the next audible step is literally this: read lines 1–7 out loud and see whether the
seam (`sefMehna`), the agreement (`hosDahas`), the topic marker (`a orGi …`) and the negation ending
(`… thyMAra mei`) sound like what you want. If they do not, the failure will be **in the seam or in the
colour system**, not in the word order — and that is precisely what this test was built to find out.



