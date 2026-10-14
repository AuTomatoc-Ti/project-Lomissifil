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

## bases starting with `(none)`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 81 | aefmae | aefmaef | ae-fmaef | aeFmaef | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 82 | aefmae | aefmaew | ae-fmaew | aeFmaew | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 83 | aefmae | aefmaeh | ae-fmaeh | aeFmaeh | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 84 | aefmae | aefmae | ae-fmae | aeFmae | +2 | un-donated cluster fm (+2) |

## bases starting with `b`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 85 | baefma | baefmaf | bae-fmaf | baeFmaf | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 86 | baefma | baefmaw | bae-fmaw | baeFmaw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 87 | baefma | baefmah | bae-fmah | baeFmah | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 88 | baefma | baefma | bae-fma | baeFma | +2 | un-donated cluster fm (+2) |

## bases starting with `br`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 89 | braefmae | braefmaef | brae-fmaef | braeFmaef | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 90 | braefmae | braefmaew | brae-fmaew | braeFmaew | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 91 | braefmae | braefmaeh | brae-fmaeh | braeFmaeh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 92 | braefmae | braefmae | brae-fmae | braeFmae | +3 | un-donated cluster fm (+2); onset cluster br (+1) |

## bases starting with `c`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 93 | caeifmo | caeifmof | caei-fmof | caeiFmof | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 94 | caeifmo | caeifmow | caei-fmow | caeiFmow | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 95 | caeifmo | caeifmoh | caei-fmoh | caeiFmoh | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 96 | caeifmo | caeifmo | caei-fmo | caeiFmo | +2 | un-donated cluster fm (+2) |

## bases starting with `d`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 97 | daefmo | daefmof | dae-fmof | daeFmof | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 98 | daefmo | daefmow | dae-fmow | daeFmow | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 99 | daefmo | daefmoh | dae-fmoh | daeFmoh | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 100 | daefmo | daefmo | dae-fmo | daeFmo | +2 | un-donated cluster fm (+2) |

## bases starting with `dr`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 101 | draefmae | draefmaef | drae-fmaef | draeFmaef | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster dr (+1) |
| 102 | draefmae | draefmaew | drae-fmaew | draeFmaew | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster dr (+1) |
| 103 | draefmae | draefmaeh | drae-fmaeh | draeFmaeh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster dr (+1) |
| 104 | draefmae | draefmae | drae-fmae | draeFmae | +3 | un-donated cluster fm (+2); onset cluster dr (+1) |

## bases starting with `f`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 105 | faefmei | faefmeif | fae-fmeif | faeFmeif | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 106 | faefmei | faefmeiw | fae-fmeiw | faeFmeiw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 107 | faefmei | faefmeih | fae-fmeih | faeFmeih | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 108 | faefmei | faefmei | fae-fmei | faeFmei | +2 | un-donated cluster fm (+2) |

## bases starting with `g`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 109 | gaefme | gaefmef | gae-fmef | gaeFmef | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 110 | gaefme | gaefmew | gae-fmew | gaeFmew | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 111 | gaefme | gaefmeh | gae-fmeh | gaeFmeh | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 112 | gaefme | gaefme | gae-fme | gaeFme | +2 | un-donated cluster fm (+2) |

## bases starting with `gr`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 113 | graefmae | graefmaef | grae-fmaef | graeFmaef | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster gr (+1) |
| 114 | graefmae | graefmaew | grae-fmaew | graeFmaew | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster gr (+1) |
| 115 | graefmae | graefmaeh | grae-fmaeh | graeFmaeh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster gr (+1) |
| 116 | graefmae | graefmae | grae-fmae | graeFmae | +3 | un-donated cluster fm (+2); onset cluster gr (+1) |

## bases starting with `h`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 117 | haefmou | haefmouf | hae-fmouf | haeFmouf | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 118 | haefmou | haefmouw | hae-fmouw | haeFmouw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 119 | haefmou | haefmouh | hae-fmouh | haeFmouh | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 120 | haefmou | haefmou | hae-fmou | haeFmou | +2 | un-donated cluster fm (+2) |

