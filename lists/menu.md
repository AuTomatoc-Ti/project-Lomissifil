# lists/menu.md - GENERATED coining menu. DO NOT ANNOTATE HERE.

Regenerate with:

```
python3 tools/menu.py > lists/menu.md
```

**Picks go in `lists/picks.md`** - record the FORM TEXT, not just a number. Any note written in this
file is lost on regeneration.

## The ranking is deliberate (author's ruling 2026-10-14)

`tools/fingerprint.py` measured which parts of our sound profile are **un-donated** (see
`../decision/06-neutrality.md` -> "Measurement"). This menu pushes those to the top:

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
syllable). **A group of five rows is ONE base**, in the fixed order `+f | +w (/v/) | +h | +s | bare`,
and a base yields exactly **2** roots - so pick **at most one** from the `{+f, +w}` pair and **at most
one** from the `{+h, +s, bare}` trio. (`+s` is new in **R4**: the `s` branch is RESERVED for a future
adjective / adverb / exceptional-case job, so a `+s` pick is an ordinary root whose meaning slot is
held.)

> Sound-only: R3 is PARKED, so assign **no meanings** (`../decision/03-open-questions.md` section 0
> item 14). A pick is not a word; `../reference/example.md` stays the only source for examples.

---
## Top 20 bases - the most "ours" material

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 1 | braefmae | braefmaef | brae-fmaef | braeFmaef | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 2 | braefmae | braefmaew | brae-fmaew | braeFmaew | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 3 | braefmae | braefmaeh | brae-fmaeh | braeFmaeh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 4 | braefmae | braefmaes | brae-fmaes | braeFmaes | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster br (+1) |
| 5 | braefmae | braefmae | brae-fmae | braeFmae | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 6 | braefnae | braefnaef | brae-fnaef | braeFnaef | +5 | area-rule final (+2); un-donated cluster fn (+2); onset cluster br (+1) |
| 7 | braefnae | braefnaew | brae-fnaew | braeFnaew | +5 | area-rule final (+2); un-donated cluster fn (+2); onset cluster br (+1) |
| 8 | braefnae | braefnaeh | brae-fnaeh | braeFnaeh | +5 | area-rule final (+2); un-donated cluster fn (+2); onset cluster br (+1) |
| 9 | braefnae | braefnaes | brae-fnaes | braeFnaes | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fn (+2); onset cluster br (+1) |
| 10 | braefnae | braefnae | brae-fnae | braeFnae | +3 | un-donated cluster fn (+2); onset cluster br (+1) |
| 11 | braehmae | braehmaef | brae-hmaef | braeHmaef | +5 | area-rule final (+2); un-donated cluster hm (+2); onset cluster br (+1) |
| 12 | braehmae | braehmaew | brae-hmaew | braeHmaew | +5 | area-rule final (+2); un-donated cluster hm (+2); onset cluster br (+1) |
| 13 | braehmae | braehmaeh | brae-hmaeh | braeHmaeh | +5 | area-rule final (+2); un-donated cluster hm (+2); onset cluster br (+1) |
| 14 | braehmae | braehmaes | brae-hmaes | braeHmaes | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster hm (+2); onset cluster br (+1) |
| 15 | braehmae | braehmae | brae-hmae | braeHmae | +3 | un-donated cluster hm (+2); onset cluster br (+1) |
| 16 | braehnae | braehnaef | brae-hnaef | braeHnaef | +5 | area-rule final (+2); un-donated cluster hn (+2); onset cluster br (+1) |
| 17 | braehnae | braehnaew | brae-hnaew | braeHnaew | +5 | area-rule final (+2); un-donated cluster hn (+2); onset cluster br (+1) |
| 18 | braehnae | braehnaeh | brae-hnaeh | braeHnaeh | +5 | area-rule final (+2); un-donated cluster hn (+2); onset cluster br (+1) |
| 19 | braehnae | braehnaes | brae-hnaes | braeHnaes | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster hn (+2); onset cluster br (+1) |
| 20 | braehnae | braehnae | brae-hnae | braeHnae | +3 | un-donated cluster hn (+2); onset cluster br (+1) |
| 21 | braeifmaei | braeifmaeif | braei-fmaeif | braeiFmaeif | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 22 | braeifmaei | braeifmaeiw | braei-fmaeiw | braeiFmaeiw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 23 | braeifmaei | braeifmaeih | braei-fmaeih | braeiFmaeih | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 24 | braeifmaei | braeifmaeis | braei-fmaeis | braeiFmaeis | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster br (+1) |
| 25 | braeifmaei | braeifmaei | braei-fmaei | braeiFmaei | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 26 | braeifnaei | braeifnaeif | braei-fnaeif | braeiFnaeif | +5 | area-rule final (+2); un-donated cluster fn (+2); onset cluster br (+1) |
| 27 | braeifnaei | braeifnaeiw | braei-fnaeiw | braeiFnaeiw | +5 | area-rule final (+2); un-donated cluster fn (+2); onset cluster br (+1) |
| 28 | braeifnaei | braeifnaeih | braei-fnaeih | braeiFnaeih | +5 | area-rule final (+2); un-donated cluster fn (+2); onset cluster br (+1) |
| 29 | braeifnaei | braeifnaeis | braei-fnaeis | braeiFnaeis | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fn (+2); onset cluster br (+1) |
| 30 | braeifnaei | braeifnaei | braei-fnaei | braeiFnaei | +3 | un-donated cluster fn (+2); onset cluster br (+1) |
| 31 | braeihmaei | braeihmaeif | braei-hmaeif | braeiHmaeif | +5 | area-rule final (+2); un-donated cluster hm (+2); onset cluster br (+1) |
| 32 | braeihmaei | braeihmaeiw | braei-hmaeiw | braeiHmaeiw | +5 | area-rule final (+2); un-donated cluster hm (+2); onset cluster br (+1) |
| 33 | braeihmaei | braeihmaeih | braei-hmaeih | braeiHmaeih | +5 | area-rule final (+2); un-donated cluster hm (+2); onset cluster br (+1) |
| 34 | braeihmaei | braeihmaeis | braei-hmaeis | braeiHmaeis | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster hm (+2); onset cluster br (+1) |
| 35 | braeihmaei | braeihmaei | braei-hmaei | braeiHmaei | +3 | un-donated cluster hm (+2); onset cluster br (+1) |
| 36 | braeihnaei | braeihnaeif | braei-hnaeif | braeiHnaeif | +5 | area-rule final (+2); un-donated cluster hn (+2); onset cluster br (+1) |
| 37 | braeihnaei | braeihnaeiw | braei-hnaeiw | braeiHnaeiw | +5 | area-rule final (+2); un-donated cluster hn (+2); onset cluster br (+1) |
| 38 | braeihnaei | braeihnaeih | braei-hnaeih | braeiHnaeih | +5 | area-rule final (+2); un-donated cluster hn (+2); onset cluster br (+1) |
| 39 | braeihnaei | braeihnaeis | braei-hnaeis | braeiHnaeis | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster hn (+2); onset cluster br (+1) |
| 40 | braeihnaei | braeihnaei | braei-hnaei | braeiHnaei | +3 | un-donated cluster hn (+2); onset cluster br (+1) |
| 41 | braeijmaei | braeijmaeif | braei-jmaeif | braeiJmaeif | +5 | area-rule final (+2); un-donated cluster jm (+2); onset cluster br (+1) |
| 42 | braeijmaei | braeijmaeiw | braei-jmaeiw | braeiJmaeiw | +5 | area-rule final (+2); un-donated cluster jm (+2); onset cluster br (+1) |
| 43 | braeijmaei | braeijmaeih | braei-jmaeih | braeiJmaeih | +5 | area-rule final (+2); un-donated cluster jm (+2); onset cluster br (+1) |
| 44 | braeijmaei | braeijmaeis | braei-jmaeis | braeiJmaeis | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster jm (+2); onset cluster br (+1) |
| 45 | braeijmaei | braeijmaei | braei-jmaei | braeiJmaei | +3 | un-donated cluster jm (+2); onset cluster br (+1) |
| 46 | braeijnaei | braeijnaeif | braei-jnaeif | braeiJnaeif | +5 | area-rule final (+2); un-donated cluster jn (+2); onset cluster br (+1) |
| 47 | braeijnaei | braeijnaeiw | braei-jnaeiw | braeiJnaeiw | +5 | area-rule final (+2); un-donated cluster jn (+2); onset cluster br (+1) |
| 48 | braeijnaei | braeijnaeih | braei-jnaeih | braeiJnaeih | +5 | area-rule final (+2); un-donated cluster jn (+2); onset cluster br (+1) |
| 49 | braeijnaei | braeijnaeis | braei-jnaeis | braeiJnaeis | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster jn (+2); onset cluster br (+1) |
| 50 | braeijnaei | braeijnaei | braei-jnaei | braeiJnaei | +3 | un-donated cluster jn (+2); onset cluster br (+1) |
| 51 | braeiwmaei | braeiwmaeif | braei-wmaeif | braeiWmaeif | +5 | area-rule final (+2); un-donated cluster wm (+2); onset cluster br (+1) |
| 52 | braeiwmaei | braeiwmaeiw | braei-wmaeiw | braeiWmaeiw | +5 | area-rule final (+2); un-donated cluster wm (+2); onset cluster br (+1) |
| 53 | braeiwmaei | braeiwmaeih | braei-wmaeih | braeiWmaeih | +5 | area-rule final (+2); un-donated cluster wm (+2); onset cluster br (+1) |
| 54 | braeiwmaei | braeiwmaeis | braei-wmaeis | braeiWmaeis | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster wm (+2); onset cluster br (+1) |
| 55 | braeiwmaei | braeiwmaei | braei-wmaei | braeiWmaei | +3 | un-donated cluster wm (+2); onset cluster br (+1) |
| 56 | braeiwnaei | braeiwnaeif | braei-wnaeif | braeiWnaeif | +5 | area-rule final (+2); un-donated cluster wn (+2); onset cluster br (+1) |
| 57 | braeiwnaei | braeiwnaeiw | braei-wnaeiw | braeiWnaeiw | +5 | area-rule final (+2); un-donated cluster wn (+2); onset cluster br (+1) |
| 58 | braeiwnaei | braeiwnaeih | braei-wnaeih | braeiWnaeih | +5 | area-rule final (+2); un-donated cluster wn (+2); onset cluster br (+1) |
| 59 | braeiwnaei | braeiwnaeis | braei-wnaeis | braeiWnaeis | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster wn (+2); onset cluster br (+1) |
| 60 | braeiwnaei | braeiwnaei | braei-wnaei | braeiWnaei | +3 | un-donated cluster wn (+2); onset cluster br (+1) |
| 61 | braejmae | braejmaef | brae-jmaef | braeJmaef | +5 | area-rule final (+2); un-donated cluster jm (+2); onset cluster br (+1) |
| 62 | braejmae | braejmaew | brae-jmaew | braeJmaew | +5 | area-rule final (+2); un-donated cluster jm (+2); onset cluster br (+1) |
| 63 | braejmae | braejmaeh | brae-jmaeh | braeJmaeh | +5 | area-rule final (+2); un-donated cluster jm (+2); onset cluster br (+1) |
| 64 | braejmae | braejmaes | brae-jmaes | braeJmaes | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster jm (+2); onset cluster br (+1) |
| 65 | braejmae | braejmae | brae-jmae | braeJmae | +3 | un-donated cluster jm (+2); onset cluster br (+1) |
| 66 | braejnae | braejnaef | brae-jnaef | braeJnaef | +5 | area-rule final (+2); un-donated cluster jn (+2); onset cluster br (+1) |
| 67 | braejnae | braejnaew | brae-jnaew | braeJnaew | +5 | area-rule final (+2); un-donated cluster jn (+2); onset cluster br (+1) |
| 68 | braejnae | braejnaeh | brae-jnaeh | braeJnaeh | +5 | area-rule final (+2); un-donated cluster jn (+2); onset cluster br (+1) |
| 69 | braejnae | braejnaes | brae-jnaes | braeJnaes | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster jn (+2); onset cluster br (+1) |
| 70 | braejnae | braejnae | brae-jnae | braeJnae | +3 | un-donated cluster jn (+2); onset cluster br (+1) |
| 71 | braeufmaeu | braeufmaeuf | braeu-fmaeuf | braeuFmaeuf | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 72 | braeufmaeu | braeufmaeuw | braeu-fmaeuw | braeuFmaeuw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 73 | braeufmaeu | braeufmaeuh | braeu-fmaeuh | braeuFmaeuh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 74 | braeufmaeu | braeufmaeus | braeu-fmaeus | braeuFmaeus | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster br (+1) |
| 75 | braeufmaeu | braeufmaeu | braeu-fmaeu | braeuFmaeu | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 76 | braeufnaeu | braeufnaeuf | braeu-fnaeuf | braeuFnaeuf | +5 | area-rule final (+2); un-donated cluster fn (+2); onset cluster br (+1) |
| 77 | braeufnaeu | braeufnaeuw | braeu-fnaeuw | braeuFnaeuw | +5 | area-rule final (+2); un-donated cluster fn (+2); onset cluster br (+1) |
| 78 | braeufnaeu | braeufnaeuh | braeu-fnaeuh | braeuFnaeuh | +5 | area-rule final (+2); un-donated cluster fn (+2); onset cluster br (+1) |
| 79 | braeufnaeu | braeufnaeus | braeu-fnaeus | braeuFnaeus | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fn (+2); onset cluster br (+1) |
| 80 | braeufnaeu | braeufnaeu | braeu-fnaeu | braeuFnaeu | +3 | un-donated cluster fn (+2); onset cluster br (+1) |
| 81 | braeuhmaeu | braeuhmaeuf | braeu-hmaeuf | braeuHmaeuf | +5 | area-rule final (+2); un-donated cluster hm (+2); onset cluster br (+1) |
| 82 | braeuhmaeu | braeuhmaeuw | braeu-hmaeuw | braeuHmaeuw | +5 | area-rule final (+2); un-donated cluster hm (+2); onset cluster br (+1) |
| 83 | braeuhmaeu | braeuhmaeuh | braeu-hmaeuh | braeuHmaeuh | +5 | area-rule final (+2); un-donated cluster hm (+2); onset cluster br (+1) |
| 84 | braeuhmaeu | braeuhmaeus | braeu-hmaeus | braeuHmaeus | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster hm (+2); onset cluster br (+1) |
| 85 | braeuhmaeu | braeuhmaeu | braeu-hmaeu | braeuHmaeu | +3 | un-donated cluster hm (+2); onset cluster br (+1) |
| 86 | braeuhnaeu | braeuhnaeuf | braeu-hnaeuf | braeuHnaeuf | +5 | area-rule final (+2); un-donated cluster hn (+2); onset cluster br (+1) |
| 87 | braeuhnaeu | braeuhnaeuw | braeu-hnaeuw | braeuHnaeuw | +5 | area-rule final (+2); un-donated cluster hn (+2); onset cluster br (+1) |
| 88 | braeuhnaeu | braeuhnaeuh | braeu-hnaeuh | braeuHnaeuh | +5 | area-rule final (+2); un-donated cluster hn (+2); onset cluster br (+1) |
| 89 | braeuhnaeu | braeuhnaeus | braeu-hnaeus | braeuHnaeus | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster hn (+2); onset cluster br (+1) |
| 90 | braeuhnaeu | braeuhnaeu | braeu-hnaeu | braeuHnaeu | +3 | un-donated cluster hn (+2); onset cluster br (+1) |
| 91 | braeujmaeu | braeujmaeuf | braeu-jmaeuf | braeuJmaeuf | +5 | area-rule final (+2); un-donated cluster jm (+2); onset cluster br (+1) |
| 92 | braeujmaeu | braeujmaeuw | braeu-jmaeuw | braeuJmaeuw | +5 | area-rule final (+2); un-donated cluster jm (+2); onset cluster br (+1) |
| 93 | braeujmaeu | braeujmaeuh | braeu-jmaeuh | braeuJmaeuh | +5 | area-rule final (+2); un-donated cluster jm (+2); onset cluster br (+1) |
| 94 | braeujmaeu | braeujmaeus | braeu-jmaeus | braeuJmaeus | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster jm (+2); onset cluster br (+1) |
| 95 | braeujmaeu | braeujmaeu | braeu-jmaeu | braeuJmaeu | +3 | un-donated cluster jm (+2); onset cluster br (+1) |
| 96 | braeujnaeu | braeujnaeuf | braeu-jnaeuf | braeuJnaeuf | +5 | area-rule final (+2); un-donated cluster jn (+2); onset cluster br (+1) |
| 97 | braeujnaeu | braeujnaeuw | braeu-jnaeuw | braeuJnaeuw | +5 | area-rule final (+2); un-donated cluster jn (+2); onset cluster br (+1) |
| 98 | braeujnaeu | braeujnaeuh | braeu-jnaeuh | braeuJnaeuh | +5 | area-rule final (+2); un-donated cluster jn (+2); onset cluster br (+1) |
| 99 | braeujnaeu | braeujnaeus | braeu-jnaeus | braeuJnaeus | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster jn (+2); onset cluster br (+1) |
| 100 | braeujnaeu | braeujnaeu | braeu-jnaeu | braeuJnaeu | +3 | un-donated cluster jn (+2); onset cluster br (+1) |

