<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:29:22+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "it"
}
-->
# Generatore di Piani di Studio con Chainlit & Microsoft Learn Docs MCP

## Prerequisiti

- Python 3.8 o superiore  
- pip (gestore pacchetti Python)  
- Connessione a Internet per collegarsi al server Microsoft Learn Docs MCP  

## Installazione

1. Clona questo repository o scarica i file del progetto.  
2. Installa le dipendenze richieste:

   ```bash
   pip install -r requirements.txt
   ```

## Utilizzo

### Scenario 1: Query Semplice a Docs MCP  
Un client da riga di comando che si collega al server Docs MCP, invia una domanda e stampa il risultato.

1. Esegui lo script:  
   ```bash
   python scenario1.py
   ```  
2. Inserisci la tua domanda sulla documentazione al prompt.

### Scenario 2: Generatore di Piani di Studio (App Web Chainlit)  
Un’interfaccia web (basata su Chainlit) che permette agli utenti di generare un piano di studio personalizzato, settimana per settimana, su qualsiasi argomento tecnico.

1. Avvia l’app Chainlit:  
   ```bash
   chainlit run scenario2.py
   ```  
2. Apri l’URL locale fornito nel terminale (ad esempio, http://localhost:8000) nel browser.  
3. Nella finestra di chat, inserisci l’argomento di studio e il numero di settimane in cui vuoi studiare (es. "Certificazione AI-900, 8 settimane").  
4. L’app risponderà con un piano di studio dettagliato per settimana, includendo link alla documentazione Microsoft Learn pertinente.

**Variabili d’Ambiente Richieste:**  

Per usare lo Scenario 2 (l’app web Chainlit con Azure OpenAI), devi impostare le seguenti variabili d’ambiente in una directory `.env` file in the `python`:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Compila questi valori con i dettagli della tua risorsa Azure OpenAI prima di avviare l’app.

> **[!TIP]** Puoi facilmente distribuire i tuoi modelli usando [Azure AI Foundry](https://ai.azure.com/).

### Scenario 3: Documentazione In-Editor con MCP Server in VS Code

Invece di passare da una scheda del browser all’altra per cercare documentazione, puoi integrare Microsoft Learn Docs direttamente in VS Code usando il server MCP. Questo ti permette di:  
- Cercare e leggere la documentazione dentro VS Code senza uscire dall’ambiente di sviluppo.  
- Fare riferimento alla documentazione e inserire link direttamente nei file README o nei materiali del corso.  
- Usare GitHub Copilot e MCP insieme per un flusso di lavoro documentale AI-powered fluido.

**Esempi di utilizzo:**  
- Aggiungere rapidamente link di riferimento a un README mentre scrivi la documentazione di un corso o progetto.  
- Usare Copilot per generare codice e MCP per trovare e citare subito la documentazione pertinente.  
- Rimanere concentrato nell’editor e aumentare la produttività.

> [!IMPORTANT]  
> Assicurati di avere un file valido [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

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

Questi esempi mostrano la flessibilità dell’app per diversi obiettivi di apprendimento e tempistiche.

## Riferimenti

- [Documentazione Chainlit](https://docs.chainlit.io/)  
- [Documentazione MCP](https://github.com/MicrosoftDocs/mcp)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di considerare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche si raccomanda la traduzione professionale effettuata da un umano. Non ci assumiamo alcuna responsabilità per incomprensioni o interpretazioni errate derivanti dall’uso di questa traduzione.