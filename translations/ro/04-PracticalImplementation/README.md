<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5384bbb2a92d00d5d7e66274dbe0331d",
  "translation_date": "2025-06-20T18:45:18+00:00",
  "source_file": "04-PracticalImplementation/README.md",
  "language_code": "ro"
}
-->
# Implementare practică

Implementarea practică este momentul în care puterea Model Context Protocol (MCP) devine concretă. Deși înțelegerea teoriei și arhitecturii din spatele MCP este importantă, valoarea reală apare atunci când aplici aceste concepte pentru a construi, testa și implementa soluții care rezolvă probleme din lumea reală. Acest capitol face legătura între cunoștințele conceptuale și dezvoltarea practică, ghidându-te prin procesul de a aduce la viață aplicații bazate pe MCP.

Indiferent dacă dezvolți asistenți inteligenți, integrezi AI în fluxuri de lucru de afaceri sau construiești unelte personalizate pentru procesarea datelor, MCP oferă o bază flexibilă. Designul său independent de limbaj și SDK-urile oficiale pentru limbaje de programare populare îl fac accesibil unui spectru larg de dezvoltatori. Folosind aceste SDK-uri, poți prototipa rapid, itera și scala soluțiile tale pe diferite platforme și medii.

În secțiunile următoare vei găsi exemple practice, coduri demonstrative și strategii de implementare care arată cum să implementezi MCP în C#, Java, TypeScript, JavaScript și Python. De asemenea, vei învăța cum să depanezi și să testezi serverele MCP, să gestionezi API-urile și să implementezi soluții în cloud folosind Azure. Aceste resurse practice sunt concepute pentru a accelera procesul tău de învățare și pentru a te ajuta să construiești cu încredere aplicații MCP robuste și pregătite pentru producție.

## Prezentare generală

Această lecție se concentrează pe aspectele practice ale implementării MCP în mai multe limbaje de programare. Vom explora cum să folosești SDK-urile MCP în C#, Java, TypeScript, JavaScript și Python pentru a construi aplicații robuste, a depana și testa serverele MCP și a crea resurse, prompturi și unelte reutilizabile.

## Obiective de învățare

La finalul acestei lecții, vei putea:
- Implementa soluții MCP folosind SDK-urile oficiale în diverse limbaje de programare
- Depana și testa sistematic serverele MCP
- Crea și folosi funcționalități ale serverului (Resurse, Prompturi și Unelte)
- Proiecta fluxuri de lucru eficiente MCP pentru sarcini complexe
- Optimizarea implementărilor MCP pentru performanță și fiabilitate

## Resurse SDK oficiale

Model Context Protocol oferă SDK-uri oficiale pentru mai multe limbaje:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) 
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

## Lucrul cu SDK-urile MCP

Această secțiune oferă exemple practice de implementare MCP în mai multe limbaje de programare. Poți găsi coduri demonstrative în directorul `samples` organizate pe limbaje.

### Exemple disponibile

Repository-ul include [implementări de exemplu](../../../04-PracticalImplementation/samples) în următoarele limbaje:

- [C#](./samples/csharp/README.md)
- [Java](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Fiecare exemplu demonstrează conceptele cheie MCP și tiparele de implementare pentru limbajul și ecosistemul respectiv.

## Funcționalități principale ale serverului

Serverele MCP pot implementa orice combinație a acestor funcționalități:

### Resurse
Resursele oferă context și date pentru utilizator sau modelul AI:
- Repozitoare de documente
- Baze de cunoștințe
- Surse de date structurate
- Sisteme de fișiere

### Prompturi
Prompturile sunt mesaje și fluxuri de lucru șablonizate pentru utilizatori:
- Șabloane de conversație predefinite
- Modele ghidate de interacțiune
- Structuri specializate de dialog

### Unelte
Uneltele sunt funcții pe care modelul AI le poate executa:
- Utilitare de procesare a datelor
- Integrare cu API-uri externe
- Capacități computaționale
- Funcționalități de căutare

## Exemple de implementare: C#

Repository-ul oficial C# SDK conține mai multe implementări demonstrative care arată diferite aspecte ale MCP:

- **Client MCP de bază**: Exemplu simplu care arată cum să creezi un client MCP și să apelezi unelte
- **Server MCP de bază**: Implementare minimă a unui server cu înregistrare simplă a uneltelor
- **Server MCP avansat**: Server complet cu înregistrare unelte, autentificare și gestionare erori
- **Integrare ASP.NET**: Exemple care demonstrează integrarea cu ASP.NET Core
- **Tipare de implementare a uneltelor**: Diverse tipare pentru implementarea uneltelor cu niveluri diferite de complexitate

SDK-ul MCP pentru C# este în stadiu preview și API-urile pot suferi modificări. Vom actualiza continuu acest blog pe măsură ce SDK-ul evoluează.

### Funcționalități cheie
- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)

- Construirea [primului tău Server MCP](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

Pentru exemple complete de implementare C#, vizitează [repository-ul oficial cu exemple C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Exemplu de implementare: Java

SDK-ul Java oferă opțiuni robuste pentru implementarea MCP cu funcționalități de nivel enterprise.

### Funcționalități cheie

- Integrare cu Spring Framework
- Siguranță puternică a tipurilor
- Suport pentru programare reactivă
- Gestionare completă a erorilor

Pentru un exemplu complet de implementare Java, vezi [exemplul Java](samples/java/containerapp/README.md) din directorul de exemple.

## Exemplu de implementare: JavaScript

SDK-ul JavaScript oferă o abordare ușoară și flexibilă pentru implementarea MCP.

### Funcționalități cheie

- Suport pentru Node.js și browser
- API bazat pe Promises
- Integrare ușoară cu Express și alte framework-uri
- Suport WebSocket pentru streaming

Pentru un exemplu complet de implementare JavaScript, vezi [exemplul JavaScript](samples/javascript/README.md) din directorul de exemple.

## Exemplu de implementare: Python

SDK-ul Python oferă o abordare pythonică pentru implementarea MCP cu integrări excelente în framework-urile ML.

### Funcționalități cheie

- Suport async/await cu asyncio
- Integrare cu Flask și FastAPI
- Înregistrare simplă a uneltelor
- Integrare nativă cu biblioteci populare ML

Pentru un exemplu complet de implementare Python, vezi [exemplul Python](samples/python/README.md) din directorul de exemple.

## Gestionarea API-urilor

Azure API Management este o soluție excelentă pentru securizarea serverelor MCP. Ideea este să pui o instanță Azure API Management în fața serverului MCP și să lași aceasta să gestioneze funcționalități pe care probabil le vei dori, cum ar fi:

- limitarea ratei cererilor
- gestionarea token-urilor
- monitorizare
- echilibrare a încărcării
- securitate

### Exemplu Azure

Iată un exemplu Azure care face exact asta, adică [crearea unui server MCP și securizarea lui cu Azure API Management](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Vezi cum se desfășoară fluxul de autorizare în imaginea de mai jos:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true) 

În imaginea de mai sus, se întâmplă următoarele:

- Autentificarea/Autorizarea se realizează folosind Microsoft Entra.
- Azure API Management acționează ca un gateway și folosește politici pentru a direcționa și gestiona traficul.
- Azure Monitor înregistrează toate cererile pentru analize ulterioare.

#### Fluxul de autorizare

Să analizăm mai detaliat fluxul de autorizare:

![Diagramă de secvență](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### Specificația autorizării MCP

Află mai multe despre [specificația autorizării MCP](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization#2-10-third-party-authorization-flow)

## Implementarea unui server MCP remote pe Azure

Să vedem dacă putem implementa exemplul menționat mai devreme:

1. Clonează repository-ul

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

2. Înregistrează `Microsoft.App` cu comanda:

    ` resource provider.
    * If you are using Azure CLI, run `az provider register --namespace Microsoft.App --wait`.
    * If you are using Azure PowerShell, run `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Then run `

    Așteaptă puțin și verifică cu `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` dacă înregistrarea s-a finalizat.

3. Rulează această comandă [azd](https://aka.ms/azd) pentru a provisiona serviciul de API management, funcția app (cu codul) și toate celelalte resurse Azure necesare:

    ```shell
    azd up
    ```

    Această comandă ar trebui să implementeze toate resursele cloud pe Azure.

### Testarea serverului cu MCP Inspector

1. Într-o **fereastră nouă de terminal**, instalează și pornește MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Ar trebui să vezi o interfață similară cu:

    ![Conectare la Node inspector](../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.ro.png) 

2. Apasă CTRL și dă click pentru a încărca aplicația web MCP Inspector de la URL-ul afișat de aplicație (ex: http://127.0.0.1:6274/#resources)
3. Setează tipul de transport la `SSE`
1. Set the URL to your running API Management SSE endpoint displayed after `azd up` și apasă **Connect**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

4. **Listarea uneltelor**. Click pe o unealtă și apoi **Run Tool**.  

Dacă toate pașii au fost urmați corect, ar trebui să fii acum conectat la serverul MCP și să fi reușit să apelezi o unealtă.

## Servere MCP pentru Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Acest set de repository-uri reprezintă un template quickstart pentru construirea și implementarea rapidă a serverelor MCP remote personalizate folosind Azure Functions cu Python, C# .NET sau Node/TypeScript.

Aceste exemple oferă o soluție completă care permite dezvoltatorilor să:

- Dezvolte și ruleze local: să dezvolte și să depaneze un server MCP pe o mașină locală
- Implementeze în Azure: să implementeze ușor în cloud cu o comandă simplă azd up
- Se conecteze din clienți: să se conecteze la serverul MCP din diverse clienți, inclusiv modul agent Copilot din VS Code și instrumentul MCP Inspector

### Funcționalități cheie:

- Securitate prin design: Serverul MCP este securizat folosind chei și HTTPS
- Opțiuni de autentificare: Suportă OAuth folosind autentificarea încorporată și/sau API Management
- Izolare de rețea: Permite izolarea rețelei folosind Azure Virtual Networks (VNET)
- Arhitectură serverless: Folosește Azure Functions pentru execuție scalabilă, bazată pe evenimente
- Dezvoltare locală: Suport complet pentru dezvoltare și depanare locală
- Implementare simplificată: Proces de implementare simplificat în Azure

Repository-ul include toate fișierele de configurare necesare, codul sursă și definițiile infrastructurii pentru a începe rapid cu o implementare MCP pregătită pentru producție.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Exemplu de implementare MCP folosind Azure Functions cu Python

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Exemplu de implementare MCP folosind Azure Functions cu C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Exemplu de implementare MCP folosind Azure Functions cu Node/TypeScript.

## Concluzii importante

- SDK-urile MCP oferă unelte specifice limbajelor pentru implementarea soluțiilor MCP robuste
- Procesul de depanare și testare este esențial pentru aplicații MCP fiabile
- Șabloanele de prompt reutilizabile asigură interacțiuni consistente cu AI-ul
- Fluxurile de lucru bine proiectate pot orchestra sarcini complexe folosind mai multe unelte
- Implementarea soluțiilor MCP necesită atenție la securitate, performanță și gestionarea erorilor

## Exercițiu

Proiectează un flux de lucru MCP practic care să rezolve o problemă reală din domeniul tău:

1. Identifică 3-4 unelte care ar fi utile pentru rezolvarea acestei probleme
2. Creează o diagramă a fluxului de lucru care arată cum interacționează aceste unelte
3. Implementează o versiune de bază a uneia dintre unelte folosind limbajul preferat
4. Creează un șablon de prompt care să ajute modelul să folosească eficient unealta ta

## Resurse suplimentare


---

Următorul: [Subiecte avansate](../05-AdvancedTopics/README.md)

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere automată AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un traducător uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.