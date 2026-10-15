# data/generated/picks-sheet.md - GENERATED audition sheet. DO NOT ANNOTATE HERE.

Regenerate with:

```
python3 tools/syllabify.py --sheet > data/generated/picks-sheet.md
```

Any annotation written in this file is **lost** on regeneration. **Picks go in `data/hand/picks.md`.**
The numbers are **this sheet's own** sample of the current (post-P6) pool. ⚠️ A retired audio run of
2026-10-14 used a **different, frozen** pre-P6 sample: its numbers do NOT correspond to these, and the
synthesiser is rejected for good (`../../archive/README.md`).

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

Every group of 7 rows is ONE base: `+f` | `+w` (= /v/) | `+h` | `+s` | `+m` | `+r` | bare. A base yields
**exactly 2** roots, so pick **at most one** from the `{+f, +w}` pair and **at most one** from the
`{+h, +s, +m, +r, bare}` group. (`+s` is reserved for adjective/adverb duty, `+m` suits front-vowel
roots, `+r` is for function words -- **R4**/**R6**.)

> Sound-only. R3 is PARKED, so assign **no meanings** (../../docs/decisions/03-open-questions.md section 0
> item 14). A pick is not a word; `../../reference/example.md` stays the only source for examples.

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

Source: `data/generated/roots-bases-current.txt` (26769 packed bases); sample 48 bases, seed 20261014.
! A retired audio run of 2026-10-14 used a DIFFERENT sample
(the pre-P6 pool) and is frozen - its numbers are not comparable with these.

## roots-01.wav  (numbered 1-32)

| # | base | form | syllables | stress (P4/N1) | note |
|---|---|---|---|---|---|
| 1 | tharri | tharrif | thar-rif | tharRif |  |
| 2 | tharri | tharriw | thar-riw | tharRiw |  |
| 3 | tharri | tharrih | thar-rih | tharRih |  |
| 4 | tharri | tharris | thar-ris | tharRis |  |
| 5 | tharri | tharrim | thar-rim | tharRim |  |
| 6 | tharri | tharrir | thar-rir | tharRir |  |
| 7 | tharri | tharri | thar-ri | tharRi |  |
| 8 | naljau | naljauf | nal-jauf | nalJauf |  |
| 9 | naljau | naljauw | nal-jauw | nalJauw |  |
| 10 | naljau | naljauh | nal-jauh | nalJauh |  |
| 11 | naljau | naljaus | nal-jaus | nalJaus |  |
| 12 | naljau | naljaum | nal-jaum | nalJaum |  |
| 13 | naljau | naljaur | nal-jaur | nalJaur |  |
| 14 | naljau | naljau | nal-jau | nalJau |  |
| 15 | diwmy | diwmyf | di-wmyf | diWmyf |  |
| 16 | diwmy | diwmyw | di-wmyw | diWmyw |  |
| 17 | diwmy | diwmyh | di-wmyh | diWmyh |  |
| 18 | diwmy | diwmys | di-wmys | diWmys |  |
| 19 | diwmy | diwmym | di-wmym | diWmym |  |
| 20 | diwmy | diwmyr | di-wmyr | diWmyr |  |
| 21 | diwmy | diwmy | di-wmy | diWmy |  |
| 22 | sulsi | sulsif | sul-sif | sulSif |  |
| 23 | sulsi | sulsiw | sul-siw | sulSiw |  |
| 24 | sulsi | sulsih | sul-sih | sulSih |  |
| 25 | sulsi | sulsis | sul-sis | sulSis |  |
| 26 | sulsi | sulsim | sul-sim | sulSim |  |
| 27 | sulsi | sulsir | sul-sir | sulSir |  |
| 28 | sulsi | sulsi | sul-si | sulSi |  |
| 29 | thywe | thywef | thy-wef | thyWef |  |
| 30 | thywe | thywew | thy-wew | thyWew |  |
| 31 | thywe | thyweh | thy-weh | thyWeh |  |
| 32 | thywe | thywes | thy-wes | thyWes |  |
| 33 | thywe | thywem | thy-wem | thyWem |  |
| 34 | thywe | thywer | thy-wer | thyWer |  |
| 35 | thywe | thywe | thy-we | thyWe |  |
| 36 | daefno | daefnof | dae-fnof | daeFnof |  |
| 37 | daefno | daefnow | dae-fnow | daeFnow |  |
| 38 | daefno | daefnoh | dae-fnoh | daeFnoh |  |
| 39 | daefno | daefnos | dae-fnos | daeFnos |  |
| 40 | daefno | daefnom | dae-fnom | daeFnom |  |
| 41 | daefno | daefnor | dae-fnor | daeFnor |  |
| 42 | daefno | daefno | dae-fno | daeFno |  |
| 43 | wounmai | wounmaif | woun-maif | wounMaif |  |
| 44 | wounmai | wounmaiw | woun-maiw | wounMaiw |  |
| 45 | wounmai | wounmaih | woun-maih | wounMaih |  |
| 46 | wounmai | wounmais | woun-mais | wounMais |  |
| 47 | wounmai | wounmaim | woun-maim | wounMaim |  |
| 48 | wounmai | wounmair | woun-mair | wounMair |  |
| 49 | wounmai | wounmai | woun-mai | wounMai |  |
| 50 | leissau | leissauf | leis-sauf | leisSauf |  |
| 51 | leissau | leissauw | leis-sauw | leisSauw |  |
| 52 | leissau | leissauh | leis-sauh | leisSauh |  |
| 53 | leissau | leissaus | leis-saus | leisSaus |  |
| 54 | leissau | leissaum | leis-saum | leisSaum |  |
| 55 | leissau | leissaur | leis-saur | leisSaur |  |
| 56 | leissau | leissau | leis-sau | leisSau |  |

## roots-02.wav  (numbered 57-88)

| # | base | form | syllables | stress (P4/N1) | note |
|---|---|---|---|---|---|
| 57 | oigroi | oigroif | oi-groif | oiGroif |  |
| 58 | oigroi | oigroiw | oi-groiw | oiGroiw |  |
| 59 | oigroi | oigroih | oi-groih | oiGroih |  |
| 60 | oigroi | oigrois | oi-grois | oiGrois |  |
| 61 | oigroi | oigroim | oi-groim | oiGroim |  |
| 62 | oigroi | oigroir | oi-groir | oiGroir |  |
| 63 | oigroi | oigroi | oi-groi | oiGroi |  |
| 64 | maeidau | maeidauf | maei-dauf | maeiDauf |  |
| 65 | maeidau | maeidauw | maei-dauw | maeiDauw |  |
| 66 | maeidau | maeidauh | maei-dauh | maeiDauh |  |
| 67 | maeidau | maeidaus | maei-daus | maeiDaus |  |
| 68 | maeidau | maeidaum | maei-daum | maeiDaum |  |
| 69 | maeidau | maeidaur | maei-daur | maeiDaur |  |
| 70 | maeidau | maeidau | maei-dau | maeiDau |  |
| 71 | graeljou | graeljouf | grael-jouf | graelJouf |  |
| 72 | graeljou | graeljouw | grael-jouw | graelJouw |  |
| 73 | graeljou | graeljouh | grael-jouh | graelJouh |  |
| 74 | graeljou | graeljous | grael-jous | graelJous |  |
| 75 | graeljou | graeljoum | grael-joum | graelJoum |  |
| 76 | graeljou | graeljour | grael-jour | graelJour |  |
| 77 | graeljou | graeljou | grael-jou | graelJou |  |
| 78 | rourwae | rourwaef | rour-waef | rourWaef |  |
| 79 | rourwae | rourwaew | rour-waew | rourWaew |  |
| 80 | rourwae | rourwaeh | rour-waeh | rourWaeh |  |
| 81 | rourwae | rourwaes | rour-waes | rourWaes |  |
| 82 | rourwae | rourwaem | rour-waem | rourWaem |  |
| 83 | rourwae | rourwaer | rour-waer | rourWaer |  |
| 84 | rourwae | rourwae | rour-wae | rourWae |  |
| 85 | grorfu | grorfuf | gror-fuf | grorFuf |  |
| 86 | grorfu | grorfuw | gror-fuw | grorFuw |  |
| 87 | grorfu | grorfuh | gror-fuh | grorFuh |  |
| 88 | grorfu | grorfus | gror-fus | grorFus |  |
| 89 | grorfu | grorfum | gror-fum | grorFum |  |
| 90 | grorfu | grorfur | gror-fur | grorFur |  |
| 91 | grorfu | grorfu | gror-fu | grorFu |  |
| 92 | goulwau | goulwauf | goul-wauf | goulWauf |  |
| 93 | goulwau | goulwauw | goul-wauw | goulWauw |  |
| 94 | goulwau | goulwauh | goul-wauh | goulWauh |  |
| 95 | goulwau | goulwaus | goul-waus | goulWaus |  |
| 96 | goulwau | goulwaum | goul-waum | goulWaum |  |
| 97 | goulwau | goulwaur | goul-waur | goulWaur |  |
| 98 | goulwau | goulwau | goul-wau | goulWau |  |
| 99 | meumkou | meumkouf | meum-kouf | meumKouf | P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 100 | meumkou | meumkouw | meum-kouw | meumKouw | P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 101 | meumkou | meumkouh | meum-kouh | meumKouh | P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 102 | meumkou | meumkous | meum-kous | meumKous | P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 103 | meumkou | meumkoum | meum-koum | meumKoum | P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 104 | meumkou | meumkour | meum-kour | meumKour | P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 105 | meumkou | meumkou | meum-kou | meumKou | P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 106 | grimwaei | grimwaeif | grim-waeif | grimWaeif |  |
| 107 | grimwaei | grimwaeiw | grim-waeiw | grimWaeiw |  |
| 108 | grimwaei | grimwaeih | grim-waeih | grimWaeih |  |
| 109 | grimwaei | grimwaeis | grim-waeis | grimWaeis |  |
| 110 | grimwaei | grimwaeim | grim-waeim | grimWaeim |  |
| 111 | grimwaei | grimwaeir | grim-waeir | grimWaeir |  |
| 112 | grimwaei | grimwaei | grim-waei | grimWaei |  |

## roots-03.wav  (numbered 113-144)

| # | base | form | syllables | stress (P4/N1) | note |
|---|---|---|---|---|---|
| 113 | weusmo | weusmof | weus-mof | weusMof |  |
| 114 | weusmo | weusmow | weus-mow | weusMow |  |
| 115 | weusmo | weusmoh | weus-moh | weusMoh |  |
| 116 | weusmo | weusmos | weus-mos | weusMos |  |
| 117 | weusmo | weusmom | weus-mom | weusMom |  |
| 118 | weusmo | weusmor | weus-mor | weusMor |  |
| 119 | weusmo | weusmo | weus-mo | weusMo |  |
| 120 | daeijae | daeijaef | daei-jaef | daeiJaef |  |
| 121 | daeijae | daeijaew | daei-jaew | daeiJaew |  |
| 122 | daeijae | daeijaeh | daei-jaeh | daeiJaeh |  |
| 123 | daeijae | daeijaes | daei-jaes | daeiJaes |  |
| 124 | daeijae | daeijaem | daei-jaem | daeiJaem |  |
| 125 | daeijae | daeijaer | daei-jaer | daeiJaer |  |
| 126 | daeijae | daeijae | daei-jae | daeiJae |  |
| 127 | nahmu | nahmuf | na-hmuf | naHmuf |  |
| 128 | nahmu | nahmuw | na-hmuw | naHmuw |  |
| 129 | nahmu | nahmuh | na-hmuh | naHmuh |  |
| 130 | nahmu | nahmus | na-hmus | naHmus |  |
| 131 | nahmu | nahmum | na-hmum | naHmum |  |
| 132 | nahmu | nahmur | na-hmur | naHmur |  |
| 133 | nahmu | nahmu | na-hmu | naHmu |  |
| 134 | jeicoi | jeicoif | jei-coif | jeiCoif |  |
| 135 | jeicoi | jeicoiw | jei-coiw | jeiCoiw |  |
| 136 | jeicoi | jeicoih | jei-coih | jeiCoih |  |
| 137 | jeicoi | jeicois | jei-cois | jeiCois |  |
| 138 | jeicoi | jeicoim | jei-coim | jeiCoim |  |
| 139 | jeicoi | jeicoir | jei-coir | jeiCoir |  |
| 140 | jeicoi | jeicoi | jei-coi | jeiCoi |  |
| 141 | wunnge | wunngef | wun-ngef | wunNgef | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 142 | wunnge | wunngew | wun-ngew | wunNgew | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 143 | wunnge | wunngeh | wun-ngeh | wunNgeh | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 144 | wunnge | wunnges | wun-nges | wunNges | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 145 | wunnge | wunngem | wun-ngem | wunNgem | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 146 | wunnge | wunnger | wun-nger | wunNger | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 147 | wunnge | wunnge | wun-nge | wunNge | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 148 | gihoi | gihoif | gi-hoif | giHoif |  |
| 149 | gihoi | gihoiw | gi-hoiw | giHoiw |  |
| 150 | gihoi | gihoih | gi-hoih | giHoih |  |
| 151 | gihoi | gihois | gi-hois | giHois |  |
| 152 | gihoi | gihoim | gi-hoim | giHoim |  |
| 153 | gihoi | gihoir | gi-hoir | giHoir |  |
| 154 | gihoi | gihoi | gi-hoi | giHoi |  |
| 155 | jimji | jimjif | jim-jif | jimJif |  |
| 156 | jimji | jimjiw | jim-jiw | jimJiw |  |
| 157 | jimji | jimjih | jim-jih | jimJih |  |
| 158 | jimji | jimjis | jim-jis | jimJis |  |
| 159 | jimji | jimjim | jim-jim | jimJim |  |
| 160 | jimji | jimjir | jim-jir | jimJir |  |
| 161 | jimji | jimji | jim-ji | jimJi |  |
| 162 | jaurmy | jaurmyf | jaur-myf | jaurMyf |  |
| 163 | jaurmy | jaurmyw | jaur-myw | jaurMyw |  |
| 164 | jaurmy | jaurmyh | jaur-myh | jaurMyh |  |
| 165 | jaurmy | jaurmys | jaur-mys | jaurMys |  |
| 166 | jaurmy | jaurmym | jaur-mym | jaurMym |  |
| 167 | jaurmy | jaurmyr | jaur-myr | jaurMyr |  |
| 168 | jaurmy | jaurmy | jaur-my | jaurMy |  |

## roots-04.wav  (numbered 169-200)

| # | base | form | syllables | stress (P4/N1) | note |
|---|---|---|---|---|---|
| 169 | fojnoi | fojnoif | fo-jnoif | foJnoif |  |
| 170 | fojnoi | fojnoiw | fo-jnoiw | foJnoiw |  |
| 171 | fojnoi | fojnoih | fo-jnoih | foJnoih |  |
| 172 | fojnoi | fojnois | fo-jnois | foJnois |  |
| 173 | fojnoi | fojnoim | fo-jnoim | foJnoim |  |
| 174 | fojnoi | fojnoir | fo-jnoir | foJnoir |  |
| 175 | fojnoi | fojnoi | fo-jnoi | foJnoi |  |
| 176 | eimeu | eimeuf | ei-meuf | eiMeuf |  |
| 177 | eimeu | eimeuw | ei-meuw | eiMeuw |  |
| 178 | eimeu | eimeuh | ei-meuh | eiMeuh |  |
| 179 | eimeu | eimeus | ei-meus | eiMeus |  |
| 180 | eimeu | eimeum | ei-meum | eiMeum |  |
| 181 | eimeu | eimeur | ei-meur | eiMeur |  |
| 182 | eimeu | eimeu | ei-meu | eiMeu |  |
| 183 | bysngeu | bysngeuf | bys-ngeuf | bysNgeuf | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 184 | bysngeu | bysngeuw | bys-ngeuw | bysNgeuw | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 185 | bysngeu | bysngeuh | bys-ngeuh | bysNgeuh | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 186 | bysngeu | bysngeus | bys-ngeus | bysNgeus | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 187 | bysngeu | bysngeum | bys-ngeum | bysNgeum | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 188 | bysngeu | bysngeur | bys-ngeur | bysNgeur | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 189 | bysngeu | bysngeu | bys-ngeu | bysNgeu | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 190 | shausrei | shausreif | shaus-reif | shausReif |  |
| 191 | shausrei | shausreiw | shaus-reiw | shausReiw |  |
| 192 | shausrei | shausreih | shaus-reih | shausReih |  |
| 193 | shausrei | shausreis | shaus-reis | shausReis |  |
| 194 | shausrei | shausreim | shaus-reim | shausReim |  |
| 195 | shausrei | shausreir | shaus-reir | shausReir |  |
| 196 | shausrei | shausrei | shaus-rei | shausRei |  |
| 197 | josshoi | josshoif | jos-shoif | josShoif | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 198 | josshoi | josshoiw | jos-shoiw | josShoiw | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 199 | josshoi | josshoih | jos-shoih | josShoih | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 200 | josshoi | josshois | jos-shois | josShois | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 201 | josshoi | josshoim | jos-shoim | josShoim | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 202 | josshoi | josshoir | jos-shoir | josShoir | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 203 | josshoi | josshoi | jos-shoi | josShoi | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 204 | sheisme | sheismef | sheis-mef | sheisMef |  |
| 205 | sheisme | sheismew | sheis-mew | sheisMew |  |
| 206 | sheisme | sheismeh | sheis-meh | sheisMeh |  |
| 207 | sheisme | sheismes | sheis-mes | sheisMes |  |
| 208 | sheisme | sheismem | sheis-mem | sheisMem |  |
| 209 | sheisme | sheismer | sheis-mer | sheisMer |  |
| 210 | sheisme | sheisme | sheis-me | sheisMe |  |
| 211 | gommi | gommif | gom-mif | gomMif |  |
| 212 | gommi | gommiw | gom-miw | gomMiw |  |
| 213 | gommi | gommih | gom-mih | gomMih |  |
| 214 | gommi | gommis | gom-mis | gomMis |  |
| 215 | gommi | gommim | gom-mim | gomMim |  |
| 216 | gommi | gommir | gom-mir | gomMir |  |
| 217 | gommi | gommi | gom-mi | gomMi |  |
| 218 | seimsei | seimseif | seim-seif | seimSeif |  |
| 219 | seimsei | seimseiw | seim-seiw | seimSeiw |  |
| 220 | seimsei | seimseih | seim-seih | seimSeih |  |
| 221 | seimsei | seimseis | seim-seis | seimSeis |  |
| 222 | seimsei | seimseim | seim-seim | seimSeim |  |
| 223 | seimsei | seimseir | seim-seir | seimSeir |  |
| 224 | seimsei | seimsei | seim-sei | seimSei |  |

## roots-05.wav  (numbered 225-256)

| # | base | form | syllables | stress (P4/N1) | note |
|---|---|---|---|---|---|
| 225 | mamma | mammaf | mam-maf | mamMaf |  |
| 226 | mamma | mammaw | mam-maw | mamMaw |  |
| 227 | mamma | mammah | mam-mah | mamMah |  |
| 228 | mamma | mammas | mam-mas | mamMas |  |
| 229 | mamma | mammam | mam-mam | mamMam |  |
| 230 | mamma | mammar | mam-mar | mamMar |  |
| 231 | mamma | mamma | mam-ma | mamMa |  |
| 232 | welsa | welsaf | wel-saf | welSaf |  |
| 233 | welsa | welsaw | wel-saw | welSaw |  |
| 234 | welsa | welsah | wel-sah | welSah |  |
| 235 | welsa | welsas | wel-sas | welSas |  |
| 236 | welsa | welsam | wel-sam | welSam |  |
| 237 | welsa | welsar | wel-sar | welSar |  |
| 238 | welsa | welsa | wel-sa | welSa |  |
| 239 | rocau | rocauf | ro-cauf | roCauf |  |
| 240 | rocau | rocauw | ro-cauw | roCauw |  |
| 241 | rocau | rocauh | ro-cauh | roCauh |  |
| 242 | rocau | rocaus | ro-caus | roCaus |  |
| 243 | rocau | rocaum | ro-caum | roCaum |  |
| 244 | rocau | rocaur | ro-caur | roCaur |  |
| 245 | rocau | rocau | ro-cau | roCau |  |
| 246 | nunko | nunkof | nun-kof | nunKof | P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 247 | nunko | nunkow | nun-kow | nunKow | P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 248 | nunko | nunkoh | nun-koh | nunKoh | P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 249 | nunko | nunkos | nun-kos | nunKos | P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 250 | nunko | nunkom | nun-kom | nunKom | P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 251 | nunko | nunkor | nun-kor | nunKor | P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 252 | nunko | nunko | nun-ko | nunKo | P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 253 | ronae | ronaef | ro-naef | roNaef |  |
| 254 | ronae | ronaew | ro-naew | roNaew |  |
| 255 | ronae | ronaeh | ro-naeh | roNaeh |  |
| 256 | ronae | ronaes | ro-naes | roNaes |  |
| 257 | ronae | ronaem | ro-naem | roNaem |  |
| 258 | ronae | ronaer | ro-naer | roNaer |  |
| 259 | ronae | ronae | ro-nae | roNae |  |
| 260 | hoimno | hoimnof | hoim-nof | hoimNof |  |
| 261 | hoimno | hoimnow | hoim-now | hoimNow |  |
| 262 | hoimno | hoimnoh | hoim-noh | hoimNoh |  |
| 263 | hoimno | hoimnos | hoim-nos | hoimNos |  |
| 264 | hoimno | hoimnom | hoim-nom | hoimNom |  |
| 265 | hoimno | hoimnor | hoim-nor | hoimNor |  |
| 266 | hoimno | hoimno | hoim-no | hoimNo |  |
| 267 | gonfei | gonfeif | gon-feif | gonFeif |  |
| 268 | gonfei | gonfeiw | gon-feiw | gonFeiw |  |
| 269 | gonfei | gonfeih | gon-feih | gonFeih |  |
| 270 | gonfei | gonfeis | gon-feis | gonFeis |  |
| 271 | gonfei | gonfeim | gon-feim | gonFeim |  |
| 272 | gonfei | gonfeir | gon-feir | gonFeir |  |
| 273 | gonfei | gonfei | gon-fei | gonFei |  |
| 274 | waufy | waufyf | wau-fyf | wauFyf |  |
| 275 | waufy | waufyw | wau-fyw | wauFyw |  |
| 276 | waufy | waufyh | wau-fyh | wauFyh |  |
| 277 | waufy | waufys | wau-fys | wauFys |  |
| 278 | waufy | waufym | wau-fym | wauFym |  |
| 279 | waufy | waufyr | wau-fyr | wauFyr |  |
| 280 | waufy | waufy | wau-fy | wauFy |  |

## roots-06.wav  (numbered 281-312)

| # | base | form | syllables | stress (P4/N1) | note |
|---|---|---|---|---|---|
| 281 | feisga | feisgaf | feis-gaf | feisGaf |  |
| 282 | feisga | feisgaw | feis-gaw | feisGaw |  |
| 283 | feisga | feisgah | feis-gah | feisGah |  |
| 284 | feisga | feisgas | feis-gas | feisGas |  |
| 285 | feisga | feisgam | feis-gam | feisGam |  |
| 286 | feisga | feisgar | feis-gar | feisGar |  |
| 287 | feisga | feisga | feis-ga | feisGa |  |
| 288 | thorwi | thorwif | thor-wif | thorWif |  |
| 289 | thorwi | thorwiw | thor-wiw | thorWiw |  |
| 290 | thorwi | thorwih | thor-wih | thorWih |  |
| 291 | thorwi | thorwis | thor-wis | thorWis |  |
| 292 | thorwi | thorwim | thor-wim | thorWim |  |
| 293 | thorwi | thorwir | thor-wir | thorWir |  |
| 294 | thorwi | thorwi | thor-wi | thorWi |  |
| 295 | jaeihne | jaeihnef | jaei-hnef | jaeiHnef |  |
| 296 | jaeihne | jaeihnew | jaei-hnew | jaeiHnew |  |
| 297 | jaeihne | jaeihneh | jaei-hneh | jaeiHneh |  |
| 298 | jaeihne | jaeihnes | jaei-hnes | jaeiHnes |  |
| 299 | jaeihne | jaeihnem | jaei-hnem | jaeiHnem |  |
| 300 | jaeihne | jaeihner | jaei-hner | jaeiHner |  |
| 301 | jaeihne | jaeihne | jaei-hne | jaeiHne |  |
| 302 | neumhe | neumhef | neum-hef | neumHef |  |
| 303 | neumhe | neumhew | neum-hew | neumHew |  |
| 304 | neumhe | neumheh | neum-heh | neumHeh |  |
| 305 | neumhe | neumhes | neum-hes | neumHes |  |
| 306 | neumhe | neumhem | neum-hem | neumHem |  |
| 307 | neumhe | neumher | neum-her | neumHer |  |
| 308 | neumhe | neumhe | neum-he | neumHe |  |
| 309 | draeuthu | draeuthuf | draeu-thuf | draeuThuf | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 310 | draeuthu | draeuthuw | draeu-thuw | draeuThuw | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 311 | draeuthu | draeuthuh | draeu-thuh | draeuThuh | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 312 | draeuthu | draeuthus | draeu-thus | draeuThus | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 313 | draeuthu | draeuthum | draeu-thum | draeuThum | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 314 | draeuthu | draeuthur | draeu-thur | draeuThur | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 315 | draeuthu | draeuthu | draeu-thu | draeuThu | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 316 | braisngeu | braisngeuf | brais-ngeuf | braisNgeuf | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 317 | braisngeu | braisngeuw | brais-ngeuw | braisNgeuw | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 318 | braisngeu | braisngeuh | brais-ngeuh | braisNgeuh | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 319 | braisngeu | braisngeus | brais-ngeus | braisNgeus | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 320 | braisngeu | braisngeum | brais-ngeum | braisNgeum | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 321 | braisngeu | braisngeur | brais-ngeur | braisNgeur | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 322 | braisngeu | braisngeu | brais-ngeu | braisNgeu | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 323 | shesshaeu | shesshaeuf | shes-shaeuf | shesShaeuf | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 324 | shesshaeu | shesshaeuw | shes-shaeuw | shesShaeuw | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 325 | shesshaeu | shesshaeuh | shes-shaeuh | shesShaeuh | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 326 | shesshaeu | shesshaeus | shes-shaeus | shesShaeus | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 327 | shesshaeu | shesshaeum | shes-shaeum | shesShaeum | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 328 | shesshaeu | shesshaeur | shes-shaeur | shesShaeur | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 329 | shesshaeu | shesshaeu | shes-shaeu | shesShaeu | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 330 | graeiswau | graeiswauf | graeis-wauf | graeisWauf |  |
| 331 | graeiswau | graeiswauw | graeis-wauw | graeisWauw |  |
| 332 | graeiswau | graeiswauh | graeis-wauh | graeisWauh |  |
| 333 | graeiswau | graeiswaus | graeis-waus | graeisWaus |  |
| 334 | graeiswau | graeiswaum | graeis-waum | graeisWaum |  |
| 335 | graeiswau | graeiswaur | graeis-waur | graeisWaur |  |
| 336 | graeiswau | graeiswau | graeis-wau | graeisWau |  |


---

## What this sheet does NOT do

- It does not cover the **M3a seam** (a root-final `f` / `w` / `h` in front of a case suffix,
  always unstressed) - that layer is unjudged, see `../docs/decisions/03-open-questions.md` section 0
  item 20.
- It cannot show the **/n/ + /g/ (`nk`) class** of candidates: the pool was packed before `P6`
  existed and contains no `nk` spelling at all (`../../docs/decisions/03-open-questions.md` section 0 item 24).
- It does not say which form is a good word. That is the pick, and it is yours to make.
