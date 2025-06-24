<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:32:23+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "cs"
}
-->
# Generátor studijního plánu s Chainlit & Microsoft Learn Docs MCP

## Požadavky

- Python 3.8 nebo novější
- pip (správce balíčků pro Python)
- Připojení k internetu pro přístup k serveru Microsoft Learn Docs MCP

## Instalace

1. Naklonujte si tento repozitář nebo stáhněte soubory projektu.
2. Nainstalujte potřebné závislosti:

   ```bash
   pip install -r requirements.txt
   ```

## Použití

### Scénář 1: Jednoduchý dotaz na Docs MCP
Příkazový klient, který se připojí k serveru Docs MCP, odešle dotaz a vypíše výsledek.

1. Spusťte skript:
   ```bash
   python scenario1.py
   ```
2. Na výzvu zadejte svůj dotaz ohledně dokumentace.

### Scénář 2: Generátor studijního plánu (Chainlit webová aplikace)
Webové rozhraní (využívající Chainlit), které umožňuje uživatelům vytvořit si osobní týdenní studijní plán pro jakékoliv technické téma.

1. Spusťte aplikaci Chainlit:
   ```bash
   chainlit run scenario2.py
   ```
2. V prohlížeči otevřete lokální URL zobrazenou v terminálu (např. http://localhost:8000).
3. V chatovacím okně zadejte téma studia a počet týdnů, po které chcete studovat (např. "AI-900 certification, 8 weeks").
4. Aplikace vám odpoví týdenním studijním plánem včetně odkazů na relevantní dokumentaci Microsoft Learn.

**Požadované proměnné prostředí:**

Pro použití scénáře 2 (Chainlit webová aplikace s Azure OpenAI) je potřeba nastavit následující proměnné prostředí v souboru `.env` file in the `python`:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Před spuštěním aplikace vyplňte tyto hodnoty podle údajů vašeho Azure OpenAI zdroje.

> **Tip:** Snadno si můžete nasadit vlastní modely pomocí [Azure AI Foundry](https://ai.azure.com/).

### Scénář 3: Dokumentace v editoru s MCP serverem ve VS Code

Místo přepínání mezi záložkami pro vyhledávání dokumentace můžete mít Microsoft Learn Docs přímo ve VS Code pomocí MCP serveru. To vám umožní:
- Vyhledávat a číst dokumentaci přímo ve VS Code bez opuštění vývojového prostředí.
- Odkazovat na dokumentaci a vkládat odkazy přímo do README nebo souborů kurzu.
- Používat GitHub Copilot a MCP společně pro plynulý, AI podporovaný pracovní tok s dokumentací.

**Příklady využití:**
- Rychle přidat odkazy na dokumentaci do README během psaní kurzu nebo projektové dokumentace.
- Použít Copilot pro generování kódu a MCP pro okamžité vyhledání a citování relevantní dokumentace.
- Zůstat soustředěný v editoru a zvýšit produktivitu.

> [!IMPORTANT]
> Ujistěte se, že máte platný [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

## Why Chainlit for Scenario 2?

Chainlit is a modern open-source framework for building conversational web applications. It makes it easy to create chat-based user interfaces that connect to backend services like the Microsoft Learn Docs MCP server. This project uses Chainlit to provide a simple, interactive way to generate personalized study plans in real time. By leveraging Chainlit, you can quickly build and deploy chat-based tools that enhance productivity and learning.

## What This Does

This app allows users to create a personalized study plan by simply entering a topic and a duration. The app parses your input, queries the Microsoft Learn Docs MCP server for relevant content, and organizes the results into a structured, week-by-week plan. Each week’s recommendations are displayed in the chat, making it easy to follow and track your progress. The integration ensures you always get the latest, most relevant learning resources.

## Sample Queries

Try these queries in the chat window to see how the app responds:

- `AI-900 certification, 8 weeks`
- `Learn Azure Functions, 4 weeks`
- `Azure DevOps, 6 weeks`
- `Data engineering on Azure, 10 weeks`
- `Microsoft security fundamentals, 5 weeks`
- `Power Platform, 7 weeks`
- `Azure AI services, 12 weeks`
- `Cloud architecture, 9 weeks`

Tyto příklady ukazují flexibilitu aplikace pro různé studijní cíle a časové rámce.

## Reference

- [Chainlit Documentation](https://docs.chainlit.io/)
- [MCP Documentation](https://github.com/MicrosoftDocs/mcp)

**Prohlášení o vyloučení odpovědnosti**:  
Tento dokument byl přeložen pomocí AI překladatelské služby [Co-op Translator](https://github.com/Azure/co-op-translator). Přestože usilujeme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho mateřském jazyce by měl být považován za autoritativní zdroj. Pro zásadní informace se doporučuje profesionální lidský překlad. Nejsme odpovědní za jakékoliv nedorozumění nebo nesprávné výklady vyplývající z použití tohoto překladu.