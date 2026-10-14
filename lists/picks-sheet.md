# lists/picks-sheet.md - GENERATED audition sheet. DO NOT ANNOTATE HERE.

Regenerate with:

```
python3 tools/syllabify.py --sheet > lists/picks-sheet.md
```

Any annotation written in this file is **lost** on regeneration. **Picks go in `lists/picks.md`.**
The numbers are **this sheet's own** sample of the current pool. ⚠️ The audio run of 2026-10-14
(`../audio/roots-index.txt`) was a **different, frozen** sample of the pre-P6 pool: its numbers do
NOT correspond to these, and `audio/` must never be regenerated (`../audio/00-README.md`).

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

## Reading rules (P6) - and the two flags left

**`sh` and `ng` are ALWAYS one phoneme** (`sh` = the *sh* of *ship*, `ng` = the *ng* of *sing*),
and **a stop after a nasal coda is obligatorily hard**: `/m/` or `/n/` + `/b d g/` is written
`mp np mt nt mk nk` and sung `[p t k]`. That is `P6` (ruled 2026-10-14), so a row containing `ng`
never means "n then g" and nothing below needs a guess about the reading.

Two flags can appear:

- **`stress capital lands on a DIGRAPH`** - the stressed syllable starts with `sh` / `th` / `ng` / `ae`
  (one sound, two letters) and N1 has no rule for that case yet. The `stress` column capitalises the
  first letter; treat it as provisional.
- **`ILLEGAL under P6`** - the form spells a nasal coda + **soft** stop (`mb nb md nd mg`), which P6
  forbids: it must be respelled with the hard letter (`namgae` -> `namkae`). ⚠️ **A pick on such a row
  is still valid as a SOUND** - only the spelling changes, and the pool regeneration (which respells
  these) is a separate, later step.

Also: `stress` is only the DEFAULT (P4). A composer may overwrite it in notation - that is
performance, not a different word.

---

Source: `lists/roots-bases-current.txt` (26769 packed bases); sample 48 bases, seed 20261014.
! The audio run of 2026-10-14 (`../audio/roots-index.txt`) used a DIFFERENT sample
(the pre-P6 pool) and is frozen - its numbers are not comparable with these.

## roots-01.wav  (numbered 1-32)

| # | base | form | syllables | stress (P4/N1) | note |
|---|---|---|---|---|---|
| 1 | tharri | tharrif | thar-rif | tharRif |  |
| 2 | tharri | tharriw | thar-riw | tharRiw |  |
| 3 | tharri | tharrih | thar-rih | tharRih |  |
| 4 | tharri | tharri | thar-ri | tharRi |  |
| 5 | naljau | naljauf | nal-jauf | nalJauf |  |
| 6 | naljau | naljauw | nal-jauw | nalJauw |  |
| 7 | naljau | naljauh | nal-jauh | nalJauh |  |
| 8 | naljau | naljau | nal-jau | nalJau |  |
| 9 | diwmy | diwmyf | di-wmyf | diWmyf |  |
| 10 | diwmy | diwmyw | di-wmyw | diWmyw |  |
| 11 | diwmy | diwmyh | di-wmyh | diWmyh |  |
| 12 | diwmy | diwmy | di-wmy | diWmy |  |
| 13 | sulsi | sulsif | sul-sif | sulSif |  |
| 14 | sulsi | sulsiw | sul-siw | sulSiw |  |
| 15 | sulsi | sulsih | sul-sih | sulSih |  |
| 16 | sulsi | sulsi | sul-si | sulSi |  |
| 17 | thywe | thywef | thy-wef | thyWef |  |
| 18 | thywe | thywew | thy-wew | thyWew |  |
| 19 | thywe | thyweh | thy-weh | thyWeh |  |
| 20 | thywe | thywe | thy-we | thyWe |  |
| 21 | daefno | daefnof | dae-fnof | daeFnof |  |
| 22 | daefno | daefnow | dae-fnow | daeFnow |  |
| 23 | daefno | daefnoh | dae-fnoh | daeFnoh |  |
| 24 | daefno | daefno | dae-fno | daeFno |  |
| 25 | wounmai | wounmaif | woun-maif | wounMaif |  |
| 26 | wounmai | wounmaiw | woun-maiw | wounMaiw |  |
| 27 | wounmai | wounmaih | woun-maih | wounMaih |  |
| 28 | wounmai | wounmai | woun-mai | wounMai |  |
| 29 | leissau | leissauf | leis-sauf | leisSauf |  |
| 30 | leissau | leissauw | leis-sauw | leisSauw |  |
| 31 | leissau | leissauh | leis-sauh | leisSauh |  |
| 32 | leissau | leissau | leis-sau | leisSau |  |

