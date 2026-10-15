# Lomissifil

> **Lomissifil is the PROJECT name, not the language name.** The language itself is still unnamed
> (`docs/decisions/03-open-questions.md` §0 item 17).

A **constructed language** designed to sound beautiful in **epic/powerful power metal ·
emotionally delicate post-rock · resonant symphonic vocals · ethereal nostalgic folk**.
Standing priority order (`.clinerules/colang.md`):

1. **beauty** — music, poetry, novel;
2. **neutrality** — no loanwords, not too much like any one natural language;
3. **typability** — ASCII letters only, no custom symbols.

## Start here

| If you want… | Read |
|---|---|
| **the design itself** (index + decision log + quick reference) | `docs/decisions/00-README.md` |
| **what is still pending** — the ONLY authority for open items | `docs/decisions/03-open-questions.md` §0 |
| **the rules of the workspace** (goal, example policy, doc map) | `.clinerules/colang.md` |
| **how to continue / background + tooling** | `docs/draft/handoff.md` |
| **which words may be used in examples** — the only source | `reference/example.md` |
| **the audio/synthesiser history (retired)** | `archive/README.md` |

## Layout

```
README.md                     this file — the map
.clinerules/colang.md         workspace rules (read before editing)
docs/
  decisions/                  LOCKED design + decision log + open questions
    00-README.md              index · status · decision log · action items
    01-phonology.md           inventory, phonotactics, stress
    02-notation.md            spelling policy + expressive notation
    03-open-questions.md      what is NOT decided yet (§0 = canonical list)
    04-lexicon-capacity.md    capacity (historical — superseded by 05)
    05-root-shape-limit.md    capacity under the tighter root-shape rule
    06-neutrality.md          the donor ledger (goal 2)
  draft/                      working material (NOT locked)
    handoff.md                background, tooling, how to continue
    brainstorm.md             scratch record of the grade discussion (§1–§9h)
    01-first-lines.md         the first integration test (legal clauses)
data/
  README.md                   what the generated data is (and is not)
  generated/                  machine output — NEVER annotate (lost on regeneration)
  hand/                       hand-written: picks.md, proposed.md
reference/example.md          the lexicon: the ONLY place example words may come from
tools/                        the scripts that check and generate everything
  archive/                    retired scripts (do NOT re-run)
archive/README.md             retired material + its history
```

## Hard rules (do not violate)

- **Examples** (decisions, textbook) may use **only** words already in `reference/example.md`.
- **Generated files are never annotated** — `data/generated/*` is overwritten on regeneration;
  notes belong in `data/hand/` or the decision log.
- **No tone/pitch**, and the language **never *sounds* chords**. "tonic / subdominant / dominant"
  are **metaphors** for three vowel-colour classes — see the terminology warning at the top of
  `docs/decisions/00-README.md`.
- **Pending items live only in `docs/decisions/03-open-questions.md` §0.**

## Regenerate the data

All scripts are run from the repo root and are deterministic (fixed `--seed`):

```
python3 tools/enumerate_roots.py --pack --config current --seeds 4 --emit data/generated/roots-bases-current.txt
python3 tools/menu.py        > data/generated/menu.md
python3 tools/syllabify.py --sheet > data/generated/picks-sheet.md
python3 tools/seam.py        > data/generated/seam-sheet.md
```

Checkers: `python3 tools/syllabify.py --check`, `python3 tools/check_roots.py`,
`python3 tools/check_suffixes.py`, `python3 tools/grades.py --selftest`,
`python3 tools/clause.py --selftest` (a whole clause: cases, chords, class warnings),
`python3 tools/neutrality.py --selftest` (the donor ledger, recounted from the table itself),
`python3 tools/fingerprint.py --profile`.
