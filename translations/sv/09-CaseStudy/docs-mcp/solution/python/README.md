<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:30:23+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "sv"
}
-->
# Study Plan Generator med Chainlit & Microsoft Learn Docs MCP

## Förutsättningar

- Python 3.8 eller högre
- pip (Python paketchef)
- Internetuppkoppling för att ansluta till Microsoft Learn Docs MCP-servern

## Installation

1. Klona detta repository eller ladda ner projektfilerna.
2. Installera de nödvändiga beroenden:

   ```bash
   pip install -r requirements.txt
   ```

## Användning

### Scenario 1: Enkel fråga till Docs MCP
En kommandoradsklient som ansluter till Docs MCP-servern, skickar en fråga och skriver ut resultatet.

1. Kör skriptet:
   ```bash
   python scenario1.py
   ```
2. Skriv in din dokumentationsfråga vid prompten.

### Scenario 2: Study Plan Generator (Chainlit Web App)
Ett webbaserat gränssnitt (med Chainlit) som låter användare skapa en personlig, veckovis studieplan för vilket tekniskt ämne som helst.

1. Starta Chainlit-appen:
   ```bash
   chainlit run scenario2.py
   ```
2. Öppna den lokala URL som visas i terminalen (t.ex. http://localhost:8000) i din webbläsare.
3. Skriv in ditt studietema och antal veckor du vill studera (t.ex. "AI-900 certification, 8 weeks") i chattfönstret.
4. Appen svarar med en veckovis studieplan, inklusive länkar till relevant Microsoft Learn-dokumentation.

**Nödvändiga miljövariabler:**

För att använda Scenario 2 (Chainlit web app med Azure OpenAI) måste du ange följande miljövariabler i en `.env` file in the `python`-katalog:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Fyll i dessa värden med dina Azure OpenAI-resursuppgifter innan du kör appen.

> **Tip:** Du kan enkelt distribuera egna modeller med [Azure AI Foundry](https://ai.azure.com/).

### Scenario 3: In-Editor Docs med MCP-server i VS Code

Istället för att byta flikar i webbläsaren för att söka dokumentation kan du ta in Microsoft Learn Docs direkt i VS Code med hjälp av MCP-servern. Detta gör att du kan:
- Söka och läsa dokumentation direkt i VS Code utan att lämna din kodmiljö.
- Referera dokumentation och infoga länkar direkt i din README eller kursfiler.
- Använda GitHub Copilot och MCP tillsammans för ett sömlöst, AI-drivet dokumentationsflöde.

**Exempel på användningsområden:**
- Lägg snabbt till referenslänkar i en README medan du skriver kurs- eller projektdokumentation.
- Använd Copilot för att generera kod och MCP för att omedelbart hitta och citera relevant dokumentation.
- Håll fokus i editorn och öka produktiviteten.

> [!IMPORTANT]
> Se till att du har en giltig [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

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

Dessa exempel visar på appens flexibilitet för olika lärandemål och tidsramar.

## Referenser

- [Chainlit Documentation](https://docs.chainlit.io/)
- [MCP Documentation](https://github.com/MicrosoftDocs/mcp)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, var vänlig uppmärksam på att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.