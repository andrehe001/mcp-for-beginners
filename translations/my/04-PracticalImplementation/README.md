<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5384bbb2a92d00d5d7e66274dbe0331d",
  "translation_date": "2025-06-20T18:48:28+00:00",
  "source_file": "04-PracticalImplementation/README.md",
  "language_code": "my"
}
-->
# လက်တွေ့အသုံးပြုခြင်း

လက်တွေ့အသုံးပြုခြင်းသည် Model Context Protocol (MCP) ၏ အင်အားကို ထင်ရှားစေသောနေရာဖြစ်သည်။ MCP ၏ သီအိုရီနှင့် ဖွဲ့စည်းပုံကို နားလည်ခြင်းမှာ အရေးကြီးသော်လည်း၊ အမှန်တကယ်တန်ဖိုးရှိတာကတော့ ဒီအယူအဆတွေကို အသုံးပြု၍ အမှန်တကယ်ဖြေရှင်းချက်တွေကို တည်ဆောက်၊ စမ်းသပ်၊ ထုတ်လုပ်ခြင်းဖြစ်သည်။ ဒီအခန်းက MCP အခြေခံ အက်ပ်ပလီကေးရှင်းတွေကို ဖန်တီးရာတွင် သဘောတရားနဲ့ လက်တွေ့ ဖွံ့ဖြိုးတိုးတက်မှုကြားက အကွာအဝေးကို တည်ဆောက်ပေးပြီး လမ်းညွှန်ပေးမှာ ဖြစ်သည်။

သင့်အနေဖြင့် ဉာဏ်ရည်မြင့် အကူအညီပေးသူများ ဖန်တီးခြင်း၊ AI ကို စီးပွားရေးလုပ်ငန်းစဉ်များနှင့် ပေါင်းစည်းခြင်း သို့မဟုတ် ဒေတာကို ကိုင်တွယ်ရာတွင် အသုံးပြုမည့် စိတ်ကြိုက်ကိရိယာများ တည်ဆောက်ခြင်း စသည့် လုပ်ငန်းများတွင် MCP သည် အလွယ်တကူ ကိုက်ညီနိုင်သော အခြေခံကျသော ဖွဲ့စည်းမှုကို ပေးစွမ်းသည်။ ၎င်း၏ ဘာသာစကားမရွေး ဒီဇိုင်းနှင့် လူကြိုက်များသော ပရိုဂရမ်မင်းဘာသာစကားများအတွက် တရားဝင် SDK များကြောင့် တိုးတက်သော ဖွံ့ဖြိုးသူများအတွက် လွယ်ကူစွာ ဝင်ရောက်အသုံးပြုနိုင်သည်။ ဒီ SDK များကို အသုံးပြုခြင်းအားဖြင့် သင်သည် မျိုးစုံသော ပလက်ဖောင်းများနှင့် ပတ်ဝန်းကျင်များပေါ်တွင် လျင်မြန်စွာ ပရိုတိုတိုက် ပြုလုပ်၊ ပြန်လည်ပြင်ဆင်၊ တိုးချဲ့နိုင်မည်ဖြစ်သည်။

အောက်ပါအပိုင်းများတွင် C#, Java, TypeScript, JavaScript, နှင့် Python တို့တွင် MCP ကို အသုံးပြု၍ လက်တွေ့ ဥပမာများ၊ နမူနာကုဒ်များနှင့် ထုတ်လုပ်ခြင်း များကို တွေ့မြင်နိုင်မည်ဖြစ်ပြီး MCP ဆာဗာများကို ဘယ်လို ပြင်ဆင်စမ်းသပ်မလဲ၊ API များကို စီမံခန့်ခွဲမလဲ၊ Azure ကို အသုံးပြု၍ ဖြန့်ချိမလဲ စသည့် လမ်းညွှန်ချက်များပါဝင်သည်။ ဒီလက်တွေ့အရင်းအမြစ်များသည် သင်၏ သင်ယူမှုကို မြန်ဆန်စေပြီး သင့်အား ယုံကြည်စိတ်ချစွာ ပြည့်စုံပြီး ထုတ်လုပ်မှုအဆင်သင့် MCP အက်ပ်များ ဖန်တီးနိုင်ရန် ကူညီပေးမည်ဖြစ်သည်။

