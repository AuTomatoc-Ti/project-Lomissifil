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
| **-2** | the form **IS an English word** | measured: 143 of 105,936 forms (0.135%) are in Webster's 2nd |

Every row shows **why** it scored. The weights live in one place: `tools/menu.py`, `score()`.

⚠️ This biases the *shortlist*, never the language: the pool is untouched, and a low score is not a
verdict - it only means "this form is built from material that many languages share".

## How to read a row

`#` is this menu's own numbering. `syllables` and `stress` come from `tools/syllabify.py` (default
stress = the 2nd syllable of the root, P4/N1; the capital lands on the *first letter* of the stressed
syllable). **A group of four rows is ONE base**, in the fixed order `+f | +w (/v/) | +h | bare`, and a
base yields exactly **2** roots - so pick **at most one** from the `{+f, +w}` pair and **at most one**
from the `{+h, bare}` pair.

> Sound-only: R3 is PARKED, so assign **no meanings** (`../decision/03-open-questions.md` section 0
> item 14). A pick is not a word; `../reference/example.md` stays the only source for examples.

---
## Top 20 bases - the most "ours" material

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 1 | braefmae | braefmaef | brae-fmaef | braeFmaef | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 2 | braefmae | braefmaew | brae-fmaew | braeFmaew | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 3 | braefmae | braefmaeh | brae-fmaeh | braeFmaeh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 4 | braefmae | braefmae | brae-fmae | braeFmae | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 5 | braefnae | braefnaef | brae-fnaef | braeFnaef | +5 | area-rule final (+2); un-donated cluster fn (+2); onset cluster br (+1) |
| 6 | braefnae | braefnaew | brae-fnaew | braeFnaew | +5 | area-rule final (+2); un-donated cluster fn (+2); onset cluster br (+1) |
| 7 | braefnae | braefnaeh | brae-fnaeh | braeFnaeh | +5 | area-rule final (+2); un-donated cluster fn (+2); onset cluster br (+1) |
| 8 | braefnae | braefnae | brae-fnae | braeFnae | +3 | un-donated cluster fn (+2); onset cluster br (+1) |
| 9 | braehmae | braehmaef | brae-hmaef | braeHmaef | +5 | area-rule final (+2); un-donated cluster hm (+2); onset cluster br (+1) |
| 10 | braehmae | braehmaew | brae-hmaew | braeHmaew | +5 | area-rule final (+2); un-donated cluster hm (+2); onset cluster br (+1) |
| 11 | braehmae | braehmaeh | brae-hmaeh | braeHmaeh | +5 | area-rule final (+2); un-donated cluster hm (+2); onset cluster br (+1) |
| 12 | braehmae | braehmae | brae-hmae | braeHmae | +3 | un-donated cluster hm (+2); onset cluster br (+1) |
| 13 | braehnae | braehnaef | brae-hnaef | braeHnaef | +5 | area-rule final (+2); un-donated cluster hn (+2); onset cluster br (+1) |
| 14 | braehnae | braehnaew | brae-hnaew | braeHnaew | +5 | area-rule final (+2); un-donated cluster hn (+2); onset cluster br (+1) |
| 15 | braehnae | braehnaeh | brae-hnaeh | braeHnaeh | +5 | area-rule final (+2); un-donated cluster hn (+2); onset cluster br (+1) |
| 16 | braehnae | braehnae | brae-hnae | braeHnae | +3 | un-donated cluster hn (+2); onset cluster br (+1) |
| 17 | braeifmaei | braeifmaeif | braei-fmaeif | braeiFmaeif | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 18 | braeifmaei | braeifmaeiw | braei-fmaeiw | braeiFmaeiw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 19 | braeifmaei | braeifmaeih | braei-fmaeih | braeiFmaeih | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 20 | braeifmaei | braeifmaei | braei-fmaei | braeiFmaei | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 21 | braeifnaei | braeifnaeif | braei-fnaeif | braeiFnaeif | +5 | area-rule final (+2); un-donated cluster fn (+2); onset cluster br (+1) |
| 22 | braeifnaei | braeifnaeiw | braei-fnaeiw | braeiFnaeiw | +5 | area-rule final (+2); un-donated cluster fn (+2); onset cluster br (+1) |
| 23 | braeifnaei | braeifnaeih | braei-fnaeih | braeiFnaeih | +5 | area-rule final (+2); un-donated cluster fn (+2); onset cluster br (+1) |
| 24 | braeifnaei | braeifnaei | braei-fnaei | braeiFnaei | +3 | un-donated cluster fn (+2); onset cluster br (+1) |
| 25 | braeihmaei | braeihmaeif | braei-hmaeif | braeiHmaeif | +5 | area-rule final (+2); un-donated cluster hm (+2); onset cluster br (+1) |
| 26 | braeihmaei | braeihmaeiw | braei-hmaeiw | braeiHmaeiw | +5 | area-rule final (+2); un-donated cluster hm (+2); onset cluster br (+1) |
| 27 | braeihmaei | braeihmaeih | braei-hmaeih | braeiHmaeih | +5 | area-rule final (+2); un-donated cluster hm (+2); onset cluster br (+1) |
| 28 | braeihmaei | braeihmaei | braei-hmaei | braeiHmaei | +3 | un-donated cluster hm (+2); onset cluster br (+1) |
| 29 | braeihnaei | braeihnaeif | braei-hnaeif | braeiHnaeif | +5 | area-rule final (+2); un-donated cluster hn (+2); onset cluster br (+1) |
| 30 | braeihnaei | braeihnaeiw | braei-hnaeiw | braeiHnaeiw | +5 | area-rule final (+2); un-donated cluster hn (+2); onset cluster br (+1) |
| 31 | braeihnaei | braeihnaeih | braei-hnaeih | braeiHnaeih | +5 | area-rule final (+2); un-donated cluster hn (+2); onset cluster br (+1) |
| 32 | braeihnaei | braeihnaei | braei-hnaei | braeiHnaei | +3 | un-donated cluster hn (+2); onset cluster br (+1) |
| 33 | braeijmaei | braeijmaeif | braei-jmaeif | braeiJmaeif | +5 | area-rule final (+2); un-donated cluster jm (+2); onset cluster br (+1) |
| 34 | braeijmaei | braeijmaeiw | braei-jmaeiw | braeiJmaeiw | +5 | area-rule final (+2); un-donated cluster jm (+2); onset cluster br (+1) |
| 35 | braeijmaei | braeijmaeih | braei-jmaeih | braeiJmaeih | +5 | area-rule final (+2); un-donated cluster jm (+2); onset cluster br (+1) |
| 36 | braeijmaei | braeijmaei | braei-jmaei | braeiJmaei | +3 | un-donated cluster jm (+2); onset cluster br (+1) |
| 37 | braeijnaei | braeijnaeif | braei-jnaeif | braeiJnaeif | +5 | area-rule final (+2); un-donated cluster jn (+2); onset cluster br (+1) |
| 38 | braeijnaei | braeijnaeiw | braei-jnaeiw | braeiJnaeiw | +5 | area-rule final (+2); un-donated cluster jn (+2); onset cluster br (+1) |
| 39 | braeijnaei | braeijnaeih | braei-jnaeih | braeiJnaeih | +5 | area-rule final (+2); un-donated cluster jn (+2); onset cluster br (+1) |
| 40 | braeijnaei | braeijnaei | braei-jnaei | braeiJnaei | +3 | un-donated cluster jn (+2); onset cluster br (+1) |
| 41 | braeiwmaei | braeiwmaeif | braei-wmaeif | braeiWmaeif | +5 | area-rule final (+2); un-donated cluster wm (+2); onset cluster br (+1) |
| 42 | braeiwmaei | braeiwmaeiw | braei-wmaeiw | braeiWmaeiw | +5 | area-rule final (+2); un-donated cluster wm (+2); onset cluster br (+1) |
| 43 | braeiwmaei | braeiwmaeih | braei-wmaeih | braeiWmaeih | +5 | area-rule final (+2); un-donated cluster wm (+2); onset cluster br (+1) |
| 44 | braeiwmaei | braeiwmaei | braei-wmaei | braeiWmaei | +3 | un-donated cluster wm (+2); onset cluster br (+1) |
| 45 | braeiwnaei | braeiwnaeif | braei-wnaeif | braeiWnaeif | +5 | area-rule final (+2); un-donated cluster wn (+2); onset cluster br (+1) |
| 46 | braeiwnaei | braeiwnaeiw | braei-wnaeiw | braeiWnaeiw | +5 | area-rule final (+2); un-donated cluster wn (+2); onset cluster br (+1) |
| 47 | braeiwnaei | braeiwnaeih | braei-wnaeih | braeiWnaeih | +5 | area-rule final (+2); un-donated cluster wn (+2); onset cluster br (+1) |
| 48 | braeiwnaei | braeiwnaei | braei-wnaei | braeiWnaei | +3 | un-donated cluster wn (+2); onset cluster br (+1) |
| 49 | braejmae | braejmaef | brae-jmaef | braeJmaef | +5 | area-rule final (+2); un-donated cluster jm (+2); onset cluster br (+1) |
| 50 | braejmae | braejmaew | brae-jmaew | braeJmaew | +5 | area-rule final (+2); un-donated cluster jm (+2); onset cluster br (+1) |
| 51 | braejmae | braejmaeh | brae-jmaeh | braeJmaeh | +5 | area-rule final (+2); un-donated cluster jm (+2); onset cluster br (+1) |
| 52 | braejmae | braejmae | brae-jmae | braeJmae | +3 | un-donated cluster jm (+2); onset cluster br (+1) |
| 53 | braejnae | braejnaef | brae-jnaef | braeJnaef | +5 | area-rule final (+2); un-donated cluster jn (+2); onset cluster br (+1) |
| 54 | braejnae | braejnaew | brae-jnaew | braeJnaew | +5 | area-rule final (+2); un-donated cluster jn (+2); onset cluster br (+1) |
| 55 | braejnae | braejnaeh | brae-jnaeh | braeJnaeh | +5 | area-rule final (+2); un-donated cluster jn (+2); onset cluster br (+1) |
| 56 | braejnae | braejnae | brae-jnae | braeJnae | +3 | un-donated cluster jn (+2); onset cluster br (+1) |
| 57 | braeufmaeu | braeufmaeuf | braeu-fmaeuf | braeuFmaeuf | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 58 | braeufmaeu | braeufmaeuw | braeu-fmaeuw | braeuFmaeuw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 59 | braeufmaeu | braeufmaeuh | braeu-fmaeuh | braeuFmaeuh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 60 | braeufmaeu | braeufmaeu | braeu-fmaeu | braeuFmaeu | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 61 | braeufnaeu | braeufnaeuf | braeu-fnaeuf | braeuFnaeuf | +5 | area-rule final (+2); un-donated cluster fn (+2); onset cluster br (+1) |
| 62 | braeufnaeu | braeufnaeuw | braeu-fnaeuw | braeuFnaeuw | +5 | area-rule final (+2); un-donated cluster fn (+2); onset cluster br (+1) |
| 63 | braeufnaeu | braeufnaeuh | braeu-fnaeuh | braeuFnaeuh | +5 | area-rule final (+2); un-donated cluster fn (+2); onset cluster br (+1) |
| 64 | braeufnaeu | braeufnaeu | braeu-fnaeu | braeuFnaeu | +3 | un-donated cluster fn (+2); onset cluster br (+1) |
| 65 | braeuhmaeu | braeuhmaeuf | braeu-hmaeuf | braeuHmaeuf | +5 | area-rule final (+2); un-donated cluster hm (+2); onset cluster br (+1) |
| 66 | braeuhmaeu | braeuhmaeuw | braeu-hmaeuw | braeuHmaeuw | +5 | area-rule final (+2); un-donated cluster hm (+2); onset cluster br (+1) |
| 67 | braeuhmaeu | braeuhmaeuh | braeu-hmaeuh | braeuHmaeuh | +5 | area-rule final (+2); un-donated cluster hm (+2); onset cluster br (+1) |
| 68 | braeuhmaeu | braeuhmaeu | braeu-hmaeu | braeuHmaeu | +3 | un-donated cluster hm (+2); onset cluster br (+1) |
| 69 | braeuhnaeu | braeuhnaeuf | braeu-hnaeuf | braeuHnaeuf | +5 | area-rule final (+2); un-donated cluster hn (+2); onset cluster br (+1) |
| 70 | braeuhnaeu | braeuhnaeuw | braeu-hnaeuw | braeuHnaeuw | +5 | area-rule final (+2); un-donated cluster hn (+2); onset cluster br (+1) |
| 71 | braeuhnaeu | braeuhnaeuh | braeu-hnaeuh | braeuHnaeuh | +5 | area-rule final (+2); un-donated cluster hn (+2); onset cluster br (+1) |
| 72 | braeuhnaeu | braeuhnaeu | braeu-hnaeu | braeuHnaeu | +3 | un-donated cluster hn (+2); onset cluster br (+1) |
| 73 | braeujmaeu | braeujmaeuf | braeu-jmaeuf | braeuJmaeuf | +5 | area-rule final (+2); un-donated cluster jm (+2); onset cluster br (+1) |
| 74 | braeujmaeu | braeujmaeuw | braeu-jmaeuw | braeuJmaeuw | +5 | area-rule final (+2); un-donated cluster jm (+2); onset cluster br (+1) |
| 75 | braeujmaeu | braeujmaeuh | braeu-jmaeuh | braeuJmaeuh | +5 | area-rule final (+2); un-donated cluster jm (+2); onset cluster br (+1) |
| 76 | braeujmaeu | braeujmaeu | braeu-jmaeu | braeuJmaeu | +3 | un-donated cluster jm (+2); onset cluster br (+1) |
| 77 | braeujnaeu | braeujnaeuf | braeu-jnaeuf | braeuJnaeuf | +5 | area-rule final (+2); un-donated cluster jn (+2); onset cluster br (+1) |
| 78 | braeujnaeu | braeujnaeuw | braeu-jnaeuw | braeuJnaeuw | +5 | area-rule final (+2); un-donated cluster jn (+2); onset cluster br (+1) |
| 79 | braeujnaeu | braeujnaeuh | braeu-jnaeuh | braeuJnaeuh | +5 | area-rule final (+2); un-donated cluster jn (+2); onset cluster br (+1) |
| 80 | braeujnaeu | braeujnaeu | braeu-jnaeu | braeuJnaeu | +3 | un-donated cluster jn (+2); onset cluster br (+1) |

