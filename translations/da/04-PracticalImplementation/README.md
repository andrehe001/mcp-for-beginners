<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5384bbb2a92d00d5d7e66274dbe0331d",
  "translation_date": "2025-06-20T18:37:30+00:00",
  "source_file": "04-PracticalImplementation/README.md",
  "language_code": "da"
}
-->
# Praktisk implementering

Praktisk implementering er, hvor kraften i Model Context Protocol (MCP) bliver håndgribelig. Selvom det er vigtigt at forstå teorien og arkitekturen bag MCP, opstår den egentlige værdi, når du anvender disse koncepter til at bygge, teste og implementere løsninger, der løser virkelige problemer. Dette kapitel bygger bro mellem konceptuel viden og praktisk udvikling og guider dig gennem processen med at bringe MCP-baserede applikationer til live.

Uanset om du udvikler intelligente assistenter, integrerer AI i forretningsprocesser eller bygger specialværktøjer til databehandling, giver MCP en fleksibel platform. Dets sprogagnostiske design og officielle SDK’er til populære programmeringssprog gør det tilgængeligt for mange udviklere. Ved at udnytte disse SDK’er kan du hurtigt prototype, iterere og skalere dine løsninger på tværs af forskellige platforme og miljøer.

I de følgende afsnit finder du praktiske eksempler, kodeeksempler og implementeringsstrategier, der viser, hvordan man implementerer MCP i C#, Java, TypeScript, JavaScript og Python. Du lærer også, hvordan du debugger og tester dine MCP-servere, håndterer API’er og implementerer løsninger i skyen ved hjælp af Azure. Disse praktiske ressourcer er designet til at fremskynde din læring og hjælpe dig med at opbygge robuste og produktionsklare MCP-applikationer med selvtillid.

## Oversigt

Denne lektion fokuserer på de praktiske aspekter af MCP-implementering på tværs af flere programmeringssprog. Vi undersøger, hvordan man bruger MCP SDK’er i C#, Java, TypeScript, JavaScript og Python til at bygge robuste applikationer, debugge og teste MCP-servere samt skabe genanvendelige ressourcer, prompts og værktøjer.

## Læringsmål

Efter denne lektion vil du kunne:
- Implementere MCP-løsninger ved hjælp af officielle SDK’er i forskellige programmeringssprog
- Debugge og teste MCP-servere systematisk
- Oprette og bruge serverfunktioner (Ressourcer, Prompts og Værktøjer)
- Designe effektive MCP-arbejdsgange til komplekse opgaver
- Optimere MCP-implementeringer for ydeevne og pålidelighed

## Officielle SDK-ressourcer

Model Context Protocol tilbyder officielle SDK’er til flere sprog:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) 
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

## Arbejde med MCP SDK’er

Dette afsnit giver praktiske eksempler på implementering af MCP på tværs af flere programmeringssprog. Du kan finde eksempel-kode i `samples`-mappen, organiseret efter sprog.

### Tilgængelige eksempler

Repository’et indeholder [eksempler på implementeringer](../../../04-PracticalImplementation/samples) i følgende sprog:

- [C#](./samples/csharp/README.md)
- [Java](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Hvert eksempel demonstrerer centrale MCP-koncepter og implementeringsmønstre for det pågældende sprog og økosystem.

## Centrale serverfunktioner

MCP-servere kan implementere en hvilken som helst kombination af disse funktioner:

### Ressourcer
Ressourcer leverer kontekst og data til brugeren eller AI-modellen:
- Dokumentarkiver
- Vidensbaser
- Strukturerede datakilder
- Filsystemer

### Prompts
Prompts er skabelonbaserede beskeder og arbejdsgange til brugere:
- Foruddefinerede samtaleskabeloner
- Guidede interaktionsmønstre
- Specialiserede dialogstrukturer

### Værktøjer
Værktøjer er funktioner, som AI-modellen kan udføre:
- Data-behandlingsværktøjer
- Integrationer med eksterne API’er
- Beregningsfunktioner
- Søgefunktionalitet

## Eksempelimplementeringer: C#

Det officielle C# SDK-repository indeholder flere eksempler, der viser forskellige aspekter af MCP:

- **Basic MCP Client**: Simpelt eksempel, der viser, hvordan man opretter en MCP-klient og kalder værktøjer
- **Basic MCP Server**: Minimal serverimplementering med grundlæggende værktøjsregistrering
- **Advanced MCP Server**: Fuldt udstyret server med værktøjsregistrering, autentificering og fejlhåndtering
- **ASP.NET Integration**: Eksempler, der viser integration med ASP.NET Core
- **Tool Implementation Patterns**: Forskellige mønstre til implementering af værktøjer med varierende kompleksitet

MCP C# SDK’et er i preview, og API’er kan ændre sig. Vi vil løbende opdatere denne blog, efterhånden som SDK’et udvikler sig.

### Nøglefunktioner
- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)

- Byg din [første MCP Server](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

For komplette C# implementeringseksempler, besøg det [officielle C# SDK-eksempellager](https://github.com/modelcontextprotocol/csharp-sdk)

## Eksempelimplementering: Java-implementering

Java SDK tilbyder robuste MCP-implementeringsmuligheder med enterprise-grade funktioner.

### Nøglefunktioner

- Spring Framework-integration
- Stærk typesikkerhed
- Understøttelse af reaktiv programmering
- Omfattende fejlhåndtering

For et komplet Java-eksempel, se [Java sample](samples/java/containerapp/README.md) i eksempelmappen.

## Eksempelimplementering: JavaScript-implementering

JavaScript SDK’en giver en let og fleksibel tilgang til MCP-implementering.

### Nøglefunktioner

- Understøttelse af Node.js og browsere
- Promise-baseret API
- Nem integration med Express og andre frameworks
- WebSocket-understøttelse til streaming

For et komplet JavaScript-eksempel, se [JavaScript sample](samples/javascript/README.md) i eksempelmappen.

## Eksempelimplementering: Python-implementering

Python SDK’en tilbyder en pythonisk tilgang til MCP-implementering med fremragende integration til ML-frameworks.

### Nøglefunktioner

- Async/await-understøttelse med asyncio
- Flask og FastAPI-integration
- Enkel værktøjsregistrering
- Naturlig integration med populære ML-biblioteker

For et komplet Python-eksempel, se [Python sample](samples/python/README.md) i eksempelmappen.

## API-styring

Azure API Management er en fremragende løsning til at sikre MCP-servere. Ideen er at placere en Azure API Management-instans foran din MCP-server og lade den håndtere funktioner, som du sandsynligvis vil have brug for, såsom:

- rate limiting
- tokenhåndtering
- overvågning
- load balancing
- sikkerhed

### Azure-eksempel

Her er et Azure-eksempel, der gør netop det, altså [opretter en MCP-server og sikrer den med Azure API Management](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Se hvordan autorisationsflowet foregår i billedet nedenfor:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true) 

I det foregående billede sker følgende:

- Autentificering/autorisation sker via Microsoft Entra.
- Azure API Management fungerer som gateway og bruger politikker til at styre og håndtere trafik.
- Azure Monitor logger alle forespørgsler til videre analyse.

#### Autorisationsflow

Lad os se nærmere på autorisationsflowet:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP autorisationsspecifikation

Læs mere om [MCP Authorization specification](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization#2-10-third-party-authorization-flow)

## Implementer Remote MCP Server til Azure

Lad os se, om vi kan implementere det eksempel, vi nævnte tidligere:

1. Klon repoet

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. Registrer `Microsoft.App` resource provider.
    * If you are using Azure CLI, run `az provider register --namespace Microsoft.App --wait`.
    * If you are using Azure PowerShell, run `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Then run `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` og vent lidt, før du tjekker, om registreringen er fuldført.

2. Kør denne [azd](https://aka.ms/azd)-kommando for at provisionere API Management service, function app (med kode) og alle andre nødvendige Azure-ressourcer

    ```shell
    azd up
    ```

    Denne kommando bør implementere alle cloud-ressourcerne på Azure

### Test din server med MCP Inspector

1. I et **nyt terminalvindue**, installer og kør MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Du bør se en brugerflade, der ligner:

    ![Connect to Node inspector](../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.da.png) 

1. CTRL-klik for at åbne MCP Inspector webappen via den URL, som appen viser (f.eks. http://127.0.0.1:6274/#resources)
1. Sæt transporttypen til `SSE`
1. Set the URL to your running API Management SSE endpoint displayed after `azd up` og **Connect**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

5. **List Tools**. Klik på et værktøj og **Run Tool**.

Hvis alle trin er gennemført korrekt, bør du nu være forbundet til MCP-serveren og have kunnet kalde et værktøj.

## MCP-servere til Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Denne samling af repositories er en hurtigstartskabelon til at bygge og implementere tilpassede remote MCP (Model Context Protocol) servere ved hjælp af Azure Functions med Python, C# .NET eller Node/TypeScript.

Eksemplerne tilbyder en komplet løsning, der gør det muligt for udviklere at:

- Bygge og køre lokalt: Udvikle og debugge en MCP-server på en lokal maskine
- Implementere til Azure: Nem implementering til skyen med en simpel azd up-kommando
- Forbinde fra klienter: Forbinde til MCP-serveren fra forskellige klienter, herunder VS Code’s Copilot agent-tilstand og MCP Inspector-værktøjet

### Nøglefunktioner:

- Sikkerhed by design: MCP-serveren sikres ved hjælp af nøgler og HTTPS
- Autentificeringsmuligheder: Understøtter OAuth via indbygget autentificering og/eller API Management
- Netværksisolation: Muliggør netværksisolation ved hjælp af Azure Virtual Networks (VNET)
- Serverless arkitektur: Udnytter Azure Functions til skalerbar, eventdrevet eksekvering
- Lokal udvikling: Omfattende støtte til lokal udvikling og debugging
- Enkel implementering: Strømlinet implementeringsproces til Azure

Repository’et indeholder alle nødvendige konfigurationsfiler, kildekode og infrastrukturbeskrivelser for hurtigt at komme i gang med en produktionsklar MCP-serverimplementering.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Eksempelimplementering af MCP med Azure Functions i Python

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Eksempelimplementering af MCP med Azure Functions i C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Eksempelimplementering af MCP med Azure Functions i Node/TypeScript.

## Vigtige pointer

- MCP SDK’er leverer sprog-specifikke værktøjer til implementering af robuste MCP-løsninger
- Debugging og test er afgørende for pålidelige MCP-applikationer
- Genanvendelige promptskabeloner sikrer konsistente AI-interaktioner
- Godt designede arbejdsgange kan orkestrere komplekse opgaver med flere værktøjer
- Implementering af MCP-løsninger kræver fokus på sikkerhed, ydeevne og fejlhåndtering

## Øvelse

Design en praktisk MCP-arbejdsgang, der løser et reelt problem inden for dit område:

1. Identificer 3-4 værktøjer, som ville være nyttige til at løse dette problem
2. Lav et arbejdsgangsdiagram, der viser, hvordan disse værktøjer interagerer
3. Implementer en grundlæggende version af et af værktøjerne i dit foretrukne sprog
4. Opret en promptskabelon, der hjælper modellen med effektivt at bruge dit værktøj

## Yderligere ressourcer


---

Næste: [Avancerede emner](../05-AdvancedTopics/README.md)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for eventuelle misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.