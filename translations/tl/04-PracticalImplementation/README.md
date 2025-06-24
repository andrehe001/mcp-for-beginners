<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5384bbb2a92d00d5d7e66274dbe0331d",
  "translation_date": "2025-06-20T18:42:10+00:00",
  "source_file": "04-PracticalImplementation/README.md",
  "language_code": "tl"
}
-->
# Praktikal na Pagpapatupad

Ang praktikal na pagpapatupad ay kung saan nagiging konkreto ang kapangyarihan ng Model Context Protocol (MCP). Bagaman mahalaga ang pag-unawa sa teorya at arkitektura sa likod ng MCP, ang tunay na halaga nito ay lumalabas kapag inilalapat mo ang mga konseptong ito upang bumuo, subukan, at i-deploy ang mga solusyon na tumutugon sa mga totoong problema. Ang kabanatang ito ay nag-uugnay sa pagitan ng konseptwal na kaalaman at praktikal na pag-develop, na ginagabayan ka sa proseso ng paggawa ng mga aplikasyon batay sa MCP.

Kung ikaw man ay gumagawa ng mga intelligent assistant, nagsasama ng AI sa mga workflow ng negosyo, o bumubuo ng mga custom na tool para sa pagproseso ng data, nagbibigay ang MCP ng isang flexible na pundasyon. Ang disenyo nitong hindi nakadepende sa wika at mga opisyal na SDK para sa mga sikat na programming language ay ginagawang accessible ito sa malawak na hanay ng mga developer. Sa pamamagitan ng paggamit ng mga SDK na ito, maaari kang mabilis na gumawa ng prototype, mag-iterate, at mag-scale ng iyong mga solusyon sa iba't ibang platform at kapaligiran.

Sa mga sumusunod na seksyon, makikita mo ang mga praktikal na halimbawa, sample code, at mga estratehiya sa deployment na nagpapakita kung paano ipatupad ang MCP sa C#, Java, TypeScript, JavaScript, at Python. Matututuhan mo rin kung paano i-debug at subukan ang iyong mga MCP server, pamahalaan ang mga API, at i-deploy ang mga solusyon sa cloud gamit ang Azure. Ang mga hands-on na materyal na ito ay idinisenyo upang pabilisin ang iyong pagkatuto at tulungan kang tiwalaang bumuo ng matibay at production-ready na mga aplikasyon gamit ang MCP.

## Pangkalahatang-ideya

Nakatuon ang araling ito sa mga praktikal na aspeto ng pagpapatupad ng MCP sa iba't ibang programming language. Tatalakayin natin kung paano gamitin ang MCP SDKs sa C#, Java, TypeScript, JavaScript, at Python upang makabuo ng matibay na aplikasyon, mag-debug at mag-test ng MCP server, at gumawa ng mga reusable na resources, prompts, at tools.

## Mga Layunin sa Pagkatuto

Sa pagtatapos ng araling ito, magagawa mong:
- Ipatupad ang mga solusyon gamit ang MCP sa pamamagitan ng opisyal na SDK sa iba't ibang programming language
- Sistematikong i-debug at subukan ang mga MCP server
- Gumawa at gumamit ng mga server feature (Resources, Prompts, at Tools)
- Magdisenyo ng epektibong MCP workflows para sa mga komplikadong gawain
- I-optimize ang mga implementasyon ng MCP para sa performance at pagiging maaasahan

## Mga Opisyal na SDK na Mapagkukunan

Nagbibigay ang Model Context Protocol ng mga opisyal na SDK para sa iba't ibang wika:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) 
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

## Paggamit ng MCP SDKs

Nagbibigay ang seksyong ito ng mga praktikal na halimbawa ng pagpapatupad ng MCP sa iba't ibang programming language. Makikita mo ang sample code sa `samples` na direktoryo na nakaayos ayon sa wika.

### Mga Magagamit na Sample

Kasama sa repositoryo ang mga [sample implementation](../../../04-PracticalImplementation/samples) sa mga sumusunod na wika:

