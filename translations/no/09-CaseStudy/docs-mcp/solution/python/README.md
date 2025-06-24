<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:30:41+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "no"
}
-->
# Studieplan-generator med Chainlit & Microsoft Learn Docs MCP

## Forutsetninger

- Python 3.8 eller nyere
- pip (Python pakkehåndterer)
- Internett-tilgang for å koble til Microsoft Learn Docs MCP-serveren

## Installasjon

1. Klon dette depotet eller last ned prosjektfilene.
2. Installer nødvendige avhengigheter:

   ```bash
   pip install -r requirements.txt
   ```

## Bruk

### Scenario 1: Enkel forespørsel til Docs MCP  
En kommandolinjeklient som kobler til Docs MCP-serveren, sender en forespørsel og viser resultatet.

1. Kjør skriptet:  
   ```bash
   python scenario1.py
   ```  
2. Skriv inn dokumentasjonsspørsmålet ditt ved prompten.

### Scenario 2: Studieplan-generator (Chainlit nettapp)  
En nettbasert grensesnitt (med Chainlit) som lar brukere lage en personlig, uke-for-uke studieplan for et teknisk emne.

1. Start Chainlit-appen:  
   ```bash
   chainlit run scenario2.py
   ```  
2. Åpne den lokale URL-en som vises i terminalen (f.eks. http://localhost:8000) i nettleseren din.  
3. Skriv inn studietemaet ditt og antall uker du ønsker å studere (f.eks. "AI-900 certification, 8 weeks") i chattevinduet.  
4. Appen svarer med en uke-for-uke studieplan, inkludert lenker til relevant Microsoft Learn-dokumentasjon.

**Påkrevde miljøvariabler:**  

For å bruke Scenario 2 (Chainlit-nettappen med Azure OpenAI), må du sette følgende miljøvariabler i en `.env` file in the `python`-mappe:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Fyll inn disse verdiene med detaljene for din Azure OpenAI-ressurs før du kjører appen.

> **Tip:** Du kan enkelt distribuere dine egne modeller ved å bruke [Azure AI Foundry](https://ai.azure.com/).

### Scenario 3: In-Editor Docs med MCP-server i VS Code

I stedet for å bytte nettleserfaner for å søke dokumentasjon, kan du hente Microsoft Learn Docs direkte inn i VS Code ved hjelp av MCP-serveren. Dette gjør at du kan:  
- Søke og lese dokumentasjon inne i VS Code uten å forlate kodingmiljøet.  
- Referere dokumentasjon og sette inn lenker direkte i README- eller kursfiler.  
- Bruke GitHub Copilot og MCP sammen for en sømløs, AI-drevet dokumentasjonsflyt.

**Eksempler på bruk:**  
- Legg raskt til referanselenker i en README mens du skriver kurs- eller prosjektdokumentasjon.  
- Bruk Copilot til å generere kode og MCP til å finne og sitere relevant dokumentasjon umiddelbart.  
- Hold fokus i editoren og øk produktiviteten.

> [!IMPORTANT]  
> Sørg for at du har en gyldig [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

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

Disse eksemplene viser hvor fleksibel appen er for ulike læringsmål og tidsrammer.

## Referanser

- [Chainlit Dokumentasjon](https://docs.chainlit.io/)  
- [MCP Dokumentasjon](https://github.com/MicrosoftDocs/mcp)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår som følge av bruk av denne oversettelsen.