# Brainstorm — RAW (author's, unprocessed)

> **STATUS MAP (read this first).** This file is the *scratch* record; the authoritative decisions live in
> `docs/decisions/00-README.md` (decision log) and the pending list in `docs/decisions/03-open-questions.md` §0.
> - §1–§2 — the original brainstorm (front/back vowels, rhyme, harmony/oppositeness). **§2's warning block
>   is still the key terminology correction.**
> - §3 — the first "tonic / subdominant / dominant" proposal.
> - §4, §4b–§4e — the full picture: case system, grade table, trigger. **All decided (H2/H3/H4).**
> - §5, §5b — the seam rules (M3a) and the one-syllable suffix (M3b). **Decided.**
> - §6, §6b–§6c — unresolved clauses (H5), negation (S1), particle audibility (H6). **Decided.**
> - §7, §7b(now §9h) — word order (S2) and "which suffix sounds the word's chord" (M2c). **Decided.**
> - §8, §9, §9a–§9h — M4/M4a (the case table), the "key" analogy (H7), VOC & the article (H8). **Decided.**
> Older passages are kept for the reasoning trail; where they contradict a later section, the later one wins.

Status: **RAW / not decisions.** Recorded so nothing is lost. The mechanics are **not yet**
explained (the author said they will explain later). Do **not** build on this as if it were
decided, and do not treat it as a locked layer.

## 1. Vowel division: front / back

- Divide the vowels into **front / back**.

> **Agent note:** a front/back division **already exists** in the locked phonology —
> `../decisions/01-phonology.md` §2 "bright <-> dark palette": front `{i, e, y, ae}` vs back `{u, o, a}`,
> used today as an **expressive texture knob** (bright for folk/post-rock, dark for epic/power
> metal). So the new part is presumably to give that division a **grammatical/structural job**
> (harmony), not to invent the division itself.

## 2. Rhyme + vowel harmony / oppositeness

- Emphasise **rhyme** (押韻).
- **Vowel harmony / "oppositeness"** — ~~to be explained by the author~~ → **explained and largely
  decided**: it is the three-grade vowel-colour system (§3 onward; `docs/decisions/00-README.md` H1–H8).

> **UPDATE:** since then — the scope is **suffixes only, roots free** (**H1**); the mechanic turned out to
> be the grade system (same vowel / the class's central vowel / the opposite pole, read against the root's
> last vowel), and it is now largely locked (H2–H7). **Rhyme itself, however, is still undesigned** (see
> `docs/decisions/03-open-questions.md` §0 item 16).

## Collateral damage to check (agent, recorded while reading, for later discussion)

> **Status of these four:** (1) resolved by **H1** (scope = suffixes only, roots free); (2) resolved by
> **H3 + M2c** (the grade vowel is a *redundant cue* by design, so predictability is a feature);
> (3) and (4) are **still open design jobs** — rhyme, and harmony-vs-the-leap.

1. **Root-internal harmony would break locked assets.** Under the *strictest* reading
   (harmony applies inside roots too, diphthong off-glides count, no neutral vowels):
   - 4 of the 8 diphthongs cross the divide — `ai`, `eu`, `oi`, `aeu` (split by the *nucleus*
     class the other 4 do not cross: `au`, `ei`, `ou`, `aei`);
   - reference word `roi` (day) = `oi` → crosses;
   - `aurorius` (front `i` inside an otherwise back word) and `austareus` (front `e`) → cross.
   **Two sub-parameters fix this, and they must be chosen explicitly:** (a) does the
   off-glide count for harmony, or only the nucleus? (b) are `i` / `e` **neutral**
   (the Turkish/Finnish solution)? With "nucleus only" + "`i`,`e` neutral", **nothing breaks
   at all** — all 8 diphthongs and all 6 reference words survive.