## အနှစ်ချုပ်

ဒီသင်ခန်းစာမှာ MCP ကို မျိုးစုံသော ပရိုဂရမ်းမင်းဘာသာစကားများဖြင့် လက်တွေ့ အသုံးပြုခြင်းဆိုင်ရာ အချက်အလက်များကို အာရုံစိုက်ထားသည်။ C#, Java, TypeScript, JavaScript, နှင့် Python တို့တွင် MCP SDK များကို အသုံးပြု၍ သက်တောင့်သက်သာရှိသော အက်ပ်များ ဖန်တီးခြင်း၊ MCP ဆာဗာများကို ပြင်ဆင်စမ်းသပ်ခြင်း၊ ပြန်လည်အသုံးပြုနိုင်သော အရင်းအမြစ်များ၊ prompt များနှင့် ကိရိယာများ ဖန်တီးခြင်းတို့ကို လေ့လာမည်ဖြစ်သည်။

## သင်ယူရမည့် ရည်မှန်းချက်များ

ဒီသင်ခန်းစာ အဆုံးသတ်သည့်အချိန်မှာ သင်သည် -

- မျိုးစုံသော ပရိုဂရမ်းမင်းဘာသာစကားများအတွက် တရားဝင် SDK များကို အသုံးပြု၍ MCP ဖြေရှင်းချက်များကို တည်ဆောက်နိုင်မည်။
- MCP ဆာဗာများကို စနစ်တကျ ပြင်ဆင်စမ်းသပ်နိုင်မည်။
- ဆာဗာအင်္ဂါရပ်များ (Resources, Prompts, နှင့် Tools) ကို ဖန်တီးအသုံးပြုနိုင်မည်။
- စိတ်ရှုပ်ထွေးသော လုပ်ငန်းများအတွက် ထိရောက်သော MCP လုပ်ငန်းစဉ်များကို ဒီဇိုင်းဆွဲနိုင်မည်။
- စွမ်းဆောင်ရည်နှင့် ယုံကြည်စိတ်ချရမှုအတွက် MCP ကို အကောင်းဆုံး အကောင်အထည်ဖော်နိုင်မည်။

## တရားဝင် SDK အရင်းအမြစ်များ

Model Context Protocol သည် မျိုးစုံသော ဘာသာစကားများအတွက် တရားဝင် SDK များကို ပံ့ပိုးပေးသည် -

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

## MCP SDK များနှင့် အလုပ်လုပ်ခြင်း

ဒီအပိုင်းတွင် MCP ကို မျိုးစုံသော ပရိုဂရမ်းမင်းဘာသာစကားများဖြင့် အကောင်အထည်ဖော်နည်း လက်တွေ့ ဥပမာများ ပါရှိသည်။ `samples` ဖိုင်တွဲတွင် ဘာသာစကားအလိုက် စီစဉ်ထားသော နမူနာကုဒ်များကို တွေ့နိုင်သည်။

### ရနိုင်သော နမူနာများ

ဒီ repository တွင် အောက်ပါ ဘာသာစကားများအတွက် [နမူနာ အကောင်အထည်ဖော်မှုများ](../../../04-PracticalImplementation/samples) ပါဝင်သည် -