## one-syllable roots (the `roi` class): top 12 of 285 - they are EXEMPT from the soft distance>=2 rule, so they resemble each other by nature

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 81 | bra | braf | braf | Braf | +3 | area-rule final (+2); onset cluster br (+1) |
| 82 | bra | braw | braw | Braw | +1 | area-rule final (+2); onset cluster br (+1); IS an English word (-2) |
| 83 | bra | brah | brah | Brah | +3 | area-rule final (+2); onset cluster br (+1) |
| 84 | bra | bra | bra | Bra | -1 | onset cluster br (+1); IS an English word (-2) |
| 85 | brae | braef | braef | Braef | +3 | area-rule final (+2); onset cluster br (+1) |
| 86 | brae | braew | braew | Braew | +3 | area-rule final (+2); onset cluster br (+1) |
| 87 | brae | braeh | braeh | Braeh | +3 | area-rule final (+2); onset cluster br (+1) |
| 88 | brae | brae | brae | Brae | -1 | onset cluster br (+1); IS an English word (-2) |
| 89 | braei | braeif | braeif | Braeif | +3 | area-rule final (+2); onset cluster br (+1) |
| 90 | braei | braeiw | braeiw | Braeiw | +3 | area-rule final (+2); onset cluster br (+1) |
| 91 | braei | braeih | braeih | Braeih | +3 | area-rule final (+2); onset cluster br (+1) |
| 92 | braei | braei | braei | Braei | +1 | onset cluster br (+1) |
| 93 | braeu | braeuf | braeuf | Braeuf | +3 | area-rule final (+2); onset cluster br (+1) |
| 94 | braeu | braeuw | braeuw | Braeuw | +3 | area-rule final (+2); onset cluster br (+1) |
| 95 | braeu | braeuh | braeuh | Braeuh | +3 | area-rule final (+2); onset cluster br (+1) |
| 96 | braeu | braeu | braeu | Braeu | +1 | onset cluster br (+1) |
| 97 | brai | braif | braif | Braif | +3 | area-rule final (+2); onset cluster br (+1) |
| 98 | brai | braiw | braiw | Braiw | +3 | area-rule final (+2); onset cluster br (+1) |
| 99 | brai | braih | braih | Braih | +3 | area-rule final (+2); onset cluster br (+1) |
| 100 | brai | brai | brai | Brai | +1 | onset cluster br (+1) |
| 101 | brau | brauf | brauf | Brauf | +3 | area-rule final (+2); onset cluster br (+1) |
| 102 | brau | brauw | brauw | Brauw | +3 | area-rule final (+2); onset cluster br (+1) |
| 103 | brau | brauh | brauh | Brauh | +3 | area-rule final (+2); onset cluster br (+1) |
| 104 | brau | brau | brau | Brau | +1 | onset cluster br (+1) |
| 105 | bre | bref | bref | Bref | +3 | area-rule final (+2); onset cluster br (+1) |
| 106 | bre | brew | brew | Brew | +1 | area-rule final (+2); onset cluster br (+1); IS an English word (-2) |
| 107 | bre | breh | breh | Breh | +3 | area-rule final (+2); onset cluster br (+1) |
| 108 | bre | bre | bre | Bre | +1 | onset cluster br (+1) |
| 109 | brei | breif | breif | Breif | +3 | area-rule final (+2); onset cluster br (+1) |
| 110 | brei | breiw | breiw | Breiw | +3 | area-rule final (+2); onset cluster br (+1) |
| 111 | brei | breih | breih | Breih | +3 | area-rule final (+2); onset cluster br (+1) |
| 112 | brei | brei | brei | Brei | -1 | onset cluster br (+1); IS an English word (-2) |
| 113 | breu | breuf | breuf | Breuf | +3 | area-rule final (+2); onset cluster br (+1) |
| 114 | breu | breuw | breuw | Breuw | +3 | area-rule final (+2); onset cluster br (+1) |
| 115 | breu | breuh | breuh | Breuh | +3 | area-rule final (+2); onset cluster br (+1) |
| 116 | breu | breu | breu | Breu | +1 | onset cluster br (+1) |
| 117 | bri | brif | brif | Brif | +3 | area-rule final (+2); onset cluster br (+1) |
| 118 | bri | briw | briw | Briw | +3 | area-rule final (+2); onset cluster br (+1) |
| 119 | bri | brih | brih | Brih | +3 | area-rule final (+2); onset cluster br (+1) |
| 120 | bri | bri | bri | Bri | +1 | onset cluster br (+1) |
| 121 | bro | brof | brof | Brof | +3 | area-rule final (+2); onset cluster br (+1) |
| 122 | bro | brow | brow | Brow | +1 | area-rule final (+2); onset cluster br (+1); IS an English word (-2) |
| 123 | bro | broh | broh | Broh | +3 | area-rule final (+2); onset cluster br (+1) |
| 124 | bro | bro | bro | Bro | +1 | onset cluster br (+1) |
| 125 | broi | broif | broif | Broif | +3 | area-rule final (+2); onset cluster br (+1) |
| 126 | broi | broiw | broiw | Broiw | +3 | area-rule final (+2); onset cluster br (+1) |
| 127 | broi | broih | broih | Broih | +3 | area-rule final (+2); onset cluster br (+1) |
| 128 | broi | broi | broi | Broi | +1 | onset cluster br (+1) |