2. **Harmony + the voicing knob ⇒ meaning rides on consonants alone.** If suffix vowels are
   predictable from harmony, a suffix's vowel carries no information, and stop voicing is
   already non-distinctive (C2b). The distinctive affix alphabet is therefore the ~**16**
   distinctive consonants. That is a natural **cap on how rich the morphology can get** —
   relevant to M2, whose density the author has now deferred.
3. **Rhyme may become automatic.** If suffix vowels are harmony-determined and suffixes sit at
   word ends, word endings rhyme **by rule**. A beauty device that fires for free can start to
   feel mechanical. Alternative: make rhyme ride on the **stressed** vowel (which is inside the
   root, hence lexical) instead of on the suffix.
4. **Harmony and the leap are structurally opposed.** The 4 hiatus "leaps" (`iu yu ia ya`) jump
   from front-high to extreme-back *by design* — i.e. they are **anti-harmonic** on purpose.
   Harmony = unity; the leap = contrast. They must be given **different jobs**, not merged.
   *(⚠️ "harmony" here means vowel-colour agreement — see the terminology warning below.)*

> **⚠️ TERMINOLOGY CORRECTION (author, and it corrects an overstatement of mine).** The language has
> **no tone/pitch** and **never sounds chords**. "tonic / subdominant / dominant", "I/IV/V",
> "progression", "cadence" are **metaphors for grammar-level labels**; the only physical facts are the
> vowels' **colour** (bright↔dark) and the **relational contrast** between a suffix vowel and its root's
> last vowel. I previously wrote things like "audible chord" and "silent blueprint note" — that was
> **wrong**; the correct statement is: **a suffix always exposes a contrast marker, a particle exposes
> none.**
>
> **Derived consequence that MATTERS (agent):** because the value is *relational*, the **absolute colour
> of a grade flips with the root's class** — "dominant" is `a` (**dark**) after a front-class root but
> `i` (**bright**) after a back-class root. Therefore:
> 1. any naive mapping "dominant = dark/tension" fails for about half the words;
> 2. the only **stable, learnable** thing is the **degree of contrast** (0 = tonic / +1 = subdominant /
>    maximum = dominant);
> 3. a future prosody↔melody mapping must therefore be built on **contrast relative to the word's own
>    centre**, never on absolute colour.
>
> **Good news:** the *shape* of the skeleton IS stable — in default order a declarative is
> "same / opposite / same" regardless of the roots' classes. So the **contour is stable; the colours
> vary with the roots.**

---

## 3. PROPOSED MECHANIC — "tonic / subdominant / dominant" grades (the author's "opposity")

Idea (author, inspired by functional harmony): give a suffix **three** vowel grades instead of the
binary front/back choice, e.g. with a root whose relevant vowel is `i` and a consonant `n`:

| grade | music analogue | vowel relation to the trigger | example |
|---|---|---|---|
| **tonic** | chord I | **exactly the same** vowel | `lati-ni` |
| **subdominant** | chord IV | **same group**, different element | `lati-ne` |
| **dominant** | chord V | **opposite group** | `lati-na` |

Consequence: a suffix = **consonant (category) x vowel (grade)** — two orthogonal axes, i.e. roughly
16 distinctive consonants x 3 grades ≈ **48 distinguishable suffix shapes**. Note this *repairs*
the earlier problem #2: the suffix vowel is no longer predictable, so it carries information again.

*(`lati` is **not** in `reference/example.md`; used here only as a mechanism sketch, not as an
example word. Concrete suffix shapes still belong to M3.)*

### Parameters that must be pinned before this can be locked

1. **Is the grade SEMANTIC or POETIC?** (the crux — see below)
2. **What defines a "group"?** The author's split is front/back. ⚠️ `y` is the problem case: it is
   **front but rounded**, i.e. acoustically darker than `i`/`e`/`ae`. If "same group" is defined by
   frontness, `y` and `i` are "the same colour" but will not *sound* the same. Options: frontness,
   rounding, height, or the locked **bright/dark** palette — these give different memberships.
