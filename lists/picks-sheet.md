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

Source: `lists/roots-bases-current.txt` (26484 packed bases); sample 48 bases, seed 20261014.
! The audio run of 2026-10-14 (`../audio/roots-index.txt`) used a DIFFERENT sample
(the pre-P6 pool) and is frozen - its numbers are not comparable with these.

## roots-01.wav  (numbered 1-32)

| # | base | form | syllables | stress (P4/N1) | note |
|---|---|---|---|---|---|
| 1 | thaeumto | thaeumtof | thaeum-tof | thaeumTof | P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 2 | thaeumto | thaeumtow | thaeum-tow | thaeumTow | P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 3 | thaeumto | thaeumtoh | thaeum-toh | thaeumToh | P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 4 | thaeumto | thaeumto | thaeum-to | thaeumTo | P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 5 | naeilrou | naeilrouf | naeil-rouf | naeilRouf |  |
| 6 | naeilrou | naeilrouw | naeil-rouw | naeilRouw |  |
| 7 | naeilrou | naeilrouh | naeil-rouh | naeilRouh |  |
| 8 | naeilrou | naeilrou | naeil-rou | naeilRou |  |
| 9 | donwoi | donwoif | don-woif | donWoif |  |
| 10 | donwoi | donwoiw | don-woiw | donWoiw |  |
| 11 | donwoi | donwoih | don-woih | donWoih |  |
| 12 | donwoi | donwoi | don-woi | donWoi |  |
| 13 | shasgeu | shasgeuf | shas-geuf | shasGeuf |  |
| 14 | shasgeu | shasgeuw | shas-geuw | shasGeuw |  |
| 15 | shasgeu | shasgeuh | shas-geuh | shasGeuh |  |
| 16 | shasgeu | shasgeu | shas-geu | shasGeu |  |
| 17 | waesgei | waesgeif | waes-geif | waesGeif |  |
| 18 | waesgei | waesgeiw | waes-geiw | waesGeiw |  |
| 19 | waesgei | waesgeih | waes-geih | waesGeih |  |
| 20 | waesgei | waesgei | waes-gei | waesGei |  |
| 21 | daengou | daengouf | dae-ngouf | daeNgouf | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 22 | daengou | daengouw | dae-ngouw | daeNgouw | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 23 | daengou | daengouh | dae-ngouh | daeNgouh | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 24 | daengou | daengou | dae-ngou | daeNgou | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 25 | yrgy | yrgyf | yr-gyf | yrGyf |  |
| 26 | yrgy | yrgyw | yr-gyw | yrGyw |  |
| 27 | yrgy | yrgyh | yr-gyh | yrGyh |  |
| 28 | yrgy | yrgy | yr-gy | yrGy |  |
| 29 | lirlai | lirlaif | lir-laif | lirLaif |  |
| 30 | lirlai | lirlaiw | lir-laiw | lirLaiw |  |
| 31 | lirlai | lirlaih | lir-laih | lirLaih |  |
| 32 | lirlai | lirlai | lir-lai | lirLai |  |

## roots-02.wav  (numbered 33-64)

