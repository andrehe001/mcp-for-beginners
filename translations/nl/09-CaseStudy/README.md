<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6940b1e931e51821b219aa9dcfe8c4ee",
  "translation_date": "2025-06-23T11:12:00+00:00",
  "source_file": "09-CaseStudy/README.md",
  "language_code": "nl"
}
-->
# MCP in Actie: Praktijkvoorbeelden

Het Model Context Protocol (MCP) verandert de manier waarop AI-toepassingen omgaan met data, tools en diensten. In deze sectie worden praktijkvoorbeelden gepresenteerd die laten zien hoe MCP wordt toegepast in verschillende bedrijfsomgevingen.

## Overzicht

Deze sectie toont concrete voorbeelden van MCP-implementaties en benadrukt hoe organisaties dit protocol gebruiken om complexe zakelijke uitdagingen aan te pakken. Door deze casestudies te bekijken, krijg je inzicht in de veelzijdigheid, schaalbaarheid en praktische voordelen van MCP in de praktijk.

## Belangrijkste Leerdoelen

Door deze casestudies te verkennen, zul je:

- Begrijpen hoe MCP kan worden ingezet om specifieke zakelijke problemen op te lossen  
- Kennismaken met verschillende integratiepatronen en architecturale benaderingen  
- Best practices herkennen voor het implementeren van MCP in bedrijfsomgevingen  
- Inzicht krijgen in de uitdagingen en oplossingen die bij echte implementaties zijn opgedaan  
- Kansen ontdekken om vergelijkbare patronen in je eigen projecten toe te passen  

## Uitgelichte Casestudies

### 1. [Azure AI Travel Agents – Referentie-implementatie](./travelagentsample.md)

Deze casestudy onderzoekt Microsofts uitgebreide referentieoplossing die laat zien hoe je een multi-agent, AI-gestuurde reisplanningsapplicatie bouwt met MCP, Azure OpenAI en Azure AI Search. Het project laat zien:

- Multi-agent orchestratie via MCP  
- Integratie van bedrijfsdata met Azure AI Search  
- Veilige, schaalbare architectuur met Azure-diensten  
- Uitbreidbare tooling met herbruikbare MCP-componenten  
- Conversational user experience aangedreven door Azure OpenAI  

De architectuur en implementatiedetails bieden waardevolle inzichten in het bouwen van complexe multi-agent systemen met MCP als coördinatielaag.

### 2. [Azure DevOps-items bijwerken met YouTube-gegevens](./UpdateADOItemsFromYT.md)

Deze casestudy toont een praktische toepassing van MCP voor het automatiseren van workflowprocessen. Het laat zien hoe MCP-tools kunnen worden gebruikt om:

- Gegevens van online platforms (YouTube) te extraheren  
- Werkitems in Azure DevOps-systemen bij te werken  
- Herhaalbare automatiseringsworkflows te creëren  
- Data te integreren over verschillende systemen heen  

Dit voorbeeld illustreert hoe zelfs relatief eenvoudige MCP-implementaties aanzienlijke efficiëntiewinst kunnen opleveren door routinetaken te automatiseren en de dataconsistentie te verbeteren.

### 3. [Realtime documentatie ophalen met MCP](./docs-mcp/README.md)

Deze casestudy begeleidt je bij het verbinden van een Python consoleclient met een Model Context Protocol (MCP) server om realtime, contextbewuste Microsoft-documentatie op te halen en te loggen. Je leert hoe je:

- Verbindt met een MCP-server via een Python client en de officiële MCP SDK  
- Streaming HTTP-clients gebruikt voor efficiënte, realtime dataopvraging  
- Documentatietools op de server aanroept en reacties direct naar de console logt  
- Up-to-date Microsoft-documentatie integreert in je workflow zonder de terminal te verlaten  

Het hoofdstuk bevat een praktische opdracht, een minimale werkende codevoorbeeld en links naar aanvullende bronnen voor verdieping. Bekijk de volledige walkthrough en code in het gekoppelde hoofdstuk om te begrijpen hoe MCP de toegang tot documentatie en de productiviteit van ontwikkelaars in console-omgevingen kan transformeren.

### 4. [Interactieve studieplangenerator webapp met MCP](./docs-mcp/README.md)