## bases starting with `(none)`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 129 | aefmae | aefmaef | ae-fmaef | aeFmaef | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 130 | aefmae | aefmaew | ae-fmaew | aeFmaew | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 131 | aefmae | aefmaeh | ae-fmaeh | aeFmaeh | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 132 | aefmae | aefmae | ae-fmae | aeFmae | +2 | un-donated cluster fm (+2) |
| 133 | a | af | af | Af | +2 | area-rule final (+2) |
| 134 | a | aw | aw | Aw | +0 | area-rule final (+2); IS an English word (-2) |
| 135 | a | ah | ah | Ah | +0 | area-rule final (+2); IS an English word (-2) |
| 136 | a | a | a | A | +0 | - |

## bases starting with `b`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 137 | baefma | baefmaf | bae-fmaf | baeFmaf | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 138 | baefma | baefmaw | bae-fmaw | baeFmaw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 139 | baefma | baefmah | bae-fmah | baeFmah | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 140 | baefma | baefma | bae-fma | baeFma | +2 | un-donated cluster fm (+2) |
| 141 | ba | baf | baf | Baf | +2 | area-rule final (+2) |
| 142 | ba | baw | baw | Baw | +0 | area-rule final (+2); IS an English word (-2) |
| 143 | ba | bah | bah | Bah | +0 | area-rule final (+2); IS an English word (-2) |
| 144 | ba | ba | ba | Ba | -2 | IS an English word (-2) |

