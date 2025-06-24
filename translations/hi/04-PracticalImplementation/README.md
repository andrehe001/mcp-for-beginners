<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5384bbb2a92d00d5d7e66274dbe0331d",
  "translation_date": "2025-06-20T18:25:00+00:00",
  "source_file": "04-PracticalImplementation/README.md",
  "language_code": "hi"
}
-->
# Practical Implementation

प्रैक्टिकल इम्प्लीमेंटेशन वह जगह है जहाँ Model Context Protocol (MCP) की ताकत वास्तविक रूप में सामने आती है। जबकि MCP के पीछे के सिद्धांत और आर्किटेक्चर को समझना महत्वपूर्ण है, असली मूल्य तब आता है जब आप इन अवधारणाओं को उपयोग में लाकर ऐसे समाधान बनाते हैं, टेस्ट करते हैं, और डिप्लॉय करते हैं जो असली दुनिया की समस्याओं को हल करते हैं। यह अध्याय सैद्धांतिक ज्ञान और व्यावहारिक विकास के बीच का पुल है, जो आपको MCP-आधारित एप्लिकेशन को जीवित करने की प्रक्रिया में मार्गदर्शन करता है।

चाहे आप इंटेलिजेंट असिस्टेंट विकसित कर रहे हों, व्यवसायिक वर्कफ़्लोज़ में AI को इंटीग्रेट कर रहे हों, या डेटा प्रोसेसिंग के लिए कस्टम टूल बना रहे हों, MCP एक लचीला आधार प्रदान करता है। इसकी भाषा-स्वतंत्र डिजाइन और लोकप्रिय प्रोग्रामिंग भाषाओं के लिए आधिकारिक SDKs इसे कई डेवलपर्स के लिए सुलभ बनाते हैं। इन SDKs का उपयोग करके, आप जल्दी से प्रोटोटाइप बना सकते हैं, पुनरावृत्ति कर सकते हैं, और विभिन्न प्लेटफार्मों और वातावरणों में अपने समाधान को स्केल कर सकते हैं।

आगामी सेक्शन्स में, आपको व्यावहारिक उदाहरण, सैंपल कोड, और डिप्लॉयमेंट रणनीतियाँ मिलेंगी जो दिखाती हैं कि कैसे MCP को C#, Java, TypeScript, JavaScript, और Python में इम्प्लीमेंट किया जा सकता है। आप यह भी सीखेंगे कि MCP सर्वर्स को कैसे डिबग और टेस्ट करें, APIs का प्रबंधन कैसे करें, और Azure का उपयोग करके क्लाउड में समाधान कैसे डिप्लॉय करें। ये व्यावहारिक संसाधन आपकी सीखने की गति बढ़ाने और आत्मविश्वास के साथ मजबूत, प्रोडक्शन-तैयार MCP एप्लिकेशन बनाने में मदद करने के लिए डिज़ाइन किए गए हैं।

## Overview

यह पाठ MCP के व्यावहारिक पहलुओं पर केंद्रित है, जो कई प्रोग्रामिंग भाषाओं में इम्प्लीमेंटेशन को कवर करता है। हम देखेंगे कि C#, Java, TypeScript, JavaScript, और Python में MCP SDKs का उपयोग करके मजबूत एप्लिकेशन कैसे बनाएं, MCP सर्वर्स को डिबग और टेस्ट करें, और पुन: उपयोगी संसाधन, प्रॉम्प्ट, और टूल कैसे बनाएं।

## Learning Objectives

इस पाठ के अंत तक, आप सक्षम होंगे:
- विभिन्न प्रोग्रामिंग भाषाओं में आधिकारिक SDKs का उपयोग करके MCP समाधान इम्प्लीमेंट करना
- MCP सर्वर्स को व्यवस्थित तरीके से डिबग और टेस्ट करना
- सर्वर फीचर्स (Resources, Prompts, और Tools) बनाना और उपयोग करना
- जटिल कार्यों के लिए प्रभावी MCP वर्कफ़्लोज़ डिजाइन करना
- प्रदर्शन और विश्वसनीयता के लिए MCP इम्प्लीमेंटेशन का अनुकूलन करना

## Official SDK Resources

Model Context Protocol कई भाषाओं के लिए आधिकारिक SDKs प्रदान करता है:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

## Working with MCP SDKs

