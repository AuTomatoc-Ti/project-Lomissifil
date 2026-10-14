# audio/ — audition material (generated, NOT words)

Everything here is **synthesised** with `espeak-ng -v fi` — the engine described in
`../draft/handoff.md` and **rejected on 2026-10-14** (see the banner below). These are
**non-semantic sound-strings**: no meaning is claimed, and
**nothing here is a word** — examples may still only use `../reference/example.md`
(`.clinerules/colang.md`).

They used to live in `/tmp/lomissifil-audition/`, which is wiped on reboot. They now live here so
you can find them. ⚠️ The `/tmp` copies still exist and are **not** the canonical ones.

> ⛔ **FROZEN — do not generate more (author's ruling, 2026-10-14).** `espeak-ng` output is judged
> **rough and unneutral** (a Finnish voice is forced onto the language), so **no further WAVs will be
> generated, here or in `/tmp`**. This directory is a **historical record** of the tests that *did*
> run — do **not** re-run `tools/audition_*.py`. What replaces it is **still open**
> (`../decision/03-open-questions.md` §0 item 19), and the **M1 full re-test** (§A.2 there) must now
> be done **live**, not through a synthesiser.

## Files

| file | what to listen for |
|---|---|
| `01-suffix-chain.wav` | M1 direction — the 4 roots × 7 cases, as **suffixes** |
| `02-prefix-chain.wav` | the same morphemes as **prefixes** |
| `03-ab-both-ways-seli.wav` | direct A/B: suffix, then prefix, case by case |
| `04-rhyme-acc.wav` · `04-rhyme-dat.wav` | the rhyme consequence (same case, different root class) |
| `05-seam-vinitial.wav` | the prefix seam (`niarGonna` … are illegal) |
| `roots-01.wav` … `roots-06.wav` | candidate bare roots (step 3) |
| `roots-index.txt` | one line per base, its 4 numbered forms |

**M1 was accepted by ear on 2026-10-14** (`../decision/03-open-questions.md` §A.2) — so `01`–`05`
are the record of that test, not a pending task.

## The roots audition (`roots-01`…`06`, 48 bases = 192 forms)

Each **group of 4 = one base**, in a fixed order:

```
  1 thasthof   |   2 thasthow   |   3 thasthoh   |   4 thastho
  base+f       |   base+w(/v/)  |   base+h       |   bare (no final)
```

By **R1/R3** each base yields **exactly 2** roots (one from `{f, w}`, one from `{h, <nothing>}`),
so **pick at most one from each column pair** — but for the audition just mark what sounds good.
`w` = /v/; the letter **`v` is the vibrato mark, not a letter**, so a /v/-final root is `…w`.

**Workflow (historical):** play a file, read `roots-index.txt`, note the numbers (they are continuous
across the six files: 1–32, 33–64, … 161–192). ~4–6 favourites per file is plenty to start.
⚠️ Since the synthesiser was **rejected on 2026-10-14** (banner above), the working signal is now the
**written list** — read `roots-index.txt` and record picks in `../lists/picks.md`.

The command that produced this material (~~regenerate~~ — **do not re-run**):

```
python3 tools/audition_roots.py --out audio --bases 48 > audio/roots-index.txt 2>&1
```

(`--src` defaults to `../lists/roots-bases-current.txt`, so the sample follows the current rule set.
`--seed` is fixed, so the same 48 bases come back.)

> `tools/audition_m1.py` has no `--out` option yet, so it still writes to `/tmp/lomissifil-audition/`.
> The `01`–`05` files here are copies of that run.

## Why these are big, and what to do about git

12 WAVs ≈ **11.5 MB** of uncompressed PCM. `.gitignore` currently ignores only `.DS_Store`. If you
do **not** want them in history, add `audio/*.wav` to `.gitignore` (the `.txt` index is small and
worth keeping). On macOS they can also be shrunk ~10x with `afconvert -f m4af -d aac` if you would
rather keep the audio itself under version control.
