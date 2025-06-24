<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6940b1e931e51821b219aa9dcfe8c4ee",
  "translation_date": "2025-06-23T11:10:31+00:00",
  "source_file": "09-CaseStudy/README.md",
  "language_code": "da"
}
-->
# MCP i praksis: Virkelige case-studier

Model Context Protocol (MCP) ændrer måden, AI-applikationer interagerer med data, værktøjer og tjenester på. Denne sektion præsenterer virkelige case-studier, der demonstrerer praktiske anvendelser af MCP i forskellige virksomhedsscenarier.

## Oversigt

Denne sektion viser konkrete eksempler på MCP-implementeringer og fremhæver, hvordan organisationer udnytter denne protokol til at løse komplekse forretningsudfordringer. Ved at gennemgå disse case-studier får du indsigt i MCP’s alsidighed, skalerbarhed og praktiske fordele i virkelige situationer.

## Centrale læringsmål

Ved at udforske disse case-studier vil du:

- Forstå, hvordan MCP kan anvendes til at løse specifikke forretningsproblemer
- Lære om forskellige integrationsmønstre og arkitektoniske tilgange
- Genkende bedste praksis for implementering af MCP i virksomheds-miljøer
- Få indsigt i udfordringer og løsninger, der opstår i virkelige implementeringer
- Identificere muligheder for at anvende lignende mønstre i dine egne projekter

## Udvalgte case-studier

### 1. [Azure AI Travel Agents – Reference Implementation](./travelagentsample.md)

Dette case-studie undersøger Microsofts omfattende referencesystem, som viser, hvordan man bygger en multi-agent, AI-drevet rejseplanlægningsapplikation ved hjælp af MCP, Azure OpenAI og Azure AI Search. Projektet fremviser:

- Multi-agent orkestrering via MCP
- Enterprise data-integration med Azure AI Search
- Sikker og skalerbar arkitektur ved brug af Azure-tjenester
- Udvideligt værktøjssæt med genanvendelige MCP-komponenter
- Konverserende brugeroplevelse drevet af Azure OpenAI

Arkitektur- og implementeringsdetaljerne giver værdifuld indsigt i at bygge komplekse multi-agent systemer med MCP som koordinationslag.

### 2. [Opdatering af Azure DevOps-elementer fra YouTube-data](./UpdateADOItemsFromYT.md)

Dette case-studie viser en praktisk anvendelse af MCP til automatisering af arbejdsprocesser. Det demonstrerer, hvordan MCP-værktøjer kan bruges til at:

- Udtrække data fra online platforme (YouTube)
- Opdatere arbejdsopgaver i Azure DevOps-systemer
- Oprette gentagelige automatiserings-workflows
- Integrere data på tværs af forskellige systemer

Dette eksempel illustrerer, hvordan selv relativt simple MCP-implementeringer kan give betydelige effektivitetsgevinster ved at automatisere rutineopgaver og forbedre datakonsistens på tværs af systemer.

### 3. [Real-time dokumenthentning med MCP](./docs-mcp/README.md)

Dette case-studie guider dig gennem, hvordan du forbinder en Python-konsolklient til en Model Context Protocol (MCP) server for at hente og logge Microsoft-dokumentation i realtid, der er kontekstbevidst. Du lærer at:

- Forbinde til en MCP-server med en Python-klient og den officielle MCP SDK
- Bruge streaming HTTP-klienter til effektiv, realtids datahentning
- Kalde dokumentationsværktøjer på serveren og logge svar direkte til konsollen
- Integrere opdateret Microsoft-dokumentation i din arbejdsproces uden at forlade terminalen

Kapitel inkluderer en praktisk opgave, et minimalt fungerende kodeeksempel og links til yderligere ressourcer for dybere læring. Se den fulde gennemgang og kode i det linkede kapitel for at forstå, hvordan MCP kan forvandle dokumentationsadgang og udviklerproduktivitet i konsolbaserede miljøer.

### 4. [Interaktiv studieplan-generator webapp med MCP](./docs-mcp/README.md)

