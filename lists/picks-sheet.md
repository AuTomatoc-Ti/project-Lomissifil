# lists/picks-sheet.md - GENERATED audition sheet. DO NOT ANNOTATE HERE.

Regenerate with:

```
python3 tools/syllabify.py --sheet > lists/picks-sheet.md
```

Any annotation written in this file is **lost** on regeneration. **Picks go in `lists/picks.md`.**
The row numbers are the same as `../audio/roots-index.txt` (same seed, same sample), so a pick can
be recorded as a number in either file.

## How to read a row

| column | meaning |
|---|---|
| `form` | the citation form, plain lowercase (P4: the dictionary form is unstressed) |
| `syllables` | the syllable split, `-` between syllables |
| `stress` | where the **default** stress falls (P4/N1): 2nd syllable of the root, CAPITAL on the first letter of that syllable |

Reading it aloud needs no engine and no IPA - only these letter values:

`a` = the dark open vowel of *father* · `ae` = the bright vowel of *cat* · `e` = close-mid front ·
`o` = close-mid back · `i` = /i/ · `u` = /u/ · `y` = French *u* / German *ue* ·
`w` = /v/ · `sh` = the *sh* of *ship* · `th` = the *th* of *thin* · `c` = the *ch* of *church* ·
`j` = the *y* of *yes* · `r` = a single tap · a doubled letter (`ss nn ll mm rr ww`) = a long sound ·
a diphthong (`ai au ei eu oi ou aei aeu`) is ONE syllable, a hiatus (`iu yu ia ya`) is TWO.

## Rules for the pick (R1/R3)

Every group of 4 rows is ONE base: `+f` | `+w` (= /v/) | `+h` | bare. A base yields **exactly 2**
roots, so pick **at most one** from the `{+f, +w}` pair and **at most one** from the
`{+h, bare}` pair.

> Sound-only. R3 is PARKED, so assign **no meanings** (decision/03-open-questions.md section 0
> item 14). A pick is not a word; `../reference/example.md` stays the only source for examples.

## Reading rule (P6) - and the one flag left

