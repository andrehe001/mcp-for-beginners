<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "36de9fae488d6de554d969fe8e0801a8",
  "translation_date": "2025-06-20T19:20:45+00:00",
  "source_file": "09-CaseStudy/apimsample.md",
  "language_code": "sv"
}
-->
# Fallstudie: Exponera REST API i API Management som en MCP-server

Azure API Management är en tjänst som erbjuder en Gateway ovanpå dina API-endpoints. Så här fungerar det: Azure API Management agerar som en proxy framför dina API:er och kan avgöra hur inkommande förfrågningar hanteras.

Genom att använda tjänsten får du en rad funktioner som:

- **Säkerhet**, där du kan använda allt från API-nycklar, JWT till hanterad identitet.
- **Begränsning av anrop**, en utmärkt funktion som låter dig bestämma hur många anrop som får passera per tidsenhet. Detta säkerställer att alla användare får en bra upplevelse och att din tjänst inte överbelastas med förfrågningar.
- **Skalning och lastbalansering**. Du kan konfigurera flera endpoints för att fördela belastningen och även bestämma hur lastbalanseringen ska ske.
- **AI-funktioner som semantisk caching**, tokenbegränsning och tokenövervakning med mera. Dessa är kraftfulla funktioner som förbättrar svarstider och hjälper dig hålla koll på din tokenanvändning. [Läs mer här](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Varför MCP + Azure API Management?

Model Context Protocol håller snabbt på att bli en standard för agentbaserade AI-appar och hur verktyg och data exponeras på ett enhetligt sätt. Azure API Management är ett naturligt val när du behöver "hantera" API:er. MCP-servrar integreras ofta med andra API:er för att exempelvis lösa förfrågningar till ett verktyg. Därför är kombinationen av Azure API Management och MCP mycket logisk.

## Översikt

I detta specifika fall kommer vi att lära oss hur man exponerar API-endpoints som en MCP-server. Genom att göra detta kan vi enkelt göra dessa endpoints till en del av en agentbaserad app samtidigt som vi utnyttjar funktionerna i Azure API Management.

## Viktiga funktioner

- Du väljer vilka endpoint-metoder som ska exponeras som verktyg.
- De extra funktionerna du får beror på vad du konfigurerar i policydelen för ditt API. Här visar vi hur du kan lägga till begränsning av anrop.

## Förberedelse: importera ett API

Om du redan har ett API i Azure API Management kan du hoppa över detta steg. Annars kan du kika på denna länk, [importera ett API till Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Exponera API som MCP-server

För att exponera API-endpoints, följ dessa steg:

1. Gå till Azure Portal och följ adressen <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
Navigera till din API Management-instans.

1. I vänstermenyn, välj APIs > MCP Servers > + Create new MCP Server.

1. Under API, välj ett REST API som ska exponeras som MCP-server.

1. Välj en eller flera API-operationer att exponera som verktyg. Du kan välja alla operationer eller bara specifika.

    ![Välj metoder att exponera](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Välj **Create**.

1. Gå till menyalternativen **APIs** och **MCP Servers**, du bör nu se följande:

    ![Se MCP-servern i huvudpanelen](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP-servern är skapad och API-operationerna exponeras som verktyg. MCP-servern visas i MCP Servers-panelen. Kolumnen URL visar endpointen för MCP-servern som du kan anropa för test eller i en klientapplikation.

## Valfritt: Konfigurera policies

Azure API Management har kärnkonceptet policies där du kan sätta upp olika regler för dina endpoints, som exempelvis begränsning av anrop eller semantisk caching. Dessa policies skrivs i XML.

Så här kan du skapa en policy för att begränsa anrop till din MCP-server:

1. I portalen, under APIs, välj **MCP Servers**.

1. Välj den MCP-server du skapade.

1. I vänstermenyn, under MCP, välj **Policies**.

1. I policyeditorn, lägg till eller redigera de policies du vill applicera på MCP-serverns verktyg. Policies definieras i XML-format. Till exempel kan du lägga till en policy som begränsar anrop till MCP-serverns verktyg (i detta exempel 5 anrop per 30 sekunder per klient-IP-adress). Här är XML som begränsar anropen:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Här är en bild på policyeditorn:

    ![Policyeditor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## Testa

Låt oss säkerställa att vår MCP-server fungerar som den ska.

För detta använder vi Visual Studio Code och GitHub Copilot i Agent-läge. Vi kommer att lägga till MCP-servern i en *mcp.json*. Genom att göra detta agerar Visual Studio Code som en klient med agentfunktioner och slutanvändare kan skriva en prompt och interagera med servern.

Så här lägger du till MCP-servern i Visual Studio Code:

1. Använd kommandot MCP: **Add Server från Command Palette**.

1. När du blir tillfrågad, välj servertypen: **HTTP (HTTP eller Server Sent Events)**.

1. Ange URL för MCP-servern i API Management. Exempel: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (för SSE-endpoint) eller **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (för MCP-endpoint), notera skillnaden mellan transporterna är `/sse` or `/mcp`.

1. Ange ett server-ID efter eget val. Detta är inte ett kritiskt värde men hjälper dig att minnas vilken serverinstans det är.

1. Välj om konfigurationen ska sparas i workspace-inställningar eller användarinställningar.

  - **Workspace-inställningar** - Serverkonfigurationen sparas i en .vscode/mcp.json-fil som bara är tillgänglig i det aktuella workspace:et.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    Om du istället väljer streaming HTTP som transport ser det lite annorlunda ut:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Användarinställningar** - Serverkonfigurationen läggs till i din globala *settings.json*-fil och är tillgänglig i alla workspaces. Konfigurationen ser ut ungefär så här:

    ![Användarinställning](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Du behöver också lägga till en konfiguration, en header för att autentisera korrekt mot Azure API Management. Den använder en header som heter **Ocp-Apim-Subscription-Key**.

    - Så här kan du lägga till den i inställningarna:

    ![Lägga till header för autentisering](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), detta gör att en prompt visas där du får ange API-nyckeln som du hittar i Azure Portal för din Azure API Management-instans.

    - För att lägga till den i *mcp.json* istället, kan du göra så här:

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

### Använd Agent-läge

Nu är allt konfigurerat i antingen inställningarna eller i *.vscode/mcp.json*. Låt oss testa.

Det ska finnas en Verktygsikon som denna, där de exponerade verktygen från din server listas:

![Verktyg från servern](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Klicka på verktygsikonen så bör du se en lista med verktyg som denna:

    ![Verktyg](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Skriv en prompt i chatten för att anropa verktyget. Om du till exempel valt ett verktyg för att hämta information om en order kan du fråga agenten om en order. Här är ett exempel på prompt:

    ```text
    get information from order 2
    ```

    Du kommer nu att få en verktygsikon som frågar om du vill fortsätta med att anropa verktyget. Välj att fortsätta och du bör se ett svar som detta:

    ![Resultat från prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **Det du ser ovan beror på vilka verktyg du har konfigurerat, men tanken är att du får ett textbaserat svar som ovan.**

## Referenser

Så här kan du lära dig mer:

- [Tutorial om Azure API Management och MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python-exempel: Säkerställ fjärranslutna MCP-servrar med Azure API Management (experimentellt)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP-klient auktorisationslab](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Använd Azure API Management-tillägget för VS Code för att importera och hantera API:er](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Registrera och upptäck fjärr-MCP-servrar i Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Ett utmärkt repo som visar många AI-funktioner med Azure API Management
- [AI Gateway workshops](https://azure-samples.github.io/AI-Gateway/) Innehåller workshops med Azure Portal, vilket är ett bra sätt att börja utforska AI-funktioner.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen var medveten om att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål ska betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.