## one-syllable roots (the `roi` class): top 12 of 285 - they are EXEMPT from the soft distance>=2 rule, so they resemble each other by nature

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 101 | bra | braf | braf | Braf | +3 | area-rule final (+2); onset cluster br (+1) |
| 102 | bra | braw | braw | Braw | +1 | area-rule final (+2); onset cluster br (+1); IS an English word (-2) |
| 103 | bra | brah | brah | Brah | +3 | area-rule final (+2); onset cluster br (+1) |
| 104 | bra | bras | bras | Bras | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 105 | bra | bra | bra | Bra | -1 | onset cluster br (+1); IS an English word (-2) |
| 106 | brae | braef | braef | Braef | +3 | area-rule final (+2); onset cluster br (+1) |
| 107 | brae | braew | braew | Braew | +3 | area-rule final (+2); onset cluster br (+1) |
| 108 | brae | braeh | braeh | Braeh | +3 | area-rule final (+2); onset cluster br (+1) |
| 109 | brae | braes | braes | Braes | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 110 | brae | brae | brae | Brae | -1 | onset cluster br (+1); IS an English word (-2) |
| 111 | braei | braeif | braeif | Braeif | +3 | area-rule final (+2); onset cluster br (+1) |
| 112 | braei | braeiw | braeiw | Braeiw | +3 | area-rule final (+2); onset cluster br (+1) |
| 113 | braei | braeih | braeih | Braeih | +3 | area-rule final (+2); onset cluster br (+1) |
| 114 | braei | braeis | braeis | Braeis | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 115 | braei | braei | braei | Braei | +1 | onset cluster br (+1) |
| 116 | braeu | braeuf | braeuf | Braeuf | +3 | area-rule final (+2); onset cluster br (+1) |
| 117 | braeu | braeuw | braeuw | Braeuw | +3 | area-rule final (+2); onset cluster br (+1) |
| 118 | braeu | braeuh | braeuh | Braeuh | +3 | area-rule final (+2); onset cluster br (+1) |
| 119 | braeu | braeus | braeus | Braeus | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 120 | braeu | braeu | braeu | Braeu | +1 | onset cluster br (+1) |
| 121 | brai | braif | braif | Braif | +3 | area-rule final (+2); onset cluster br (+1) |
| 122 | brai | braiw | braiw | Braiw | +3 | area-rule final (+2); onset cluster br (+1) |
| 123 | brai | braih | braih | Braih | +3 | area-rule final (+2); onset cluster br (+1) |
| 124 | brai | brais | brais | Brais | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 125 | brai | brai | brai | Brai | +1 | onset cluster br (+1) |
| 126 | brau | brauf | brauf | Brauf | +3 | area-rule final (+2); onset cluster br (+1) |
| 127 | brau | brauw | brauw | Brauw | +3 | area-rule final (+2); onset cluster br (+1) |
| 128 | brau | brauh | brauh | Brauh | +3 | area-rule final (+2); onset cluster br (+1) |
| 129 | brau | braus | braus | Braus | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 130 | brau | brau | brau | Brau | +1 | onset cluster br (+1) |
| 131 | bre | bref | bref | Bref | +3 | area-rule final (+2); onset cluster br (+1) |
| 132 | bre | brew | brew | Brew | +1 | area-rule final (+2); onset cluster br (+1); IS an English word (-2) |
| 133 | bre | breh | breh | Breh | +3 | area-rule final (+2); onset cluster br (+1) |
| 134 | bre | bres | bres | Bres | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 135 | bre | bre | bre | Bre | +1 | onset cluster br (+1) |
| 136 | brei | breif | breif | Breif | +3 | area-rule final (+2); onset cluster br (+1) |
| 137 | brei | breiw | breiw | Breiw | +3 | area-rule final (+2); onset cluster br (+1) |
| 138 | brei | breih | breih | Breih | +3 | area-rule final (+2); onset cluster br (+1) |
| 139 | brei | breis | breis | Breis | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 140 | brei | brei | brei | Brei | -1 | onset cluster br (+1); IS an English word (-2) |
| 141 | breu | breuf | breuf | Breuf | +3 | area-rule final (+2); onset cluster br (+1) |
| 142 | breu | breuw | breuw | Breuw | +3 | area-rule final (+2); onset cluster br (+1) |
| 143 | breu | breuh | breuh | Breuh | +3 | area-rule final (+2); onset cluster br (+1) |
| 144 | breu | breus | breus | Breus | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 145 | breu | breu | breu | Breu | +1 | onset cluster br (+1) |
| 146 | bri | brif | brif | Brif | +3 | area-rule final (+2); onset cluster br (+1) |
| 147 | bri | briw | briw | Briw | +3 | area-rule final (+2); onset cluster br (+1) |
| 148 | bri | brih | brih | Brih | +3 | area-rule final (+2); onset cluster br (+1) |
| 149 | bri | bris | bris | Bris | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 150 | bri | bri | bri | Bri | +1 | onset cluster br (+1) |
| 151 | bro | brof | brof | Brof | +3 | area-rule final (+2); onset cluster br (+1) |
| 152 | bro | brow | brow | Brow | +1 | area-rule final (+2); onset cluster br (+1); IS an English word (-2) |
| 153 | bro | broh | broh | Broh | +3 | area-rule final (+2); onset cluster br (+1) |
| 154 | bro | bros | bros | Bros | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 155 | bro | bro | bro | Bro | +1 | onset cluster br (+1) |
| 156 | broi | broif | broif | Broif | +3 | area-rule final (+2); onset cluster br (+1) |
| 157 | broi | broiw | broiw | Broiw | +3 | area-rule final (+2); onset cluster br (+1) |
| 158 | broi | broih | broih | Broih | +3 | area-rule final (+2); onset cluster br (+1) |
| 159 | broi | brois | brois | Brois | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 160 | broi | broi | broi | Broi | +1 | onset cluster br (+1) |

