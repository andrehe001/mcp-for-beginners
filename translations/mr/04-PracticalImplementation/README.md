<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5384bbb2a92d00d5d7e66274dbe0331d",
  "translation_date": "2025-06-20T18:26:34+00:00",
  "source_file": "04-PracticalImplementation/README.md",
  "language_code": "mr"
}
-->
# Practical Implementation

व्यावहारिक अंमलबजावणी म्हणजे Model Context Protocol (MCP) ची ताकद प्रत्यक्षात अनुभवायला मिळते. MCP च्या सिद्धांत आणि आर्किटेक्चर समजून घेणं महत्त्वाचं आहे, पण खरी किंमत तेव्हा उमगते जेव्हा तुम्ही या संकल्पनांचा वापर करून वास्तविक समस्यांवर उपाय तयार करता, चाचणी करता आणि तैनात करता. हा प्रकरण सैद्धांतिक ज्ञान आणि प्रत्यक्ष विकास यामधील अंतर कमी करतो आणि MCP-आधारित अनुप्रयोग तयार करण्याच्या प्रक्रियेत तुम्हाला मार्गदर्शन करतो.

तुम्ही बुद्धिमान सहाय्यक तयार करत असाल, व्यवसाय प्रक्रियेत AI समाकलित करत असाल किंवा डेटा प्रक्रिया साठी सानुकूल साधने तयार करत असाल, MCP एक लवचिक पाया पुरवतो. त्याची भाषा-स्वतंत्र रचना आणि लोकप्रिय प्रोग्रामिंग भाषांसाठी अधिकृत SDKs अनेक विकासकांसाठी सुलभ करतात. या SDKs चा वापर करून तुम्ही जलद प्रोटोटाइप तयार करू शकता, पुनरावृत्ती करू शकता आणि विविध प्लॅटफॉर्म आणि वातावरणांवर तुमचे उपाय स्केल करू शकता.

पुढील विभागांमध्ये तुम्हाला व्यावहारिक उदाहरणे, नमुना कोड आणि तैनाती धोरणे सापडतील जी C#, Java, TypeScript, JavaScript आणि Python मध्ये MCP कसे अंमलात आणायचे हे दाखवतात. तुम्हाला MCP सर्व्हर डिबग आणि चाचणी कशी करायची, API कसे व्यवस्थापित करायचे आणि Azure वापरून क्लाउडवर उपाय कसे तैनात करायचे हे देखील शिकायला मिळेल. हे हाताळण्याजोगे स्रोत तुमच्या शिकण्याला वेग देण्यासाठी आणि विश्वासाने मजबूत, उत्पादन-तयार MCP अनुप्रयोग तयार करण्यासाठी डिझाइन केले आहेत.

## Overview

हा धडा विविध प्रोग्रामिंग भाषांमध्ये MCP अंमलबजावणीच्या व्यावहारिक बाबींवर लक्ष केंद्रित करतो. आपण C#, Java, TypeScript, JavaScript आणि Python मध्ये MCP SDKs कसे वापरायचे, MCP सर्व्हर डिबग आणि चाचणी कशी करायची आणि पुनर्वापरयोग्य संसाधने, प्रॉम्प्ट आणि साधने कशी तयार करायची हे पाहू.

## Learning Objectives

या धड्याच्या शेवटी, तुम्ही सक्षम असाल:
- विविध प्रोग्रामिंग भाषांमध्ये अधिकृत SDKs वापरून MCP उपाय अंमलात आणणे
- MCP सर्व्हरची व्यवस्थित डिबगिंग आणि चाचणी करणे
- सर्व्हर वैशिष्ट्ये (Resources, Prompts, आणि Tools) तयार करणे आणि वापरणे
- क्लिष्ट कामांसाठी प्रभावी MCP वर्कफ्लोज डिझाइन करणे
- कार्यक्षमता आणि विश्वासार्हतेसाठी MCP अंमलबजावणीचे ऑप्टिमायझेशन करणे

## Official SDK Resources

Model Context Protocol अनेक भाषांसाठी अधिकृत SDKs पुरवतो:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

## Working with MCP SDKs

