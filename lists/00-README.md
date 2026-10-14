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
| lines | **26,751** bases |
| sha1 | `2cedb3f520e0b63c1494f51ec9bcb106a32c431f` (was mislabelled *sha256*; a 40-hex digest is a **sha1** — verified 2026-10-14) |
| sha256 | `57f683f25c5521eaead632005c9fb5a9714fd7bd9c87686ddbe31938d4c08205` |
| encoding | ASCII, lowercase `a`–`z` only, one base per line, **sorted** |
| config | `current` — 15 nuclei · O1=18 · O2=27 · O2c=16 · codas `m n l r s` |
| base space | 457,425 (4 main shapes) + 76 leaps = **457,501** |
| selection | greedy packing, pairwise **segment-distance ≥ 2**, best of 4 seeds |
| ⇒ coined roots | **~53,502** — each base yields exactly **2** roots (see below) |

Regenerate with exactly:

```
python3 tools/enumerate_roots.py --pack --config current --seeds 4 --emit lists/roots-bases-current.txt
```

**Reproducibility (honest caveat).** The winning pack is **seed 0 = the unshuffled order**, so the
file is deterministic *for this command*. If you pass **more** seeds a shuffled order may beat it
and the file will legitimately differ — that is a better pack, not a bug.

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

### What is deliberately NOT here

- The `legacy-mono4` / `legacy-diph4` / `legacy-core` configs reproduce `decision/05`'s own figures
  (48,020 / 220,500 / 264,600) — **validation only**, not a coining source.
- Earlier 16,148- and 20,025-base lists existed **only in `/tmp` and were superseded**: they predate
  the single-onset → cluster model change (`decision/05-root-shape-limit.md`, UPDATE **§6**), so they
  were **not** copied in — they contained **no clusters at all**.