- [C#](./samples/csharp/README.md)
- [Java](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Ipinapakita ng bawat sample ang mga pangunahing konsepto ng MCP at mga pattern ng pagpapatupad para sa partikular na wika at ecosystem.

## Pangunahing Mga Feature ng Server

Maaaring ipatupad ng mga MCP server ang anumang kumbinasyon ng mga feature na ito:

### Resources
Nagbibigay ang Resources ng konteksto at datos para magamit ng user o AI model:
- Mga repositoryo ng dokumento
- Mga knowledge base
- Mga istrukturadong pinagmumulan ng datos
- Mga file system

### Prompts
Ang Prompts ay mga templated na mensahe at workflow para sa mga user:
- Mga paunang-gawang template ng usapan
- Mga gabay sa interaksyon
- Mga espesyal na istruktura ng dayalogo

### Tools
Ang Tools ay mga function na ipinatutupad ng AI model:
- Mga utility para sa pagproseso ng data
- Integrasyon sa mga external na API
- Mga kakayahan sa pagkalkula
- Functionality para sa paghahanap

## Mga Sample na Pagpapatupad: C#

Naglalaman ang opisyal na C# SDK repository ng ilang sample na nagpapakita ng iba't ibang aspeto ng MCP:

- **Basic MCP Client**: Simpleng halimbawa kung paano gumawa ng MCP client at tumawag ng mga tool
- **Basic MCP Server**: Minimal na pagpapatupad ng server na may basic tool registration
- **Advanced MCP Server**: Kompletong server na may tool registration, authentication, at error handling
- **ASP.NET Integration**: Mga halimbawa ng integrasyon sa ASP.NET Core
- **Tool Implementation Patterns**: Iba't ibang pattern para sa pagpapatupad ng mga tool na may iba't ibang antas ng komplikasyon

Ang MCP C# SDK ay nasa preview pa at maaaring magbago ang mga API. Patuloy naming ia-update ang blog na ito habang umuunlad ang SDK.

### Mga Pangunahing Feature 
- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)

- Paggawa ng iyong [unang MCP Server](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

Para sa kumpletong mga sample ng C# implementation, bisitahin ang [opisyal na C# SDK samples repository](https://github.com/modelcontextprotocol/csharp-sdk)

## Sample na pagpapatupad: Java Implementation

Nag-aalok ang Java SDK ng matibay na mga opsyon para sa pagpapatupad ng MCP na may enterprise-grade na mga feature.

### Mga Pangunahing Feature

- Integrasyon sa Spring Framework
- Malakas na type safety
- Suporta sa reactive programming
- Komprehensibong error handling

Para sa kumpletong Java implementation sample, tingnan ang [Java sample](samples/java/containerapp/README.md) sa samples directory.

## Sample na pagpapatupad: JavaScript Implementation

Nagbibigay ang JavaScript SDK ng magaan at flexible na paraan ng pagpapatupad ng MCP.

### Mga Pangunahing Feature

- Suporta para sa Node.js at browser
- Promise-based na API
- Madaling integrasyon sa Express at iba pang framework
- Suporta sa WebSocket para sa streaming

Para sa kumpletong JavaScript implementation sample, tingnan ang [JavaScript sample](samples/javascript/README.md) sa samples directory.

## Sample na pagpapatupad: Python Implementation

Nag-aalok ang Python SDK ng Pythonic na paraan ng pagpapatupad ng MCP na may mahusay na integrasyon sa mga ML framework.

### Mga Pangunahing Feature

- Suporta sa async/await gamit ang asyncio
- Integrasyon sa Flask at FastAPI
- Simpleng tool registration
- Native na integrasyon sa mga sikat na ML library

Para sa kumpletong Python implementation sample, tingnan ang [Python sample](samples/python/README.md) sa samples directory.

## Pamamahala ng API

Ang Azure API Management ay mahusay na solusyon para sa pag-secure ng MCP Servers. Ang ideya ay maglagay ng Azure API Management instance sa harap ng iyong MCP Server at hayaang ito ang humawak ng mga feature na malamang na kailangan mo tulad ng:

- rate limiting
- pamamahala ng token
- monitoring
- load balancing
- seguridad

### Azure Sample

Narito ang isang Azure Sample na gumagawa nito, i.e. [gumawa ng MCP Server at i-secure ito gamit ang Azure API Management](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Tingnan kung paano nangyayari ang authorization flow sa larawan sa ibaba:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true) 

Sa larawang ito, nangyayari ang mga sumusunod:

- Ginagawa ang Authentication/Authorization gamit ang Microsoft Entra.
- Gumaganap ang Azure API Management bilang gateway at gumagamit ng mga polisiya para idirekta at pamahalaan ang traffic.
- Ipinapadala ng Azure Monitor ang lahat ng request para sa karagdagang pagsusuri.

#### Authorization flow

Mas detalyadong tingnan ang authorization flow:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP authorization specification

Alamin pa ang tungkol sa [MCP Authorization specification](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization#2-10-third-party-authorization-flow)

## I-deploy ang Remote MCP Server sa Azure

Tingnan natin kung paano natin maide-deploy ang sample na nabanggit kanina:

1. I-clone ang repo

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. Magrehistro gamit ang `Microsoft.App` resource provider.
    * If you are using Azure CLI, run `az provider register --namespace Microsoft.App --wait`.
    * If you are using Azure PowerShell, run `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Then run `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` at maghintay ng ilang sandali upang suriin kung kumpleto na ang rehistrasyon.

2. Patakbuhin ang [azd](https://aka.ms/azd) command na ito para mag-provision ng api management service, function app (kasama ang code) at lahat ng iba pang kinakailangang Azure resources

    ```shell
    azd up
    ```

    Dapat ideploy ng mga command na ito ang lahat ng cloud resources sa Azure

### Pagsubok ng iyong server gamit ang MCP Inspector

1. Sa isang **bagong terminal window**, i-install at patakbuhin ang MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Makikita mo ang interface na kahalintulad nito:

    ![Connect to Node inspector](../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.tl.png) 

1. CTRL-click upang i-load ang MCP Inspector web app mula sa URL na ipinapakita ng app (halimbawa http://127.0.0.1:6274/#resources)
1. Itakda ang transport type sa `SSE`
1. Set the URL to your running API Management SSE endpoint displayed after `azd up` at **Connect**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

5. **Listahan ng Tools**. I-click ang isang tool at piliin ang **Run Tool**.

Kung nagtagumpay ang lahat ng hakbang, dapat ay nakakonekta ka na sa MCP server at nagawa mong tawagan ang isang tool.

## MCP servers para sa Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Ang set ng mga repositoryong ito ay mga quickstart template para sa paggawa at pag-deploy ng custom remote MCP (Model Context Protocol) servers gamit ang Azure Functions sa Python, C# .NET o Node/TypeScript.

Nagbibigay ang mga Sample ng kumpletong solusyon na nagpapahintulot sa mga developer na:

- Bumuo at magpatakbo nang lokal: Mag-develop at mag-debug ng MCP server sa lokal na makina
- Mag-deploy sa Azure: Madaling mag-deploy sa cloud gamit ang simpleng azd up command
- Kumonekta mula sa mga client: Kumonekta sa MCP server mula sa iba't ibang client kabilang ang VS Code's Copilot agent mode at MCP Inspector tool

### Mga Pangunahing Feature:

- Seguridad bilang disenyo: Ang MCP server ay naka-secure gamit ang mga key at HTTPS
- Mga opsyon sa authentication: Sinusuportahan ang OAuth gamit ang built-in na auth at/o API Management
- Network isolation: Pinapayagan ang network isolation gamit ang Azure Virtual Networks (VNET)
- Serverless architecture: Ginagamit ang Azure Functions para sa scalable, event-driven na pagpapatupad
- Lokal na pag-develop: Komprehensibong suporta sa lokal na pag-develop at debugging
- Simpleng deployment: Pinadaling proseso ng deployment papuntang Azure

Kasama sa repositoryo ang lahat ng kinakailangang configuration files, source code, at infrastructure definitions upang mabilis kang makapagsimula sa production-ready na implementasyon ng MCP server.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Sample na implementasyon ng MCP gamit ang Azure Functions sa Python

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Sample na implementasyon ng MCP gamit ang Azure Functions sa C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Sample na implementasyon ng MCP gamit ang Azure Functions sa Node/TypeScript.

## Mga Pangunahing Punto

- Nagbibigay ang MCP SDKs ng mga tool na partikular sa wika para sa matibay na implementasyon ng MCP solutions
- Kritikal ang proseso ng debugging at testing para sa maaasahang MCP applications
- Pinapadali ng reusable prompt templates ang consistent na AI interactions
- Ang maayos na disenyo ng workflows ay maaaring mag-orchestrate ng mga komplikadong gawain gamit ang maraming tool
- Kinakailangan ang pagsasaalang-alang sa seguridad, performance, at error handling sa pagpapatupad ng MCP solutions

## Ehersisyo

Magdisenyo ng praktikal na MCP workflow na tumutugon sa isang totoong problema sa iyong larangan:

1. Tukuyin ang 3-4 na tool na magiging kapaki-pakinabang para malutas ang problemang ito
2. Gumawa ng workflow diagram na nagpapakita kung paano nag-iinteract ang mga tool na ito
3. Ipatupad ang isang basic na bersyon ng isa sa mga tool gamit ang iyong paboritong wika
4. Gumawa ng prompt template na makakatulong sa model na epektibong magamit ang iyong tool

## Karagdagang Mapagkukunan


---

Susunod: [Advanced Topics](../05-AdvancedTopics/README.md)

**Paalala:**  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang sariling wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.