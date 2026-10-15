# data/hand/class-proposal.md — the V0 class (I / II / D) of every root (HAND-WRITTEN; a PROPOSAL)

**Status:** PROPOSAL 2026-10-15, from the `V0` rulings of 2026-10-15. **IMPLEMENTED the same day:**
every row below now lives in `../../reference/example.md`'s CLASS & POS section (read by
`../../tools/clause.py`), the 6 rows marked `?` are listed in `03-open-questions.md` §0 **item 36** and
await the author's veto, and the 15 `—` rows are recorded there as `II*` (the noun default). A class is
**advisory**: it records the root's *natural* reading and is what the checker warns about — it never
overrides the sentence. **Nothing here is locked, and nothing here touches the word lines of
`../../reference/example.md`** (still the only source for examples).

**Input:** the 36 roots of `../../reference/example.md` (read 2026-10-15) = 4 demo + 5 batch 2 + 27
batch 1. **Out of scope:** the two names and the function words `ar` / `mer` / `mei` (R5: no suffixes,
no verb use).

## The checklist (the "quick rule")

Ask **one** question of the root's *typical* situation: **is there necessarily an instigator?**

| class | answer | `V0` reads as | `V1` (`-rV`) | `V2` (`-nV`) |
|---|---|---|---|---|
| **I** (agentive) | yes — a willed act / making / perception / speech | participant in **NOM** (AG) | explicit "there IS one" | not a legal use |
| **II** (patientive) | no — a state, a property, a natural process | participant in **ACC** (PT) | not a legal use | explicit "there is NONE" |
| **D** (dual) | **both framings are natural** (a causative / anticausative pair) | either — read off the participant's case | legal | legal |
| **—** | the root has **no verb sense yet** | — | — | — |

Like the R6 soft rules in `../../tools/check_roots.py`, a mismatch is a **warning**, not a break:
the author always decides.

## The proposal (sorted by class; `?` = a judgement call to confirm)

| root | gloss (`example.md`) | verb sense | class | why |
|---|---|---|---|---|
| desa | the making | to make | **I** | the clearest willed act in the list |
| os | have | to have | **I** | RULED 2026-10-15: two participants ⇒ agentive side |
| thyma | think | to think | **I** | RULED by the demo (`orGi thyMara`) |
| argonna | love | to love | **I** ? | two participants like `os`; the demo already makes mental activity agentive — but "love" is stative, so `II` is arguable |
| onla | the leave | to leave | **I** ? | willed departure — but "be left behind" would be the dual partner |
| res | be | to be | **II** | RULED 2026-10-15 |
| drera | thunder | to thunder | **II** | impersonal natural event |
| foih | ice | to freeze | **II** | change of state with no instigator |
| fumi | flower | to bloom | **II** | natural process |
| hu | wind | to blow (of wind) | **II** | impersonal natural event |
| losdo | happy | to be happy | **II** | state (this root is also the MOD/adjective example) |
| hosda | certain | to be certain | **II** | property (also a MOD/adjective root) |
| sinkoi | solitude | to be alone | **II** | state |
| roi | day | to dawn | **II** ? | natural event — the verb sense is a derivation, not in the gloss |
| asdo | knowledge | to know | **II** ? | stative, no willer — but it sits next to `thyma` (I) |
| eli | life | to live | **II** ? | state/process with no instigator |
| noih | emptiness | to be empty | **II** ? | abstract property |
| seli | birth | be born / give birth | **D** | the clearest dual pair in the list |
| aba | seed | sprout / sow | **D** | classical anticausative pair |
| ila | the stop | stop (intr.) / stop (tr.) | **D** | the stop can just happen or be caused |
| gridi | the promise | be promised / promise | **D** | a promise is given (willed) and kept or broken (patient) |
| esgim | foot | — | **—** | body-part noun, no verb sense |
| aldem | face | — | **—** | body-part noun |
| winah | eye | — | **—** | body-part noun |
| hinah | ear | — | **—** | body-part noun |
| orgi | heart | — | **—** | concrete noun |
| sym | god | — | **—** | noun |
| sefmeh | world | — | **—** | concrete noun |
| walu | wood | — | **—** | concrete noun |
| bosga | place | — | **—** | concrete noun |
| cou | autumn | — | **—** | season noun |
| esa | the all | — | **—** | noun |
| ima | present / now | — | **—** | time noun |
| basdo | (no meaning yet) | — | **—** | no gloss |
| boih | (no meaning yet) | — | **—** | no gloss |
| brega | (no meaning yet) | — | **—** | no gloss |

