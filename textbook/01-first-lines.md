# textbook/01 — the first lines (integration test, 2026-10-14)

**What this is.** The first *integrated* test of the locked layers: NOM/ACC case marking (`M4a`), the
grade/chord system (`H1`–`H8`), the `M3a` seam, the `M2b`/`M2c` suffix rules, adjective agreement
(item 29) and negation (`S1`). Every clause below uses **only** words from `../reference/example.md`
(the project's rule), and **every FORM was checked mechanically** with
`python3 ../tools/check_roots.py --forms …` — all of them pass the locked rules (none needed a repair
except the seam, which is by design).

⚠️ **Stress is counted from the ROOT** (`P4c`), so a suffix never steals it and a **one-syllable root
keeps its own stress**. The checker prints the *bare-root* default and says so; the marks below are the
root-based ones (`sefmehna` → `sefMehna`, `res`+`-ri` → `Resri`).

## Line 1 — the minimal clause (chord I–I)

    orGi thyMAri
    heart think-V1
    "the heart thinks"

| word | syllables | how it is built |
|---|---|---|
| `orgi` (heart) | or-gi | **NOM = zero suffix** (`M4a`) |
| `thymari` | thy-ma-ri | **V1** = `r` + the grade vowel. The trigger is `thyma`'s last nucleus `y`, which **counts as `i`** for the grade system ⇒ tonic ⇒ `ri` |

Chords: NOM = **I**, V1 = **I** ⇒ **I–I**. `H2` predicts that a clause with **no dominant-category
word cannot half-cadence** — this line is exactly that case, and it is musically apt: "the heart
thinks" does not resolve anywhere.

## Line 2 — the design's signature cadence (I–V–I)

    orGi sefMehna thyMAri
    heart world-ACC think-V1
    "the heart thinks the world"

| form | syllables | what happens |
|---|---|---|
| `sefmehna` | se-fme-**hna** | **the `M3a` seam, tier 1**: `sefmeh` (an `h`-final root) + `-na` ⇒ the `hn` **VCV cluster**, i.e. the two consonants become ONE onset — no repair, no extra vowel |
| `thymari` | thy-ma-ri | V1, tonic, as above |

Chords: I → **V** (ACC = dominant) → I ⇒ **I–V–I, the perfect cadence** the whole design was aimed at
(`S2` + `H2`). Note the stress: `orGi` · `sefMehna` · `thyMAri` — the root's syllable always wins.

## Line 3 — an adjective, default order (the case KNOB, refinement of 2026-10-14)

    orGi hosDahas sefMehna thyMAri
    heart certain-AGR world-ACC think-V1
    "the heart thinks the certain world"

- `hosdah` is a **vowel-final adjective**, so it is coined as an **`h`-class root** (`hosda` → `hosdah`,
  `R6`); in NOM it would simply be `hosdah`, with no ending at all (item 29, cell (iii)).
- Here it modifies a **case-marked** head, so it takes the **agreeing ending only**: the head's suffix
  vowel is `a` (ACC = dominant, after the front root `sefmeh`) ⇒ `hosdahas`.
- **It does NOT take the case suffix.** That is the author's refinement: in the default order the
  adjacency already says which noun it belongs to, and case on the adjective would be **pure redundancy
  in song**. The case on an adjective is a **knob** — used only when the order is mixed.

## Line 4 — the same content, scrambled (why the knob exists)

    sefMehna hosDahasna thyMAri orGi
    world-ACC certain-AGR-ACC think-V1 heart
    "the world — the certain one — the heart thinks" (the same statement, poetically re-ordered)

Both the noun and the adjective now carry ACC, so the listener can **re-pair** them across the
scramble. This is the author's own pattern `a b-na A B-na`: marking appears exactly where the order
stops carrying the information. ⚠️ Cost, stated honestly: in a heavily scrambled line the pairing can
stay locally ambiguous — that is the poet's choice, not a defect.

## Line 5 — negation (chord I–I–V, deliberately unresolved)

    orGi thyMAri mei
    heart think-V1 not
    "the heart does not think"

`mei` is **postposed to what it negates** (`S1`). `H5` gives function words the **dominant** grade, so a
negative clause always **ends on V** — it cannot sound finished, which is exactly what negation means
musically. (Whether a *function word* carries a performance stress at all is **undefined** — see gap 9.)

## What this test EXPOSED (the honest gap list)

| # | gap | why the demo hit it | owner |
|---|---|---|---|
| 1 | **pronouns** — `I` / `you` / `it` | the most song-useful sentence ("I love you") is currently **impossible** | `M6` (open) |
| 2 | **number** (singular/plural) | "hearts" / "worlds" have no marking at all | `M4b` (open) |
| 3 | **tense / aspect** | every line above is present/imperfect only; `ima` (now) is a root, but there is **no tense morphology** | `M5`/`M5a` (open) |
| 4 | **noun predicate / copula** | "the world is certain" — `res` (be) exists as a root, but how a predicate is built is undefined (`Resri`? a bare noun?) | `M5`/`M6` (open) |
| 5 | **questions** | nothing exists yet | `M6` (open) |
| 6 | **verb valency** | line 1 uses `thymari` intransitively, line 2 transitively; nothing says which is legal | `M5` (open) |
| 7 | **"towards / go-to"** | `ar` (from) exists; the other half of `03` §0 item 8 has no word | §0 item 8 (half open) |
| 8 | **negation scope** | "does not think" ✓ vs "it is not the heart that thinks" ✗ | §0 item 8 (open) |
| 9 | **stress on function words** | `mei` is one syllable and `P4` speaks only of *roots*, so a particle's stress is undefined | new small item |
| 10 | **a clause tool** | these lines were assembled **by hand** (word-by-word verified); nothing composes or checks whole clauses yet | tooling |

## What this test does NOT say

It is a **grammatical** demonstration, not an aesthetic verdict. **Nobody has heard any of it**: the
synthesiser was rejected (`03` §0 item 19) and the audition method is the author **reading the written
forms aloud**. So the next audible step is literally this: read lines 1–5 out loud and see whether the
seam (`sefMehna`), the agreement (`hosDahas`) and the negation ending (`… thyMAri mei`) sound like what
you want. If they do not, the failure will be **in the seam or in the colour system**, not in the word
order — and that is precisely what this test was built to find out.