यह सेक्शन कई प्रोग्रामिंग भाषाओं में MCP इम्प्लीमेंटेशन के व्यावहारिक उदाहरण प्रदान करता है। आप `samples` डायरेक्टरी में भाषा अनुसार व्यवस्थित सैंपल कोड पा सकते हैं।

### Available Samples

रिपॉजिटरी में निम्नलिखित भाषाओं में [सैंपल इम्प्लीमेंटेशन](../../../04-PracticalImplementation/samples) शामिल हैं:

- [C#](./samples/csharp/README.md)
- [Java](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

प्रत्येक सैंपल उस विशेष भाषा और इकोसिस्टम के लिए MCP की मुख्य अवधारणाओं और इम्प्लीमेंटेशन पैटर्न को दर्शाता है।

## Core Server Features

MCP सर्वर निम्नलिखित फीचर्स के किसी भी संयोजन को लागू कर सकते हैं:

### Resources
Resources उपयोगकर्ता या AI मॉडल के लिए संदर्भ और डेटा प्रदान करते हैं:
- दस्तावेज़ रिपॉजिटरी
- नॉलेज बेस
- संरचित डेटा स्रोत
- फ़ाइल सिस्टम

### Prompts
Prompts उपयोगकर्ताओं के लिए टेम्प्लेटेड संदेश और वर्कफ़्लोज़ होते हैं:
- पूर्व-निर्धारित संवाद टेम्प्लेट
- मार्गदर्शित इंटरैक्शन पैटर्न
- विशेषीकृत संवाद संरचनाएँ

### Tools
Tools AI मॉडल द्वारा निष्पादित किए जाने वाले फ़ंक्शन होते हैं:
- डेटा प्रोसेसिंग यूटिलिटीज़
- बाहरी API इंटीग्रेशन
- गणनात्मक क्षमताएँ
- खोज कार्यक्षमता

## Sample Implementations: C#

आधिकारिक C# SDK रिपॉजिटरी में MCP के विभिन्न पहलुओं को प्रदर्शित करने वाले कई सैंपल इम्प्लीमेंटेशन शामिल हैं:

- **Basic MCP Client**: MCP क्लाइंट बनाने और टूल कॉल करने का सरल उदाहरण
- **Basic MCP Server**: बेसिक टूल रजिस्ट्रेशन के साथ न्यूनतम सर्वर इम्प्लीमेंटेशन
- **Advanced MCP Server**: टूल रजिस्ट्रेशन, प्रमाणीकरण, और त्रुटि प्रबंधन के साथ पूर्ण फीचर वाला सर्वर
- **ASP.NET Integration**: ASP.NET Core के साथ इंटीग्रेशन दिखाने वाले उदाहरण
- **Tool Implementation Patterns**: विभिन्न जटिलता स्तरों के साथ टूल इम्प्लीमेंट करने के लिए विभिन्न पैटर्न

MCP C# SDK अभी प्रीव्यू में है और APIs में बदलाव हो सकते हैं। जैसे-जैसे SDK विकसित होगा, हम इस ब्लॉग को अपडेट करते रहेंगे।

### Key Features 
- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)

- अपना [पहला MCP Server](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/) बनाना।

पूर्ण C# इम्प्लीमेंटेशन सैंपल के लिए, आधिकारिक [C# SDK सैंपल रिपॉजिटरी](https://github.com/modelcontextprotocol/csharp-sdk) देखें।

## Sample implementation: Java Implementation

Java SDK एंटरप्राइज-ग्रेड फीचर्स के साथ मजबूत MCP इम्प्लीमेंटेशन विकल्प प्रदान करता है।

### Key Features

- Spring Framework इंटीग्रेशन
- मजबूत टाइप सुरक्षा
- रिएक्टिव प्रोग्रामिंग सपोर्ट
- व्यापक त्रुटि प्रबंधन

पूर्ण Java इम्प्लीमेंटेशन सैंपल के लिए, सैंपल डायरेक्टरी में [Java sample](samples/java/containerapp/README.md) देखें।

## Sample implementation: JavaScript Implementation

JavaScript SDK MCP इम्प्लीमेंटेशन के लिए हल्का और लचीला दृष्टिकोण प्रदान करता है।

### Key Features

- Node.js और ब्राउज़र सपोर्ट
- प्रॉमिस-आधारित API
- Express और अन्य फ्रेमवर्क के साथ आसान इंटीग्रेशन
- स्ट्रीमिंग के लिए WebSocket सपोर्ट

पूर्ण JavaScript इम्प्लीमेंटेशन सैंपल के लिए, सैंपल डायरेक्टरी में [JavaScript sample](samples/javascript/README.md) देखें।

## Sample implementation: Python Implementation

Python SDK MCP इम्प्लीमेंटेशन के लिए पायथोनिक दृष्टिकोण प्रदान करता है, जिसमें उत्कृष्ट ML फ्रेमवर्क इंटीग्रेशन शामिल हैं।

### Key Features

- asyncio के साथ Async/await सपोर्ट
- Flask और FastAPI इंटीग्रेशन
- सरल टूल रजिस्ट्रेशन
- लोकप्रिय ML लाइब्रेरीज के साथ नेटिव इंटीग्रेशन

पूर्ण Python इम्प्लीमेंटेशन सैंपल के लिए, सैंपल डायरेक्टरी में [Python sample](samples/python/README.md) देखें।

## API management 

Azure API Management MCP Servers को सुरक्षित करने का एक बेहतरीन तरीका है। विचार यह है कि आप अपने MCP Server के सामने एक Azure API Management इंस्टेंस लगाएं और इसे उन फीचर्स को संभालने दें जो आप चाहते हैं, जैसे:

- रेट लिमिटिंग
- टोकन प्रबंधन
- मॉनिटरिंग
- लोड बैलेंसिंग
- सुरक्षा

### Azure Sample

यहाँ एक Azure Sample है जो बिल्कुल यही करता है, यानी [MCP Server बनाना और Azure API Management के साथ इसे सुरक्षित करना](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)।

नीचे की छवि में देखें कि ऑथोराइजेशन फ्लो कैसे होता है:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true) 

