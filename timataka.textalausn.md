# Gagnaúrvinnsla

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


Eftir að hafa keyrt forritið okkar með skipuninni python3 code/timataka.py --url "https://timataka.net/hledsluhlaupid2024/urslit/?race=2&cat=m&age_from=19&age_to=29" --output data/hledsluhlaup24.csv --debug varð til skrá með eftirfarandi upplýsingum: 

Rank,BIB,Name,Year,Club,Split,Time,Behind,Chiptime
3,1456,Þorlákur Rafnsson,1995,Fjallahlaupaþjálfun,00:20:53 (5KM),00:41:15                                                                                        											,+04:54,00:41:08

Þessar niðurstöður stemma við gögnin okkar. 

