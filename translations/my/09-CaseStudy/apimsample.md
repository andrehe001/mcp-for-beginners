<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "36de9fae488d6de554d969fe8e0801a8",
  "translation_date": "2025-06-20T19:26:49+00:00",
  "source_file": "09-CaseStudy/apimsample.md",
  "language_code": "my"
}
-->
# Case Study: Expose REST API in API Management as an MCP server

Azure API Management သည် သင့် API Endpoints များအပေါ်တွင် Gateway တစ်ခုကို ပေးသည့် ဝန်ဆောင်မှုဖြစ်သည်။ ၎င်းသည် သင့် API များရှေ့တွင် proxy အဖြစ် လုပ်ဆောင်ပြီး ဝင်ရောက်လာသော တောင်းဆိုမှုများကို ဘာလုပ်ဆောင်မည်ကို ဆုံးဖြတ်ပေးသည်။

ဒါကို အသုံးပြုခြင်းအားဖြင့် အောက်ပါ လုပ်ဆောင်ချက်များစွာကို ထည့်သွင်းနိုင်သည်-

- **လုံခြုံရေး**, API key များ၊ JWT နှင့် managed identity အပါအဝင် အရာအားလုံးကို အသုံးပြုနိုင်သည်။
- **ခွင့်ပြုချက် ကန့်သတ်ခြင်း**, တစ်ချိန်ကာလအတွင်း ဘယ်နှစ်ခေါ်ဆိုမှုများကို ခွင့်ပြုမည်ကို ဆုံးဖြတ်နိုင်ခြင်းသည် အသုံးပြုသူများအား အကောင်းဆုံးအတွေ့အကြုံ ပေးနိုင်ပြီး ဝန်ဆောင်မှုအား တောင်းဆိုမှုများကြောင့် မလွန်ပြည့်စုံမှုမရှိစေရန် ကူညီပေးသည်။
- **တိုးချဲ့ခြင်းနှင့် လုပ်ငန်းတင်ချိန်ချိန်ညှိခြင်း**။ လုပ်ငန်းတင်ချိန်ချိန်ညှိရန် အများအပြား endpoint များကို သတ်မှတ်နိုင်ပြီး "load balance" မည်သို့လုပ်မည်ကိုလည်း ဆုံးဖြတ်နိုင်သည်။
- **AI အင်္ဂါရပ်များဖြစ်သည့် semantic caching, token limit, token monitoring နှင့် အခြားများ**။ ၎င်းတို့သည် တုံ့ပြန်မှုမြန်ဆန်မှုကို တိုးတက်စေပြီး token အသုံးစရိတ်ကို ထိန်းချုပ်နိုင်ရန် ကူညီပေးသည်။ [ဒီမှာ ပိုမိုဖတ်ရှုပါ](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities)။

## Why MCP + Azure API Management?

Model Context Protocol သည် agentic AI apps များအတွက် စံသတ်မှတ်ချက်တစ်ခုဖြစ်လာပြီး tools နှင့် data များကို တစ်ပြိုင်နက်တည်း ဖော်ပြပေးနိုင်ရန် အသုံးပြုသည်။ API များကို "စီမံခန့်ခွဲရန်" လိုအပ်သောအခါ Azure API Management သည် သဘာဝအတိုင်းရွေးချယ်မှုဖြစ်သည်။ MCP Servers များသည် တောင်းဆိုမှုများကို tool တစ်ခုသို့ ဖြေရှင်းရန် အခြား API များနှင့် ပေါင်းစည်းပြီး အသုံးပြုသည်။ ထို့ကြောင့် Azure API Management နှင့် MCP ကို ပေါင်းစပ်အသုံးပြုခြင်းမှာ အလွန်သင့်တော်သည်။

## Overview

ဒီအထူးသဖြင့် API endpoints များကို MCP Server အဖြစ် ဖော်ပြပေးရန် သင်ယူမည်ဖြစ်သည်။ ၎င်းအားဖြင့် agentic app အတွက် endpoints များကို လွယ်ကူစွာ ပေါင်းစပ်နိုင်ပြီး Azure API Management ၏ လုပ်ဆောင်ချက်များကိုလည်း အသုံးချနိုင်မည်ဖြစ်သည်။

## Key Features

- သင့်လိုချင်သည့် endpoint method များကို tools အဖြစ် ရွေးချယ်နိုင်သည်။
- သင့် API ၏ policy အပိုင်းတွင် သတ်မှတ်ထားသည့်အတိုင်း အပိုလုပ်ဆောင်ချက်များ ရရှိမည်ဖြစ်သည်။ ဒီမှာတော့ rate limiting ကို ထည့်သွင်းပုံကို ပြသမည်။

## Pre-step: import an API

သင်မှာ Azure API Management ထဲတွင် API ရှိပြီးသားဖြစ်ပါက ဒီအဆင့်ကို ကျော်လွှားနိုင်သည်။ မရှိပါက ဒီလင့်ခ်ကို ကြည့်ပါ၊ [importing an API to Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api)။