**`sh` and `ng` are ALWAYS one phoneme** (`sh` = the *sh* of *ship*, `ng` = the *ng* of *sing*) - that
is `P6`, ruled 2026-10-14. So a row containing `ng` never means "n then g": the sequence **coda `n` +
/g/** is written **`nk`** instead, and nothing below needs a guess.

The one flag left is **`stress capital lands on a DIGRAPH`**: the stressed syllable starts with
`sh` / `th` / `ng` / `ae` - one sound written with two letters - and N1 has no rule for that case yet
(it is an open item). The `stress` column capitalises the first letter; treat it as provisional.

Also: `stress` is only the DEFAULT (P4). A composer may overwrite it in notation - that is
performance, not a different word.

---

Source: `lists/roots-bases-current.txt` (26751 packed bases); sample 48 bases, seed 20261014 - the SAME sample as
`../audio/roots-index.txt`.

## roots-01.wav  (numbered 1-32)

| # | base | form | syllables | stress (P4/N1) | note |
|---|---|---|---|---|---|
| 1 | thastho | thasthof | thas-thof | thasThof | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 2 | thastho | thasthow | thas-thow | thasThow | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 3 | thastho | thasthoh | thas-thoh | thasThoh | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 4 | thastho | thastho | thas-tho | thasTho | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 5 | namgae | namgaef | nam-gaef | namGaef |  |
| 6 | namgae | namgaew | nam-gaew | namGaew |  |
| 7 | namgae | namgaeh | nam-gaeh | namGaeh |  |
| 8 | namgae | namgae | nam-gae | namGae |  |
| 9 | dobrae | dobraef | do-braef | doBraef |  |
| 10 | dobrae | dobraew | do-braew | doBraew |  |
| 11 | dobrae | dobraeh | do-braeh | doBraeh |  |
| 12 | dobrae | dobrae | do-brae | doBrae |  |
| 13 | sumtho | sumthof | sum-thof | sumThof | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 14 | sumtho | sumthow | sum-thow | sumThow | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 15 | sumtho | sumthoh | sum-thoh | sumThoh | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 16 | sumtho | sumtho | sum-tho | sumTho | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 17 | ujmu | ujmuf | u-jmuf | uJmuf |  |
| 18 | ujmu | ujmuw | u-jmuw | uJmuw |  |
| 19 | ujmu | ujmuh | u-jmuh | uJmuh |  |
| 20 | ujmu | ujmu | u-jmu | uJmu |  |
| 21 | daehno | daehnof | dae-hnof | daeHnof |  |
| 22 | daehno | daehnow | dae-hnow | daeHnow |  |
| 23 | daehno | daehnoh | dae-hnoh | daeHnoh |  |
| 24 | daehno | daehno | dae-hno | daeHno |  |
| 25 | woursaeu | woursaeuf | wour-saeuf | wourSaeuf |  |
| 26 | woursaeu | woursaeuw | wour-saeuw | wourSaeuw |  |
| 27 | woursaeu | woursaeuh | wour-saeuh | wourSaeuh |  |
| 28 | woursaeu | woursaeu | wour-saeu | wourSaeu |  |
| 29 | leubraei | leubraeif | leu-braeif | leuBraeif |  |
| 30 | leubraei | leubraeiw | leu-braeiw | leuBraeiw |  |
| 31 | leubraei | leubraeih | leu-braeih | leuBraeih |  |
| 32 | leubraei | leubraei | leu-braei | leuBraei |  |

## roots-02.wav  (numbered 33-64)

| # | base | form | syllables | stress (P4/N1) | note |
|---|---|---|---|---|---|
| 33 | oillo | oillof | oil-lof | oilLof |  |
| 34 | oillo | oillow | oil-low | oilLow |  |
| 35 | oillo | oilloh | oil-loh | oilLoh |  |
| 36 | oillo | oillo | oil-lo | oilLo |  |
| 37 | maeijnei | maeijneif | maei-jneif | maeiJneif |  |
| 38 | maeijnei | maeijneiw | maei-jneiw | maeiJneiw |  |
| 39 | maeijnei | maeijneih | maei-jneih | maeiJneih |  |
| 40 | maeijnei | maeijnei | maei-jnei | maeiJnei |  |
| 41 | graemdae | graemdaef | graem-daef | graemDaef |  |
| 42 | graemdae | graemdaew | graem-daew | graemDaew |  |
| 43 | graemdae | graemdaeh | graem-daeh | graemDaeh |  |
| 44 | graemdae | graemdae | graem-dae | graemDae |  |
| 45 | rouswaei | rouswaeif | rous-waeif | rousWaeif |  |
| 46 | rouswaei | rouswaeiw | rous-waeiw | rousWaeiw |  |
| 47 | rouswaei | rouswaeih | rous-waeih | rousWaeih |  |
| 48 | rouswaei | rouswaei | rous-waei | rousWaei |  |
| 49 | grortheu | grortheuf | gror-theuf | grorTheuf | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 50 | grortheu | grortheuw | gror-theuw | grorTheuw | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 51 | grortheu | grortheuh | gror-theuh | grorTheuh | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 52 | grortheu | grortheu | gror-theu | grorTheu | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 53 | goumneu | goumneuf | goum-neuf | goumNeuf |  |
| 54 | goumneu | goumneuw | goum-neuw | goumNeuw |  |
| 55 | goumneu | goumneuh | goum-neuh | goumNeuh |  |
| 56 | goumneu | goumneu | goum-neu | goumNeu |  |
| 57 | meuneu | meuneuf | meu-neuf | meuNeuf |  |
| 58 | meuneu | meuneuw | meu-neuw | meuNeuw |  |
| 59 | meuneu | meuneuh | meu-neuh | meuNeuh |  |
| 60 | meuneu | meuneu | meu-neu | meuNeu |  |
| 61 | grinngeu | grinngeuf | grin-ngeuf | grinNgeuf | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 62 | grinngeu | grinngeuw | grin-ngeuw | grinNgeuw | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 63 | grinngeu | grinngeuh | grin-ngeuh | grinNgeuh | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 64 | grinngeu | grinngeu | grin-ngeu | grinNgeu | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |

## roots-03.wav  (numbered 65-96)

| # | base | form | syllables | stress (P4/N1) | note |
|---|---|---|---|---|---|
| 65 | wifeu | wifeuf | wi-feuf | wiFeuf |  |
| 66 | wifeu | wifeuw | wi-feuw | wiFeuw |  |
| 67 | wifeu | wifeuh | wi-feuh | wiFeuh |  |
| 68 | wifeu | wifeu | wi-feu | wiFeu |  |
| 69 | daeilfeu | daeilfeuf | daeil-feuf | daeilFeuf |  |
| 70 | daeilfeu | daeilfeuw | daeil-feuw | daeilFeuw |  |
| 71 | daeilfeu | daeilfeuh | daeil-feuh | daeilFeuh |  |
| 72 | daeilfeu | daeilfeu | daeil-feu | daeilFeu |  |
| 73 | nalne | nalnef | nal-nef | nalNef |  |
| 74 | nalne | nalnew | nal-new | nalNew |  |
| 75 | nalne | nalneh | nal-neh | nalNeh |  |
| 76 | nalne | nalne | nal-ne | nalNe |  |
| 77 | jeijau | jeijauf | jei-jauf | jeiJauf |  |
| 78 | jeijau | jeijauw | jei-jauw | jeiJauw |  |
| 79 | jeijau | jeijauh | jei-jauh | jeiJauh |  |
| 80 | jeijau | jeijau | jei-jau | jeiJau |  |
| 81 | wurshi | wurshif | wur-shif | wurShif | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 82 | wurshi | wurshiw | wur-shiw | wurShiw | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 83 | wurshi | wurshih | wur-shih | wurShih | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 84 | wurshi | wurshi | wur-shi | wurShi | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 85 | gildu | gilduf | gil-duf | gilDuf |  |
| 86 | gildu | gilduw | gil-duw | gilDuw |  |
| 87 | gildu | gilduh | gil-duh | gilDuh |  |
| 88 | gildu | gildu | gil-du | gilDu |  |
| 89 | jinci | jincif | jin-cif | jinCif |  |
| 90 | jinci | jinciw | jin-ciw | jinCiw |  |
| 91 | jinci | jincih | jin-cih | jinCih |  |
| 92 | jinci | jinci | jin-ci | jinCi |  |
| 93 | jausgae | jausgaef | jaus-gaef | jausGaef |  |
| 94 | jausgae | jausgaew | jaus-gaew | jausGaew |  |
| 95 | jausgae | jausgaeh | jaus-gaeh | jausGaeh |  |
| 96 | jausgae | jausgae | jaus-gae | jausGae |  |

## roots-04.wav  (numbered 97-128)

| # | base | form | syllables | stress (P4/N1) | note |
|---|---|---|---|---|---|
| 97 | foljy | foljyf | fol-jyf | folJyf |  |
| 98 | foljy | foljyw | fol-jyw | folJyw |  |
| 99 | foljy | foljyh | fol-jyh | folJyh |  |
| 100 | foljy | foljy | fol-jy | folJy |  |
| 101 | eimlaeu | eimlaeuf | eim-laeuf | eimLaeuf |  |
| 102 | eimlaeu | eimlaeuw | eim-laeuw | eimLaeuw |  |
| 103 | eimlaeu | eimlaeuh | eim-laeuh | eimLaeuh |  |
| 104 | eimlaeu | eimlaeu | eim-laeu | eimLaeu |  |
| 105 | bysseu | bysseuf | bys-seuf | bysSeuf |  |
| 106 | bysseu | bysseuw | bys-seuw | bysSeuw |  |
| 107 | bysseu | bysseuh | bys-seuh | bysSeuh |  |
| 108 | bysseu | bysseu | bys-seu | bysSeu |  |
| 109 | shefaeu | shefaeuf | she-faeuf | sheFaeuf |  |
| 110 | shefaeu | shefaeuw | she-faeuw | sheFaeuw |  |
| 111 | shefaeu | shefaeuh | she-faeuh | sheFaeuh |  |
| 112 | shefaeu | shefaeu | she-faeu | sheFaeu |  |
| 113 | joibri | joibrif | joi-brif | joiBrif |  |
| 114 | joibri | joibriw | joi-briw | joiBriw |  |
| 115 | joibri | joibrih | joi-brih | joiBrih |  |
| 116 | joibri | joibri | joi-bri | joiBri |  |
| 117 | sheucou | sheucouf | sheu-couf | sheuCouf |  |
| 118 | sheucou | sheucouw | sheu-couw | sheuCouw |  |
| 119 | sheucou | sheucouh | sheu-couh | sheuCouh |  |
| 120 | sheucou | sheucou | sheu-cou | sheuCou |  |
| 121 | gomthou | gomthouf | gom-thouf | gomThouf | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 122 | gomthou | gomthouw | gom-thouw | gomThouw | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 123 | gomthou | gomthouh | gom-thouh | gomThouh | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 124 | gomthou | gomthou | gom-thou | gomThou | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 125 | seinsoi | seinsoif | sein-soif | seinSoif |  |
| 126 | seinsoi | seinsoiw | sein-soiw | seinSoiw |  |
| 127 | seinsoi | seinsoih | sein-soih | seinSoih |  |
| 128 | seinsoi | seinsoi | sein-soi | seinSoi |  |

## roots-05.wav  (numbered 129-160)

| # | base | form | syllables | stress (P4/N1) | note |
|---|---|---|---|---|---|
| 129 | mangi | mangif | ma-ngif | maNgif | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 130 | mangi | mangiw | ma-ngiw | maNgiw | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 131 | mangi | mangih | ma-ngih | maNgih | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 132 | mangi | mangi | ma-ngi | maNgi | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 133 | wenci | wencif | wen-cif | wenCif |  |
| 134 | wenci | wenciw | wen-ciw | wenCiw |  |
| 135 | wenci | wencih | wen-cih | wenCih |  |
| 136 | wenci | wenci | wen-ci | wenCi |  |
| 137 | roldai | roldaif | rol-daif | rolDaif |  |
| 138 | roldai | roldaiw | rol-daiw | rolDaiw |  |
| 139 | roldai | roldaih | rol-daih | rolDaih |  |
| 140 | roldai | roldai | rol-dai | rolDai |  |
| 141 | nurfeu | nurfeuf | nur-feuf | nurFeuf |  |
| 142 | nurfeu | nurfeuw | nur-feuw | nurFeuw |  |
| 143 | nurfeu | nurfeuh | nur-feuh | nurFeuh |  |
| 144 | nurfeu | nurfeu | nur-feu | nurFeu |  |
| 145 | rora | roraf | ro-raf | roRaf |  |
| 146 | rora | roraw | ro-raw | roRaw |  |
| 147 | rora | rorah | ro-rah | roRah |  |
| 148 | rora | rora | ro-ra | roRa |  |
| 149 | hoindu | hoinduf | hoin-duf | hoinDuf |  |
| 150 | hoindu | hoinduw | hoin-duw | hoinDuw |  |
| 151 | hoindu | hoinduh | hoin-duh | hoinDuh |  |
| 152 | hoindu | hoindu | hoin-du | hoinDu |  |
| 153 | gonny | gonnyf | gon-nyf | gonNyf |  |
| 154 | gonny | gonnyw | gon-nyw | gonNyw |  |
| 155 | gonny | gonnyh | gon-nyh | gonNyh |  |
| 156 | gonny | gonny | gon-ny | gonNy |  |
| 157 | waulny | waulnyf | waul-nyf | waulNyf |  |
| 158 | waulny | waulnyw | waul-nyw | waulNyw |  |
| 159 | waulny | waulnyh | waul-nyh | waulNyh |  |
| 160 | waulny | waulny | waul-ny | waulNy |  |

## roots-06.wav  (numbered 161-192)

| # | base | form | syllables | stress (P4/N1) | note |
|---|---|---|---|---|---|
| 161 | feisna | feisnaf | feis-naf | feisNaf |  |
| 162 | feisna | feisnaw | feis-naw | feisNaw |  |
| 163 | feisna | feisnah | feis-nah | feisNah |  |
| 164 | feisna | feisna | feis-na | feisNa |  |
| 165 | thowai | thowaif | tho-waif | thoWaif |  |
| 166 | thowai | thowaiw | tho-waiw | thoWaiw |  |
| 167 | thowai | thowaih | tho-waih | thoWaih |  |
| 168 | thowai | thowai | tho-wai | thoWai |  |
| 169 | jaeilleu | jaeilleuf | jaeil-leuf | jaeilLeuf |  |
| 170 | jaeilleu | jaeilleuw | jaeil-leuw | jaeilLeuw |  |
| 171 | jaeilleu | jaeilleuh | jaeil-leuh | jaeilLeuh |  |
| 172 | jaeilleu | jaeilleu | jaeil-leu | jaeilLeu |  |
| 173 | neunca | neuncaf | neun-caf | neunCaf |  |
| 174 | neunca | neuncaw | neun-caw | neunCaw |  |
| 175 | neunca | neuncah | neun-cah | neunCah |  |
| 176 | neunca | neunca | neun-ca | neunCa |  |
| 177 | draibrai | draibraif | drai-braif | draiBraif |  |
| 178 | draibrai | draibraiw | drai-braiw | draiBraiw |  |
| 179 | draibrai | draibraih | drai-braih | draiBraih |  |
| 180 | draibrai | draibrai | drai-brai | draiBrai |  |
| 181 | braisshei | braissheif | brais-sheif | braisSheif | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 182 | braisshei | braissheiw | brais-sheiw | braisSheiw | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 183 | braisshei | braissheih | brais-sheih | braisSheih | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 184 | braisshei | braisshei | brais-shei | braisShei | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 185 | sheiga | sheigaf | shei-gaf | sheiGaf |  |
| 186 | sheiga | sheigaw | shei-gaw | sheiGaw |  |
| 187 | sheiga | sheigah | shei-gah | sheiGah |  |
| 188 | sheiga | sheiga | shei-ga | sheiGa |  |
| 189 | graeuco | graeucof | graeu-cof | graeuCof |  |
| 190 | graeuco | graeucow | graeu-cow | graeuCow |  |
| 191 | graeuco | graeucoh | graeu-coh | graeuCoh |  |
| 192 | graeuco | graeuco | graeu-co | graeuCo |  |


---

## What this sheet does NOT do

- It does not cover the **M3a seam** (a root-final `f` / `w` / `h` in front of a case suffix,
  always unstressed) - that layer is unjudged, see `../decision/03-open-questions.md` section 0
  item 20.
- It cannot show the **/n/ + /g/ (`nk`) class** of candidates: the pool was packed before `P6`
  existed and contains no `nk` spelling at all (`03-open-questions.md` section 0 item 24).
- It does not say which form is a good word. That is the pick, and it is yours to make.
