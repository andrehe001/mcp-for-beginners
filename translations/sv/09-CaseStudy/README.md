<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6940b1e931e51821b219aa9dcfe8c4ee",
  "translation_date": "2025-06-23T11:09:59+00:00",
  "source_file": "09-CaseStudy/README.md",
  "language_code": "sv"
}
-->
# MCP i praktiken: Fallstudier från verkligheten

Model Context Protocol (MCP) förändrar hur AI-applikationer interagerar med data, verktyg och tjänster. Denna sektion presenterar verkliga fallstudier som visar praktiska tillämpningar av MCP i olika företagsmiljöer.

## Översikt

Här visas konkreta exempel på MCP-implementationer, med fokus på hur organisationer använder detta protokoll för att lösa komplexa affärsutmaningar. Genom att studera dessa fallstudier får du insikter i MCP:s mångsidighet, skalbarhet och praktiska fördelar i verkliga situationer.

## Viktiga lärandemål

Genom att utforska dessa fallstudier kommer du att:

- Förstå hur MCP kan användas för att lösa specifika affärsproblem
- Lära dig om olika integrationsmönster och arkitektoniska tillvägagångssätt
- Känna igen bästa praxis för att implementera MCP i företagsmiljöer
- Få insikter i utmaningar och lösningar vid verkliga implementationer
- Identifiera möjligheter att använda liknande mönster i egna projekt

## Utvalda fallstudier

### 1. [Azure AI Travel Agents – Referensimplementation](./travelagentsample.md)

Denna fallstudie granskar Microsofts omfattande referenslösning som visar hur man bygger en multi-agent, AI-driven reseplaneringsapplikation med MCP, Azure OpenAI och Azure AI Search. Projektet visar:

- Multi-agent orkestrering via MCP
- Företagsdataintegration med Azure AI Search
- Säker och skalbar arkitektur med Azure-tjänster
- Utbyggbara verktyg med återanvändbara MCP-komponenter
- Konversationsbaserad användarupplevelse med Azure OpenAI

Arkitekturen och implementationsdetaljerna ger värdefulla insikter i att bygga komplexa multi-agent system med MCP som samordningslager.

### 2. [Uppdatera Azure DevOps-objekt från YouTube-data](./UpdateADOItemsFromYT.md)

Denna fallstudie visar en praktisk användning av MCP för att automatisera arbetsflöden. Den visar hur MCP-verktyg kan användas för att:

- Extrahera data från onlineplattformar (YouTube)
- Uppdatera arbetsobjekt i Azure DevOps-system
- Skapa upprepbara automatiseringsarbetsflöden
- Integrera data över olika system

Exemplet illustrerar hur även relativt enkla MCP-implementationer kan ge betydande effektivitet genom att automatisera rutinuppgifter och förbättra datakonsistens mellan system.

### 3. [Dokumentationshämtning i realtid med MCP](./docs-mcp/README.md)

Denna fallstudie guidar dig genom att koppla en Python-konsolklient till en MCP-server för att hämta och logga kontextmedveten Microsoft-dokumentation i realtid. Du lär dig att:

- Ansluta till en MCP-server med en Python-klient och den officiella MCP SDK:n
- Använda strömmande HTTP-klienter för effektiv realtidsdatahämtning
- Anropa dokumentationsverktyg på servern och logga svar direkt i konsolen
- Integrera uppdaterad Microsoft-dokumentation i arbetsflödet utan att lämna terminalen

Kapitel innehåller en praktisk uppgift, ett minimalt fungerande kodexempel och länkar till ytterligare resurser för fördjupad inlärning. Se hela genomgången och koden i det länkade kapitlet för att förstå hur MCP kan förändra dokumentationsåtkomst och utvecklarproduktivitet i konsolmiljöer.

### 4. [Interaktiv studieplansgenerator webapp med MCP](./docs-mcp/README.md)

