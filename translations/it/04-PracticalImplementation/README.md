<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5384bbb2a92d00d5d7e66274dbe0331d",
  "translation_date": "2025-06-20T18:33:49+00:00",
  "source_file": "04-PracticalImplementation/README.md",
  "language_code": "it"
}
-->
# Implementazione Pratica

L'implementazione pratica è il momento in cui la potenza del Model Context Protocol (MCP) diventa concreta. Pur essendo importante comprendere la teoria e l'architettura dietro MCP, il vero valore emerge quando applichi questi concetti per costruire, testare e distribuire soluzioni che risolvono problemi reali. Questo capitolo colma il divario tra conoscenza concettuale e sviluppo pratico, guidandoti nel processo di realizzazione di applicazioni basate su MCP.

Che tu stia sviluppando assistenti intelligenti, integrando l'AI nei flussi di lavoro aziendali o creando strumenti personalizzati per l'elaborazione dei dati, MCP offre una base flessibile. Il suo design indipendente dal linguaggio e gli SDK ufficiali per i linguaggi di programmazione più diffusi lo rendono accessibile a un ampio spettro di sviluppatori. Sfruttando questi SDK, puoi prototipare rapidamente, iterare e scalare le tue soluzioni su diverse piattaforme e ambienti.

Nelle sezioni seguenti troverai esempi pratici, codice di esempio e strategie di deployment che mostrano come implementare MCP in C#, Java, TypeScript, JavaScript e Python. Imparerai anche come fare il debug e testare i server MCP, gestire le API e distribuire soluzioni sul cloud usando Azure. Queste risorse pratiche sono pensate per accelerare il tuo apprendimento e aiutarti a costruire con sicurezza applicazioni MCP robuste e pronte per la produzione.

## Panoramica

Questa lezione si concentra sugli aspetti pratici dell’implementazione MCP in diversi linguaggi di programmazione. Esploreremo come utilizzare gli SDK MCP in C#, Java, TypeScript, JavaScript e Python per costruire applicazioni solide, fare debug e testare i server MCP, e creare risorse, prompt e strumenti riutilizzabili.

## Obiettivi di Apprendimento

Al termine di questa lezione, sarai in grado di:
- Implementare soluzioni MCP usando gli SDK ufficiali in vari linguaggi di programmazione
- Fare debug e test sistematici dei server MCP
- Creare e utilizzare funzionalità server (Risorse, Prompt e Strumenti)
- Progettare workflow MCP efficaci per compiti complessi
- Ottimizzare le implementazioni MCP per prestazioni e affidabilità

## Risorse SDK Ufficiali

Il Model Context Protocol offre SDK ufficiali per diversi linguaggi:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) 
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

## Lavorare con gli SDK MCP

Questa sezione fornisce esempi pratici di implementazione MCP in diversi linguaggi di programmazione. Puoi trovare codice di esempio nella directory `samples` organizzato per linguaggio.

### Esempi Disponibili

Il repository include [implementazioni di esempio](../../../04-PracticalImplementation/samples) nei seguenti linguaggi:

- [C#](./samples/csharp/README.md)
- [Java](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Ogni esempio mostra i concetti chiave di MCP e i pattern di implementazione per quel linguaggio e ecosistema specifico.

## Funzionalità Core del Server

I server MCP possono implementare qualsiasi combinazione di queste funzionalità:

### Risorse
Le risorse forniscono contesto e dati per l’utente o il modello AI:
- Repository di documenti
- Basi di conoscenza
- Fonti di dati strutturati
- Sistemi di file

### Prompt
I prompt sono messaggi e workflow predefiniti per gli utenti:
- Template di conversazione preimpostati
- Schemi di interazione guidata
- Strutture di dialogo specializzate

### Strumenti
Gli strumenti sono funzioni che il modello AI può eseguire:
- Utilità per l’elaborazione dei dati
- Integrazioni con API esterne
- Capacità computazionali
- Funzionalità di ricerca

## Esempi di Implementazione: C#

Il repository ufficiale del C# SDK contiene diversi esempi che mostrano vari aspetti di MCP:

- **Basic MCP Client**: esempio semplice che mostra come creare un client MCP e chiamare gli strumenti
- **Basic MCP Server**: implementazione minimale del server con registrazione base degli strumenti
- **Advanced MCP Server**: server completo con registrazione degli strumenti, autenticazione e gestione degli errori
- **Integrazione ASP.NET**: esempi di integrazione con ASP.NET Core
- **Pattern di implementazione degli strumenti**: vari pattern per implementare strumenti con diversi livelli di complessità

Il C# SDK MCP è in preview e le API potrebbero cambiare. Aggiorneremo costantemente questo blog man mano che l’SDK si evolve.

### Funzionalità Chiave
- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)

- Costruisci il tuo [primo MCP Server](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

Per esempi completi di implementazione in C#, visita il [repository ufficiale degli esempi C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Esempio di implementazione: Java

Il Java SDK offre opzioni robuste per l’implementazione MCP con funzionalità di livello enterprise.

### Funzionalità Chiave

- Integrazione con Spring Framework
- Forte tipizzazione
- Supporto alla programmazione reattiva
- Gestione completa degli errori

Per un esempio completo di implementazione Java, consulta il [Java sample](samples/java/containerapp/README.md) nella directory degli esempi.

## Esempio di implementazione: JavaScript

Il JavaScript SDK offre un approccio leggero e flessibile all’implementazione MCP.

### Funzionalità Chiave

- Supporto per Node.js e browser
- API basata su Promise
- Integrazione semplice con Express e altri framework
- Supporto WebSocket per lo streaming

Per un esempio completo di implementazione JavaScript, consulta il [JavaScript sample](samples/javascript/README.md) nella directory degli esempi.

## Esempio di implementazione: Python

Il Python SDK offre un approccio pythonico all’implementazione MCP con ottime integrazioni per framework ML.

### Funzionalità Chiave

- Supporto async/await con asyncio
- Integrazione con Flask e FastAPI
- Registrazione semplice degli strumenti
- Integrazione nativa con librerie ML popolari

Per un esempio completo di implementazione Python, consulta il [Python sample](samples/python/README.md) nella directory degli esempi.

## Gestione API

Azure API Management è una soluzione efficace per proteggere i server MCP. L’idea è mettere un’istanza di Azure API Management davanti al tuo server MCP e lasciargli gestire funzionalità che potresti voler avere, come:

- limitazione della velocità (rate limiting)
- gestione dei token
- monitoraggio
- bilanciamento del carico
- sicurezza

### Esempio Azure

Ecco un esempio Azure che fa esattamente questo, cioè [creare un MCP Server e proteggerlo con Azure API Management](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Guarda come avviene il flusso di autorizzazione nell’immagine qui sotto:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true) 

Nell’immagine precedente, accade quanto segue:

- L’autenticazione/autorizzazione avviene tramite Microsoft Entra.
- Azure API Management funge da gateway e usa policy per indirizzare e gestire il traffico.
- Azure Monitor registra tutte le richieste per analisi successive.

#### Flusso di autorizzazione

Vediamo il flusso di autorizzazione più nel dettaglio:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### Specifica di autorizzazione MCP

Scopri di più sulla [specifica di autorizzazione MCP](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization#2-10-third-party-authorization-flow)

## Distribuire un Remote MCP Server su Azure

Vediamo se riusciamo a distribuire l’esempio menzionato prima:

1. Clona il repository

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

2. Registra `Microsoft.App` resource provider.
    * If you are using Azure CLI, run `az provider register --namespace Microsoft.App --wait`.
    * If you are using Azure PowerShell, run `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Then run `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` e dopo un po’ verifica se la registrazione è completata.

3. Esegui questo comando [azd](https://aka.ms/azd) per creare il servizio API Management, la function app (con il codice) e tutte le altre risorse Azure necessarie

    ```shell
    azd up
    ```

    Questo comando dovrebbe distribuire tutte le risorse cloud su Azure

### Testare il tuo server con MCP Inspector

1. In una **nuova finestra del terminale**, installa e avvia MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Dovresti vedere un’interfaccia simile a questa:

    ![Connect to Node inspector](../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.it.png) 

2. CTRL-click per caricare l’app web MCP Inspector dall’URL mostrato dall’app (es. http://127.0.0.1:6274/#resources)
3. Imposta il tipo di trasporto su `SSE`
1. Set the URL to your running API Management SSE endpoint displayed after `azd up` e **Connetti**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

5. **Elenca gli Strumenti**. Clicca su uno strumento e **Esegui Strumento**.  

Se tutti i passaggi sono andati a buon fine, ora dovresti essere connesso al server MCP e aver potuto chiamare uno strumento.

## Server MCP per Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Questa serie di repository è un template quickstart per costruire e distribuire server MCP (Model Context Protocol) remoti personalizzati usando Azure Functions con Python, C# .NET o Node/TypeScript.

Gli esempi forniscono una soluzione completa che permette agli sviluppatori di:

- Costruire ed eseguire localmente: sviluppare e fare debug di un server MCP su macchina locale
- Distribuire su Azure: distribuire facilmente sul cloud con un semplice comando azd up
- Connettersi dai client: collegarsi al server MCP da vari client inclusi la modalità agente Copilot di VS Code e lo strumento MCP Inspector

### Funzionalità Chiave:

- Sicurezza by design: il server MCP è protetto tramite chiavi e HTTPS
- Opzioni di autenticazione: supporta OAuth usando autenticazione integrata e/o API Management
- Isolamento di rete: permette isolamento di rete usando Azure Virtual Networks (VNET)
- Architettura serverless: sfrutta Azure Functions per un’esecuzione scalabile e basata su eventi
- Sviluppo locale: supporto completo per sviluppo e debug locale
- Deployment semplice: processo di distribuzione semplificato su Azure

Il repository include tutti i file di configurazione necessari, il codice sorgente e le definizioni infrastrutturali per iniziare rapidamente con un’implementazione MCP pronta per la produzione.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Implementazione di esempio MCP usando Azure Functions con Python

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Implementazione di esempio MCP usando Azure Functions con C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Implementazione di esempio MCP usando Azure Functions con Node/TypeScript.

## Punti Chiave

- Gli SDK MCP forniscono strumenti specifici per linguaggio per implementare soluzioni MCP robuste
- Il processo di debug e test è fondamentale per applicazioni MCP affidabili
- I template di prompt riutilizzabili permettono interazioni AI coerenti
- Workflow ben progettati possono orchestrare compiti complessi usando più strumenti
- Implementare soluzioni MCP richiede attenzione a sicurezza, prestazioni e gestione degli errori

## Esercizio

Progetta un workflow MCP pratico che affronti un problema reale nel tuo ambito:

1. Identifica 3-4 strumenti utili per risolvere questo problema
2. Crea un diagramma del workflow che mostri come questi strumenti interagiscono
3. Implementa una versione base di uno degli strumenti usando il linguaggio che preferisci
4. Crea un template di prompt che aiuti il modello a usare efficacemente il tuo strumento

## Risorse Aggiuntive


---

Successivo: [Argomenti Avanzati](../05-AdvancedTopics/README.md)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando il servizio di traduzione automatica [Co-op Translator](https://github.com/Azure/co-op-translator). Pur impegnandoci per garantire l’accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua nativa deve essere considerato la fonte autorevole. Per informazioni critiche si raccomanda la traduzione professionale umana. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall’uso di questa traduzione.