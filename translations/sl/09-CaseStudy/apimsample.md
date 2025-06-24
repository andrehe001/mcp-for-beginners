<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "36de9fae488d6de554d969fe8e0801a8",
  "translation_date": "2025-06-20T19:26:32+00:00",
  "source_file": "09-CaseStudy/apimsample.md",
  "language_code": "sl"
}
-->
# Študija primera: Izpostavitev REST API v API Management kot MCP strežnik

Azure API Management je storitev, ki zagotavlja prehod (Gateway) nad vašimi API končnimi točkami. Deluje tako, da Azure API Management deluje kot proxy pred vašimi API-ji in lahko odloča, kaj storiti z dohodnimi zahtevki.

Z njegovo uporabo dodate vrsto funkcij, kot so:

- **Varnost**, lahko uporabljate vse od API ključev, JWT do upravljanih identitet.
- **Omejevanje hitrosti**, odlična funkcija, ki omogoča določiti, koliko klicev lahko preide v določenem časovnem obdobju. To pomaga zagotoviti odlično uporabniško izkušnjo za vse in tudi, da vaša storitev ni preobremenjena z zahtevki.
- **Prilagajanje zmogljivosti in uravnoteženje obremenitve**. Lahko nastavite več končnih točk za uravnoteženje obremenitve in se odločite, kako želite "uravnotežiti obremenitev".
- **AI funkcije, kot so semantično predpomnjenje**, omejitev tokenov, spremljanje tokenov in še več. Te funkcije izboljšujejo odzivnost in vam pomagajo nadzorovati porabo tokenov. [Preberite več tukaj](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Zakaj MCP + Azure API Management?

Model Context Protocol hitro postaja standard za agentne AI aplikacije in način izpostavitve orodij ter podatkov na dosleden način. Azure API Management je naravna izbira, ko morate "upravljati" API-je. MCP strežniki se pogosto integrirajo z drugimi API-ji za reševanje zahtevkov, na primer do orodja. Zato kombinacija Azure API Management in MCP smiselno deluje skupaj.

## Pregled

V tem konkretnem primeru se bomo naučili, kako izpostaviti API končne točke kot MCP strežnik. S tem lahko te končne točke enostavno vključimo v agentno aplikacijo, hkrati pa izkoristimo funkcije Azure API Management.

## Ključne funkcije

- Izberete metode končne točke, ki jih želite izpostaviti kot orodja.
- Dodatne funkcije, ki jih dobite, so odvisne od nastavitev v politiki za vaš API. Tukaj bomo pokazali, kako dodati omejevanje hitrosti.

## Predhodni korak: uvoz API-ja

Če že imate API v Azure API Management, odlično, lahko ta korak preskočite. Če ne, si oglejte ta povezavo, [uvoz API-ja v Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Izpostavitev API-ja kot MCP strežnik

Za izpostavitev API končnih točk sledite naslednjim korakom:

1. Pojdite v Azure Portal na naslov <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
Pojdite do vaše instance API Management.

1. V levem meniju izberite APIs > MCP Servers > + Create new MCP Server.

1. V API-ju izberite REST API, ki ga želite izpostaviti kot MCP strežnik.

1. Izberite eno ali več API operacij, ki jih želite izpostaviti kot orodja. Lahko izberete vse operacije ali le določene.

    ![Izberite metode za izpostavitev](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Izberite **Create**.

1. Pojdite v meni **APIs** in **MCP Servers**, kjer bi morali videti naslednje:

    ![Prikaz MCP strežnika v glavnem oknu](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP strežnik je ustvarjen in API operacije so izpostavljene kot orodja. MCP strežnik je prikazan v seznamu MCP Servers. Stolpec URL prikazuje končno točko MCP strežnika, ki jo lahko pokličete za testiranje ali znotraj odjemalske aplikacije.

## Izbirno: konfiguracija politik

Azure API Management temelji na konceptu politik, kjer nastavite različna pravila za vaše končne točke, na primer omejevanje hitrosti ali semantično predpomnjenje. Te politike so zapisane v XML.

Tako lahko nastavite politiko za omejevanje hitrosti MCP strežnika:

1. V portalu pod APIs izberite **MCP Servers**.

1. Izberite MCP strežnik, ki ste ga ustvarili.

1. V levem meniju pod MCP izberite **Policies**.

1. V urejevalniku politik dodajte ali uredite politike, ki jih želite uporabiti za orodja MCP strežnika. Politike so definirane v XML formatu. Na primer, lahko dodate politiko, ki omeji klice orodij MCP strežnika (v tem primeru 5 klicev na 30 sekund na IP naslov klienta). Tukaj je XML, ki bo omogočil omejevanje hitrosti:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Slika urejevalnika politik:

    ![Urejevalnik politik](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Preizkusite

Preverimo, ali naš MCP strežnik deluje, kot je pričakovano.

Za to bomo uporabili Visual Studio Code in GitHub Copilot v načinu agenta. MCP strežnik bomo dodali v datoteko *mcp.json*. S tem bo Visual Studio Code deloval kot odjemalec z agentnimi zmožnostmi, končni uporabniki pa bodo lahko vpisali ukaz in komunicirali s strežnikom.

Kako dodati MCP strežnik v Visual Studio Code:

1. Uporabite ukaz MCP: **Add Server iz Command Palette**.

1. Ko vas vpraša, izberite tip strežnika: **HTTP (HTTP ali Server Sent Events)**.

1. Vnesite URL MCP strežnika v API Management. Primer: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (za SSE endpoint) ali **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (za MCP endpoint), opazite razliko v prenosu `/sse` or `/mcp`.

1. Vnesite ID strežnika po želji. Ni pomembna vrednost, vendar vam bo pomagala zapomniti, za kateri strežnik gre.

1. Izberite, ali želite konfiguracijo shraniti v nastavitve delovnega prostora ali uporabniške nastavitve.

  - **Nastavitve delovnega prostora** - konfiguracija strežnika se shrani v datoteko .vscode/mcp.json, ki je na voljo samo v trenutnem delovnem prostoru.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    ali če izberete streaming HTTP kot prenos, bo nekoliko drugače:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Uporabniške nastavitve** - konfiguracija strežnika se doda v globalno datoteko *settings.json* in je na voljo v vseh delovnih prostorih. Konfiguracija izgleda takole:

    ![Uporabniške nastavitve](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Prav tako morate dodati konfiguracijo, glavo, da se pravilno avtorizira proti Azure API Management. Uporablja se glava z imenom **Ocp-Apim-Subscription-Key**.

    - Tako jo lahko dodate v nastavitve:

    ![Dodajanje glave za avtorizacijo](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), to bo povzročilo prikaz poziva, kjer vnesete vrednost API ključa, ki ga najdete v Azure Portalu za vašo Azure API Management instanco.

   - Če jo želite dodati v *mcp.json*, lahko to storite tako:

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

### Uporaba načina agenta

Zdaj smo pripravljeni bodisi v nastavitvah bodisi v *.vscode/mcp.json*. Preizkusimo.

Moral bi se pojaviti gumb Orodja (Tools), kjer so navedena orodja, izpostavljena iz vašega strežnika:

![Orodja s strežnika](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Kliknite ikono orodij in videli boste seznam orodij:

    ![Orodja](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Vnesite ukaz v klepet za zagon orodja. Na primer, če ste izbrali orodje za pridobitev informacij o naročilu, lahko vprašate agenta o naročilu. Tukaj je primer ukaza:

    ```text
    get information from order 2
    ```

    Prikazal se bo gumb orodij, ki vas bo pozval, da nadaljujete z uporabo orodja. Izberite nadaljevanje in videli boste izhod, kot je ta:

    ![Rezultat ukaza](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **to, kar vidite zgoraj, je odvisno od orodij, ki ste jih nastavili, ideja pa je, da dobite besedilni odgovor, kot je prikazan zgoraj**


## Reference

Tukaj se lahko naučite več:

- [Vadnica o Azure API Management in MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python primer: Varnost oddaljenih MCP strežnikov z uporabo Azure API Management (eksperimentalno)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP klient laboratorij za avtorizacijo](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Uporaba razširitve Azure API Management za VS Code za uvoz in upravljanje API-jev](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Registracija in odkrivanje oddaljenih MCP strežnikov v Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Odličen repozitorij, ki prikazuje številne AI zmogljivosti z Azure API Management
- [AI Gateway delavnice](https://azure-samples.github.io/AI-Gateway/) Vsebuje delavnice z uporabo Azure Portala, kar je odličen način za začetek ocenjevanja AI zmogljivosti.

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za prevajanje z umetno inteligenco [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da avtomatizirani prevodi lahko vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za kakršnekoli nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne prevzemamo odgovornosti.