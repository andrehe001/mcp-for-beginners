<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5384bbb2a92d00d5d7e66274dbe0331d",
  "translation_date": "2025-06-20T18:19:27+00:00",
  "source_file": "04-PracticalImplementation/README.md",
  "language_code": "de"
}
-->
# Praktische Umsetzung

Die praktische Umsetzung ist der Moment, in dem die Stärke des Model Context Protocol (MCP) greifbar wird. Während das Verständnis der Theorie und Architektur hinter MCP wichtig ist, zeigt sich der wahre Wert erst, wenn Sie diese Konzepte anwenden, um Lösungen zu entwickeln, zu testen und bereitzustellen, die reale Probleme lösen. Dieses Kapitel schlägt die Brücke zwischen theoretischem Wissen und praktischer Entwicklung und führt Sie durch den Prozess, MCP-basierte Anwendungen zum Leben zu erwecken.

Egal, ob Sie intelligente Assistenten entwickeln, KI in Geschäftsabläufe integrieren oder maßgeschneiderte Werkzeuge für die Datenverarbeitung erstellen – MCP bietet eine flexible Grundlage. Sein sprachunabhängiges Design und die offiziellen SDKs für gängige Programmiersprachen machen es für eine breite Entwicklergruppe zugänglich. Durch die Nutzung dieser SDKs können Sie schnell Prototypen erstellen, iterieren und Ihre Lösungen auf verschiedenen Plattformen und Umgebungen skalieren.

In den folgenden Abschnitten finden Sie praktische Beispiele, Beispielcode und Bereitstellungsstrategien, die zeigen, wie MCP in C#, Java, TypeScript, JavaScript und Python implementiert wird. Sie lernen außerdem, wie Sie MCP-Server debuggen und testen, APIs verwalten und Lösungen mit Azure in der Cloud bereitstellen. Diese praxisnahen Ressourcen sind darauf ausgelegt, Ihr Lernen zu beschleunigen und Ihnen zu helfen, robuste, produktionsreife MCP-Anwendungen sicher zu entwickeln.

## Überblick

Diese Lektion konzentriert sich auf praktische Aspekte der MCP-Implementierung in verschiedenen Programmiersprachen. Wir erkunden, wie MCP SDKs in C#, Java, TypeScript, JavaScript und Python verwendet werden, um robuste Anwendungen zu erstellen, MCP-Server zu debuggen und zu testen sowie wiederverwendbare Ressourcen, Prompts und Tools zu erstellen.

## Lernziele

Am Ende dieser Lektion werden Sie in der Lage sein:
- MCP-Lösungen mit offiziellen SDKs in verschiedenen Programmiersprachen zu implementieren
- MCP-Server systematisch zu debuggen und zu testen
- Serverfunktionen (Resources, Prompts und Tools) zu erstellen und zu nutzen
- Effektive MCP-Workflows für komplexe Aufgaben zu entwerfen
- MCP-Implementierungen hinsichtlich Leistung und Zuverlässigkeit zu optimieren

## Offizielle SDK-Ressourcen

Das Model Context Protocol bietet offizielle SDKs für mehrere Sprachen:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) 
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

## Arbeiten mit MCP SDKs

Dieser Abschnitt bietet praktische Beispiele zur Implementierung von MCP in mehreren Programmiersprachen. Beispielcode finden Sie im Verzeichnis `samples`, das nach Sprachen organisiert ist.

### Verfügbare Beispiele

Das Repository enthält [Beispielimplementierungen](../../../04-PracticalImplementation/samples) in den folgenden Sprachen:

- [C#](./samples/csharp/README.md)
- [Java](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Jedes Beispiel veranschaulicht zentrale MCP-Konzepte und Implementierungsmuster für die jeweilige Sprache und das Ökosystem.

## Kernfunktionen des Servers

MCP-Server können jede Kombination dieser Funktionen implementieren:

### Resources
Resources stellen Kontext und Daten bereit, die vom Benutzer oder dem KI-Modell genutzt werden:
- Dokumenten-Repositorien
- Wissensdatenbanken
- Strukturierte Datenquellen
- Dateisysteme

### Prompts
Prompts sind vorgefertigte Nachrichten und Abläufe für Benutzer:
- Vordefinierte Gesprächsvorlagen
- Geführte Interaktionsmuster
- Spezialisierte Dialogstrukturen

### Tools
Tools sind Funktionen, die das KI-Modell ausführen kann:
- Dienstprogramme zur Datenverarbeitung
- Integration externer APIs
- Rechenkapazitäten
- Suchfunktionen

## Beispielimplementierungen: C#

Das offizielle C# SDK-Repository enthält mehrere Beispielimplementierungen, die verschiedene Aspekte von MCP demonstrieren:

- **Basic MCP Client**: Einfaches Beispiel, das zeigt, wie man einen MCP-Client erstellt und Tools aufruft
- **Basic MCP Server**: Minimale Serverimplementierung mit grundlegender Tool-Registrierung
- **Advanced MCP Server**: Voll ausgestatteter Server mit Tool-Registrierung, Authentifizierung und Fehlerbehandlung
- **ASP.NET Integration**: Beispiele zur Integration mit ASP.NET Core
- **Tool Implementation Patterns**: Verschiedene Muster zur Implementierung von Tools mit unterschiedlichen Komplexitätsgraden

Das MCP C# SDK befindet sich in der Vorschau, daher können sich APIs ändern. Wir werden diesen Blog kontinuierlich aktualisieren, während sich das SDK weiterentwickelt.

### Wichtige Funktionen
- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)

- Erstellen Sie Ihren [ersten MCP Server](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

Für vollständige C# Implementierungsbeispiele besuchen Sie das [offizielle C# SDK Beispiel-Repository](https://github.com/modelcontextprotocol/csharp-sdk).

## Beispielimplementierung: Java-Implementierung

Das Java SDK bietet robuste MCP-Implementierungsoptionen mit Enterprise-Features.

### Wichtige Funktionen

- Integration mit Spring Framework
- Starke Typsicherheit
- Unterstützung für reaktive Programmierung
- Umfassende Fehlerbehandlung

Für ein vollständiges Java-Beispiel siehe [Java sample](samples/java/containerapp/README.md) im Beispielverzeichnis.

## Beispielimplementierung: JavaScript-Implementierung

Das JavaScript SDK bietet einen leichten und flexiblen Ansatz zur MCP-Implementierung.

### Wichtige Funktionen

- Unterstützung für Node.js und Browser
- Promise-basierte API
- Einfache Integration mit Express und anderen Frameworks
- WebSocket-Unterstützung für Streaming

Für ein vollständiges JavaScript-Beispiel siehe [JavaScript sample](samples/javascript/README.md) im Beispielverzeichnis.

## Beispielimplementierung: Python-Implementierung

Das Python SDK bietet einen pythonischen Ansatz zur MCP-Implementierung mit exzellenter Integration in ML-Frameworks.

### Wichtige Funktionen

- Async/await-Unterstützung mit asyncio
- Integration mit Flask und FastAPI
- Einfache Tool-Registrierung
- Native Integration mit beliebten ML-Bibliotheken

Für ein vollständiges Python-Beispiel siehe [Python sample](samples/python/README.md) im Beispielverzeichnis.

## API-Management

Azure API Management ist eine hervorragende Lösung, um MCP-Server abzusichern. Die Idee ist, eine Azure API Management-Instanz vor Ihren MCP-Server zu setzen und Funktionen zu nutzen, die Sie wahrscheinlich benötigen, wie:

- Rate Limiting
- Tokenverwaltung
- Monitoring
- Lastverteilung
- Sicherheit

### Azure-Beispiel

Hier ist ein Azure-Beispiel, das genau das macht, also [einen MCP-Server erstellt und mit Azure API Management sichert](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Sehen Sie im folgenden Bild, wie der Autorisierungsablauf funktioniert:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true) 

Im oben gezeigten Bild passiert Folgendes:

- Authentifizierung/Autorisierung erfolgt über Microsoft Entra.
- Azure API Management fungiert als Gateway und nutzt Richtlinien zur Steuerung und Verwaltung des Datenverkehrs.
- Azure Monitor protokolliert alle Anfragen zur weiteren Analyse.

#### Autorisierungsablauf

Werfen wir einen genaueren Blick auf den Autorisierungsablauf:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP-Autorisierungsspezifikation

Erfahren Sie mehr über die [MCP Authorization specification](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization#2-10-third-party-authorization-flow).

## Remote MCP Server auf Azure bereitstellen

Sehen wir uns an, wie wir das zuvor erwähnte Beispiel bereitstellen können:

1. Klonen Sie das Repository

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

2. Registrieren Sie `Microsoft.App` resource provider.
    * If you are using Azure CLI, run `az provider register --namespace Microsoft.App --wait`.
    * If you are using Azure PowerShell, run `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Then run `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` und prüfen Sie nach einiger Zeit, ob die Registrierung abgeschlossen ist.

3. Führen Sie diesen [azd](https://aka.ms/azd)-Befehl aus, um den API-Management-Dienst, die Function App (mit Code) und alle weiteren benötigten Azure-Ressourcen bereitzustellen

    ```shell
    azd up
    ```

    Dieser Befehl sollte alle Cloud-Ressourcen auf Azure bereitstellen.

### Testen Ihres Servers mit MCP Inspector

1. Öffnen Sie ein **neues Terminalfenster**, installieren und starten Sie MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Sie sollten eine Benutzeroberfläche ähnlich der folgenden sehen:

    ![Connect to Node inspector](../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.de.png) 

2. Klicken Sie mit gedrückter STRG-Taste, um die MCP Inspector Web-App über die vom Tool angezeigte URL zu laden (z.B. http://127.0.0.1:6274/#resources)
3. Stellen Sie den Transporttyp auf `SSE`
1. Set the URL to your running API Management SSE endpoint displayed after `azd up` ein und klicken Sie auf **Connect**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

5. **Tools auflisten**. Klicken Sie auf ein Tool und wählen Sie **Run Tool**.

Wenn alle Schritte erfolgreich waren, sind Sie nun mit dem MCP-Server verbunden und konnten ein Tool aufrufen.

## MCP-Server für Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Dieses Set von Repositories ist eine Schnellstartvorlage zum Erstellen und Bereitstellen benutzerdefinierter Remote MCP (Model Context Protocol) Server mithilfe von Azure Functions mit Python, C# .NET oder Node/TypeScript.

Die Beispiele bieten eine Komplettlösung, die Entwicklern ermöglicht:

- Lokal zu entwickeln und auszuführen: Entwicklung und Debugging eines MCP-Servers auf einer lokalen Maschine
- Bereitstellung in Azure: Einfache Cloud-Bereitstellung mit einem einfachen azd up-Befehl
- Verbindung von Clients: Verbindung zum MCP-Server von verschiedenen Clients, einschließlich des Copilot Agent-Modus von VS Code und dem MCP Inspector Tool

### Wichtige Funktionen:

- Sicherheit von Grund auf: Der MCP-Server ist durch Schlüssel und HTTPS gesichert
- Authentifizierungsoptionen: Unterstützt OAuth mit integrierter Authentifizierung und/oder API Management
- Netzwerkisolierung: Ermöglicht Netzwerkisolierung mit Azure Virtual Networks (VNET)
- Serverless-Architektur: Nutzt Azure Functions für skalierbare, ereignisgesteuerte Ausführung
- Lokale Entwicklung: Umfassende Unterstützung für lokale Entwicklung und Debugging
- Einfache Bereitstellung: Vereinfachter Bereitstellungsprozess für Azure

Das Repository enthält alle notwendigen Konfigurationsdateien, Quellcode und Infrastrukturdefinitionen, um schnell mit einer produktionsreifen MCP-Serverimplementierung zu starten.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) – Beispielimplementierung von MCP mit Azure Functions und Python

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) – Beispielimplementierung von MCP mit Azure Functions und C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) – Beispielimplementierung von MCP mit Azure Functions und Node/TypeScript

## Wichtige Erkenntnisse

- MCP SDKs bieten sprachspezifische Werkzeuge zur Implementierung robuster MCP-Lösungen
- Der Debugging- und Testprozess ist entscheidend für zuverlässige MCP-Anwendungen
- Wiederverwendbare Prompt-Vorlagen ermöglichen konsistente KI-Interaktionen
- Gut gestaltete Workflows können komplexe Aufgaben mit mehreren Tools orchestrieren
- Bei der Implementierung von MCP-Lösungen sind Sicherheit, Leistung und Fehlerbehandlung zu berücksichtigen

## Übung

Entwerfen Sie einen praktischen MCP-Workflow, der ein reales Problem in Ihrem Fachgebiet löst:

1. Identifizieren Sie 3–4 Tools, die zur Lösung dieses Problems nützlich wären
2. Erstellen Sie ein Workflow-Diagramm, das zeigt, wie diese Tools zusammenwirken
3. Implementieren Sie eine einfache Version eines der Tools in Ihrer bevorzugten Sprache
4. Erstellen Sie eine Prompt-Vorlage, die dem Modell hilft, Ihr Tool effektiv zu nutzen

## Zusätzliche Ressourcen


---

Weiter: [Fortgeschrittene Themen](../05-AdvancedTopics/README.md)

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe des KI-Übersetzungsdienstes [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner Ursprungssprache ist als maßgebliche Quelle zu betrachten. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die durch die Nutzung dieser Übersetzung entstehen.