# lists/ — generated data (NOT vocabulary)

This directory holds **generated** lists: data for the design process, not decisions, and **not**
the example word list. It is the only place in this repo that holds `.txt` — deliberately, because
these files are machine-produced, whereas everything else here is prose (`.md`).

> ⚠️ **`reference/example.md` remains the ONLY place words may come from in examples**
> (`.clinerules/colang.md`). **Nothing in `lists/` is a word yet.**

> ⚠️ **Annotations written inside a generated file are LOST on regeneration.** Picks therefore live
> in **`lists/picks.md`** (hand-written, never machine-generated) — never inside the `.txt`.

## `roots-bases-current.txt` — the coining source

| | |
|---|---|
| lines | **26,484** bases |
| sha1 | `f532e58e3cfe45e66835a615eebc7a3b0f1a38e0` |
| sha256 | `7404a917639955801aea18d195070ad8f68b0cb19ebcb04150478d530906dab3` |
| encoding | ASCII, lowercase `a`–`z` only, one base per line, **sorted** |
| config | `current` — 15 nuclei · O1=18 · O2=27 · O2c=16 · codas `m n l r s` |
| base space | **453,150** (4 main shapes) + 76 leaps = **453,226** — P6 (2026-10-14); the older `457,425 / 457,501` family predates the `/s/`+`/h/` exclusion, see `../decision/05-root-shape-limit.md` P6 UPDATE |
| selection | greedy packing, pairwise **segment-distance ≥ 2**, best of 4 seeds |
| ⇒ coined roots | **~52,968** — each base yields exactly **2** roots (see below) |

Regenerate with exactly:

```
python3 tools/enumerate_roots.py --pack --config current --seeds 4 --emit lists/roots-bases-current.txt
```

**Reproducibility (honest caveat).** The winning pack is **seed 0 = the unshuffled order**, so the
file is deterministic *for this command*. If you pass **more** seeds a shuffled order may beat it
and the file will legitimately differ — that is a better pack, not a bug. (Confirmed on the P6
re-emission: seed 0 → **26,484**; seeds 1-3 → 21,4xx each. Seed 0 also reproduces exactly the
*unique* line count of the pre-P6 file, i.e. the only real change was dropping its 267 duplicates and
respelling under P6.)

### A base is NOT yet a root

By **R1 / R3** (`decision/00-README.md`), every base yields **exactly 2** bare roots: one from the
`{f, w}` branch and one from the `{h, <nothing>}` branch. (`w` = /v/; the letter **`v` is the
*vibrato* mark**, not a letter — so a /v/-final root is `…w`, never `…v`.) To see all four raw
candidates of a base:

```
python3 tools/enumerate_roots.py --pairs 20        # samples 20 bases, 4 forms each
```

> ⚠️ **R3 is PARKED.** The branches *will* carry grammatical meaning, but the content is undecided,
> so **coinage is SOUND-ONLY for now** — do not assign pair semantics
> (`decision/03-open-questions.md` §0 item 14).

## `picks-sheet.md` — the readable form of the same audition (generated `.md`)

The synthesiser is rejected (`../decision/03-open-questions.md` §0 item 19), so the audition signal is
now the **written form** — and the raw index (`../audio/roots-index.txt`) shows neither the syllable
split nor the stress. `picks-sheet.md` adds both, computed by `tools/syllabify.py` from the locked
rules (nothing new is invented in that script):

```
python3 tools/syllabify.py --sheet > lists/picks-sheet.md
python3 tools/syllabify.py --check          # verifies the splitter against the reference words
python3 tools/syllabify.py --stats          # histogram of a whole list: syllables + both flags
```

