<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5384bbb2a92d00d5d7e66274dbe0331d",
  "translation_date": "2025-06-20T18:38:41+00:00",
  "source_file": "04-PracticalImplementation/README.md",
  "language_code": "fi"
}
-->
# Käytännön toteutus

Käytännön toteutus on se vaihe, jossa Model Context Protocolin (MCP) voima konkretisoituu. Vaikka MCP:n teorian ja arkkitehtuurin ymmärtäminen on tärkeää, todellinen arvo syntyy, kun sovellat näitä käsitteitä rakentaaksesi, testataksesi ja ottaaksesi käyttöön ratkaisuja, jotka ratkaisevat oikean maailman ongelmia. Tämä luku yhdistää käsitteellisen tiedon ja käytännön kehityksen, ohjaten sinua MCP-pohjaisten sovellusten elävöittämisessä.

Olitpa kehittämässä älykkäitä avustajia, integroimassa tekoälyä liiketoimintaprosesseihin tai rakentamassa räätälöityjä työkaluja datan käsittelyyn, MCP tarjoaa joustavan perustan. Sen kieliriippumaton rakenne ja viralliset SDK:t suosituimmille ohjelmointikielille tekevät siitä helposti lähestyttävän laajalle kehittäjäjoukolle. Hyödyntämällä näitä SDK:ita voit nopeasti prototyypittää, iteröidä ja skaalata ratkaisuja eri alustoilla ja ympäristöissä.

Seuraavissa osioissa löydät käytännön esimerkkejä, koodinäytteitä ja käyttöönotto-strategioita, jotka näyttävät, miten MCP toteutetaan C#:ssa, Javassa, TypeScriptissä, JavaScriptissä ja Pythonissa. Opit myös, miten MCP-palvelimia virheenkorjataan ja testataan, hallitaan API-rajapintoja sekä otetaan ratkaisuja käyttöön pilvessä Azuren avulla. Nämä käytännön resurssit on suunniteltu nopeuttamaan oppimistasi ja auttamaan sinua rakentamaan luotettavia, tuotantovalmiita MCP-sovelluksia itsevarmasti.

## Yleiskatsaus

Tämä oppitunti keskittyy MCP:n käytännön toteutukseen useilla ohjelmointikielillä. Tutustumme siihen, miten MCP SDK:ita käytetään C#:ssa, Javassa, TypeScriptissä, JavaScriptissä ja Pythonissa vahvojen sovellusten rakentamiseen, MCP-palvelinten virheenkorjaukseen ja testaamiseen sekä uudelleenkäytettävien resurssien, kehotteiden ja työkalujen luomiseen.

## Oppimistavoitteet

Tämän oppitunnin jälkeen osaat:
- Toteuttaa MCP-ratkaisuja virallisilla SDK:illa eri ohjelmointikielillä
- Virheenkorjata ja testata MCP-palvelimia systemaattisesti
- Luoda ja käyttää palvelintoimintoja (Resources, Prompts ja Tools)
- Suunnitella tehokkaita MCP-työnkulkuja monimutkaisiin tehtäviin
- Optimoida MCP-toteutuksia suorituskyvyn ja luotettavuuden näkökulmasta

## Viralliset SDK-resurssit

Model Context Protocol tarjoaa viralliset SDK:t useille kielille:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) 
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

## MCP SDK:iden käyttö

Tässä osiossa esitellään käytännön esimerkkejä MCP:n toteuttamisesta useilla ohjelmointikielillä. Näytekoodit löytyvät `samples`-hakemistosta, järjestettynä kielittäin.

### Saatavilla olevat esimerkit

Repositoriossa on [näytetoteutuksia](../../../04-PracticalImplementation/samples) seuraavilla kielillä:

- [C#](./samples/csharp/README.md)
- [Java](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Jokainen esimerkki havainnollistaa keskeisiä MCP-konsepteja ja toteutusmalleja kyseiselle kielelle ja ekosysteemille.

## Keskeiset palvelintoiminnot

MCP-palvelimet voivat toteuttaa minkä tahansa yhdistelmän seuraavista ominaisuuksista:

### Resources
Resources tarjoavat kontekstin ja datan käyttäjälle tai tekoälymallille:
- Asiakirjahakemistot
- Tietopohjat
- Rakenteelliset tietolähteet
- Tiedostojärjestelmät

### Prompts
Prompts ovat valmiiksi mallinnettuja viestejä ja työnkulkuja käyttäjille:
- Ennalta määritellyt keskustelumallit
- Ohjatut vuorovaikutuskuviot
- Erikoistuneet dialogirakenteet

### Tools
Tools ovat toimintoja, joita tekoälymalli voi suorittaa:
- Datan käsittelytyökalut
- Ulkoiset API-integraatiot
- Laskennalliset toiminnot
- Hakutoiminnot

## Näytetoteutukset: C#

Virallinen C# SDK -repositorio sisältää useita esimerkkitoteutuksia, jotka havainnollistavat MCP:n eri puolia:

- **Perus MCP Client**: Yksinkertainen esimerkki MCP-clientin luomisesta ja työkalujen kutsumisesta
- **Perus MCP Server**: Minimipalvelin, jossa on perustyökalujen rekisteröinti
- **Kehittynyt MCP Server**: Täysimittainen palvelin, jossa on työkalujen rekisteröinti, autentikointi ja virheenkäsittely
- **ASP.NET-integraatio**: Esimerkkejä ASP.NET Core -integraatiosta
- **Työkalujen toteutusmallit**: Eri monimutkaisuustasojen työkalujen toteutusmalleja

MCP C# SDK on ennakkoversiossa, ja API:t voivat muuttua. Päivitämme tätä blogia jatkuvasti SDK:n kehittyessä.

### Keskeiset ominaisuudet
- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)

- Ensimmäisen [MCP-palvelimen rakentaminen](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

Täydelliset C# toteutusnäytteet löytyvät [virallisen C# SDK:n näytereposta](https://github.com/modelcontextprotocol/csharp-sdk)

## Näytetoteutus: Java

Java SDK tarjoaa vahvat MCP-toteutusvaihtoehdot yritystason ominaisuuksilla.

### Keskeiset ominaisuudet

- Spring Framework -integraatio
- Vahva tyyppiturvallisuus
- Reaktiivisen ohjelmoinnin tuki
- Laaja virheenkäsittely

Täydellinen Java-toteutusnäyte löytyy [Java-esimerkistä](samples/java/containerapp/README.md) näytekansiosta.

## Näytetoteutus: JavaScript

JavaScript SDK tarjoaa kevyen ja joustavan tavan toteuttaa MCP.

### Keskeiset ominaisuudet

- Tuki Node.js:lle ja selaimille
- Promise-pohjainen API
- Helppo integraatio Expressin ja muiden kehysten kanssa
- WebSocket-tuki suoratoistoon

Täydellinen JavaScript-toteutusnäyte löytyy [JavaScript-esimerkistä](samples/javascript/README.md) näytekansiosta.

## Näytetoteutus: Python

Python SDK tarjoaa pythonilaisen lähestymistavan MCP-toteutukseen erinomaisilla ML-kehysintegraatioilla.

### Keskeiset ominaisuudet

- Async/await-tuki asyncio-kirjastolla
- Flask- ja FastAPI-integraatiot
- Yksinkertainen työkalujen rekisteröinti
- Natiivisti tuettu integraatio suosittuihin ML-kirjastoihin

Täydellinen Python-toteutusnäyte löytyy [Python-esimerkistä](samples/python/README.md) näytekansiosta.

## API-hallinta

Azure API Management on erinomainen ratkaisu MCP-palvelinten suojaamiseen. Ajatuksena on laittaa Azure API Management -instanssi MCP-palvelimen eteen ja antaa sen hoitaa toiminnot, joita todennäköisesti tarvitset, kuten:

- nopeusrajoitukset
- tokenien hallinta
- valvonta
- kuormantasapaino
- tietoturva

### Azure-esimerkki

Tässä on Azure-esimerkki, joka tekee juuri tämän, eli [luo MCP-palvelimen ja suojaa sen Azure API Managementilla](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Katso, miten valtuutusprosessi etenee alla olevassa kuvassa:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true) 

Edellisessä kuvassa tapahtuu seuraavaa:

- Autentikointi/valtuutus tapahtuu Microsoft Entran avulla.
- Azure API Management toimii porttina ja käyttää sääntöjä liikenteen ohjaukseen ja hallintaan.
- Azure Monitor kirjaa kaikki pyynnöt myöhempää analyysiä varten.

#### Valtuutusprosessi

Tutustutaan valtuutusprosessiin tarkemmin:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP-valtuutuksen määrittely

Lue lisää [MCP Authorization -määrittelystä](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization#2-10-third-party-authorization-flow)

## Etä-MCP-palvelimen käyttöönotto Azureen

Katsotaan, voimmeko ottaa käyttöön aiemmin mainitun esimerkin:

1. Klonkaa repo

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. Rekisteröi `Microsoft.App` komennolla  
   `` resource provider.
    * If you are using Azure CLI, run `az provider register --namespace Microsoft.App --wait`.
    * If you are using Azure PowerShell, run `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Then run `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState`  
   odota hetki ja tarkista, onko rekisteröinti valmis.

2. Suorita tämä [azd](https://aka.ms/azd) komento, jolla provisioidaan API Management -palvelu, funktiosovellus (koodin kanssa) ja kaikki muut tarvittavat Azure-resurssit

    ```shell
    azd up
    ```

    Tämä komento ottaa käyttöön kaikki pilvipalvelut Azureen

### Palvelimen testaaminen MCP Inspectorilla

1. Avaa **uusi komentorivi-ikkuna**, asenna ja käynnistä MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Näet käyttöliittymän, joka näyttää tältä:

    ![Connect to Node inspector](../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.fi.png) 

1. CTRL-klikkaa ladataksesi MCP Inspector -web-sovelluksen sovelluksen näyttämästä URL-osoitteesta (esim. http://127.0.0.1:6274/#resources)
1. Aseta siirtotyyppi `SSE`
1. Set the URL to your running API Management SSE endpoint displayed after `azd up` ja **Yhdistä**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

5. **Listaa työkalut**. Klikkaa työkalua ja valitse **Run Tool**.

Jos kaikki vaiheet onnistuivat, olet nyt yhteydessä MCP-palvelimeen ja pystyt kutsumaan työkalua.

## MCP-palvelimet Azureen

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Tämä joukko repositorioita tarjoaa pika-alustat MCP-palvelimien rakentamiseen ja käyttöönottoon Azure Functions -ympäristössä Pythonilla, C# .NET:llä tai Node/TypeScriptillä.

Näytteet tarjoavat täydellisen ratkaisun, joka mahdollistaa kehittäjille:

- Paikallisen rakentamisen ja ajon: Kehitä ja virheenkorjaa MCP-palvelin paikallisella koneella
- Käyttöönoton Azureen: Helppo pilveen siirtyminen yksinkertaisella azd up -komennolla
- Yhteyden muodostamisen asiakkailta: Yhdistä MCP-palvelimeen eri asiakkailta, kuten VS Code Copilot -agenttimoodilla ja MCP Inspector -työkalulla

### Keskeiset ominaisuudet:

- Turvallisuus suunnittelusta lähtien: MCP-palvelin on suojattu avaimilla ja HTTPS:llä
- Autentikointivaihtoehdot: Tukee OAuth:ta sisäänrakennetulla autentikoinnilla ja/tai API Managementilla
- Verkkoinfrastruktuurin eristäminen: Mahdollistaa verkkoinfrastruktuurin eristämisen Azure Virtual Networkien (VNET) avulla
- Serverless-arkkitehtuuri: Hyödyntää Azure Functionsia skaalautuvaan, tapahtumapohjaiseen suoritukseen
- Paikallinen kehitys: Kattava tuki paikalliseen kehitykseen ja virheenkorjaukseen
- Yksinkertainen käyttöönotto: Sujuva käyttöönotto Azureen

Repositoriossa on kaikki tarvittavat konfiguraatiotiedostot, lähdekoodi ja infrastruktuurin määrittelyt, jotta pääset nopeasti alkuun tuotantovalmiin MCP-palvelimen toteutuksessa.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) – MCP:n näytetoteutus Azure Functionsilla Pythonilla

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) – MCP:n näytetoteutus Azure Functionsilla C# .NET:llä

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) – MCP:n näytetoteutus Azure Functionsilla Node/TypeScriptillä

## Keskeiset opit

- MCP SDK:t tarjoavat kielikohtaiset työkalut vahvojen MCP-ratkaisujen toteutukseen
- Virheenkorjaus ja testaus ovat kriittisiä luotettaville MCP-sovelluksille
- Uudelleenkäytettävät kehotepohjat mahdollistavat johdonmukaiset tekoälyvuorovaikutukset
- Hyvin suunnitellut työnkulut voivat orkestroida monimutkaisia tehtäviä useilla työkaluilla
- MCP-ratkaisujen toteutuksessa on huomioitava tietoturva, suorituskyky ja virheenkäsittely

## Harjoitus

Suunnittele käytännön MCP-työnkulku, joka ratkaisee todellisen ongelman omalla alallasi:

1. Tunnista 3–4 työkalua, jotka olisivat hyödyllisiä ongelman ratkaisemisessa
2. Laadi työnkulun kaavio, joka näyttää, miten nämä työkalut toimivat yhdessä
3. Toteuta perusversio yhdestä työkaluista valitsemallasi kielellä
4. Luo kehotepohja, joka auttaa mallia käyttämään työkalua tehokkaasti

## Lisäresurssit


---

Seuraava: [Edistyneet aiheet](../05-AdvancedTopics/README.md)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset saattavat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeiden tietojen osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.