3. **Which specific vowel is "subdominant"?** The groups are **asymmetric**: front has 4 vowels
   `{i,e,y,ae}`, back has 3 `{u,o,a}`. So "same group, different element" has 3 choices after a
   front trigger but only 2 after a back trigger. Without a rule, one suffix has several legal
   shapes → ambiguity.
4. **What is the trigger, exactly?** The last vowel? The stressed vowel? And for a root ending in
   a diphthong (`roi` = `oi`) or a hiatus, which element counts? Mixed-vowel roots are legal
   (H1), so e.g. `aurorius` would be triggered by its final `u` → back class.
5. **Suffix shape consequence.** If a suffix begins with a **consonant**, no vowel contact arises.
   If it begins with a **vowel**, the tonic grade can produce illegal contacts (`ii`, `aa` are not
   legal) — so the grade system pushes suffixes toward **consonant-initial** shapes (which is also
   where the meaning will live).
6. **Rhyme interaction.** If the grade is **fixed by grammar**, word endings rhyme by rule again
   (the "automatic rhyme" risk). If the grade is **free**, rhyme becomes a real poetic tool — but
   then it carries no grammatical information.

---

## 4. FULL PICTURE (author, explained) — a case system graded by harmonic function

The suffixes are **temp examples**, not finalised. **The consonant sequence carries the
grammatical identity; the vowel realises the harmonic grade.**

| form | grammatical | harmonic function | grade |
|---|---|---|---|
| `lati-` | root / NOM | **I** tonic | (zero suffix) |
| `lati-na` | ACC | **V** dominant | opposite group |
| `lati-sa` | GEN | **V** dominant | opposite group |
| `lati-nem` | DAT | **IV** subdominant | same group, other vowel |
| `lati-ner` | LOC | **IV** subdominant | same group, other vowel |
| `lati-ri` | Verb class 1 | **I** tonic | same vowel |
| `lati-ni` | Verb class 2 | **I** tonic | same vowel |

Author's example progressions (same content, different order):
- `lati latina latiri` = **I-V-I**
- `lati latina latinem latini` = **I-V-IV-I**
- `latiri lati latisa latina` = **I-I-IV-V**

### Agent's assessment — what is strong
- The assignment **matches musical semantics**: NOM/verb = home/closure = I; ACC/GEN = "still
  awaiting its verb" = unresolved = V; DAT/LOC = setting/circumstance = departure = IV.
- **The real payoff:** because the language is case-marking, **word order is free, so the poet can
  choose the chord progression without changing the meaning** — the three examples are
  reorderings (note the verb-first one). That turns the idea from decoration into a
  **compositional tool**.
- It supplies the bridge to the (not started) prosody <-> melody area.

### Consequences / risks (agent)
1. **It commits the language to case marking + FREE WORD ORDER** — a syntax-level commitment
   (`docs/decisions/03-open-questions.md` §F is empty), and it interlocks with M1/M2 and the still
   PROVISIONAL P4d.
2. **The table must cover clause-level semantics, not just cases.** Questions, negation and
   non-final/subordinate clauses are exactly where a song must *not* resolve — the table has no
   entry for them. Under "grade fixed per CATEGORY", a clause with no dominant-category word
   (e.g. `lati latiri` = I-I) **cannot produce a V ending at all**.
3. **The vowel is a REDUNDANT CUE, not an extra information axis.** The grade follows from the
   category, so once you know the morpheme you know the vowel; capacity stays with the
   **consonant** (~16 distinctive). Redundancy is still valuable when sung (a cue that survives
   noise) — but it must not be counted twice.