Deze casestudy laat zien hoe je een interactieve webapp bouwt met Chainlit en het Model Context Protocol (MCP) om gepersonaliseerde studieplannen te genereren voor elk onderwerp. Gebruikers kunnen een onderwerp opgeven (zoals "AI-900 certificering") en een studietijd (bijvoorbeeld 8 weken), waarna de app een week-tot-week overzicht geeft van aanbevolen content. Chainlit zorgt voor een conversatiegerichte chatinterface, wat de ervaring boeiend en adaptief maakt.

- Conversational webapp aangedreven door Chainlit  
- Gebruikersgestuurde prompts voor onderwerp en duur  
- Week-tot-week contentaanbevelingen met MCP  
- Realtime, adaptieve reacties in een chatinterface  

Het project laat zien hoe conversational AI en MCP gecombineerd kunnen worden om dynamische, gebruikersgestuurde educatieve tools te maken in een moderne webomgeving.

### 5. [In-Editor Docs met MCP Server in VS Code](./docs-mcp/README.md)

Deze casestudy laat zien hoe je Microsoft Learn Docs direct in je VS Code-omgeving haalt met de MCP-server—geen gedoe meer met browser tabs! Je ziet hoe je:

- Direct docs zoekt en leest binnen VS Code via het MCP-paneel of de commandopalet  
- Documentatie refereert en links invoegt in je README of cursus markdown-bestanden  
- GitHub Copilot en MCP samen gebruikt voor naadloze, AI-gestuurde documentatie- en codeworkflows  
- Je documentatie valideert en verbetert met realtime feedback en Microsoft-accuratesse  
- MCP integreert met GitHub-workflows voor continue documentatievalidatie  

De implementatie bevat:  
- Voorbeeld `.vscode/mcp.json` configuratie voor eenvoudige setup  
- Screenshot-gebaseerde walkthroughs van de in-editor ervaring  
- Tips om Copilot en MCP te combineren voor maximale productiviteit  

Dit scenario is ideaal voor cursusmakers, documentatieschrijvers en ontwikkelaars die gefocust willen blijven in hun editor terwijl ze werken met docs, Copilot en validatietools—alles aangedreven door MCP.

### 6. [APIM MCP Server Creatie](./apimsample.md)

Deze casestudy geeft een stapsgewijze handleiding voor het maken van een MCP-server met Azure API Management (APIM). Het behandelt:  
- Het opzetten van een MCP-server in Azure API Management  
- API-operaties blootstellen als MCP-tools  
- Policies configureren voor rate limiting en beveiliging  
- De MCP-server testen met Visual Studio Code en GitHub Copilot  

Dit voorbeeld laat zien hoe je de mogelijkheden van Azure benut om een robuuste MCP-server te creëren die in diverse toepassingen kan worden ingezet, waardoor de integratie van AI-systemen met enterprise-API's wordt verbeterd.

## Conclusie

Deze casestudies benadrukken de veelzijdigheid en praktische toepassingen van het Model Context Protocol in de praktijk. Van complexe multi-agent systemen tot gerichte automatiseringsworkflows, MCP biedt een gestandaardiseerde manier om AI-systemen te verbinden met de tools en data die ze nodig hebben om waarde te leveren.

Door deze implementaties te bestuderen, krijg je inzicht in architecturale patronen, implementatiestrategieën en best practices die je kunt toepassen in je eigen MCP-projecten. De voorbeelden tonen aan dat MCP niet slechts een theoretisch kader is, maar een praktische oplossing voor echte zakelijke uitdagingen.

## Aanvullende Bronnen

- [Azure AI Travel Agents GitHub Repository](https://github.com/Azure-Samples/azure-ai-travel-agents)  
- [Azure DevOps MCP Tool](https://github.com/microsoft/azure-devops-mcp)  
- [Playwright MCP Tool](https://github.com/microsoft/playwright-mcp)  
- [Microsoft Docs MCP Server](https://github.com/MicrosoftDocs/mcp)  
- [MCP Community Examples](https://github.com/microsoft/mcp)

**Disclaimer**:  
Dit document is vertaald met behulp van de AI-vertalingsservice [Co-op Translator](https://github.com/Azure/co-op-translator). Hoewel we streven naar nauwkeurigheid, dient u er rekening mee te houden dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet als de gezaghebbende bron worden beschouwd. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor eventuele misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.