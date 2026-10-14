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

Every group of 5 rows is ONE base: `+f` | `+w` (= /v/) | `+h` | `+s` | bare. A base yields **exactly 2**
roots, so pick **at most one** from the `{+f, +w}` pair and **at most one** from the
`{+h, +s, bare}` trio. (`+s` is new in **R4**; the `s` branch is RESERVED for a future
adjective / adverb / exceptional-case job, so its meaning slot is held.)

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
| 4 | tharri | tharris | thar-ris | tharRis |  |
| 5 | tharri | tharri | thar-ri | tharRi |  |
| 6 | naljau | naljauf | nal-jauf | nalJauf |  |
| 7 | naljau | naljauw | nal-jauw | nalJauw |  |
| 8 | naljau | naljauh | nal-jauh | nalJauh |  |
| 9 | naljau | naljaus | nal-jaus | nalJaus |  |
| 10 | naljau | naljau | nal-jau | nalJau |  |
| 11 | diwmy | diwmyf | di-wmyf | diWmyf |  |
| 12 | diwmy | diwmyw | di-wmyw | diWmyw |  |
| 13 | diwmy | diwmyh | di-wmyh | diWmyh |  |
| 14 | diwmy | diwmys | di-wmys | diWmys |  |
| 15 | diwmy | diwmy | di-wmy | diWmy |  |
| 16 | sulsi | sulsif | sul-sif | sulSif |  |
| 17 | sulsi | sulsiw | sul-siw | sulSiw |  |
| 18 | sulsi | sulsih | sul-sih | sulSih |  |
| 19 | sulsi | sulsis | sul-sis | sulSis |  |
| 20 | sulsi | sulsi | sul-si | sulSi |  |
| 21 | thywe | thywef | thy-wef | thyWef |  |
| 22 | thywe | thywew | thy-wew | thyWew |  |
| 23 | thywe | thyweh | thy-weh | thyWeh |  |
| 24 | thywe | thywes | thy-wes | thyWes |  |
| 25 | thywe | thywe | thy-we | thyWe |  |
| 26 | daefno | daefnof | dae-fnof | daeFnof |  |
| 27 | daefno | daefnow | dae-fnow | daeFnow |  |
| 28 | daefno | daefnoh | dae-fnoh | daeFnoh |  |
| 29 | daefno | daefnos | dae-fnos | daeFnos |  |
| 30 | daefno | daefno | dae-fno | daeFno |  |
| 31 | wounmai | wounmaif | woun-maif | wounMaif |  |
| 32 | wounmai | wounmaiw | woun-maiw | wounMaiw |  |
| 33 | wounmai | wounmaih | woun-maih | wounMaih |  |
| 34 | wounmai | wounmais | woun-mais | wounMais |  |
| 35 | wounmai | wounmai | woun-mai | wounMai |  |
| 36 | leissau | leissauf | leis-sauf | leisSauf |  |
| 37 | leissau | leissauw | leis-sauw | leisSauw |  |
| 38 | leissau | leissauh | leis-sauh | leisSauh |  |
| 39 | leissau | leissaus | leis-saus | leisSaus |  |
| 40 | leissau | leissau | leis-sau | leisSau |  |

## roots-02.wav  (numbered 41-72)