`--stats` on the current pack (re-emitted 2026-10-14, after P6): **26,484 forms, 100% two-syllable,
0 illegal, 15.1% stressed on a digraph, 9.1% read as ONE phoneme (`sh`/`ng`, P6), 2,142 (8.1%) with a
P6 hard spelling (`mp np mt nt mk nk`), and 0 ILLEGAL under P6**. The pack is **clean**: no duplicate
spellings, no P6-illegal forms. (The *previous* file — `26,751` bases, sha1 `2cedb3f5…` — predated P6:
it held **1,338** P6-illegal spellings and **267 duplicate lines** = pairs at distance 0, which
contradicted the "pairwise ≥ 2" claim below. Both defects are gone; the old file is in git history.)
⚠️ It is still **100% two-syllable**: the pack covers the 2-syllable core only, so it contains **no
`roi`-class short root** — see `../decision/03-open-questions.md` §0 item 22.

It is the **same 48 bases with the same numbering** as `../audio/roots-index.txt`. It is generated, so
**never annotate it** — the picks belong in `picks.md`. Two things it flags, both genuine open/undecided
points rather than script opinions:

- a **stressed syllable that begins with a digraph** (`sh` / `th` / `ng` / `ae`) — N1 has no rule for
  that case yet;
- **`sh` / `ng` where the coda+onset reading is also legal** (`a-sha` vs `as-ha`, `so-nga` vs `son-ga`).

## `menu.md` — the coining menu (generated; deliberately BIASED)

The author's ruling (2026-10-14): the menu ranks the pool so that **material nobody else has floats
to the top**, using the measurement in `../decision/06-neutrality.md` ("Measurement"):

```
python3 tools/menu.py > lists/menu.md                 # top 20 + every onset + every first vowel
python3 tools/menu.py --group th --per 6              # browse one sound in depth
```

| points | trigger | why it counts as ours |
|---|---|---|
| **+2** | word-final `f`/`w`/`h` | the area rule (A15) — no donor |
| **+2** | an intervocalic cluster `fm fn hm hn wm wn jm jn` | A13 — near-unattested |
| **+2** | a hiatus leap `iu yu ia ya` | A4 — no donor |
| **+1** | an onset cluster `pr br tr dr kr gr` | A12 — a whitelist, not a copy |
| **-2** | the form **IS an English word** | 143 of 105,936 forms (0.135%) are |

Every row shows its reasons, so the ordering can be audited; the weights live in one place
(`tools/menu.py`, `score()`). The menu also ends with the **English collision list**, so a pick can
never hit a real English word by accident. It is generated: **picks go in `picks.md`** (record the
form TEXT, not just the menu's number).

## `seam-sheet.md` — the M3a seam, to be read ALOUD (generated)

The seam (a root ending in `f`/`w`/`h` + a suffix) fires for **3 of every 4** coined roots, lands
**unstressed**, and has never been judged by ear — and the synthesiser is rejected. The author's
method (2026-10-14) is therefore **reading the written forms aloud**, and this file is that material:

```
python3 tools/seam.py > lists/seam-sheet.md          # 6 bases x (3 finals + bare) x 9 suffixes
python3 tools/seam.py --bases 12 --seed 7            # more material, another sample
```

Each table shows a root with all 9 suffixes (7 cases + 2 verb classes), the **seam tier** that fired,
and the stress **counted from the root** (P4c — so a suffix never steals the stress). The closing
section, "Do the siblings stay distinct?", is the reason the `<= 2 per base` rule in `picks.md` is a
**correctness** rule: the two alternatives inside one branch collide in GEN/INS/OBL/V1.

⚠️ It also **verifies** M3a: **tier 3 (the copied vowel) never fires** for the current suffix set,
because all 9 suffixes start with `m n l r s` and tiers 1-2 cover all 15 combinations — so the seam is
fully determined today, and tier 3 is future-proofing for suffixes that do not exist yet.

### What is deliberately NOT here

- The `legacy-mono4` / `legacy-diph4` / `legacy-core` configs reproduce `decision/05`'s own figures
  (48,020 / 220,500 / 264,600) — **validation only**, not a coining source.
- Earlier 16,148- and 20,025-base lists existed **only in `/tmp` and were superseded**: they predate
  the single-onset → cluster model change (`decision/05-root-shape-limit.md`, UPDATE **§6**), so they
  were **not** copied in — they contained **no clusters at all**.