## bases starting with `j`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 121 | jaefmaeu | jaefmaeuf | jae-fmaeuf | jaeFmaeuf | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 122 | jaefmaeu | jaefmaeuw | jae-fmaeuw | jaeFmaeuw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 123 | jaefmaeu | jaefmaeuh | jae-fmaeuh | jaeFmaeuh | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 124 | jaefmaeu | jaefmaeu | jae-fmaeu | jaeFmaeu | +2 | un-donated cluster fm (+2) |

## bases starting with `l`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 125 | laefmy | laefmyf | lae-fmyf | laeFmyf | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 126 | laefmy | laefmyw | lae-fmyw | laeFmyw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 127 | laefmy | laefmyh | lae-fmyh | laeFmyh | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 128 | laefmy | laefmy | lae-fmy | laeFmy | +2 | un-donated cluster fm (+2) |

## bases starting with `m`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 129 | maefmu | maefmuf | mae-fmuf | maeFmuf | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 130 | maefmu | maefmuw | mae-fmuw | maeFmuw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 131 | maefmu | maefmuh | mae-fmuh | maeFmuh | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 132 | maefmu | maefmu | mae-fmu | maeFmu | +2 | un-donated cluster fm (+2) |

## bases starting with `n`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 133 | naefmi | naefmif | nae-fmif | naeFmif | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 134 | naefmi | naefmiw | nae-fmiw | naeFmiw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 135 | naefmi | naefmih | nae-fmih | naeFmih | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 136 | naefmi | naefmi | nae-fmi | naeFmi | +2 | un-donated cluster fm (+2) |

## bases starting with `r`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 137 | raefmai | raefmaif | rae-fmaif | raeFmaif | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 138 | raefmai | raefmaiw | rae-fmaiw | raeFmaiw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 139 | raefmai | raefmaih | rae-fmaih | raeFmaih | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 140 | raefmai | raefmai | rae-fmai | raeFmai | +2 | un-donated cluster fm (+2) |

## bases starting with `s`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 141 | saefmoi | saefmoif | sae-fmoif | saeFmoif | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 142 | saefmoi | saefmoiw | sae-fmoiw | saeFmoiw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 143 | saefmoi | saefmoih | sae-fmoih | saeFmoih | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 144 | saefmoi | saefmoi | sae-fmoi | saeFmoi | +2 | un-donated cluster fm (+2) |

## bases starting with `sh`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 145 | shaefmeu | shaefmeuf | shae-fmeuf | shaeFmeuf | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 146 | shaefmeu | shaefmeuw | shae-fmeuw | shaeFmeuw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 147 | shaefmeu | shaefmeuh | shae-fmeuh | shaeFmeuh | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 148 | shaefmeu | shaefmeu | shae-fmeu | shaeFmeu | +2 | un-donated cluster fm (+2) |

## bases starting with `th`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 149 | thaefmaei | thaefmaeif | thae-fmaeif | thaeFmaeif | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 150 | thaefmaei | thaefmaeiw | thae-fmaeiw | thaeFmaeiw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 151 | thaefmaei | thaefmaeih | thae-fmaeih | thaeFmaeih | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 152 | thaefmaei | thaefmaei | thae-fmaei | thaeFmaei | +2 | un-donated cluster fm (+2) |

## bases starting with `w`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 153 | waefmau | waefmauf | wae-fmauf | waeFmauf | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 154 | waefmau | waefmauw | wae-fmauw | waeFmauw | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 155 | waefmau | waefmauh | wae-fmauh | waeFmauh | +4 | area-rule final (+2); un-donated cluster fm (+2) |
| 156 | waefmau | waefmau | wae-fmau | waeFmau | +2 | un-donated cluster fm (+2) |