| # | base | form | syllables | stress (P4/N1) | note |
|---|---|---|---|---|---|
| 41 | oigroi | oigroif | oi-groif | oiGroif |  |
| 42 | oigroi | oigroiw | oi-groiw | oiGroiw |  |
| 43 | oigroi | oigroih | oi-groih | oiGroih |  |
| 44 | oigroi | oigrois | oi-grois | oiGrois |  |
| 45 | oigroi | oigroi | oi-groi | oiGroi |  |
| 46 | maeidau | maeidauf | maei-dauf | maeiDauf |  |
| 47 | maeidau | maeidauw | maei-dauw | maeiDauw |  |
| 48 | maeidau | maeidauh | maei-dauh | maeiDauh |  |
| 49 | maeidau | maeidaus | maei-daus | maeiDaus |  |
| 50 | maeidau | maeidau | maei-dau | maeiDau |  |
| 51 | graeljou | graeljouf | grael-jouf | graelJouf |  |
| 52 | graeljou | graeljouw | grael-jouw | graelJouw |  |
| 53 | graeljou | graeljouh | grael-jouh | graelJouh |  |
| 54 | graeljou | graeljous | grael-jous | graelJous |  |
| 55 | graeljou | graeljou | grael-jou | graelJou |  |
| 56 | rourwae | rourwaef | rour-waef | rourWaef |  |
| 57 | rourwae | rourwaew | rour-waew | rourWaew |  |
| 58 | rourwae | rourwaeh | rour-waeh | rourWaeh |  |
| 59 | rourwae | rourwaes | rour-waes | rourWaes |  |
| 60 | rourwae | rourwae | rour-wae | rourWae |  |
| 61 | grorfu | grorfuf | gror-fuf | grorFuf |  |
| 62 | grorfu | grorfuw | gror-fuw | grorFuw |  |
| 63 | grorfu | grorfuh | gror-fuh | grorFuh |  |
| 64 | grorfu | grorfus | gror-fus | grorFus |  |
| 65 | grorfu | grorfu | gror-fu | grorFu |  |
| 66 | goulwau | goulwauf | goul-wauf | goulWauf |  |
| 67 | goulwau | goulwauw | goul-wauw | goulWauw |  |
| 68 | goulwau | goulwauh | goul-wauh | goulWauh |  |
| 69 | goulwau | goulwaus | goul-waus | goulWaus |  |
| 70 | goulwau | goulwau | goul-wau | goulWau |  |
| 71 | meumkou | meumkouf | meum-kouf | meumKouf | P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 72 | meumkou | meumkouw | meum-kouw | meumKouw | P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 73 | meumkou | meumkouh | meum-kouh | meumKouh | P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 74 | meumkou | meumkous | meum-kous | meumKous | P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 75 | meumkou | meumkou | meum-kou | meumKou | P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 76 | grimwaei | grimwaeif | grim-waeif | grimWaeif |  |
| 77 | grimwaei | grimwaeiw | grim-waeiw | grimWaeiw |  |
| 78 | grimwaei | grimwaeih | grim-waeih | grimWaeih |  |
| 79 | grimwaei | grimwaeis | grim-waeis | grimWaeis |  |
| 80 | grimwaei | grimwaei | grim-waei | grimWaei |  |

## roots-03.wav  (numbered 81-112)