## bases starting with `(none)`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 161 | aefmae | aefmaef | ae-fmaef | aeFmaef | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 162 | aefmae | aefmaew | ae-fmaew | aeFmaew | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 163 | aefmae | aefmaeh | ae-fmaeh | aeFmaeh | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 164 | aefmae | aefmaes | ae-fmaes | aeFmaes | +1 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2) |
| 165 | aefmae | aefmae | ae-fmae | aeFmae | +2 | un-donated cluster fm (+2) |
| 166 | a | af | af | Af | +2 | area-rule final (+2) |
| 167 | a | aw | aw | Aw | +0 | area-rule final (+2); IS an English word (-2) |
| 168 | a | ah | ah | Ah | +0 | area-rule final (+2); IS an English word (-2) |
| 169 | a | as | as | As | -3 | `s`-final: reserved branch, meant to be RARE (-1); IS an English word (-2) |
| 170 | a | a | a | A | +0 | - |

## bases starting with `b`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 171 | baefma | baefmaf | bae-fmaf | baeFmaf | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 172 | baefma | baefmaw | bae-fmaw | baeFmaw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 173 | baefma | baefmah | bae-fmah | baeFmah | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 174 | baefma | baefmas | bae-fmas | baeFmas | +1 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2) |
| 175 | baefma | baefma | bae-fma | baeFma | +2 | un-donated cluster fm (+2) |
| 176 | ba | baf | baf | Baf | +2 | area-rule final (+2) |
| 177 | ba | baw | baw | Baw | +0 | area-rule final (+2); IS an English word (-2) |
| 178 | ba | bah | bah | Bah | +0 | area-rule final (+2); IS an English word (-2) |
| 179 | ba | bas | bas | Bas | -3 | `s`-final: reserved branch, meant to be RARE (-1); IS an English word (-2) |
| 180 | ba | ba | ba | Ba | -2 | IS an English word (-2) |

