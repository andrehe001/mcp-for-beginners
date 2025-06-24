<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "36de9fae488d6de554d969fe8e0801a8",
  "translation_date": "2025-06-20T19:13:11+00:00",
  "source_file": "09-CaseStudy/apimsample.md",
  "language_code": "de"
}
-->
# Fallstudie: REST-API in API Management als MCP-Server bereitstellen

Azure API Management ist ein Dienst, der ein Gateway über Ihren API-Endpunkten bereitstellt. Dabei fungiert Azure API Management als Proxy vor Ihren APIs und kann entscheiden, wie mit eingehenden Anfragen verfahren wird.

Durch die Nutzung erhalten Sie eine Vielzahl von Funktionen wie:

- **Sicherheit**: Sie können alles von API-Schlüsseln, JWT bis hin zu Managed Identity verwenden.
- **Rate Limiting**: Eine großartige Funktion ist die Möglichkeit, zu bestimmen, wie viele Aufrufe pro Zeiteinheit durchgelassen werden. Dies sorgt dafür, dass alle Nutzer eine gute Erfahrung machen und Ihr Dienst nicht mit Anfragen überlastet wird.
- **Skalierung & Lastverteilung**: Sie können mehrere Endpunkte einrichten, um die Last zu verteilen, und auch entscheiden, wie die Lastverteilung erfolgen soll.
- **KI-Funktionen wie semantisches Caching**, Token-Limits und Token-Überwachung und mehr. Diese Funktionen verbessern die Reaktionsfähigkeit und helfen Ihnen, Ihre Token-Ausgaben im Blick zu behalten. [Mehr dazu hier lesen](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Warum MCP + Azure API Management?

Das Model Context Protocol entwickelt sich schnell zum Standard für agentenbasierte KI-Anwendungen und wie Werkzeuge und Daten konsistent bereitgestellt werden. Azure API Management ist die natürliche Wahl, wenn Sie APIs „managen“ müssen. MCP-Server integrieren sich oft mit anderen APIs, um beispielsweise Anfragen an ein Werkzeug weiterzuleiten. Daher macht die Kombination von Azure API Management und MCP sehr viel Sinn.

## Überblick

In diesem speziellen Anwendungsfall lernen wir, wie man API-Endpunkte als MCP-Server bereitstellt. Dadurch können wir diese Endpunkte einfach in eine agentenbasierte App integrieren und gleichzeitig die Funktionen von Azure API Management nutzen.

## Hauptfunktionen

- Sie wählen die Endpunkt-Methoden aus, die Sie als Werkzeuge bereitstellen möchten.
- Die zusätzlichen Funktionen hängen davon ab, was Sie im Policy-Bereich Ihrer API konfigurieren. Hier zeigen wir Ihnen, wie Sie Rate Limiting hinzufügen können.

## Vorbereitung: API importieren

Falls Sie bereits eine API in Azure API Management haben, können Sie diesen Schritt überspringen. Wenn nicht, schauen Sie sich diesen Link an: [API in Azure API Management importieren](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## API als MCP-Server bereitstellen

Um die API-Endpunkte bereitzustellen, gehen Sie wie folgt vor:

1. Navigieren Sie zum Azure-Portal unter <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
Öffnen Sie Ihre API Management-Instanz.

1. Wählen Sie im linken Menü APIs > MCP Servers > + Create new MCP Server.

1. Wählen Sie unter API eine REST-API aus, die Sie als MCP-Server bereitstellen möchten.

1. Wählen Sie eine oder mehrere API-Operationen aus, die Sie als Werkzeuge bereitstellen wollen. Sie können alle oder nur bestimmte Operationen auswählen.

    ![Methoden zur Bereitstellung auswählen](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Klicken Sie auf **Create**.

1. Navigieren Sie im Menü zu **APIs** und **MCP Servers**, dort sollten Sie Folgendes sehen:

    ![MCP-Server im Hauptbereich anzeigen](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    Der MCP-Server wurde erstellt und die API-Operationen sind als Werkzeuge verfügbar. Der MCP-Server wird im MCP Servers-Bereich angezeigt. Die URL-Spalte zeigt den Endpunkt des MCP-Servers, den Sie zum Testen oder in einer Client-Anwendung aufrufen können.

## Optional: Richtlinien konfigurieren

Azure API Management verwendet das Konzept der Policies, mit denen Sie verschiedene Regeln für Ihre Endpunkte festlegen können, z. B. Rate Limiting oder semantisches Caching. Diese Richtlinien werden in XML geschrieben.

So können Sie eine Richtlinie für das Rate Limiting Ihres MCP-Servers einrichten:

1. Wählen Sie im Portal unter APIs **MCP Servers** aus.

1. Wählen Sie den erstellten MCP-Server aus.

1. Wählen Sie im linken Menü unter MCP **Policies**.

1. Fügen Sie im Policy-Editor die gewünschten Richtlinien hinzu oder bearbeiten Sie diese. Die Richtlinien sind im XML-Format definiert. Zum Beispiel können Sie eine Richtlinie hinzufügen, die die Aufrufe der MCP-Server-Werkzeuge limitiert (in diesem Beispiel 5 Aufrufe pro 30 Sekunden und Client-IP-Adresse). Hier ist ein XML-Beispiel für das Rate Limiting:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    So sieht der Policy-Editor aus:

    ![Policy-Editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Ausprobieren

Lassen Sie uns sicherstellen, dass unser MCP-Server wie gewünscht funktioniert.

Dafür verwenden wir Visual Studio Code und GitHub Copilot im Agent-Modus. Wir fügen den MCP-Server zu einer *mcp.json* Datei hinzu. So fungiert Visual Studio Code als Client mit agentenbasierten Fähigkeiten, und Endbenutzer können eine Eingabeaufforderung eingeben und mit dem Server interagieren.

So fügen Sie den MCP-Server in Visual Studio Code hinzu:

1. Verwenden Sie den MCP-Befehl **Add Server** aus der Befehlspalette.

1. Wählen Sie bei der Aufforderung den Servertyp: **HTTP (HTTP oder Server Sent Events)**.

1. Geben Sie die URL des MCP-Servers in API Management ein. Beispiel: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (für SSE-Endpunkt) oder **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (für MCP-Endpunkt), beachten Sie den Unterschied der Übertragungsarten `/sse` or `/mcp`.

1. Geben Sie eine Server-ID Ihrer Wahl ein. Dieser Wert ist nicht wichtig, hilft aber, die Serverinstanz zu identifizieren.

1. Wählen Sie, ob die Konfiguration in den Workspace-Einstellungen oder den Benutzereinstellungen gespeichert werden soll.

  - **Workspace-Einstellungen** – Die Serverkonfiguration wird in einer .vscode/mcp.json Datei gespeichert, die nur im aktuellen Workspace verfügbar ist.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    Oder wenn Sie Streaming HTTP als Transport wählen, sieht es etwas anders aus:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Benutzereinstellungen** – Die Serverkonfiguration wird in Ihrer globalen *settings.json* Datei hinzugefügt und steht in allen Workspaces zur Verfügung. Die Konfiguration sieht ungefähr so aus:

    ![Benutzereinstellung](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Sie müssen außerdem eine Konfiguration hinzufügen, einen Header, damit die Authentifizierung gegenüber Azure API Management korrekt funktioniert. Es wird ein Header namens **Ocp-Apim-Subscription-Key** verwendet.

    - So fügen Sie ihn in den Einstellungen hinzu:

    ![Header für Authentifizierung hinzufügen](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png)  
    Dadurch wird eine Eingabeaufforderung angezeigt, in der Sie den API-Schlüssel eingeben können, den Sie im Azure-Portal für Ihre Azure API Management-Instanz finden.

    - Um ihn stattdessen in *mcp.json* hinzuzufügen, verwenden Sie folgendes Format:

    ```json
    "inputs": [
      {
        "type": "promptString",
        "id": "apim_key",
        "description": "API Key for Azure API Management",
        "password": true
      }
    ]
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp",
            "headers": {
                "Ocp-Apim-Subscription-Key": "Bearer ${input:apim_key}"
            }
        }
    }
    ```

### Agent-Modus verwenden

Jetzt sind wir sowohl in den Einstellungen als auch in *.vscode/mcp.json* eingerichtet. Probieren wir es aus.

Es sollte ein Werkzeuge-Symbol erscheinen, wo die vom Server bereitgestellten Werkzeuge aufgelistet sind:

![Werkzeuge vom Server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Klicken Sie auf das Werkzeuge-Symbol, Sie sollten eine Liste von Werkzeugen sehen, etwa so:

    ![Werkzeuge](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Geben Sie eine Eingabeaufforderung im Chat ein, um das Werkzeug zu nutzen. Wenn Sie zum Beispiel ein Werkzeug ausgewählt haben, das Informationen zu einer Bestellung liefert, können Sie den Agenten danach fragen. Hier ein Beispielprompt:

    ```text
    get information from order 2
    ```

    Ihnen wird nun ein Werkzeuge-Symbol angezeigt, das Sie auffordert, mit dem Aufruf eines Werkzeugs fortzufahren. Wählen Sie „Weiter“, um das Werkzeug auszuführen. Sie sollten dann eine Ausgabe wie diese sehen:

    ![Ergebnis der Eingabeaufforderung](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **Was Sie sehen, hängt von den eingerichteten Werkzeugen ab, aber die Idee ist, dass Sie eine textuelle Antwort erhalten, wie oben gezeigt.**

## Quellen

Hier können Sie mehr erfahren:

- [Tutorial zu Azure API Management und MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python-Beispiel: Sichere Remote-MCP-Server mit Azure API Management (experimentell)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP-Client-Autorisierungslabor](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Verwendung der Azure API Management-Erweiterung für VS Code zum Importieren und Verwalten von APIs](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Registrieren und Entdecken von Remote-MCP-Servern im Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Großartiges Repository, das viele KI-Funktionen mit Azure API Management zeigt
- [AI Gateway Workshops](https://azure-samples.github.io/AI-Gateway/) Enthält Workshops mit Azure Portal, ein hervorragender Einstieg, um KI-Funktionen zu evaluieren.

**Haftungsausschluss**:  
Dieses Dokument wurde mit dem KI-Übersetzungsdienst [Co-op Translator](https://github.com/Azure/co-op-translator) übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache gilt als maßgebliche Quelle. Für wichtige Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.