4. **Each case gets 2-3 allomorphs** (the vowel is relative to the root's trigger class), so the
   case table doubles/triples.
5. **The M3 collision, now concrete:** these suffixes are `n`-, `s`- and `r`-initial, and a root
   ending in `f`/`v`/`h` can only take `n`-initial ones (`fn`/`wm`… are legal, `fs`/`fr` are not)
   — such roots would be **unable to take GEN or verb-class-1** without a sandhi rule.
6. Nit: per **C2**, the citation form of the demo root is **`ladi`**, not `lati` (`t` is a stop;
   the dictionary form is voiced, `lati` is the "hard" performance variant).
7. `NOM = zero suffix` should be confirmed (bare root as citation form).

### 4b. Fork resolved (H2) — and the demo already implies HOW the grades must be derived

- **H2 (decided):** the grade is bound to the **category** (not a clause-level mode). Word order
  alone sets the progression; a clause with no dominant-category word can never end on V.
- **The demo quietly rules out one reading.** With "subdominant = same group, one rung" and
  "dominant = the opposite group" taken naively:
  - trigger `i` → subdominant `e` ✓ (matches the demo);
  - trigger `i` → dominant = the back ladder at the **same height** = `u` → `-nu` ✗ **the demo
    says `-na`**.
  So the demo implies **dominant = the far end / maximal contrast**, not "same rung". Combined with
  "subdominant = one step darker", the whole thing collapses into a **single bright <-> dark axis**:
  **tonic = the trigger, subdominant = one step darker, dominant = the opposite pole.** That axis is
  *already* in the locked phonology (§2 palette) — which is what would make the grades **derivable
  rather than hand-picked**, and therefore actually *audible* as functions instead of being names.
### 4c. Pinned since (author) — the grade table is now down to ONE open cell

Pinned:
- **`y` counts as `i`** in the grade system (so a `y`-final root behaves exactly like an `i`-final
  one). **Consequence: `y` never appears in suffix vowels** — it stays a root-only signature sound.
  *(Assumption to confirm; the alternative would be "class = front but tonic = `y` itself".)*
- **`dominant` is always one of the two POLES: `i` / `a`.** Front-class trigger → `a`; back-class
  trigger → `i`. So dominant never lands on `e`, `ae`, `o` or `u`.
- Verified against the demo: the suffix is `consonant-sequence (identity) + grade vowel`, e.g.
  ACC `-n` + dom = `-na`; GEN `-s` + dom = `-sa`; DAT `-n`+`m` + sub = `-nem`; LOC `-n`+`r` + sub
  = `-ner`; verb 1 `-r` + tonic = `-ri`; verb 2 `-n` + tonic = `-ni`. **The demo is internally
  consistent.**

### 4d. Grade table — DECIDED (H3): subdominant = the class's CENTRAL vowel, unconditionally

Author's choice: **front class → subdominant `e`; back class → `o`** (no exception when the trigger
is itself the central vowel). Triple = (tonic / subdominant / dominant):

| trigger | tonic | sub | dom |
|---|---|---|---|
| `i` | `i` | `e` | `a` |
| `y` | `i` | `e` | `a` |
| `e` | `e` | **`e`** | `a` |
| `ae` | `ae` | `e` | `a` |
| `u` | `u` | `o` | `i` |
| `o` | `o` | **`o`** | `i` |
| `a` | `a` | `o` | `i` |

- The table is a clean **mirror**: front `sub e / dom a`, back `sub o / dom i`.
- Suffix vowel inventory = **`i e ae a o u`** (6); **`y` never appears in a suffix**.
- ⚠️ **Accepted consequence:** where the trigger is the central vowel (`e`/`o`), **tonic and
  subdominant coincide** → I and IV sound the same on those words. It causes no grammatical
  ambiguity (identity lives in the consonant), but the progression loses the I/IV contrast there.
  **Coining rule it implies: never distinguish two morphemes by tonic-vs-subdominant alone.**
- Still open: **the trigger vowel** rule (see below) and `NOM = zero suffix`.

### 4e. Trigger — DECIDED (H4)

**The root's last syllable nucleus.** A diphthong-final root triggers on its **nucleus** (`roi` →
`o`, not the glide `i`). For 1- and 2-syllable roots this coincides with "the stressed vowel", so it
only diverges on **3-syllable** roots (`argonna` → `a`, not the stressed `o`).
Why it was preferred over the stressed vowel: **P4 makes stress a performance choice**, so a
stressed-vowel trigger would let a performer recolour every suffix vowel (and destabilise the written
word form). The last nucleus is fixed at the lexical level.