## bases starting with `br`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 181 | braefmae | braefmaef | brae-fmaef | braeFmaef | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 182 | braefmae | braefmaew | brae-fmaew | braeFmaew | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 183 | braefmae | braefmaeh | brae-fmaeh | braeFmaeh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 184 | braefmae | braefmaes | brae-fmaes | braeFmaes | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster br (+1) |
| 185 | braefmae | braefmae | brae-fmae | braeFmae | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 186 | bra | braf | braf | Braf | +3 | area-rule final (+2); onset cluster br (+1) |
| 187 | bra | braw | braw | Braw | +1 | area-rule final (+2); onset cluster br (+1); IS an English word (-2) |
| 188 | bra | brah | brah | Brah | +3 | area-rule final (+2); onset cluster br (+1) |
| 189 | bra | bras | bras | Bras | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 190 | bra | bra | bra | Bra | -1 | onset cluster br (+1); IS an English word (-2) |

## bases starting with `c`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 191 | caeifmo | caeifmof | caei-fmof | caeiFmof | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 192 | caeifmo | caeifmow | caei-fmow | caeiFmow | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 193 | caeifmo | caeifmoh | caei-fmoh | caeiFmoh | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 194 | caeifmo | caeifmos | caei-fmos | caeiFmos | +1 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2) |
| 195 | caeifmo | caeifmo | caei-fmo | caeiFmo | +2 | un-donated cluster fm (+2) |
| 196 | ca | caf | caf | Caf | +2 | area-rule final (+2) |
| 197 | ca | caw | caw | Caw | +0 | area-rule final (+2); IS an English word (-2) |
| 198 | ca | cah | cah | Cah | +2 | area-rule final (+2) |
| 199 | ca | cas | cas | Cas | -1 | `s`-final: reserved branch, meant to be RARE (-1) |
| 200 | ca | ca | ca | Ca | -2 | IS an English word (-2) |

## bases starting with `d`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 201 | daefmo | daefmof | dae-fmof | daeFmof | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 202 | daefmo | daefmow | dae-fmow | daeFmow | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 203 | daefmo | daefmoh | dae-fmoh | daeFmoh | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 204 | daefmo | daefmos | dae-fmos | daeFmos | +1 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2) |
| 205 | daefmo | daefmo | dae-fmo | daeFmo | +2 | un-donated cluster fm (+2) |
| 206 | da | daf | daf | Daf | +2 | area-rule final (+2) |
| 207 | da | daw | daw | Daw | +0 | area-rule final (+2); IS an English word (-2) |
| 208 | da | dah | dah | Dah | +0 | area-rule final (+2); IS an English word (-2) |
| 209 | da | das | das | Das | -3 | `s`-final: reserved branch, meant to be RARE (-1); IS an English word (-2) |
| 210 | da | da | da | Da | -2 | IS an English word (-2) |

## bases starting with `dr`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 211 | draefmae | draefmaef | drae-fmaef | draeFmaef | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster dr (+1) |
| 212 | draefmae | draefmaew | drae-fmaew | draeFmaew | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster dr (+1) |
| 213 | draefmae | draefmaeh | drae-fmaeh | draeFmaeh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster dr (+1) |
| 214 | draefmae | draefmaes | drae-fmaes | draeFmaes | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster dr (+1) |
| 215 | draefmae | draefmae | drae-fmae | draeFmae | +3 | un-donated cluster fm (+2); onset cluster dr (+1) |
| 216 | dra | draf | draf | Draf | +3 | area-rule final (+2); onset cluster dr (+1) |
| 217 | dra | draw | draw | Draw | +1 | area-rule final (+2); onset cluster dr (+1); IS an English word (-2) |
| 218 | dra | drah | drah | Drah | +3 | area-rule final (+2); onset cluster dr (+1) |
| 219 | dra | dras | dras | Dras | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster dr (+1) |
| 220 | dra | dra | dra | Dra | +1 | onset cluster dr (+1) |