Denna fallstudie visar hur man bygger en interaktiv webbapplikation med Chainlit och Model Context Protocol (MCP) för att generera personliga studieplaner för valfritt ämne. Användare kan ange ett ämne (t.ex. "AI-900-certifiering") och studietid (t.ex. 8 veckor), och appen ger en vecka-för-vecka-översikt över rekommenderat innehåll. Chainlit möjliggör en konversationsbaserad chattgränssnitt, vilket gör upplevelsen engagerande och anpassningsbar.

- Konversationsbaserad webbapp driven av Chainlit
- Användardrivna frågor för ämne och varaktighet
- Vecka-för-vecka innehållsrekommendationer med MCP
- Realtids- och adaptiva svar i chattgränssnitt

Projektet visar hur konversations-AI och MCP kan kombineras för att skapa dynamiska, användarstyrda utbildningsverktyg i en modern webbmiljö.

### 5. [Inbyggd dokumentation med MCP-server i VS Code](./docs-mcp/README.md)

Denna fallstudie visar hur du kan få Microsoft Learn Docs direkt i VS Code med hjälp av MCP-servern – inga fler flikbyten i webbläsaren! Du får se hur du kan:

- Söka och läsa dokumentation direkt i VS Code via MCP-panelen eller kommandopaletten
- Referera dokumentation och infoga länkar direkt i README- eller kursmarkdowndokument
- Använda GitHub Copilot och MCP tillsammans för sömlösa AI-drivna dokumentations- och kodarbetsflöden
- Validera och förbättra dokumentationen med realtidsfeedback och Microsoft-säkerställd korrekthet
- Integrera MCP med GitHub-arbetsflöden för kontinuerlig dokumentationsvalidering

Implementationen innehåller:
- Exempel på `.vscode/mcp.json`-konfiguration för enkel uppsättning
- Skärmdumpsbaserade genomgångar av inbyggda upplevelsen
- Tips för att kombinera Copilot och MCP för maximal produktivitet

Detta scenario är perfekt för kursförfattare, dokumentationsskrivare och utvecklare som vill hålla fokus i sin editor medan de arbetar med docs, Copilot och valideringsverktyg – allt drivet av MCP.

### 6. [Skapa MCP-server med APIM](./apimsample.md)

Denna fallstudie ger en steg-för-steg-guide för hur man skapar en MCP-server med Azure API Management (APIM). Den täcker:

- Uppsättning av MCP-server i Azure API Management
- Exponering av API-operationer som MCP-verktyg
- Konfigurering av policies för hastighetsbegränsning och säkerhet
- Testning av MCP-servern med Visual Studio Code och GitHub Copilot

Exemplet visar hur man kan utnyttja Azures kapaciteter för att skapa en robust MCP-server som kan användas i olika applikationer och förbättra integrationen av AI-system med företags-API:er.

## Slutsats

Dessa fallstudier belyser MCP:s mångsidighet och praktiska användningsområden i verkliga situationer. Från komplexa multi-agent system till riktade automatiseringsarbetsflöden erbjuder MCP ett standardiserat sätt att koppla AI-system till de verktyg och data de behöver för att skapa värde.

Genom att studera dessa implementationer kan du få insikter i arkitekturmönster, implementationsstrategier och bästa praxis som kan tillämpas i egna MCP-projekt. Exemplen visar att MCP inte bara är en teoretisk ram utan en praktisk lösning på verkliga affärsutmaningar.

## Ytterligare resurser

- [Azure AI Travel Agents GitHub Repository](https://github.com/Azure-Samples/azure-ai-travel-agents)
- [Azure DevOps MCP Tool](https://github.com/microsoft/azure-devops-mcp)
- [Playwright MCP Tool](https://github.com/microsoft/playwright-mcp)
- [Microsoft Docs MCP Server](https://github.com/MicrosoftDocs/mcp)
- [MCP Community Examples](https://github.com/microsoft/mcp)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-översättningstjänsten [Co-op Translator](https://github.com/Azure/co-op-translator). Även om vi strävar efter noggrannhet, vänligen observera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på dess modersmål ska betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för några missförstånd eller feltolkningar som uppstår vid användning av denna översättning.