Still unconfirmed in this area: **`NOM = zero suffix`** (the demo implies it).

---

## 5. SEAM RULES (decided, M3a) — root-final `f`/`v`/`h` + consonant-initial suffix

Author's three-tier rule (verbatim in substance): **(1)** group the two consonants as a CC if that
CC is already whitelisted → `f/v/h` + `m`/`n` = `fm fn hm hn wm wn` ✓ nothing changes; **(2)** if not,
**sync**: `{f,v}`+`s` → `ss`, `{f,v}`+`r` → `rr`, `h`+`s` → `s`, `h`+`r` → `r` (note the two areas
behave differently: `{f,v}` merges into a geminate, `h` simply drops); **(3)** last resort — insert a
vowel **copied from the root's last vowel**.

| suffix onset | after `f` / `v` | after `h` |
|---|---|---|
| `m` | `fm` / `wm` (tier 1) | `hm` (tier 1) |
| `n` | `fn` / `wn` (tier 1) | `hn` (tier 1) |
| `l` | **missing → proposed `ll`** | **missing → proposed `l`** |
| `r` | `rr` (tier 2) | `r` (tier 2) |
| `s` | `ss` (tier 2) | `s` (tier 2) |

Gaps / notes (agent):
- **`l` is not covered by tiers 1–2** → proposed completion (pending confirmation).
- If the root's last vowel is `y`, tier 3 would copy `y` into a non-root position, which contradicts
  H3's "`y` never appears outside a root" — needs a decision (`y` → `i`?).
- The **trigger** of the grade stays the root's original last nucleus; the inserted vowel does not
  become a new trigger.
- **This rule is why the suffix-initial inventory is `{m,n,l,r,s}`:** and that in turn forces the
  following shape (M3b).

### 5b. Suffix shape — DECIDED (M3b): one syllable `C V (C)`

`-nem` cannot be `nm` + `e` (because `nm` is not a legal onset). The only legal reading is
**`n` (onset) + `e` (grade vowel) + `m` (coda)** — a single syllable. Decided (author's choice A):

```
suffix = [onset ∈ {m,n,l,r,s}] + [grade vowel] + [optional coda ∈ {m,n,l,r,s}]
```

Consequences:
1. **One suffix = one syllable = one note** — the composition unit equals the musical beat.
2. **Suffix chains can never break phonotactics**: a suffix's coda + the next suffix's onset is
   exactly a legal medial CC (coda + single onset).
3. **Identity space = onset x coda = 5 x 6 = 30** forms — the budget for M4–M6.
4. The grade vowel is a **cue**, not extra identity (H3's coining rule still applies: two identities
   may share a consonant shape only if their grades differ — e.g. the demo's ACC `n`+dominant vs
   V2 `n`+tonic ✓).

Still pending in this area: the missing `l` seam rules, the `y`-copy question (tier 3), and
`NOM = zero suffix`.

---

## 6. Unresolved clauses — DECIDED (H5): dominant-grade FUNCTION WORDS

Author's choice B: questions / negation / non-final clauses are served by **freestanding function
words that are assigned the dominant grade (V)**. They are **word-level and take no suffixes**.

Why this is more than bookkeeping:
- It guarantees the half-cadence: a clause with no case-marked dominant word can still end on V.
- A plain statement can be ordered so it **cadences on the tonic verb** → the syntax produces correct
  musical behaviour instead of merely naming it.
- Because word order is free, the poet can keep a negator at the end (tension) **or** move it earlier
  and let the verb close on I — the same content, two harmonic outcomes.
- It introduces a **second word class** (function words). The lexicon must list them separately.
  They may be single syllables: 1-syllable words are legitimate.

### RESOLVED (H6): a particle does NOT sound its grade — see §6b/§6c below

H1 says harmony is realized **on suffix vowels**, and a bare particle has none. Readings:

| option | how the particle's grade sounds | cost |
|---|---|---|
| **A. reference = the preceding word** | the particle's vowel = the dominant vowel for the *preceding* word's class (front context → `a`, back context → `i`, mirroring H3) | shape varies with position; a clause-initial particle (e.g. an initial question word) has no reference → needs a fallback |
| **B. reference = the clause's VERB** (= its "tonic") | stable regardless of word order; adds a real **clause-level key** concept — the clause's colour reference is its tonic | one more rule layer (word-internal harmony = suffix ← its root; clause-level harmony = particle ← the verb); needs a fallback for verbless clauses |
| **C. the particle does not sound its grade** | fixed shape; the grammar just marks it V, and the *composer* realizes the chord | simplest; but the grade is then part of the "harmonic blueprint" rather than audible |

**DECIDED = H6: option C.** So the language has **two tiers** of harmonic signalling:
**suffixes always expose a colour-contrast marker** (H1/H3) while **particles expose none** (H6).

### 6b. Negation — S1: `mei`, postposed

The author's example: negation uses **`mei`**, placed **behind the word it negates** (constituent
negation). Harmonic consequences, which turn out to be a gain:
- Negating a **noun** → a V word sits **mid-clause** = a *passing dominant* (the progression
  automatically contains a V chord).