## bases starting with `br`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 145 | braefmae | braefmaef | brae-fmaef | braeFmaef | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 146 | braefmae | braefmaew | brae-fmaew | braeFmaew | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 147 | braefmae | braefmaeh | brae-fmaeh | braeFmaeh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 148 | braefmae | braefmae | brae-fmae | braeFmae | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 149 | bra | braf | braf | Braf | +3 | area-rule final (+2); onset cluster br (+1) |
| 150 | bra | braw | braw | Braw | +1 | area-rule final (+2); onset cluster br (+1); IS an English word (-2) |
| 151 | bra | brah | brah | Brah | +3 | area-rule final (+2); onset cluster br (+1) |
| 152 | bra | bra | bra | Bra | -1 | onset cluster br (+1); IS an English word (-2) |

## bases starting with `c`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 153 | caeifmo | caeifmof | caei-fmof | caeiFmof | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 154 | caeifmo | caeifmow | caei-fmow | caeiFmow | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 155 | caeifmo | caeifmoh | caei-fmoh | caeiFmoh | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 156 | caeifmo | caeifmo | caei-fmo | caeiFmo | +2 | un-donated cluster fm (+2) |
| 157 | ca | caf | caf | Caf | +2 | area-rule final (+2) |
| 158 | ca | caw | caw | Caw | +0 | area-rule final (+2); IS an English word (-2) |
| 159 | ca | cah | cah | Cah | +2 | area-rule final (+2) |
| 160 | ca | ca | ca | Ca | -2 | IS an English word (-2) |

## bases starting with `d`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 161 | daefmo | daefmof | dae-fmof | daeFmof | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 162 | daefmo | daefmow | dae-fmow | daeFmow | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 163 | daefmo | daefmoh | dae-fmoh | daeFmoh | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 164 | daefmo | daefmo | dae-fmo | daeFmo | +2 | un-donated cluster fm (+2) |
| 165 | da | daf | daf | Daf | +2 | area-rule final (+2) |
| 166 | da | daw | daw | Daw | +0 | area-rule final (+2); IS an English word (-2) |
| 167 | da | dah | dah | Dah | +0 | area-rule final (+2); IS an English word (-2) |
| 168 | da | da | da | Da | -2 | IS an English word (-2) |

