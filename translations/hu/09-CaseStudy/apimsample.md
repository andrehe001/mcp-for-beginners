<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "36de9fae488d6de554d969fe8e0801a8",
  "translation_date": "2025-06-20T19:24:05+00:00",
  "source_file": "09-CaseStudy/apimsample.md",
  "language_code": "hu"
}
-->
# Esettanulmány: REST API közzététele API Management-ben MCP szerverként

Az Azure API Management egy olyan szolgáltatás, amely egy átjárót biztosít az API végpontjaid felett. Lényege, hogy az Azure API Management proxyként működik az API-k előtt, és eldöntheti, hogyan kezelje a bejövő kéréseket.

Használatával számos funkciót adhatsz hozzá, például:

- **Biztonság**, használhatsz API kulcsokat, JWT-t vagy menedzselt identitást.
- **Hívásszám korlátozás**, egy nagyszerű funkció, amellyel megadhatod, hogy adott időegységenként hány hívás engedélyezett. Ez segít abban, hogy minden felhasználó jó élményt kapjon, és a szolgáltatásod ne legyen túlterhelve.
- **Skálázás és terheléselosztás**. Több végpontot állíthatsz be a terhelés kiegyenlítésére, és eldöntheted, hogyan történjen a terheléselosztás.
- **Mesterséges intelligencia funkciók, mint a szemantikus gyorsítótárazás**, token limit és token monitorozás, és még sok más. Ezek a funkciók javítják a válaszadási sebességet, és segítenek nyomon követni a token felhasználást. [További információ](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Miért MCP + Azure API Management?

A Model Context Protocol gyorsan szabvánnyá válik az ügynökalapú AI alkalmazásoknál, és arra, hogy eszközöket és adatokat egységes módon tegyünk elérhetővé. Az Azure API Management természetes választás, ha API-kat kell "kezelni". Az MCP szerverek gyakran integrálódnak más API-kkal, hogy például eszközökhöz továbbítsák a kéréseket. Ezért az Azure API Management és az MCP együttes használata nagyon logikus.

## Áttekintés

Ebben a konkrét esetben megtanuljuk, hogyan tegyünk elérhetővé API végpontokat MCP szerverként. Így könnyedén beilleszthetjük ezeket az ügynökalapú alkalmazásba, miközben kihasználjuk az Azure API Management funkcióit.

## Főbb jellemzők

- Kiválaszthatod, mely végpont metódusokat szeretnéd eszközként elérhetővé tenni.
- A további funkciók attól függnek, hogy milyen szabályokat állítasz be az API policy szekciójában. Itt megmutatjuk, hogyan adhatsz hozzá hívásszám korlátozást.

## Előfeltétel: API importálása

Ha már van API-d az Azure API Management-ben, akkor ezt a lépést átugorhatod. Ha nincs, nézd meg ezt a linket: [API importálása az Azure API Management-be](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## API közzététele MCP szerverként

Az API végpontok közzétételéhez kövesd az alábbi lépéseket:

1. Navigálj az Azure Portalra a következő címen: <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
Nyisd meg az API Management példányodat.

1. A bal oldali menüben válaszd az APIs > MCP Servers > + Create new MCP Server menüpontot.

1. Az API-nál válassz egy REST API-t, amelyet MCP szerverként szeretnél közzétenni.

1. Válassz ki egy vagy több API műveletet, amelyeket eszközként szeretnél elérhetővé tenni. Kiválaszthatod az összes műveletet vagy csak bizonyosakat.

    ![Válaszd ki az elérhető metódusokat](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Kattints a **Create** gombra.

1. Navigálj az **APIs** > **MCP Servers** menüpontra, itt a következőt kell látnod:

    ![Az MCP szerver megjelenése a fő nézetben](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    Az MCP szerver létrejött, és az API műveletek eszközként elérhetővé váltak. Az MCP szerver megjelenik az MCP Servers panelen. Az URL oszlopban látható az MCP szerver végpontja, amelyet teszteléshez vagy kliens alkalmazásból hívhatsz.

## Opcionális: Szabályok konfigurálása

Az Azure API Management alapelve a szabályok (policies), ahol különféle szabályokat állíthatsz be a végpontokra, például hívásszám korlátozást vagy szemantikus gyorsítótárazást. Ezeket a szabályokat XML-ben írják.

Így állíthatsz be szabályt a MCP szerver hívásszám korlátozására:

1. A portálon az APIs alatt válaszd a **MCP Servers**-t.

1. Válaszd ki a létrehozott MCP szervert.

1. A bal oldali menüben, az MCP alatt válaszd a **Policies**-t.

1. A szabály szerkesztőben add hozzá vagy szerkeszd a kívánt szabályokat az MCP szerver eszközeihez. A szabályokat XML formátumban kell megadni. Például hozzáadhatsz egy szabályt, amely korlátozza a hívásokat (ebben a példában 5 hívás 30 másodpercenként egy kliens IP címről). Az alábbi XML korlátozni fogja a hívásokat:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Íme egy kép a szabály szerkesztőről:

    ![Szabály szerkesztő](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Próbáld ki

Győződjünk meg róla, hogy az MCP szerverünk a várt módon működik.

Ehhez a Visual Studio Code-ot és a GitHub Copilot Agent módját fogjuk használni. Az MCP szervert hozzáadjuk egy *mcp.json* fájlhoz. Így a Visual Studio Code kliensként fog működni ügynökalapú képességekkel, és a végfelhasználók promptokat írhatnak, majd kommunikálhatnak a szerverrel.

Nézzük, hogyan adjuk hozzá az MCP szervert a Visual Studio Code-ban:

1. Használd a MCP: **Add Server parancsot a Command Palette-ben**.

1. Amikor kéri, válaszd ki a szerver típusát: **HTTP (HTTP vagy Server Sent Events)**.

1. Írd be az MCP szerver URL-jét az API Management-ben. Például: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (SSE végpont esetén) vagy **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (MCP végpont esetén), vedd észre a különbséget a protokollok között: `/sse` or `/mcp`.

1. Adj meg egy tetszőleges szerver azonosítót. Ez nem kritikus érték, de segít emlékezni, melyik szerver példányról van szó.

1. Válaszd ki, hogy a konfigurációt a workspace vagy a user beállításokhoz szeretnéd menteni.

  - **Workspace beállítások** - A szerver konfigurációja egy .vscode/mcp.json fájlba kerül, amely csak az aktuális munkaterületen érhető el.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    vagy ha streaming HTTP protokollt választasz, akkor kicsit másképp néz ki:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **User beállítások** - A szerver konfigurációja a globális *settings.json* fájlba kerül, és minden munkaterületen elérhető. A konfiguráció hasonló a következőhöz:

    ![User beállítás](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Hozzá kell adnod egy konfigurációt, egy fejlécet, hogy megfelelően hitelesítsen az Azure API Management felé. Ehhez egy **Ocp-Apim-Subscription-Key** nevű fejlécet használ.

    - Így adhatod hozzá a beállításokhoz:

    ![Hitelesítő fejléc hozzáadása](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), ez egy promptot fog megjeleníteni, ahol meg kell adnod az API kulcs értékét, amit az Azure Portálon találsz az Azure API Management példányodhoz.

   - Ha inkább a *mcp.json*-hez szeretnéd hozzáadni, így teheted meg:

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

### Ügynök mód használata

Most, hogy beállítottuk akár a beállításokban, akár a *.vscode/mcp.json* fájlban, próbáljuk ki.

Látnod kell egy Eszközök ikont, ahol a szerver által elérhetővé tett eszközök listája jelenik meg:

![Szerver eszközei](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Kattints az eszköz ikonra, és megjelenik az eszközök listája:

    ![Eszközök](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Írj be egy promptot a csevegésbe az eszköz meghívásához. Például, ha kiválasztottál egy eszközt, amely rendelés információt ad, kérdezhetsz a rendelésről az ügynöktől. Íme egy példa prompt:

    ```text
    get information from order 2
    ```

    Most megjelenik egy eszköz ikon, amely megkérdezi, hogy folytatod-e az eszköz hívását. Válaszd a folytatást, és a következőhöz hasonló eredményt kell látnod:

    ![Eredmény a promptból](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **ami fent látható, az attól függ, milyen eszközöket állítottál be, de az ötlet az, hogy szöveges választ kapj, mint fent**


## Hivatkozások

Így tudsz többet megtudni:

- [Azure API Management és MCP bemutató](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python példa: Távoli MCP szerverek biztonságos használata Azure API Management segítségével (kísérleti)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP kliens engedélyezési labor](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Használd az Azure API Management bővítményt VS Code-hoz API-k importálásához és kezeléséhez](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Távoli MCP szerverek regisztrálása és felfedezése az Azure API Center-ben](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Nagyszerű repó, amely sok AI funkciót mutat be az Azure API Management segítségével
- [AI Gateway workshopok](https://azure-samples.github.io/AI-Gateway/) Tartalmaz workshopokat az Azure Portál használatával, ami remek módja az AI képességek kipróbálásának.

**Felelősségkizárás**:  
Ez a dokumentum az AI fordítószolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum anyanyelvű változatát kell tekinteni hiteles forrásnak. Kritikus információk esetén professzionális emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.