- Negating the **verb** → the negator is **last** → the clause **half-cadences** on V.
- Since word order is free, the poet chooses which of the two they want.
- `mei` is a legal shape (`m` + the diphthong `ei`, one syllable) ✓.

### 6c. Optional extension worth considering (not decided)

By analogy with the **voicing knob** (performers may freely flip a stop's voicing as a *performance*
choice), the composer could be allowed to **re-colour a particle's vowel** as a performance choice.
That would let a composer give a particle's vowel a colour of its own without touching the grammar.
Risk: a re-coloured particle could collide with an existing word (`mei` → `mia`?), so it would need a
"never creates a homophone of a real word" constraint.

---

## 7. S2 decided (word order) + the new question it forces: which suffix sounds the chord?

**S2 (decided):** free scrambling + a preferred **verb-final** default order (prose = default, poetry
permutes freely; particles stay adjacent to their host). Consistency check: the author's first example
`lati latina latiri` = I-V-I **is** the default order, and `latiri lati latisa latina` is its
scrambled twin.

### The forced question: a word with several suffixes would carry several grade vowels

Under M2 the density is deferred, so suffixes WILL stack (number + case; aspect + tense …). But every
suffix's vowel is fixed by its category (H2/H3), so a stacked word contains several grade vowels.
Which one is the word's chord?

| option | what a stacked word is | cost |
|---|---|---|
| **A. the outermost (rightmost) suffix decides** | the word = **one chord**, consistent with M2's "farther = more syntactic"; the inner suffixes' grade vowels still appear, as **redundant cues** | inner suffixes have no harmonic role (pure redundancy) — but that redundancy directly helps the §F intelligibility risk |
| **B. every suffix is its own chord** | a word = a **mini-progression** (a word could itself move IV→V!) — maximally distinctive | every syllable must be parsed for grade; the clean "word = chord" metaphor disappears; the heaviest listening load of any option |
| **C. only some categories carry a grade** (e.g. only clause-level roles: case + verb class); number/possession/tense use a fixed neutral vowel | the word = one chord, carried by the graded suffix | needs a **neutral vowel** for the ungraded suffixes (another rule), and those suffixes lose both the redundancy cue and the harmony |

**DECIDED = M2c: option A.**

## 9. M4 in full: the case inventory, VOC by vowel colour (H8), the "key" analogy (H7), and the relational colour

### 9a. Cases — FINAL TABLE (author's shapes + grades, verified)