| # | base | form | syllables | stress (P4/N1) | note |
|---|---|---|---|---|---|
| 81 | weusmo | weusmof | weus-mof | weusMof |  |
| 82 | weusmo | weusmow | weus-mow | weusMow |  |
| 83 | weusmo | weusmoh | weus-moh | weusMoh |  |
| 84 | weusmo | weusmos | weus-mos | weusMos |  |
| 85 | weusmo | weusmo | weus-mo | weusMo |  |
| 86 | daeijae | daeijaef | daei-jaef | daeiJaef |  |
| 87 | daeijae | daeijaew | daei-jaew | daeiJaew |  |
| 88 | daeijae | daeijaeh | daei-jaeh | daeiJaeh |  |
| 89 | daeijae | daeijaes | daei-jaes | daeiJaes |  |
| 90 | daeijae | daeijae | daei-jae | daeiJae |  |
| 91 | nahmu | nahmuf | na-hmuf | naHmuf |  |
| 92 | nahmu | nahmuw | na-hmuw | naHmuw |  |
| 93 | nahmu | nahmuh | na-hmuh | naHmuh |  |
| 94 | nahmu | nahmus | na-hmus | naHmus |  |
| 95 | nahmu | nahmu | na-hmu | naHmu |  |
| 96 | jeicoi | jeicoif | jei-coif | jeiCoif |  |
| 97 | jeicoi | jeicoiw | jei-coiw | jeiCoiw |  |
| 98 | jeicoi | jeicoih | jei-coih | jeiCoih |  |
| 99 | jeicoi | jeicois | jei-cois | jeiCois |  |
| 100 | jeicoi | jeicoi | jei-coi | jeiCoi |  |
| 101 | wunnge | wunngef | wun-ngef | wunNgef | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 102 | wunnge | wunngew | wun-ngew | wunNgew | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 103 | wunnge | wunngeh | wun-ngeh | wunNgeh | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 104 | wunnge | wunnges | wun-nges | wunNges | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 105 | wunnge | wunnge | wun-nge | wunNge | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 106 | gihoi | gihoif | gi-hoif | giHoif |  |
| 107 | gihoi | gihoiw | gi-hoiw | giHoiw |  |
| 108 | gihoi | gihoih | gi-hoih | giHoih |  |
| 109 | gihoi | gihois | gi-hois | giHois |  |
| 110 | gihoi | gihoi | gi-hoi | giHoi |  |
| 111 | jimji | jimjif | jim-jif | jimJif |  |
| 112 | jimji | jimjiw | jim-jiw | jimJiw |  |
| 113 | jimji | jimjih | jim-jih | jimJih |  |
| 114 | jimji | jimjis | jim-jis | jimJis |  |
| 115 | jimji | jimji | jim-ji | jimJi |  |
| 116 | jaurmy | jaurmyf | jaur-myf | jaurMyf |  |
| 117 | jaurmy | jaurmyw | jaur-myw | jaurMyw |  |
| 118 | jaurmy | jaurmyh | jaur-myh | jaurMyh |  |
| 119 | jaurmy | jaurmys | jaur-mys | jaurMys |  |
| 120 | jaurmy | jaurmy | jaur-my | jaurMy |  |

## roots-04.wav  (numbered 121-152)

| # | base | form | syllables | stress (P4/N1) | note |
|---|---|---|---|---|---|
| 121 | fojnoi | fojnoif | fo-jnoif | foJnoif |  |
| 122 | fojnoi | fojnoiw | fo-jnoiw | foJnoiw |  |
| 123 | fojnoi | fojnoih | fo-jnoih | foJnoih |  |
| 124 | fojnoi | fojnois | fo-jnois | foJnois |  |
| 125 | fojnoi | fojnoi | fo-jnoi | foJnoi |  |
| 126 | eimeu | eimeuf | ei-meuf | eiMeuf |  |
| 127 | eimeu | eimeuw | ei-meuw | eiMeuw |  |
| 128 | eimeu | eimeuh | ei-meuh | eiMeuh |  |
| 129 | eimeu | eimeus | ei-meus | eiMeus |  |
| 130 | eimeu | eimeu | ei-meu | eiMeu |  |
| 131 | bysngeu | bysngeuf | bys-ngeuf | bysNgeuf | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 132 | bysngeu | bysngeuw | bys-ngeuw | bysNgeuw | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 133 | bysngeu | bysngeuh | bys-ngeuh | bysNgeuh | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 134 | bysngeu | bysngeus | bys-ngeus | bysNgeus | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 135 | bysngeu | bysngeu | bys-ngeu | bysNgeu | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 136 | shausrei | shausreif | shaus-reif | shausReif |  |
| 137 | shausrei | shausreiw | shaus-reiw | shausReiw |  |
| 138 | shausrei | shausreih | shaus-reih | shausReih |  |
| 139 | shausrei | shausreis | shaus-reis | shausReis |  |
| 140 | shausrei | shausrei | shaus-rei | shausRei |  |
| 141 | josshoi | josshoif | jos-shoif | josShoif | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 142 | josshoi | josshoiw | jos-shoiw | josShoiw | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 143 | josshoi | josshoih | jos-shoih | josShoih | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 144 | josshoi | josshois | jos-shois | josShois | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 145 | josshoi | josshoi | jos-shoi | josShoi | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 146 | sheisme | sheismef | sheis-mef | sheisMef |  |
| 147 | sheisme | sheismew | sheis-mew | sheisMew |  |
| 148 | sheisme | sheismeh | sheis-meh | sheisMeh |  |
| 149 | sheisme | sheismes | sheis-mes | sheisMes |  |
| 150 | sheisme | sheisme | sheis-me | sheisMe |  |
| 151 | gommi | gommif | gom-mif | gomMif |  |
| 152 | gommi | gommiw | gom-miw | gomMiw |  |
| 153 | gommi | gommih | gom-mih | gomMih |  |
| 154 | gommi | gommis | gom-mis | gomMis |  |
| 155 | gommi | gommi | gom-mi | gomMi |  |
| 156 | seimsei | seimseif | seim-seif | seimSeif |  |
| 157 | seimsei | seimseiw | seim-seiw | seimSeiw |  |
| 158 | seimsei | seimseih | seim-seih | seimSeih |  |
| 159 | seimsei | seimseis | seim-seis | seimSeis |  |
| 160 | seimsei | seimsei | seim-sei | seimSei |  |