- [C#](./samples/csharp/README.md)
- [Java](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

နမူနာတိုင်းသည် အဆိုပါ ဘာသာစကားနှင့် ပတ်ဝန်းကျင်အတွက် MCP ၏ အဓိကအယူအဆများနှင့် အကောင်အထည်ဖော်မှု နမူနာများကို ပြသပေးသည်။

## အဓိက ဆာဗာ အင်္ဂါရပ်များ

MCP ဆာဗာများသည် အောက်ပါ အင်္ဂါရပ်များကို မည်သည့်ပေါင်းစပ်မှုဖြင့်မဆို အကောင်အထည်ဖော်နိုင်သည် -

### Resources  
Resources သည် အသုံးပြုသူ သို့မဟုတ် AI မော်ဒယ် အသုံးပြုရန် အကြောင်းအရာနှင့် ဒေတာများ ပေးစွမ်းသည် -  
- စာရွက်စာတမ်း စုစည်းရာနေရာများ  
- သိပ္ပံပညာအခြေခံများ  
- ဖွဲ့စည်းထားသော ဒေတာ များ  
- ဖိုင်စနစ်များ  

### Prompts  
Prompts သည် အသုံးပြုသူများအတွက် စံနှုန်းထား စကားပြော ပုံစံများနှင့် လုပ်ငန်းစဉ်များ ဖြစ်သည် -  
- ကြိုတင် သတ်မှတ်ထားသော စကားပြော ပုံစံများ  
- လမ်းညွှန် အပြန်အလှန် ဆက်သွယ်မှု ပုံစံများ  
- အထူးပြု စကားပြော ဖွဲ့စည်းမှုများ  

### Tools  
Tools သည် AI မော်ဒယ်က ဆောင်ရွက်နိုင်ရန် လုပ်ဆောင်ချက်များ ဖြစ်သည် -  
- ဒေတာ ကိုင်တွယ်မှု ကိရိယာများ  
- ပြင်ပ API ပေါင်းစည်းမှုများ  
- တွက်ချက်နိုင်စွမ်းများ  
- ရှာဖွေရေး လုပ်ဆောင်ချက်များ  

## နမူနာ အကောင်အထည်ဖော်မှု: C#

တရားဝင် C# SDK repository တွင် MCP ၏ အစိတ်အပိုင်းများကို ပြသသည့် နမူနာ အကောင်အထည်ဖော်မှုများ ပါဝင်သည် -

- **အခြေခံ MCP Client**: MCP client တစ်ခု ဖန်တီး၍ tool များ ခေါ်ယူနည်း ရိုးရှင်း ဥပမာ  
- **အခြေခံ MCP Server**: အနည်းဆုံး tool မှတ်ပုံတင်မှုပါရှိသည့် ဆာဗာ အကောင်အထည်ဖော်မှု  
- **တိုးတက်ပြီး MCP Server**: tool မှတ်ပုံတင်ခြင်း၊ အတည်ပြုခြင်းနှင့် အမှားစီမံခန့်ခွဲမှုပါရှိသော အပြည့်အစုံ ဆာဗာ  
- **ASP.NET ပေါင်းစည်းမှု**: ASP.NET Core နှင့် ပေါင်းစည်းခြင်း ဥပမာများ  
- **Tool အကောင်အထည်ဖော်မှု ပုံစံများ**: အမျိုးမျိုးသော အဆင့်အတန်းများဖြင့် tool များ ဖန်တီးနည်းပုံစံများ  

MCP C# SDK သည် စမ်းသပ်ကာလတွင်ရှိပြီး API များ ပြောင်းလဲနိုင်ပါသည်။ SDK တိုးတက်လာသည့်အတိုင်း ဒီဘလော့ဂ်ကို ဆက်လက် အပ်ဒိတ်လုပ်သွားမည်ဖြစ်သည်။

### အဓိက အင်္ဂါရပ်များ  
- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)  
- သင့် [ပထမဆုံး MCP Server တည်ဆောက်ခြင်း](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/)  

C# အကောင်အထည်ဖော်မှု နမူနာများ အပြည့်အစုံအတွက် [တရားဝင် C# SDK နမူနာ repository](https://github.com/modelcontextprotocol/csharp-sdk) ကို ကြည့်ရှုနိုင်သည်။

## နမူနာ အကောင်အထည်ဖော်မှု: Java Implementation

Java SDK သည် စက်မှုလုပ်ငန်းအဆင့်အတန်းအတွက် MCP အကောင်အထည်ဖော်မှု ရွေးချယ်စရာများကို ပံ့ပိုးပေးသည်။

### အဓိက အင်္ဂါရပ်များ

- Spring Framework ပေါင်းစည်းမှု  
- အမျိုးအစားလုံခြုံမှု ကြီးမားမှု  
- Reactive programming ပံ့ပိုးမှု  
- အပြည့်အစုံ အမှားစီမံခန့်ခွဲမှု  

Java အကောင်အထည်ဖော်မှု နမူနာ အပြည့်အစုံအတွက် samples ဖိုင်တွဲရှိ [Java sample](samples/java/containerapp/README.md) ကို ကြည့်ရှုပါ။

## နမူနာ အကောင်အထည်ဖော်မှု: JavaScript Implementation

JavaScript SDK သည် MCP အကောင်အထည်ဖော်မှုအတွက် အလင်းလျှပ်နှင့် အလွယ်တကူ လိုက်လျောညီထွေဖြစ်စေသော နည်းလမ်းတစ်ခုကို ပေးစွမ်းသည်။

### အဓိက အင်္ဂါရပ်များ

- Node.js နှင့် browser ပံ့ပိုးမှု  
- Promise အခြေခံ API  
- Express နှင့် အခြား framework များနှင့် လွယ်ကူစွာ ပေါင်းစည်းနိုင်ခြင်း  
- Streaming အတွက် WebSocket ပံ့ပိုးမှု  

JavaScript အကောင်အထည်ဖော်မှု နမူနာ အပြည့်အစုံအတွက် samples ဖိုင်တွဲရှိ [JavaScript sample](samples/javascript/README.md) ကို ကြည့်ရှုပါ။

## နမူနာ အကောင်အထည်ဖော်မှု: Python Implementation

Python SDK သည် ML framework များနှင့် ကောင်းမွန်စွာ ပေါင်းစည်းနိုင်သော Python စတိုင် MCP အကောင်အထည်ဖော်မှုကို ပံ့ပိုးပေးသည်။

### အဓိက အင်္ဂါရပ်များ

- asyncio ဖြင့် async/await ပံ့ပိုးမှု  
- Flask နှင့် FastAPI ပေါင်းစည်းမှု  
- ရိုးရှင်းသော tool မှတ်ပုံတင်ခြင်း  
- လူကြိုက်များသော ML စာကြည့်တိုက်များနှင့် သဘာဝပေါင်းစည်းမှု  

Python အကောင်အထည်ဖော်မှု နမူနာ အပြည့်အစုံအတွက် samples ဖိုင်တွဲရှိ [Python sample](samples/python/README.md) ကို ကြည့်ရှုပါ။

## API စီမံခန့်ခွဲမှု

Azure API Management သည် MCP ဆာဗာများကို ဘယ်လိုလုံခြုံစေမလဲ ဆိုတဲ့ မေးခွန်းကို အကောင်းဆုံး ဖြေရှင်းချက်တစ်ခုဖြစ်သည်။ အဓိကအကြံဉာဏ်မှာ MCP ဆာဗာရှေ့တွင် Azure API Management ကို တပ်ဆင်ပြီး သင့်လိုအပ်ချက်များအတွက် အောက်ပါ အင်္ဂါရပ်များကို ကိုင်တွယ်ပေးရန်ဖြစ်သည် -

- rate limiting  
- token management  
- monitoring  
- load balancing  
- security  

### Azure နမူနာ

ဒီနေရာမှာ Azure နမူနာတစ်ခု ရှိပြီး MCP ဆာဗာတစ်ခု ဖန်တီးပြီး Azure API Management ဖြင့် လုံခြုံစေခြင်းကို ပြသသည်။ (https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

အောက်ပါ ပုံတွင် authorization လုပ်ငန်းစဉ် ဖြစ်ပုံကို ကြည့်ရှုနိုင်သည် -

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

ဤပုံတွင် ဖြစ်ပေါ်နေသော အရာများမှာ -

- Authentication/Authorization ကို Microsoft Entra ဖြင့် ပြုလုပ်သည်။  
- Azure API Management သည် gateway အဖြစ် လုပ်ဆောင်ကာ မူဝါဒများဖြင့် traffic ကို စီမံခန့်ခွဲသည်။  
- Azure Monitor သည် တောင်းဆိုမှုများအားလုံးကို မှတ်တမ်းတင်သည်။  

#### Authorization လုပ်ငန်းစဉ်

Authorization လုပ်ငန်းစဉ်ကို ပိုမိုအသေးစိတ် ကြည့်ရအောင် -

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP authorization specification

ပိုမိုသိရှိလိုပါက [MCP Authorization specification](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization#2-10-third-party-authorization-flow) ကို လေ့လာနိုင်ပါသည်။

## Remote MCP Server ကို Azure တွင် ဖြန့်ချိခြင်း

ယခင်တွင် ဖော်ပြခဲ့သည့် နမူနာကို ဖြန့်ချိနိုင်မလား ကြည့်ကြရအောင် -

1. Repo ကို Clone လုပ်ပါ

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

2. `Microsoft.App` provider ကို မှတ်ပုံတင်ပါ - `` resource provider.
    * If you are using Azure CLI, run `az provider register --namespace Microsoft.App --wait`.
    * If you are using Azure PowerShell, run `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Then run `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` ကို အချိန်အနည်းငယ်ကြာပြီးမှ မှတ်ပုံတင်ပြီးပြီဆိုတာ စစ်ဆေးပါ။

3. ဒီ [azd](https://aka.ms/azd) command ကို အသုံးပြု၍ API Management service, function app (ကုဒ်ပါဝင်သည်) နှင့် Azure ၏ အခြားလိုအပ်သော အရင်းအမြစ်များကို Provision ပြုလုပ်ပါ

    ```shell
    azd up
    ```

    ဒီ command သည် Azure ပေါ်တွင် cloud အရင်းအမြစ်များအားလုံးကို ဖြန့်ချိပေးမည်ဖြစ်သည်။

### MCP Inspector ဖြင့် ဆာဗာ စမ်းသပ်ခြင်း

1. **အသစ်သော terminal မျက်နှာပြင်တွင်** MCP Inspector ကို install လုပ်ပြီး run ပါ

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    အောက်ပါ ပုံစံမျိုးသော အင်တာဖေ့စ်ကို မြင်ရမည်ဖြစ်သည် -

    ![Connect to Node inspector](../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.my.png)

2. CTRL နှိပ်ပြီး MCP Inspector web app ကို URL မှ (ဥပမာ - http://127.0.0.1:6274/#resources) ပြသသောနေရာမှ load လုပ်ပါ  
3. `transport type` ကို `SSE`
1. Set the URL to your running API Management SSE endpoint displayed after `azd up` သို့ ပြောင်းပြီး **Connect** ခလုတ်ကို နှိပ်ပါ

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

5. **List Tools**. Tool တစ်ခုကို နှိပ်ပြီး **Run Tool** လုပ်ပါ။

အဆင့်အားလုံးအောင်မြင်ပါက MCP ဆာဗာနှင့် ချိတ်ဆက်ပြီး Tool ကို ခေါ်ယူနိုင်ပြီ ဖြစ်ပါသည်။

## Azure အတွက် MCP ဆာဗာများ

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) သည် Azure Functions နှင့် Python,

**ချက်ချင်းအသိပေးချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှုဖြစ်သော [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးပမ်းနေသော်လည်း၊ အလိုအလျောက်ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် မှားယွင်းမှုများ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူလစာတမ်းကို မိမိဘာသာစကားဖြင့်သာ တရားဝင်အချက်အလက်အရင်းအမြစ်အဖြစ် သတ်မှတ်သင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် ပရော်ဖက်ရှင်နယ် လူသားဘာသာပြန်မှုကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုမှုကြောင့် ဖြစ်ပေါ်နိုင်သော နားလည်မှားယွင်းမှုများ သို့မဟုတ် မှားယွင်းဖော်ပြချက်များအတွက် ကျွန်ုပ်တို့မှာ တာဝန်မရှိပါ။