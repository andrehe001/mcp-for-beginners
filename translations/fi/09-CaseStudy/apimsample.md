<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "36de9fae488d6de554d969fe8e0801a8",
  "translation_date": "2025-06-20T19:21:40+00:00",
  "source_file": "09-CaseStudy/apimsample.md",
  "language_code": "fi"
}
-->
# Case Study: Paljasta REST API API Managementissa MCP-palvelimena

Azure API Management on palvelu, joka tarjoaa portin API-päätteidesi päälle. Se toimii niin, että Azure API Management toimii välityspalvelimena API:esi edessä ja voi päättää, mitä tehdä saapuville pyynnöille.

Sen avulla saat käyttöösi monia ominaisuuksia, kuten:

- **Turvallisuus**, voit käyttää kaikkea API-avaimista ja JWT:stä hallittuun identiteettiin.
- **Kutsujen rajoittaminen**, erinomainen ominaisuus, jonka avulla voit päättää, kuinka monta kutsua pääsee läpi tietyn aikayksikön aikana. Tämä varmistaa, että kaikilla käyttäjillä on hyvä käyttökokemus ja palvelusi ei kuormitu liikaa.
- **Skaalaus ja kuormantasapainotus**. Voit määrittää useita päätepisteitä kuorman tasaamiseksi ja voit myös valita, miten "kuormantasapainotus" tehdään.
- **AI-ominaisuudet kuten semanttinen välimuisti**, token-rajoitukset, token-valvonta ja paljon muuta. Nämä ominaisuudet parantavat vasteaikaa ja auttavat sinua hallitsemaan token-kulutustasi. [Lue lisää tästä](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Miksi MCP + Azure API Management?

Model Context Protocol on nopeasti muodostumassa standardiksi agenttipohjaisille AI-sovelluksille ja työkalujen sekä datan yhdenmukaiseen paljastamiseen. Azure API Management on luonnollinen valinta, kun sinun täytyy "hallita" API:ita. MCP-palvelimet integroituvat usein muihin API:hin esimerkiksi ratkaistakseen pyyntöjä työkaluille. Siksi Azure API Managementin ja MCP:n yhdistäminen on järkevää.

## Yleiskatsaus

Tässä tapauksessa opimme paljastamaan API-päätepisteitä MCP-palvelimena. Näin voimme helposti tehdä näistä päätepisteistä osan agenttipohjaista sovellusta ja hyödyntää samalla Azure API Managementin ominaisuuksia.

## Keskeiset ominaisuudet

- Valitset ne päätepisteiden metodit, jotka haluat paljastaa työkaluina.
- Lisäominaisuudet riippuvat siitä, mitä määrittelet API:si politiikkaosiossa. Tässä näytämme, miten voit lisätä kutsujen rajoittamisen.

## Esivaihe: API:n tuonti

Jos sinulla on jo API Azure API Managementissa, hienoa, voit ohittaa tämän vaiheen. Jos ei, tutustu tähän linkkiin, [API:n tuonti Azure API Managementiin](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Paljasta API MCP-palvelimena

Paljastaaksesi API-päätepisteet, seuraa näitä ohjeita:

1. Siirry Azure-portaaliin osoitteessa <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
   Mene API Management -instanssiisi.

1. Valitse vasemman valikon kautta APIs > MCP Servers > + Create new MCP Server.

1. Valitse API-kohdassa REST API, jonka haluat paljastaa MCP-palvelimena.

1. Valitse yksi tai useampi API-toiminto paljastettavaksi työkaluina. Voit valita kaikki toiminnot tai vain tietyt.

    ![Valitse paljastettavat metodit](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Valitse **Create**.

1. Siirry valikkoon **APIs** ja **MCP Servers**, ja sinun pitäisi nähdä seuraavaa:

    ![Näytä MCP-palvelin pääikkunassa](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP-palvelin on luotu ja API-toiminnot on paljastettu työkaluina. MCP-palvelin näkyy MCP Servers -välilehdellä. URL-sarake näyttää MCP-palvelimen päätepisteen, jota voit kutsua testaukseen tai asiakasohjelmassa.

## Valinnainen: Politiikkojen määrittäminen

Azure API Managementissa on politiikkojen peruskäsite, jossa määritetään erilaisia sääntöjä päätepisteille, kuten kutsujen rajoittaminen tai semanttinen välimuisti. Nämä politiikat kirjoitetaan XML-muodossa.

Näin voit määrittää politiikan MCP-palvelimesi kutsujen rajoittamiseksi:

1. Portaalissa, APIs-kohdassa, valitse **MCP Servers**.

1. Valitse luomasi MCP-palvelin.

1. Vasemman valikon MCP-osiossa valitse **Policies**.

1. Politiikkamuokkaimessa lisää tai muokkaa haluamiasi politiikkoja MCP-palvelimen työkaluille. Politiikat määritellään XML-muodossa. Esimerkiksi voit lisätä politiikan, joka rajoittaa kutsuja MCP-palvelimen työkaluissa (tässä esimerkissä 5 kutsua 30 sekunnissa asiakas-IP-osoitetta kohden). Tässä XML, joka toteuttaa rajoituksen:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Tässä kuva politiikkamuokkaimesta:

    ![Politiikkamuokkaimen kuva](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## Kokeile

Varmistetaan, että MCP-palvelimemme toimii kuten pitää.

Tätä varten käytämme Visual Studio Codea ja GitHub Copilotia sen Agent-tilassa. Lisäämme MCP-palvelimen *mcp.json*-tiedostoon. Näin Visual Studio Code toimii agenttikapasiteettia omaavana asiakkaana, ja loppukäyttäjät voivat kirjoittaa kehotteen ja olla vuorovaikutuksessa palvelimen kanssa.

Näin lisäät MCP-palvelimen Visual Studio Codeen:

1. Käytä MCP: **Add Server** -komentoa Command Paletesta.

1. Kun sinua pyydetään, valitse palvelintyyppi: **HTTP (HTTP tai Server Sent Events)**.

1. Syötä MCP-palvelimen URL Azure API Managementissa. Esimerkiksi: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (SSE-päätepiste) tai **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (MCP-päätepiste). Huomaa ero kuljetuksissa `/sse` or `/mcp`.

1. Syötä haluamasi palvelin-ID. Tämä ei ole kriittinen arvo, mutta auttaa muistamaan palvelininstanssin.

1. Valitse, tallennetaanko asetukset työtilan asetuksiin vai käyttäjäasetuksiin.

  - **Workspace settings** – Palvelinasetukset tallennetaan .vscode/mcp.json -tiedostoon, joka on käytettävissä vain nykyisessä työtilassa.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    Jos valitset streaming HTTP -kuljetuksen, se on hieman erilainen:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **User settings** – Palvelinasetukset lisätään globaalisti *settings.json* -tiedostoon ja ovat käytettävissä kaikissa työtiloissa. Asetus näyttää suunnilleen tältä:

    ![Käyttäjäasetusten kuva](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Sinun täytyy myös lisätä asetuksiin otsikko, jolla varmistetaan asianmukainen autentikointi Azure API Managementiin. Käytössä on otsikko nimeltä **Ocp-Apim-Subscription-Key**.

    - Näin lisäät sen asetuksiin:

    ![Otsikon lisääminen autentikointiin](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), tämän jälkeen saat kehotteen syöttää API-avaimen, jonka löydät Azure-portaalista Azure API Management -instanssiltasi.

   - Jos haluat lisätä sen *mcp.json*-tiedostoon, voit tehdä sen näin:

    ```json
    "inputs": [
      {
        "type": "promptString",
        "id": "apim_key",
        "description": "API Key for Azure API Management",
        "password": true
      }
    ]
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp",
            "headers": {
                "Ocp-Apim-Subscription-Key": "Bearer ${input:apim_key}"
            }
        }
    }
    ```

### Käytä Agent-tilaa

Nyt kun olemme valmiit joko asetuksissa tai *.vscode/mcp.json*-tiedostossa, kokeillaan.

Sinun pitäisi nähdä Työkalut-kuvake, jossa näkyvät palvelimesi paljastamat työkalut:

![Työkalut palvelimelta](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Klikkaa työkalukuvaketta, ja sinun pitäisi nähdä työkaluluettelo:

    ![Työkalut](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Kirjoita kehotteeseen viesti kutsuaksesi työkalua. Esimerkiksi, jos valitsit työkalun tilaustiedon hakemiseen, voit kysyä agentilta tilauksesta. Tässä esimerkki kehotteesta:

    ```text
    get information from order 2
    ```

    Näet nyt työkalukuvakkeen, joka pyytää jatkamaan työkalun kutsua. Valitse jatkaaksesi työkalun käyttöä, ja näet tuloksen seuraavasti:

    ![Tulokset kehotteesta](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **Mitä näet riippuu siitä, mitä työkaluja olet määrittänyt, mutta ideana on saada tekstimuotoinen vastaus kuten yllä.**

## Viitteet

Näin opit lisää:

- [Opas Azure API Managementiin ja MCP:hen](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python-esimerkki: Turvalliset etä-MCP-palvelimet Azure API Managementilla (kokeellinen)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP-asiakkaan valtuutuslaboratorio](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Käytä Azure API Management -laajennusta VS Codeen API:iden tuontiin ja hallintaan](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Rekisteröi ja löydä etä-MCP-palvelimia Azure API Centerissä](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Erinomainen repositorio, joka esittelee monia AI-ominaisuuksia Azure API Managementilla
- [AI Gateway -työpajat](https://azure-samples.github.io/AI-Gateway/) Sisältää työpajoja Azure-portaalin avulla, erinomainen tapa aloittaa AI-ominaisuuksien arviointi.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty tekoälypohjaisella käännöspalvelulla [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinymmärryksistä tai tulkinnoista.