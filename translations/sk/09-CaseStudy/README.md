<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6940b1e931e51821b219aa9dcfe8c4ee",
  "translation_date": "2025-06-23T11:16:41+00:00",
  "source_file": "09-CaseStudy/README.md",
  "language_code": "sk"
}
-->
# MCP v praxi: Skutočné prípadové štúdie

Model Context Protocol (MCP) mení spôsob, akým AI aplikácie komunikujú s dátami, nástrojmi a službami. Táto sekcia predstavuje reálne prípadové štúdie, ktoré ukazujú praktické využitie MCP v rôznych podnikových scenároch.

## Prehľad

Táto sekcia prináša konkrétne príklady implementácií MCP a zdôrazňuje, ako organizácie využívajú tento protokol na riešenie zložitých obchodných výziev. Preskúmaním týchto prípadových štúdií získate prehľad o všestrannosti, škálovateľnosti a praktických výhodách MCP v reálnych situáciách.

## Kľúčové ciele učenia

Preskúmaním týchto prípadových štúdií budete:

- Rozumieť, ako možno MCP využiť na riešenie konkrétnych obchodných problémov
- Spoznáte rôzne integračné vzory a architektonické prístupy
- Identifikovať osvedčené postupy pri implementácii MCP v podnikových prostrediach
- Získať poznatky o výzvach a riešeniach, ktoré sa vyskytli pri reálnych implementáciách
- Objaviť príležitosti na aplikáciu podobných vzorov vo vlastných projektoch

## Vybrané prípadové štúdie

### 1. [Azure AI Travel Agents – Referenčná implementácia](./travelagentsample.md)

Táto prípadová štúdia skúma komplexné referenčné riešenie od Microsoftu, ktoré demonštruje, ako vytvoriť viacagentovú AI aplikáciu na plánovanie ciest pomocou MCP, Azure OpenAI a Azure AI Search. Projekt ukazuje:

- Orchestráciu viac agentov cez MCP
- Integráciu podnikových dát s Azure AI Search
- Bezpečnú a škálovateľnú architektúru využívajúcu Azure služby
- Rozšíriteľné nástroje s opakovane použiteľnými MCP komponentmi
- Konverzačný používateľský zážitok poháňaný Azure OpenAI

Architektúra a detaily implementácie poskytujú cenné poznatky o budovaní zložitých viacagentových systémov s MCP ako koordinačnou vrstvou.

### 2. [Aktualizácia položiek Azure DevOps z údajov YouTube](./UpdateADOItemsFromYT.md)

Táto prípadová štúdia ukazuje praktické využitie MCP na automatizáciu pracovných procesov. Demonštruje, ako možno MCP nástroje použiť na:

- Extrahovanie dát z online platforiem (YouTube)
- Aktualizáciu pracovných položiek v systémoch Azure DevOps
- Vytvorenie opakovateľných automatizačných pracovných tokov
- Integráciu dát medzi rôznymi systémami

Tento príklad ilustruje, že aj relatívne jednoduché implementácie MCP môžu priniesť výrazné zlepšenie efektivity automatizáciou rutinných úloh a zvýšením konzistencie dát naprieč systémami.

### 3. [Získavanie dokumentácie v reálnom čase pomocou MCP](./docs-mcp/README.md)

Táto prípadová štúdia vás prevedie pripojením Python konzolového klienta k MCP serveru na získavanie a zaznamenávanie aktuálnej, kontextovo relevantnej dokumentácie Microsoftu v reálnom čase. Naučíte sa, ako:

- Pripojiť sa k MCP serveru pomocou Python klienta a oficiálneho MCP SDK
- Používať streaming HTTP klientov pre efektívne získavanie dát v reálnom čase
- Volat nástroje na dokumentáciu na serveri a zaznamenávať odpovede priamo do konzoly
- Integrovať aktuálnu Microsoft dokumentáciu do svojho pracovného toku bez opustenia terminálu

Kapitola obsahuje praktické zadanie, minimálny funkčný ukážkový kód a odkazy na ďalšie zdroje pre hlbšie štúdium. Pozrite si kompletný návod a kód v prepojenej kapitole, aby ste pochopili, ako MCP môže zmeniť prístup k dokumentácii a zvýšiť produktivitu vývojárov v konzolovom prostredí.

### 4. [Interaktívna webová aplikácia na generovanie študijných plánov s MCP](./docs-mcp/README.md)

