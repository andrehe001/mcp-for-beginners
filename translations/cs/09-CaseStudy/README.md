<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6940b1e931e51821b219aa9dcfe8c4ee",
  "translation_date": "2025-06-23T11:16:08+00:00",
  "source_file": "09-CaseStudy/README.md",
  "language_code": "cs"
}
-->
# MCP v praxi: Případové studie ze skutečného světa

Model Context Protocol (MCP) mění způsob, jakým AI aplikace komunikují s daty, nástroji a službami. Tato sekce představuje případové studie ze skutečného života, které ukazují praktické využití MCP v různých podnikových scénářích.

## Přehled

Tato část ukazuje konkrétní příklady implementací MCP a zdůrazňuje, jak organizace využívají tento protokol k řešení složitých obchodních výzev. Prozkoumáním těchto případových studií získáte přehled o všestrannosti, škálovatelnosti a praktických výhodách MCP v reálných situacích.

## Hlavní cíle učení

Prozkoumáním těchto případových studií budete:

- Rozumět, jak lze MCP využít k řešení konkrétních obchodních problémů
- Seznámit se s různými integračními vzory a architektonickými přístupy
- Poznat osvědčené postupy pro implementaci MCP v podnikových prostředích
- Získat přehled o výzvách a řešeních při reálných implementacích
- Identifikovat příležitosti k použití podobných vzorů ve vlastních projektech

## Vybrané případové studie

### 1. [Azure AI Travel Agents – Referenční implementace](./travelagentsample.md)

Tato případová studie zkoumá komplexní referenční řešení Microsoftu, které ukazuje, jak vytvořit aplikaci pro plánování cestování s více agenty poháněnou AI pomocí MCP, Azure OpenAI a Azure AI Search. Projekt ukazuje:

- Orchestrace více agentů pomocí MCP
- Integraci podnikových dat s Azure AI Search
- Bezpečnou a škálovatelnou architekturu využívající Azure služby
- Rozšiřitelné nástroje s opakovaně použitelnými MCP komponentami
- Konverzační uživatelský zážitek poháněný Azure OpenAI

Architektura a detaily implementace poskytují cenné poznatky o tvorbě složitých systémů s více agenty, kde MCP slouží jako koordinační vrstva.

### 2. [Aktualizace položek Azure DevOps z dat YouTube](./UpdateADOItemsFromYT.md)

Tato případová studie ukazuje praktické využití MCP pro automatizaci pracovních procesů. Demonstruje, jak lze nástroje MCP použít k:

- Extrakci dat z online platforem (YouTube)
- Aktualizaci pracovních položek v systémech Azure DevOps
- Vytváření opakovatelných automatizačních workflow
- Integraci dat mezi různými systémy

Tento příklad ilustruje, jak i relativně jednoduché implementace MCP mohou výrazně zvýšit efektivitu automatizací rutinních úkolů a zlepšením konzistence dat napříč systémy.

### 3. [Získávání dokumentace v reálném čase s MCP](./docs-mcp/README.md)

Tato případová studie vás provede připojením Python konzolového klienta k Model Context Protocol (MCP) serveru za účelem získávání a zaznamenávání aktuální, kontextově relevantní dokumentace Microsoftu v reálném čase. Naučíte se, jak:

- Připojit se k MCP serveru pomocí Python klienta a oficiálního MCP SDK
- Používat streamingové HTTP klienty pro efektivní získávání dat v reálném čase
- Volat nástroje dokumentace na serveru a zaznamenávat odpovědi přímo do konzole
- Integrovat aktuální dokumentaci Microsoftu do pracovního postupu bez opuštění terminálu

Kapitola obsahuje praktické cvičení, minimální funkční ukázku kódu a odkazy na další zdroje pro hlubší studium. Projděte si kompletní návod a kód v přiložené kapitole, abyste pochopili, jak MCP může změnit přístup k dokumentaci a zvýšit produktivitu vývojářů v konzolových prostředích.

### 4. [Interaktivní webová aplikace pro generování studijního plánu s MCP](./docs-mcp/README.md)

