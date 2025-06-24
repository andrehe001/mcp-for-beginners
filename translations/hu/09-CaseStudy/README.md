<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6940b1e931e51821b219aa9dcfe8c4ee",
  "translation_date": "2025-06-23T11:15:30+00:00",
  "source_file": "09-CaseStudy/README.md",
  "language_code": "hu"
}
-->
# MCP a gyakorlatban: Valós esettanulmányok

A Model Context Protocol (MCP) átalakítja, hogyan lépnek kapcsolatba az AI-alkalmazások az adatokkal, eszközökkel és szolgáltatásokkal. Ez a szakasz valós esettanulmányokat mutat be, amelyek az MCP gyakorlati alkalmazásait szemléltetik különböző vállalati helyzetekben.

## Áttekintés

Ebben a részben konkrét MCP-megvalósításokat láthatunk, amelyek kiemelik, hogyan használják a szervezetek ezt a protokollt összetett üzleti kihívások megoldására. Ezeknek az esettanulmányoknak a vizsgálatával betekintést nyerhetsz az MCP sokoldalúságába, skálázhatóságába és a valós helyzetekben nyújtott gyakorlati előnyeibe.

## Fő tanulási célok

Az esettanulmányok megismerésével:

- Megérted, hogyan alkalmazható az MCP konkrét üzleti problémák megoldására
- Megtanulod a különböző integrációs mintákat és architekturális megközelítéseket
- Felismered a legjobb gyakorlatokat az MCP vállalati környezetben történő bevezetéséhez
- Beletekintést nyersz a valós megvalósítások során felmerülő kihívásokba és megoldásokba
- Lehetőségeket azonosítasz arra, hogy hasonló mintákat alkalmazz a saját projektjeidben

## Kiemelt esettanulmányok

### 1. [Azure AI Utazási Ügynökök – Referenciamegvalósítás](./travelagentsample.md)

Ez az esettanulmány bemutatja a Microsoft átfogó referencia megoldását, amely megmutatja, hogyan lehet MCP, Azure OpenAI és Azure AI Search segítségével többügynökös, mesterséges intelligencia-alapú utazástervező alkalmazást építeni. A projekt bemutatja:

- Többügynökös koordináció MCP-n keresztül
- Vállalati adat integráció Azure AI Search segítségével
- Biztonságos, skálázható architektúra Azure szolgáltatásokkal
- Bővíthető eszköztár újrahasznosítható MCP komponensekkel
- Beszélgetés-alapú felhasználói élmény Azure OpenAI támogatással

Az architektúra és a megvalósítás részletei értékes betekintést nyújtanak összetett, többügynökös rendszerek építéséhez MCP mint koordinációs réteg használatával.

### 2. [Azure DevOps elemek frissítése YouTube adatok alapján](./UpdateADOItemsFromYT.md)

Ez az esettanulmány egy gyakorlati MCP alkalmazást mutat be munkafolyamatok automatizálására. Megtudhatod, hogyan használhatók az MCP eszközök az alábbiakhoz:

- Adatok kinyerése online platformokról (YouTube)
- Munkafeladatok frissítése Azure DevOps rendszerekben
- Ismételhető automatizált munkafolyamatok létrehozása
- Adatintegráció különböző rendszerek között

Ez a példa megmutatja, hogy még viszonylag egyszerű MCP-megvalósítások is jelentős hatékonyságnövekedést eredményezhetnek a rutinfeladatok automatizálásával és az adatok konzisztenciájának javításával.

### 3. [Valós idejű dokumentáció lekérése MCP-vel](./docs-mcp/README.md)

Ez az esettanulmány végigvezet azon, hogyan csatlakoztathatsz egy Python konzolos klienset egy Model Context Protocol (MCP) szerverhez, hogy valós idejű, kontextusérzékeny Microsoft dokumentációt kérj le és naplózz. Megtanulhatod, hogyan:

- Csatlakozz MCP szerverhez Python kliens és hivatalos MCP SDK segítségével
- Használj streaming HTTP klienset hatékony, valós idejű adatlekéréshez
- Hívj dokumentációs eszközöket a szerveren és naplózd a válaszokat közvetlenül a konzolra
- Integráld a naprakész Microsoft dokumentációt munkafolyamataidba anélkül, hogy elhagynád a terminált

A fejezet gyakorlati feladatot, minimális működő kódmintát és további forrásokra mutató linkeket tartalmaz a mélyebb tanuláshoz. A teljes lépésről-lépésre útmutatót és a kódot a hivatkozott fejezetben találod, hogy megértsd, miként változtathatja meg az MCP a dokumentációhoz való hozzáférést és a fejlesztői hatékonyságot konzolos környezetben.

### 4. [Interaktív tanulási terv generátor webalkalmazás MCP-vel](./docs-mcp/README.md)

