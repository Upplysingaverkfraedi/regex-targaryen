## 1. Leita að kennitölu:

Skrifið tvær reglulegar segðir til að finna kennitölur einstaklinga og fyrirtækja í texta.
Skrifið Python kóða sem leitar að kennitölum samkvæmt reglulegu segðunum og prentar niðurstöðurnar.
Keyrið kóðann með valmöguleikum til að leita annað hvort af einstaklinga, fyrirtækja eða báðum í einu.

### Svar: 

**Til að finna kennitölur einstaklinga.**

Kennitölur einstaklinga eru byggðar svona upp: 
Fæðingardagur: Sex fyrstu tölustafir kennitölunnar sýna dag, mánuð og ár (DDMMYY).
Raðtala: Tveir næstu tölustafir (stafir 7 og 8) eru raðtala sem er úthlutað í röð frá og með 20.
Vartala: Næsti tölustafur (stafur 9) er vartala sem reiknast út með Modulus 11 aðferð og getur verið frá 0 til 9.
Aldur: Aftasti tölustafurinn (stafur 10) gefur til kynna öldina sem viðkomandi er fæddur á, og getur verið 8, 9 eða 0 (t.d. 0 fyrir 2000-2099, 9 fyrir 1900-1999).

#### Reglulega segðin:
\b[0123]\d{1}[012]\d{3}-[2-9]\d{2}[8-9|0]\b

\b orðaskil
[0123] fyrsti stafurinn er 0, 1, 2 eða 3
\d{1} næsti tölustafur er frá 0-9
[012] næsti tölustafur er 0, 1 eða 2 því allir mánuðir byrja á því
\d{3} einhver tala frá 0-9 því þetta er seinni mánaðartalan sem getur verið 0-9. og so eru 2 tölur fyrir árið sem er líka frá 0-9
- svo er bandstrik
[2-9] fyrri talan í raðtölunni (sem byrjar frá og með 20)
\d{2} þetta eru 2 tölustafir frá 0-9. (sem gefur þá seinni töluna í raðtölunni og svo vartöluna).
[8-9|0] Síðasta talan er svo 8, 9 eða 0.
\b orðaskil ef það eru t.d. fleiri tölur/bókstafir alveg upp við þá er þetta ekki gild kennitala


**Til að finna kennitölur fyrirtækja.** 

#### Reglulega segðin:
\b[4567]\d{5}-\d{4}\b

\b orðaskil
[4567] Fyrsti stafurinn í kt. fyrirtækja er 4, 5,6 eða 7
\d{5} Svo koma 5 tölustafir á eftir.
- Svo kemur bandstrik 
\d{4} Svo koma 4 tölustafir.
\b orðaskil
 
**Hægt er að finna kóðann undir regex_kt.py**


## 2. Leita að netfangi
E-mail geta verið af ýmsum gerðum, en oftast eru þau skilgreind með eftirfarandi sniði: <local-part>@<domain>.<top-level-domain> Skilgreining á löglegu netfangi gefið í RFC 5322 en Wikipedia gefur gagnleg dæmi um hvað má og má ekki.

Að útbúa regluleg segð sem getur fundið öll lögleg netföng er talsvert flókið, en við skulum einskorða okkur við tiltölulega algeng snið.

Útfærið eina reglulega segð í Python sem getur fundið öll eftirfarandi netföng úr textaskránni data/email.txt:

### Svar: 

**Hérna er regluleg segð til að finna lögleg netföng:**

^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]{1,63}\.[a-zA-Z]{2,6}(?:\.[a-zA-Z]{2,6})*$

Hérna er útskýringin á segðinni
    [a-zA-Z0-9_.+-]: Notendanafnið (fyrir @). Leyfir litla og stóra stafi, tölur frá 0-9, undirstrik, punkt og plús og mínus
    +: Táknar að einn eða fleiri stafir eru aðeins leyfilegar (þannig að þetta sé ekki tómt)
    @[a-zA-Z0-9-]: leyfir litla og stóra stafi í domain, tölustafi frá 0-9 og bandstrik. En bandstrik er ekki leyft fyrst eða seinast.
    {1,63}: Domainið getur innihaldið 1-63 stafi samkvæmt standard emaili
    \.: Setur punkt þarna á milli (t.d hi.is)
    [a-zA-Z]{2,6}: Leyfir bara stóra og litla bókstafi og passar að það séu 2-6 stafir. 
    
    (?: ..): Þetta er optional eins og email getur verið xx@hi.is eða xx@explorer.co.uk

**Hægt er að finna kóðann undir regex_email2.py**

## 3. Endurraða skrá

Notið reglulega segð til að endurraða línum úr CSV-skrá með nafni, heimilisfangi og símanúmeri.
Umbreytið gögnunum í sniði: heimilisfang, símanúmer og nafn. Skiptið , út fyrir \t nema á eftir kenninafni.
Vistaðu úttakið í TSV-skrá með Python kóða.

**Reglulega segðin**
([^,]+)\s([^,]+),\s([^,]+),\s([^,]+),\s(.+)

**Reglulega segðin ([^,]+)**
Þessi segð kemur fram fjórum sinnum til þess að skipta línunni upp í fjóra parta. 
Passar við einn staf sem er ekki til í listanum hér að neðan [^,].
Plús "+" Passar við fyrri táknið á milli eins og ótakmarkaðs tíma, eins oft og mögulegt er, gefur til baka eftir þörfum.

**Meta escape**
\s passar við hvaða hvíta staf "whitespace character" sem er (jafngildir [\r\n\t\f\v ])

**Reglulega segðin (.+), aftasti hópurinn**
Þetta er segðin sem kemur fyrir aftast í stóru reglulegu segðinni. 
Punktur "." passar við hvaða staf sem er (nema fyrir línulok). 
Plús "+" passar við fyrri táknið á milli eins og ótakmarkaðs tíma, eins oft og mögulegt er og gefur til baka eftir þörfum. 