## bases whose first vowel is `a`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 157 | brafma | brafmaf | bra-fmaf | braFmaf | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 158 | brafma | brafmaw | bra-fmaw | braFmaw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 159 | brafma | brafmah | bra-fmah | braFmah | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 160 | brafma | brafma | bra-fma | braFma | +3 | un-donated cluster fm (+2); onset cluster br (+1) |

## bases whose first vowel is `ae`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 161 | braefmae | braefmaef | brae-fmaef | braeFmaef | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 162 | braefmae | braefmaew | brae-fmaew | braeFmaew | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 163 | braefmae | braefmaeh | brae-fmaeh | braeFmaeh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 164 | braefmae | braefmae | brae-fmae | braeFmae | +3 | un-donated cluster fm (+2); onset cluster br (+1) |

## bases whose first vowel is `aei`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 165 | braeifmaei | braeifmaeif | braei-fmaeif | braeiFmaeif | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 166 | braeifmaei | braeifmaeiw | braei-fmaeiw | braeiFmaeiw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 167 | braeifmaei | braeifmaeih | braei-fmaeih | braeiFmaeih | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 168 | braeifmaei | braeifmaei | braei-fmaei | braeiFmaei | +3 | un-donated cluster fm (+2); onset cluster br (+1) |

## bases whose first vowel is `aeu`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 169 | braeufmaeu | braeufmaeuf | braeu-fmaeuf | braeuFmaeuf | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 170 | braeufmaeu | braeufmaeuw | braeu-fmaeuw | braeuFmaeuw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 171 | braeufmaeu | braeufmaeuh | braeu-fmaeuh | braeuFmaeuh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 172 | braeufmaeu | braeufmaeu | braeu-fmaeu | braeuFmaeu | +3 | un-donated cluster fm (+2); onset cluster br (+1) |

## bases whose first vowel is `ai`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 173 | braifmai | braifmaif | brai-fmaif | braiFmaif | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 174 | braifmai | braifmaiw | brai-fmaiw | braiFmaiw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 175 | braifmai | braifmaih | brai-fmaih | braiFmaih | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 176 | braifmai | braifmai | brai-fmai | braiFmai | +3 | un-donated cluster fm (+2); onset cluster br (+1) |

## bases whose first vowel is `au`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 177 | braufmau | braufmauf | brau-fmauf | brauFmauf | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 178 | braufmau | braufmauw | brau-fmauw | brauFmauw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 179 | braufmau | braufmauh | brau-fmauh | brauFmauh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 180 | braufmau | braufmau | brau-fmau | brauFmau | +3 | un-donated cluster fm (+2); onset cluster br (+1) |

## bases whose first vowel is `e`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 181 | brefme | brefmef | bre-fmef | breFmef | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 182 | brefme | brefmew | bre-fmew | breFmew | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 183 | brefme | brefmeh | bre-fmeh | breFmeh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 184 | brefme | brefme | bre-fme | breFme | +3 | un-donated cluster fm (+2); onset cluster br (+1) |

## bases whose first vowel is `ei`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 185 | breifmei | breifmeif | brei-fmeif | breiFmeif | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 186 | breifmei | breifmeiw | brei-fmeiw | breiFmeiw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 187 | breifmei | breifmeih | brei-fmeih | breiFmeih | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 188 | breifmei | breifmei | brei-fmei | breiFmei | +3 | un-donated cluster fm (+2); onset cluster br (+1) |

## bases whose first vowel is `eu`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 189 | breufmeu | breufmeuf | breu-fmeuf | breuFmeuf | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 190 | breufmeu | breufmeuw | breu-fmeuw | breuFmeuw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 191 | breufmeu | breufmeuh | breu-fmeuh | breuFmeuh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 192 | breufmeu | breufmeu | breu-fmeu | breuFmeu | +3 | un-donated cluster fm (+2); onset cluster br (+1) |

## bases whose first vowel is `i`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 193 | brifmi | brifmif | bri-fmif | briFmif | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 194 | brifmi | brifmiw | bri-fmiw | briFmiw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 195 | brifmi | brifmih | bri-fmih | briFmih | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 196 | brifmi | brifmi | bri-fmi | briFmi | +3 | un-donated cluster fm (+2); onset cluster br (+1) |