Ez az esettanulmány bemutatja, hogyan építhetsz interaktív webalkalmazást Chainlit és a Model Context Protocol (MCP) segítségével, amely személyre szabott tanulási terveket készít bármilyen témában. A felhasználók megadhatnak egy tárgyat (például „AI-900 tanúsítvány”) és tanulási időtartamot (pl. 8 hét), az alkalmazás pedig heti bontásban javasol tartalmakat. A Chainlit beszélgetés-alapú chatfelületet biztosít, így az élmény interaktív és alkalmazkodó.

- Beszélgetés-alapú webalkalmazás Chainlit-tel
- Felhasználói vezérelt témakör és időtartam megadása
- Heti bontású tartalomajánlások MCP segítségével
- Valós idejű, alkalmazkodó válaszok chatfelületen

A projekt bemutatja, hogyan kombinálható a beszélgetés-alapú AI és az MCP dinamikus, felhasználóközpontú oktatási eszközök létrehozásához modern webes környezetben.

### 5. [Szerkesztőn belüli dokumentáció MCP szerverrel VS Code-ban](./docs-mcp/README.md)

Ez az esettanulmány megmutatja, hogyan hozhatod be a Microsoft Learn dokumentációt közvetlenül a VS Code környezetedbe MCP szerver segítségével — így nem kell böngészőfüleket váltogatnod! Megtudhatod, hogyan:

- Azonnal kereshetsz és olvashatsz dokumentációt VS Code-on belül az MCP panel vagy parancspaletta használatával
- Hivatkozhatsz dokumentációra és illeszthetsz be linkeket közvetlenül README vagy tananyagos markdown fájlokba
- Együtt használhatod a GitHub Copilot-ot és az MCP-t zökkenőmentes, AI-alapú dokumentációs és kódmunkafolyamatokhoz
- Valós idejű visszajelzéssel és Microsoft által biztosított pontossággal validálhatod és javíthatod dokumentációdat
- Integrálhatod az MCP-t GitHub munkafolyamatokkal a folyamatos dokumentációellenőrzéshez

A megvalósítás tartalmazza:
- Példa `.vscode/mcp.json` konfigurációt az egyszerű beállításhoz
- Képernyőképekkel illusztrált útmutatókat a szerkesztőn belüli élményhez
- Tippeket a Copilot és MCP együttes használatához a maximális termelékenység érdekében

Ez a megoldás ideális tananyagfejlesztőknek, dokumentációíróknak és fejlesztőknek, akik szeretnének a szerkesztőjükben maradva dolgozni a dokumentációval, Copilot-tal és validációs eszközökkel — mindezt MCP által támogatva.

### 6. [APIM MCP szerver létrehozása](./apimsample.md)

Ez az esettanulmány lépésről lépésre bemutatja, hogyan készíthetsz MCP szervert Azure API Management (APIM) segítségével. Lefedi:

- MCP szerver beállítása Azure API Management-ben
- API műveletek MCP eszközökként történő közzététele
- Házirendek konfigurálása a sebességkorlátozás és biztonság érdekében
- MCP szerver tesztelése Visual Studio Code és GitHub Copilot segítségével

Ez a példa megmutatja, hogyan használhatod ki az Azure lehetőségeit egy megbízható MCP szerver létrehozásához, amely különböző alkalmazásokban javítja az AI rendszerek és vállalati API-k integrációját.

## Összegzés

Ezek az esettanulmányok kiemelik a Model Context Protocol sokoldalúságát és gyakorlati alkalmazásait valós helyzetekben. Az összetett többügynökös rendszerektől a célzott automatizált munkafolyamatokig az MCP egységes módot kínál arra, hogy az AI rendszerek összekapcsolódjanak a szükséges eszközökkel és adatokkal, így értéket teremtsenek.

Ezeknek a megvalósításoknak a tanulmányozásával betekintést nyerhetsz az architekturális mintákba, megvalósítási stratégiákba és legjobb gyakorlatokba, amelyeket a saját MCP projektjeidben is alkalmazhatsz. A példák bizonyítják, hogy az MCP nem pusztán elméleti keretrendszer, hanem valós üzleti kihívásokra adott gyakorlati megoldás.

## További források

- [Azure AI Travel Agents GitHub tár](https://github.com/Azure-Samples/azure-ai-travel-agents)
- [Azure DevOps MCP eszköz](https://github.com/microsoft/azure-devops-mcp)
- [Playwright MCP eszköz](https://github.com/microsoft/playwright-mcp)
- [Microsoft Docs MCP szerver](https://github.com/MicrosoftDocs/mcp)
- [MCP közösségi példák](https://github.com/microsoft/mcp)

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár a pontosságra törekszünk, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum anyanyelvű változatát kell tekinteni a hiteles forrásnak. Kritikus információk esetén szakmai, emberi fordítást javaslunk. Nem vállalunk felelősséget az ezen fordítás használatából eredő félreértésekért vagy félreértelmezésekért.