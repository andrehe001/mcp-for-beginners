<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6940b1e931e51821b219aa9dcfe8c4ee",
  "translation_date": "2025-06-23T11:11:27+00:00",
  "source_file": "09-CaseStudy/README.md",
  "language_code": "fi"
}
-->
# MCP käytännössä: Todellisia tapaustutkimuksia

Model Context Protocol (MCP) muuttaa tapaa, jolla tekoälysovellukset vuorovaikuttavat datan, työkalujen ja palveluiden kanssa. Tässä osiossa esitellään todellisia tapaustutkimuksia, jotka havainnollistavat MCP:n käytännön sovelluksia eri yritystilanteissa.

## Yleiskatsaus

Tässä osiossa esitellään konkreettisia MCP-toteutuksia, jotka korostavat, miten organisaatiot hyödyntävät tätä protokollaa ratkaistakseen monimutkaisia liiketoiminnan haasteita. Tarkastelemalla näitä tapaustutkimuksia saat näkemyksiä MCP:n monipuolisuudesta, skaalautuvuudesta ja käytännön hyödyistä todellisissa tilanteissa.

## Keskeiset oppimistavoitteet

Näitä tapaustutkimuksia tarkastelemalla opit:

- Miten MCP:tä voidaan soveltaa tiettyjen liiketoimintaongelmien ratkaisuun
- Eri integraatiomallit ja arkkitehtoniset lähestymistavat
- Parhaat käytännöt MCP:n käyttöönotossa yritysympäristöissä
- Haasteet ja ratkaisut, joita todellisissa toteutuksissa on kohdattu
- Mahdollisuudet soveltaa vastaavia malleja omissa projekteissasi

## Esitellyt tapaustutkimukset

### 1. [Azure AI Travel Agents – Referenssitoteutus](./travelagentsample.md)

Tässä tapaustutkimuksessa tarkastellaan Microsoftin kattavaa referenssiratkaisua, joka näyttää, miten rakentaa moniagenttinen, tekoälyllä toimiva matkasuunnittelu­applikaatio MCP:n, Azure OpenAI:n ja Azure AI Searchin avulla. Projekti esittelee:

- Moniagenttien orkestrointi MCP:n kautta
- Yritysdatan integrointi Azure AI Searchilla
- Turvallinen ja skaalautuva arkkitehtuuri Azure-palveluilla
- Laajennettavat työkalut uudelleenkäytettävillä MCP-komponenteilla
- Keskustelupohjainen käyttäjäkokemus Azure OpenAI:n voimin

Arkkitehtuuri ja toteutuksen yksityiskohdat tarjoavat arvokkaita näkemyksiä monimutkaisten moniagenttijärjestelmien rakentamisesta MCP:n koordinaatiokerroksena.

### 2. [Azure DevOps -kohteiden päivitys YouTube-datasta](./UpdateADOItemsFromYT.md)

Tässä tapaustutkimuksessa demonstroidaan MCP:n käytännön sovellusta työnkulkujen automatisointiin. Se näyttää, miten MCP-työkaluja voi käyttää:

- Datan poimintaan verkkopalveluista (YouTube)
- Työkohteiden päivittämiseen Azure DevOps -järjestelmissä
- Toistettavien automaatiotyönkulkujen luomiseen
- Datan integrointiin eri järjestelmien välillä

Tämä esimerkki havainnollistaa, miten jopa suhteellisen yksinkertaiset MCP-toteutukset voivat tuoda merkittäviä tehokkuushyötyjä automatisoimalla rutiinitehtäviä ja parantamalla datan yhdenmukaisuutta järjestelmien välillä.

### 3. [Reaaliaikainen dokumentaation haku MCP:llä](./docs-mcp/README.md)

Tässä tapaustutkimuksessa opastetaan, miten Python-konsoliasiakas yhdistetään Model Context Protocol (MCP) -palvelimeen reaaliaikaisen, kontekstitietoisen Microsoft-dokumentaation hakemiseksi ja lokittamiseksi. Opit, miten:

- Yhdistetään MCP-palvelimeen Python-asiakkaalla ja virallisella MCP SDK:lla
- Käytetään suoratoistavia HTTP-asiakkaita tehokkaaseen reaaliaikaiseen datanhakuun
- Kutsutaan dokumentaatiotyökaluja palvelimella ja tallennetaan vastaukset suoraan konsoliin
- Integroituu ajantasainen Microsoft-dokumentaatio työnkulkuun ilman terminaalista poistumista

Luku sisältää käytännön tehtävän, minimaalisen toimivan koodiesimerkin sekä linkkejä lisäresursseihin syvempää oppimista varten. Katso koko läpikäynti ja koodi linkatusta luvusta ymmärtääksesi, miten MCP voi muuttaa dokumentaation saatavuutta ja kehittäjien tuottavuutta konsolipohjaisissa ympäristöissä.

### 4. [Interaktiivinen opintosuunnitelman generaattori web-sovellus MCP:llä](./docs-mcp/README.md)