पिछली छवि में निम्नलिखित होता है:

- Microsoft Entra का उपयोग करके प्रमाणीकरण/अधिकार प्रदान करना होता है।
- Azure API Management एक गेटवे के रूप में कार्य करता है और ट्रैफ़िक को निर्देशित और प्रबंधित करने के लिए नीतियों का उपयोग करता है।
- Azure Monitor आगे के विश्लेषण के लिए सभी अनुरोधों को लॉग करता है।

#### Authorization flow

आइए ऑथोराइजेशन फ्लो को और विस्तार से देखें:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP authorization specification

[MCP Authorization specification](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization#2-10-third-party-authorization-flow) के बारे में और जानें।

## Deploy Remote MCP Server to Azure

आइए देखें कि क्या हम पहले बताए गए सैंपल को डिप्लॉय कर सकते हैं:

1. रिपॉजिटरी क्लोन करें

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

2. `Microsoft.App` रजिस्टर करें

    `` resource provider.
    * If you are using Azure CLI, run `az provider register --namespace Microsoft.App --wait`.
    * If you are using Azure PowerShell, run `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Then run `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` कमांड चलाएं और कुछ समय बाद देखें कि रजिस्ट्रेशन पूरा हुआ या नहीं।

3. इस [azd](https://aka.ms/azd) कमांड को चलाएं ताकि API Management सर्विस, फंक्शन ऐप (कोड के साथ), और अन्य आवश्यक Azure संसाधन प्राविजन हो सकें:

    ```shell
    azd up
    ```

    यह कमांड Azure पर सभी क्लाउड संसाधनों को डिप्लॉय कर देगा।

### Testing your server with MCP Inspector

1. एक **नई टर्मिनल विंडो** में MCP Inspector इंस्टॉल और रन करें:

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    आपको एक इंटरफेस दिखाई देगा, जो कुछ ऐसा दिखेगा:

    ![Connect to Node inspector](../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.hi.png) 

2. CTRL क्लिक करें ताकि MCP Inspector वेब ऐप उस URL से लोड हो जाए जो ऐप दिखाता है (जैसे http://127.0.0.1:6274/#resources)
3. ट्रांसपोर्ट टाइप को `SSE`
1. Set the URL to your running API Management SSE endpoint displayed after `azd up` पर सेट करें और **Connect** करें:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

5. **List Tools**। किसी टूल पर क्लिक करें और **Run Tool** करें।

यदि सभी चरण सफल रहे, तो अब आप MCP सर्वर से जुड़ चुके हैं और आपने टूल कॉल कर लिया है।

## MCP servers for Azure 

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): यह रिपॉजिटरीज का सेट Python, C# .NET या Node/TypeScript का उपयोग करके Azure Functions के साथ कस्टम रिमोट MCP (Model Context Protocol) सर्वर बनाने और डिप्लॉय करने के लिए क्विकस्टार्ट टेम्पलेट है।

यह सैंपल डेवलपर्स को निम्नलिखित सुविधाएँ प्रदान करता है:

- लोकल पर बिल्ड और रन: स्थानीय मशीन पर MCP सर्वर विकसित और डिबग करें
- Azure पर डिप्लॉय: एक सरल azd up कमांड से क्लाउड पर आसानी से डिप्लॉय करें
- क्लाइंट्स से कनेक्ट करें: VS Code के Copilot एजेंट मोड और MCP Inspector टूल सहित विभिन्न क्लाइंट्स से MCP सर्वर से कनेक्ट करें

### Key Features:

- डिज़ाइन से सुरक्षा: MCP सर्वर को कीज़ और HTTPS के माध्यम से सुरक्षित किया गया है
- प्रमाणीकरण विकल्प: बिल्ट-इन ऑथ और/या API Management के माध्यम से OAuth सपोर्ट करता है
- नेटवर्क अलगाव: Azure Virtual Networks (VNET) के माध्यम से नेटवर्क अलगाव की अनुमति देता है
- सर्वरलेस आर्किटेक्चर: स्केलेबल, इवेंट-ड्रिवन निष्पादन के लिए Azure Functions का उपयोग करता है
- स्थानीय विकास: व्यापक स्थानीय विकास और डिबगिंग सपोर्ट
- सरल डिप्लॉयमेंट: Azure के लिए सुव्यवस्थित डिप्लॉयमेंट प्रक्रिया

रिपॉजिटरी में सभी आवश्यक कॉन्फ़िगरेशन फाइलें, सोर्स कोड, और इन्फ्रास्ट्रक्चर डिफ़िनिशन शामिल हैं ताकि आप जल्दी से प्रोडक्शन-तैयार MCP सर्वर इम्प्लीमेंटेशन शुरू कर सकें।

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Python के साथ Azure Functions का उपयोग करके MCP का सैंपल इम्प्लीमेंटेशन

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - C# .NET के साथ Azure Functions का उपयोग करके MCP का सैंपल इम्प्लीमेंटेशन

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Node/TypeScript के साथ Azure Functions का उपयोग करके MCP का सैंपल इम्प्लीमेंटेशन

## Key Takeaways

- MCP SDKs भाषा-विशिष्ट टूल प्रदान करते हैं जो मजबूत MCP समाधान इम्प्लीमेंट करने में मदद करते हैं
- डिबगिंग और टेस्टिंग प्रक्रिया विश्वसनीय MCP एप्लिकेशन के लिए महत्वपूर्ण है
- पुन: उपयोगी प्रॉम्प्ट टेम्प्लेट्स AI इंटरैक्शन को सुसंगत बनाते हैं
- अच्छी तरह डिज़ाइन किए गए वर्कफ़्लोज़ कई टूल्स का उपयोग करके जटिल कार्यों का समन्वय कर सकते हैं
- MCP समाधान लागू करते समय सुरक्षा, प्रदर्शन, और त्रुटि प्रबंधन का ध्यान रखना आवश्यक है

## Exercise

अपने डोमेन में किसी वास्तविक समस्या को हल करने वाला एक व्यावहारिक MCP वर्कफ़्लो डिज़ाइन करें:

1. उस समस्या को हल करने के लिए 3-4 उपयोगी टूल्स की पहचान करें
2. एक वर्कफ़्लो डायग्राम बनाएं जो दिखाए कि ये टूल्स कैसे इंटरैक्ट करते हैं
3. अपनी पसंदीदा भाषा का उपयोग करके एक टूल का बेसिक वर्शन इम्प्लीमेंट करें
4. एक प्रॉम्प्ट टेम्प्लेट बनाएं जो मॉडल को आपके टूल का प्रभावी उपयोग करने में मदद करे

## Additional Resources


---

Next: [Advanced Topics](../05-AdvancedTopics/README.md)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या गलतियाँ हो सकती हैं। मूल दस्तावेज़ को इसकी मूल भाषा में प्राधिकृत स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।