

## 2. Leita að netfangi
E-mail geta verið af ýmsum gerðum, en oftast eru þau skilgreind með eftirfarandi sniði: <local-part>@<domain>.<top-level-domain> Skilgreining á löglegu netfangi gefið í RFC 5322 en Wikipedia gefur gagnleg dæmi um hvað má og má ekki.

Að útbúa regluleg segð sem getur fundið öll lögleg netföng er talsvert flókið, en við skulum einskorða okkur við tiltölulega algeng snið.

Útfærið eina reglulega segð í Python sem getur fundið öll eftirfarandi netföng úr textaskránni data/email.txt:

### Svar: 

*Hérna er regluleg segð til að finna lögleg netföng:*

^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]{1,63}\.[a-zA-Z]{2,6}(?:\.[a-zA-Z]{2,6})*$

Hérna er útskýringin á segðinni
    [a-zA-Z0-9_.+-]: Notendanafnið (fyrir @). Leyfir litla og stóra stafi, tölur frá 0-9, undirstrik, punkt og plús og mínus
    +: Táknar að einn eða fleiri stafir eru aðeins leyfilegar (þannig að þetta sé ekki tómt)
    @[a-zA-Z0-9-]: leyfir litla og stóra stafi í domain, tölustafi frá 0-9 og bandstrik. En bandstrik er ekki leyft fyrst eða seinast.
    {1,63}: Domainið getur innihaldið 1-63 stafi samkvæmt standard emaili
    \.: Setur punkt þarna á milli (t.d hi.is)
    [a-zA-Z]{2,6}: Leyfir bara stóra og litla bókstafi og passar að það séu 2-6 stafir. 
    
    (?: ..): Þetta er optional eins og email getur verið xx@hi.is eða xx@explorer.co.uk

*Hægt er að finna kóðann undir regex_email2.py*