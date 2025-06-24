<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6940b1e931e51821b219aa9dcfe8c4ee",
  "translation_date": "2025-06-23T11:14:26+00:00",
  "source_file": "09-CaseStudy/README.md",
  "language_code": "tl"
}
-->
# MCP sa Aksyon: Mga Kaso ng Pag-aaral sa Totoong Mundo

Ang Model Context Protocol (MCP) ay nagbabago kung paano nakikipag-ugnayan ang mga AI application sa data, mga tool, at mga serbisyo. Ipinapakita sa seksyong ito ang mga totoong kaso ng pag-aaral na nagpapakita ng praktikal na aplikasyon ng MCP sa iba't ibang sitwasyon sa enterprise.

## Pangkalahatang-ideya

Ipinapakita ng seksyong ito ang mga kongkretong halimbawa ng mga implementasyon ng MCP, na binibigyang-diin kung paano ginagamit ng mga organisasyon ang protocol na ito upang lutasin ang mga kumplikadong hamon sa negosyo. Sa pamamagitan ng pagsusuri sa mga kasong ito, makakakuha ka ng mga pananaw tungkol sa pagiging flexible, kakayahang palawakin, at mga praktikal na benepisyo ng MCP sa mga totoong sitwasyon.

## Mga Pangunahing Layunin sa Pagkatuto

Sa pag-aaral ng mga kasong ito, matututuhan mo:

- Paano maaaring gamitin ang MCP upang lutasin ang mga tiyak na problema sa negosyo
- Mga iba't ibang pattern ng integrasyon at mga arkitekturang pamamaraan
- Mga pinakamahusay na gawain para sa pagpapatupad ng MCP sa mga enterprise na kapaligiran
- Mga hamon at solusyong naranasan sa mga totoong implementasyon
- Mga oportunidad upang gamitin ang kaparehong mga pattern sa iyong sariling mga proyekto

## Mga Tampok na Kaso ng Pag-aaral

### 1. [Azure AI Travel Agents – Reference Implementation](./travelagentsample.md)

Sinusuri ng kasong ito ang komprehensibong reference solution ng Microsoft na nagpapakita kung paano bumuo ng multi-agent, AI-powered na travel planning application gamit ang MCP, Azure OpenAI, at Azure AI Search. Ipinapakita ng proyekto ang:

- Multi-agent orchestration gamit ang MCP
- Integrasyon ng enterprise data sa Azure AI Search
- Secure at scalable na arkitektura gamit ang Azure services
- Extensible na mga tool gamit ang reusable na mga MCP components
- Conversational na karanasan ng user na pinapagana ng Azure OpenAI

Nagbibigay ang arkitektura at mga detalye ng implementasyon ng mahahalagang pananaw sa pagbuo ng mga kumplikadong multi-agent system gamit ang MCP bilang coordination layer.

### 2. [Updating Azure DevOps Items from YouTube Data](./UpdateADOItemsFromYT.md)

Ipinapakita ng kasong ito ang praktikal na aplikasyon ng MCP para sa pag-automate ng mga workflow process. Ipinapakita nito kung paano magagamit ang mga MCP tool upang:

- Kunin ang data mula sa mga online platform (YouTube)
- I-update ang mga work item sa Azure DevOps systems
- Gumawa ng mga paulit-ulit na automation workflow
- Mag-integrate ng data mula sa magkakaibang sistema

Ipinapakita ng halimbawa na ito kung paano kahit ang mga medyo simpleng implementasyon ng MCP ay maaaring magbigay ng malaking pagbuti sa kahusayan sa pamamagitan ng pag-automate ng mga rutinang gawain at pagpapahusay ng consistency ng data sa iba't ibang sistema.

### 3. [Real-Time Documentation Retrieval with MCP](./docs-mcp/README.md)

Ginagabayan ka ng kasong ito kung paano ikonekta ang isang Python console client sa Model Context Protocol (MCP) server upang kunin at i-log ang real-time, context-aware na dokumentasyon ng Microsoft. Matututuhan mo kung paano:

- Kumonekta sa isang MCP server gamit ang Python client at ang opisyal na MCP SDK
- Gumamit ng streaming HTTP clients para sa epektibo at real-time na pagkuha ng data
- Tawagan ang mga documentation tool sa server at direktang i-log ang mga sagot sa console
- Isama ang napapanahong Microsoft documentation sa iyong workflow nang hindi umaalis sa terminal

Kasama sa kabanata ang hands-on na assignment, isang minimal na working code sample, at mga link sa karagdagang mga mapagkukunan para sa mas malalim na pag-aaral. Tingnan ang buong walkthrough at code sa naka-link na kabanata upang maunawaan kung paano mababago ng MCP ang pag-access sa dokumentasyon at produktibidad ng developer sa mga console-based na kapaligiran.

