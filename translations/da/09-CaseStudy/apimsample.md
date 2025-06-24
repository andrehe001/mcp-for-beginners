<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "36de9fae488d6de554d969fe8e0801a8",
  "translation_date": "2025-06-20T19:21:02+00:00",
  "source_file": "09-CaseStudy/apimsample.md",
  "language_code": "da"
}
-->
# Case Study: Eksponer REST API i API Management som en MCP-server

Azure API Management er en tjeneste, der fungerer som en Gateway oven på dine API-endpoints. Den fungerer som en proxy foran dine API’er og kan afgøre, hvad der skal ske med indkommende forespørgsler.

Ved at bruge den får du en række funktioner som:

- **Sikkerhed**, hvor du kan bruge alt fra API-nøgler, JWT til managed identity.
- **Ratebegrænsning**, en fantastisk funktion, der giver dig mulighed for at bestemme, hvor mange kald der kan passere inden for en bestemt tidsenhed. Det sikrer, at alle brugere får en god oplevelse, og at din service ikke bliver overbelastet med forespørgsler.
- **Skalering og load balancing**. Du kan opsætte flere endpoints for at fordele belastningen, og du kan også vælge, hvordan load balancingen skal foregå.
- **AI-funktioner som semantisk caching**, tokenbegrænsning, tokenovervågning og mere. Disse funktioner forbedrer både svartiden og hjælper dig med at holde styr på dit tokenforbrug. [Læs mere her](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Hvorfor MCP + Azure API Management?

Model Context Protocol er hurtigt ved at blive en standard for agentiske AI-apps og til at eksponere værktøjer og data på en ensartet måde. Azure API Management er et naturligt valg, når du skal "styre" API’er. MCP-servere integrerer ofte med andre API’er for eksempelvis at løse forespørgsler til et værktøj. Derfor giver kombinationen af Azure API Management og MCP god mening.

## Oversigt

I dette specifikke tilfælde lærer vi at eksponere API-endpoints som en MCP-server. På den måde kan vi nemt gøre disse endpoints til en del af en agentisk app, samtidig med at vi udnytter funktionerne i Azure API Management.

## Nøglefunktioner

- Du vælger de endpoint-metoder, du ønsker at eksponere som værktøjer.
- De ekstra funktioner, du får, afhænger af, hvad du konfigurerer i politiksektionen for dit API. Her vil vi vise, hvordan du kan tilføje ratebegrænsning.

## Forberedelse: importer et API

Hvis du allerede har et API i Azure API Management, kan du springe dette trin over. Hvis ikke, kan du se denne vejledning, [import af et API til Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Eksponer API som MCP-server

For at eksponere API-endpoints, følg disse trin:

1. Gå til Azure Portal og denne adresse <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
   Naviger til din API Management-instans.

1. I venstremenuen vælg APIs > MCP Servers > + Create new MCP Server.

1. Under API vælg et REST API, som skal eksponeres som en MCP-server.

1. Vælg en eller flere API-operationer, som skal eksponeres som værktøjer. Du kan vælge alle operationer eller kun specifikke.

    ![Vælg metoder til eksponering](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Vælg **Create**.

1. Gå til menuen **APIs** og **MCP Servers**, hvor du bør se følgende:

    ![Se MCP-serveren i hovedpanelet](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP-serveren er oprettet, og API-operationerne er eksponeret som værktøjer. MCP-serveren vises i MCP Servers-panelet. URL-kolonnen viser endpointet for MCP-serveren, som du kan kalde til test eller i en klientapplikation.

## Valgfrit: Konfigurer politikker

Azure API Management har det centrale koncept politikker, hvor du kan sætte regler for dine endpoints, som for eksempel ratebegrænsning eller semantisk caching. Disse politikker skrives i XML.

Sådan kan du opsætte en politik til ratebegrænsning af din MCP-server:

1. I portalen, under APIs, vælg **MCP Servers**.

1. Vælg den MCP-server, du har oprettet.

1. I venstremenuen under MCP vælg **Policies**.

1. I policy-editoren tilføj eller rediger de politikker, du vil anvende på MCP-serverens værktøjer. Politikkerne defineres i XML-format. For eksempel kan du tilføje en politik, der begrænser kald til MCP-serverens værktøjer (i dette eksempel 5 kald per 30 sekunder per klient-IP-adresse). Her er XML, der vil håndhæve ratebegrænsningen:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Her er et billede af policy-editoren:

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Prøv det af

Lad os sikre, at vores MCP-server fungerer som forventet.

Til dette vil vi bruge Visual Studio Code og GitHub Copilot i Agent-tilstand. Vi tilføjer MCP-serveren til en *mcp.json*-fil. På den måde fungerer Visual Studio Code som en klient med agentiske egenskaber, og slutbrugere kan skrive en prompt og interagere med serveren.

Sådan tilføjer du MCP-serveren i Visual Studio Code:

1. Brug MCP: **Add Server-kommandoen fra Command Palette**.

1. Når du bliver bedt om det, vælg servertype: **HTTP (HTTP eller Server Sent Events)**.

1. Indtast URL’en til MCP-serveren i API Management. Eksempel: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (for SSE-endpoint) eller **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (for MCP-endpoint), bemærk forskellen i transporten er `/sse` or `/mcp`.

1. Indtast et server-ID efter eget valg. Det er ikke en vigtig værdi, men det hjælper dig med at huske, hvilken serverinstans det er.

1. Vælg, om konfigurationen skal gemmes i dine workspace-indstillinger eller brugerindstillinger.

  - **Workspace-indstillinger** – Serverkonfigurationen gemmes i en .vscode/mcp.json-fil, som kun er tilgængelig i det aktuelle workspace.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    eller hvis du vælger streaming HTTP som transport, vil det se lidt anderledes ud:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Brugerindstillinger** – Serverkonfigurationen tilføjes til din globale *settings.json*-fil og er tilgængelig i alle workspaces. Konfigurationen ligner følgende:

    ![Brugerindstilling](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Du skal også tilføje en konfiguration, et header, for at sikre korrekt autentificering mod Azure API Management. Den bruger en header kaldet **Ocp-Apim-Subscription-Key**.

    - Sådan tilføjer du den i indstillingerne:

    ![Tilføj header til autentificering](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), dette vil udløse en prompt, hvor du bliver bedt om API-nøgleværdien, som du kan finde i Azure Portal for din Azure API Management-instans.

   - For at tilføje den i *mcp.json* i stedet, kan du gøre det således:

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

### Brug Agent-tilstand

Nu er vi klar, enten i indstillingerne eller i *.vscode/mcp.json*. Lad os prøve det.

Der burde være et ikon for Tools, hvor de eksponerede værktøjer fra din server vises:

![Værktøjer fra serveren](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Klik på værktøjsikonet, og du skulle se en liste over værktøjer som denne:

    ![Værktøjer](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Indtast en prompt i chatten for at aktivere værktøjet. For eksempel, hvis du har valgt et værktøj til at hente oplysninger om en ordre, kan du spørge agenten om en ordre. Her er et eksempel på en prompt:

    ```text
    get information from order 2
    ```

    Du vil nu få vist et værktøjsikon, der spørger, om du vil fortsætte med at kalde værktøjet. Vælg at fortsætte, og du skulle nu se et output som dette:

    ![Resultat fra prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **Det, du ser ovenfor, afhænger af, hvilke værktøjer du har sat op, men idéen er, at du får et tekstbaseret svar som vist.**

## Referencer

Sådan kan du lære mere:

- [Tutorial om Azure API Management og MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python-eksempel: Sikker fjern-MCP-servere ved hjælp af Azure API Management (eksperimentel)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP klient autorisations-lab](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Brug Azure API Management-udvidelsen til VS Code til at importere og administrere API’er](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Registrer og find fjern-MCP-servere i Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Fantastisk repo, der viser mange AI-funktioner med Azure API Management
- [AI Gateway workshops](https://azure-samples.github.io/AI-Gateway/) Indeholder workshops ved brug af Azure Portal, hvilket er en god måde at begynde at evaluere AI-funktioner på.

**Ansvarsfraskrivelse**:  
Dette dokument er oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.