## roots-02.wav  (numbered 33-64)

| # | base | form | syllables | stress (P4/N1) | note |
|---|---|---|---|---|---|
| 33 | oigroi | oigroif | oi-groif | oiGroif |  |
| 34 | oigroi | oigroiw | oi-groiw | oiGroiw |  |
| 35 | oigroi | oigroih | oi-groih | oiGroih |  |
| 36 | oigroi | oigroi | oi-groi | oiGroi |  |
| 37 | maeidau | maeidauf | maei-dauf | maeiDauf |  |
| 38 | maeidau | maeidauw | maei-dauw | maeiDauw |  |
| 39 | maeidau | maeidauh | maei-dauh | maeiDauh |  |
| 40 | maeidau | maeidau | maei-dau | maeiDau |  |
| 41 | graeljou | graeljouf | grael-jouf | graelJouf |  |
| 42 | graeljou | graeljouw | grael-jouw | graelJouw |  |
| 43 | graeljou | graeljouh | grael-jouh | graelJouh |  |
| 44 | graeljou | graeljou | grael-jou | graelJou |  |
| 45 | rourwae | rourwaef | rour-waef | rourWaef |  |
| 46 | rourwae | rourwaew | rour-waew | rourWaew |  |
| 47 | rourwae | rourwaeh | rour-waeh | rourWaeh |  |
| 48 | rourwae | rourwae | rour-wae | rourWae |  |
| 49 | grorfu | grorfuf | gror-fuf | grorFuf |  |
| 50 | grorfu | grorfuw | gror-fuw | grorFuw |  |
| 51 | grorfu | grorfuh | gror-fuh | grorFuh |  |
| 52 | grorfu | grorfu | gror-fu | grorFu |  |
| 53 | goulwau | goulwauf | goul-wauf | goulWauf |  |
| 54 | goulwau | goulwauw | goul-wauw | goulWauw |  |
| 55 | goulwau | goulwauh | goul-wauh | goulWauh |  |
| 56 | goulwau | goulwau | goul-wau | goulWau |  |
| 57 | meumkou | meumkouf | meum-kouf | meumKouf | P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 58 | meumkou | meumkouw | meum-kouw | meumKouw | P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 59 | meumkou | meumkouh | meum-kouh | meumKouh | P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 60 | meumkou | meumkou | meum-kou | meumKou | P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 61 | grimwaei | grimwaeif | grim-waeif | grimWaeif |  |
| 62 | grimwaei | grimwaeiw | grim-waeiw | grimWaeiw |  |
| 63 | grimwaei | grimwaeih | grim-waeih | grimWaeih |  |
| 64 | grimwaei | grimwaei | grim-waei | grimWaei |  |

## roots-03.wav  (numbered 65-96)

| # | base | form | syllables | stress (P4/N1) | note |
|---|---|---|---|---|---|
| 65 | weusmo | weusmof | weus-mof | weusMof |  |
| 66 | weusmo | weusmow | weus-mow | weusMow |  |
| 67 | weusmo | weusmoh | weus-moh | weusMoh |  |
| 68 | weusmo | weusmo | weus-mo | weusMo |  |
| 69 | daeijae | daeijaef | daei-jaef | daeiJaef |  |
| 70 | daeijae | daeijaew | daei-jaew | daeiJaew |  |
| 71 | daeijae | daeijaeh | daei-jaeh | daeiJaeh |  |
| 72 | daeijae | daeijae | daei-jae | daeiJae |  |
| 73 | nahmu | nahmuf | na-hmuf | naHmuf |  |
| 74 | nahmu | nahmuw | na-hmuw | naHmuw |  |
| 75 | nahmu | nahmuh | na-hmuh | naHmuh |  |
| 76 | nahmu | nahmu | na-hmu | naHmu |  |
| 77 | jeicoi | jeicoif | jei-coif | jeiCoif |  |
| 78 | jeicoi | jeicoiw | jei-coiw | jeiCoiw |  |
| 79 | jeicoi | jeicoih | jei-coih | jeiCoih |  |
| 80 | jeicoi | jeicoi | jei-coi | jeiCoi |  |
| 81 | wunnge | wunngef | wun-ngef | wunNgef | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 82 | wunnge | wunngew | wun-ngew | wunNgew | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 83 | wunnge | wunngeh | wun-ngeh | wunNgeh | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 84 | wunnge | wunnge | wun-nge | wunNge | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 85 | gihoi | gihoif | gi-hoif | giHoif |  |
| 86 | gihoi | gihoiw | gi-hoiw | giHoiw |  |
| 87 | gihoi | gihoih | gi-hoih | giHoih |  |
| 88 | gihoi | gihoi | gi-hoi | giHoi |  |
| 89 | jimji | jimjif | jim-jif | jimJif |  |
| 90 | jimji | jimjiw | jim-jiw | jimJiw |  |
| 91 | jimji | jimjih | jim-jih | jimJih |  |
| 92 | jimji | jimji | jim-ji | jimJi |  |
| 93 | jaurmy | jaurmyf | jaur-myf | jaurMyf |  |
| 94 | jaurmy | jaurmyw | jaur-myw | jaurMyw |  |
| 95 | jaurmy | jaurmyh | jaur-myh | jaurMyh |  |
| 96 | jaurmy | jaurmy | jaur-my | jaurMy |  |

