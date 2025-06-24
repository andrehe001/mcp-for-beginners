<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5384bbb2a92d00d5d7e66274dbe0331d",
  "translation_date": "2025-06-20T18:44:06+00:00",
  "source_file": "04-PracticalImplementation/README.md",
  "language_code": "cs"
}
-->
# Praktická implementace

Praktická implementace je moment, kdy se síla Model Context Protocolu (MCP) stává skutečně hmatatelnou. I když je důležité porozumět teorii a architektuře MCP, skutečná hodnota se projeví až při aplikaci těchto konceptů pro vytváření, testování a nasazování řešení, která řeší reálné problémy. Tato kapitola překonává propast mezi teoretickými znalostmi a praktickým vývojem a provede vás procesem oživení aplikací založených na MCP.

Ať už vyvíjíte inteligentní asistenty, integrujete AI do podnikových procesů nebo vytváříte vlastní nástroje pro zpracování dat, MCP poskytuje flexibilní základ. Jeho jazykově nezávislý design a oficiální SDK pro populární programovací jazyky zpřístupňují MCP širokému spektru vývojářů. Díky těmto SDK můžete rychle prototypovat, iterovat a škálovat svá řešení napříč různými platformami a prostředími.

V následujících sekcích najdete praktické příklady, ukázkový kód a strategie nasazení, které ukazují, jak implementovat MCP v C#, Javě, TypeScriptu, JavaScriptu a Pythonu. Naučíte se také, jak ladit a testovat MCP servery, spravovat API a nasazovat řešení do cloudu pomocí Azure. Tyto praktické zdroje jsou navrženy tak, aby urychlily vaše učení a pomohly vám sebejistě vyvíjet robustní a produkčně připravené MCP aplikace.

## Přehled

Tato lekce se zaměřuje na praktické aspekty implementace MCP v různých programovacích jazycích. Prozkoumáme, jak používat MCP SDK v C#, Javě, TypeScriptu, JavaScriptu a Pythonu k vytváření robustních aplikací, ladění a testování MCP serverů a tvorbě znovupoužitelných zdrojů, promptů a nástrojů.

## Výukové cíle

Na konci této lekce budete schopni:
- Implementovat MCP řešení pomocí oficiálních SDK v různých programovacích jazycích
- Systematicky ladit a testovat MCP servery
- Vytvářet a používat serverové funkce (Resources, Prompts a Tools)
- Navrhovat efektivní MCP workflow pro složité úkoly
- Optimalizovat MCP implementace pro výkon a spolehlivost

## Oficiální SDK zdroje

Model Context Protocol nabízí oficiální SDK pro několik jazyků:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) 
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

## Práce s MCP SDK

Tato sekce obsahuje praktické příklady implementace MCP v různých programovacích jazycích. Ukázkový kód najdete ve složce `samples` uspořádané podle jazyka.

### Dostupné ukázky

Repositář obsahuje [ukázkové implementace](../../../04-PracticalImplementation/samples) v těchto jazycích:

