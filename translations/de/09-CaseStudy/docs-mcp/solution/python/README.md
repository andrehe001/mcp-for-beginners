<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:26:23+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "de"
}
-->
# Study Plan Generator mit Chainlit & Microsoft Learn Docs MCP

## Voraussetzungen

- Python 3.8 oder höher  
- pip (Python-Paketmanager)  
- Internetzugang, um eine Verbindung zum Microsoft Learn Docs MCP-Server herzustellen  

## Installation

1. Klone dieses Repository oder lade die Projektdateien herunter.  
2. Installiere die benötigten Abhängigkeiten:

   ```bash
   pip install -r requirements.txt
   ```

## Verwendung

### Szenario 1: Einfache Abfrage an Docs MCP  
Ein Kommandozeilen-Client, der eine Verbindung zum Docs MCP-Server herstellt, eine Anfrage sendet und das Ergebnis ausgibt.

1. Starte das Skript:  
   ```bash
   python scenario1.py
   ```  
2. Gib deine Dokumentationsfrage an der Eingabeaufforderung ein.

### Szenario 2: Study Plan Generator (Chainlit Web App)  
Eine webbasierte Oberfläche (mit Chainlit), die es Nutzern ermöglicht, einen personalisierten, wöchentlichen Lernplan für jedes technische Thema zu erstellen.

1. Starte die Chainlit-App:  
   ```bash
   chainlit run scenario2.py
   ```  
2. Öffne die im Terminal angegebene lokale URL (z. B. http://localhost:8000) in deinem Browser.  
3. Gib im Chatfenster dein Lernthema und die Anzahl der Wochen ein, die du lernen möchtest (z. B. „AI-900 certification, 8 weeks“).  
4. Die App antwortet mit einem wöchentlichen Lernplan inklusive Links zu relevanten Microsoft Learn-Dokumentationen.

**Erforderliche Umgebungsvariablen:**  

Um Szenario 2 (die Chainlit Web App mit Azure OpenAI) nutzen zu können, musst du folgende Umgebungsvariablen in einem `.env` file in the `python` Verzeichnis setzen:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Fülle diese Werte mit deinen Azure OpenAI-Ressourcendaten aus, bevor du die App startest.

> **Tipp:** Du kannst deine eigenen Modelle ganz einfach mit [Azure AI Foundry](https://ai.azure.com/) bereitstellen.

### Szenario 3: In-Editor Docs mit MCP-Server in VS Code

Anstatt zwischen Browser-Tabs zu wechseln, um Dokumentationen zu suchen, kannst du Microsoft Learn Docs direkt in VS Code über den MCP-Server integrieren. Das ermöglicht dir:  
- Dokumentationen direkt in VS Code zu suchen und zu lesen, ohne deine Entwicklungsumgebung zu verlassen.  
- Referenzen und Links direkt in deine README- oder Kursdateien einzufügen.  
- GitHub Copilot und MCP zusammen für einen nahtlosen, KI-gestützten Dokumentationsworkflow zu nutzen.

**Beispielanwendungen:**  
- Schnell Referenzlinks in eine README einfügen, während du eine Kurs- oder Projektdokumentation schreibst.  
- Copilot zum Generieren von Code verwenden und MCP, um relevante Dokumentation sofort zu finden und zu zitieren.  
- Im Editor konzentriert bleiben und die Produktivität steigern.

> [!IMPORTANT]  
> Stelle sicher, dass du eine gültige [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

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

Diese Beispiele zeigen die Flexibilität der App für unterschiedliche Lernziele und Zeitrahmen.

## Referenzen

- [Chainlit Documentation](https://docs.chainlit.io/)  
- [MCP Documentation](https://github.com/MicrosoftDocs/mcp)

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir auf Genauigkeit achten, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Nutzung dieser Übersetzung entstehen.