| # | base | form | syllables | stress (P4/N1) | note |
|---|---|---|---|---|---|
| 33 | ralsaei | ralsaeif | ral-saeif | ralSaeif |  |
| 34 | ralsaei | ralsaeiw | ral-saeiw | ralSaeiw |  |
| 35 | ralsaei | ralsaeih | ral-saeih | ralSaeih |  |
| 36 | ralsaei | ralsaei | ral-saei | ralSaei |  |
| 37 | maeusshaei | maeusshaeif | maeus-shaeif | maeusShaeif | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 38 | maeusshaei | maeusshaeiw | maeus-shaeiw | maeusShaeiw | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 39 | maeusshaei | maeusshaeih | maeus-shaeih | maeusShaeih | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 40 | maeusshaei | maeusshaei | maeus-shaei | maeusShaei | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 41 | graeimthae | graeimthaef | graeim-thaef | graeimThaef | stress capital lands on a DIGRAPH (convention OPEN: 03 section C); P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 42 | graeimthae | graeimthaew | graeim-thaew | graeimThaew | stress capital lands on a DIGRAPH (convention OPEN: 03 section C); P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 43 | graeimthae | graeimthaeh | graeim-thaeh | graeimThaeh | stress capital lands on a DIGRAPH (convention OPEN: 03 section C); P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 44 | graeimthae | graeimthae | graeim-thae | graeimThae | stress capital lands on a DIGRAPH (convention OPEN: 03 section C); P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 45 | sajmeu | sajmeuf | sa-jmeuf | saJmeuf |  |
| 46 | sajmeu | sajmeuw | sa-jmeuw | saJmeuw |  |
| 47 | sajmeu | sajmeuh | sa-jmeuh | saJmeuh |  |
| 48 | sajmeu | sajmeu | sa-jmeu | saJmeu |  |
| 49 | groubrou | groubrouf | grou-brouf | grouBrouf |  |
| 50 | groubrou | groubrouw | grou-brouw | grouBrouw |  |
| 51 | groubrou | groubrouh | grou-brouh | grouBrouh |  |
| 52 | groubrou | groubrou | grou-brou | grouBrou |  |
| 53 | gunlo | gunlof | gun-lof | gunLof |  |
| 54 | gunlo | gunlow | gun-low | gunLow |  |
| 55 | gunlo | gunloh | gun-loh | gunLoh |  |
| 56 | gunlo | gunlo | gun-lo | gunLo |  |
| 57 | momheu | momheuf | mom-heuf | momHeuf |  |
| 58 | momheu | momheuw | mom-heuw | momHeuw |  |
| 59 | momheu | momheuh | mom-heuh | momHeuh |  |
| 60 | momheu | momheu | mom-heu | momHeu |  |
| 61 | groseu | groseuf | gro-seuf | groSeuf |  |
| 62 | groseu | groseuw | gro-seuw | groSeuw |  |
| 63 | groseu | groseuh | gro-seuh | groSeuh |  |
| 64 | groseu | groseu | gro-seu | groSeu |  |

## roots-03.wav  (numbered 65-96)

| # | base | form | syllables | stress (P4/N1) | note |
|---|---|---|---|---|---|
| 65 | woisjaeu | woisjaeuf | wois-jaeuf | woisJaeuf |  |
| 66 | woisjaeu | woisjaeuw | wois-jaeuw | woisJaeuw |  |
| 67 | woisjaeu | woisjaeuh | wois-jaeuh | woisJaeuh |  |
| 68 | woisjaeu | woisjaeu | wois-jaeu | woisJaeu |  |
| 69 | daeirnau | daeirnauf | daeir-nauf | daeirNauf |  |
| 70 | daeirnau | daeirnauw | daeir-nauw | daeirNauw |  |
| 71 | daeirnau | daeirnauh | daeir-nauh | daeirNauh |  |
| 72 | daeirnau | daeirnau | daeir-nau | daeirNau |  |
| 73 | naeilbei | naeilbeif | naeil-beif | naeilBeif |  |
| 74 | naeilbei | naeilbeiw | naeil-beiw | naeilBeiw |  |
| 75 | naeilbei | naeilbeih | naeil-beih | naeilBeih |  |
| 76 | naeilbei | naeilbei | naeil-bei | naeilBei |  |
| 77 | jeungeu | jeungeuf | jeu-ngeuf | jeuNgeuf | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 78 | jeungeu | jeungeuw | jeu-ngeuw | jeuNgeuw | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 79 | jeungeu | jeungeuh | jeu-ngeuh | jeuNgeuh | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 80 | jeungeu | jeungeu | jeu-ngeu | jeuNgeu | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 81 | golsoi | golsoif | gol-soif | golSoif |  |
| 82 | golsoi | golsoiw | gol-soiw | golSoiw |  |
| 83 | golsoi | golsoih | gol-soih | golSoih |  |
| 84 | golsoi | golsoi | gol-soi | golSoi |  |
| 85 | joicei | joiceif | joi-ceif | joiCeif |  |
| 86 | joicei | joiceiw | joi-ceiw | joiCeiw |  |
| 87 | joicei | joiceih | joi-ceih | joiCeih |  |
| 88 | joicei | joicei | joi-cei | joiCei |  |
| 89 | jeimjei | jeimjeif | jeim-jeif | jeimJeif |  |
| 90 | jeimjei | jeimjeiw | jeim-jeiw | jeimJeiw |  |
| 91 | jeimjei | jeimjeih | jeim-jeih | jeimJeih |  |
| 92 | jeimjei | jeimjei | jeim-jei | jeimJei |  |
| 93 | foildo | foildof | foil-dof | foilDof |  |
| 94 | foildo | foildow | foil-dow | foilDow |  |
| 95 | foildo | foildoh | foil-doh | foilDoh |  |
| 96 | foildo | foildo | foil-do | foilDo |  |