## bases starting with `dr`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 169 | draefmae | draefmaef | drae-fmaef | draeFmaef | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster dr (+1) |
| 170 | draefmae | draefmaew | drae-fmaew | draeFmaew | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster dr (+1) |
| 171 | draefmae | draefmaeh | drae-fmaeh | draeFmaeh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster dr (+1) |
| 172 | draefmae | draefmae | drae-fmae | draeFmae | +3 | un-donated cluster fm (+2); onset cluster dr (+1) |
| 173 | dra | draf | draf | Draf | +3 | area-rule final (+2); onset cluster dr (+1) |
| 174 | dra | draw | draw | Draw | +1 | area-rule final (+2); onset cluster dr (+1); IS an English word (-2) |
| 175 | dra | drah | drah | Drah | +3 | area-rule final (+2); onset cluster dr (+1) |
| 176 | dra | dra | dra | Dra | +1 | onset cluster dr (+1) |

## bases starting with `f`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 177 | faefmei | faefmeif | fae-fmeif | faeFmeif | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 178 | faefmei | faefmeiw | fae-fmeiw | faeFmeiw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 179 | faefmei | faefmeih | fae-fmeih | faeFmeih | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 180 | faefmei | faefmei | fae-fmei | faeFmei | +2 | un-donated cluster fm (+2) |
| 181 | fa | faf | faf | Faf | +2 | area-rule final (+2) |
| 182 | fa | faw | faw | Faw | +2 | area-rule final (+2) |
| 183 | fa | fah | fah | Fah | +2 | area-rule final (+2) |
| 184 | fa | fa | fa | Fa | -2 | IS an English word (-2) |

## bases starting with `g`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 185 | gaefme | gaefmef | gae-fmef | gaeFmef | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 186 | gaefme | gaefmew | gae-fmew | gaeFmew | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 187 | gaefme | gaefmeh | gae-fmeh | gaeFmeh | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 188 | gaefme | gaefme | gae-fme | gaeFme | +2 | un-donated cluster fm (+2) |
| 189 | ga | gaf | gaf | Gaf | +2 | area-rule final (+2) |
| 190 | ga | gaw | gaw | Gaw | +0 | area-rule final (+2); IS an English word (-2) |
| 191 | ga | gah | gah | Gah | +2 | area-rule final (+2) |
| 192 | ga | ga | ga | Ga | -2 | IS an English word (-2) |

## bases starting with `gr`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 193 | graefmae | graefmaef | grae-fmaef | graeFmaef | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster gr (+1) |
| 194 | graefmae | graefmaew | grae-fmaew | graeFmaew | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster gr (+1) |
| 195 | graefmae | graefmaeh | grae-fmaeh | graeFmaeh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster gr (+1) |
| 196 | graefmae | graefmae | grae-fmae | graeFmae | +3 | un-donated cluster fm (+2); onset cluster gr (+1) |
| 197 | gra | graf | graf | Graf | +3 | area-rule final (+2); onset cluster gr (+1) |
| 198 | gra | graw | graw | Graw | +3 | area-rule final (+2); onset cluster gr (+1) |
| 199 | gra | grah | grah | Grah | +3 | area-rule final (+2); onset cluster gr (+1) |
| 200 | gra | gra | gra | Gra | -1 | onset cluster gr (+1); IS an English word (-2) |

## bases starting with `h`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 201 | haefmou | haefmouf | hae-fmouf | haeFmouf | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 202 | haefmou | haefmouw | hae-fmouw | haeFmouw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 203 | haefmou | haefmouh | hae-fmouh | haeFmouh | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 204 | haefmou | haefmou | hae-fmou | haeFmou | +2 | un-donated cluster fm (+2) |
| 205 | ha | haf | haf | Haf | +2 | area-rule final (+2) |
| 206 | ha | haw | haw | Haw | +0 | area-rule final (+2); IS an English word (-2) |
| 207 | ha | hah | hah | Hah | +0 | area-rule final (+2); IS an English word (-2) |
| 208 | ha | ha | ha | Ha | -2 | IS an English word (-2) |

## bases starting with `j`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 209 | jaefmaeu | jaefmaeuf | jae-fmaeuf | jaeFmaeuf | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 210 | jaefmaeu | jaefmaeuw | jae-fmaeuw | jaeFmaeuw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 211 | jaefmaeu | jaefmaeuh | jae-fmaeuh | jaeFmaeuh | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 212 | jaefmaeu | jaefmaeu | jae-fmaeu | jaeFmaeu | +2 | un-donated cluster fm (+2) |
| 213 | ja | jaf | jaf | Jaf | +2 | area-rule final (+2) |
| 214 | ja | jaw | jaw | Jaw | +0 | area-rule final (+2); IS an English word (-2) |
| 215 | ja | jah | jah | Jah | +2 | area-rule final (+2) |
| 216 | ja | ja | ja | Ja | +0 | - |

## bases starting with `l`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 217 | laefmy | laefmyf | lae-fmyf | laeFmyf | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 218 | laefmy | laefmyw | lae-fmyw | laeFmyw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 219 | laefmy | laefmyh | lae-fmyh | laeFmyh | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 220 | laefmy | laefmy | lae-fmy | laeFmy | +2 | un-donated cluster fm (+2) |
| 221 | la | laf | laf | Laf | +2 | area-rule final (+2) |
| 222 | la | law | law | Law | +0 | area-rule final (+2); IS an English word (-2) |
| 223 | la | lah | lah | Lah | +2 | area-rule final (+2) |
| 224 | la | la | la | La | -2 | IS an English word (-2) |

## bases starting with `m`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 225 | maefmu | maefmuf | mae-fmuf | maeFmuf | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 226 | maefmu | maefmuw | mae-fmuw | maeFmuw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 227 | maefmu | maefmuh | mae-fmuh | maeFmuh | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 228 | maefmu | maefmu | mae-fmu | maeFmu | +2 | un-donated cluster fm (+2) |
| 229 | ma | maf | maf | Maf | +2 | area-rule final (+2) |
| 230 | ma | maw | maw | Maw | +0 | area-rule final (+2); IS an English word (-2) |
| 231 | ma | mah | mah | Mah | +0 | area-rule final (+2); IS an English word (-2) |
| 232 | ma | ma | ma | Ma | -2 | IS an English word (-2) |