| case | grade | suffix skeleton | form after a front-class root (trigger `i`: tonic `i`, sub `e`, dom `a`) |
|---|---|---|---|
| **NOM** | I | zero | `lati` |
| **ACC** | V | `n` | `-na` |
| **GEN** | V | `s` | `-sa` |
| **DAT** | IV | `m` (changed from `-nem`) | `-me` |
| **LOC** | IV | `n` + coda `r` | `-ner` |
| **INS** | IV | `s` + coda `r` | `-ser` |
| **OBL** | IV | `l` (collision fix) | `-le` ⚠️ **SUPERSEDED (`M5d`, 2026-10-14): OBL = `l` + subdominant + **`r`** = `-ler`/`-lor`; the bare `-le` is gone. The M3a `l` seam row it forced STILL stands (the onset is still `l`)** |
| **Verb 1** | I | `r` | `-ri` |
| **Verb 2** | I | `n` | `-ni` |

Notes (agent):
- Every form satisfies M3b's `C V (C)` and every vowel matches H3/H4 ✓ — **the table is internally consistent.**
- **Verb 2 vs ACC**: same skeleton `n`, distinguished by **grade alone** (tonic vs dominant). This is
  exactly what H3's coining rule permits (dominant and tonic never coincide), so the design works ✓.
- **Identity budget:** 6 skeletons used (`n`, `s`, `m`, `nr`, `sr`, `l`) of 30 → **24 left**.
- The OBL choice (`-le`) **forces the `l` row of the M3a seam** → adopted as `{f,v}`+`l` → `ll`,
  `h`+`l` → `l` (the analogue of the `r`/`s` rows).
