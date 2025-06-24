<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "db532b1ec386c9ce38c791653dc3c881",
  "translation_date": "2025-06-21T14:43:19+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/scenario3/README.md",
  "language_code": "cs"
}
-->
# Scénář 3: Dokumentace přímo v editoru s MCP serverem ve VS Code

## Přehled

V tomto scénáři se naučíte, jak přenést Microsoft Learn Docs přímo do prostředí Visual Studio Code pomocí MCP serveru. Místo neustálého přepínání mezi záložkami pro hledání dokumentace můžete oficiální dokumentaci procházet, vyhledávat a odkazovat přímo ve svém editoru. Tento přístup zjednodušuje váš pracovní tok, pomáhá vám zůstat soustředění a umožňuje bezproblémovou integraci s nástroji jako GitHub Copilot.

- Vyhledávejte a čtěte dokumentaci ve VS Code, aniž byste opustili své vývojové prostředí.
- Vkládejte odkazy na dokumentaci přímo do README nebo souborů kurzu.
- Kombinujte GitHub Copilot a MCP pro plynulý pracovní postup podpořený umělou inteligencí.

## Výukové cíle

Na konci této kapitoly budete umět nastavit a používat MCP server ve VS Code k vylepšení své dokumentace a vývojového procesu. Budete schopni:

- Nakonfigurovat pracovní prostor pro použití MCP serveru při hledání dokumentace.
- Vyhledávat a vkládat dokumentaci přímo z VS Code.
- Spojit sílu GitHub Copilota a MCP pro produktivnější pracovní postup s podporou AI.

Tyto dovednosti vám pomohou zůstat soustředění, zlepšit kvalitu dokumentace a zvýšit vaši produktivitu jako vývojáře nebo technického pisatele.

## Řešení

Pro získání přístupu k dokumentaci přímo v editoru budete postupovat podle série kroků, které integrují MCP server s VS Code a GitHub Copilotem. Toto řešení je ideální pro autory kurzů, dokumentační pracovníky a vývojáře, kteří chtějí zůstat soustředění v editoru při práci s dokumentací a Copilotem.

- Rychle přidávejte odkazy na README při psaní kurzu nebo projektové dokumentace.
- Používejte Copilota k generování kódu a MCP k okamžitému vyhledání a citování relevantní dokumentace.
- Zůstaňte soustředění v editoru a zvyšte svou produktivitu.

### Podrobný návod krok za krokem

Pro začátek postupujte podle těchto kroků. Ke každému kroku můžete přidat screenshot z assets složky pro lepší vizuální představu.