## bases starting with `f`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 221 | faefmei | faefmeif | fae-fmeif | faeFmeif | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 222 | faefmei | faefmeiw | fae-fmeiw | faeFmeiw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 223 | faefmei | faefmeih | fae-fmeih | faeFmeih | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 224 | faefmei | faefmeis | fae-fmeis | faeFmeis | +1 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2) |
| 225 | faefmei | faefmei | fae-fmei | faeFmei | +2 | un-donated cluster fm (+2) |
| 226 | fa | faf | faf | Faf | +2 | area-rule final (+2) |
| 227 | fa | faw | faw | Faw | +2 | area-rule final (+2) |
| 228 | fa | fah | fah | Fah | +2 | area-rule final (+2) |
| 229 | fa | fas | fas | Fas | -1 | `s`-final: reserved branch, meant to be RARE (-1) |
| 230 | fa | fa | fa | Fa | -2 | IS an English word (-2) |

## bases starting with `g`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 231 | gaefme | gaefmef | gae-fmef | gaeFmef | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 232 | gaefme | gaefmew | gae-fmew | gaeFmew | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 233 | gaefme | gaefmeh | gae-fmeh | gaeFmeh | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 234 | gaefme | gaefmes | gae-fmes | gaeFmes | +1 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2) |
| 235 | gaefme | gaefme | gae-fme | gaeFme | +2 | un-donated cluster fm (+2) |
| 236 | ga | gaf | gaf | Gaf | +2 | area-rule final (+2) |
| 237 | ga | gaw | gaw | Gaw | +0 | area-rule final (+2); IS an English word (-2) |
| 238 | ga | gah | gah | Gah | +2 | area-rule final (+2) |
| 239 | ga | gas | gas | Gas | -3 | `s`-final: reserved branch, meant to be RARE (-1); IS an English word (-2) |
| 240 | ga | ga | ga | Ga | -2 | IS an English word (-2) |

## bases starting with `gr`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 241 | graefmae | graefmaef | grae-fmaef | graeFmaef | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster gr (+1) |
| 242 | graefmae | graefmaew | grae-fmaew | graeFmaew | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster gr (+1) |
| 243 | graefmae | graefmaeh | grae-fmaeh | graeFmaeh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster gr (+1) |
| 244 | graefmae | graefmaes | grae-fmaes | graeFmaes | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster gr (+1) |
| 245 | graefmae | graefmae | grae-fmae | graeFmae | +3 | un-donated cluster fm (+2); onset cluster gr (+1) |
| 246 | gra | graf | graf | Graf | +3 | area-rule final (+2); onset cluster gr (+1) |
| 247 | gra | graw | graw | Graw | +3 | area-rule final (+2); onset cluster gr (+1) |
| 248 | gra | grah | grah | Grah | +3 | area-rule final (+2); onset cluster gr (+1) |
| 249 | gra | gras | gras | Gras | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster gr (+1) |
| 250 | gra | gra | gra | Gra | -1 | onset cluster gr (+1); IS an English word (-2) |

## bases starting with `h`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 251 | haefmou | haefmouf | hae-fmouf | haeFmouf | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 252 | haefmou | haefmouw | hae-fmouw | haeFmouw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 253 | haefmou | haefmouh | hae-fmouh | haeFmouh | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 254 | haefmou | haefmous | hae-fmous | haeFmous | +1 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2) |
| 255 | haefmou | haefmou | hae-fmou | haeFmou | +2 | un-donated cluster fm (+2) |
| 256 | ha | haf | haf | Haf | +2 | area-rule final (+2) |
| 257 | ha | haw | haw | Haw | +0 | area-rule final (+2); IS an English word (-2) |
| 258 | ha | hah | hah | Hah | +0 | area-rule final (+2); IS an English word (-2) |
| 259 | ha | has | has | Has | -1 | `s`-final: reserved branch, meant to be RARE (-1) |
| 260 | ha | ha | ha | Ha | -2 | IS an English word (-2) |

## bases starting with `j`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 261 | jaefmaeu | jaefmaeuf | jae-fmaeuf | jaeFmaeuf | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 262 | jaefmaeu | jaefmaeuw | jae-fmaeuw | jaeFmaeuw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 263 | jaefmaeu | jaefmaeuh | jae-fmaeuh | jaeFmaeuh | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 264 | jaefmaeu | jaefmaeus | jae-fmaeus | jaeFmaeus | +1 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2) |
| 265 | jaefmaeu | jaefmaeu | jae-fmaeu | jaeFmaeu | +2 | un-donated cluster fm (+2) |
| 266 | ja | jaf | jaf | Jaf | +2 | area-rule final (+2) |
| 267 | ja | jaw | jaw | Jaw | +0 | area-rule final (+2); IS an English word (-2) |
| 268 | ja | jah | jah | Jah | +2 | area-rule final (+2) |
| 269 | ja | jas | jas | Jas | -1 | `s`-final: reserved branch, meant to be RARE (-1) |
| 270 | ja | ja | ja | Ja | +0 | - |

## bases starting with `l`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 271 | laefmy | laefmyf | lae-fmyf | laeFmyf | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 272 | laefmy | laefmyw | lae-fmyw | laeFmyw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 273 | laefmy | laefmyh | lae-fmyh | laeFmyh | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 274 | laefmy | laefmys | lae-fmys | laeFmys | +1 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2) |
| 275 | laefmy | laefmy | lae-fmy | laeFmy | +2 | un-donated cluster fm (+2) |
| 276 | la | laf | laf | Laf | +2 | area-rule final (+2) |
| 277 | la | law | law | Law | +0 | area-rule final (+2); IS an English word (-2) |
| 278 | la | lah | lah | Lah | +2 | area-rule final (+2) |
| 279 | la | las | las | Las | -3 | `s`-final: reserved branch, meant to be RARE (-1); IS an English word (-2) |
| 280 | la | la | la | La | -2 | IS an English word (-2) |

## bases starting with `m`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 281 | maefmu | maefmuf | mae-fmuf | maeFmuf | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 282 | maefmu | maefmuw | mae-fmuw | maeFmuw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 283 | maefmu | maefmuh | mae-fmuh | maeFmuh | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 284 | maefmu | maefmus | mae-fmus | maeFmus | +1 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2) |
| 285 | maefmu | maefmu | mae-fmu | maeFmu | +2 | un-donated cluster fm (+2) |
| 286 | ma | maf | maf | Maf | +2 | area-rule final (+2) |
| 287 | ma | maw | maw | Maw | +0 | area-rule final (+2); IS an English word (-2) |
| 288 | ma | mah | mah | Mah | +0 | area-rule final (+2); IS an English word (-2) |
| 289 | ma | mas | mas | Mas | -3 | `s`-final: reserved branch, meant to be RARE (-1); IS an English word (-2) |
| 290 | ma | ma | ma | Ma | -2 | IS an English word (-2) |