हा विभाग विविध प्रोग्रामिंग भाषांमध्ये MCP अंमलबजावणीसाठी व्यावहारिक उदाहरणे पुरवतो. तुम्हाला `samples` निर्देशिकेत भाषेनुसार नमुना कोड सापडेल.

### Available Samples

रिपॉझिटरीमध्ये खालील भाषांमध्ये [नमुना अंमलबजावणी](../../../04-PracticalImplementation/samples) उपलब्ध आहेत:

- [C#](./samples/csharp/README.md)
- [Java](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

प्रत्येक नमुन्यात त्या विशिष्ट भाषा आणि इकोसिस्टमसाठी MCP च्या मुख्य संकल्पना आणि अंमलबजावणी पद्धती दाखवल्या आहेत.

## Core Server Features

MCP सर्व्हर खालील कोणत्याही वैशिष्ट्यांचा संयोजन अंमलात आणू शकतात:

### Resources
Resources वापरकर्त्याला किंवा AI मॉडेलला संदर्भ आणि डेटा पुरवतात:
- दस्तऐवज संग्रह
- ज्ञानभांडार
- संरचित डेटा स्रोत
- फाइल सिस्टम

### Prompts
Prompts म्हणजे वापरकर्त्यांसाठी साचा केलेले संदेश आणि वर्कफ्लोज:
- पूर्वनिर्धारित संवाद साचे
- मार्गदर्शित संवाद नमुने
- विशेष संवाद संरचना

### Tools
Tools म्हणजे AI मॉडेलने कार्यान्वित करावयाच्या फंक्शन्स:
- डेटा प्रक्रिया साधने
- बाह्य API समाकलन
- संगणकीय क्षमता
- शोध कार्यक्षमता

## Sample Implementations: C#

अधिकृत C# SDK रिपॉझिटरीमध्ये MCP च्या विविध पैलूंचे नमुना अंमलबजावणी उपलब्ध आहेत:

- **Basic MCP Client**: MCP क्लायंट तयार करून साधे टूल कॉल कसे करायचे हे दाखवणारे उदाहरण
- **Basic MCP Server**: मूलभूत टूल नोंदणीसह साधी सर्व्हर अंमलबजावणी
- **Advanced MCP Server**: टूल नोंदणी, प्रमाणीकरण आणि त्रुटी हाताळणीसह पूर्ण वैशिष्ट्यांचा सर्व्हर
- **ASP.NET Integration**: ASP.NET Core सोबत समाकलन दाखवणारे उदाहरण
- **Tool Implementation Patterns**: विविध क्लिष्टतेच्या टूल्ससाठी अंमलबजावणी पद्धती

C# MCP SDK सध्या प्रिव्ह्यूमध्ये आहे आणि API मध्ये बदल होऊ शकतात. SDK सुधारत राहील म्हणून हा ब्लॉग नियमित अद्ययावत केला जाईल.

### Key Features
- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)

- तुमचा [पहिला MCP Server](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/) तयार करा.

पूर्ण C# अंमलबजावणी नमुन्यांसाठी, अधिकृत C# SDK नमुना रिपॉझिटरी पहा: [official C# SDK samples repository](https://github.com/modelcontextprotocol/csharp-sdk)

## Sample implementation: Java Implementation

Java SDK एंटरप्राइझ-ग्रेड वैशिष्ट्यांसह मजबूत MCP अंमलबजावणी पर्याय पुरवतो.

### Key Features

- Spring Framework समाकलन
- मजबूत टाइप सुरक्षा
- Reactive प्रोग्रामिंग समर्थन
- सर्वसमावेशक त्रुटी हाताळणी

पूर्ण Java अंमलबजावणी नमुन्यासाठी, नमुना निर्देशिकेतील [Java sample](samples/java/containerapp/README.md) पहा.

## Sample implementation: JavaScript Implementation

JavaScript SDK हलकी आणि लवचिक MCP अंमलबजावणीसाठी पर्याय पुरवतो.

### Key Features

- Node.js आणि ब्राउझर समर्थन
- Promise-आधारित API
- Express आणि इतर फ्रेमवर्कसोबत सहज समाकलन
- स्ट्रीमिंगसाठी WebSocket समर्थन

पूर्ण JavaScript अंमलबजावणी नमुन्यासाठी, नमुना निर्देशिकेतील [JavaScript sample](samples/javascript/README.md) पहा.

## Sample implementation: Python Implementation

Python SDK उत्कृष्ट ML फ्रेमवर्क समाकलनासह Python-शैलीतील MCP अंमलबजावणी प्रदान करतो.

### Key Features

- asyncio सह async/await समर्थन
- Flask आणि FastAPI समाकलन
- साधी टूल नोंदणी
- लोकप्रिय ML लायब्ररींसोबत मूळ समाकलन

पूर्ण Python अंमलबजावणी नमुन्यासाठी, नमुना निर्देशिकेतील [Python sample](samples/python/README.md) पहा.

## API management

Azure API Management हा एक उत्तम उपाय आहे ज्याद्वारे आपण MCP सर्व्हर सुरक्षित करू शकतो. यामध्ये तुमच्या MCP सर्व्हरच्या समोर Azure API Management ची एक उदाहरण ठेऊन, तुम्हाला हव्या असलेल्या वैशिष्ट्यांची हाताळणी केली जाते, जसे की:

- दर मर्यादा (rate limiting)
- टोकन व्यवस्थापन
- निरीक्षण (monitoring)
- लोड बॅलन्सिंग
- सुरक्षा

### Azure Sample

येथे Azure Sample आहे जो याचं उदाहरण देतो, म्हणजे MCP Server तयार करणे आणि Azure API Management वापरून त्याला सुरक्षित करणे ([link](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)).

खालील प्रतिमेत अधिकृततेचा प्रवाह कसा होतो ते पहा:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

या प्रतिमेत खालील गोष्टी घडतात:

- Microsoft Entra वापरून प्रमाणीकरण/अधिकृतता केली जाते.
- Azure API Management एक गेटवे म्हणून काम करते आणि धोरणांचा वापर करून ट्रॅफिकचे मार्गदर्शन आणि व्यवस्थापन करते.
- Azure Monitor पुढील विश्लेषणासाठी सर्व विनंत्या लॉग करतो.

#### Authorization flow

चला अधिक सविस्तरपणे अधिकृततेचा प्रवाह पाहू:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP authorization specification

[MCP Authorization specification](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization#2-10-third-party-authorization-flow) बद्दल अधिक जाणून घ्या.

## Deploy Remote MCP Server to Azure

आपण आधी नमूद केलेल्या नमुन्याचा तैनाती कशी करायची ते पाहू:

1. रिपॉझिटरी क्लोन करा

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

2. `Microsoft.App` नोंदणी करा

    ` resource provider.
    * If you are using Azure CLI, run `az provider register --namespace Microsoft.App --wait`.
    * If you are using Azure PowerShell, run `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Then run `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState

    काही वेळाने नोंदणी पूर्ण झाली की नाही ते तपासा.

3. हा [azd](https://aka.ms/azd) कमांड चालवा ज्यामुळे API Management सेवा, फंक्शन अॅप (कोडसह) आणि इतर आवश्यक Azure संसाधने तयार होतील

    ```shell
    azd up
    ```

    या कमांडने Azure वर सर्व क्लाउड संसाधने तैनात होतात.

### Testing your server with MCP Inspector

1. **नवीन टर्मिनल विंडो** मध्ये MCP Inspector इंस्टॉल करा आणि चालवा

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    तुम्हाला खालीलप्रमाणे इंटरफेस दिसेल:

    ![Connect to Node inspector](../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.mr.png)

2. CTRL क्लिक करून MCP Inspector वेब अॅप URL वरून लोड करा (उदा. http://127.0.0.1:6274/#resources)
3. ट्रान्सपोर्ट प्रकार `SSE` वर सेट करा आणि **Connect** करा:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

4. **List Tools**. टूलवर क्लिक करा आणि **Run Tool** करा.

जर सर्व पावले यशस्वी झाली तर तुम्ही आता MCP सर्व्हरशी जोडलेले आहात आणि टूल कॉल करू शकलात.

## MCP servers for Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): या रिपॉझिटरीजमध्ये Azure Functions वापरून Python, C# .NET किंवा Node/TypeScript सह सानुकूल दूरस्थ MCP सर्व्हर जलद तयार करण्याचे टेम्पलेट्स आहेत.

या नमुन्यांमुळे विकासकांना संपूर्ण उपाय मिळतो ज्यामुळे ते:

- स्थानिकरित्या तयार आणि चालवू शकतात: स्थानिक संगणकावर MCP सर्व्हर विकसित आणि डिबग करू शकतात
- Azure वर तैनात करू शकतात: सोप्या azd up कमांडने क्लाउडवर तैनात करू शकतात
- क्लायंट्सकडून कनेक्ट होऊ शकतात: विविध क्लायंट्स जसे VS Code चे Copilot agent mode आणि MCP Inspector टूल वापरून कनेक्ट होऊ शकतात

### Key Features:

- सुरक्षेची रचना: MCP सर्व्हर कीज आणि HTTPS वापरून सुरक्षित केला आहे
- प्रमाणीकरण पर्याय: अंगभूत ऑथ आणि/किंवा API Management वापरून OAuth समर्थन
- नेटवर्क पृथक्करण: Azure Virtual Networks (VNET) वापरून नेटवर्क पृथक्करण परवानगी देते
- सर्व्हरलेस आर्किटेक्चर: स्केलेबल, इव्हेंट-चालित अंमलबजावणीसाठी Azure Functions वापरते
- स्थानिक विकास: संपूर्ण स्थानिक विकास आणि डिबगिंग समर्थन
- सोपी तैनाती: Azure वर सुलभ तैनाती प्रक्रिया

रिपॉझिटरीमध्ये सर्व आवश्यक कॉन्फिगरेशन फाइल्स, स्रोत कोड आणि इन्फ्रास्ट्रक्चर व्याख्या आहेत ज्यामुळे उत्पादन-तयार MCP सर्व्हर अंमलबजावणीसाठी त्वरीत सुरुवात करता येते.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Python सह Azure Functions वापरून MCP चे नमुना अंमलबजावणी

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - C# .NET सह Azure Functions वापरून MCP चे नमुना अंमलबजावणी

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Node/TypeScript सह Azure Functions वापरून MCP चे नमुना अंमलबजावणी.

## Key Takeaways

- MCP SDKs भाषानुसार टूल्स पुरवतात जे मजबूत MCP उपाय अंमलात आणण्यासाठी उपयुक्त आहेत
- डिबगिंग आणि चाचणी प्रक्रिया विश्वासार्ह MCP अनुप्रयोगांसाठी अत्यंत महत्त्वाची आहे
- पुनर्वापरयोग्य प्रॉम्प्ट टेम्प्लेट्स सातत्यपूर्ण AI संवाद सक्षम करतात
- चांगल्या रचनेचे वर्कफ्लोज अनेक टूल्स वापरून क्लिष्ट कामे सुलभ करतात
- MCP उपाय अंमलात आणताना सुरक्षा, कार्यक्षमता आणि त्रुटी हाताळणी विचारात घ्यावी लागते

## Exercise

तुमच्या क्षेत्रातील एखाद्या वास्तविक समस्येवर उपाय करणारा व्यावहारिक MCP वर्कफ्लो डिझाइन करा:

1. या समस्येचा निराकरण करण्यासाठी 3-4 उपयुक्त टूल्स ओळखा
2. या टूल्स कसे परस्पर संवाद साधतात हे दाखवणारा वर्कफ्लो आकृती तयार करा
3. तुमच्या पसंतीच्या भाषेत एका टूलचा मूलभूत आवृत्ती तयार करा
4. मॉडेलला तुमचे टूल प्रभावीपणे वापरता यावे यासाठी प्रॉम्प्ट टेम्प्लेट तयार करा

## Additional Resources


---

Next: [Advanced Topics](../05-AdvancedTopics/README.md)

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेचा अभाव असू शकतो. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करणे शिफारसीय आहे. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थ लावणीबद्दल आम्ही जबाबदार नाही.