1. **Přidejte konfiguraci MCP:**
   V kořenovém adresáři projektu vytvořte soubor `.vscode/mcp.json` a přidejte následující konfiguraci:
   ```json
   {
     "servers": {
       "LearnDocsMCP": {
         "url": "https://learn.microsoft.com/api/mcp"
       }
     }
   }
   ```
   Tato konfigurace říká VS Code, jak se připojit k [`Microsoft Learn Docs MCP serveru`](https://github.com/MicrosoftDocs/mcp).
   
   ![Krok 1: Přidejte mcp.json do složky .vscode](../../../../../../translated_images/step1-mcp-json.c06a007fccc3edfaf0598a31903c9ec71476d9fd3ae6c1b2b4321fd38688ca4b.cs.png)
    
2. **Otevřete panel GitHub Copilot Chat:**
   Pokud ještě nemáte nainstalované rozšíření GitHub Copilot, přejděte do zobrazení Extensions ve VS Code a nainstalujte ho. Můžete si ho stáhnout přímo z [Visual Studio Code Marketplace](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat). Poté otevřete panel Copilot Chat v postranním panelu.

   ![Krok 2: Otevřete panel Copilot Chat](../../../../../../translated_images/step2-copilot-panel.f1cc86e9b9b8cd1a85e4df4923de8bafee4830541ab255e3c90c09777fed97db.cs.png)

3. **Povolte agent mode a ověřte nástroje:**
   V panelu Copilot Chat zapněte agent mode.

   ![Krok 3: Povolte agent mode a ověřte nástroje](../../../../../../translated_images/step3-agent-mode.cdc32520fd7dd1d149c3f5226763c1d85a06d3c041d4cc983447625bdbeff4d4.cs.png)

   Po zapnutí agent mode ověřte, že je MCP server uveden mezi dostupnými nástroji. To zajišťuje, že Copilot agent má přístup k dokumentačnímu serveru pro získávání relevantních informací.
   
   ![Krok 3: Ověření nástroje MCP server](../../../../../../translated_images/step3-verify-mcp-tool.76096a6329cbfecd42888780f322370a0d8c8fa003ed3eeb7ccd23f0fc50c1ad.cs.png)

4. **Začněte nový chat a zadejte dotaz agentovi:**
   Otevřete nový chat v panelu Copilot Chat. Nyní můžete agenta požádat o dokumentační dotazy. Agent použije MCP server k vyhledání a zobrazení relevantní dokumentace Microsoft Learn přímo ve vašem editoru.

   - *„Snažím se napsat studijní plán pro téma X. Budu se mu věnovat 8 týdnů, pro každý týden navrhni obsah, který bych měl studovat.“*

   ![Krok 4: Zadejte dotaz agentovi v chatu](../../../../../../translated_images/step4-prompt-chat.12187bb001605efc5077992b621f0fcd1df12023c5dce0464f8eb8f3d595218f.cs.png)

5. **Živý dotaz:**

   > Podívejme se na živý dotaz ze sekce [#get-help](https://discord.gg/D6cRhjHWSC) v Azure AI Foundry Discordu ([zobrazit původní zprávu](https://discord.com/channels/1113626258182504448/1385498306720829572)):
   
   *„Hledám odpovědi na to, jak nasadit multi-agentní řešení s AI agenty vyvinutými na Azure AI Foundry. Vidím, že neexistuje přímá metoda nasazení, jako jsou kanály Copilot Studio. Jaké jsou tedy různé způsoby nasazení, aby podnikové uživatele mohly interagovat a dokončit práci?
Existuje mnoho článků/blogů, které uvádějí, že můžeme použít Azure Bot službu, která by mohla fungovat jako most mezi MS Teams a Azure AI Foundry agenty. Bude to fungovat, pokud nastavím Azure bota, který se připojí k Orchestrator Agentovi na Azure AI Foundry přes Azure function k provádění orchestrace, nebo potřebuji vytvořit Azure function pro každého AI agenta v multi-agentním řešení, aby orchestrace probíhala na Bot frameworku? Jakékoliv další návrhy jsou vítány.“*

   ![Krok 5: Živé dotazy](../../../../../../translated_images/step5-live-queries.49db3e4a50bea27327e3cb18c24d263b7d134930d78e7392f9515a1c00264a7f.cs.png)

   Agent odpoví s relevantními odkazy na dokumentaci a shrnutími, které pak můžete přímo vložit do svých markdown souborů nebo použít jako reference ve svém kódu.
   
### Ukázkové dotazy

Zde je několik příkladů dotazů, které můžete vyzkoušet. Tyto dotazy ukážou, jak MCP server a Copilot spolupracují a poskytují okamžitou, kontextově podloženou dokumentaci a reference přímo ve VS Code:

- „Ukáž mi, jak používat Azure Functions triggers.“
- „Vlož odkaz na oficiální dokumentaci Azure Key Vault.“
- „Jaké jsou nejlepší postupy pro zabezpečení Azure zdrojů?“
- „Najdi quickstart pro Azure AI služby.“

Tyto dotazy demonstrují, jak MCP server a Copilot společně poskytují rychlou a relevantní dokumentaci bez nutnosti opouštět VS Code.

---

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Originální dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro kritické informace se doporučuje využít profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo mylné výklady vyplývající z použití tohoto překladu.