- ⚠️ **Balance — CORRECTED after the author's challenge.** The distribution is **1 · 2 · 4** (I · V · IV).
  My claim that OBL is high-frequency was **unfounded** and is **withdrawn**: with six cases covering the
  normal noun roles, the else-case is plausibly *low*-frequency. And the skeleton is not flat in practice
  — the **most frequent** cases (NOM/ACC/GEN = subject / object / possessor) already carry the **I vs V**
  contrast. What remains is mild: a clause made entirely of oblique cases is colour-uniform (all IV),
  which **M4b (inner-suffix grades) may fix by itself**, since inner suffixes sound their own vowels too
  (M2c says only the outermost suffix decides the word's chord *label*, not that inner ones are silent).
  Options if you still want balance: move **INS** (a means = "unfinished until used") or **OBL**
  ("not yet classified") to dominant → 1 · 3 · 3.
- ✅ **DECIDED: keep 1 · 2 · 4 — with `INS → dominant` held in RESERVE** (author): if future corpus or
  music work shows too many IV in a clause, INS is the one-line fix (and it yields 1 · 3 · 3). The
  semantic hook is ready ("a means is unfinished until used"), so it needs no re-litigating.

### 9b. VOC & article — expressed by vowel colour (author)

- VOC is **not** a case. VOC *and* the article (`a/an/the`) share one device: **vowel colour**, chosen
  **emotionally** by the speaker/poet.
- Emotional division (author's example list — 7 vowels → 7 emotions):

| vowel | emotion |
|---|---|
| **A** | angry / brave / energetic |
| **AE** | disgust / hate |
| **O** | surprise / awe |
| **E** | joy / searching / pride |
| **I** | sad / depression / lonely |
| **U** | calm / mercy |
| **Y** | fear / mysterious / confusing |

- Typographic intent: **small capital = article; large capital = VOC** (and a VOC word is naturally
  stressed, which the author notes is desirable for emphasis).

### 9c. RESOLVED — the device is a lone vowel WORD (no small caps involved)

**Agent error, withdrawn:** I read "small capital" as typographic *small caps* (ᴠ) and claimed an ASCII
conflict. The author meant **lowercase / uppercase letters**. The actual design:

| written | meaning |
|---|---|
| `a`, `e`, `o`, `i`, `u`, `ae`, `y` (a lone lowercase vowel word) | **article** (a/an/the) |
| `A`, `E`, `O`, `I`, `U`, `Ae`, `Y` (same word, initial capital) | **VOC** |

- Plain ASCII ✓ (goal 3 fine). No font features, no Unicode.
- One **residual rule** is needed: **a one-letter word written with a capital is read as VOC, not as a
  stress mark** — otherwise `A` could be parsed as an emphasized article.
- **Bonus:** because emotion sits on this *separate word*, it never interferes with the root's identity
  or with a suffix's grade → **conflict 2 (where does the emotional vowel attach) dissolves by itself.**
  The "two meanings on one phonetic dimension" worry also disappears: the emotion is not on the noun's
  vowels at all.

### 9d. RESOLVED too — the emotional vowel attaches to the ARTICLE/VOC word itself

Since the article/VOC device **is** a lone vowel word (§9c), the emotional vowel attaches there and
nowhere else:

- it cannot destroy the root's identity (the root keeps its own vowels), and
- it cannot collide with a grade (no suffix is involved).

Bonus synergy: **emotion = vowel, intensity = the existing performance marks** (length `aa`, stressed
CAPITAL, vibrato `v`) → the language already has a **two-axis emotional system** (which emotion × how
strongly) with no new machinery.

### 9e. Where the grammatical load lives

**M4 (decided):** the grammatical load stays in the **case paradigm** (suffixes), not in particles.
Honest reason: a suffix always exposes a **colour-contrast marker**; a particle exposes **none** (H6), so
a particle-marked noun would be colour-identical to a bare root.

### The author's justification for the relational design (H7) — and the one place it strains

> "the absolute colour flipping with the root's class is **my design**, just like an actual dominant
> chord changes when you use a different major or minor scale"

This is a real and elegant framing: **class (front/back) ≈ the word's mode/key; grade ≈ the function**,
and the mode changes the *material* while the function stays — exactly like a dominant chord in major
vs minor.

It does **not** contradict the earlier warning; it is the same fact seen from the other side:

| who | what they use | why |
|---|---|---|
| **composer** | the grade **label** (function) → pick the chord | the absolute vowel is irrelevant to the function, so the flipping costs nothing |
| **listener / singer** | the **contrast relative to each word's own centre** | because the "key" is per word, a naive listener hears a chain of *local* contrasts, not one global progression |

⚠️ **Where the analogy strains (agent):** in music the key is fixed per piece or section, but here **every
word carries its own key** (its root's class). So a clause is not a single progression; it is a sequence
of local contrasts whose *shape* is stable (a default declarative is always same / opposite / same). The
composer must therefore **choose a key** for the music and map the grade labels onto it — the skeleton
tells them the functions, never the pitches.

### What M4 still needs

1. each case's **grade label** (only NOM = tonic and ACC/GEN = dominant are fixed so far),
2. whether **NUMBER** is a suffixed category,
3. **grade labels for the non-role categories** (number, tense, aspect, mood, negation, person) — forced,
   because every suffix's vowel must come from somewhere (H2),
4. the **H8 conflicts** (§9c: small capitals are not ASCII; §9d: where the emotional vowel attaches).

### 9h. The chord colour is RELATIONAL (author's clarification — written earlier as §7b)

The colour is **not an absolute property of a vowel** — it is the **contrast between the suffix's vowel
and the bare root's last vowel** (H4's trigger). So:

- `-na` is **dominant** after an `i`-root (front trigger → dominant = `a`) but **tonic** after an
  `a`-root (`a` = the same vowel).
- Therefore a suffix's *spelling* does not by itself tell you its function: you need the root's class.
  **Parsing is unaffected** (identity lives in the consonant; the grade follows from the category), so
  the system is **doubly redundant** — which is exactly what a sung language wants.
- In a noun, the outermost slot is the **case**, so **a noun's chord = its case's function**.
- The redundancy is deliberate: it is the mitigation for §F (unstressed one-syllable case suffixes are
  where sung intelligibility dies first).







