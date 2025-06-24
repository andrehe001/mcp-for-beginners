<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "36de9fae488d6de554d969fe8e0801a8",
  "translation_date": "2025-06-20T19:23:46+00:00",
  "source_file": "09-CaseStudy/apimsample.md",
  "language_code": "sw"
}
-->
# Case Study: Kufichua REST API katika API Management kama MCP server

Azure API Management, ni huduma inayotoa Gateway juu ya API Endpoints zako. Inavyofanya kazi ni kwamba Azure API Management hufanya kazi kama proxy mbele ya API zako na inaweza kuamua nini cha kufanya na maombi yanayoingia.

Kwa kuitumia, unaongeza vipengele vingi kama:

- **Usalama**, unaweza kutumia kila kitu kuanzia API keys, JWT hadi managed identity.
- **Kudhibiti idadi ya maombi**, kipengele kizuri ni uwezo wa kuamua ni maombi mangapi yanayopitishwa kwa kipindi fulani cha wakati. Hii husaidia kuhakikisha watumiaji wote wanapata uzoefu mzuri na pia huduma yako haizidiwi na maombi.
- **Kupandisha kiwango & Kusawazisha mzigo**. Unaweza kuweka idadi ya endpoints ili kusawazisha mzigo na pia unaweza kuamua jinsi ya "kusawazisha mzigo".
- **Vipengele vya AI kama semantic caching**, token limit na token monitoring na zaidi. Hivi ni vipengele bora vinavyoboresha mwitikio na pia vinakusaidia kufuatilia matumizi ya token zako. [Soma zaidi hapa](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Kwa nini MCP + Azure API Management?

Model Context Protocol inazidi kuwa kiwango cha kawaida kwa programu za agentic AI na jinsi ya kufichua zana na data kwa njia ya muendelezo. Azure API Management ni chaguo la asili unapohitaji "kusimamia" APIs. MCP Servers mara nyingi huunganishwa na APIs nyingine kutatua maombi kwa zana kwa mfano. Kwa hiyo kuunganisha Azure API Management na MCP kuna mantiki kubwa.

## Muhtasari

Katika kesi hii maalum tutajifunza jinsi ya kufichua API endpoints kama MCP Server. Kwa kufanya hivyo, tunaweza kwa urahisi kufanya endpoints hizi kuwa sehemu ya programu ya agentic huku tukitumia vipengele kutoka Azure API Management.

## Vipengele Muhimu

- Unachagua njia za endpoint unazotaka kufichua kama zana.
- Vipengele vya ziada unavyopata vinategemea kile unachokisanidi katika sehemu ya sera kwa API yako. Lakini hapa tutaonyesha jinsi ya kuongeza rate limiting.

## Hatua ya awali: ingiza API

Kama tayari una API katika Azure API Management, ni vizuri, basi unaweza kuruka hatua hii. Ikiwa huna, angalia kiungo hiki, [kuingiza API katika Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Fichua API kama MCP Server

Ili kufichua API endpoints, fuata hatua hizi:

1. Nenda kwenye Azure Portal na anwani ifuatayo <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
Nenda kwenye mfano wako wa API Management.

1. Katika menyu ya kushoto, chagua APIs > MCP Servers > + Create new MCP Server.

1. Katika API, chagua REST API kufichua kama MCP server.

1. Chagua moja au zaidi ya API Operations kufichua kama zana. Unaweza kuchagua shughuli zote au shughuli maalum tu.

    ![Chagua njia za kufichua](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. Chagua **Create**.

1. Nenda kwenye chaguo la menyu **APIs** na **MCP Servers**, utapaswa kuona yafuatayo:

    ![Tazama MCP Server kwenye dirisha kuu](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP server imeundwa na API operations zimefichuliwa kama zana. MCP server inaorodheshwa kwenye dirisha la MCP Servers. Safu ya URL inaonyesha endpoint ya MCP server ambayo unaweza kuitumia kwa majaribio au ndani ya programu ya mteja.

## Hiari: Sanidi sera

Azure API Management ina dhana kuu ya sera ambapo unaweka sheria tofauti kwa endpoints zako kama vile rate limiting au semantic caching. Sera hizi zinaandikwa kwa XML.

Hivi ndivyo unavyoweza kusanidi sera ya kudhibiti idadi ya maombi kwa MCP Server yako:

1. Katika portal, chini ya APIs, chagua **MCP Servers**.

1. Chagua MCP server uliyounda.

1. Katika menyu ya kushoto, chini ya MCP, chagua **Policies**.

1. Katika mhariri wa sera, ongeza au hariri sera unazotaka kutekeleza kwa zana za MCP server. Sera zinafafanuliwa kwa muundo wa XML. Kwa mfano, unaweza kuongeza sera ya kupunguza maombi kwa zana za MCP server (katika mfano huu, maombi 5 kwa kila sekunde 30 kwa anwani ya IP ya mteja). Hapa ni XML itakayosababisha kudhibiti idadi ya maombi:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Hii ni picha ya mhariri wa sera:

    ![Mhariri wa sera](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Jaribu

Tuhakikishe MCP Server yetu inafanya kazi kama ilivyokusudiwa.

Kwa hili, tutatumia Visual Studio Code na GitHub Copilot na hali yake ya Agent. Tutaunda MCP server kwenye *mcp.json*. Kwa kufanya hivyo, Visual Studio Code itafanya kazi kama mteja mwenye uwezo wa agentic na watumiaji wa mwisho wataweza kuandika ombi na kuingiliana na server hiyo.

Tazama jinsi ya kuongeza MCP server katika Visual Studio Code:

1. Tumia amri ya MCP: **Add Server kutoka Command Palette**.

1. Ukitaka, chagua aina ya server: **HTTP (HTTP au Server Sent Events)**.

1. Weka URL ya MCP server katika API Management. Mfano: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (kwa SSE endpoint) au **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (kwa MCP endpoint), angalia tofauti kati ya usafirishaji ni `/sse` or `/mcp`.

1. Weka kitambulisho cha server unachotaka. Hii si thamani muhimu lakini itakusaidia kukumbuka mfano huu wa server.

1. Chagua kama unataka kuhifadhi usanidi kwenye mipangilio ya workspace au mipangilio ya mtumiaji.

  - **Mipangilio ya workspace** - Usanidi wa server unaohifadhiwa kwenye faili la .vscode/mcp.json linalopatikana tu kwenye workspace ya sasa.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    au kama utachagua streaming HTTP kama usafirishaji itakuwa tofauti kidogo:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Mipangilio ya mtumiaji** - Usanidi wa server unaongezwa kwenye faili yako ya *settings.json* ya ulimwengu na upatikane katika workspaces zote. Usanidi unaonekana kama ifuatavyo:

    ![Mipangilio ya mtumiaji](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Pia unahitaji kuongeza usanidi, kichwa cha habari ili kuhakikisha inathibitishwa ipasavyo kuelekea Azure API Management. Inatumia kichwa kinachoitwa **Ocp-Apim-Subscription-Key**.

    - Hivi ndivyo unavyoweza kuiongeza kwenye mipangilio:

    ![Kuongeza kichwa cha uthibitishaji](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), hii itasababisha onyo kuonekana kukuomba thamani ya API key ambayo unaweza kuipata katika Azure Portal kwa mfano wako wa Azure API Management.

   - Ili kuiongeza kwenye *mcp.json* badala yake, unaweza kuiongeza kama ifuatavyo:

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

### Tumia hali ya Agent

Sasa tumejipanga kabisa iwe kwenye mipangilio au *.vscode/mcp.json*. Hebu tujaribu.

Kutakuwa na ikoni ya Zana kama hii, ambapo zana zilizofichuliwa kutoka kwa server yako zinaorodheshwa:

![Zana kutoka kwa server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Bonyeza ikoni ya zana na utapata orodha ya zana kama ifuatavyo:

    ![Zana](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Weka ombi kwenye mazungumzo kuitisha zana. Kwa mfano, kama umechagua zana ya kupata taarifa kuhusu agizo, unaweza kumuuliza wakala kuhusu agizo. Huu ni mfano wa ombi:

    ```text
    get information from order 2
    ```

    Sasa utaonyeshwa ikoni ya zana ikikuomba uendelee kuitisha zana. Chagua kuendelea kuendesha zana, sasa utapata matokeo kama ifuatavyo:

    ![Matokeo kutoka kwa ombi](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **kile unachoona hapo juu kinategemea zana ulizosanidi, lakini wazo ni kwamba unapata jibu la maandishi kama lilivyo hapo juu**


## Marejeleo

Hivi ndivyo unavyoweza kujifunza zaidi:

- [Mafunzo kuhusu Azure API Management na MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Mfano wa Python: Kuhifadhi MCP servers za mbali kwa usalama kwa kutumia Azure API Management (jaribio)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Maabara ya idhini ya mteja MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Tumia ugani wa Azure API Management kwa VS Code kuingiza na kusimamia APIs](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Jisajili na gundua MCP servers za mbali katika Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Hifadhi nzuri inayonyesha uwezo mwingi wa AI kwa Azure API Management
- [Warsha za AI Gateway](https://azure-samples.github.io/AI-Gateway/) Zina warsha zinazotumia Azure Portal, njia nzuri ya kuanza kutathmini uwezo wa AI.

**Kiarifu cha Kutokujali**:  
Nyaraka hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuhakikisha usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upotovu wa taarifa. Nyaraka ya asili katika lugha yake ya mama inapaswa kuchukuliwa kama chanzo halali. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatubeba dhamana kwa maelewano au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.