## Expose API as MCP Server

API endpoints များကို ဖော်ပြရန် အောက်ပါ အဆင့်များကို လိုက်နာပါ-

1. Azure Portal သို့ ဝင်၍ <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> သို့ သွားပါ။ သင့် API Management instance ကို ရွေးချယ်ပါ။

1. ဘယ်ဘက် menu တွင် APIs > MCP Servers > + Create new MCP Server ကို ရွေးချယ်ပါ။

1. API တွင် MCP server အဖြစ် ဖော်ပြလိုသော REST API ကို ရွေးချယ်ပါ။

1. Tools အဖြစ် ဖော်ပြလိုသော API Operations တစ်ခု သို့မဟုတ် အများကြီးကို ရွေးချယ်ပါ။ များအားလုံး သို့မဟုတ် သတ်မှတ်ထားသော operation များကိုသာ ရွေးချယ်နိုင်သည်။

    ![Select methods to expose](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)


1. **Create** ကို နှိပ်ပါ။

1. Menu options တွင် **APIs** နှင့် **MCP Servers** သို့ သွားပါ၊ အောက်ပါအတိုင်း မြင်ရမည်-

    ![See the MCP Server in the main pane](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP server သည် ဖန်တီးပြီး API operations များကို tools အဖြစ် ဖော်ပြထားသည်။ MCP server သည် MCP Servers panel တွင် စာရင်းပြုစုထားသည်။ URL ကော်လံတွင် MCP server ၏ endpoint ကို ဖော်ပြထားပြီး စမ်းသပ်ရန် သို့မဟုတ် client application အတွင်းမှ ခေါ်ဆိုနိုင်သည်။

## Optional: Configure policies

Azure API Management တွင် policy များကို အခြေခံ၍ endpoint များအတွက် စည်းမျဉ်းစည်းကမ်းများ (ဥပမာ rate limiting သို့မဟုတ် semantic caching) ကို သတ်မှတ်နိုင်သည်။ ၎င်း policy များကို XML ဖြင့်ရေးသားသည်။

MCP Server အတွက် rate limiting policy ကို သတ်မှတ်ပုံမှာ အောက်ပါအတိုင်းဖြစ်သည်-

1. Portal တွင် APIs အောက်မှ **MCP Servers** ကို ရွေးချယ်ပါ။

1. ဖန်တီးထားသော MCP server ကို ရွေးချယ်ပါ။

1. ဘယ်ဘက် menu တွင် MCP အောက်မှ **Policies** ကို ရွေးပါ။

1. Policy editor တွင် MCP server ၏ tools များအတွက် သတ်မှတ်လိုသည့် policy များကို ထည့်သွင်း သို့မဟုတ် ပြင်ဆင်ပါ။ Policy များကို XML ဖော်မတ်ဖြင့် သတ်မှတ်ထားသည်။ ဥပမာအနေဖြင့် MCP server ၏ tools များကို ခေါ်ဆိုမှုအရေအတွက်ကို ကန့်သတ်ရန် (ဤဥပမာတွင် ၃၀ စက္ကန့်အတွင်း client IP တစ်ခုလျှင် ၅ ခေါ်ဆိုမှု) policy ကို ထည့်သွင်းနိုင်သည်။ အောက်ပါ XML သည် rate limiting ဖြစ်စေမည်။

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Policy editor ၏ ပုံရိပ်-

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Try it out

MCP Server သည် ရည်ရွယ်ချက်အတိုင်း လုပ်ဆောင်နေကြောင်း သေချာစေပါမည်။

ဒါအတွက် Visual Studio Code နှင့် GitHub Copilot ၏ Agent mode ကို အသုံးပြုမည်ဖြစ်သည်။ MCP server ကို *mcp.json* တွင် ထည့်သွင်းမည်ဖြစ်သည်။ ၎င်းအားဖြင့် Visual Studio Code သည် agentic အင်အားဖြင့် client အဖြစ် လုပ်ဆောင်ပြီး အသုံးပြုသူများသည် prompt ရိုက်ထည့်၍ server နှင့် ဆက်သွယ်နိုင်မည်ဖြစ်သည်။

Visual Studio Code တွင် MCP server ကို ထည့်သွင်းပုံ-

1. Command Palette မှ MCP: **Add Server command** ကို အသုံးပြုပါ။

1. Prompt တွင် server အမျိုးအစားကို ရွေးချယ်ပါ- **HTTP (HTTP or Server Sent Events)**။

1. API Management ၏ MCP server URL ကို ထည့်ပါ။ ဥပမာ- **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (SSE endpoint အတွက်) သို့မဟုတ် **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (MCP endpoint အတွက်)၊ transport များ၏ ကွာခြားချက်မှာ `/sse` or `/mcp` ဖြစ်သည်။

1. သင်ကြိုက်နှစ်သက်သည့် server ID ကို ထည့်ပါ။ အရေးကြီးသော တန်ဖိုးမဟုတ်ပေမယ့် server instance ကို မှတ်မိရန် ကူညီပါသည်။

1. configuration ကို workspace settings သို့မဟုတ် user settings မှာ သိမ်းဆည်းမည်ကို ရွေးပါ။

  - **Workspace settings** - server configuration ကို .vscode/mcp.json ဖိုင်တွင်သာ သိမ်းဆည်းမည်ဖြစ်ပြီး လက်ရှိ workspace တွင်သာ အသုံးပြုနိုင်သည်။

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    သို့မဟုတ် streaming HTTP ကို transport အဖြစ် ရွေးချယ်ပါက အနည်းငယ်ကွာခြားသည်-

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **User settings** - server configuration ကို global *settings.json* ဖိုင်တွင် ထည့်သွင်းပြီး workspace အားလုံးတွင် အသုံးပြုနိုင်သည်။ configuration သည် အောက်ပါအတိုင်း ဖြစ်သည်-

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Azure API Management သို့ မှန်ကန်စွာ authenticate လုပ်ရန် header တစ်ခုထည့်သွင်းရမည်ဖြစ်သည်။ အဆိုပါ header ကို **Ocp-Apim-Subscription-Key** ဟု ခေါ်သည်။

    - settings တွင် ထည့်သွင်းပုံ-

    ![Adding header for authentication](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png)၊ ၎င်းသည် API key တန်ဖိုးကို မေးမြန်းမည်ဖြစ်ပြီး သင်၏ Azure API Management instance အတွက် Azure Portal မှ ရယူနိုင်သည်။

   - *mcp.json* ထဲတွင် ထည့်သွင်းရန်-

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

### Use Agent mode

အခု settings သို့မဟုတ် *.vscode/mcp.json* တွင် ပြင်ဆင်ပြီးဖြစ်သည်။ စမ်းသပ်ကြည့်ပါ။

Tools icon တစ်ခုရှိပြီး server မှ ဖော်ပြထားသော tools များကို ပြသမည်-

![Tools from the server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Tools icon ကို နှိပ်ပါ၊ tools များစာရင်းကို မြင်ရမည်-

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. tool ကို ခေါ်ဆိုရန် chat တွင် prompt တစ်ခု ရိုက်ထည့်ပါ။ ဥပမာ၊ order အကြောင်း သိရှိရန် tool တစ်ခု ရွေးထားပါက agent ကို order အကြောင်း မေးနိုင်သည်။ ဤမှာ ဥပမာ prompt-

    ```text
    get information from order 2
    ```

    အခု tools icon သို့ သင့်အား prompt ပေးမည်၊ tool ကို ခေါ်ဆိုရန် ဆက်လက်ရွေးချယ်ပါ။ ထို့နောက် အောက်ပါအတိုင်း အဖြေကို မြင်ရမည်-

    ![Result from prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **အထက်ဖော်ပြထားသည့်အတိုင်း သင့်တပ်ဆင်ထားသော tools များပေါ်မူတည်ပြီး စာသားဖြင့် တုံ့ပြန်ချက်ရရှိမည်ဖြစ်သည်။**


## References

ပိုမိုလေ့လာလိုပါက-

- [Tutorial on Azure API Management and MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python sample: Secure remote MCP servers using Azure API Management (experimental)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP client authorization lab](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Use the Azure API Management extension for VS Code to import and manage APIs](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Register and discover remote MCP servers in Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Azure API Management ဖြင့် AI အင်္ဂါရပ်များစွာကို ပြသထားသော repo အကောင်းတစ်ခု
- [AI Gateway workshops](https://azure-samples.github.io/AI-Gateway/) Azure Portal ကို အသုံးပြု၍ AI အင်္ဂါရပ်များကို စမ်းသပ်သည့် workshop များ ပါဝင်သည်။ AI အင်္ဂါရပ်များကို စတင်သုံးသပ်ရန် အကောင်းဆုံးနည်းလမ်းတစ်ခုဖြစ်သည်။

**အသိပေးချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ တိကျမှုအတွက် ကြိုးစားပေမယ့် အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း ကျေးဇူးပြု၍ သတိပြုပါ။ မူလစာတမ်းကို မူရင်းဘာသာဖြင့်သာ အတည်ပြုရမည့် အရင်းအမြစ်အဖြစ် သတ်မှတ်ရန် လိုအပ်ပါသည်။ အရေးကြီးသော သတင်းအချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူ့ဘာသာပြန်မှ ပြန်လည်ဘာသာပြန်ရန် အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုခြင်းကြောင့် ဖြစ်ပေါ်လာသော နားမလည်မှုများ သို့မဟုတ် မှားယွင်းဖော်ပြချက်များအတွက် ကျွန်ုပ်တို့မှာ တာဝန်မရှိပါ။