Dette case-studie viser, hvordan man bygger en interaktiv webapplikation ved hjælp af Chainlit og Model Context Protocol (MCP) til at generere personlige studieplaner for ethvert emne. Brugere kan angive et fag (f.eks. "AI-900 certificering") og en studietid (f.eks. 8 uger), hvorefter appen giver en uge-for-uge oversigt over anbefalet indhold. Chainlit muliggør en konverserende chatgrænseflade, der gør oplevelsen engagerende og tilpasningsdygtig.

- Konverserende webapp drevet af Chainlit
- Brugerstyrede input for emne og varighed
- Uge-for-uge indholds-anbefalinger ved hjælp af MCP
- Realtids, adaptive svar i chatgrænsefladen

Projektet illustrerer, hvordan konverserende AI og MCP kan kombineres for at skabe dynamiske, brugerstyrede undervisningsværktøjer i et moderne webmiljø.

### 5. [In-Editor Docs med MCP-server i VS Code](./docs-mcp/README.md)

Dette case-studie viser, hvordan du kan bringe Microsoft Learn Docs direkte ind i dit VS Code-miljø ved hjælp af MCP-serveren – ingen grund til at skifte browserfaner! Du får indsigt i, hvordan du kan:

- Søge og læse dokumentation øjeblikkeligt inde i VS Code via MCP-panelet eller kommandopaletten
- Referere til dokumentation og indsætte links direkte i dine README- eller kursus-markdownfiler
- Bruge GitHub Copilot og MCP sammen for en problemfri, AI-drevet dokumentations- og kodeworkflow
- Validere og forbedre din dokumentation med realtids-feedback og Microsoft-sikret nøjagtighed
- Integrere MCP med GitHub-workflows til kontinuerlig dokumentationsvalidering

Implementeringen inkluderer:
- Eksempel på `.vscode/mcp.json` konfiguration for nem opsætning
- Skærmbilledebaserede gennemgange af in-editor oplevelsen
- Tips til at kombinere Copilot og MCP for maksimal produktivitet

Dette scenarie er ideelt for kursusforfattere, dokumentationsskrivere og udviklere, der ønsker at holde fokus i deres editor, mens de arbejder med docs, Copilot og valideringsværktøjer – alt sammen drevet af MCP.

### 6. [Oprettelse af APIM MCP-server](./apimsample.md)

Dette case-studie giver en trin-for-trin guide til, hvordan man opretter en MCP-server ved hjælp af Azure API Management (APIM). Det dækker:

- Opsætning af en MCP-server i Azure API Management
- Eksponering af API-operationer som MCP-værktøjer
- Konfiguration af politikker for ratebegrænsning og sikkerhed
- Test af MCP-serveren med Visual Studio Code og GitHub Copilot

Dette eksempel viser, hvordan man udnytter Azures muligheder til at skabe en robust MCP-server, som kan bruges i forskellige applikationer og forbedre integrationen af AI-systemer med virksomheds-API’er.

## Konklusion

Disse case-studier fremhæver Model Context Protocols alsidighed og praktiske anvendelser i virkelige scenarier. Fra komplekse multi-agent systemer til målrettede automatiserings-workflows tilbyder MCP en standardiseret måde at forbinde AI-systemer med de værktøjer og data, de har brug for for at skabe værdi.

Ved at studere disse implementeringer kan du få indsigt i arkitekturmønstre, implementeringsstrategier og bedste praksis, som du kan anvende i dine egne MCP-projekter. Eksemplerne viser, at MCP ikke blot er en teoretisk ramme, men en praktisk løsning på reelle forretningsudfordringer.

## Yderligere ressourcer

- [Azure AI Travel Agents GitHub Repository](https://github.com/Azure-Samples/azure-ai-travel-agents)
- [Azure DevOps MCP Tool](https://github.com/microsoft/azure-devops-mcp)
- [Playwright MCP Tool](https://github.com/microsoft/playwright-mcp)
- [Microsoft Docs MCP Server](https://github.com/MicrosoftDocs/mcp)
- [MCP Community Examples](https://github.com/microsoft/mcp)

**Ansvarsfraskrivelse**:  
Dette dokument er oversat ved hjælp af AI-oversættelsestjenesten [Co-op Translator](https://github.com/Azure/co-op-translator). Selvom vi bestræber os på nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det oprindelige dokument på dets modersmål bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.