## 4. Gagnaúrvinnsla

Algengt gagnaúrvinnsluvandamál er að taka hrágögn (t.d. af vefsíðum) og breyta þeim í vinnanlegt form fyrir frekari greiningu.

Þetta verkefni snýst um að vinna með gögn frá tímataka.net, sem heldur utan um allar tímatökur á Íslandi. Markmiðið er að skrapa gögn úr vefsíðum sem sýna úrslit keppna og umbreyta þeim í CSV-skrá sem er auðvelt að vinna með fyrir frekari greiningu. Þið skuluð velja mót þar sem einhver hópmeðlimur þekkir keppanda eða hefur verulegan áhuga á.

## Lausn

Í þessu verkefni unnum við með gögn frá úrslitum Hleðsluhlaupsins árið 2024 hjá körlum á aldrinum 19-29 ára
(https://timataka.net/hledsluhlaupid2024/urslit/?race=2&cat=m&age_from=19&age_to=29). 
Gögnin sem hér þurfti að sækja voru Rank (e.sæti) keppandans, BiB númer, Nafn, Year, Club, Split tími, Time, Behind og Chiptime. 

Hér má sjá reglulega segð sem sækir öll gögn um Þorlák Rafnsson sem lenti í 3. sæti í keppninni. 

<tr>\s*<td class="hidden-xs">(\d+)</td>\s*<td>(\d+)</td>\s*<td>Þorlákur Rafnsson</td>\s*<td class="hidden-xs">(\d+)</td>\s*<td class="hidden-xs">(.*?)</td>\s*<td>(.*?)<br></td>\s*<td>(.*?)</td>\s*<td>(.*?)</td>\s*<td>(.*?)</td>

Brjótum hana aðeins niður: 

- <tr>: Byrjar á að parast við fyrstu línuna í töflunni. <tr> táknar eina röð í html töflunni. 

- \s*: Leyfir hvítt bil (eða ekkert bil) eftir <tr>. 

- <td class="hidden-xs">(\d+)</td>: Þetta passar við fyrsta dálkinn (<td>) með class="hidden-xs". Reglulega segðin grípur innihald dálksins, sem eru einungis tölur, með (\d+), sem þýðir „einn eða fleiri tölustafir“. Þetta gæti t.d. verið Rank keppandans.

- \s*<td>(\d+)</td>: Passar við næsta dálk (<td>) sem inniheldur keppnisnúmerið (BIB). Aftur er það tölur með (\d+).

- \s*<td>Þorlákur Rafnsson</td>: Passar nákvæmlega við dálkinn sem inniheldur nafnið „Þorlákur Rafnsson“. Þetta er fastur texti, þar sem nafnið er ekki breytilegt.

- \s*<td class="hidden-xs">(\d+)</td>: Passar við fæðingarár keppandans, sem er táknaður með tölum ((\d+)).

- \s*<td class="hidden-xs">(.*?)</td>: Þetta passar við dálkinn sem inniheldur nafn félagsins. Hér er notað .*?, sem fangar alla stafi innan dálksins. Það síðan stöðvast við næsta <td> (þegar næsta dálkur byrjar). 

- \s*<td>(.*?)<br></td>: Passar við dálkinn sem inniheldur Split tímann (00:20:53 (5KM)) þar sem <br> eru línuskil. Aftur er notað .*? til að grípa textann fyrir <br>.

- \s*<td>(.*?)</td>: Passar við heildartímann. Það getur verið hvaða texti sem er (.*?), og textinn er innan <td>.
Við síðan endurtökum þessa segð tvisvar sinnum til að sækja Behind og Chiptime.

(\d+): Fangar eina eða fleiri tölur. Þegar þetta er notað, mun það skila tölum úr samsvarandi hluta HTML-töflunnar.
(.*?): Grípur hvaða texta sem er, en með ? verður það „lazy“, sem þýðir að það mun stöðvast eins fljótt og mögulegt er (það mun ekki fanga meira en nauðsynlegt er).

Einnig útfærðum við reglulega segð sem passar að URL sé frá tímataka.net og sýnir úrslit:
https://(www\.)?timataka\.net/.+/urslit/\?race=\d+.*

Brjótum hana aðeins niður: 

- https://(www\.)?: Þetta passar við URL sem byrjar á https:// og getur innihaldið www. en það þarf þess ekki (það er táknað með ?).
- timataka\.net: Passar nákvæmlega við lén timataka.net. 
/.+/urslit/: Passar við hvaða sem er (t.d. nafnið á keppninni eða hlaupinu) sem endar á /urslit/ sem vísar á úrslita síðuna.
\?race=\d+: Passar við fyrirspurnina í URL-inu sem inniheldur ?race= ásamt einum eða fleiri tölustöfum (\d+).
.*: Passar við allt sem kemur eftir það, sem þýðir að það er ekki sérstök krafa um hvað kemur á eftir þessu. 


Eftir að hafa keyrt forritið okkar, timataka.py með skipuninni python3 code/timataka.py --url "https://timataka.net/hledsluhlaupid2024/urslit/?race=2&cat=m&age_from=19&age_to=29" --output data/hledsluhlaup24.csv --debug varð til skráin hledsluhlaup24.csv með eftirfarandi upplýsingum: 

Rank,BIB,Name,Year,Club,Split,Time,Behind,Chiptime
3,1456,Þorlákur Rafnsson,1995,Fjallahlaupaþjálfun,00:20:53 (5KM),00:41:15                                                                                        											,+04:54,00:41:08

Þessar niðurstöður stemma við gögnin okkar. 