- [C#](./samples/csharp/README.md)
- [Java](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Každá ukázka demonstruje klíčové koncepty MCP a vzory implementace pro daný jazyk a ekosystém.

## Základní funkce serveru

MCP servery mohou implementovat libovolnou kombinaci těchto funkcí:

### Resources
Resources poskytují kontext a data pro uživatele nebo AI model:
- Repozitáře dokumentů
- Znalostní báze
- Strukturované datové zdroje
- Souborové systémy

### Prompts
Prompts jsou šablonované zprávy a workflow pro uživatele:
- Předdefinované šablony konverzací
- Řízené vzory interakce
- Specializované dialogové struktury

### Tools
Tools jsou funkce, které AI model může vykonávat:
- Nástroje pro zpracování dat
- Integrace s externími API
- Výpočetní schopnosti
- Funkce vyhledávání

## Ukázkové implementace: C#

Oficiální repositář C# SDK obsahuje několik ukázkových implementací, které demonstrují různé aspekty MCP:

- **Základní MCP klient**: Jednoduchý příklad, jak vytvořit MCP klienta a volat nástroje
- **Základní MCP server**: Minimální implementace serveru s registrací základních nástrojů
- **Pokročilý MCP server**: Plně vybavený server s registrací nástrojů, autentizací a zpracováním chyb
- **Integrace ASP.NET**: Příklady ukazující integraci s ASP.NET Core
- **Vzory implementace nástrojů**: Různé vzory pro implementaci nástrojů s různou úrovní složitosti

MCP C# SDK je ve fázi preview a API se mohou měnit. Tento blog budeme průběžně aktualizovat, jak SDK bude vyvíjeno.

### Klíčové funkce
- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)

- Vytvoření [prvního MCP serveru](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

Pro kompletní ukázky implementací v C# navštivte [oficiální repositář C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Ukázková implementace: Java

Java SDK nabízí robustní možnosti implementace MCP s funkcemi na úrovni podnikových aplikací.

### Klíčové funkce

- Integrace se Spring Frameworkem
- Silná typová bezpečnost
- Podpora reaktivního programování
- Komplexní zpracování chyb

Pro kompletní ukázku implementace v Javě si prohlédněte [Java sample](samples/java/containerapp/README.md) ve složce samples.

## Ukázková implementace: JavaScript

JavaScript SDK poskytuje lehký a flexibilní přístup k implementaci MCP.

### Klíčové funkce

- Podpora Node.js i prohlížeče
- API založené na Promise
- Snadná integrace s Express a dalšími frameworky
- Podpora WebSocket pro streamování

Pro kompletní ukázku implementace v JavaScriptu si prohlédněte [JavaScript sample](samples/javascript/README.md) ve složce samples.

## Ukázková implementace: Python

Python SDK nabízí pythonický přístup k implementaci MCP s vynikající integrací ML frameworků.

### Klíčové funkce

- Podpora async/await s asyncio
- Integrace s Flask a FastAPI
- Jednoduchá registrace nástrojů
- Nativní integrace s populárními ML knihovnami

Pro kompletní ukázku implementace v Pythonu si prohlédněte [Python sample](samples/python/README.md) ve složce samples.

## Správa API

Azure API Management je skvělým řešením, jak zabezpečit MCP servery. Myšlenkou je umístit instanci Azure API Management před váš MCP server a nechat ji spravovat funkce, které pravděpodobně budete chtít, jako jsou:

- omezení rychlosti (rate limiting)
- správa tokenů
- monitorování
- vyvažování zátěže
- zabezpečení

### Azure ukázka

Tady je ukázka z Azure, která přesně toto dělá, tedy [vytváří MCP server a zabezpečuje ho pomocí Azure API Management](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Podívejte se, jak probíhá autorizační tok na následujícím obrázku:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

Na obrázku výše se děje:

- Autentizace/autorizace probíhá pomocí Microsoft Entra.
- Azure API Management funguje jako brána a pomocí politik řídí a spravuje provoz.
- Azure Monitor zaznamenává všechny požadavky pro další analýzu.

#### Autorizační tok

Podívejme se na autorizační tok podrobněji:

![Sekvenční diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### Specifikace MCP autorizace

Více informací najdete v [MCP Authorization specification](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization#2-10-third-party-authorization-flow)

## Nasazení vzdáleného MCP serveru do Azure

Podívejme se, jestli můžeme nasadit ukázku, kterou jsme zmínili dříve:

1. Naklonujte repozitář

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

2. Zaregistrujte `Microsoft.App` resource provider.
    * If you are using Azure CLI, run `az provider register --namespace Microsoft.App --wait`.
    * If you are using Azure PowerShell, run `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Then run `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` a po chvíli zkontrolujte, zda je registrace dokončena.

3. Spusťte tento příkaz [azd](https://aka.ms/azd) k vytvoření služby API Management, funkční aplikace (s kódem) a všech dalších potřebných Azure zdrojů

    ```shell
    azd up
    ```

    Tento příkaz by měl nasadit všechny cloudové zdroje na Azure.

### Testování serveru pomocí MCP Inspector

1. V **novém terminálovém okně** nainstalujte a spusťte MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Měli byste vidět rozhraní podobné tomuto:

    ![Připojení k Node inspector](../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.cs.png)

2. CTRL kliknutím načtěte webovou aplikaci MCP Inspector z URL zobrazené aplikací (např. http://127.0.0.1:6274/#resources)
3. Nastavte typ přenosu na `SSE`
1. Set the URL to your running API Management SSE endpoint displayed after `azd up` a **Připojte se**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

5. **Vypsat nástroje**. Klikněte na nástroj a **Spusťte nástroj**.

Pokud vše proběhlo správně, nyní byste měli být připojeni k MCP serveru a mohli jste zavolat nástroj.

## MCP servery pro Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Tato sada repozitářů je šablona rychlého startu pro vytváření a nasazování vlastních vzdálených MCP (Model Context Protocol) serverů pomocí Azure Functions v Pythonu, C# .NET nebo Node/TypeScript.

Ukázky poskytují kompletní řešení, které umožňuje vývojářům:

- Vytvářet a spouštět lokálně: Vyvíjet a ladit MCP server na lokálním počítači
- Nasadit do Azure: Snadné nasazení do cloudu pomocí jednoduchého příkazu azd up
- Připojit se z klientů: Připojit se k MCP serveru z různých klientů včetně režimu agenta Copilot ve VS Code a nástroje MCP Inspector

### Klíčové funkce:

- Bezpečnost již v základu: MCP server je zabezpečen pomocí klíčů a HTTPS
- Možnosti autentizace: Podpora OAuth pomocí vestavěné autentizace a/nebo API Management
- Izolace sítě: Umožňuje síťovou izolaci pomocí Azure Virtual Networks (VNET)
- Serverless architektura: Využívá Azure Functions pro škálovatelné, událostmi řízené vykonávání
- Lokální vývoj: Komplexní podpora lokálního vývoje a ladění
- Jednoduché nasazení: Zjednodušený proces nasazení do Azure

Repozitář obsahuje všechny potřebné konfigurační soubory, zdrojový kód a definice infrastruktury, aby bylo možné rychle začít s produkčně připravenou implementací MCP serveru.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Ukázková implementace MCP pomocí Azure Functions v Pythonu

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Ukázková implementace MCP pomocí Azure Functions v C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Ukázková implementace MCP pomocí Azure Functions v Node/TypeScript.

## Hlavní poznatky

- MCP SDK poskytují jazykově specifické nástroje pro implementaci robustních MCP řešení
- Proces ladění a testování je klíčový pro spolehlivé MCP aplikace
- Znovupoužitelné šablony promptů umožňují konzistentní AI interakce
- Dobře navržená workflow mohou koordinovat složité úkoly pomocí více nástrojů
- Implementace MCP řešení vyžaduje zvážení bezpečnosti, výkonu a zpracování chyb

## Cvičení

Navrhněte praktický MCP workflow, který řeší reálný problém ve vašem oboru:

1. Identifikujte 3-4 nástroje, které by byly užitečné pro řešení tohoto problému
2. Vytvořte diagram workflow, který ukazuje, jak tyto nástroje spolupracují
3. Implementujte základní verzi jednoho z nástrojů ve vámi preferovaném jazyce
4. Vytvořte šablonu promptu, která pomůže modelu efektivně používat váš nástroj

## Další zdroje


---

Další: [Pokročilá témata](../05-AdvancedTopics/README.md)

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo chybné výklady vyplývající z použití tohoto překladu.