## bases starting with `n`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 233 | naefmi | naefmif | nae-fmif | naeFmif | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 234 | naefmi | naefmiw | nae-fmiw | naeFmiw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 235 | naefmi | naefmih | nae-fmih | naeFmih | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 236 | naefmi | naefmi | nae-fmi | naeFmi | +2 | un-donated cluster fm (+2) |
| 237 | na | naf | naf | Naf | +2 | area-rule final (+2) |
| 238 | na | naw | naw | Naw | +0 | area-rule final (+2); IS an English word (-2) |
| 239 | na | nah | nah | Nah | +2 | area-rule final (+2) |
| 240 | na | na | na | Na | -2 | IS an English word (-2) |

## bases starting with `r`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 241 | raefmai | raefmaif | rae-fmaif | raeFmaif | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 242 | raefmai | raefmaiw | rae-fmaiw | raeFmaiw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 243 | raefmai | raefmaih | rae-fmaih | raeFmaih | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 244 | raefmai | raefmai | rae-fmai | raeFmai | +2 | un-donated cluster fm (+2) |
| 245 | ra | raf | raf | Raf | +2 | area-rule final (+2) |
| 246 | ra | raw | raw | Raw | +0 | area-rule final (+2); IS an English word (-2) |
| 247 | ra | rah | rah | Rah | +0 | area-rule final (+2); IS an English word (-2) |
| 248 | ra | ra | ra | Ra | -2 | IS an English word (-2) |

## bases starting with `s`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 249 | saefmoi | saefmoif | sae-fmoif | saeFmoif | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 250 | saefmoi | saefmoiw | sae-fmoiw | saeFmoiw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 251 | saefmoi | saefmoih | sae-fmoih | saeFmoih | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 252 | saefmoi | saefmoi | sae-fmoi | saeFmoi | +2 | un-donated cluster fm (+2) |
| 253 | sa | saf | saf | Saf | +2 | area-rule final (+2) |
| 254 | sa | saw | saw | Saw | +0 | area-rule final (+2); IS an English word (-2) |
| 255 | sa | sah | sah | Sah | +0 | area-rule final (+2); IS an English word (-2) |
| 256 | sa | sa | sa | Sa | -2 | IS an English word (-2) |

## bases starting with `sh`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 257 | shaefmeu | shaefmeuf | shae-fmeuf | shaeFmeuf | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 258 | shaefmeu | shaefmeuw | shae-fmeuw | shaeFmeuw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 259 | shaefmeu | shaefmeuh | shae-fmeuh | shaeFmeuh | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 260 | shaefmeu | shaefmeu | shae-fmeu | shaeFmeu | +2 | un-donated cluster fm (+2) |
| 261 | sha | shaf | shaf | Shaf | +2 | area-rule final (+2) |
| 262 | sha | shaw | shaw | Shaw | +0 | area-rule final (+2); IS an English word (-2) |
| 263 | sha | shah | shah | Shah | +0 | area-rule final (+2); IS an English word (-2) |
| 264 | sha | sha | sha | Sha | -2 | IS an English word (-2) |

## bases starting with `th`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 265 | thaefmaei | thaefmaeif | thae-fmaeif | thaeFmaeif | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 266 | thaefmaei | thaefmaeiw | thae-fmaeiw | thaeFmaeiw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 267 | thaefmaei | thaefmaeih | thae-fmaeih | thaeFmaeih | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 268 | thaefmaei | thaefmaei | thae-fmaei | thaeFmaei | +2 | un-donated cluster fm (+2) |
| 269 | tha | thaf | thaf | Thaf | +2 | area-rule final (+2) |
| 270 | tha | thaw | thaw | Thaw | +0 | area-rule final (+2); IS an English word (-2) |
| 271 | tha | thah | thah | Thah | +2 | area-rule final (+2) |
| 272 | tha | tha | tha | Tha | -2 | IS an English word (-2) |

## bases starting with `w`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 273 | waefmau | waefmauf | wae-fmauf | waeFmauf | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 274 | waefmau | waefmauw | wae-fmauw | waeFmauw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 275 | waefmau | waefmauh | wae-fmauh | waeFmauh | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 276 | waefmau | waefmau | wae-fmau | waeFmau | +2 | un-donated cluster fm (+2) |
| 277 | wae | waef | waef | Waef | +2 | area-rule final (+2) |
| 278 | wae | waew | waew | Waew | +2 | area-rule final (+2) |
| 279 | wae | waeh | waeh | Waeh | +2 | area-rule final (+2) |
| 280 | wae | wae | wae | Wae | -2 | IS an English word (-2) |

## bases whose first vowel is `a`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 281 | brafma | brafmaf | bra-fmaf | braFmaf | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 282 | brafma | brafmaw | bra-fmaw | braFmaw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 283 | brafma | brafmah | bra-fmah | braFmah | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 284 | brafma | brafma | bra-fma | braFma | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 285 | bra | braf | braf | Braf | +3 | area-rule final (+2); onset cluster br (+1) |
| 286 | bra | braw | braw | Braw | +1 | area-rule final (+2); onset cluster br (+1); IS an English word (-2) |
| 287 | bra | brah | brah | Brah | +3 | area-rule final (+2); onset cluster br (+1) |
| 288 | bra | bra | bra | Bra | -1 | onset cluster br (+1); IS an English word (-2) |

## bases whose first vowel is `ae`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 289 | braefmae | braefmaef | brae-fmaef | braeFmaef | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 290 | braefmae | braefmaew | brae-fmaew | braeFmaew | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 291 | braefmae | braefmaeh | brae-fmaeh | braeFmaeh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 292 | braefmae | braefmae | brae-fmae | braeFmae | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 293 | brae | braef | braef | Braef | +3 | area-rule final (+2); onset cluster br (+1) |
| 294 | brae | braew | braew | Braew | +3 | area-rule final (+2); onset cluster br (+1) |
| 295 | brae | braeh | braeh | Braeh | +3 | area-rule final (+2); onset cluster br (+1) |
| 296 | brae | brae | brae | Brae | -1 | onset cluster br (+1); IS an English word (-2) |

