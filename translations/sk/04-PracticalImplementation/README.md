<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5384bbb2a92d00d5d7e66274dbe0331d",
  "translation_date": "2025-06-20T18:44:32+00:00",
  "source_file": "04-PracticalImplementation/README.md",
  "language_code": "sk"
}
-->
# Praktická implementácia

Praktická implementácia je moment, kedy sa sila Model Context Protocolu (MCP) stáva hmatateľnou. Aj keď je dôležité pochopiť teóriu a architektúru MCP, skutočná hodnota sa prejaví, keď tieto koncepty použijete na vytváranie, testovanie a nasadzovanie riešení, ktoré riešia reálne problémy. Táto kapitola prekladá medzeru medzi konceptuálnymi znalosťami a praktickým vývojom a vedie vás procesom oživenia aplikácií založených na MCP.

Či už vyvíjate inteligentných asistentov, integrujete AI do podnikových pracovných tokov alebo tvoríte vlastné nástroje na spracovanie dát, MCP poskytuje flexibilný základ. Jeho nezávislý dizajn na programovacom jazyku a oficiálne SDK pre populárne jazyky ho sprístupňujú širokému spektru vývojárov. Využitím týchto SDK môžete rýchlo prototypovať, iterovať a škálovať riešenia na rôznych platformách a prostrediach.

V nasledujúcich častiach nájdete praktické príklady, ukážkový kód a stratégie nasadenia, ktoré demonštrujú, ako implementovať MCP v C#, Jave, TypeScripte, JavaScripte a Pythone. Tiež sa naučíte, ako debugovať a testovať MCP servery, spravovať API a nasadzovať riešenia do cloudu pomocou Azure. Tieto praktické zdroje sú navrhnuté tak, aby zrýchlili vaše učenie a pomohli vám sebavedome vytvárať robustné, produkčne pripravené MCP aplikácie.

## Prehľad

Táto lekcia sa zameriava na praktické aspekty implementácie MCP naprieč viacerými programovacími jazykmi. Preskúmame, ako používať MCP SDK v C#, Jave, TypeScripte, JavaScripte a Pythone na tvorbu robustných aplikácií, debugovanie a testovanie MCP serverov a vytváranie opakovane použiteľných zdrojov, promptov a nástrojov.

## Ciele učenia

Na konci tejto lekcie budete schopní:
- Implementovať MCP riešenia pomocou oficiálnych SDK v rôznych programovacích jazykoch
- Systematicky debugovať a testovať MCP servery
- Vytvárať a používať funkcie servera (Resources, Prompts a Tools)
- Navrhovať efektívne MCP pracovné toky pre zložité úlohy
- Optimalizovať implementácie MCP pre výkon a spoľahlivosť

## Oficiálne SDK zdroje

Model Context Protocol ponúka oficiálne SDK pre viaceré jazyky:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

## Práca s MCP SDK

Táto sekcia poskytuje praktické príklady implementácie MCP v rôznych programovacích jazykoch. Ukážkový kód nájdete v priečinku `samples` usporiadanom podľa jazyka.

### Dostupné ukážky

Repozitár obsahuje [ukážkové implementácie](../../../04-PracticalImplementation/samples) v nasledujúcich jazykoch:

- [C#](./samples/csharp/README.md)
- [Java](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Každá ukážka demonštruje kľúčové koncepty MCP a vzory implementácie pre daný jazyk a ekosystém.

## Základné funkcie servera

MCP servery môžu implementovať akúkoľvek kombináciu týchto funkcií:

### Resources  
Resources poskytujú kontext a dáta, ktoré používateľ alebo AI model využívajú:
- Úložiská dokumentov
- Znalostné bázy
- Štruktúrované dátové zdroje
- Súborové systémy

### Prompts  
Prompts sú šablónované správy a pracovné toky pre používateľov:
- Preddefinované šablóny konverzácií
- Usmernené vzory interakcie
- Špecializované dialógové štruktúry

### Tools  
Tools sú funkcie, ktoré AI model vykonáva:
- Nástroje na spracovanie dát
- Integrácie s externými API
- Výpočtové schopnosti
- Vyhľadávacie funkcie

## Ukážkové implementácie: C#

Oficiálny repozitár C# SDK obsahuje niekoľko ukážkových implementácií, ktoré demonštrujú rôzne aspekty MCP:

- **Základný MCP klient**: Jednoduchý príklad, ako vytvoriť MCP klienta a volať nástroje
- **Základný MCP server**: Minimálna implementácia servera so základnou registráciou nástrojov
- **Pokročilý MCP server**: Plnohodnotný server s registráciou nástrojov, autentifikáciou a spracovaním chýb
- **Integrácia ASP.NET**: Príklady ukazujúce integráciu s ASP.NET Core
- **Vzory implementácie nástrojov**: Rôzne vzory pre implementáciu nástrojov s rôznou mierou zložitosti

C# SDK MCP je vo verzii preview a API sa môžu meniť. Tento blog budeme priebežne aktualizovať podľa vývoja SDK.

### Kľúčové funkcie  
- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)

- Vytvorenie [prvého MCP servera](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

Pre kompletné ukážky implementácie v C# navštívte [oficiálny repozitár C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Ukážková implementácia: Java

Java SDK ponúka robustné možnosti implementácie MCP s funkciami na úrovni podnikov.

### Kľúčové funkcie

- Integrácia so Spring Framework
- Silná typová bezpečnosť
- Podpora reaktívneho programovania
- Komplexné spracovanie chýb

Pre kompletný príklad implementácie v Jave pozrite [Java sample](samples/java/containerapp/README.md) v priečinku so vzorkami.

## Ukážková implementácia: JavaScript

JavaScript SDK poskytuje ľahký a flexibilný prístup k implementácii MCP.

### Kľúčové funkcie

- Podpora Node.js aj prehliadača
- API založené na Promise
- Jednoduchá integrácia s Express a ďalšími frameworkmi
- Podpora WebSocket pre streaming

Pre kompletný príklad implementácie v JavaScripte pozrite [JavaScript sample](samples/javascript/README.md) v priečinku so vzorkami.

## Ukážková implementácia: Python

Python SDK ponúka „pythonický“ prístup k implementácii MCP s výbornou integráciou do ML frameworkov.

### Kľúčové funkcie

- Podpora async/await s asyncio
- Integrácia s Flask a FastAPI
- Jednoduchá registrácia nástrojov
- Nativna integrácia s populárnymi ML knižnicami

Pre kompletný príklad implementácie v Pythone pozrite [Python sample](samples/python/README.md) v priečinku so vzorkami.

## Správa API

Azure API Management je skvelým riešením, ako zabezpečiť MCP servery. Myšlienka je umiestniť Azure API Management inštanciu pred váš MCP server a nechať ju spravovať funkcie, ktoré pravdepodobne budete potrebovať, ako napríklad:

- obmedzovanie počtu požiadaviek (rate limiting)
- správa tokenov
- monitorovanie
- vyvažovanie záťaže
- bezpečnosť

### Azure príklad

Tu je Azure príklad, ktorý robí presne toto, teda [vytvára MCP server a zabezpečuje ho pomocou Azure API Management](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Pozrite sa, ako prebieha autorizácia na nasledujúcom obrázku:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

Na obrázku sa deje nasledovné:

- Autentifikácia/autorizácia prebieha pomocou Microsoft Entra.
- Azure API Management funguje ako brána a používa politiky na smerovanie a správu prevádzky.
- Azure Monitor zaznamenáva všetky požiadavky na ďalšiu analýzu.

#### Priebeh autorizácie

Pozrime sa podrobnejšie na priebeh autorizácie:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### Špecifikácia MCP autorizácie

Viac informácií nájdete v [MCP Authorization specification](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization#2-10-third-party-authorization-flow)

## Nasadenie vzdialeného MCP servera na Azure

Pozrime sa, či dokážeme nasadiť ukážku, ktorú sme spomenuli vyššie:

1. Klonujte repozitár

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

2. Zaregistrujte `Microsoft.App` resource provider.
    * If you are using Azure CLI, run `az provider register --namespace Microsoft.App --wait`.
    * If you are using Azure PowerShell, run `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Then run `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` a po chvíli skontrolujte, či je registrácia dokončená.

3. Spustite tento príkaz [azd](https://aka.ms/azd) na vytvorenie služby API Management, funkčnej aplikácie (s kódom) a všetkých ďalších potrebných Azure zdrojov

    ```shell
    azd up
    ```

    Tento príkaz by mal nasadiť všetky cloudové zdroje na Azure.

### Testovanie servera pomocou MCP Inspector

1. V **novom terminálovom okne** nainštalujte a spustite MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Mali by ste vidieť rozhranie podobné tomuto:

    ![Connect to Node inspector](../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.sk.png)

2. CTRL kliknite, aby ste načítali MCP Inspector webovú aplikáciu z URL zobrazeného v aplikácii (napr. http://127.0.0.1:6274/#resources)
3. Nastavte typ transportu na `SSE`
1. Set the URL to your running API Management SSE endpoint displayed after `azd up` a **Pripojte sa**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

5. **Zoznam nástrojov**. Kliknite na nástroj a **Spustite nástroj**.

Ak všetky kroky prebehli úspešne, teraz ste pripojení k MCP serveru a podarilo sa vám zavolať nástroj.

## MCP servery pre Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Táto sada repozitárov je šablónou pre rýchly štart na vytváranie a nasadzovanie vlastných vzdialených MCP (Model Context Protocol) serverov pomocou Azure Functions v Pythone, C# .NET alebo Node/TypeScript.

Ukážky poskytujú kompletné riešenie, ktoré umožňuje vývojárom:

- Vytvárať a spúšťať lokálne: Vyvíjať a debugovať MCP server na lokálnom počítači
- Nasadiť na Azure: Jednoducho nasadiť do cloudu pomocou jednoduchého príkazu azd up
- Pripojiť sa z klientov: Pripojiť sa k MCP serveru z rôznych klientov vrátane režimu agenta Copilot vo VS Code a nástroja MCP Inspector

### Kľúčové vlastnosti:

- Bezpečnosť už v základe: MCP server je zabezpečený pomocou kľúčov a HTTPS
- Možnosti autentifikácie: Podpora OAuth s natívnou autentifikáciou a/alebo API Management
- Izolácia siete: Umožňuje izoláciu siete pomocou Azure Virtual Networks (VNET)
- Serverless architektúra: Využíva Azure Functions pre škálovateľné, udalostne riadené vykonávanie
- Lokálny vývoj: Komplexná podpora lokálneho vývoja a debugovania
- Jednoduché nasadenie: Zjednodušený proces nasadenia do Azure

Repozitár obsahuje všetky potrebné konfiguračné súbory, zdrojový kód a definície infraštruktúry, aby ste mohli rýchlo začať s produkčne pripravenou implementáciou MCP servera.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Ukážková implementácia MCP pomocou Azure Functions v Pythone

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Ukážková implementácia MCP pomocou Azure Functions v C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Ukážková implementácia MCP pomocou Azure Functions v Node/TypeScript.

## Kľúčové poznatky

- MCP SDK poskytujú jazykovo špecifické nástroje na implementáciu robustných MCP riešení
- Proces debugovania a testovania je kritický pre spoľahlivé MCP aplikácie
- Opakovane použiteľné šablóny promptov umožňujú konzistentnú AI interakciu
- Dobre navrhnuté pracovné toky dokážu koordinovať zložité úlohy s využitím viacerých nástrojov
- Implementácia MCP riešení vyžaduje zohľadnenie bezpečnosti, výkonu a spracovania chýb

## Cvičenie

Navrhnite praktický MCP pracovný tok, ktorý rieši reálny problém vo vašej oblasti:

1. Identifikujte 3-4 nástroje, ktoré by boli užitočné na riešenie tohto problému
2. Vytvorte diagram pracovného toku, ktorý ukazuje, ako tieto nástroje spolupracujú
3. Implementujte základnú verziu jedného z nástrojov vo vašom preferovanom jazyku
4. Vytvorte šablónu promptu, ktorá pomôže modelu efektívne používať váš nástroj

## Dodatočné zdroje


---

Ďalej: [Pokročilé témy](../05-AdvancedTopics/README.md)

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Hoci sa snažíme o presnosť, prosím, majte na pamäti, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre dôležité informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.