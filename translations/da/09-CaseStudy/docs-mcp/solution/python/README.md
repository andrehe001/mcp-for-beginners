<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:30:32+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "da"
}
-->
# Studieplansgenerator med Chainlit & Microsoft Learn Docs MCP

## Forudsætninger

- Python 3.8 eller nyere  
- pip (Python-pakkehåndtering)  
- Internetadgang for at forbinde til Microsoft Learn Docs MCP-serveren  

## Installation

1. Klon dette repository eller download projektfilerne.  
2. Installer de nødvendige afhængigheder:

   ```bash
   pip install -r requirements.txt
   ```

## Brug

### Scenario 1: Simpelt opslag til Docs MCP  
En kommandolinjeklient, der forbinder til Docs MCP-serveren, sender et spørgsmål og viser resultatet.

1. Kør scriptet:  
   ```bash
   python scenario1.py
   ```  
2. Indtast dit dokumentationsspørgsmål ved prompten.

### Scenario 2: Studieplansgenerator (Chainlit Web App)  
En webbaseret grænseflade (ved brug af Chainlit), der giver brugere mulighed for at generere en personlig, uge-for-uge studieplan for ethvert teknisk emne.

1. Start Chainlit-appen:  
   ```bash
   chainlit run scenario2.py
   ```  
2. Åbn den lokale URL, der vises i terminalen (f.eks. http://localhost:8000) i din browser.  
3. Indtast dit studiemne og antallet af uger, du vil studere (f.eks. "AI-900 certification, 8 uger") i chatvinduet.  
4. Appen vil svare med en uge-for-uge studieplan, inklusive links til relevant Microsoft Learn-dokumentation.

**Nødvendige miljøvariabler:**

For at bruge Scenario 2 (Chainlit webappen med Azure OpenAI) skal du sætte følgende miljøvariabler i en `.env` file in the `python`-fil:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Udfyld disse værdier med dine Azure OpenAI-ressourcedetaljer, inden du kører appen.

> **Tip:** Du kan nemt implementere dine egne modeller via [Azure AI Foundry](https://ai.azure.com/).

### Scenario 3: Dokumentation i editoren med MCP-server i VS Code

I stedet for at skifte browserfane for at søge dokumentation, kan du hente Microsoft Learn Docs direkte ind i VS Code ved hjælp af MCP-serveren. Dette gør det muligt at:  
- Søge og læse dokumentation i VS Code uden at forlade dit udviklingsmiljø.  
- Referere dokumentation og indsætte links direkte i dine README- eller kursusfiler.  
- Bruge GitHub Copilot og MCP sammen for en smidig, AI-drevet dokumentationsworkflow.

**Eksempler på brugssituationer:**  
- Tilføj hurtigt referencelinks til en README, mens du skriver kursus- eller projekt-dokumentation.  
- Brug Copilot til at generere kode og MCP til øjeblikkeligt at finde og citere relevant dokumentation.  
- Forbliv fokuseret i din editor og øg produktiviteten.

> [!IMPORTANT]  
> Sørg for at have en gyldig [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

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

Disse eksempler viser appens fleksibilitet til forskellige læringsmål og tidsrammer.

## Referencer

- [Chainlit Dokumentation](https://docs.chainlit.io/)  
- [MCP Dokumentation](https://github.com/MicrosoftDocs/mcp)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.