## bases starting with `n`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 291 | naefmi | naefmif | nae-fmif | naeFmif | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 292 | naefmi | naefmiw | nae-fmiw | naeFmiw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 293 | naefmi | naefmih | nae-fmih | naeFmih | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 294 | naefmi | naefmis | nae-fmis | naeFmis | +1 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2) |
| 295 | naefmi | naefmi | nae-fmi | naeFmi | +2 | un-donated cluster fm (+2) |
| 296 | na | naf | naf | Naf | +2 | area-rule final (+2) |
| 297 | na | naw | naw | Naw | +0 | area-rule final (+2); IS an English word (-2) |
| 298 | na | nah | nah | Nah | +2 | area-rule final (+2) |
| 299 | na | nas | nas | Nas | -1 | `s`-final: reserved branch, meant to be RARE (-1) |
| 300 | na | na | na | Na | -2 | IS an English word (-2) |

## bases starting with `r`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 301 | raefmai | raefmaif | rae-fmaif | raeFmaif | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 302 | raefmai | raefmaiw | rae-fmaiw | raeFmaiw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 303 | raefmai | raefmaih | rae-fmaih | raeFmaih | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 304 | raefmai | raefmais | rae-fmais | raeFmais | +1 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2) |
| 305 | raefmai | raefmai | rae-fmai | raeFmai | +2 | un-donated cluster fm (+2) |
| 306 | ra | raf | raf | Raf | +2 | area-rule final (+2) |
| 307 | ra | raw | raw | Raw | +0 | area-rule final (+2); IS an English word (-2) |
| 308 | ra | rah | rah | Rah | +0 | area-rule final (+2); IS an English word (-2) |
| 309 | ra | ras | ras | Ras | -3 | `s`-final: reserved branch, meant to be RARE (-1); IS an English word (-2) |
| 310 | ra | ra | ra | Ra | -2 | IS an English word (-2) |

## bases starting with `s`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 311 | saefmoi | saefmoif | sae-fmoif | saeFmoif | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 312 | saefmoi | saefmoiw | sae-fmoiw | saeFmoiw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 313 | saefmoi | saefmoih | sae-fmoih | saeFmoih | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 314 | saefmoi | saefmois | sae-fmois | saeFmois | +1 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2) |
| 315 | saefmoi | saefmoi | sae-fmoi | saeFmoi | +2 | un-donated cluster fm (+2) |
| 316 | sa | saf | saf | Saf | +2 | area-rule final (+2) |
| 317 | sa | saw | saw | Saw | +0 | area-rule final (+2); IS an English word (-2) |
| 318 | sa | sah | sah | Sah | +0 | area-rule final (+2); IS an English word (-2) |
| 319 | sa | sas | sas | Sas | -1 | `s`-final: reserved branch, meant to be RARE (-1) |
| 320 | sa | sa | sa | Sa | -2 | IS an English word (-2) |

## bases starting with `sh`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 321 | shaefmeu | shaefmeuf | shae-fmeuf | shaeFmeuf | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 322 | shaefmeu | shaefmeuw | shae-fmeuw | shaeFmeuw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 323 | shaefmeu | shaefmeuh | shae-fmeuh | shaeFmeuh | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 324 | shaefmeu | shaefmeus | shae-fmeus | shaeFmeus | +1 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2) |
| 325 | shaefmeu | shaefmeu | shae-fmeu | shaeFmeu | +2 | un-donated cluster fm (+2) |
| 326 | sha | shaf | shaf | Shaf | +2 | area-rule final (+2) |
| 327 | sha | shaw | shaw | Shaw | +0 | area-rule final (+2); IS an English word (-2) |
| 328 | sha | shah | shah | Shah | +0 | area-rule final (+2); IS an English word (-2) |
| 329 | sha | shas | shas | Shas | -1 | `s`-final: reserved branch, meant to be RARE (-1) |
| 330 | sha | sha | sha | Sha | -2 | IS an English word (-2) |

## bases starting with `th`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 331 | thaefmaei | thaefmaeif | thae-fmaeif | thaeFmaeif | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 332 | thaefmaei | thaefmaeiw | thae-fmaeiw | thaeFmaeiw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 333 | thaefmaei | thaefmaeih | thae-fmaeih | thaeFmaeih | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 334 | thaefmaei | thaefmaeis | thae-fmaeis | thaeFmaeis | +1 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2) |
| 335 | thaefmaei | thaefmaei | thae-fmaei | thaeFmaei | +2 | un-donated cluster fm (+2) |
| 336 | tha | thaf | thaf | Thaf | +2 | area-rule final (+2) |
| 337 | tha | thaw | thaw | Thaw | +0 | area-rule final (+2); IS an English word (-2) |
| 338 | tha | thah | thah | Thah | +2 | area-rule final (+2) |
| 339 | tha | thas | thas | Thas | -1 | `s`-final: reserved branch, meant to be RARE (-1) |
| 340 | tha | tha | tha | Tha | -2 | IS an English word (-2) |

## bases starting with `w`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 341 | waefmau | waefmauf | wae-fmauf | waeFmauf | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 342 | waefmau | waefmauw | wae-fmauw | waeFmauw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 343 | waefmau | waefmauh | wae-fmauh | waeFmauh | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 344 | waefmau | waefmaus | wae-fmaus | waeFmaus | +1 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2) |
| 345 | waefmau | waefmau | wae-fmau | waeFmau | +2 | un-donated cluster fm (+2) |
| 346 | wae | waef | waef | Waef | +2 | area-rule final (+2) |
| 347 | wae | waew | waew | Waew | +2 | area-rule final (+2) |
| 348 | wae | waeh | waeh | Waeh | +2 | area-rule final (+2) |
| 349 | wae | waes | waes | Waes | -1 | `s`-final: reserved branch, meant to be RARE (-1) |
| 350 | wae | wae | wae | Wae | -2 | IS an English word (-2) |

## bases whose first vowel is `a`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 351 | brafma | brafmaf | bra-fmaf | braFmaf | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 352 | brafma | brafmaw | bra-fmaw | braFmaw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 353 | brafma | brafmah | bra-fmah | braFmah | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 354 | brafma | brafmas | bra-fmas | braFmas | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster br (+1) |
| 355 | brafma | brafma | bra-fma | braFma | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 356 | bra | braf | braf | Braf | +3 | area-rule final (+2); onset cluster br (+1) |
| 357 | bra | braw | braw | Braw | +1 | area-rule final (+2); onset cluster br (+1); IS an English word (-2) |
| 358 | bra | brah | brah | Brah | +3 | area-rule final (+2); onset cluster br (+1) |
| 359 | bra | bras | bras | Bras | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 360 | bra | bra | bra | Bra | -1 | onset cluster br (+1); IS an English word (-2) |

## bases whose first vowel is `ae`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 361 | braefmae | braefmaef | brae-fmaef | braeFmaef | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 362 | braefmae | braefmaew | brae-fmaew | braeFmaew | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 363 | braefmae | braefmaeh | brae-fmaeh | braeFmaeh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 364 | braefmae | braefmaes | brae-fmaes | braeFmaes | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster br (+1) |
| 365 | braefmae | braefmae | brae-fmae | braeFmae | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 366 | brae | braef | braef | Braef | +3 | area-rule final (+2); onset cluster br (+1) |
| 367 | brae | braew | braew | Braew | +3 | area-rule final (+2); onset cluster br (+1) |
| 368 | brae | braeh | braeh | Braeh | +3 | area-rule final (+2); onset cluster br (+1) |
| 369 | brae | braes | braes | Braes | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 370 | brae | brae | brae | Brae | -1 | onset cluster br (+1); IS an English word (-2) |