## roots-04.wav  (numbered 97-128)

| # | base | form | syllables | stress (P4/N1) | note |
|---|---|---|---|---|---|
| 97 | fojnoi | fojnoif | fo-jnoif | foJnoif |  |
| 98 | fojnoi | fojnoiw | fo-jnoiw | foJnoiw |  |
| 99 | fojnoi | fojnoih | fo-jnoih | foJnoih |  |
| 100 | fojnoi | fojnoi | fo-jnoi | foJnoi |  |
| 101 | eimeu | eimeuf | ei-meuf | eiMeuf |  |
| 102 | eimeu | eimeuw | ei-meuw | eiMeuw |  |
| 103 | eimeu | eimeuh | ei-meuh | eiMeuh |  |
| 104 | eimeu | eimeu | ei-meu | eiMeu |  |
| 105 | bysngeu | bysngeuf | bys-ngeuf | bysNgeuf | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 106 | bysngeu | bysngeuw | bys-ngeuw | bysNgeuw | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 107 | bysngeu | bysngeuh | bys-ngeuh | bysNgeuh | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 108 | bysngeu | bysngeu | bys-ngeu | bysNgeu | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 109 | shausrei | shausreif | shaus-reif | shausReif |  |
| 110 | shausrei | shausreiw | shaus-reiw | shausReiw |  |
| 111 | shausrei | shausreih | shaus-reih | shausReih |  |
| 112 | shausrei | shausrei | shaus-rei | shausRei |  |
| 113 | josshoi | josshoif | jos-shoif | josShoif | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 114 | josshoi | josshoiw | jos-shoiw | josShoiw | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 115 | josshoi | josshoih | jos-shoih | josShoih | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 116 | josshoi | josshoi | jos-shoi | josShoi | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 117 | sheisme | sheismef | sheis-mef | sheisMef |  |
| 118 | sheisme | sheismew | sheis-mew | sheisMew |  |
| 119 | sheisme | sheismeh | sheis-meh | sheisMeh |  |
| 120 | sheisme | sheisme | sheis-me | sheisMe |  |
| 121 | gommi | gommif | gom-mif | gomMif |  |
| 122 | gommi | gommiw | gom-miw | gomMiw |  |
| 123 | gommi | gommih | gom-mih | gomMih |  |
| 124 | gommi | gommi | gom-mi | gomMi |  |
| 125 | seimsei | seimseif | seim-seif | seimSeif |  |
| 126 | seimsei | seimseiw | seim-seiw | seimSeiw |  |
| 127 | seimsei | seimseih | seim-seih | seimSeih |  |
| 128 | seimsei | seimsei | seim-sei | seimSei |  |

## roots-05.wav  (numbered 129-160)

