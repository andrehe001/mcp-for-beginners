<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "36de9fae488d6de554d969fe8e0801a8",
  "translation_date": "2025-06-20T19:26:13+00:00",
  "source_file": "09-CaseStudy/apimsample.md",
  "language_code": "hr"
}
-->
# Case Study: Izlaganje REST API-ja u API Managementu kao MCP server

Azure API Management je usluga koja pruža Gateway iznad vaših API Endpointa. Način rada je takav da Azure API Management djeluje kao proxy ispred vaših API-ja i može odlučiti što će napraviti s dolaznim zahtjevima.

Korištenjem ove usluge, dobivate cijeli niz značajki poput:

- **Sigurnosti**, možete koristiti sve od API ključeva, JWT do managed identity.
- **Ograničenja brzine (Rate limiting)**, odlična značajka koja vam omogućuje da odlučite koliko poziva može proći u određenom vremenskom razdoblju. To pomaže osigurati da svi korisnici imaju izvrsno iskustvo i da vaš servis ne bude preopterećen zahtjevima.
- **Skaliranje i balansiranje opterećenja**. Možete postaviti više endpointa za raspodjelu opterećenja i odlučiti kako želite "balansirati opterećenje".
- **AI značajke poput semantičkog keširanja**, ograničenja tokena, praćenja tokena i još mnogo toga. Ove značajke poboljšavaju odzivnost i pomažu vam pratiti potrošnju tokena. [Više pročitajte ovdje](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Zašto MCP + Azure API Management?

Model Context Protocol brzo postaje standard za agentne AI aplikacije i način izlaganja alata i podataka na dosljedan način. Azure API Management je prirodan izbor kad trebate "upravljati" API-jima. MCP serveri često se integriraju s drugim API-jima kako bi, na primjer, riješili zahtjeve prema nekom alatu. Stoga kombinacija Azure API Managementa i MCP-a ima puno smisla.

## Pregled

U ovom konkretnom slučaju naučit ćemo kako izložiti API endpoint kao MCP Server. Time možemo lako učiniti ove endpointove dijelom agentne aplikacije, a istovremeno iskoristiti značajke Azure API Managementa.

## Ključne značajke

- Birate metode endpointa koje želite izložiti kao alate.
- Dodatne značajke koje dobivate ovise o konfiguraciji u sekciji politika za vaš API. Ovdje ćemo pokazati kako dodati ograničenje brzine (rate limiting).

## Pripremni korak: uvoz API-ja

Ako već imate API u Azure API Managementu, odlično, ovaj korak možete preskočiti. Ako ne, pogledajte ovaj link, [uvoz API-ja u Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Izlaganje API-ja kao MCP Server

Za izlaganje API endpointa slijedite ove korake:

1. Otvorite Azure Portal i idite na adresu <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
   Otvorite vašu instancu API Managementa.

1. U lijevom izborniku odaberite APIs > MCP Servers > + Create new MCP Server.

1. U API sekciji odaberite REST API koji želite izložiti kao MCP server.

1. Odaberite jednu ili više API operacija koje želite izložiti kao alate. Možete odabrati sve operacije ili samo određene.

    ![Select methods to expose](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Kliknite **Create**.

1. U izborniku odaberite **APIs** i **MCP Servers**, trebali biste vidjeti sljedeće:

    ![See the MCP Server in the main pane](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP server je kreiran, a API operacije su izložene kao alati. MCP server je prikazan u MCP Servers panelu. Stupac URL prikazuje endpoint MCP servera koji možete koristiti za testiranje ili u klijentskoj aplikaciji.

## Opcionalno: Konfiguracija politika

Azure API Management ima osnovni koncept politika u kojima postavljate različita pravila za vaše endpointove, poput ograničenja brzine ili semantičkog keširanja. Te se politike definiraju u XML formatu.

Evo kako možete postaviti politiku za ograničenje brzine na vašem MCP Serveru:

1. U portalu, pod APIs, odaberite **MCP Servers**.

1. Odaberite MCP server koji ste kreirali.

1. U lijevom izborniku, pod MCP, odaberite **Policies**.

1. U uređivaču politika dodajte ili uredite politike koje želite primijeniti na alate MCP servera. Politike su definirane u XML formatu. Na primjer, možete dodati politiku za ograničenje poziva na alate MCP servera (u ovom primjeru, 5 poziva na 30 sekundi po IP adresi klijenta). Evo XML koda koji će to omogućiti:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Evo slike uređivača politika:

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## Isprobajte

Provjerimo radi li naš MCP Server kako treba.

Za ovo ćemo koristiti Visual Studio Code i GitHub Copilot u Agent modu. Dodati ćemo MCP server u *mcp.json*. Time će Visual Studio Code djelovati kao klijent s agentnim mogućnostima, a krajnji korisnici moći će unijeti prompt i komunicirati s tim serverom.

Evo kako dodati MCP server u Visual Studio Code:

1. Koristite MCP: **Add Server command iz Command Palettea**.

1. Kada vas se pita, odaberite tip servera: **HTTP (HTTP ili Server Sent Events)**.

1. Unesite URL MCP servera u API Managementu. Primjer: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (za SSE endpoint) ili **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (za MCP endpoint). Obratite pažnju na razliku u transportu: `/sse` or `/mcp`.

1. Unesite ID servera po želji. Nije važno što odaberete, ali će vam pomoći da zapamtite o kojoj se instanci radi.

1. Odaberite želite li spremiti konfiguraciju u postavke radnog prostora ili korisničke postavke.

  - **Workspace settings** - Konfiguracija servera se sprema u datoteku .vscode/mcp.json koja je dostupna samo u trenutnom radnom prostoru.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    ili, ako odaberete streaming HTTP kao transport, izgledat će malo drugačije:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **User settings** - Konfiguracija servera se dodaje u globalnu *settings.json* datoteku i dostupna je u svim radnim prostorima. Konfiguracija izgleda ovako:

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Također trebate dodati konfiguraciju, odnosno header za pravilnu autentikaciju prema Azure API Managementu. Koristi se header naziva **Ocp-Apim-Subscription-Key**.

    - Evo kako ga dodati u postavke:

    ![Adding header for authentication](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), što će uzrokovati da se pojavi prompt za unos vrijednosti API ključa koji možete pronaći u Azure Portalu za vašu instancu Azure API Managementa.

   - Za dodavanje u *mcp.json* umjesto toga, možete ga dodati ovako:

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

### Koristite Agent mod

Sada smo spremni, bilo u postavkama ili u *.vscode/mcp.json*. Isprobajmo.

Trebala bi se pojaviti ikona Tools (Alati) poput ove, gdje su navedeni izloženi alati s vašeg servera:

![Tools from the server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Kliknite na ikonu alata i trebali biste vidjeti popis alata kao na slici:

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Unesite prompt u chat za pokretanje alata. Na primjer, ako ste odabrali alat za dobivanje informacija o narudžbi, možete pitati agenta o narudžbi. Evo primjera prompta:

    ```text
    get information from order 2
    ```

    Sada će vam se pojaviti ikona alata koja traži da nastavite s pozivanjem alata. Odaberite nastavak pokretanja alata, trebali biste vidjeti izlaz poput ovog:

    ![Result from prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **što vidite ovisi o alatima koje ste postavili, ali ideja je da dobijete tekstualni odgovor poput ovog gore**

## Reference

Evo gdje možete saznati više:

- [Tutorial o Azure API Managementu i MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python primjer: Sigurni udaljeni MCP serveri koristeći Azure API Management (eksperimentalno)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Laboratorij za autorizaciju MCP klijenta](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Koristite Azure API Management ekstenziju za VS Code za uvoz i upravljanje API-jima](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Registracija i pronalazak udaljenih MCP servera u Azure API Centeru](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Odličan repozitorij koji prikazuje mnoge AI mogućnosti s Azure API Managementom
- [AI Gateway radionice](https://azure-samples.github.io/AI-Gateway/) Sadrži radionice koristeći Azure Portal, što je odličan način za početak evaluacije AI mogućnosti.

**Izjava o odricanju odgovornosti**:  
Ovaj dokument je preveden pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.