## bases whose first vowel is `aei`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 297 | braeifmaei | braeifmaeif | braei-fmaeif | braeiFmaeif | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 298 | braeifmaei | braeifmaeiw | braei-fmaeiw | braeiFmaeiw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 299 | braeifmaei | braeifmaeih | braei-fmaeih | braeiFmaeih | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 300 | braeifmaei | braeifmaei | braei-fmaei | braeiFmaei | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 301 | braei | braeif | braeif | Braeif | +3 | area-rule final (+2); onset cluster br (+1) |
| 302 | braei | braeiw | braeiw | Braeiw | +3 | area-rule final (+2); onset cluster br (+1) |
| 303 | braei | braeih | braeih | Braeih | +3 | area-rule final (+2); onset cluster br (+1) |
| 304 | braei | braei | braei | Braei | +1 | onset cluster br (+1) |

## bases whose first vowel is `aeu`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 305 | braeufmaeu | braeufmaeuf | braeu-fmaeuf | braeuFmaeuf | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 306 | braeufmaeu | braeufmaeuw | braeu-fmaeuw | braeuFmaeuw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 307 | braeufmaeu | braeufmaeuh | braeu-fmaeuh | braeuFmaeuh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 308 | braeufmaeu | braeufmaeu | braeu-fmaeu | braeuFmaeu | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 309 | braeu | braeuf | braeuf | Braeuf | +3 | area-rule final (+2); onset cluster br (+1) |
| 310 | braeu | braeuw | braeuw | Braeuw | +3 | area-rule final (+2); onset cluster br (+1) |
| 311 | braeu | braeuh | braeuh | Braeuh | +3 | area-rule final (+2); onset cluster br (+1) |
| 312 | braeu | braeu | braeu | Braeu | +1 | onset cluster br (+1) |

## bases whose first vowel is `ai`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 313 | braifmai | braifmaif | brai-fmaif | braiFmaif | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 314 | braifmai | braifmaiw | brai-fmaiw | braiFmaiw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 315 | braifmai | braifmaih | brai-fmaih | braiFmaih | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 316 | braifmai | braifmai | brai-fmai | braiFmai | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 317 | brai | braif | braif | Braif | +3 | area-rule final (+2); onset cluster br (+1) |
| 318 | brai | braiw | braiw | Braiw | +3 | area-rule final (+2); onset cluster br (+1) |
| 319 | brai | braih | braih | Braih | +3 | area-rule final (+2); onset cluster br (+1) |
| 320 | brai | brai | brai | Brai | +1 | onset cluster br (+1) |

## bases whose first vowel is `au`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 321 | braufmau | braufmauf | brau-fmauf | brauFmauf | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 322 | braufmau | braufmauw | brau-fmauw | brauFmauw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 323 | braufmau | braufmauh | brau-fmauh | brauFmauh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 324 | braufmau | braufmau | brau-fmau | brauFmau | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 325 | brau | brauf | brauf | Brauf | +3 | area-rule final (+2); onset cluster br (+1) |
| 326 | brau | brauw | brauw | Brauw | +3 | area-rule final (+2); onset cluster br (+1) |
| 327 | brau | brauh | brauh | Brauh | +3 | area-rule final (+2); onset cluster br (+1) |
| 328 | brau | brau | brau | Brau | +1 | onset cluster br (+1) |

## bases whose first vowel is `e`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 329 | brefme | brefmef | bre-fmef | breFmef | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 330 | brefme | brefmew | bre-fmew | breFmew | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 331 | brefme | brefmeh | bre-fmeh | breFmeh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 332 | brefme | brefme | bre-fme | breFme | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 333 | bre | bref | bref | Bref | +3 | area-rule final (+2); onset cluster br (+1) |
| 334 | bre | brew | brew | Brew | +1 | area-rule final (+2); onset cluster br (+1); IS an English word (-2) |
| 335 | bre | breh | breh | Breh | +3 | area-rule final (+2); onset cluster br (+1) |
| 336 | bre | bre | bre | Bre | +1 | onset cluster br (+1) |

## bases whose first vowel is `ei`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 337 | breifmei | breifmeif | brei-fmeif | breiFmeif | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 338 | breifmei | breifmeiw | brei-fmeiw | breiFmeiw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 339 | breifmei | breifmeih | brei-fmeih | breiFmeih | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 340 | breifmei | breifmei | brei-fmei | breiFmei | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 341 | brei | breif | breif | Breif | +3 | area-rule final (+2); onset cluster br (+1) |
| 342 | brei | breiw | breiw | Breiw | +3 | area-rule final (+2); onset cluster br (+1) |
| 343 | brei | breih | breih | Breih | +3 | area-rule final (+2); onset cluster br (+1) |
| 344 | brei | brei | brei | Brei | -1 | onset cluster br (+1); IS an English word (-2) |

## bases whose first vowel is `eu`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 345 | breufmeu | breufmeuf | breu-fmeuf | breuFmeuf | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 346 | breufmeu | breufmeuw | breu-fmeuw | breuFmeuw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 347 | breufmeu | breufmeuh | breu-fmeuh | breuFmeuh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 348 | breufmeu | breufmeu | breu-fmeu | breuFmeu | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 349 | breu | breuf | breuf | Breuf | +3 | area-rule final (+2); onset cluster br (+1) |
| 350 | breu | breuw | breuw | Breuw | +3 | area-rule final (+2); onset cluster br (+1) |
| 351 | breu | breuh | breuh | Breuh | +3 | area-rule final (+2); onset cluster br (+1) |
| 352 | breu | breu | breu | Breu | +1 | onset cluster br (+1) |

## bases whose first vowel is `i`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 353 | brifmi | brifmif | bri-fmif | briFmif | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 354 | brifmi | brifmiw | bri-fmiw | briFmiw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 355 | brifmi | brifmih | bri-fmih | briFmih | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 356 | brifmi | brifmi | bri-fmi | briFmi | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 357 | bri | brif | brif | Brif | +3 | area-rule final (+2); onset cluster br (+1) |
| 358 | bri | briw | briw | Briw | +3 | area-rule final (+2); onset cluster br (+1) |
| 359 | bri | brih | brih | Brih | +3 | area-rule final (+2); onset cluster br (+1) |
| 360 | bri | bri | bri | Bri | +1 | onset cluster br (+1) |