## roots-05.wav  (numbered 161-192)

| # | base | form | syllables | stress (P4/N1) | note |
|---|---|---|---|---|---|
| 161 | mamma | mammaf | mam-maf | mamMaf |  |
| 162 | mamma | mammaw | mam-maw | mamMaw |  |
| 163 | mamma | mammah | mam-mah | mamMah |  |
| 164 | mamma | mammas | mam-mas | mamMas |  |
| 165 | mamma | mamma | mam-ma | mamMa |  |
| 166 | welsa | welsaf | wel-saf | welSaf |  |
| 167 | welsa | welsaw | wel-saw | welSaw |  |
| 168 | welsa | welsah | wel-sah | welSah |  |
| 169 | welsa | welsas | wel-sas | welSas |  |
| 170 | welsa | welsa | wel-sa | welSa |  |
| 171 | rocau | rocauf | ro-cauf | roCauf |  |
| 172 | rocau | rocauw | ro-cauw | roCauw |  |
| 173 | rocau | rocauh | ro-cauh | roCauh |  |
| 174 | rocau | rocaus | ro-caus | roCaus |  |
| 175 | rocau | rocau | ro-cau | roCau |  |
| 176 | nunko | nunkof | nun-kof | nunKof | P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 177 | nunko | nunkow | nun-kow | nunKow | P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 178 | nunko | nunkoh | nun-koh | nunKoh | P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 179 | nunko | nunkos | nun-kos | nunKos | P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 180 | nunko | nunko | nun-ko | nunKo | P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 181 | ronae | ronaef | ro-naef | roNaef |  |
| 182 | ronae | ronaew | ro-naew | roNaew |  |
| 183 | ronae | ronaeh | ro-naeh | roNaeh |  |
| 184 | ronae | ronaes | ro-naes | roNaes |  |
| 185 | ronae | ronae | ro-nae | roNae |  |
| 186 | hoimno | hoimnof | hoim-nof | hoimNof |  |
| 187 | hoimno | hoimnow | hoim-now | hoimNow |  |
| 188 | hoimno | hoimnoh | hoim-noh | hoimNoh |  |
| 189 | hoimno | hoimnos | hoim-nos | hoimNos |  |
| 190 | hoimno | hoimno | hoim-no | hoimNo |  |
| 191 | gonfei | gonfeif | gon-feif | gonFeif |  |
| 192 | gonfei | gonfeiw | gon-feiw | gonFeiw |  |
| 193 | gonfei | gonfeih | gon-feih | gonFeih |  |
| 194 | gonfei | gonfeis | gon-feis | gonFeis |  |
| 195 | gonfei | gonfei | gon-fei | gonFei |  |
| 196 | waufy | waufyf | wau-fyf | wauFyf |  |
| 197 | waufy | waufyw | wau-fyw | wauFyw |  |
| 198 | waufy | waufyh | wau-fyh | wauFyh |  |
| 199 | waufy | waufys | wau-fys | wauFys |  |
| 200 | waufy | waufy | wau-fy | wauFy |  |