Tässä tapaustutkimuksessa demonstroidaan, miten rakentaa interaktiivinen web-sovellus Chainlitin ja Model Context Protocolin (MCP) avulla, joka luo henkilökohtaisia opintosuunnitelmia mille tahansa aiheelle. Käyttäjät voivat määritellä aiheen (esim. "AI-900 -sertifiointi") ja opiskeluajan (esim. 8 viikkoa), ja sovellus tarjoaa viikkokohtaisen suositusten jaon. Chainlit mahdollistaa keskustelupohjaisen chat-käyttöliittymän, joka tekee kokemuksesta mukaansatempaavan ja sopeutuvan.

- Keskustelupohjainen web-sovellus Chainlitin voimin
- Käyttäjän ohjaamat aiheen ja keston syötteet
- Viikkokohtaiset sisältösuositukset MCP:n avulla
- Reaaliaikaiset, sopeutuvat vastaukset chat-käyttöliittymässä

Projekti havainnollistaa, miten keskusteleva tekoäly ja MCP voidaan yhdistää luomaan dynaamisia, käyttäjälähtöisiä opetustyökaluja nykyaikaisessa web-ympäristössä.

### 5. [Editorin sisäinen dokumentaatio MCP-palvelimella VS Codessa](./docs-mcp/README.md)

Tässä tapaustutkimuksessa näytetään, miten Microsoft Learn Docs voidaan tuoda suoraan VS Code -ympäristöön MCP-palvelimen avulla – selainvälilehtien välillä hyppiminen jää pois! Näet, miten:

- Dokumentaatiota voi hakea ja lukea välittömästi VS Codessa MCP-paneelin tai komentopalettin kautta
- Viitata dokumentaatioon ja lisätä linkkejä suoraan README- tai kurssin markdown-tiedostoihin
- Käyttää GitHub Copilotia ja MCP:tä saumattomasti yhdessä tekoälypohjaisiin dokumentaatio- ja koodityönkulkuihin
- Varmistaa ja parantaa dokumentaatiota reaaliaikaisella palautteella ja Microsoftin lähteistä saatavalla tarkkuudella
- Integroida MCP GitHub-työnkulkuihin jatkuvaa dokumentaation validointia varten

Toteutus sisältää:
- Esimerkin `.vscode/mcp.json` -konfiguraatiosta helppoa käyttöönottoa varten
- Kuvakaappauspohjaiset läpikäynnit editorin sisäisestä käyttökokemuksesta
- Vinkkejä Copilotin ja MCP:n yhdistämiseen maksimaalisen tuottavuuden saavuttamiseksi

Tämä skenaario sopii erinomaisesti kurssien tekijöille, dokumentaation kirjoittajille ja kehittäjille, jotka haluavat pysyä keskittyneinä editorissa työskennellessään dokumentaation, Copilotin ja validointityökalujen kanssa – kaikki MCP:n voimin.

### 6. [APIM MCP -palvelimen luominen](./apimsample.md)

Tässä tapaustutkimuksessa annetaan vaiheittainen opas MCP-palvelimen luomiseen Azure API Managementin (APIM) avulla. Käsitellään:

- MCP-palvelimen perustaminen Azure API Managementissa
- API-toimintojen avaaminen MCP-työkaluina
- Politiikkojen määrittely nopeusrajoituksille ja turvallisuudelle
- MCP-palvelimen testaaminen Visual Studio Codella ja GitHub Copilotilla

Tämä esimerkki havainnollistaa, miten Azure-palveluiden ominaisuuksia voidaan hyödyntää kestävän MCP-palvelimen luomisessa, jota voi käyttää monissa sovelluksissa tekoälyjärjestelmien ja yritys-API:en integraation parantamiseksi.

## Yhteenveto

Nämä tapaustutkimukset korostavat Model Context Protocolin monipuolisuutta ja käytännön sovelluksia todellisissa tilanteissa. Monimutkaisista moniagenttijärjestelmistä kohdennettuun automaatioon MCP tarjoaa standardoidun tavan yhdistää tekoälyjärjestelmät tarvittaviin työkaluihin ja datoihin arvon tuottamiseksi.

Näitä toteutuksia tutkimalla saat näkemyksiä arkkitehtuurimalleista, toteutusstrategioista ja parhaista käytännöistä, joita voit soveltaa omissa MCP-projekteissasi. Esimerkit osoittavat, että MCP ei ole pelkkä teoreettinen kehys, vaan käytännöllinen ratkaisu todellisiin liiketoiminnan haasteisiin.

## Lisäresurssit

- [Azure AI Travel Agents GitHub-repositorio](https://github.com/Azure-Samples/azure-ai-travel-agents)
- [Azure DevOps MCP Tool](https://github.com/microsoft/azure-devops-mcp)
- [Playwright MCP Tool](https://github.com/microsoft/playwright-mcp)
- [Microsoft Docs MCP Server](https://github.com/MicrosoftDocs/mcp)
- [MCP Community Examples](https://github.com/microsoft/mcp)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty tekoälypohjaisella käännöspalvelulla [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää auktoritatiivisena lähteenä. Tärkeiden tietojen osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinymmärryksistä tai virhetulkintojen seurauksista.