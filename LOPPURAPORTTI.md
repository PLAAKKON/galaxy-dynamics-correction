# GDC – galaksin kehityshistorian vaikutus tähtiratoihin ja massanmääritykseen
**Rajattu päätöstutkimus 27.10.2026 · Simulaatiotutkimus, ei havainnoista sovitettu massamalli**

## Tutkimuskysymys
Voiko galaksin varhainen, myöhemmin kadonnut suuntariippuvainen gravitaatiohäiriö jättää tähtien radoille pitkän aikavälin muistin, ja kuinka paljon nykyhetken yksinkertaistettu nopeusperusteinen massaindikaattori voi tämän vuoksi poiketa häiriöttömästä kontrollista?

## Toteutus
- Neljä historiaa: häiriötön kontrolli, yksi lyhyt pyörivä m=2-häiriö, yksi pidempi m=2-häiriö ja kaksi erillistä m=2-häiriötä. Viimeisessä vaiheessa kaikki häiriöt vaimenevat.
- Viisi riippumatonta alkujakaumaa (seed 0–4), 1 200 massatonta testitähteä kussakin, r=6–14 kpc. Yhteensä 24 000 laskennallista tähtirataa.
- Integrointiaika 3 Gyr ja aika-askel 0,002 Gyr. Taustapotentiaali on aksisymmetrinen logaritminen potentiaali, jonka v0=200 km/s ja ydinsäde 0,5 kpc.
- Häiriö: Φ₂ = ε v₀² [r²/(r²+a²)] cos[2(φ−Ωt)] × ajallinen Gauss-pulssi; ε=0,015; a=5 kpc. Ensimmäisten pulssien Ω=25 km/s/kpc ja toisen 19 km/s/kpc. Lyhyen pulssin keskus 0,65 Gyr ja leveys 0,23 Gyr, pitkän 0,65 Gyr ja 0,42 Gyr, kaksipulssisen keskukset 0,55 ja 1,4 Gyr, leveys 0,22 Gyr.
- Sama alkujakauma kullekin saman seedin historiahaaralle.
- Raportoidut luvut ovat viiden seedin keskiarvoja. Numeerinen integraatio on symplektinen leapfrog, mutta ulkoisen ajasta riippuvan potentiaalin takia yksittäisen tähden energia ei säily häiriön aikana; pyörimismäärä voi siirtyä potentiaalin määräämään taustaan.

## Päätulokset
| Historia | <|ΔRg|> (kpc) | <|ΔLz/Lz0|> (%) | Osuus |ΔRg| > 0,5 kpc (%) |
|---|---:|---:|---:|
| Kontrolli | 0,000 | 0,00 | 0,0 |
| Lyhyt häiriö | 0,366 | 4,35 | 23,8 |
| Pidempi häiriö | 0,359 | 4,06 | 22,1 |
| Kaksi häiriötä | 0,919 | 9,66 | 61,6 |

Ohjaussäde Rg=Lz/v0 on tässä likiarvo. Häiriöttömässä kontrollissa Lz pysyy numeerisesti vakiona. Häiriöiden jälkeen Lz jää eri arvoksi, vaikka ulkoinen potentiaali on palannut alkuperäiseen muotoonsa. Näin muodostuu todellinen simuloitu historiariippuvuus.

### Yksinkertaistetun massaindikaattorin poikkeama kontrollista (prosenttiyksikköä)
Kaava: 100 × [(<vφ>/vc)^2−1], josta vähennetään kontrollin vastaava arvo samalla sädevyöhykkeellä ja samalla seedillä. Tämä ei ole itsejohdonmukaisen kiekon kokonaismassan määritys eikä todistettu halo-massavirhe.

| Nykyinen sädevyöhyke, keskus | Lyhyt häiriö | Pidempi häiriö | Kaksi häiriötä |
|---|---:|---:|---:|
| 7 kpc | +0,00 | −0,04 | −0,01 |
| 9 kpc | +0,02 | +0,00 | +0,19 |
| 11 kpc | +1,16 | +1,33 | +0,82 |
| 13 kpc | +2,29 | +5,00 | +1,92 |

