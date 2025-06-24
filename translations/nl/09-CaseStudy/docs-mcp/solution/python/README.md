<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:31:01+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "nl"
}
-->
# Studieplangenerator met Chainlit & Microsoft Learn Docs MCP

## Vereisten

- Python 3.8 of hoger
- pip (Python package manager)
- Internettoegang om verbinding te maken met de Microsoft Learn Docs MCP-server

## Installatie

1. Clone deze repository of download de projectbestanden.
2. Installeer de benodigde dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Gebruik

### Scenario 1: Eenvoudige vraag aan Docs MCP  
Een command-line client die verbinding maakt met de Docs MCP-server, een vraag verstuurt en het resultaat toont.

1. Voer het script uit:  
   ```bash
   python scenario1.py
   ```  
2. Voer je documentatievraag in bij de prompt.

### Scenario 2: Studieplangenerator (Chainlit Web App)  
Een webinterface (met Chainlit) waarmee gebruikers een gepersonaliseerd, week-voor-week studieplan kunnen genereren voor elk technisch onderwerp.

1. Start de Chainlit-app:  
   ```bash
   chainlit run scenario2.py
   ```  
2. Open de lokale URL die in je terminal wordt weergegeven (bijv. http://localhost:8000) in je browser.  
3. Voer in het chatvenster je studiethema en het aantal weken in dat je wilt studeren (bijv. "AI-900 certification, 8 weeks").  
4. De app geeft een week-voor-week studieplan terug, inclusief links naar relevante Microsoft Learn-documentatie.

**Vereiste omgevingsvariabelen:**  

Om Scenario 2 te gebruiken (de Chainlit webapp met Azure OpenAI), moet je de volgende omgevingsvariabelen instellen in een `.env` file in the `python`-bestand:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Vul deze waarden in met je Azure OpenAI-resourcegegevens voordat je de app start.

> **Tip:** Je kunt eenvoudig je eigen modellen implementeren via [Azure AI Foundry](https://ai.azure.com/).

### Scenario 3: Documentatie in de editor met MCP-server in VS Code

In plaats van van browser-tabblad te wisselen om documentatie te zoeken, kun je Microsoft Learn Docs direct in VS Code gebruiken via de MCP-server. Hiermee kun je:  
- Documentatie zoeken en lezen binnen VS Code zonder je programmeeromgeving te verlaten.  
- Documentatie verwijzen en links direct invoegen in je README- of cursusbestanden.  
- GitHub Copilot en MCP samen gebruiken voor een naadloze, AI-gestuurde documentatieworkflow.

**Voorbeelden van gebruik:**  
- Snel referentielinks toevoegen aan een README tijdens het schrijven van cursus- of projectdocumentatie.  
- Copilot gebruiken om code te genereren en MCP om direct relevante documentatie te vinden en te citeren.  
- Gefocust blijven in je editor en je productiviteit verhogen.

> [!IMPORTANT]  
> Zorg dat je een geldig [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

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
- `Cloud architecture, 9 weeks` hebt.

Deze voorbeelden laten zien hoe flexibel de app is voor verschillende leerdoelen en tijdsperiodes.

## Referenties

- [Chainlit Documentation](https://docs.chainlit.io/)  
- [MCP Documentation](https://github.com/MicrosoftDocs/mcp)

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het oorspronkelijke document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.