## roots-04.wav  (numbered 97-128)

| # | base | form | syllables | stress (P4/N1) | note |
|---|---|---|---|---|---|
| 97 | eulhu | eulhuf | eul-huf | eulHuf |  |
| 98 | eulhu | eulhuw | eul-huw | eulHuw |  |
| 99 | eulhu | eulhuh | eul-huh | eulHuh |  |
| 100 | eulhu | eulhu | eul-hu | eulHu |  |
| 101 | brahma | brahmaf | bra-hmaf | braHmaf |  |
| 102 | brahma | brahmaw | bra-hmaw | braHmaw |  |
| 103 | brahma | brahmah | bra-hmah | braHmah |  |
| 104 | brahma | brahma | bra-hma | braHma |  |
| 105 | sheunheu | sheunheuf | sheun-heuf | sheunHeuf |  |
| 106 | sheunheu | sheunheuw | sheun-heuw | sheunHeuw |  |
| 107 | sheunheu | sheunheuh | sheun-heuh | sheunHeuh |  |
| 108 | sheunheu | sheunheu | sheun-heu | sheunHeu |  |
| 109 | jounpe | jounpef | joun-pef | jounPef | P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 110 | jounpe | jounpew | joun-pew | jounPew | P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 111 | jounpe | jounpeh | joun-peh | jounPeh | P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 112 | jounpe | jounpe | joun-pe | jounPe | P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 113 | shonshi | shonshif | shon-shif | shonShif | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 114 | shonshi | shonshiw | shon-shiw | shonShiw | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 115 | shonshi | shonshih | shon-shih | shonShih | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 116 | shonshi | shonshi | shon-shi | shonShi | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 117 | goinngy | goinngyf | goin-ngyf | goinNgyf | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 118 | goinngy | goinngyw | goin-ngyw | goinNgyw | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 119 | goinngy | goinngyh | goin-ngyh | goinNgyh | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 120 | goinngy | goinngy | goin-ngy | goinNgy | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 121 | sisshei | sissheif | sis-sheif | sisSheif | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 122 | sisshei | sissheiw | sis-sheiw | sisSheiw | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 123 | sisshei | sissheih | sis-sheih | sisSheih | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 124 | sisshei | sisshei | sis-shei | sisShei | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 125 | maeilsha | maeilshaf | maeil-shaf | maeilShaf | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 126 | maeilsha | maeilshaw | maeil-shaw | maeilShaw | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 127 | maeilsha | maeilshah | maeil-shah | maeilShah | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |
| 128 | maeilsha | maeilsha | maeil-sha | maeilSha | stress capital lands on a DIGRAPH (convention OPEN: 03 section C) |

## roots-05.wav  (numbered 129-160)

| # | base | form | syllables | stress (P4/N1) | note |
|---|---|---|---|---|---|
| 129 | willu | willuf | wil-luf | wilLuf |  |
| 130 | willu | willuw | wil-luw | wilLuw |  |
| 131 | willu | willuh | wil-luh | wilLuh |  |
| 132 | willu | willu | wil-lu | wilLu |  |
| 133 | roumju | roumjuf | roum-juf | roumJuf |  |
| 134 | roumju | roumjuw | roum-juw | roumJuw |  |
| 135 | roumju | roumjuh | roum-juh | roumJuh |  |
| 136 | roumju | roumju | roum-ju | roumJu |  |
| 137 | orlai | orlaif | or-laif | orLaif |  |
| 138 | orlai | orlaiw | or-laiw | orLaiw |  |
| 139 | orlai | orlaih | or-laih | orLaih |  |
| 140 | orlai | orlai | or-lai | orLai |  |
| 141 | rousjy | rousjyf | rous-jyf | rousJyf |  |
| 142 | rousjy | rousjyw | rous-jyw | rousJyw |  |
| 143 | rousjy | rousjyh | rous-jyh | rousJyh |  |
| 144 | rousjy | rousjy | rous-jy | rousJy |  |
| 145 | housroi | housroif | hous-roif | housRoif |  |
| 146 | housroi | housroiw | hous-roiw | housRoiw |  |
| 147 | housroi | housroih | hous-roih | housRoih |  |
| 148 | housroi | housroi | hous-roi | housRoi |  |
| 149 | goirbeu | goirbeuf | goir-beuf | goirBeuf |  |
| 150 | goirbeu | goirbeuw | goir-beuw | goirBeuw |  |
| 151 | goirbeu | goirbeuh | goir-beuh | goirBeuh |  |
| 152 | goirbeu | goirbeu | goir-beu | goirBeu |  |
| 153 | weiwau | weiwauf | wei-wauf | weiWauf |  |
| 154 | weiwau | weiwauw | wei-wauw | weiWauw |  |
| 155 | weiwau | weiwauh | wei-wauh | weiWauh |  |
| 156 | weiwau | weiwau | wei-wau | weiWau |  |
| 157 | feusfy | feusfyf | feus-fyf | feusFyf |  |
| 158 | feusfy | feusfyw | feus-fyw | feusFyw |  |
| 159 | feusfy | feusfyh | feus-fyh | feusFyh |  |
| 160 | feusfy | feusfy | feus-fy | feusFy |  |