### 4. [Interactive Study Plan Generator Web App with MCP](./docs-mcp/README.md)

Ipinapakita ng kasong ito kung paano bumuo ng interactive na web application gamit ang Chainlit at Model Context Protocol (MCP) upang makagawa ng personalized na study plan para sa anumang paksa. Maaaring tukuyin ng mga user ang isang subject (tulad ng "AI-900 certification") at tagal ng pag-aaral (hal., 8 linggo), at magbibigay ang app ng linggo-linggong breakdown ng mga inirekomendang nilalaman. Pinapagana ng Chainlit ang isang conversational chat interface, na ginagawang mas nakaka-engganyo at adaptable ang karanasan.

- Conversational web app na pinapagana ng Chainlit
- Mga prompt mula sa user para sa paksa at tagal
- Linggo-linggong mga rekomendasyon ng nilalaman gamit ang MCP
- Real-time at adaptive na mga tugon sa chat interface

Ipinapakita ng proyekto kung paano pinagsasama ang conversational AI at MCP upang makalikha ng mga dynamic at user-driven na mga tool pang-edukasyon sa isang modernong web environment.

### 5. [In-Editor Docs with MCP Server in VS Code](./docs-mcp/README.md)

Ipinapakita ng kasong ito kung paano mo maidaragdag ang Microsoft Learn Docs nang direkta sa iyong VS Code environment gamit ang MCP server—hindi na kailangang magpalipat-lipat ng browser tabs! Makikita mo kung paano:

- Mabilis na maghanap at magbasa ng docs sa loob ng VS Code gamit ang MCP panel o command palette
- Mag-referensya ng dokumentasyon at maglagay ng mga link nang direkta sa iyong README o course markdown files
- Pagsamahin ang GitHub Copilot at MCP para sa seamless, AI-powered na documentation at code workflows
- I-validate at pagandahin ang iyong dokumentasyon gamit ang real-time na feedback at katumpakan mula sa Microsoft
- Isama ang MCP sa GitHub workflows para sa tuloy-tuloy na validation ng dokumentasyon

Kasama sa implementasyon ang:
- Halimbawa ng `.vscode/mcp.json` configuration para sa madaling setup
- Mga screenshot-based walkthrough ng in-editor na karanasan
- Mga tip para pagsamahin ang Copilot at MCP para sa pinakamataas na produktibidad

Ang senaryong ito ay perpekto para sa mga course authors, documentation writers, at developers na nais manatiling nakatuon sa kanilang editor habang nagtatrabaho gamit ang docs, Copilot, at mga validation tool—lahat ay pinapagana ng MCP.

### 6. [APIM MCP Server Creation](./apimsample.md)

Nagbibigay ang kasong ito ng step-by-step na gabay kung paano gumawa ng MCP server gamit ang Azure API Management (APIM). Sinasaklaw nito ang:

- Pagsasaayos ng MCP server sa Azure API Management
- Pag-expose ng API operations bilang MCP tools
- Pag-configure ng mga polisiya para sa rate limiting at seguridad
- Pagsubok ng MCP server gamit ang Visual Studio Code at GitHub Copilot

Ipinapakita ng halimbawa kung paano magagamit ang kakayahan ng Azure upang makalikha ng matibay na MCP server na maaaring gamitin sa iba't ibang aplikasyon, na nagpapahusay sa integrasyon ng mga AI system sa mga enterprise API.

## Konklusyon

Ipinapakita ng mga kasong ito ang pagiging flexible at praktikal na aplikasyon ng Model Context Protocol sa mga totoong sitwasyon. Mula sa mga kumplikadong multi-agent system hanggang sa mga targeted automation workflow, nagbibigay ang MCP ng isang standardized na paraan upang ikonekta ang mga AI system sa mga tool at data na kailangan nila upang maghatid ng halaga.

Sa pag-aaral ng mga implementasyong ito, makakakuha ka ng mga pananaw sa mga pattern ng arkitektura, mga estratehiya sa pagpapatupad, at mga pinakamahusay na gawain na maaaring ilapat sa iyong sariling mga proyekto ng MCP. Ipinapakita ng mga halimbawa na ang MCP ay hindi lamang isang teoretikal na balangkas kundi isang praktikal na solusyon sa mga totoong hamon sa negosyo.

## Karagdagang mga Mapagkukunan

- [Azure AI Travel Agents GitHub Repository](https://github.com/Azure-Samples/azure-ai-travel-agents)
- [Azure DevOps MCP Tool](https://github.com/microsoft/azure-devops-mcp)
- [Playwright MCP Tool](https://github.com/microsoft/playwright-mcp)
- [Microsoft Docs MCP Server](https://github.com/MicrosoftDocs/mcp)
- [MCP Community Examples](https://github.com/microsoft/mcp)

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa kanyang orihinal na wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.