## bases whose first vowel is `aei`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 371 | braeifmaei | braeifmaeif | braei-fmaeif | braeiFmaeif | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 372 | braeifmaei | braeifmaeiw | braei-fmaeiw | braeiFmaeiw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 373 | braeifmaei | braeifmaeih | braei-fmaeih | braeiFmaeih | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 374 | braeifmaei | braeifmaeis | braei-fmaeis | braeiFmaeis | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster br (+1) |
| 375 | braeifmaei | braeifmaei | braei-fmaei | braeiFmaei | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 376 | braei | braeif | braeif | Braeif | +3 | area-rule final (+2); onset cluster br (+1) |
| 377 | braei | braeiw | braeiw | Braeiw | +3 | area-rule final (+2); onset cluster br (+1) |
| 378 | braei | braeih | braeih | Braeih | +3 | area-rule final (+2); onset cluster br (+1) |
| 379 | braei | braeis | braeis | Braeis | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 380 | braei | braei | braei | Braei | +1 | onset cluster br (+1) |

## bases whose first vowel is `aeu`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 381 | braeufmaeu | braeufmaeuf | braeu-fmaeuf | braeuFmaeuf | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 382 | braeufmaeu | braeufmaeuw | braeu-fmaeuw | braeuFmaeuw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 383 | braeufmaeu | braeufmaeuh | braeu-fmaeuh | braeuFmaeuh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 384 | braeufmaeu | braeufmaeus | braeu-fmaeus | braeuFmaeus | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster br (+1) |
| 385 | braeufmaeu | braeufmaeu | braeu-fmaeu | braeuFmaeu | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 386 | braeu | braeuf | braeuf | Braeuf | +3 | area-rule final (+2); onset cluster br (+1) |
| 387 | braeu | braeuw | braeuw | Braeuw | +3 | area-rule final (+2); onset cluster br (+1) |
| 388 | braeu | braeuh | braeuh | Braeuh | +3 | area-rule final (+2); onset cluster br (+1) |
| 389 | braeu | braeus | braeus | Braeus | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 390 | braeu | braeu | braeu | Braeu | +1 | onset cluster br (+1) |

## bases whose first vowel is `ai`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 391 | braifmai | braifmaif | brai-fmaif | braiFmaif | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 392 | braifmai | braifmaiw | brai-fmaiw | braiFmaiw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 393 | braifmai | braifmaih | brai-fmaih | braiFmaih | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 394 | braifmai | braifmais | brai-fmais | braiFmais | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster br (+1) |
| 395 | braifmai | braifmai | brai-fmai | braiFmai | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 396 | brai | braif | braif | Braif | +3 | area-rule final (+2); onset cluster br (+1) |
| 397 | brai | braiw | braiw | Braiw | +3 | area-rule final (+2); onset cluster br (+1) |
| 398 | brai | braih | braih | Braih | +3 | area-rule final (+2); onset cluster br (+1) |
| 399 | brai | brais | brais | Brais | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 400 | brai | brai | brai | Brai | +1 | onset cluster br (+1) |

## bases whose first vowel is `au`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 401 | braufmau | braufmauf | brau-fmauf | brauFmauf | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 402 | braufmau | braufmauw | brau-fmauw | brauFmauw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 403 | braufmau | braufmauh | brau-fmauh | brauFmauh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 404 | braufmau | braufmaus | brau-fmaus | brauFmaus | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster br (+1) |
| 405 | braufmau | braufmau | brau-fmau | brauFmau | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 406 | brau | brauf | brauf | Brauf | +3 | area-rule final (+2); onset cluster br (+1) |
| 407 | brau | brauw | brauw | Brauw | +3 | area-rule final (+2); onset cluster br (+1) |
| 408 | brau | brauh | brauh | Brauh | +3 | area-rule final (+2); onset cluster br (+1) |
| 409 | brau | braus | braus | Braus | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 410 | brau | brau | brau | Brau | +1 | onset cluster br (+1) |

## bases whose first vowel is `e`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 411 | brefme | brefmef | bre-fmef | breFmef | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 412 | brefme | brefmew | bre-fmew | breFmew | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 413 | brefme | brefmeh | bre-fmeh | breFmeh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 414 | brefme | brefmes | bre-fmes | breFmes | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster br (+1) |
| 415 | brefme | brefme | bre-fme | breFme | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 416 | bre | bref | bref | Bref | +3 | area-rule final (+2); onset cluster br (+1) |
| 417 | bre | brew | brew | Brew | +1 | area-rule final (+2); onset cluster br (+1); IS an English word (-2) |
| 418 | bre | breh | breh | Breh | +3 | area-rule final (+2); onset cluster br (+1) |
| 419 | bre | bres | bres | Bres | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 420 | bre | bre | bre | Bre | +1 | onset cluster br (+1) |

## bases whose first vowel is `ei`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 421 | breifmei | breifmeif | brei-fmeif | breiFmeif | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 422 | breifmei | breifmeiw | brei-fmeiw | breiFmeiw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 423 | breifmei | breifmeih | brei-fmeih | breiFmeih | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 424 | breifmei | breifmeis | brei-fmeis | breiFmeis | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster br (+1) |
| 425 | breifmei | breifmei | brei-fmei | breiFmei | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 426 | brei | breif | breif | Breif | +3 | area-rule final (+2); onset cluster br (+1) |
| 427 | brei | breiw | breiw | Breiw | +3 | area-rule final (+2); onset cluster br (+1) |
| 428 | brei | breih | breih | Breih | +3 | area-rule final (+2); onset cluster br (+1) |
| 429 | brei | breis | breis | Breis | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 430 | brei | brei | brei | Brei | -1 | onset cluster br (+1); IS an English word (-2) |

## bases whose first vowel is `eu`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 431 | breufmeu | breufmeuf | breu-fmeuf | breuFmeuf | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 432 | breufmeu | breufmeuw | breu-fmeuw | breuFmeuw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 433 | breufmeu | breufmeuh | breu-fmeuh | breuFmeuh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 434 | breufmeu | breufmeus | breu-fmeus | breuFmeus | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster br (+1) |
| 435 | breufmeu | breufmeu | breu-fmeu | breuFmeu | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 436 | breu | breuf | breuf | Breuf | +3 | area-rule final (+2); onset cluster br (+1) |
| 437 | breu | breuw | breuw | Breuw | +3 | area-rule final (+2); onset cluster br (+1) |
| 438 | breu | breuh | breuh | Breuh | +3 | area-rule final (+2); onset cluster br (+1) |
| 439 | breu | breus | breus | Breus | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 440 | breu | breu | breu | Breu | +1 | onset cluster br (+1) |

