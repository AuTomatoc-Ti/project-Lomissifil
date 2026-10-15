# data/generated/menu.md - GENERATED coining menu. DO NOT ANNOTATE HERE.

Regenerate with:

```
python3 tools/menu.py > data/generated/menu.md
```

**Picks go in `data/hand/picks.md`** - record the FORM TEXT, not just a number. Any note written in this
file is lost on regeneration.

## The ranking is deliberate (author's ruling 2026-10-14)

`tools/fingerprint.py` measured which parts of our sound profile are **un-donated** (see
`../../docs/decisions/06-neutrality.md` -> "Measurement"). This menu pushes those to the top:

| points | what triggers it | why it counts as ours |
|---|---|---|
| **+2** | word-final `f` / `w` / `h` | the **area rule** (A15) - no language in the reference set does this |
| **+2** | an intervocalic cluster `fm fn hm hn wm wn jm jn` | A13 - near-unattested |
| **+2** | a hiatus "leap" `iu yu ia ya` | A4 - a designed 2x2, no donor |
| **+1** | an onset cluster `pr br tr dr kr gr` | A12 - a whitelist, not a copy of any language |
| **-1** | an `s`-final form | **R4**: the `s` branch is RESERVED for a future adjective / adverb job, so `s`-final roots are meant to be **RARE** (author's ruling) |
| **-2** | the form **IS an English word** | measured: 421 of 133,845 forms (0.315%) are in Webster's 2nd |

Every row shows **why** it scored. The weights live in one place: `tools/menu.py`, `score()`.

⚠️ This biases the *shortlist*, never the language: the pool is untouched, and a low score is not a
verdict - it only means "this form is built from material that many languages share".

## How to read a row

`#` is this menu's own numbering. `syllables` and `stress` come from `tools/syllabify.py` (default
stress = the 2nd syllable of the root, P4/N1; the capital lands on the *first letter* of the stressed
syllable). **A group of seven rows is ONE base**, in the fixed order
`+f | +w (/v/) | +h | +s | +m | +r | bare`, and a base yields exactly **2** roots - so pick **at most
one** from the `{+f, +w}` pair and **at most one** from the `{+h, +s, +m, +r, bare}` group. (`+s` is
reserved for adjective/adverb duty, `+m` suits front-vowel roots, `+r` is for function words -- see
**R4**/**R6** in the decision log; the menu prints a soft-rule note when a form breaks one.)

> Sound-only: R3 is PARKED, so assign **no meanings** (`../../docs/decisions/03-open-questions.md` section 0
> item 14). A pick is not a word; `../../reference/example.md` stays the only source for examples.

---
## Top 20 bases - the most "ours" material

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 1 | braefmae | braefmaef | brae-fmaef | braeFmaef | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 2 | braefmae | braefmaew | brae-fmaew | braeFmaew | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 3 | braefmae | braefmaeh | brae-fmaeh | braeFmaeh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 4 | braefmae | braefmaes | brae-fmaes | braeFmaes | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster br (+1) |
| 5 | braefmae | braefmaem | brae-fmaem | braeFmaem | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 6 | braefmae | braefmaer | brae-fmaer | braeFmaer | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 7 | braefmae | braefmae | brae-fmae | braeFmae | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 8 | braefnae | braefnaef | brae-fnaef | braeFnaef | +5 | area-rule final (+2); un-donated cluster fn (+2); onset cluster br (+1) |
| 9 | braefnae | braefnaew | brae-fnaew | braeFnaew | +5 | area-rule final (+2); un-donated cluster fn (+2); onset cluster br (+1) |
| 10 | braefnae | braefnaeh | brae-fnaeh | braeFnaeh | +5 | area-rule final (+2); un-donated cluster fn (+2); onset cluster br (+1) |
| 11 | braefnae | braefnaes | brae-fnaes | braeFnaes | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fn (+2); onset cluster br (+1) |
| 12 | braefnae | braefnaem | brae-fnaem | braeFnaem | +3 | un-donated cluster fn (+2); onset cluster br (+1) |
| 13 | braefnae | braefnaer | brae-fnaer | braeFnaer | +3 | un-donated cluster fn (+2); onset cluster br (+1) |
| 14 | braefnae | braefnae | brae-fnae | braeFnae | +3 | un-donated cluster fn (+2); onset cluster br (+1) |
| 15 | braehmae | braehmaef | brae-hmaef | braeHmaef | +5 | area-rule final (+2); un-donated cluster hm (+2); onset cluster br (+1) |
| 16 | braehmae | braehmaew | brae-hmaew | braeHmaew | +5 | area-rule final (+2); un-donated cluster hm (+2); onset cluster br (+1) |
| 17 | braehmae | braehmaeh | brae-hmaeh | braeHmaeh | +5 | area-rule final (+2); un-donated cluster hm (+2); onset cluster br (+1) |
| 18 | braehmae | braehmaes | brae-hmaes | braeHmaes | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster hm (+2); onset cluster br (+1) |
| 19 | braehmae | braehmaem | brae-hmaem | braeHmaem | +3 | un-donated cluster hm (+2); onset cluster br (+1) |
| 20 | braehmae | braehmaer | brae-hmaer | braeHmaer | +3 | un-donated cluster hm (+2); onset cluster br (+1) |
| 21 | braehmae | braehmae | brae-hmae | braeHmae | +3 | un-donated cluster hm (+2); onset cluster br (+1) |
| 22 | braehnae | braehnaef | brae-hnaef | braeHnaef | +5 | area-rule final (+2); un-donated cluster hn (+2); onset cluster br (+1) |
| 23 | braehnae | braehnaew | brae-hnaew | braeHnaew | +5 | area-rule final (+2); un-donated cluster hn (+2); onset cluster br (+1) |
| 24 | braehnae | braehnaeh | brae-hnaeh | braeHnaeh | +5 | area-rule final (+2); un-donated cluster hn (+2); onset cluster br (+1) |
| 25 | braehnae | braehnaes | brae-hnaes | braeHnaes | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster hn (+2); onset cluster br (+1) |
| 26 | braehnae | braehnaem | brae-hnaem | braeHnaem | +3 | un-donated cluster hn (+2); onset cluster br (+1) |
| 27 | braehnae | braehnaer | brae-hnaer | braeHnaer | +3 | un-donated cluster hn (+2); onset cluster br (+1) |
| 28 | braehnae | braehnae | brae-hnae | braeHnae | +3 | un-donated cluster hn (+2); onset cluster br (+1) |
| 29 | braeifmaei | braeifmaeif | braei-fmaeif | braeiFmaeif | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 30 | braeifmaei | braeifmaeiw | braei-fmaeiw | braeiFmaeiw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 31 | braeifmaei | braeifmaeih | braei-fmaeih | braeiFmaeih | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 32 | braeifmaei | braeifmaeis | braei-fmaeis | braeiFmaeis | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster br (+1) |
| 33 | braeifmaei | braeifmaeim | braei-fmaeim | braeiFmaeim | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 34 | braeifmaei | braeifmaeir | braei-fmaeir | braeiFmaeir | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 35 | braeifmaei | braeifmaei | braei-fmaei | braeiFmaei | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 36 | braeifnaei | braeifnaeif | braei-fnaeif | braeiFnaeif | +5 | area-rule final (+2); un-donated cluster fn (+2); onset cluster br (+1) |
| 37 | braeifnaei | braeifnaeiw | braei-fnaeiw | braeiFnaeiw | +5 | area-rule final (+2); un-donated cluster fn (+2); onset cluster br (+1) |
| 38 | braeifnaei | braeifnaeih | braei-fnaeih | braeiFnaeih | +5 | area-rule final (+2); un-donated cluster fn (+2); onset cluster br (+1) |
| 39 | braeifnaei | braeifnaeis | braei-fnaeis | braeiFnaeis | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fn (+2); onset cluster br (+1) |
| 40 | braeifnaei | braeifnaeim | braei-fnaeim | braeiFnaeim | +3 | un-donated cluster fn (+2); onset cluster br (+1) |
| 41 | braeifnaei | braeifnaeir | braei-fnaeir | braeiFnaeir | +3 | un-donated cluster fn (+2); onset cluster br (+1) |
| 42 | braeifnaei | braeifnaei | braei-fnaei | braeiFnaei | +3 | un-donated cluster fn (+2); onset cluster br (+1) |
| 43 | braeihmaei | braeihmaeif | braei-hmaeif | braeiHmaeif | +5 | area-rule final (+2); un-donated cluster hm (+2); onset cluster br (+1) |
| 44 | braeihmaei | braeihmaeiw | braei-hmaeiw | braeiHmaeiw | +5 | area-rule final (+2); un-donated cluster hm (+2); onset cluster br (+1) |
| 45 | braeihmaei | braeihmaeih | braei-hmaeih | braeiHmaeih | +5 | area-rule final (+2); un-donated cluster hm (+2); onset cluster br (+1) |
| 46 | braeihmaei | braeihmaeis | braei-hmaeis | braeiHmaeis | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster hm (+2); onset cluster br (+1) |
| 47 | braeihmaei | braeihmaeim | braei-hmaeim | braeiHmaeim | +3 | un-donated cluster hm (+2); onset cluster br (+1) |
| 48 | braeihmaei | braeihmaeir | braei-hmaeir | braeiHmaeir | +3 | un-donated cluster hm (+2); onset cluster br (+1) |
| 49 | braeihmaei | braeihmaei | braei-hmaei | braeiHmaei | +3 | un-donated cluster hm (+2); onset cluster br (+1) |
| 50 | braeihnaei | braeihnaeif | braei-hnaeif | braeiHnaeif | +5 | area-rule final (+2); un-donated cluster hn (+2); onset cluster br (+1) |
| 51 | braeihnaei | braeihnaeiw | braei-hnaeiw | braeiHnaeiw | +5 | area-rule final (+2); un-donated cluster hn (+2); onset cluster br (+1) |
| 52 | braeihnaei | braeihnaeih | braei-hnaeih | braeiHnaeih | +5 | area-rule final (+2); un-donated cluster hn (+2); onset cluster br (+1) |
| 53 | braeihnaei | braeihnaeis | braei-hnaeis | braeiHnaeis | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster hn (+2); onset cluster br (+1) |
| 54 | braeihnaei | braeihnaeim | braei-hnaeim | braeiHnaeim | +3 | un-donated cluster hn (+2); onset cluster br (+1) |
| 55 | braeihnaei | braeihnaeir | braei-hnaeir | braeiHnaeir | +3 | un-donated cluster hn (+2); onset cluster br (+1) |
| 56 | braeihnaei | braeihnaei | braei-hnaei | braeiHnaei | +3 | un-donated cluster hn (+2); onset cluster br (+1) |
| 57 | braeijmaei | braeijmaeif | braei-jmaeif | braeiJmaeif | +5 | area-rule final (+2); un-donated cluster jm (+2); onset cluster br (+1) |
| 58 | braeijmaei | braeijmaeiw | braei-jmaeiw | braeiJmaeiw | +5 | area-rule final (+2); un-donated cluster jm (+2); onset cluster br (+1) |
| 59 | braeijmaei | braeijmaeih | braei-jmaeih | braeiJmaeih | +5 | area-rule final (+2); un-donated cluster jm (+2); onset cluster br (+1) |
| 60 | braeijmaei | braeijmaeis | braei-jmaeis | braeiJmaeis | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster jm (+2); onset cluster br (+1) |
| 61 | braeijmaei | braeijmaeim | braei-jmaeim | braeiJmaeim | +3 | un-donated cluster jm (+2); onset cluster br (+1) |
| 62 | braeijmaei | braeijmaeir | braei-jmaeir | braeiJmaeir | +3 | un-donated cluster jm (+2); onset cluster br (+1) |
| 63 | braeijmaei | braeijmaei | braei-jmaei | braeiJmaei | +3 | un-donated cluster jm (+2); onset cluster br (+1) |
| 64 | braeijnaei | braeijnaeif | braei-jnaeif | braeiJnaeif | +5 | area-rule final (+2); un-donated cluster jn (+2); onset cluster br (+1) |
| 65 | braeijnaei | braeijnaeiw | braei-jnaeiw | braeiJnaeiw | +5 | area-rule final (+2); un-donated cluster jn (+2); onset cluster br (+1) |
| 66 | braeijnaei | braeijnaeih | braei-jnaeih | braeiJnaeih | +5 | area-rule final (+2); un-donated cluster jn (+2); onset cluster br (+1) |
| 67 | braeijnaei | braeijnaeis | braei-jnaeis | braeiJnaeis | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster jn (+2); onset cluster br (+1) |
| 68 | braeijnaei | braeijnaeim | braei-jnaeim | braeiJnaeim | +3 | un-donated cluster jn (+2); onset cluster br (+1) |
| 69 | braeijnaei | braeijnaeir | braei-jnaeir | braeiJnaeir | +3 | un-donated cluster jn (+2); onset cluster br (+1) |
| 70 | braeijnaei | braeijnaei | braei-jnaei | braeiJnaei | +3 | un-donated cluster jn (+2); onset cluster br (+1) |
| 71 | braeiwmaei | braeiwmaeif | braei-wmaeif | braeiWmaeif | +5 | area-rule final (+2); un-donated cluster wm (+2); onset cluster br (+1) |
| 72 | braeiwmaei | braeiwmaeiw | braei-wmaeiw | braeiWmaeiw | +5 | area-rule final (+2); un-donated cluster wm (+2); onset cluster br (+1) |
| 73 | braeiwmaei | braeiwmaeih | braei-wmaeih | braeiWmaeih | +5 | area-rule final (+2); un-donated cluster wm (+2); onset cluster br (+1) |
| 74 | braeiwmaei | braeiwmaeis | braei-wmaeis | braeiWmaeis | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster wm (+2); onset cluster br (+1) |
| 75 | braeiwmaei | braeiwmaeim | braei-wmaeim | braeiWmaeim | +3 | un-donated cluster wm (+2); onset cluster br (+1) |
| 76 | braeiwmaei | braeiwmaeir | braei-wmaeir | braeiWmaeir | +3 | un-donated cluster wm (+2); onset cluster br (+1) |
| 77 | braeiwmaei | braeiwmaei | braei-wmaei | braeiWmaei | +3 | un-donated cluster wm (+2); onset cluster br (+1) |
| 78 | braeiwnaei | braeiwnaeif | braei-wnaeif | braeiWnaeif | +5 | area-rule final (+2); un-donated cluster wn (+2); onset cluster br (+1) |
| 79 | braeiwnaei | braeiwnaeiw | braei-wnaeiw | braeiWnaeiw | +5 | area-rule final (+2); un-donated cluster wn (+2); onset cluster br (+1) |
| 80 | braeiwnaei | braeiwnaeih | braei-wnaeih | braeiWnaeih | +5 | area-rule final (+2); un-donated cluster wn (+2); onset cluster br (+1) |
| 81 | braeiwnaei | braeiwnaeis | braei-wnaeis | braeiWnaeis | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster wn (+2); onset cluster br (+1) |
| 82 | braeiwnaei | braeiwnaeim | braei-wnaeim | braeiWnaeim | +3 | un-donated cluster wn (+2); onset cluster br (+1) |
| 83 | braeiwnaei | braeiwnaeir | braei-wnaeir | braeiWnaeir | +3 | un-donated cluster wn (+2); onset cluster br (+1) |
| 84 | braeiwnaei | braeiwnaei | braei-wnaei | braeiWnaei | +3 | un-donated cluster wn (+2); onset cluster br (+1) |
| 85 | braejmae | braejmaef | brae-jmaef | braeJmaef | +5 | area-rule final (+2); un-donated cluster jm (+2); onset cluster br (+1) |
| 86 | braejmae | braejmaew | brae-jmaew | braeJmaew | +5 | area-rule final (+2); un-donated cluster jm (+2); onset cluster br (+1) |
| 87 | braejmae | braejmaeh | brae-jmaeh | braeJmaeh | +5 | area-rule final (+2); un-donated cluster jm (+2); onset cluster br (+1) |
| 88 | braejmae | braejmaes | brae-jmaes | braeJmaes | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster jm (+2); onset cluster br (+1) |
| 89 | braejmae | braejmaem | brae-jmaem | braeJmaem | +3 | un-donated cluster jm (+2); onset cluster br (+1) |
| 90 | braejmae | braejmaer | brae-jmaer | braeJmaer | +3 | un-donated cluster jm (+2); onset cluster br (+1) |
| 91 | braejmae | braejmae | brae-jmae | braeJmae | +3 | un-donated cluster jm (+2); onset cluster br (+1) |
| 92 | braejnae | braejnaef | brae-jnaef | braeJnaef | +5 | area-rule final (+2); un-donated cluster jn (+2); onset cluster br (+1) |
| 93 | braejnae | braejnaew | brae-jnaew | braeJnaew | +5 | area-rule final (+2); un-donated cluster jn (+2); onset cluster br (+1) |
| 94 | braejnae | braejnaeh | brae-jnaeh | braeJnaeh | +5 | area-rule final (+2); un-donated cluster jn (+2); onset cluster br (+1) |
| 95 | braejnae | braejnaes | brae-jnaes | braeJnaes | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster jn (+2); onset cluster br (+1) |
| 96 | braejnae | braejnaem | brae-jnaem | braeJnaem | +3 | un-donated cluster jn (+2); onset cluster br (+1) |
| 97 | braejnae | braejnaer | brae-jnaer | braeJnaer | +3 | un-donated cluster jn (+2); onset cluster br (+1) |
| 98 | braejnae | braejnae | brae-jnae | braeJnae | +3 | un-donated cluster jn (+2); onset cluster br (+1) |
| 99 | braeufmaeu | braeufmaeuf | braeu-fmaeuf | braeuFmaeuf | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 100 | braeufmaeu | braeufmaeuw | braeu-fmaeuw | braeuFmaeuw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 101 | braeufmaeu | braeufmaeuh | braeu-fmaeuh | braeuFmaeuh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 102 | braeufmaeu | braeufmaeus | braeu-fmaeus | braeuFmaeus | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster br (+1) |
| 103 | braeufmaeu | braeufmaeum | braeu-fmaeum | braeuFmaeum | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 104 | braeufmaeu | braeufmaeur | braeu-fmaeur | braeuFmaeur | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 105 | braeufmaeu | braeufmaeu | braeu-fmaeu | braeuFmaeu | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 106 | braeufnaeu | braeufnaeuf | braeu-fnaeuf | braeuFnaeuf | +5 | area-rule final (+2); un-donated cluster fn (+2); onset cluster br (+1) |
| 107 | braeufnaeu | braeufnaeuw | braeu-fnaeuw | braeuFnaeuw | +5 | area-rule final (+2); un-donated cluster fn (+2); onset cluster br (+1) |
| 108 | braeufnaeu | braeufnaeuh | braeu-fnaeuh | braeuFnaeuh | +5 | area-rule final (+2); un-donated cluster fn (+2); onset cluster br (+1) |
| 109 | braeufnaeu | braeufnaeus | braeu-fnaeus | braeuFnaeus | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fn (+2); onset cluster br (+1) |
| 110 | braeufnaeu | braeufnaeum | braeu-fnaeum | braeuFnaeum | +3 | un-donated cluster fn (+2); onset cluster br (+1) |
| 111 | braeufnaeu | braeufnaeur | braeu-fnaeur | braeuFnaeur | +3 | un-donated cluster fn (+2); onset cluster br (+1) |
| 112 | braeufnaeu | braeufnaeu | braeu-fnaeu | braeuFnaeu | +3 | un-donated cluster fn (+2); onset cluster br (+1) |
| 113 | braeuhmaeu | braeuhmaeuf | braeu-hmaeuf | braeuHmaeuf | +5 | area-rule final (+2); un-donated cluster hm (+2); onset cluster br (+1) |
| 114 | braeuhmaeu | braeuhmaeuw | braeu-hmaeuw | braeuHmaeuw | +5 | area-rule final (+2); un-donated cluster hm (+2); onset cluster br (+1) |
| 115 | braeuhmaeu | braeuhmaeuh | braeu-hmaeuh | braeuHmaeuh | +5 | area-rule final (+2); un-donated cluster hm (+2); onset cluster br (+1) |
| 116 | braeuhmaeu | braeuhmaeus | braeu-hmaeus | braeuHmaeus | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster hm (+2); onset cluster br (+1) |
| 117 | braeuhmaeu | braeuhmaeum | braeu-hmaeum | braeuHmaeum | +3 | un-donated cluster hm (+2); onset cluster br (+1) |
| 118 | braeuhmaeu | braeuhmaeur | braeu-hmaeur | braeuHmaeur | +3 | un-donated cluster hm (+2); onset cluster br (+1) |
| 119 | braeuhmaeu | braeuhmaeu | braeu-hmaeu | braeuHmaeu | +3 | un-donated cluster hm (+2); onset cluster br (+1) |
| 120 | braeuhnaeu | braeuhnaeuf | braeu-hnaeuf | braeuHnaeuf | +5 | area-rule final (+2); un-donated cluster hn (+2); onset cluster br (+1) |
| 121 | braeuhnaeu | braeuhnaeuw | braeu-hnaeuw | braeuHnaeuw | +5 | area-rule final (+2); un-donated cluster hn (+2); onset cluster br (+1) |
| 122 | braeuhnaeu | braeuhnaeuh | braeu-hnaeuh | braeuHnaeuh | +5 | area-rule final (+2); un-donated cluster hn (+2); onset cluster br (+1) |
| 123 | braeuhnaeu | braeuhnaeus | braeu-hnaeus | braeuHnaeus | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster hn (+2); onset cluster br (+1) |
| 124 | braeuhnaeu | braeuhnaeum | braeu-hnaeum | braeuHnaeum | +3 | un-donated cluster hn (+2); onset cluster br (+1) |
| 125 | braeuhnaeu | braeuhnaeur | braeu-hnaeur | braeuHnaeur | +3 | un-donated cluster hn (+2); onset cluster br (+1) |
| 126 | braeuhnaeu | braeuhnaeu | braeu-hnaeu | braeuHnaeu | +3 | un-donated cluster hn (+2); onset cluster br (+1) |
| 127 | braeujmaeu | braeujmaeuf | braeu-jmaeuf | braeuJmaeuf | +5 | area-rule final (+2); un-donated cluster jm (+2); onset cluster br (+1) |
| 128 | braeujmaeu | braeujmaeuw | braeu-jmaeuw | braeuJmaeuw | +5 | area-rule final (+2); un-donated cluster jm (+2); onset cluster br (+1) |
| 129 | braeujmaeu | braeujmaeuh | braeu-jmaeuh | braeuJmaeuh | +5 | area-rule final (+2); un-donated cluster jm (+2); onset cluster br (+1) |
| 130 | braeujmaeu | braeujmaeus | braeu-jmaeus | braeuJmaeus | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster jm (+2); onset cluster br (+1) |
| 131 | braeujmaeu | braeujmaeum | braeu-jmaeum | braeuJmaeum | +3 | un-donated cluster jm (+2); onset cluster br (+1) |
| 132 | braeujmaeu | braeujmaeur | braeu-jmaeur | braeuJmaeur | +3 | un-donated cluster jm (+2); onset cluster br (+1) |
| 133 | braeujmaeu | braeujmaeu | braeu-jmaeu | braeuJmaeu | +3 | un-donated cluster jm (+2); onset cluster br (+1) |
| 134 | braeujnaeu | braeujnaeuf | braeu-jnaeuf | braeuJnaeuf | +5 | area-rule final (+2); un-donated cluster jn (+2); onset cluster br (+1) |
| 135 | braeujnaeu | braeujnaeuw | braeu-jnaeuw | braeuJnaeuw | +5 | area-rule final (+2); un-donated cluster jn (+2); onset cluster br (+1) |
| 136 | braeujnaeu | braeujnaeuh | braeu-jnaeuh | braeuJnaeuh | +5 | area-rule final (+2); un-donated cluster jn (+2); onset cluster br (+1) |
| 137 | braeujnaeu | braeujnaeus | braeu-jnaeus | braeuJnaeus | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster jn (+2); onset cluster br (+1) |
| 138 | braeujnaeu | braeujnaeum | braeu-jnaeum | braeuJnaeum | +3 | un-donated cluster jn (+2); onset cluster br (+1) |
| 139 | braeujnaeu | braeujnaeur | braeu-jnaeur | braeuJnaeur | +3 | un-donated cluster jn (+2); onset cluster br (+1) |
| 140 | braeujnaeu | braeujnaeu | braeu-jnaeu | braeuJnaeu | +3 | un-donated cluster jn (+2); onset cluster br (+1) |

## one-syllable roots (the `roi` class): top 12 of 285 - they are EXEMPT from the soft distance>=2 rule, so they resemble each other by nature

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 141 | bra | braf | braf | Braf | +3 | area-rule final (+2); onset cluster br (+1) |
| 142 | bra | braw | braw | Braw | +1 | area-rule final (+2); onset cluster br (+1); IS an English word (-2) |
| 143 | bra | brah | brah | Brah | +3 | area-rule final (+2); onset cluster br (+1) |
| 144 | bra | bras | bras | Bras | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 145 | bra | bram | bram | Bram | -1 | onset cluster br (+1); IS an English word (-2) |
| 146 | bra | brar | brar | Brar | +1 | onset cluster br (+1) |
| 147 | bra | bra | bra | Bra | -1 | onset cluster br (+1); IS an English word (-2) |
| 148 | brae | braef | braef | Braef | +3 | area-rule final (+2); onset cluster br (+1) |
| 149 | brae | braew | braew | Braew | +3 | area-rule final (+2); onset cluster br (+1) |
| 150 | brae | braeh | braeh | Braeh | +3 | area-rule final (+2); onset cluster br (+1) |
| 151 | brae | braes | braes | Braes | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 152 | brae | braem | braem | Braem | +1 | onset cluster br (+1) |
| 153 | brae | braer | braer | Braer | +1 | onset cluster br (+1) |
| 154 | brae | brae | brae | Brae | -1 | onset cluster br (+1); IS an English word (-2) |
| 155 | braei | braeif | braeif | Braeif | +3 | area-rule final (+2); onset cluster br (+1) |
| 156 | braei | braeiw | braeiw | Braeiw | +3 | area-rule final (+2); onset cluster br (+1) |
| 157 | braei | braeih | braeih | Braeih | +3 | area-rule final (+2); onset cluster br (+1) |
| 158 | braei | braeis | braeis | Braeis | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 159 | braei | braeim | braeim | Braeim | +1 | onset cluster br (+1) |
| 160 | braei | braeir | braeir | Braeir | +1 | onset cluster br (+1) |
| 161 | braei | braei | braei | Braei | +1 | onset cluster br (+1) |
| 162 | braeu | braeuf | braeuf | Braeuf | +3 | area-rule final (+2); onset cluster br (+1) |
| 163 | braeu | braeuw | braeuw | Braeuw | +3 | area-rule final (+2); onset cluster br (+1) |
| 164 | braeu | braeuh | braeuh | Braeuh | +3 | area-rule final (+2); onset cluster br (+1) |
| 165 | braeu | braeus | braeus | Braeus | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 166 | braeu | braeum | braeum | Braeum | +1 | onset cluster br (+1) |
| 167 | braeu | braeur | braeur | Braeur | +1 | onset cluster br (+1) |
| 168 | braeu | braeu | braeu | Braeu | +1 | onset cluster br (+1) |
| 169 | brai | braif | braif | Braif | +3 | area-rule final (+2); onset cluster br (+1) |
| 170 | brai | braiw | braiw | Braiw | +3 | area-rule final (+2); onset cluster br (+1) |
| 171 | brai | braih | braih | Braih | +3 | area-rule final (+2); onset cluster br (+1) |
| 172 | brai | brais | brais | Brais | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 173 | brai | braim | braim | Braim | +1 | onset cluster br (+1) |
| 174 | brai | brair | brair | Brair | +1 | onset cluster br (+1) |
| 175 | brai | brai | brai | Brai | +1 | onset cluster br (+1) |
| 176 | brau | brauf | brauf | Brauf | +3 | area-rule final (+2); onset cluster br (+1) |
| 177 | brau | brauw | brauw | Brauw | +3 | area-rule final (+2); onset cluster br (+1) |
| 178 | brau | brauh | brauh | Brauh | +3 | area-rule final (+2); onset cluster br (+1) |
| 179 | brau | braus | braus | Braus | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 180 | brau | braum | braum | Braum | +1 | onset cluster br (+1) |
| 181 | brau | braur | braur | Braur | +1 | onset cluster br (+1) |
| 182 | brau | brau | brau | Brau | +1 | onset cluster br (+1) |
| 183 | bre | bref | bref | Bref | +3 | area-rule final (+2); onset cluster br (+1) |
| 184 | bre | brew | brew | Brew | +1 | area-rule final (+2); onset cluster br (+1); IS an English word (-2) |
| 185 | bre | breh | breh | Breh | +3 | area-rule final (+2); onset cluster br (+1) |
| 186 | bre | bres | bres | Bres | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 187 | bre | brem | brem | Brem | +1 | onset cluster br (+1) |
| 188 | bre | brer | brer | Brer | +1 | onset cluster br (+1) |
| 189 | bre | bre | bre | Bre | +1 | onset cluster br (+1) |
| 190 | brei | breif | breif | Breif | +3 | area-rule final (+2); onset cluster br (+1) |
| 191 | brei | breiw | breiw | Breiw | +3 | area-rule final (+2); onset cluster br (+1) |
| 192 | brei | breih | breih | Breih | +3 | area-rule final (+2); onset cluster br (+1) |
| 193 | brei | breis | breis | Breis | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 194 | brei | breim | breim | Breim | +1 | onset cluster br (+1) |
| 195 | brei | breir | breir | Breir | +1 | onset cluster br (+1) |
| 196 | brei | brei | brei | Brei | -1 | onset cluster br (+1); IS an English word (-2) |
| 197 | breu | breuf | breuf | Breuf | +3 | area-rule final (+2); onset cluster br (+1) |
| 198 | breu | breuw | breuw | Breuw | +3 | area-rule final (+2); onset cluster br (+1) |
| 199 | breu | breuh | breuh | Breuh | +3 | area-rule final (+2); onset cluster br (+1) |
| 200 | breu | breus | breus | Breus | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 201 | breu | breum | breum | Breum | +1 | onset cluster br (+1) |
| 202 | breu | breur | breur | Breur | +1 | onset cluster br (+1) |
| 203 | breu | breu | breu | Breu | +1 | onset cluster br (+1) |
| 204 | bri | brif | brif | Brif | +3 | area-rule final (+2); onset cluster br (+1) |
| 205 | bri | briw | briw | Briw | +3 | area-rule final (+2); onset cluster br (+1) |
| 206 | bri | brih | brih | Brih | +3 | area-rule final (+2); onset cluster br (+1) |
| 207 | bri | bris | bris | Bris | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 208 | bri | brim | brim | Brim | -1 | onset cluster br (+1); IS an English word (-2) |
| 209 | bri | brir | brir | Brir | +1 | onset cluster br (+1) |
| 210 | bri | bri | bri | Bri | +1 | onset cluster br (+1) |
| 211 | bro | brof | brof | Brof | +3 | area-rule final (+2); onset cluster br (+1) |
| 212 | bro | brow | brow | Brow | +1 | area-rule final (+2); onset cluster br (+1); IS an English word (-2) |
| 213 | bro | broh | broh | Broh | +3 | area-rule final (+2); onset cluster br (+1) |
| 214 | bro | bros | bros | Bros | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 215 | bro | brom | brom | Brom | +1 | onset cluster br (+1) |
| 216 | bro | bror | bror | Bror | +1 | onset cluster br (+1) |
| 217 | bro | bro | bro | Bro | +1 | onset cluster br (+1) |
| 218 | broi | broif | broif | Broif | +3 | area-rule final (+2); onset cluster br (+1) |
| 219 | broi | broiw | broiw | Broiw | +3 | area-rule final (+2); onset cluster br (+1) |
| 220 | broi | broih | broih | Broih | +3 | area-rule final (+2); onset cluster br (+1) |
| 221 | broi | brois | brois | Brois | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 222 | broi | broim | broim | Broim | +1 | onset cluster br (+1) |
| 223 | broi | broir | broir | Broir | +1 | onset cluster br (+1) |
| 224 | broi | broi | broi | Broi | +1 | onset cluster br (+1) |

## bases starting with `(none)`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 225 | aefmae | aefmaef | ae-fmaef | aeFmaef | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 226 | aefmae | aefmaew | ae-fmaew | aeFmaew | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 227 | aefmae | aefmaeh | ae-fmaeh | aeFmaeh | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 228 | aefmae | aefmaes | ae-fmaes | aeFmaes | +1 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2) |
| 229 | aefmae | aefmaem | ae-fmaem | aeFmaem | +2 | un-donated cluster fm (+2) |
| 230 | aefmae | aefmaer | ae-fmaer | aeFmaer | +2 | un-donated cluster fm (+2) |
| 231 | aefmae | aefmae | ae-fmae | aeFmae | +2 | un-donated cluster fm (+2) |
| 232 | a | af | af | Af | +2 | area-rule final (+2) |
| 233 | a | aw | aw | Aw | +0 | area-rule final (+2); IS an English word (-2) |
| 234 | a | ah | ah | Ah | +0 | area-rule final (+2); IS an English word (-2) |
| 235 | a | as | as | As | -3 | `s`-final: reserved branch, meant to be RARE (-1); IS an English word (-2) |
| 236 | a | am | am | Am | -2 | IS an English word (-2) |
| 237 | a | ar | ar | Ar | -2 | IS an English word (-2) |
| 238 | a | a | a | A | +0 | - |

## bases starting with `b`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 239 | baefma | baefmaf | bae-fmaf | baeFmaf | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 240 | baefma | baefmaw | bae-fmaw | baeFmaw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 241 | baefma | baefmah | bae-fmah | baeFmah | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 242 | baefma | baefmas | bae-fmas | baeFmas | +1 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2) |
| 243 | baefma | baefmam | bae-fmam | baeFmam | +2 | un-donated cluster fm (+2) |
| 244 | baefma | baefmar | bae-fmar | baeFmar | +2 | un-donated cluster fm (+2) |
| 245 | baefma | baefma | bae-fma | baeFma | +2 | un-donated cluster fm (+2) |
| 246 | ba | baf | baf | Baf | +2 | area-rule final (+2) |
| 247 | ba | baw | baw | Baw | +0 | area-rule final (+2); IS an English word (-2) |
| 248 | ba | bah | bah | Bah | +0 | area-rule final (+2); IS an English word (-2) |
| 249 | ba | bas | bas | Bas | -3 | `s`-final: reserved branch, meant to be RARE (-1); IS an English word (-2) |
| 250 | ba | bam | bam | Bam | -2 | IS an English word (-2) |
| 251 | ba | bar | bar | Bar | -2 | IS an English word (-2) |
| 252 | ba | ba | ba | Ba | -2 | IS an English word (-2) |

## bases starting with `br`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 253 | braefmae | braefmaef | brae-fmaef | braeFmaef | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 254 | braefmae | braefmaew | brae-fmaew | braeFmaew | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 255 | braefmae | braefmaeh | brae-fmaeh | braeFmaeh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 256 | braefmae | braefmaes | brae-fmaes | braeFmaes | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster br (+1) |
| 257 | braefmae | braefmaem | brae-fmaem | braeFmaem | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 258 | braefmae | braefmaer | brae-fmaer | braeFmaer | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 259 | braefmae | braefmae | brae-fmae | braeFmae | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 260 | bra | braf | braf | Braf | +3 | area-rule final (+2); onset cluster br (+1) |
| 261 | bra | braw | braw | Braw | +1 | area-rule final (+2); onset cluster br (+1); IS an English word (-2) |
| 262 | bra | brah | brah | Brah | +3 | area-rule final (+2); onset cluster br (+1) |
| 263 | bra | bras | bras | Bras | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 264 | bra | bram | bram | Bram | -1 | onset cluster br (+1); IS an English word (-2) |
| 265 | bra | brar | brar | Brar | +1 | onset cluster br (+1) |
| 266 | bra | bra | bra | Bra | -1 | onset cluster br (+1); IS an English word (-2) |

## bases starting with `c`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 267 | caeifmo | caeifmof | caei-fmof | caeiFmof | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 268 | caeifmo | caeifmow | caei-fmow | caeiFmow | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 269 | caeifmo | caeifmoh | caei-fmoh | caeiFmoh | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 270 | caeifmo | caeifmos | caei-fmos | caeiFmos | +1 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2) |
| 271 | caeifmo | caeifmom | caei-fmom | caeiFmom | +2 | un-donated cluster fm (+2) |
| 272 | caeifmo | caeifmor | caei-fmor | caeiFmor | +2 | un-donated cluster fm (+2) |
| 273 | caeifmo | caeifmo | caei-fmo | caeiFmo | +2 | un-donated cluster fm (+2) |
| 274 | ca | caf | caf | Caf | +2 | area-rule final (+2) |
| 275 | ca | caw | caw | Caw | +0 | area-rule final (+2); IS an English word (-2) |
| 276 | ca | cah | cah | Cah | +2 | area-rule final (+2) |
| 277 | ca | cas | cas | Cas | -1 | `s`-final: reserved branch, meant to be RARE (-1) |
| 278 | ca | cam | cam | Cam | -2 | IS an English word (-2) |
| 279 | ca | car | car | Car | -2 | IS an English word (-2) |
| 280 | ca | ca | ca | Ca | -2 | IS an English word (-2) |

## bases starting with `d`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 281 | daefmo | daefmof | dae-fmof | daeFmof | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 282 | daefmo | daefmow | dae-fmow | daeFmow | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 283 | daefmo | daefmoh | dae-fmoh | daeFmoh | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 284 | daefmo | daefmos | dae-fmos | daeFmos | +1 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2) |
| 285 | daefmo | daefmom | dae-fmom | daeFmom | +2 | un-donated cluster fm (+2) |
| 286 | daefmo | daefmor | dae-fmor | daeFmor | +2 | un-donated cluster fm (+2) |
| 287 | daefmo | daefmo | dae-fmo | daeFmo | +2 | un-donated cluster fm (+2) |
| 288 | da | daf | daf | Daf | +2 | area-rule final (+2) |
| 289 | da | daw | daw | Daw | +0 | area-rule final (+2); IS an English word (-2) |
| 290 | da | dah | dah | Dah | +0 | area-rule final (+2); IS an English word (-2) |
| 291 | da | das | das | Das | -3 | `s`-final: reserved branch, meant to be RARE (-1); IS an English word (-2) |
| 292 | da | dam | dam | Dam | -2 | IS an English word (-2) |
| 293 | da | dar | dar | Dar | -2 | IS an English word (-2) |
| 294 | da | da | da | Da | -2 | IS an English word (-2) |

## bases starting with `dr`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 295 | draefmae | draefmaef | drae-fmaef | draeFmaef | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster dr (+1) |
| 296 | draefmae | draefmaew | drae-fmaew | draeFmaew | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster dr (+1) |
| 297 | draefmae | draefmaeh | drae-fmaeh | draeFmaeh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster dr (+1) |
| 298 | draefmae | draefmaes | drae-fmaes | draeFmaes | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster dr (+1) |
| 299 | draefmae | draefmaem | drae-fmaem | draeFmaem | +3 | un-donated cluster fm (+2); onset cluster dr (+1) |
| 300 | draefmae | draefmaer | drae-fmaer | draeFmaer | +3 | un-donated cluster fm (+2); onset cluster dr (+1) |
| 301 | draefmae | draefmae | drae-fmae | draeFmae | +3 | un-donated cluster fm (+2); onset cluster dr (+1) |
| 302 | dra | draf | draf | Draf | +3 | area-rule final (+2); onset cluster dr (+1) |
| 303 | dra | draw | draw | Draw | +1 | area-rule final (+2); onset cluster dr (+1); IS an English word (-2) |
| 304 | dra | drah | drah | Drah | +3 | area-rule final (+2); onset cluster dr (+1) |
| 305 | dra | dras | dras | Dras | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster dr (+1) |
| 306 | dra | dram | dram | Dram | -1 | onset cluster dr (+1); IS an English word (-2) |
| 307 | dra | drar | drar | Drar | +1 | onset cluster dr (+1) |
| 308 | dra | dra | dra | Dra | +1 | onset cluster dr (+1) |

## bases starting with `f`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 309 | faefmei | faefmeif | fae-fmeif | faeFmeif | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 310 | faefmei | faefmeiw | fae-fmeiw | faeFmeiw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 311 | faefmei | faefmeih | fae-fmeih | faeFmeih | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 312 | faefmei | faefmeis | fae-fmeis | faeFmeis | +1 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2) |
| 313 | faefmei | faefmeim | fae-fmeim | faeFmeim | +2 | un-donated cluster fm (+2) |
| 314 | faefmei | faefmeir | fae-fmeir | faeFmeir | +2 | un-donated cluster fm (+2) |
| 315 | faefmei | faefmei | fae-fmei | faeFmei | +2 | un-donated cluster fm (+2) |
| 316 | fa | faf | faf | Faf | +2 | area-rule final (+2) |
| 317 | fa | faw | faw | Faw | +2 | area-rule final (+2) |
| 318 | fa | fah | fah | Fah | +2 | area-rule final (+2) |
| 319 | fa | fas | fas | Fas | -1 | `s`-final: reserved branch, meant to be RARE (-1) |
| 320 | fa | fam | fam | Fam | -2 | IS an English word (-2) |
| 321 | fa | far | far | Far | -2 | IS an English word (-2) |
| 322 | fa | fa | fa | Fa | -2 | IS an English word (-2) |

## bases starting with `g`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 323 | gaefme | gaefmef | gae-fmef | gaeFmef | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 324 | gaefme | gaefmew | gae-fmew | gaeFmew | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 325 | gaefme | gaefmeh | gae-fmeh | gaeFmeh | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 326 | gaefme | gaefmes | gae-fmes | gaeFmes | +1 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2) |
| 327 | gaefme | gaefmem | gae-fmem | gaeFmem | +2 | un-donated cluster fm (+2) |
| 328 | gaefme | gaefmer | gae-fmer | gaeFmer | +2 | un-donated cluster fm (+2) |
| 329 | gaefme | gaefme | gae-fme | gaeFme | +2 | un-donated cluster fm (+2) |
| 330 | ga | gaf | gaf | Gaf | +2 | area-rule final (+2) |
| 331 | ga | gaw | gaw | Gaw | +0 | area-rule final (+2); IS an English word (-2) |
| 332 | ga | gah | gah | Gah | +2 | area-rule final (+2) |
| 333 | ga | gas | gas | Gas | -3 | `s`-final: reserved branch, meant to be RARE (-1); IS an English word (-2) |
| 334 | ga | gam | gam | Gam | -2 | IS an English word (-2) |
| 335 | ga | gar | gar | Gar | -2 | IS an English word (-2) |
| 336 | ga | ga | ga | Ga | -2 | IS an English word (-2) |

## bases starting with `gr`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 337 | graefmae | graefmaef | grae-fmaef | graeFmaef | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster gr (+1) |
| 338 | graefmae | graefmaew | grae-fmaew | graeFmaew | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster gr (+1) |
| 339 | graefmae | graefmaeh | grae-fmaeh | graeFmaeh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster gr (+1) |
| 340 | graefmae | graefmaes | grae-fmaes | graeFmaes | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster gr (+1) |
| 341 | graefmae | graefmaem | grae-fmaem | graeFmaem | +3 | un-donated cluster fm (+2); onset cluster gr (+1) |
| 342 | graefmae | graefmaer | grae-fmaer | graeFmaer | +3 | un-donated cluster fm (+2); onset cluster gr (+1) |
| 343 | graefmae | graefmae | grae-fmae | graeFmae | +3 | un-donated cluster fm (+2); onset cluster gr (+1) |
| 344 | gra | graf | graf | Graf | +3 | area-rule final (+2); onset cluster gr (+1) |
| 345 | gra | graw | graw | Graw | +3 | area-rule final (+2); onset cluster gr (+1) |
| 346 | gra | grah | grah | Grah | +3 | area-rule final (+2); onset cluster gr (+1) |
| 347 | gra | gras | gras | Gras | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster gr (+1) |
| 348 | gra | gram | gram | Gram | -1 | onset cluster gr (+1); IS an English word (-2) |
| 349 | gra | grar | grar | Grar | +1 | onset cluster gr (+1) |
| 350 | gra | gra | gra | Gra | -1 | onset cluster gr (+1); IS an English word (-2) |

## bases starting with `h`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 351 | haefmou | haefmouf | hae-fmouf | haeFmouf | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 352 | haefmou | haefmouw | hae-fmouw | haeFmouw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 353 | haefmou | haefmouh | hae-fmouh | haeFmouh | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 354 | haefmou | haefmous | hae-fmous | haeFmous | +1 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2) |
| 355 | haefmou | haefmoum | hae-fmoum | haeFmoum | +2 | un-donated cluster fm (+2) |
| 356 | haefmou | haefmour | hae-fmour | haeFmour | +2 | un-donated cluster fm (+2) |
| 357 | haefmou | haefmou | hae-fmou | haeFmou | +2 | un-donated cluster fm (+2) |
| 358 | ha | haf | haf | Haf | +2 | area-rule final (+2) |
| 359 | ha | haw | haw | Haw | +0 | area-rule final (+2); IS an English word (-2) |
| 360 | ha | hah | hah | Hah | +0 | area-rule final (+2); IS an English word (-2) |
| 361 | ha | has | has | Has | -1 | `s`-final: reserved branch, meant to be RARE (-1) |
| 362 | ha | ham | ham | Ham | -2 | IS an English word (-2) |
| 363 | ha | har | har | Har | +0 | - |
| 364 | ha | ha | ha | Ha | -2 | IS an English word (-2) |

## bases starting with `j`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 365 | jaefmaeu | jaefmaeuf | jae-fmaeuf | jaeFmaeuf | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 366 | jaefmaeu | jaefmaeuw | jae-fmaeuw | jaeFmaeuw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 367 | jaefmaeu | jaefmaeuh | jae-fmaeuh | jaeFmaeuh | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 368 | jaefmaeu | jaefmaeus | jae-fmaeus | jaeFmaeus | +1 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2) |
| 369 | jaefmaeu | jaefmaeum | jae-fmaeum | jaeFmaeum | +2 | un-donated cluster fm (+2) |
| 370 | jaefmaeu | jaefmaeur | jae-fmaeur | jaeFmaeur | +2 | un-donated cluster fm (+2) |
| 371 | jaefmaeu | jaefmaeu | jae-fmaeu | jaeFmaeu | +2 | un-donated cluster fm (+2) |
| 372 | ja | jaf | jaf | Jaf | +2 | area-rule final (+2) |
| 373 | ja | jaw | jaw | Jaw | +0 | area-rule final (+2); IS an English word (-2) |
| 374 | ja | jah | jah | Jah | +2 | area-rule final (+2) |
| 375 | ja | jas | jas | Jas | -1 | `s`-final: reserved branch, meant to be RARE (-1) |
| 376 | ja | jam | jam | Jam | -2 | IS an English word (-2) |
| 377 | ja | jar | jar | Jar | -2 | IS an English word (-2) |
| 378 | ja | ja | ja | Ja | +0 | - |

## bases starting with `l`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 379 | laefmy | laefmyf | lae-fmyf | laeFmyf | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 380 | laefmy | laefmyw | lae-fmyw | laeFmyw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 381 | laefmy | laefmyh | lae-fmyh | laeFmyh | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 382 | laefmy | laefmys | lae-fmys | laeFmys | +1 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2) |
| 383 | laefmy | laefmym | lae-fmym | laeFmym | +2 | un-donated cluster fm (+2) |
| 384 | laefmy | laefmyr | lae-fmyr | laeFmyr | +2 | un-donated cluster fm (+2) |
| 385 | laefmy | laefmy | lae-fmy | laeFmy | +2 | un-donated cluster fm (+2) |
| 386 | la | laf | laf | Laf | +2 | area-rule final (+2) |
| 387 | la | law | law | Law | +0 | area-rule final (+2); IS an English word (-2) |
| 388 | la | lah | lah | Lah | +2 | area-rule final (+2) |
| 389 | la | las | las | Las | -3 | `s`-final: reserved branch, meant to be RARE (-1); IS an English word (-2) |
| 390 | la | lam | lam | Lam | -2 | IS an English word (-2) |
| 391 | la | lar | lar | Lar | -2 | IS an English word (-2) |
| 392 | la | la | la | La | -2 | IS an English word (-2) |

## bases starting with `m`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 393 | maefmu | maefmuf | mae-fmuf | maeFmuf | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 394 | maefmu | maefmuw | mae-fmuw | maeFmuw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 395 | maefmu | maefmuh | mae-fmuh | maeFmuh | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 396 | maefmu | maefmus | mae-fmus | maeFmus | +1 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2) |
| 397 | maefmu | maefmum | mae-fmum | maeFmum | +2 | un-donated cluster fm (+2) |
| 398 | maefmu | maefmur | mae-fmur | maeFmur | +2 | un-donated cluster fm (+2) |
| 399 | maefmu | maefmu | mae-fmu | maeFmu | +2 | un-donated cluster fm (+2) |
| 400 | ma | maf | maf | Maf | +2 | area-rule final (+2) |
| 401 | ma | maw | maw | Maw | +0 | area-rule final (+2); IS an English word (-2) |
| 402 | ma | mah | mah | Mah | +0 | area-rule final (+2); IS an English word (-2) |
| 403 | ma | mas | mas | Mas | -3 | `s`-final: reserved branch, meant to be RARE (-1); IS an English word (-2) |
| 404 | ma | mam | mam | Mam | -2 | IS an English word (-2) |
| 405 | ma | mar | mar | Mar | -2 | IS an English word (-2) |
| 406 | ma | ma | ma | Ma | -2 | IS an English word (-2) |

## bases starting with `n`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 407 | naefmi | naefmif | nae-fmif | naeFmif | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 408 | naefmi | naefmiw | nae-fmiw | naeFmiw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 409 | naefmi | naefmih | nae-fmih | naeFmih | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 410 | naefmi | naefmis | nae-fmis | naeFmis | +1 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2) |
| 411 | naefmi | naefmim | nae-fmim | naeFmim | +2 | un-donated cluster fm (+2) |
| 412 | naefmi | naefmir | nae-fmir | naeFmir | +2 | un-donated cluster fm (+2) |
| 413 | naefmi | naefmi | nae-fmi | naeFmi | +2 | un-donated cluster fm (+2) |
| 414 | na | naf | naf | Naf | +2 | area-rule final (+2) |
| 415 | na | naw | naw | Naw | +0 | area-rule final (+2); IS an English word (-2) |
| 416 | na | nah | nah | Nah | +2 | area-rule final (+2) |
| 417 | na | nas | nas | Nas | -1 | `s`-final: reserved branch, meant to be RARE (-1) |
| 418 | na | nam | nam | Nam | -2 | IS an English word (-2) |
| 419 | na | nar | nar | Nar | -2 | IS an English word (-2) |
| 420 | na | na | na | Na | -2 | IS an English word (-2) |

## bases starting with `r`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 421 | raefmai | raefmaif | rae-fmaif | raeFmaif | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 422 | raefmai | raefmaiw | rae-fmaiw | raeFmaiw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 423 | raefmai | raefmaih | rae-fmaih | raeFmaih | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 424 | raefmai | raefmais | rae-fmais | raeFmais | +1 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2) |
| 425 | raefmai | raefmaim | rae-fmaim | raeFmaim | +2 | un-donated cluster fm (+2) |
| 426 | raefmai | raefmair | rae-fmair | raeFmair | +2 | un-donated cluster fm (+2) |
| 427 | raefmai | raefmai | rae-fmai | raeFmai | +2 | un-donated cluster fm (+2) |
| 428 | ra | raf | raf | Raf | +2 | area-rule final (+2) |
| 429 | ra | raw | raw | Raw | +0 | area-rule final (+2); IS an English word (-2) |
| 430 | ra | rah | rah | Rah | +0 | area-rule final (+2); IS an English word (-2) |
| 431 | ra | ras | ras | Ras | -3 | `s`-final: reserved branch, meant to be RARE (-1); IS an English word (-2) |
| 432 | ra | ram | ram | Ram | -2 | IS an English word (-2) |
| 433 | ra | rar | rar | Rar | +0 | - |
| 434 | ra | ra | ra | Ra | -2 | IS an English word (-2) |

## bases starting with `s`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 435 | saefmoi | saefmoif | sae-fmoif | saeFmoif | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 436 | saefmoi | saefmoiw | sae-fmoiw | saeFmoiw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 437 | saefmoi | saefmoih | sae-fmoih | saeFmoih | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 438 | saefmoi | saefmois | sae-fmois | saeFmois | +1 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2) |
| 439 | saefmoi | saefmoim | sae-fmoim | saeFmoim | +2 | un-donated cluster fm (+2) |
| 440 | saefmoi | saefmoir | sae-fmoir | saeFmoir | +2 | un-donated cluster fm (+2) |
| 441 | saefmoi | saefmoi | sae-fmoi | saeFmoi | +2 | un-donated cluster fm (+2) |
| 442 | sa | saf | saf | Saf | +2 | area-rule final (+2) |
| 443 | sa | saw | saw | Saw | +0 | area-rule final (+2); IS an English word (-2) |
| 444 | sa | sah | sah | Sah | +0 | area-rule final (+2); IS an English word (-2) |
| 445 | sa | sas | sas | Sas | -1 | `s`-final: reserved branch, meant to be RARE (-1) |
| 446 | sa | sam | sam | Sam | -2 | IS an English word (-2) |
| 447 | sa | sar | sar | Sar | -2 | IS an English word (-2) |
| 448 | sa | sa | sa | Sa | -2 | IS an English word (-2) |

## bases starting with `sh`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 449 | shaefmeu | shaefmeuf | shae-fmeuf | shaeFmeuf | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 450 | shaefmeu | shaefmeuw | shae-fmeuw | shaeFmeuw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 451 | shaefmeu | shaefmeuh | shae-fmeuh | shaeFmeuh | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 452 | shaefmeu | shaefmeus | shae-fmeus | shaeFmeus | +1 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2) |
| 453 | shaefmeu | shaefmeum | shae-fmeum | shaeFmeum | +2 | un-donated cluster fm (+2) |
| 454 | shaefmeu | shaefmeur | shae-fmeur | shaeFmeur | +2 | un-donated cluster fm (+2) |
| 455 | shaefmeu | shaefmeu | shae-fmeu | shaeFmeu | +2 | un-donated cluster fm (+2) |
| 456 | sha | shaf | shaf | Shaf | +2 | area-rule final (+2) |
| 457 | sha | shaw | shaw | Shaw | +0 | area-rule final (+2); IS an English word (-2) |
| 458 | sha | shah | shah | Shah | +0 | area-rule final (+2); IS an English word (-2) |
| 459 | sha | shas | shas | Shas | -1 | `s`-final: reserved branch, meant to be RARE (-1) |
| 460 | sha | sham | sham | Sham | -2 | IS an English word (-2) |
| 461 | sha | shar | shar | Shar | +0 | - |
| 462 | sha | sha | sha | Sha | -2 | IS an English word (-2) |

## bases starting with `th`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 463 | thaefmaei | thaefmaeif | thae-fmaeif | thaeFmaeif | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 464 | thaefmaei | thaefmaeiw | thae-fmaeiw | thaeFmaeiw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 465 | thaefmaei | thaefmaeih | thae-fmaeih | thaeFmaeih | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 466 | thaefmaei | thaefmaeis | thae-fmaeis | thaeFmaeis | +1 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2) |
| 467 | thaefmaei | thaefmaeim | thae-fmaeim | thaeFmaeim | +2 | un-donated cluster fm (+2) |
| 468 | thaefmaei | thaefmaeir | thae-fmaeir | thaeFmaeir | +2 | un-donated cluster fm (+2) |
| 469 | thaefmaei | thaefmaei | thae-fmaei | thaeFmaei | +2 | un-donated cluster fm (+2) |
| 470 | tha | thaf | thaf | Thaf | +2 | area-rule final (+2) |
| 471 | tha | thaw | thaw | Thaw | +0 | area-rule final (+2); IS an English word (-2) |
| 472 | tha | thah | thah | Thah | +2 | area-rule final (+2) |
| 473 | tha | thas | thas | Thas | -1 | `s`-final: reserved branch, meant to be RARE (-1) |
| 474 | tha | tham | tham | Tham | +0 | - |
| 475 | tha | thar | thar | Thar | -2 | IS an English word (-2) |
| 476 | tha | tha | tha | Tha | -2 | IS an English word (-2) |

## bases starting with `w`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 477 | waefmau | waefmauf | wae-fmauf | waeFmauf | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 478 | waefmau | waefmauw | wae-fmauw | waeFmauw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 479 | waefmau | waefmauh | wae-fmauh | waeFmauh | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 480 | waefmau | waefmaus | wae-fmaus | waeFmaus | +1 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2) |
| 481 | waefmau | waefmaum | wae-fmaum | waeFmaum | +2 | un-donated cluster fm (+2) |
| 482 | waefmau | waefmaur | wae-fmaur | waeFmaur | +2 | un-donated cluster fm (+2) |
| 483 | waefmau | waefmau | wae-fmau | waeFmau | +2 | un-donated cluster fm (+2) |
| 484 | wae | waef | waef | Waef | +2 | area-rule final (+2) |
| 485 | wae | waew | waew | Waew | +2 | area-rule final (+2) |
| 486 | wae | waeh | waeh | Waeh | +2 | area-rule final (+2) |
| 487 | wae | waes | waes | Waes | -1 | `s`-final: reserved branch, meant to be RARE (-1) |
| 488 | wae | waem | waem | Waem | +0 | - |
| 489 | wae | waer | waer | Waer | -2 | IS an English word (-2) |
| 490 | wae | wae | wae | Wae | -2 | IS an English word (-2) |

## bases whose first vowel is `a`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 491 | brafma | brafmaf | bra-fmaf | braFmaf | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 492 | brafma | brafmaw | bra-fmaw | braFmaw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 493 | brafma | brafmah | bra-fmah | braFmah | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 494 | brafma | brafmas | bra-fmas | braFmas | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster br (+1) |
| 495 | brafma | brafmam | bra-fmam | braFmam | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 496 | brafma | brafmar | bra-fmar | braFmar | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 497 | brafma | brafma | bra-fma | braFma | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 498 | bra | braf | braf | Braf | +3 | area-rule final (+2); onset cluster br (+1) |
| 499 | bra | braw | braw | Braw | +1 | area-rule final (+2); onset cluster br (+1); IS an English word (-2) |
| 500 | bra | brah | brah | Brah | +3 | area-rule final (+2); onset cluster br (+1) |
| 501 | bra | bras | bras | Bras | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 502 | bra | bram | bram | Bram | -1 | onset cluster br (+1); IS an English word (-2) |
| 503 | bra | brar | brar | Brar | +1 | onset cluster br (+1) |
| 504 | bra | bra | bra | Bra | -1 | onset cluster br (+1); IS an English word (-2) |

## bases whose first vowel is `ae`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 505 | braefmae | braefmaef | brae-fmaef | braeFmaef | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 506 | braefmae | braefmaew | brae-fmaew | braeFmaew | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 507 | braefmae | braefmaeh | brae-fmaeh | braeFmaeh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 508 | braefmae | braefmaes | brae-fmaes | braeFmaes | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster br (+1) |
| 509 | braefmae | braefmaem | brae-fmaem | braeFmaem | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 510 | braefmae | braefmaer | brae-fmaer | braeFmaer | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 511 | braefmae | braefmae | brae-fmae | braeFmae | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 512 | brae | braef | braef | Braef | +3 | area-rule final (+2); onset cluster br (+1) |
| 513 | brae | braew | braew | Braew | +3 | area-rule final (+2); onset cluster br (+1) |
| 514 | brae | braeh | braeh | Braeh | +3 | area-rule final (+2); onset cluster br (+1) |
| 515 | brae | braes | braes | Braes | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 516 | brae | braem | braem | Braem | +1 | onset cluster br (+1) |
| 517 | brae | braer | braer | Braer | +1 | onset cluster br (+1) |
| 518 | brae | brae | brae | Brae | -1 | onset cluster br (+1); IS an English word (-2) |

## bases whose first vowel is `aei`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 519 | braeifmaei | braeifmaeif | braei-fmaeif | braeiFmaeif | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 520 | braeifmaei | braeifmaeiw | braei-fmaeiw | braeiFmaeiw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 521 | braeifmaei | braeifmaeih | braei-fmaeih | braeiFmaeih | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 522 | braeifmaei | braeifmaeis | braei-fmaeis | braeiFmaeis | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster br (+1) |
| 523 | braeifmaei | braeifmaeim | braei-fmaeim | braeiFmaeim | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 524 | braeifmaei | braeifmaeir | braei-fmaeir | braeiFmaeir | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 525 | braeifmaei | braeifmaei | braei-fmaei | braeiFmaei | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 526 | braei | braeif | braeif | Braeif | +3 | area-rule final (+2); onset cluster br (+1) |
| 527 | braei | braeiw | braeiw | Braeiw | +3 | area-rule final (+2); onset cluster br (+1) |
| 528 | braei | braeih | braeih | Braeih | +3 | area-rule final (+2); onset cluster br (+1) |
| 529 | braei | braeis | braeis | Braeis | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 530 | braei | braeim | braeim | Braeim | +1 | onset cluster br (+1) |
| 531 | braei | braeir | braeir | Braeir | +1 | onset cluster br (+1) |
| 532 | braei | braei | braei | Braei | +1 | onset cluster br (+1) |

## bases whose first vowel is `aeu`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 533 | braeufmaeu | braeufmaeuf | braeu-fmaeuf | braeuFmaeuf | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 534 | braeufmaeu | braeufmaeuw | braeu-fmaeuw | braeuFmaeuw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 535 | braeufmaeu | braeufmaeuh | braeu-fmaeuh | braeuFmaeuh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 536 | braeufmaeu | braeufmaeus | braeu-fmaeus | braeuFmaeus | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster br (+1) |
| 537 | braeufmaeu | braeufmaeum | braeu-fmaeum | braeuFmaeum | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 538 | braeufmaeu | braeufmaeur | braeu-fmaeur | braeuFmaeur | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 539 | braeufmaeu | braeufmaeu | braeu-fmaeu | braeuFmaeu | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 540 | braeu | braeuf | braeuf | Braeuf | +3 | area-rule final (+2); onset cluster br (+1) |
| 541 | braeu | braeuw | braeuw | Braeuw | +3 | area-rule final (+2); onset cluster br (+1) |
| 542 | braeu | braeuh | braeuh | Braeuh | +3 | area-rule final (+2); onset cluster br (+1) |
| 543 | braeu | braeus | braeus | Braeus | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 544 | braeu | braeum | braeum | Braeum | +1 | onset cluster br (+1) |
| 545 | braeu | braeur | braeur | Braeur | +1 | onset cluster br (+1) |
| 546 | braeu | braeu | braeu | Braeu | +1 | onset cluster br (+1) |

## bases whose first vowel is `ai`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 547 | braifmai | braifmaif | brai-fmaif | braiFmaif | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 548 | braifmai | braifmaiw | brai-fmaiw | braiFmaiw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 549 | braifmai | braifmaih | brai-fmaih | braiFmaih | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 550 | braifmai | braifmais | brai-fmais | braiFmais | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster br (+1) |
| 551 | braifmai | braifmaim | brai-fmaim | braiFmaim | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 552 | braifmai | braifmair | brai-fmair | braiFmair | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 553 | braifmai | braifmai | brai-fmai | braiFmai | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 554 | brai | braif | braif | Braif | +3 | area-rule final (+2); onset cluster br (+1) |
| 555 | brai | braiw | braiw | Braiw | +3 | area-rule final (+2); onset cluster br (+1) |
| 556 | brai | braih | braih | Braih | +3 | area-rule final (+2); onset cluster br (+1) |
| 557 | brai | brais | brais | Brais | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 558 | brai | braim | braim | Braim | +1 | onset cluster br (+1) |
| 559 | brai | brair | brair | Brair | +1 | onset cluster br (+1) |
| 560 | brai | brai | brai | Brai | +1 | onset cluster br (+1) |

## bases whose first vowel is `au`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 561 | braufmau | braufmauf | brau-fmauf | brauFmauf | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 562 | braufmau | braufmauw | brau-fmauw | brauFmauw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 563 | braufmau | braufmauh | brau-fmauh | brauFmauh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 564 | braufmau | braufmaus | brau-fmaus | brauFmaus | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster br (+1) |
| 565 | braufmau | braufmaum | brau-fmaum | brauFmaum | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 566 | braufmau | braufmaur | brau-fmaur | brauFmaur | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 567 | braufmau | braufmau | brau-fmau | brauFmau | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 568 | brau | brauf | brauf | Brauf | +3 | area-rule final (+2); onset cluster br (+1) |
| 569 | brau | brauw | brauw | Brauw | +3 | area-rule final (+2); onset cluster br (+1) |
| 570 | brau | brauh | brauh | Brauh | +3 | area-rule final (+2); onset cluster br (+1) |
| 571 | brau | braus | braus | Braus | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 572 | brau | braum | braum | Braum | +1 | onset cluster br (+1) |
| 573 | brau | braur | braur | Braur | +1 | onset cluster br (+1) |
| 574 | brau | brau | brau | Brau | +1 | onset cluster br (+1) |

## bases whose first vowel is `e`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 575 | brefme | brefmef | bre-fmef | breFmef | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 576 | brefme | brefmew | bre-fmew | breFmew | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 577 | brefme | brefmeh | bre-fmeh | breFmeh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 578 | brefme | brefmes | bre-fmes | breFmes | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster br (+1) |
| 579 | brefme | brefmem | bre-fmem | breFmem | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 580 | brefme | brefmer | bre-fmer | breFmer | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 581 | brefme | brefme | bre-fme | breFme | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 582 | bre | bref | bref | Bref | +3 | area-rule final (+2); onset cluster br (+1) |
| 583 | bre | brew | brew | Brew | +1 | area-rule final (+2); onset cluster br (+1); IS an English word (-2) |
| 584 | bre | breh | breh | Breh | +3 | area-rule final (+2); onset cluster br (+1) |
| 585 | bre | bres | bres | Bres | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 586 | bre | brem | brem | Brem | +1 | onset cluster br (+1) |
| 587 | bre | brer | brer | Brer | +1 | onset cluster br (+1) |
| 588 | bre | bre | bre | Bre | +1 | onset cluster br (+1) |

## bases whose first vowel is `ei`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 589 | breifmei | breifmeif | brei-fmeif | breiFmeif | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 590 | breifmei | breifmeiw | brei-fmeiw | breiFmeiw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 591 | breifmei | breifmeih | brei-fmeih | breiFmeih | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 592 | breifmei | breifmeis | brei-fmeis | breiFmeis | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster br (+1) |
| 593 | breifmei | breifmeim | brei-fmeim | breiFmeim | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 594 | breifmei | breifmeir | brei-fmeir | breiFmeir | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 595 | breifmei | breifmei | brei-fmei | breiFmei | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 596 | brei | breif | breif | Breif | +3 | area-rule final (+2); onset cluster br (+1) |
| 597 | brei | breiw | breiw | Breiw | +3 | area-rule final (+2); onset cluster br (+1) |
| 598 | brei | breih | breih | Breih | +3 | area-rule final (+2); onset cluster br (+1) |
| 599 | brei | breis | breis | Breis | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 600 | brei | breim | breim | Breim | +1 | onset cluster br (+1) |
| 601 | brei | breir | breir | Breir | +1 | onset cluster br (+1) |
| 602 | brei | brei | brei | Brei | -1 | onset cluster br (+1); IS an English word (-2) |

## bases whose first vowel is `eu`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 603 | breufmeu | breufmeuf | breu-fmeuf | breuFmeuf | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 604 | breufmeu | breufmeuw | breu-fmeuw | breuFmeuw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 605 | breufmeu | breufmeuh | breu-fmeuh | breuFmeuh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 606 | breufmeu | breufmeus | breu-fmeus | breuFmeus | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster br (+1) |
| 607 | breufmeu | breufmeum | breu-fmeum | breuFmeum | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 608 | breufmeu | breufmeur | breu-fmeur | breuFmeur | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 609 | breufmeu | breufmeu | breu-fmeu | breuFmeu | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 610 | breu | breuf | breuf | Breuf | +3 | area-rule final (+2); onset cluster br (+1) |
| 611 | breu | breuw | breuw | Breuw | +3 | area-rule final (+2); onset cluster br (+1) |
| 612 | breu | breuh | breuh | Breuh | +3 | area-rule final (+2); onset cluster br (+1) |
| 613 | breu | breus | breus | Breus | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 614 | breu | breum | breum | Breum | +1 | onset cluster br (+1) |
| 615 | breu | breur | breur | Breur | +1 | onset cluster br (+1) |
| 616 | breu | breu | breu | Breu | +1 | onset cluster br (+1) |

## bases whose first vowel is `i`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 617 | brifmi | brifmif | bri-fmif | briFmif | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 618 | brifmi | brifmiw | bri-fmiw | briFmiw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 619 | brifmi | brifmih | bri-fmih | briFmih | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 620 | brifmi | brifmis | bri-fmis | briFmis | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster br (+1) |
| 621 | brifmi | brifmim | bri-fmim | briFmim | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 622 | brifmi | brifmir | bri-fmir | briFmir | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 623 | brifmi | brifmi | bri-fmi | briFmi | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 624 | bri | brif | brif | Brif | +3 | area-rule final (+2); onset cluster br (+1) |
| 625 | bri | briw | briw | Briw | +3 | area-rule final (+2); onset cluster br (+1) |
| 626 | bri | brih | brih | Brih | +3 | area-rule final (+2); onset cluster br (+1) |
| 627 | bri | bris | bris | Bris | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 628 | bri | brim | brim | Brim | -1 | onset cluster br (+1); IS an English word (-2) |
| 629 | bri | brir | brir | Brir | +1 | onset cluster br (+1) |
| 630 | bri | bri | bri | Bri | +1 | onset cluster br (+1) |

## bases whose first vowel is `o`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 631 | brofmo | brofmof | bro-fmof | broFmof | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 632 | brofmo | brofmow | bro-fmow | broFmow | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 633 | brofmo | brofmoh | bro-fmoh | broFmoh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 634 | brofmo | brofmos | bro-fmos | broFmos | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster br (+1) |
| 635 | brofmo | brofmom | bro-fmom | broFmom | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 636 | brofmo | brofmor | bro-fmor | broFmor | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 637 | brofmo | brofmo | bro-fmo | broFmo | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 638 | bro | brof | brof | Brof | +3 | area-rule final (+2); onset cluster br (+1) |
| 639 | bro | brow | brow | Brow | +1 | area-rule final (+2); onset cluster br (+1); IS an English word (-2) |
| 640 | bro | broh | broh | Broh | +3 | area-rule final (+2); onset cluster br (+1) |
| 641 | bro | bros | bros | Bros | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 642 | bro | brom | brom | Brom | +1 | onset cluster br (+1) |
| 643 | bro | bror | bror | Bror | +1 | onset cluster br (+1) |
| 644 | bro | bro | bro | Bro | +1 | onset cluster br (+1) |

## bases whose first vowel is `oi`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 645 | broifmoi | broifmoif | broi-fmoif | broiFmoif | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 646 | broifmoi | broifmoiw | broi-fmoiw | broiFmoiw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 647 | broifmoi | broifmoih | broi-fmoih | broiFmoih | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 648 | broifmoi | broifmois | broi-fmois | broiFmois | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster br (+1) |
| 649 | broifmoi | broifmoim | broi-fmoim | broiFmoim | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 650 | broifmoi | broifmoir | broi-fmoir | broiFmoir | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 651 | broifmoi | broifmoi | broi-fmoi | broiFmoi | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 652 | broi | broif | broif | Broif | +3 | area-rule final (+2); onset cluster br (+1) |
| 653 | broi | broiw | broiw | Broiw | +3 | area-rule final (+2); onset cluster br (+1) |
| 654 | broi | broih | broih | Broih | +3 | area-rule final (+2); onset cluster br (+1) |
| 655 | broi | brois | brois | Brois | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 656 | broi | broim | broim | Broim | +1 | onset cluster br (+1) |
| 657 | broi | broir | broir | Broir | +1 | onset cluster br (+1) |
| 658 | broi | broi | broi | Broi | +1 | onset cluster br (+1) |

## bases whose first vowel is `ou`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 659 | broufmou | broufmouf | brou-fmouf | brouFmouf | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 660 | broufmou | broufmouw | brou-fmouw | brouFmouw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 661 | broufmou | broufmouh | brou-fmouh | brouFmouh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 662 | broufmou | broufmous | brou-fmous | brouFmous | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster br (+1) |
| 663 | broufmou | broufmoum | brou-fmoum | brouFmoum | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 664 | broufmou | broufmour | brou-fmour | brouFmour | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 665 | broufmou | broufmou | brou-fmou | brouFmou | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 666 | brou | brouf | brouf | Brouf | +3 | area-rule final (+2); onset cluster br (+1) |
| 667 | brou | brouw | brouw | Brouw | +3 | area-rule final (+2); onset cluster br (+1) |
| 668 | brou | brouh | brouh | Brouh | +3 | area-rule final (+2); onset cluster br (+1) |
| 669 | brou | brous | brous | Brous | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 670 | brou | broum | broum | Broum | +1 | onset cluster br (+1) |
| 671 | brou | brour | brour | Brour | +1 | onset cluster br (+1) |
| 672 | brou | brou | brou | Brou | +1 | onset cluster br (+1) |

## bases whose first vowel is `u`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 673 | brufmu | brufmuf | bru-fmuf | bruFmuf | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 674 | brufmu | brufmuw | bru-fmuw | bruFmuw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 675 | brufmu | brufmuh | bru-fmuh | bruFmuh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 676 | brufmu | brufmus | bru-fmus | bruFmus | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster br (+1) |
| 677 | brufmu | brufmum | bru-fmum | bruFmum | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 678 | brufmu | brufmur | bru-fmur | bruFmur | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 679 | brufmu | brufmu | bru-fmu | bruFmu | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 680 | bru | bruf | bruf | Bruf | +3 | area-rule final (+2); onset cluster br (+1) |
| 681 | bru | bruw | bruw | Bruw | +3 | area-rule final (+2); onset cluster br (+1) |
| 682 | bru | bruh | bruh | Bruh | +3 | area-rule final (+2); onset cluster br (+1) |
| 683 | bru | brus | brus | Brus | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 684 | bru | brum | brum | Brum | +1 | onset cluster br (+1) |
| 685 | bru | brur | brur | Brur | +1 | onset cluster br (+1) |
| 686 | bru | bru | bru | Bru | +1 | onset cluster br (+1) |

## bases whose first vowel is `y`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 687 | bryfmy | bryfmyf | bry-fmyf | bryFmyf | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 688 | bryfmy | bryfmyw | bry-fmyw | bryFmyw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 689 | bryfmy | bryfmyh | bry-fmyh | bryFmyh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 690 | bryfmy | bryfmys | bry-fmys | bryFmys | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster br (+1) |
| 691 | bryfmy | bryfmym | bry-fmym | bryFmym | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 692 | bryfmy | bryfmyr | bry-fmyr | bryFmyr | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 693 | bryfmy | bryfmy | bry-fmy | bryFmy | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 694 | bry | bryf | bryf | Bryf | +3 | area-rule final (+2); onset cluster br (+1) |
| 695 | bry | bryw | bryw | Bryw | +3 | area-rule final (+2); onset cluster br (+1) |
| 696 | bry | bryh | bryh | Bryh | +3 | area-rule final (+2); onset cluster br (+1) |
| 697 | bry | brys | brys | Brys | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 698 | bry | brym | brym | Brym | +1 | onset cluster br (+1) |
| 699 | bry | bryr | bryr | Bryr | +1 | onset cluster br (+1) |
| 700 | bry | bry | bry | Bry | +1 | onset cluster br (+1) |

## English collisions (measured - avoid or accept knowingly)

642 forms are literally in `/usr/share/dict/words`, so a pick can never hit one by accident:

```
aw ah as am ar abas aba abram ager age agrah agra algor aly ammi amos amor anis ani antar anta ardor argas arrau arum aru aes aer ae aim air ai airer aire auh aus aum author baw bah bas bam bar ba bago balai banker baris bari barny bae bais bes ber be bedew belga bemar bema bis bim bifer bilgy bilo birdy birgus bow bos bom bor bo bodo boga bolis bony bois bouw bouncer bounce bus bum bur bu bufo bullous buna busser by byre braw bram bra brahma branny branta brassy brae brew brei brim bribri brow brolga broma caw cam car ca caltha carry carse caum ce cerris cow cos cor coca collum conger cormous corneum cothy coif coir cougar counter courge cum cur cumshaw daw dah das dam dar da dado dali damper darger daer dae dais daira dauw daur dew de debar demos denis denim desma dis dim di dimmer diner dine dinkum dirdum dow dos dom dor do domer dome donum doris dori doum dour dum dure draw dram draba drew drow drum dry eh es em er edo elbow elder eli enter either eu fam far fa fanwe farsi fasher
```

(... and 442 more; raise --max-en)


---

## What the menu does NOT do

- It cannot tell you what sounds *beautiful* - that is the part only you can supply.
- It contains **no 1-syllable (`roi`-class) root**: the pool is the 2-syllable core
  (`../../docs/decisions/03-open-questions.md` section 0 item 22). Wanting short roots in this round means
  extending that pool FIRST - which changes the numbering here.
- It does not test the **M3a seam** (root-final `f`/`w`/`h` + a case suffix, always unstressed) -
  still unjudged (section 0 item 20), and it fires for 3 of every 4 coined roots.