Tato případová studie ukazuje, jak vytvořit interaktivní webovou aplikaci pomocí Chainlit a Model Context Protocol (MCP) pro generování personalizovaných studijních plánů na jakékoli téma. Uživatelé mohou zadat předmět (např. "certifikace AI-900") a délku studia (např. 8 týdnů), a aplikace nabídne týdenní rozpis doporučeného obsahu. Chainlit umožňuje konverzační chatové rozhraní, které dělá zážitek poutavým a adaptivním.

- Konverzační webová aplikace poháněná Chainlit
- Uživatelské vstupy pro téma a délku studia
- Doporučení obsahu rozdělená po týdnech pomocí MCP
- Reálné, adaptivní odpovědi v chatovém rozhraní

Projekt ukazuje, jak lze kombinovat konverzační AI a MCP k vytvoření dynamických, uživatelem řízených vzdělávacích nástrojů v moderním webovém prostředí.

### 5. [Dokumentace přímo v editoru s MCP serverem ve VS Code](./docs-mcp/README.md)

Tato případová studie ukazuje, jak přinést Microsoft Learn Docs přímo do prostředí VS Code pomocí MCP serveru—už žádné přepínání mezi záložkami prohlížeče! Uvidíte, jak:

- Okamžitě vyhledávat a číst dokumentaci přímo ve VS Code pomocí panelu MCP nebo příkazové palety
- Odkazovat dokumentaci a vkládat odkazy přímo do README nebo markdown souborů kurzu
- Používat GitHub Copilot a MCP společně pro plynulé, AI-poháněné pracovní postupy s dokumentací a kódem
- Validovat a vylepšovat dokumentaci s okamžitou zpětnou vazbou a přesností od Microsoftu
- Integrovat MCP s GitHub workflow pro kontinuální validaci dokumentace

Implementace obsahuje:
- Příklad konfigurace `.vscode/mcp.json` pro snadné nastavení
- Návody s obrázky zachycujícími zážitek přímo v editoru
- Tipy, jak kombinovat Copilot a MCP pro maximální produktivitu

Tento scénář je ideální pro autory kurzů, tvůrce dokumentace a vývojáře, kteří chtějí zůstat soustředění v editoru při práci s dokumentací, Copilotem a validačními nástroji—vše poháněné MCP.

### 6. [Vytvoření MCP serveru pomocí APIM](./apimsample.md)

Tato případová studie nabízí krok za krokem průvodce, jak vytvořit MCP server pomocí Azure API Management (APIM). Pokrývá:

- Nastavení MCP serveru v Azure API Management
- Zpřístupnění API operací jako MCP nástrojů
- Konfiguraci politik pro omezení rychlosti a zabezpečení
- Testování MCP serveru pomocí Visual Studio Code a GitHub Copilot

Tento příklad ukazuje, jak využít možnosti Azure k vytvoření robustního MCP serveru, který lze použít v různých aplikacích a zlepšit tak integraci AI systémů s podnikových API.

## Závěr

Tyto případové studie zdůrazňují všestrannost a praktické využití Model Context Protocol v reálných situacích. Od složitých systémů s více agenty po cílené automatizační workflow, MCP nabízí standardizovaný způsob, jak propojit AI systémy s nástroji a daty, které potřebují k poskytování hodnoty.

Studiem těchto implementací získáte vhled do architektonických vzorů, implementačních strategií a osvědčených postupů, které můžete aplikovat ve svých vlastních MCP projektech. Příklady ukazují, že MCP není jen teoretický rámec, ale praktické řešení skutečných obchodních výzev.

## Další zdroje

- [Azure AI Travel Agents GitHub Repository](https://github.com/Azure-Samples/azure-ai-travel-agents)
- [Azure DevOps MCP Tool](https://github.com/microsoft/azure-devops-mcp)
- [Playwright MCP Tool](https://github.com/microsoft/playwright-mcp)
- [Microsoft Docs MCP Server](https://github.com/MicrosoftDocs/mcp)
- [MCP Community Examples](https://github.com/microsoft/mcp)

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). I když usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho mateřském jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nejsme odpovědni za jakékoli nedorozumění nebo nesprávné výklady vzniklé z použití tohoto překladu.