| # | base | form | syllables | stress (P4/N1) | note |
|---|---|---|---|---|---|
| 129 | mamma | mammaf | mam-maf | mamMaf |  |
| 130 | mamma | mammaw | mam-maw | mamMaw |  |
| 131 | mamma | mammah | mam-mah | mamMah |  |
| 132 | mamma | mamma | mam-ma | mamMa |  |
| 133 | welsa | welsaf | wel-saf | welSaf |  |
| 134 | welsa | welsaw | wel-saw | welSaw |  |
| 135 | welsa | welsah | wel-sah | welSah |  |
| 136 | welsa | welsa | wel-sa | welSa |  |
| 137 | rocau | rocauf | ro-cauf | roCauf |  |
| 138 | rocau | rocauw | ro-cauw | roCauw |  |
| 139 | rocau | rocauh | ro-cauh | roCauh |  |
| 140 | rocau | rocau | ro-cau | roCau |  |
| 141 | nunko | nunkof | nun-kof | nunKof | P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 142 | nunko | nunkow | nun-kow | nunKow | P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 143 | nunko | nunkoh | nun-koh | nunKoh | P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 144 | nunko | nunko | nun-ko | nunKo | P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 145 | ronae | ronaef | ro-naef | roNaef |  |
| 146 | ronae | ronaew | ro-naew | roNaew |  |
| 147 | ronae | ronaeh | ro-naeh | roNaeh |  |
| 148 | ronae | ronae | ro-nae | roNae |  |
| 149 | hoimno | hoimnof | hoim-nof | hoimNof |  |
| 150 | hoimno | hoimnow | hoim-now | hoimNow |  |
| 151 | hoimno | hoimnoh | hoim-noh | hoimNoh |  |
| 152 | hoimno | hoimno | hoim-no | hoimNo |  |
| 153 | gonfei | gonfeif | gon-feif | gonFeif |  |
| 154 | gonfei | gonfeiw | gon-feiw | gonFeiw |  |
| 155 | gonfei | gonfeih | gon-feih | gonFeih |  |
| 156 | gonfei | gonfei | gon-fei | gonFei |  |
| 157 | waufy | waufyf | wau-fyf | wauFyf |  |
| 158 | waufy | waufyw | wau-fyw | wauFyw |  |
| 159 | waufy | waufyh | wau-fyh | wauFyh |  |
| 160 | waufy | waufy | wau-fy | wauFy |  |

## roots-06.wav  (numbered 161-192)

| # | base | form | syllables | stress (P4/N1) | note |
|---|---|---|---|---|---|
| 161 | feisga | feisgaf | feis-gaf | feisGaf |  |
| 162 | feisga | feisgaw | feis-gaw | feisGaw |  |
| 163 | feisga | feisgah | feis-gah | feisGah |  |
| 164 | feisga | feisga | feis-ga | feisGa |  |
| 165 | thorwi | thorwif | thor-wif | thorWif |  |
| 166 | thorwi | thorwiw | thor-wiw | thorWiw |  |
| 167 | thorwi | thorwih | thor-wih | thorWih |  |
| 168 | thorwi | thorwi | thor-wi | thorWi |  |
| 169 | jaeihne | jaeihnef | jaei-hnef | jaeiHnef |  |
| 170 | jaeihne | jaeihnew | jaei-hnew | jaeiHnew |  |
| 171 | jaeihne | jaeihneh | jaei-hneh | jaeiHneh |  |
| 172 | jaeihne | jaeihne | jaei-hne | jaeiHne |  |
| 173 | neumhe | neumhef | neum-hef | neumHef |  |
| 174 | neumhe | neumhew | neum-hew | neumHew |  |
| 175 | neumhe | neumheh | neum-heh | neumHeh |  |
| 176 | neumhe | neumhe | neum-he | neumHe |  |
| 177 | draeuthu | draeuthuf | draeu-thuf | draeuThuf | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 178 | draeuthu | draeuthuw | draeu-thuw | draeuThuw | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 179 | draeuthu | draeuthuh | draeu-thuh | draeuThuh | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 180 | draeuthu | draeuthu | draeu-thu | draeuThu | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 181 | braisngeu | braisngeuf | brais-ngeuf | braisNgeuf | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 182 | braisngeu | braisngeuw | brais-ngeuw | braisNgeuw | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 183 | braisngeu | braisngeuh | brais-ngeuh | braisNgeuh | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 184 | braisngeu | braisngeu | brais-ngeu | braisNgeu | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 185 | shesshaeu | shesshaeuf | shes-shaeuf | shesShaeuf | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 186 | shesshaeu | shesshaeuw | shes-shaeuw | shesShaeuw | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 187 | shesshaeu | shesshaeuh | shes-shaeuh | shesShaeuh | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 188 | shesshaeu | shesshaeu | shes-shaeu | shesShaeu | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 189 | graeiswau | graeiswauf | graeis-wauf | graeisWauf |  |
| 190 | graeiswau | graeiswauw | graeis-wauw | graeisWauw |  |
| 191 | graeiswau | graeiswauh | graeis-wauh | graeisWauh |  |
| 192 | graeiswau | graeiswau | graeis-wau | graeisWau |  |


---

## What this sheet does NOT do

- It does not cover the **M3a seam** (a root-final `f` / `w` / `h` in front of a case suffix,
  always unstressed) - that layer is unjudged, see `../decision/03-open-questions.md` section 0
  item 20.
- It cannot show the **/n/ + /g/ (`nk`) class** of candidates: the pool was packed before `P6`
  existed and contains no `nk` spelling at all (`03-open-questions.md` section 0 item 24).
- It does not say which form is a good word. That is the pick, and it is yours to make.
