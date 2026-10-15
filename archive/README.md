# archive/ — retired material (history, NOT live)

This folder records material that the design process **retired**. Nothing here is a decision,
and nothing here may be built on. It exists so the rest of the repo can stop referring to files
that are no longer there.

## The synthesiser audition (`audio/`) — REJECTED 2026-10-14

The M1 A/B test and the roots audition were once produced as **WAV files** with `espeak-ng -v fi`.
The author judged that output **rough and unneutral** (it imposes a Finnish voice on the language),
so **no further WAVs are to be generated — this round or in future**
(`../docs/decisions/03-open-questions.md` §0 item 19).

⚠️ **Honest state of the repo (found during the 2026-10-15 tidy-up).** The `.wav` files were
**never committed** (`.gitignore` ignores `*.wav`), and neither the audition index
(`roots-index.txt`) nor the folder's own banner was ever tracked. The `audio/` folder therefore
arrived **empty** and has been **removed**. Its history lives **here and in the decision log**,
not in files — which is why earlier documents that pointed at `audio/…` now point at this file.

**What replaced it (the live method):** the author **reads the written forms aloud** — the
orthography is 1:1, so spelling → sound needs no engine
(`../docs/decisions/03-open-questions.md` §0 item 19c). The material for that is
`../data/generated/seam-sheet.md` (the M3a seam) and `../data/generated/picks-sheet.md`
(48 bases × 7 forms).

**Retired tooling:** `../tools/archive/audition_m1.py`, `../tools/archive/audition_roots.py`
— **historical, do NOT re-run**.
