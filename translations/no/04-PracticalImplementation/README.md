<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5384bbb2a92d00d5d7e66274dbe0331d",
  "translation_date": "2025-06-20T18:37:53+00:00",
  "source_file": "04-PracticalImplementation/README.md",
  "language_code": "no"
}
-->
# Praktisk implementering

Praktisk implementering er der hvor kraften i Model Context Protocol (MCP) blir håndgripelig. Selv om det er viktig å forstå teorien og arkitekturen bak MCP, oppstår den virkelige verdien når du anvender disse konseptene for å bygge, teste og distribuere løsninger som løser reelle problemer. Dette kapittelet bygger bro mellom konseptuell kunnskap og praktisk utvikling, og veileder deg gjennom prosessen med å realisere MCP-baserte applikasjoner.

Enten du utvikler intelligente assistenter, integrerer AI i forretningsprosesser, eller bygger skreddersydde verktøy for databehandling, gir MCP et fleksibelt grunnlag. Dens språkagnostiske design og offisielle SDK-er for populære programmeringsspråk gjør det tilgjengelig for et bredt spekter av utviklere. Ved å utnytte disse SDK-ene kan du raskt lage prototyper, iterere og skalere løsningene dine på tvers av ulike plattformer og miljøer.

I de følgende seksjonene finner du praktiske eksempler, eksempel-kode og distribusjonsstrategier som viser hvordan du implementerer MCP i C#, Java, TypeScript, JavaScript og Python. Du vil også lære hvordan du feilsøker og tester MCP-servere, administrerer API-er, og distribuerer løsninger til skyen ved hjelp av Azure. Disse praktiske ressursene er laget for å akselerere læringen din og hjelpe deg å bygge robuste, produksjonsklare MCP-applikasjoner med selvtillit.

## Oversikt

Denne leksjonen fokuserer på praktiske aspekter ved MCP-implementering på tvers av flere programmeringsspråk. Vi skal utforske hvordan man bruker MCP SDK-er i C#, Java, TypeScript, JavaScript og Python for å bygge robuste applikasjoner, feilsøke og teste MCP-servere, og lage gjenbrukbare ressurser, prompts og verktøy.

## Læringsmål

Etter denne leksjonen skal du kunne:
- Implementere MCP-løsninger ved hjelp av offisielle SDK-er i ulike programmeringsspråk
- Feilsøke og teste MCP-servere systematisk
- Opprette og bruke serverfunksjoner (Ressurser, Prompts og Verktøy)
- Designe effektive MCP-arbeidsflyter for komplekse oppgaver
- Optimalisere MCP-implementeringer for ytelse og pålitelighet

## Offisielle SDK-ressurser

Model Context Protocol tilbyr offisielle SDK-er for flere språk:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) 
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

## Arbeide med MCP SDK-er

Denne seksjonen gir praktiske eksempler på implementering av MCP på tvers av flere programmeringsspråk. Du finner eksempel-kode i `samples`-mappen organisert etter språk.

### Tilgjengelige eksempler

Repositoryet inkluderer [eksempelimplementeringer](../../../04-PracticalImplementation/samples) i følgende språk:

- [C#](./samples/csharp/README.md)
- [Java](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Hvert eksempel viser sentrale MCP-konsepter og implementeringsmønstre for det spesifikke språket og økosystemet.

## Kjernefunksjoner på serveren

MCP-servere kan implementere en hvilken som helst kombinasjon av disse funksjonene:

### Ressurser
Ressurser gir kontekst og data som brukeren eller AI-modellen kan bruke:
- Dokumentarkiver
- Kunnskapsbaser
- Strukturerte datakilder
- Filsystemer

### Prompts
Prompts er malbaserte meldinger og arbeidsflyter for brukere:
- Ferdigdefinerte samtalemaler
- Veiledede interaksjonsmønstre
- Spesialiserte dialogstrukturer

### Verktøy
Verktøy er funksjoner som AI-modellen kan utføre:
- Verktøy for databehandling
- Integrasjoner med eksterne API-er
- Beregningskapasiteter
- Søke-funksjonalitet

## Eksempelimplementeringer: C#

Det offisielle C# SDK-repositoryet inneholder flere eksempelimplementeringer som demonstrerer ulike aspekter ved MCP:

- **Basic MCP Client**: Enkelt eksempel som viser hvordan man oppretter en MCP-klient og kaller verktøy
- **Basic MCP Server**: Minimal serverimplementering med grunnleggende verktøyregistrering
- **Advanced MCP Server**: Fullverdig server med verktøyregistrering, autentisering og feilhåndtering
- **ASP.NET-integrasjon**: Eksempler som viser integrasjon med ASP.NET Core
- **Verktøysimplementeringsmønstre**: Ulike mønstre for implementering av verktøy med varierende kompleksitet

MCP C# SDK er i forhåndsvisning, og API-er kan endres. Vi vil kontinuerlig oppdatere denne bloggen etter hvert som SDK-en utvikler seg.

### Nøkkelfunksjoner 
- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)

- Bygg din [første MCP Server](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

For komplette C# implementeringseksempler, besøk det [offisielle C# SDK-eksempelsrepositoryet](https://github.com/modelcontextprotocol/csharp-sdk)

## Eksempelimplementering: Java-implementering

Java SDK tilbyr robuste MCP-implementeringsmuligheter med bedriftsnivåfunksjoner.

### Nøkkelfunksjoner

- Integrasjon med Spring Framework
- Sterk typesikkerhet
- Støtte for reaktiv programmering
- Omfattende feilhåndtering

For et komplett Java-implementeringseksempel, se [Java-eksempel](samples/java/containerapp/README.md) i eksempelmappen.

## Eksempelimplementering: JavaScript-implementering

JavaScript SDK gir en lettvekts og fleksibel tilnærming til MCP-implementering.

### Nøkkelfunksjoner

- Støtte for Node.js og nettleser
- Promise-basert API
- Enkel integrasjon med Express og andre rammeverk
- WebSocket-støtte for streaming

For et komplett JavaScript-implementeringseksempel, se [JavaScript-eksempel](samples/javascript/README.md) i eksempelmappen.

## Eksempelimplementering: Python-implementering

Python SDK tilbyr en pythonisk tilnærming til MCP-implementering med utmerket integrasjon mot ML-rammeverk.

### Nøkkelfunksjoner

- Async/await-støtte med asyncio
- Integrasjon med Flask og FastAPI
- Enkel verktøyregistrering
- Naturlig integrasjon med populære ML-biblioteker

For et komplett Python-implementeringseksempel, se [Python-eksempel](samples/python/README.md) i eksempelmappen.

## API-administrasjon

Azure API Management er en god løsning for hvordan vi kan sikre MCP-servere. Ideen er å plassere en Azure API Management-instans foran MCP-serveren din og la den håndtere funksjoner du sannsynligvis ønsker, som:

- ratebegrensning
- tokenhåndtering
- overvåking
- lastbalansering
- sikkerhet

### Azure-eksempel

Her er et Azure-eksempel som gjør nettopp dette, altså [oppretter en MCP-server og sikrer den med Azure API Management](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Se hvordan autorisasjonsflyten skjer i bildet nedenfor:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true) 

I bildet over skjer følgende:

- Autentisering/autorisasjon skjer via Microsoft Entra.
- Azure API Management fungerer som en gateway og bruker policyer for å styre og administrere trafikk.
- Azure Monitor logger alle forespørsler for videre analyse.

#### Autorisasjonsflyt

La oss se nærmere på autorisasjonsflyten:

![Sekvensdiagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP autorisasjonsspesifikasjon

Lær mer om [MCP Authorization specification](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization#2-10-third-party-authorization-flow)

## Distribuer fjern-MCP-server til Azure

La oss se om vi kan distribuere eksemplet vi nevnte tidligere:

1. Klon repoet

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

2. Registrer `Microsoft.App` resource provider.
    * If you are using Azure CLI, run `az provider register --namespace Microsoft.App --wait`.
    * If you are using Azure PowerShell, run `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Then run `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` og vent litt før du sjekker om registreringen er fullført.

3. Kjør denne [azd](https://aka.ms/azd)-kommandoen for å provisionere API Management-tjenesten, funksjonsappen (med kode) og alle andre nødvendige Azure-ressurser

    ```shell
    azd up
    ```

    Denne kommandoen skal distribuere alle skyressursene på Azure

### Test serveren din med MCP Inspector

1. I et **nytt terminalvindu**, installer og kjør MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Du skal se et grensesnitt som ligner på:

    ![Koble til Node inspector](../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.no.png) 

2. CTRL-klikk for å åpne MCP Inspector webappen fra URL-en som vises i appen (f.eks. http://127.0.0.1:6274/#resources)
3. Sett transporttypen til `SSE`
1. Set the URL to your running API Management SSE endpoint displayed after `azd up` og **Koble til**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

5. **List verktøy**. Klikk på et verktøy og **Kjør verktøy**.  

Hvis alle trinnene har fungert, skal du nå være koblet til MCP-serveren og ha klart å kalle et verktøy.

## MCP-servere for Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Dette settet med repositories er en hurtigstartmal for å bygge og distribuere tilpassede fjern-MCP (Model Context Protocol) servere ved bruk av Azure Functions med Python, C# .NET eller Node/TypeScript.

Eksemplene gir en komplett løsning som lar utviklere:

- Bygge og kjøre lokalt: Utvikle og feilsøke en MCP-server på en lokal maskin
- Distribuere til Azure: Enkel distribusjon til skyen med en enkel azd up-kommando
- Koble til fra klienter: Koble til MCP-serveren fra ulike klienter, inkludert VS Codes Copilot agent-modus og MCP Inspector-verktøyet

### Nøkkelfunksjoner:

- Sikkerhet by design: MCP-serveren sikres ved bruk av nøkler og HTTPS
- Autentiseringsmuligheter: Støtter OAuth med innebygd autentisering og/eller API Management
- Nettverksisolasjon: Mulighet for nettverksisolasjon ved bruk av Azure Virtual Networks (VNET)
- Serverløs arkitektur: Utnytter Azure Functions for skalerbar, hendelsesdrevet kjøring
- Lokal utvikling: Omfattende støtte for lokal utvikling og feilsøking
- Enkel distribusjon: Strømlinjeformet distribusjonsprosess til Azure

Repositoryet inneholder alle nødvendige konfigurasjonsfiler, kildekode og infrastrukturdefinisjoner for raskt å komme i gang med en produksjonsklar MCP-serverimplementering.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Eksempelimplementering av MCP med Azure Functions i Python

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Eksempelimplementering av MCP med Azure Functions i C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Eksempelimplementering av MCP med Azure Functions i Node/TypeScript.

## Viktige punkter

- MCP SDK-er gir språkspesifikke verktøy for å implementere robuste MCP-løsninger
- Feilsøkings- og testprosessen er avgjørende for pålitelige MCP-applikasjoner
- Gjenbrukbare prompt-maler muliggjør konsistente AI-interaksjoner
- Godt designede arbeidsflyter kan orkestrere komplekse oppgaver ved bruk av flere verktøy
- Implementering av MCP-løsninger krever hensyn til sikkerhet, ytelse og feilhåndtering

## Øvelse

Design en praktisk MCP-arbeidsflyt som løser et reelt problem innen ditt område:

1. Identifiser 3-4 verktøy som ville være nyttige for å løse dette problemet
2. Lag et arbeidsflytdiagram som viser hvordan disse verktøyene samhandler
3. Implementer en grunnleggende versjon av ett av verktøyene i ditt foretrukne språk
4. Lag en prompt-mal som hjelper modellen med å bruke verktøyet ditt effektivt

## Tilleggsressurser


---

Neste: [Avanserte emner](../05-AdvancedTopics/README.md)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av AI-oversettelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det opprinnelige dokumentet på originalspråket skal anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.