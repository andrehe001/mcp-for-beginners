<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5384bbb2a92d00d5d7e66274dbe0331d",
  "translation_date": "2025-06-20T18:43:35+00:00",
  "source_file": "04-PracticalImplementation/README.md",
  "language_code": "hu"
}
-->
# Gyakorlati megvalósítás

A gyakorlati megvalósítás az a pont, ahol a Model Context Protocol (MCP) ereje kézzelfoghatóvá válik. Bár fontos megérteni az MCP mögötti elméletet és architektúrát, az igazi érték akkor bontakozik ki, amikor ezeket a fogalmakat alkalmazod valós problémák megoldására, megoldásokat építesz, tesztelsz és telepítesz. Ez a fejezet hidat képez az elméleti tudás és a gyakorlati fejlesztés között, és végigvezet az MCP-alapú alkalmazások életre keltésének folyamatán.

Akár intelligens asszisztenseket fejlesztesz, AI-t integrálsz üzleti folyamatokba, vagy egyedi eszközöket készítesz adatfeldolgozáshoz, az MCP rugalmas alapot biztosít. Nyelvfüggetlen kialakítása és a népszerű programozási nyelvekhez készült hivatalos SDK-k révén széles fejlesztői kör számára elérhető. Ezeknek az SDK-knak a segítségével gyorsan prototípust készíthetsz, iterálhatsz és méretezheted megoldásaidat különböző platformokon és környezetekben.

A következő szakaszokban gyakorlati példákat, mintakódokat és telepítési stratégiákat találsz, amelyek bemutatják, hogyan valósítható meg az MCP C#, Java, TypeScript, JavaScript és Python nyelveken. Megtanulod továbbá, hogyan hibakeresd és teszteld MCP szervereidet, hogyan kezeld az API-kat, és hogyan telepíts megoldásokat az Azure felhőbe. Ezek a gyakorlati anyagok felgyorsítják a tanulásodat, és segítenek magabiztosan építeni robosztus, éles környezetbe szánt MCP alkalmazásokat.

## Áttekintés

Ez a lecke az MCP megvalósítás gyakorlati aspektusaira fókuszál több programozási nyelven keresztül. Megvizsgáljuk, hogyan használhatók az MCP SDK-k C#, Java, TypeScript, JavaScript és Python nyelveken stabil alkalmazások építéséhez, MCP szerverek hibakereséséhez és teszteléséhez, valamint újrahasznosítható erőforrások, promptok és eszközök létrehozásához.

## Tanulási célok

A lecke végére képes leszel:
- MCP megoldásokat megvalósítani hivatalos SDK-k segítségével különböző programozási nyelveken
- MCP szervereket rendszerszerűen hibakeresni és tesztelni
- Szerverfunkciókat létrehozni és használni (Erőforrások, Promptok és Eszközök)
- Hatékony MCP munkafolyamatokat tervezni összetett feladatokhoz
- Optimalizálni az MCP megvalósításokat teljesítmény és megbízhatóság szempontjából

## Hivatalos SDK erőforrások

A Model Context Protocol több nyelvhez is kínál hivatalos SDK-kat:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) 
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

## MCP SDK-k használata

Ebben a szakaszban gyakorlati példákat találsz az MCP megvalósítására több programozási nyelven. A mintakódokat a `samples` könyvtárban nyelv szerint rendezve találod.

### Elérhető minták

A tároló tartalmaz [mintamegvalósításokat](../../../04-PracticalImplementation/samples) az alábbi nyelveken:

