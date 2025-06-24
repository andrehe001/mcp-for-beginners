<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "36de9fae488d6de554d969fe8e0801a8",
  "translation_date": "2025-06-20T19:21:58+00:00",
  "source_file": "09-CaseStudy/apimsample.md",
  "language_code": "nl"
}
-->
# Case Study: REST API blootstellen in API Management als een MCP-server

Azure API Management is een service die een Gateway biedt bovenop je API-eindpunten. Hoe het werkt, is dat Azure API Management fungeert als een proxy voor je API's en kan bepalen wat er met binnenkomende verzoeken gebeurt.

Door het te gebruiken, voeg je een heleboel functies toe, zoals:

- **Beveiliging**, je kunt alles gebruiken van API-sleutels, JWT tot managed identity.
- **Rate limiting**, een geweldige functie waarmee je kunt bepalen hoeveel oproepen er per bepaalde tijdseenheid worden toegelaten. Dit helpt ervoor te zorgen dat alle gebruikers een goede ervaring hebben en dat je service niet overbelast raakt met verzoeken.
- **Schaalbaarheid & Load balancing**. Je kunt meerdere eindpunten instellen om de belasting te verdelen en ook bepalen hoe je de "load balance" wilt uitvoeren.
- **AI-functies zoals semantische caching**, tokenlimiet en tokenmonitoring en meer. Dit zijn geweldige functies die de reactietijd verbeteren en je helpen je tokenverbruik onder controle te houden. [Lees hier meer](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Waarom MCP + Azure API Management?

Model Context Protocol wordt snel een standaard voor agentische AI-apps en hoe je tools en data op een consistente manier kunt blootstellen. Azure API Management is een logische keuze wanneer je API's moet "beheren". MCP-servers integreren vaak met andere API's om bijvoorbeeld verzoeken naar een tool te routeren. Daarom is het combineren van Azure API Management en MCP heel logisch.

## Overzicht

In deze specifieke use case leren we hoe we API-eindpunten kunnen blootstellen als een MCP-server. Hiermee kunnen we deze eindpunten eenvoudig onderdeel maken van een agentische app, terwijl we ook gebruikmaken van de functies van Azure API Management.

## Belangrijkste functies

- Je selecteert de endpoint-methodes die je wilt blootstellen als tools.
- De extra functies die je krijgt, hangen af van wat je configureert in het beleidsgedeelte voor je API. Hier laten we zien hoe je rate limiting kunt toevoegen.

## Voorbereiding: een API importeren

Als je al een API in Azure API Management hebt, dan kun je deze stap overslaan. Zo niet, bekijk dan deze link: [een API importeren in Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## API blootstellen als MCP-server

Volg deze stappen om de API-eindpunten bloot te stellen:

1. Ga naar Azure Portal en navigeer naar het volgende adres <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
Navigeer naar je API Management instantie.

1. Selecteer in het linkermenu APIs > MCP Servers > + Create new MCP Server.

1. Kies bij API een REST API die je wilt blootstellen als MCP-server.

1. Selecteer één of meerdere API-operaties om bloot te stellen als tools. Je kunt alle operaties selecteren of alleen specifieke operaties.

    ![Selecteer methodes om bloot te stellen](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Klik op **Create**.

1. Ga naar het menu **APIs** en vervolgens **MCP Servers**, je zou het volgende moeten zien:

    ![Bekijk de MCP-server in het hoofdvenster](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    De MCP-server is aangemaakt en de API-operaties zijn blootgesteld als tools. De MCP-server wordt weergegeven in het MCP Servers-paneel. De URL-kolom toont het eindpunt van de MCP-server dat je kunt aanroepen voor testen of binnen een clientapplicatie.

## Optioneel: Beleid configureren

Azure API Management gebruikt het kernconcept van policies (beleid) waarin je regels instelt voor je eindpunten, zoals rate limiting of semantische caching. Deze policies worden geschreven in XML.

Zo stel je een policy in om rate limiting toe te passen op je MCP-server:

1. Ga in de portal naar APIs en selecteer **MCP Servers**.

1. Kies de MCP-server die je hebt gemaakt.

1. Selecteer in het linkermenu onder MCP **Policies**.

1. Voeg in de policy-editor de policies toe of bewerk ze die je wilt toepassen op de tools van de MCP-server. De policies zijn gedefinieerd in XML-formaat. Bijvoorbeeld, je kunt een policy toevoegen om het aantal oproepen naar de MCP-server te beperken (in dit voorbeeld 5 oproepen per 30 seconden per client IP-adres). Dit is de XML die zorgt voor rate limiting:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Dit is een afbeelding van de policy-editor:

    ![Policy-editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## Uitproberen

Laten we controleren of onze MCP-server werkt zoals bedoeld.

Hiervoor gebruiken we Visual Studio Code en GitHub Copilot in Agent-modus. We voegen de MCP-server toe aan een *mcp.json*. Zo fungeert Visual Studio Code als een client met agentische mogelijkheden en kunnen eindgebruikers een prompt typen en interactie hebben met de server.

Zo voeg je de MCP-server toe in Visual Studio Code:

1. Gebruik de MCP: **Add Server command uit de Command Palette**.

1. Kies bij de prompt het servertype: **HTTP (HTTP of Server Sent Events)**.

1. Voer de URL in van de MCP-server in API Management. Bijvoorbeeld: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (voor SSE-eindpunt) of **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (voor MCP-eindpunt), let op het verschil tussen de transports: `/sse` or `/mcp`.

1. Voer een server-ID in naar keuze. Dit is geen belangrijke waarde, maar helpt je herinneren wat deze serverinstantie is.

1. Kies of je de configuratie wilt opslaan in je workspace-instellingen of gebruikersinstellingen.

  - **Workspace-instellingen** - De serverconfiguratie wordt opgeslagen in een .vscode/mcp.json bestand dat alleen beschikbaar is in de huidige workspace.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    Of als je streaming HTTP als transport kiest, ziet het er iets anders uit:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Gebruikersinstellingen** - De serverconfiguratie wordt toegevoegd aan je globale *settings.json* bestand en is beschikbaar in alle workspaces. De configuratie ziet er ongeveer zo uit:

    ![Gebruikersinstelling](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Je moet ook een configuratie toevoegen, een header om ervoor te zorgen dat de authenticatie correct verloopt richting Azure API Management. Het gebruikt een header genaamd **Ocp-Apim-Subscription-Key**.

    - Zo voeg je deze toe aan de instellingen:

    ![Header toevoegen voor authenticatie](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), hierdoor verschijnt een prompt die je vraagt om de API-sleutel in te voeren. Deze sleutel vind je in Azure Portal voor je Azure API Management-instantie.

    - Om het toe te voegen aan *mcp.json*, kun je het als volgt doen:

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

### Agent-modus gebruiken

Nu alles is ingesteld in de instellingen of in *.vscode/mcp.json*. Laten we het uitproberen.

Er zou een Tools-icoon moeten zijn, zoals hieronder, waar de blootgestelde tools van je server worden weergegeven:

![Tools van de server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Klik op het tools-icoon en je ziet een lijst met tools zoals deze:

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Typ een prompt in de chat om de tool aan te roepen. Bijvoorbeeld, als je een tool hebt geselecteerd om informatie over een bestelling op te vragen, kun je de agent vragen naar een bestelling. Dit is een voorbeeldprompt:

    ```text
    get information from order 2
    ```

    Je krijgt nu een tools-icoon te zien die je vraagt door te gaan met het aanroepen van een tool. Kies om door te gaan met het uitvoeren van de tool, je zou nu een resultaat moeten zien zoals hieronder:

    ![Resultaat van prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **Wat je hierboven ziet, hangt af van welke tools je hebt ingesteld, maar het idee is dat je een tekstuele respons krijgt zoals hierboven**

## Referenties

Zo kun je meer leren:

- [Tutorial over Azure API Management en MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python voorbeeld: Beveilig remote MCP-servers met Azure API Management (experimenteel)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP client autorisatielab](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Gebruik de Azure API Management extensie voor VS Code om API's te importeren en beheren](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Registreer en ontdek remote MCP-servers in Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Geweldige repo die veel AI-mogelijkheden met Azure API Management laat zien
- [AI Gateway workshops](https://azure-samples.github.io/AI-Gateway/) Bevat workshops met Azure Portal, een geweldige manier om AI-mogelijkheden te verkennen.

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsdienst [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het oorspronkelijke document in de originele taal moet als de gezaghebbende bron worden beschouwd. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.