## roots-06.wav  (numbered 161-192)

| # | base | form | syllables | stress (P4/N1) | note |
|---|---|---|---|---|---|
| 161 | thunthi | thunthif | thun-thif | thunThif | stress capital lands on a DIGRAPH (convention OPEN: 03 section C); P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 162 | thunthi | thunthiw | thun-thiw | thunThiw | stress capital lands on a DIGRAPH (convention OPEN: 03 section C); P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 163 | thunthi | thunthih | thun-thih | thunThih | stress capital lands on a DIGRAPH (convention OPEN: 03 section C); P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 164 | thunthi | thunthi | thun-thi | thunThi | stress capital lands on a DIGRAPH (convention OPEN: 03 section C); P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 165 | jaeuri | jaeurif | jaeu-rif | jaeuRif |  |
| 166 | jaeuri | jaeuriw | jaeu-riw | jaeuRiw |  |
| 167 | jaeuri | jaeurih | jaeu-rih | jaeuRih |  |
| 168 | jaeuri | jaeuri | jaeu-ri | jaeuRi |  |
| 169 | nomu | nomuf | no-muf | noMuf |  |
| 170 | nomu | nomuw | no-muw | noMuw |  |
| 171 | nomu | nomuh | no-muh | noMuh |  |
| 172 | nomu | nomu | no-mu | noMu |  |
| 173 | drairgai | drairgaif | drair-gaif | drairGaif |  |
| 174 | drairgai | drairgaiw | drair-gaiw | drairGaiw |  |
| 175 | drairgai | drairgaih | drair-gaih | drairGaih |  |
| 176 | drairgai | drairgai | drair-gai | drairGai |  |
| 177 | braulbei | braulbeif | braul-beif | braulBeif |  |
| 178 | braulbei | braulbeiw | braul-beiw | braulBeiw |  |
| 179 | braulbei | braulbeih | braul-beih | braulBeih |  |
| 180 | braulbei | braulbei | braul-bei | braulBei |  |
| 181 | shinthe | shinthef | shin-thef | shinThef | stress capital lands on a DIGRAPH (convention OPEN: 03 section C); P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 182 | shinthe | shinthew | shin-thew | shinThew | stress capital lands on a DIGRAPH (convention OPEN: 03 section C); P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 183 | shinthe | shintheh | shin-theh | shinTheh | stress capital lands on a DIGRAPH (convention OPEN: 03 section C); P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 184 | shinthe | shinthe | shin-the | shinThe | stress capital lands on a DIGRAPH (convention OPEN: 03 section C); P6: nasal coda + stop = obligatorily [p t k] (the soft/hard knob does not apply) |
| 185 | grailcoi | grailcoif | grail-coif | grailCoif |  |
| 186 | grailcoi | grailcoiw | grail-coiw | grailCoiw |  |
| 187 | grailcoi | grailcoih | grail-coih | grailCoih |  |
| 188 | grailcoi | grailcoi | grail-coi | grailCoi |  |
| 189 | drisse | drissef | dris-sef | drisSef |  |
| 190 | drisse | drissew | dris-sew | drisSew |  |
| 191 | drisse | drisseh | dris-seh | drisSeh |  |
| 192 | drisse | drisse | dris-se | drisSe |  |


---

## What this sheet does NOT do

- It does not cover the **M3a seam** (a root-final `f` / `w` / `h` in front of a case suffix,
  always unstressed) - that layer is unjudged, see `../decision/03-open-questions.md` section 0
  item 20.
- It cannot show the **/n/ + /g/ (`nk`) class** of candidates: the pool was packed before `P6`
  existed and contains no `nk` spelling at all (`03-open-questions.md` section 0 item 24).
- It does not say which form is a good word. That is the pick, and it is yours to make.