Táto prípadová štúdia ukazuje, ako vytvoriť interaktívnu webovú aplikáciu pomocou Chainlit a Model Context Protocol (MCP) na generovanie personalizovaných študijných plánov pre ľubovoľnú tému. Používatelia môžu zadať predmet (napr. "certifikácia AI-900") a dĺžku štúdia (napr. 8 týždňov) a aplikácia poskytne týždenný rozpis odporúčaného obsahu. Chainlit umožňuje konverzačné chatové rozhranie, ktoré robí zážitok pútavým a prispôsobivým.

- Konverzačná webová aplikácia poháňaná Chainlit
- Používateľom riadené zadávanie témy a trvania
- Odporúčania obsahu týždeň po týždni s využitím MCP
- Reálne časové, adaptívne odpovede v chatovom rozhraní

Projekt demonštruje, ako možno kombinovať konverzačnú AI a MCP na vytváranie dynamických, používateľom riadených vzdelávacích nástrojov v modernom webovom prostredí.

### 5. [Dokumentácia priamo v editore s MCP serverom vo VS Code](./docs-mcp/README.md)

Táto prípadová štúdia ukazuje, ako priniesť Microsoft Learn Docs priamo do vášho prostredia VS Code pomocou MCP servera – už žiadne prepínanie medzi záložkami prehliadača! Uvidíte, ako:

- Okamžite vyhľadávať a čítať dokumentáciu priamo vo VS Code pomocou MCP panelu alebo príkazovej palety
- Odkazovať na dokumentáciu a vkladať linky priamo do README alebo markdown súborov kurzov
- Používať GitHub Copilot a MCP spoločne pre plynulé AI-poháňané pracovné toky s dokumentáciou a kódom
- Overovať a vylepšovať dokumentáciu s reálnou spätnou väzbou a presnosťou od Microsoftu
- Integrovať MCP s GitHub pracovnými tokmi pre kontinuálnu validáciu dokumentácie

Implementácia obsahuje:
- Príklad `.vscode/mcp.json` konfigurácie pre jednoduché nastavenie
- Prechádzky prostredníctvom screenshotov z práce v editore
- Tipy na kombinovanie Copilota a MCP pre maximálnu produktivitu

Tento scenár je ideálny pre autorov kurzov, tvorcov dokumentácie a vývojárov, ktorí chcú zostať sústredení vo svojom editore a zároveň pracovať s dokumentáciou, Copilotom a validačnými nástrojmi – všetko poháňané MCP.

### 6. [Vytvorenie MCP servera v APIM](./apimsample.md)

Táto prípadová štúdia poskytuje krok za krokom návod, ako vytvoriť MCP server pomocou Azure API Management (APIM). Pokrýva:

- Nastavenie MCP servera v Azure API Management
- Zverejnenie API operácií ako MCP nástrojov
- Konfiguráciu politík pre obmedzenie rýchlosti a bezpečnosť
- Testovanie MCP servera pomocou Visual Studio Code a GitHub Copilot

Tento príklad ukazuje, ako využiť možnosti Azure na vytvorenie robustného MCP servera, ktorý možno použiť v rôznych aplikáciách a zlepšiť tak integráciu AI systémov s podnikových API.

## Záver

Tieto prípadové štúdie zdôrazňujú všestrannosť a praktické využitie Model Context Protocol v reálnych situáciách. Od zložitých viacagentových systémov po cielene automatizované pracovné toky, MCP poskytuje štandardizovaný spôsob prepojenia AI systémov s nástrojmi a dátami, ktoré potrebujú na vytváranie hodnoty.

Štúdiom týchto implementácií získate poznatky o architektonických vzoroch, stratégiách implementácie a osvedčených postupoch, ktoré môžete aplikovať vo vlastných MCP projektoch. Príklady ukazujú, že MCP nie je len teoretický rámec, ale praktické riešenie reálnych obchodných výziev.

## Ďalšie zdroje

- [Azure AI Travel Agents GitHub Repository](https://github.com/Azure-Samples/azure-ai-travel-agents)
- [Azure DevOps MCP Tool](https://github.com/microsoft/azure-devops-mcp)
- [Playwright MCP Tool](https://github.com/microsoft/playwright-mcp)
- [Microsoft Docs MCP Server](https://github.com/MicrosoftDocs/mcp)
- [MCP Community Examples](https://github.com/microsoft/mcp)

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, prosím, berte na vedomie, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.