## roots-06.wav  (numbered 201-232)

| # | base | form | syllables | stress (P4/N1) | note |
|---|---|---|---|---|---|
| 201 | feisga | feisgaf | feis-gaf | feisGaf |  |
| 202 | feisga | feisgaw | feis-gaw | feisGaw |  |
| 203 | feisga | feisgah | feis-gah | feisGah |  |
| 204 | feisga | feisgas | feis-gas | feisGas |  |
| 205 | feisga | feisga | feis-ga | feisGa |  |
| 206 | thorwi | thorwif | thor-wif | thorWif |  |
| 207 | thorwi | thorwiw | thor-wiw | thorWiw |  |
| 208 | thorwi | thorwih | thor-wih | thorWih |  |
| 209 | thorwi | thorwis | thor-wis | thorWis |  |
| 210 | thorwi | thorwi | thor-wi | thorWi |  |
| 211 | jaeihne | jaeihnef | jaei-hnef | jaeiHnef |  |
| 212 | jaeihne | jaeihnew | jaei-hnew | jaeiHnew |  |
| 213 | jaeihne | jaeihneh | jaei-hneh | jaeiHneh |  |
| 214 | jaeihne | jaeihnes | jaei-hnes | jaeiHnes |  |
| 215 | jaeihne | jaeihne | jaei-hne | jaeiHne |  |
| 216 | neumhe | neumhef | neum-hef | neumHef |  |
| 217 | neumhe | neumhew | neum-hew | neumHew |  |
| 218 | neumhe | neumheh | neum-heh | neumHeh |  |
| 219 | neumhe | neumhes | neum-hes | neumHes |  |
| 220 | neumhe | neumhe | neum-he | neumHe |  |
| 221 | draeuthu | draeuthuf | draeu-thuf | draeuThuf | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 222 | draeuthu | draeuthuw | draeu-thuw | draeuThuw | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 223 | draeuthu | draeuthuh | draeu-thuh | draeuThuh | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 224 | draeuthu | draeuthus | draeu-thus | draeuThus | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 225 | draeuthu | draeuthu | draeu-thu | draeuThu | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 226 | braisngeu | braisngeuf | brais-ngeuf | braisNgeuf | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 227 | braisngeu | braisngeuw | brais-ngeuw | braisNgeuw | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 228 | braisngeu | braisngeuh | brais-ngeuh | braisNgeuh | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 229 | braisngeu | braisngeus | brais-ngeus | braisNgeus | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 230 | braisngeu | braisngeu | brais-ngeu | braisNgeu | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 231 | shesshaeu | shesshaeuf | shes-shaeuf | shesShaeuf | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 232 | shesshaeu | shesshaeuw | shes-shaeuw | shesShaeuw | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 233 | shesshaeu | shesshaeuh | shes-shaeuh | shesShaeuh | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 234 | shesshaeu | shesshaeus | shes-shaeus | shesShaeus | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 235 | shesshaeu | shesshaeu | shes-shaeu | shesShaeu | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 236 | graeiswau | graeiswauf | graeis-wauf | graeisWauf |  |
| 237 | graeiswau | graeiswauw | graeis-wauw | graeisWauw |  |
| 238 | graeiswau | graeiswauh | graeis-wauh | graeisWauh |  |
| 239 | graeiswau | graeiswaus | graeis-waus | graeisWaus |  |
| 240 | graeiswau | graeiswau | graeis-wau | graeisWau |  |


---

## What this sheet does NOT do

- It does not cover the **M3a seam** (a root-final `f` / `w` / `h` in front of a case suffix,
  always unstressed) - that layer is unjudged, see `../decision/03-open-questions.md` section 0
  item 20.
- It cannot show the **/n/ + /g/ (`nk`) class** of candidates: the pool was packed before `P6`
  existed and contains no `nk` spelling at all (`03-open-questions.md` section 0 item 24).
- It does not say which form is a good word. That is the pick, and it is yours to make.