## bases whose first vowel is `o`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 197 | brofmo | brofmof | bro-fmof | broFmof | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 198 | brofmo | brofmow | bro-fmow | broFmow | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 199 | brofmo | brofmoh | bro-fmoh | broFmoh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 200 | brofmo | brofmo | bro-fmo | broFmo | +3 | un-donated cluster fm (+2); onset cluster br (+1) |

## bases whose first vowel is `oi`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 201 | broifmoi | broifmoif | broi-fmoif | broiFmoif | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 202 | broifmoi | broifmoiw | broi-fmoiw | broiFmoiw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 203 | broifmoi | broifmoih | broi-fmoih | broiFmoih | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 204 | broifmoi | broifmoi | broi-fmoi | broiFmoi | +3 | un-donated cluster fm (+2); onset cluster br (+1) |

## bases whose first vowel is `ou`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 205 | broufmou | broufmouf | brou-fmouf | brouFmouf | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 206 | broufmou | broufmouw | brou-fmouw | brouFmouw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 207 | broufmou | broufmouh | brou-fmouh | brouFmouh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 208 | broufmou | broufmou | brou-fmou | brouFmou | +3 | un-donated cluster fm (+2); onset cluster br (+1) |

## bases whose first vowel is `u`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 209 | brufmu | brufmuf | bru-fmuf | bruFmuf | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 210 | brufmu | brufmuw | bru-fmuw | bruFmuw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 211 | brufmu | brufmuh | bru-fmuh | bruFmuh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 212 | brufmu | brufmu | bru-fmu | bruFmu | +3 | un-donated cluster fm (+2); onset cluster br (+1) |

## bases whose first vowel is `y`

| # | base | form | syllables | stress | score | why |
|---|---|---|---|---|---|---|
| 213 | bryfmy | bryfmyf | bry-fmyf | bryFmyf | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 214 | bryfmy | bryfmyw | bry-fmyw | bryFmyw | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 215 | bryfmy | bryfmyh | bry-fmyh | bryFmyh | +5 | area-rule final (+2); un-donated cluster fm (+2); onset cluster br (+1) |
| 216 | bryfmy | bryfmy | bry-fmy | bryFmy | +3 | un-donated cluster fm (+2); onset cluster br (+1) |

## English collisions (measured - avoid or accept knowingly)

143 forms are literally in `/usr/share/dict/words`, so a pick can never hit one by accident:

```
aba age agrah agra aly ammi ani anta arrau aru aire bago balai bari barny bedew belga bema bilgy bilo birdy bodo boga bony bounce bufo buna byre brahma branny branta brassy bribri brolga broma caltha carry carse coca cothy courge cumshaw dado dali daira desma dine dome dori dure draba edo elbow eli fanwe farsi fishy follow gade galga gary genu geisha gossy gula grampa granny grassy graeme grebe grigri grugru hance hange hithe hohe holly horse houri hurrah impi inro lady lemna lennow lide lima logy louse lube ludo lummy mabi male mamma mana marae marla masse mainly mela merle mero minny missy mono more nabu none nuba nummi ode olga only onto ory rane ranty renne ribe rompu rude salle sella sensa serra silly songy shallow shice shilha thalli thewy theurgy thonga udi unlaw ura washo wese wince withy woibe
```


---

## What the menu does NOT do

- It cannot tell you what sounds *beautiful* - that is the part only you can supply.
- It contains **no 1-syllable (`roi`-class) root**: the pool is the 2-syllable core
  (`../decision/03-open-questions.md` section 0 item 22). Wanting short roots in this round means
  extending that pool FIRST - which changes the numbering here.
- It does not test the **M3a seam** (root-final `f`/`w`/`h` + a case suffix, always unstressed) -
  still unjudged (section 0 item 20), and it fires for 3 of every 4 coined roots.