- [C#](./samples/csharp/README.md)
- [Java](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Minden minta bemutatja az adott nyelv és ökoszisztéma kulcsfontosságú MCP koncepcióit és megvalósítási mintáit.

## Alapszerver funkciók

Az MCP szerverek bármilyen kombinációban megvalósíthatják az alábbi funkciókat:

### Erőforrások
Az erőforrások kontextust és adatokat szolgáltatnak a felhasználónak vagy az AI modellnek:
- Dokumentumtárak
- Tudásbázisok
- Strukturált adatforrások
- Fájlrendszerek

### Promptok
A promptok sablonos üzenetek és munkafolyamatok a felhasználók számára:
- Előre definiált beszélgetési sablonok
- Irányított interakciós minták
- Speciális párbeszédstruktúrák

### Eszközök
Az eszközök olyan funkciók, amelyeket az AI modell végrehajt:
- Adatfeldolgozó segédprogramok
- Külső API integrációk
- Számítási képességek
- Keresési funkciók

## Mintamegvalósítások: C#

A hivatalos C# SDK tároló több mintamegvalósítást tartalmaz, amelyek az MCP különböző aspektusait mutatják be:

- **Alap MCP kliens**: Egyszerű példa arra, hogyan hozhatsz létre MCP klienst és hívhatsz eszközöket
- **Alap MCP szerver**: Minimális szerver megvalósítás alapvető eszközregisztrációval
- **Fejlett MCP szerver**: Teljes funkcionalitású szerver eszközregisztrációval, hitelesítéssel és hibakezeléssel
- **ASP.NET integráció**: Példák az ASP.NET Core integrációjára
- **Eszköz megvalósítási minták**: Különböző minták eszközök megvalósításához különböző komplexitási szinteken

A MCP C# SDK előnézeti fázisban van, az API-k változhatnak. A blogot folyamatosan frissítjük az SDK fejlődésével.

### Kulcsfunkciók
- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)

- Első MCP szervered felépítése: [Build your first MCP Server](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

A teljes C# megvalósítási példákért látogass el a [hivatalos C# SDK minták tárolójába](https://github.com/modelcontextprotocol/csharp-sdk)

## Mintamegvalósítás: Java megvalósítás

A Java SDK robosztus MCP megvalósítási lehetőségeket kínál vállalati szintű funkciókkal.

### Kulcsfunkciók

- Spring Framework integráció
- Erős típusbiztonság
- Reaktív programozás támogatása
- Átfogó hibakezelés

Teljes Java megvalósítási példa a mintakönyvtárban: [Java minta](samples/java/containerapp/README.md).

## Mintamegvalósítás: JavaScript megvalósítás

A JavaScript SDK könnyű és rugalmas megközelítést kínál az MCP megvalósításához.

### Kulcsfunkciók

- Node.js és böngésző támogatás
- Promise-alapú API
- Könnyű integráció Express és más keretrendszerekkel
- WebSocket támogatás streaminghez

Teljes JavaScript megvalósítási példa a mintakönyvtárban: [JavaScript minta](samples/javascript/README.md).

## Mintamegvalósítás: Python megvalósítás

A Python SDK pythonos megközelítést kínál az MCP megvalósításához, kiváló ML keretrendszer integrációkkal.

### Kulcsfunkciók

- Async/await támogatás az asyncio-val
- Flask és FastAPI integráció
- Egyszerű eszközregisztráció
- Natív integráció népszerű ML könyvtárakkal

Teljes Python megvalósítási példa a mintakönyvtárban: [Python minta](samples/python/README.md).

## API kezelés

Az Azure API Management remek megoldás arra, hogyan lehet biztosítani az MCP szervereket. Az ötlet az, hogy egy Azure API Management példányt helyezel az MCP szerver elé, és az kezeli az olyan funkciókat, amelyekre valószínűleg szükséged lesz, mint például:

- sebességkorlátozás
- tokenkezelés
- monitorozás
- terheléselosztás
- biztonság

### Azure minta

Íme egy Azure minta, amely pontosan ezt valósítja meg, azaz [MCP szerver létrehozása és védelme Azure API Managementtel](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Az alábbi képen látható az engedélyezési folyamat:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

A fenti képen a következők történnek:

- Hitelesítés/engedélyezés a Microsoft Entra segítségével történik.
- Az Azure API Management átjáróként működik, és szabályzatokat használ a forgalom irányítására és kezelésére.
- Az Azure Monitor naplózza az összes kérést további elemzés céljából.

#### Engedélyezési folyamat

Nézzük meg részletesebben az engedélyezési folyamatot:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP engedélyezési specifikáció

További információkért lásd a [MCP Authorization specifikációt](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization#2-10-third-party-authorization-flow).

## Távoli MCP szerver telepítése Azure-ra

Nézzük meg, hogyan telepíthetjük az előbb említett mintát:

1. Klónozd a tárolót

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

2. Regisztráld a `Microsoft.App` szolgáltatót

    ` resource provider.
    * If you are using Azure CLI, run `az provider register --namespace Microsoft.App --wait`.
    * If you are using Azure PowerShell, run `

    majd ellenőrizd a regisztráció állapotát:

    `. Then run `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` after some time to check if the registration is complete.

2. Run this [azd](https://aka.ms/azd) command to provision the api management service, function app(with code) and all other required Azure resources

    `

3. Futtasd ezt az [azd](https://aka.ms/azd) parancsot az API Management szolgáltatás, a funkcióalkalmazás (kóddal) és az összes szükséges Azure erőforrás létrehozásához

    ```shell
    azd up
    ```

    Ez a parancs telepíti az összes felhőbeli erőforrást az Azure-on.

### MCP Inspectorral való szervertesztelés

1. Egy **új terminál ablakban** telepítsd és indítsd el az MCP Inspectort

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Egy hasonló felületet kell látnod:

    ![Connect to Node inspector](../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.hu.png)

2. CTRL kattintással töltsd be az MCP Inspector webalkalmazást az app által megjelenített URL-ről (pl. http://127.0.0.1:6274/#resources)
3. Állítsd a szállítási típust `SSE`-re és **Csatlakozás**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

5. **Eszközök listázása**. Kattints egy eszközre és válaszd a **Run Tool** opciót.

Ha minden lépés sikeres volt, most már csatlakozva vagy az MCP szerverhez, és képes voltál eszközt hívni.

## MCP szerverek Azure-hoz

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Ezek a tárolók gyorsindító sablonok egyedi távoli MCP (Model Context Protocol) szerverek építéséhez és telepítéséhez Azure Functions segítségével Python, C# .NET vagy Node/TypeScript nyelveken.

A minták teljes megoldást nyújtanak, amely lehetővé teszi a fejlesztők számára, hogy:

- Lokálisan fejlesszenek és futtassanak: MCP szerver fejlesztése és hibakeresése helyi gépen
- Telepítsenek Azure-ra: Egyszerűen telepíthető a felhőbe egyetlen azd up paranccsal
- Kliensről csatlakozzanak: Különböző kliensek, köztük a VS Code Copilot ügynök mód és az MCP Inspector eszköz használatával csatlakozhatnak az MCP szerverhez

### Kulcsfontosságú funkciók:

- Biztonság tervezésből: Az MCP szerver kulcsokkal és HTTPS-sel van védve
- Hitelesítési lehetőségek: OAuth támogatás beépített hitelesítéssel és/vagy API Managementtel
- Hálózati izoláció: Lehetővé teszi a hálózati izolációt Azure Virtuális Hálózatok (VNET) használatával
- Szerver nélküli architektúra: Azure Functions skálázható, eseményvezérelt végrehajtáshoz
- Helyi fejlesztés: Átfogó helyi fejlesztési és hibakeresési támogatás
- Egyszerű telepítés: Egyszerűsített telepítési folyamat Azure-ra

A tároló tartalmazza az összes szükséges konfigurációs fájlt, forráskódot és infrastruktúra definíciót, hogy gyorsan elindulhass egy éles környezetbe szánt MCP szerver megvalósítással.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) – MCP mintamegvalósítás Azure Functions használatával Python nyelven

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) – MCP mintamegvalósítás Azure Functions használatával C# .NET nyelven

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) – MCP mintamegvalósítás Azure Functions használatával Node/TypeScript nyelven.

## Főbb tanulságok

- Az MCP SDK-k nyelvspecifikus eszközöket biztosítanak stabil MCP megoldások megvalósításához
- A hibakeresési és tesztelési folyamat kritikus a megbízható MCP alkalmazásokhoz
- Újrahasznosítható prompt sablonok teszik lehetővé az egységes AI interakciókat
- A jól megtervezett munkafolyamatok összetett feladatokat képesek koordinálni több eszköz használatával
- Az MCP megvalósításakor figyelembe kell venni a biztonságot, a teljesítményt és a hibakezelést

## Gyakorlat

Tervezzen egy gyakorlati MCP munkafolyamatot, amely egy valós problémát old meg az Ön területén:

1. Azonosítson 3-4 olyan eszközt, amelyek hasznosak lehetnek a probléma megoldásában
2. Készítsen munkafolyamat-diagramot, amely bemutatja, hogyan lépnek interakcióba ezek az eszközök
3. Valósítson meg egy alapvető verziót az egyik eszközből a preferált nyelvén
4. Készítsen egy prompt sablont, amely segíti a modellt az eszköz hatékony használatában

## További források


---

Következő: [Haladó témák](../05-AdvancedTopics/README.md)

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások tartalmazhatnak hibákat vagy pontatlanságokat. Az eredeti dokumentum az anyanyelvén tekintendő hiteles forrásnak. Fontos információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.