## bases whose first vowel is `o`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 361 | brofmo | brofmof | bro-fmof | broFmof | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 362 | brofmo | brofmow | bro-fmow | broFmow | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 363 | brofmo | brofmoh | bro-fmoh | broFmoh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 364 | brofmo | brofmo | bro-fmo | broFmo | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 365 | bro | brof | brof | Brof | +3 | area-rule final (+2); onset cluster br (+1) |
| 366 | bro | brow | brow | Brow | +1 | area-rule final (+2); onset cluster br (+1); IS an English word (-2) |
| 367 | bro | broh | broh | Broh | +3 | area-rule final (+2); onset cluster br (+1) |
| 368 | bro | bro | bro | Bro | +1 | onset cluster br (+1) |

## bases whose first vowel is `oi`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 369 | broifmoi | broifmoif | broi-fmoif | broiFmoif | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 370 | broifmoi | broifmoiw | broi-fmoiw | broiFmoiw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 371 | broifmoi | broifmoih | broi-fmoih | broiFmoih | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 372 | broifmoi | broifmoi | broi-fmoi | broiFmoi | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 373 | broi | broif | broif | Broif | +3 | area-rule final (+2); onset cluster br (+1) |
| 374 | broi | broiw | broiw | Broiw | +3 | area-rule final (+2); onset cluster br (+1) |
| 375 | broi | broih | broih | Broih | +3 | area-rule final (+2); onset cluster br (+1) |
| 376 | broi | broi | broi | Broi | +1 | onset cluster br (+1) |

## bases whose first vowel is `ou`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 377 | broufmou | broufmouf | brou-fmouf | brouFmouf | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 378 | broufmou | broufmouw | brou-fmouw | brouFmouw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 379 | broufmou | broufmouh | brou-fmouh | brouFmouh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 380 | broufmou | broufmou | brou-fmou | brouFmou | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 381 | brou | brouf | brouf | Brouf | +3 | area-rule final (+2); onset cluster br (+1) |
| 382 | brou | brouw | brouw | Brouw | +3 | area-rule final (+2); onset cluster br (+1) |
| 383 | brou | brouh | brouh | Brouh | +3 | area-rule final (+2); onset cluster br (+1) |
| 384 | brou | brou | brou | Brou | +1 | onset cluster br (+1) |

## bases whose first vowel is `u`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 385 | brufmu | brufmuf | bru-fmuf | bruFmuf | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 386 | brufmu | brufmuw | bru-fmuw | bruFmuw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 387 | brufmu | brufmuh | bru-fmuh | bruFmuh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 388 | brufmu | brufmu | bru-fmu | bruFmu | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 389 | bru | bruf | bruf | Bruf | +3 | area-rule final (+2); onset cluster br (+1) |
| 390 | bru | bruw | bruw | Bruw | +3 | area-rule final (+2); onset cluster br (+1) |
| 391 | bru | bruh | bruh | Bruh | +3 | area-rule final (+2); onset cluster br (+1) |
| 392 | bru | bru | bru | Bru | +1 | onset cluster br (+1) |

## bases whose first vowel is `y`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 393 | bryfmy | bryfmyf | bry-fmyf | bryFmyf | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 394 | bryfmy | bryfmyw | bry-fmyw | bryFmyw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 395 | bryfmy | bryfmyh | bry-fmyh | bryFmyh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 396 | bryfmy | bryfmy | bry-fmy | bryFmy | +3 | un-donated cluster fm (+2); onset cluster br (+1) |
| 397 | bry | bryf | bryf | Bryf | +3 | area-rule final (+2); onset cluster br (+1) |
| 398 | bry | bryw | bryw | Bryw | +3 | area-rule final (+2); onset cluster br (+1) |
| 399 | bry | bryh | bryh | Bryh | +3 | area-rule final (+2); onset cluster br (+1) |
| 400 | bry | bry | bry | Bry | +1 | onset cluster br (+1) |

## English collisions (measured - avoid or accept knowingly)

338 forms are literally in `/usr/share/dict/words`, so a pick can never hit one by accident:

```
aw ah aba age agrah agra aly ammi ani anta arrau aru ae ai aire auh baw bah ba bago balai bari barny bae be bedew belga bema bilgy bilo birdy bow bo bodo boga bony bouw bounce bu bufo buna by byre braw bra brahma branny branta brassy brae brew brei bribri brow brolga broma caw ca caltha carry carse ce cow coca cothy coif courge cumshaw daw dah da dado dali dae daira dauw dew de desma di dine dow do dome dori dure draw draba drew drow dry eh edo elbow eli eu fa fanwe farsi fae few fe feif fei feu fi fishy fow fo follow fou fu gaw ga gade galga gary gau ge genu geisha gif gi go gossy goi gula gra grampa granny grassy graeme grew grebe grigri grow grouf grugru haw hah ha hance hange hau hew he hei hi hithe how ho hohe holly horse hoi houri huh hu hurrah hy if impi inro jaw jef jew ji jow jo ju law la lady lai lew lemna lennow leif lei leu lif li lide lima lof low lo logy lou louse lu lube ludo lummy ly maw mah ma mabi male
```

(... and 138 more; raise --max-en)


---

## What the menu does NOT do

- It cannot tell you what sounds *beautiful* - that is the part only you can supply.
- It contains **no 1-syllable (`roi`-class) root**: the pool is the 2-syllable core
  (`../decision/03-open-questions.md` section 0 item 22). Wanting short roots in this round means
  extending that pool FIRST - which changes the numbering here.
- It does not test the **M3a seam** (root-final `f`/`w`/`h` + a case suffix, always unstressed) -
  still unjudged (section 0 item 20), and it fires for 3 of every 4 coined roots.