## bases whose first vowel is `i`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 441 | brifmi | brifmif | bri-fmif | briFmif | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 442 | brifmi | brifmiw | bri-fmiw | briFmiw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 443 | brifmi | brifmih | bri-fmih | briFmih | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 444 | brifmi | brifmis | bri-fmis | briFmis | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster br (+1) |
| 445 | brifmi | brifmi | bri-fmi | briFmi | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 446 | bri | brif | brif | Brif | +3 | area-rule final (+2); onset cluster br (+1) |
| 447 | bri | briw | briw | Briw | +3 | area-rule final (+2); onset cluster br (+1) |
| 448 | bri | brih | brih | Brih | +3 | area-rule final (+2); onset cluster br (+1) |
| 449 | bri | bris | bris | Bris | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 450 | bri | bri | bri | Bri | +1 | onset cluster br (+1) |

## bases whose first vowel is `o`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 451 | brofmo | brofmof | bro-fmof | broFmof | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 452 | brofmo | brofmow | bro-fmow | broFmow | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 453 | brofmo | brofmoh | bro-fmoh | broFmoh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 454 | brofmo | brofmos | bro-fmos | broFmos | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster br (+1) |
| 455 | brofmo | brofmo | bro-fmo | broFmo | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 456 | bro | brof | brof | Brof | +3 | area-rule final (+2); onset cluster br (+1) |
| 457 | bro | brow | brow | Brow | +1 | area-rule final (+2); onset cluster br (+1); IS an English word (-2) |
| 458 | bro | broh | broh | Broh | +3 | area-rule final (+2); onset cluster br (+1) |
| 459 | bro | bros | bros | Bros | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 460 | bro | bro | bro | Bro | +1 | onset cluster br (+1) |

## bases whose first vowel is `oi`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 461 | broifmoi | broifmoif | broi-fmoif | broiFmoif | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 462 | broifmoi | broifmoiw | broi-fmoiw | broiFmoiw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 463 | broifmoi | broifmoih | broi-fmoih | broiFmoih | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 464 | broifmoi | broifmois | broi-fmois | broiFmois | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster br (+1) |
| 465 | broifmoi | broifmoi | broi-fmoi | broiFmoi | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 466 | broi | broif | broif | Broif | +3 | area-rule final (+2); onset cluster br (+1) |
| 467 | broi | broiw | broiw | Broiw | +3 | area-rule final (+2); onset cluster br (+1) |
| 468 | broi | broih | broih | Broih | +3 | area-rule final (+2); onset cluster br (+1) |
| 469 | broi | brois | brois | Brois | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 470 | broi | broi | broi | Broi | +1 | onset cluster br (+1) |

## bases whose first vowel is `ou`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 471 | broufmou | broufmouf | brou-fmouf | brouFmouf | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 472 | broufmou | broufmouw | brou-fmouw | brouFmouw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 473 | broufmou | broufmouh | brou-fmouh | brouFmouh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 474 | broufmou | broufmous | brou-fmous | brouFmous | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster br (+1) |
| 475 | broufmou | broufmou | brou-fmou | brouFmou | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 476 | brou | brouf | brouf | Brouf | +3 | area-rule final (+2); onset cluster br (+1) |
| 477 | brou | brouw | brouw | Brouw | +3 | area-rule final (+2); onset cluster br (+1) |
| 478 | brou | brouh | brouh | Brouh | +3 | area-rule final (+2); onset cluster br (+1) |
| 479 | brou | brous | brous | Brous | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 480 | brou | brou | brou | Brou | +1 | onset cluster br (+1) |

## bases whose first vowel is `u`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 481 | brufmu | brufmuf | bru-fmuf | bruFmuf | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 482 | brufmu | brufmuw | bru-fmuw | bruFmuw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 483 | brufmu | brufmuh | bru-fmuh | bruFmuh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 484 | brufmu | brufmus | bru-fmus | bruFmus | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster br (+1) |
| 485 | brufmu | brufmu | bru-fmu | bruFmu | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 486 | bru | bruf | bruf | Bruf | +3 | area-rule final (+2); onset cluster br (+1) |
| 487 | bru | bruw | bruw | Bruw | +3 | area-rule final (+2); onset cluster br (+1) |
| 488 | bru | bruh | bruh | Bruh | +3 | area-rule final (+2); onset cluster br (+1) |
| 489 | bru | brus | brus | Brus | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 490 | bru | bru | bru | Bru | +1 | onset cluster br (+1) |

## bases whose first vowel is `y`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 491 | bryfmy | bryfmyf | bry-fmyf | bryFmyf | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 492 | bryfmy | bryfmyw | bry-fmyw | bryFmyw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 493 | bryfmy | bryfmyh | bry-fmyh | bryFmyh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 494 | bryfmy | bryfmys | bry-fmys | bryFmys | +2 | `s`-final: reserved branch, meant to be RARE (-1); un-donated cluster fm (+2); onset cluster br (+1) |
| 495 | bryfmy | bryfmy | bry-fmy | bryFmy | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 496 | bry | bryf | bryf | Bryf | +3 | area-rule final (+2); onset cluster br (+1) |
| 497 | bry | bryw | bryw | Bryw | +3 | area-rule final (+2); onset cluster br (+1) |
| 498 | bry | bryh | bryh | Bryh | +3 | area-rule final (+2); onset cluster br (+1) |
| 499 | bry | brys | brys | Brys | +0 | `s`-final: reserved branch, meant to be RARE (-1); onset cluster br (+1) |
| 500 | bry | bry | bry | Bry | +1 | onset cluster br (+1) |

## English collisions (measured - avoid or accept knowingly)

421 forms are literally in `/usr/share/dict/words`, so a pick can never hit one by accident:

```
aw ah as abas aba age agrah agra aly ammi amos anis ani anta argas arrau aru aes ae ai aire auh aus baw bah bas ba bago balai baris bari barny bae bais bes be bedew belga bema bis bilgy bilo birdy birgus bow bos bo bodo boga bolis bony bois bouw bounce bus bu bufo bullous buna by byre braw bra brahma branny branta brassy brae brew brei bribri brow brolga broma caw ca caltha carry carse ce cerris cow cos coca cormous cothy coif courge cumshaw daw dah das da dado dali dae dais daira dauw dew de demos denis desma dis di dine dow dos do dome doris dori dure draw draba drew drow dry eh es edo elbow eli eu fa fanwe farsi fae few fe feif feis fei feu fi fibrous fishy fow fo follow fou fu gaw gas ga gade galga gary gaus gau ges ge genus genu geisha gif gi gos go gossy goi gus gula gra grampa granny grassy graeme grew grebe gris grigri grow gros grouf grus grugru haw hah ha hance hange hau hew he hei his hi hithe how ho hohe holly horse hoi houri huh hu hurrah
```

(... and 221 more; raise --max-en)


---

## What the menu does NOT do

- It cannot tell you what sounds *beautiful* - that is the part only you can supply.
- It contains **no 1-syllable (`roi`-class) root**: the pool is the 2-syllable core
  (`../decision/03-open-questions.md` section 0 item 22). Wanting short roots in this round means
  extending that pool FIRST - which changes the numbering here.
- It does not test the **M3a seam** (root-final `f`/`w`/`h` + a case suffix, always unstressed) -
  still unjudged (section 0 item 20), and it fires for 3 of every 4 coined roots.