Ratakauden ja häiriön pituuden ei nähdä tuottavan yksinkertaista monotonista massaindikaattorin muutosta. Kaksi pulssia tuottaa suurimmat tähtikohtaiset Lz-muutokset, mutta ei suurinta pyörimisnopeusperusteista massapoikkeamaa.

## Välipäätelmä, joka kestää tässä mallissa
1. **Vahvistettu mallissa:** ohimenevä ei-aksisymmetrinen gravitaatiohäiriö voi siirtää tähtien pyörimismäärää pysyvästi. Tähtien nykyinen ratakeskus riippuu kehityshistoriasta, vaikka tämänhetkinen asetettu peruspotentiaali on kaikissa tapauksissa sama.
2. **Vahvistettu mallissa:** yksinkertaisen pyörimisnopeuteen perustuvan massaproxyn historiariippuva ero voi olla muutamia prosentteja ja paikallisesti noin 5 prosenttiyksikköä tämän parametrivalinnan puitteissa.
3. **Ei vahvistettu:** mekanismit eivät tässä kokeessa selitä suurta pimeän aineen massavajetta eivätkä osoita, että pimeän aineen määrää olisi nykyisin järjestelmällisesti yliarvioitu.
4. **Erityinen rajoitus:** simulaation taustapotentiaali tuottaa jo valmiiksi tasaisen ~200 km/s kiertokäyrän; tätä ei rakennettu tunnetun baryonisen aineen itsejohdonmukaisesta massajakaumasta. Siksi koe ei ole pimeän aineen olemassaolon testi.

## Metodologiset rajoitukset
- Massattomat koetähdet eivät vaikuta potentiaaliin eivätkä toisiinsa, joten tähtijakauman uudelleenjärjestymistä ei kytketä takaisin gravitaatiokenttään.
- Ei kaasua, viskositeettia, magnetohydrodynamiikkaa, tähtien syntyä tai palautetta.
- Häiriön energia ja pyörimismäärä vaihtuvat ulkoa määrätyn pyörivän potentiaalin kanssa. Koko galaksin energian ja momentin säilymistä ei testata itsejohdonmukaisesti.
- Nykyisen sädevyöhykkeen tähdet eivät ole samoja eri simulaatioissa; otantavalikoituminen voi osaltaan selittää massaindikaattorin eroja.
- Virheanalyysi sisältää vain viisi alkujakaumaa, ei eri potentiaalimuotojen, numeerisen resoluution, havaintoprojektioiden tai fysikaalisen alihilamallin aiheuttamaa epävarmuutta.
- Yhdenkään todellisen galaksin havaintoaineiston massaa ei ole tällä ohjelmalla sovitettu.

## Vertaisarvioidun kirjallisuuden konteksti
- Sellwood & Binney (2002), *Radial mixing in galactic discs*, MNRAS 336, 785–796, https://doi.org/10.1046/j.1365-8711.2002.05806.x : resonansseihin perustuva tähtien radiaalinen migraatio on tunnettu ilmiö.
- Antoja et al. (2018), *A dynamically young and perturbed Milky Way disk*, Nature 561, 360–362, https://doi.org/10.1038/s41586-018-0510-7 : Gaia-vaiheavaruuden rakenteissa näkyy aiempien häiriöiden jälkiä.
- *Evaluating galaxy dynamical masses from kinematics and Jeans equilibrium in simulations* (2021), MNRAS 503, 5238–5253, https://doi.org/10.1093/mnras/stab833 : dynaamisen massan mittaus vaatii muun muassa hajontaliikkeiden käsittelyn.

## Lopullinen tutkimuksellinen päätös
**GDC:n historiariippuvuuden suppea mekanismi on todettu mahdolliseksi ja havaintokirjallisuuden kanssa yhteensopivaksi. Uusi simulaatiokoe osoittaa sen omassa idealisoidussa asetelmassaan, mutta ei osoita pimeän aineen puuttumista tai selitä sitä pois.**

Tämä on rajatun numeerisen tutkimuksen valmis päätelmä. Väitteen testaaminen todellisissa galakseissa edellyttää ennakkorekisteröityä massamallin sovitusprotokollaa ja riippumatonta havaintoaineistoa; kyseinen havaintotesti ei sisälly tähän tutkimukseen.