## RULED 2026-10-15 — the noun default: `II`

A root with **no verb sense** (`—` above) that is used as a verb reads as **"be / become N"**, i.e. it
falls under **II** (participant in ACC): the most neutral reading, and the one consistent with "a bare
root claims no instigator". Notation **`II*`** = "under the noun default; no verb sense recorded yet" —
deliberately distinct from the 12 explicit `II` rows, which *are* the author's decision.

Consequences:

- **The other reading is overt, not free.** "make N" (causative / agentive) is written with the
  explicit `V1` (`-rV`), so it costs a suffix and is always a visible choice.
- **Checker baseline:** a warning fires only where the lexicon records a class (`I` used on the PT
  side, `II` used on the AG side). A `II*` root warns on **nothing**, because no verb sense was ever
  claimed — this keeps the advisory noise low.
- **Coining cost ≈ 0 for noun-ish roots:** they need no class note; only exceptions (`I`, `D`) do.
- **Deferred:** the instrumental reading ("use N") gets no default; it would need its own decision.
- ⚠️ None of this is mechanically checkable yet — see "What this file does NOT do".

## Counts (as proposed, after the noun default)

- **I = 5**: `desa` · `os` · `thyma` · `argonna`? · `onla`?
- **II = 12**: `res` · `drera` · `foih` · `fumi` · `hu` · `losdo` · `hosda` · `sinkoi` · `roi`? ·
  `asdo`? · `eli`? · `noih`?
- **D = 4**: `seli` · `aba` · `ila` · `gridi`
- **`II*` (noun default) = 15**: `esgim` · `aldem` · `winah` · `hinah` · `orgi` · `sym` · `sefmeh` ·
  `walu` · `bosga` · `cou` · `esa` · `ima` · `basdo` · `boih` · `brega`

So **every one of the 36 roots now carries a class** — but the only *decisions* still missing are the
15 verb senses (they stay `II*` until something defines them).

## ⚠️ FINDING — the column is full, but 42% of it is a DEFAULT

**15 of 36 roots (42%) have no verb sense at all**, and 3 of those (`basdo`, `boih`, `brega`) have no
gloss either. The noun default lets the column be filled honestly, but it does **not** decide those
roots' verbal meaning: that still needs the valency question
(`../../docs/decisions/03-open-questions.md` §0 item 10 / `M5`).

**Consequence for the lexicon:** `reference/example.md` needs a **POS** field *before* a class column
can be read properly — the "verb sense" column above is a draft of exactly that POS field, and `II*` is
only meaningful next to it.

**Sign that the checklist is doing real work:** the four `D` rows it produced are precisely the
causative/anticausative pairs (`seli` birth, `aba` seed, `ila` stop, `gridi` promise) and none of the
concrete nouns — i.e. the criterion picks the linguistically expected set, not a random one.

## What this file does NOT do

- it does not choose the machine-readable shape of a `D` row — deferred until the clause tool exists
  (§0 item 31), because without whole-clause parsing there is nothing to check against;
- it does not check anything by itself: the checker side is an R6-style **soft warning** in
  `../../tools/check_roots.py`, and a frame-level check needs a clause tool that does not exist yet
  (`../../docs/draft/01-first-lines.md`, gap #10);
- it does not amend the locked wording: `M5c` / `M5d` / `S4` still say "the verb FORM decides the
  case" and needed to be rewritten as "`V1`/`V2` decide it by suffix; `V0` reads it off the
  participant's case" (RULED 2026-10-15, not yet written into the decision log).
