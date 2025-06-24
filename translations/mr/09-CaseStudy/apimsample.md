<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "36de9fae488d6de554d969fe8e0801a8",
  "translation_date": "2025-06-20T19:17:20+00:00",
  "source_file": "09-CaseStudy/apimsample.md",
  "language_code": "mr"
}
-->
# केस स्टडी: API Management मध्ये REST API MCP सर्व्हर म्हणून उघड करणे

Azure API Management ही सेवा आहे जी तुमच्या API Endpoints च्या वर एक Gateway पुरवते. हे कसे काम करते म्हणजे Azure API Management तुमच्या APIs च्या समोर प्रॉक्सी सारखे काम करते आणि येणाऱ्या विनंत्यांबाबत काय करायचे ते ठरवते.

हे वापरून, तुम्ही खालील अनेक वैशिष्ट्ये मिळवू शकता:

- **सुरक्षा**, तुम्ही API keys, JWT पासून managed identity पर्यंत सर्वकाही वापरू शकता.
- **रेट लिमिटिंग**, एक छान वैशिष्ट्य म्हणजे ठराविक वेळेत किती कॉल्स पार पडतील हे ठरवता येते. यामुळे सर्व वापरकर्त्यांना चांगला अनुभव मिळतो आणि तुमची सेवा विनंत्यांनी ओव्हरलोड होत नाही याची खात्री होते.
- **स्केलिंग आणि लोड बॅलन्सिंग**. तुम्ही अनेक endpoints सेट करू शकता जे लोड बॅलन्स करतील आणि तुम्ही "लोड बॅलन्स" कसे करायचे ते देखील ठरवू शकता.
- **AI वैशिष्ट्ये जसे semantic caching**, token limit आणि token monitoring वगैरे. ही वैशिष्ट्ये प्रतिसादक्षमता सुधारतात तसेच तुमच्या token खर्चावर नियंत्रण ठेवण्यास मदत करतात. [इथे अधिक वाचा](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## का MCP + Azure API Management?

Model Context Protocol (MCP) हे एजंटिक AI अ‍ॅप्ससाठी लवकरच एक मानक बनत आहे आणि टूल्स व डेटाला एकसंध पद्धतीने कसे उघड करायचे हे ठरवते. जेव्हा तुम्हाला APIs "मॅनेज" करायच्या असतात तेव्हा Azure API Management हा नैसर्गिक पर्याय आहे. MCP Servers अनेकदा इतर APIs सोबत एकत्र काम करतात जेणेकरून विनंत्या टूलकडे सोडवता येतील. त्यामुळे Azure API Management आणि MCP एकत्र करणे खूपच अर्थपूर्ण ठरते.

## आढावा

या विशिष्ट वापराच्या प्रकरणात आपण API endpoints MCP Server म्हणून उघड करायला शिकू. यामुळे हे endpoints एजंटिक अ‍ॅपचा भाग होऊ शकतात आणि Azure API Management चे वैशिष्ट्ये देखील वापरता येतात.

## मुख्य वैशिष्ट्ये

- तुम्ही जे API endpoint मेथड्स टूल्स म्हणून उघड करायच्या आहेत ते निवडता.
- तुम्हाला मिळणारी अतिरिक्त वैशिष्ट्ये तुमच्या API साठी पॉलिसी सेक्शनमध्ये केलेल्या सेटिंग्जवर अवलंबून असतात. येथे आपण रेट लिमिटिंग कशी जोडायची ते दाखवणार आहोत.

## पूर्वपायरी: API आयात करा

जर तुमच्याकडे आधीच Azure API Management मध्ये API असेल तर छान, मग हा टप्पा वगळू शकता. नसल्यास, हा दुवा पहा, [Azure API Management मध्ये API आयात करणे](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## API MCP सर्व्हर म्हणून उघड करा

API endpoints उघड करण्यासाठी खालील टप्पे पाळा:

1. Azure Portal वर जा आणि या पत्त्यावर जा <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
तुमच्या API Management इंस्टन्सकडे जा.

1. डाव्या मेनूमध्ये APIs > MCP Servers > + Create new MCP Server निवडा.

1. API मध्ये, MCP सर्व्हर म्हणून उघड करायचा REST API निवडा.

1. टूल्स म्हणून उघड करायच्या API ऑपरेशन्सपैकी एक किंवा अधिक निवडा. तुम्ही सर्व ऑपरेशन्स किंवा काही विशिष्ट ऑपरेशन्स निवडू शकता.

    ![उघड करायच्या मेथड्सची निवड करा](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. **Create** निवडा.

1. मेनूतील **APIs** आणि **MCP Servers** पर्यायाकडे जा, तुम्हाला खालील दिसेल:

    ![मुख्य पॅनमध्ये MCP Server पहा](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP सर्व्हर तयार झाला आहे आणि API ऑपरेशन्स टूल्स म्हणून उघड केले गेले आहेत. MCP सर्व्हर MCP Servers पॅनमध्ये यादीत दिसेल. URL कॉलममध्ये MCP सर्व्हरचा endpoint दिसतो ज्याला तुम्ही टेस्टिंगसाठी किंवा क्लायंट अ‍ॅप्लिकेशनमध्ये कॉल करू शकता.

## ऐच्छिक: पॉलिसी कॉन्फिगर करा

Azure API Management मध्ये पॉलिसी हा मुख्य संकल्पना आहे जिथे तुम्ही तुमच्या endpoints साठी विविध नियम सेट करता, जसे की रेट लिमिटिंग किंवा semantic caching. या पॉलिसी XML मध्ये लिहिल्या जातात.

MCP Server साठी रेट लिमिटिंग कशी सेट करायची ते इथे दाखवले आहे:

1. पोर्टलमध्ये APIs अंतर्गत **MCP Servers** निवडा.

1. तयार केलेला MCP सर्व्हर निवडा.

1. डाव्या मेनूमध्ये MCP अंतर्गत **Policies** निवडा.

1. पॉलिसी एडिटरमध्ये तुम्हाला हवी असलेली पॉलिसी जोडा किंवा संपादित करा जी MCP सर्व्हरच्या टूल्सवर लागू करायची आहे. पॉलिसी XML फॉरमॅटमध्ये असते. उदाहरणार्थ, तुम्ही एक पॉलिसी जोडू शकता जी MCP सर्व्हरच्या टूल्सवर कॉल्स मर्यादित करते (या उदाहरणात, प्रति क्लायंट IP पत्त्यावर ३० सेकंदांत ५ कॉल्स). खालील XML रेट लिमिटिंग करेल:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    पॉलिसी एडिटरचा एक स्क्रीनशॉट:

    ![पॉलिसी एडिटर](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## वापरून पाहा

आपला MCP Server अपेक्षेनुसार काम करत आहे का ते तपासूया.

यासाठी आपण Visual Studio Code आणि GitHub Copilot चे Agent मोड वापरणार आहोत. आपण MCP सर्व्हर *mcp.json* मध्ये जोडू. त्यामुळे Visual Studio Code एजंटिक क्षमतांसह क्लायंट म्हणून काम करेल आणि अंतिम वापरकर्ते प्रॉम्प्ट टाइप करून त्या सर्व्हरशी संवाद साधू शकतील.

Visual Studio Code मध्ये MCP सर्व्हर कसा जोडायचा ते पाहू:

1. Command Palette मधून MCP: **Add Server command** वापरा.

1. विचारल्यावर, सर्व्हर प्रकार निवडा: **HTTP (HTTP किंवा Server Sent Events)**.

1. API Management मधील MCP सर्व्हरचा URL प्रविष्ट करा. उदाहरण: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (SSE endpoint साठी) किंवा **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (MCP endpoint साठी), ट्रान्सपोर्टमधील फरक `/sse` or `/mcp` ह्याप्रमाणे आहे.

1. तुमच्या पसंतीनुसार एक सर्व्हर ID द्या. हे फार महत्वाचे नाही पण तुम्हाला हा सर्व्हर ओळखायला मदत करेल.

1. कॉन्फिगरेशन workspace settings किंवा user settings मध्ये जतन करण्याचा पर्याय निवडा.

  - **Workspace settings** - सर्व्हर कॉन्फिगरेशन सध्या चालू workspace मधील .vscode/mcp.json फाइलमध्ये जतन होईल.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    किंवा जर तुम्ही streaming HTTP ट्रान्सपोर्ट निवडले तर थोडा वेगळा असेल:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **User settings** - सर्व्हर कॉन्फिगरेशन तुमच्या जागतिक *settings.json* फाइलमध्ये जोडले जाईल आणि सर्व workspace मध्ये उपलब्ध राहील. कॉन्फिगरेशन खालीलप्रमाणे दिसेल:

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. तुम्हाला Azure API Management कडे योग्य प्रकारे प्रमाणीकरण करण्यासाठी एक हेडर देखील जोडावा लागेल. हे हेडर **Ocp-Apim-Subscription-Key** नावाचे असते.

    - सेटिंग्जमध्ये ते कसे जोडायचे:

    ![प्रमाणीकरणासाठी हेडर जोडणे](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png)  
    यामुळे API कीसाठी एक प्रॉम्प्ट दिसेल, जी तुम्ही Azure Portal मधून तुमच्या Azure API Management इंस्टन्ससाठी मिळवू शकता.

    - *mcp.json* मध्ये जोडायचे असल्यास, अशाप्रकारे करा:

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

### Agent मोड वापरा

आता आपण सेटिंग्जमध्ये किंवा *.vscode/mcp.json* मध्ये सगळं सेटअप केलं आहे. वापरून पाहूया.

तुमच्या सर्व्हरकडून उघड केलेले टूल्स अशी टूल्स आयकॉन दिसेल:

![सर्व्हरचे टूल्स](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. टूल्स आयकॉन क्लिक करा आणि टूल्सची यादी दिसेल:

    ![टूल्स](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. टूल invoke करण्यासाठी चॅटमध्ये प्रॉम्प्ट टाका. उदाहरणार्थ, जर तुम्ही ऑर्डर बद्दल माहिती मिळवण्याचा टूल निवडला असेल तर एजंटला ऑर्डरबाबत विचारा. एक उदाहरण प्रॉम्प्ट:

    ```text
    get information from order 2
    ```

    तुम्हाला आता टूल्स आयकॉनसह एक सूचना दिसेल ज्यात टूल कॉल करण्यासाठी विचारले जाईल. टूल चालू ठेवण्यासाठी निवडा, तुम्हाला खालीलप्रमाणे आउटपुट दिसेल:

    ![प्रॉम्प्टचा परिणाम](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **वरील उत्तर तुम्ही सेट केलेल्या टूल्सवर अवलंबून असेल, पण कल्पना अशी की तुम्हाला मजकूर स्वरूपात प्रतिसाद मिळेल**

## संदर्भ

अधिक जाणून घेण्यासाठी:

- [Azure API Management आणि MCP वर ट्यूटोरियल](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python नमुना: Azure API Management वापरून सुरक्षित रिमोट MCP सर्व्हर्स (प्रायोगिक)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP क्लायंट अधिकृतता लॅब](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [VS Code साठी Azure API Management विस्तार वापरून API आयात आणि व्यवस्थापन](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Azure API Center मध्ये रिमोट MCP सर्व्हर्स नोंदणी आणि शोध](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Azure API Management सह अनेक AI क्षमता दाखवणारे उत्कृष्ट रेपो
- [AI Gateway वर्कशॉप्स](https://azure-samples.github.io/AI-Gateway/) Azure Portal वापरून वर्कशॉप्स, AI क्षमतांचा आढावा घेण्यासाठी उत्तम मार्ग

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा अचूकतेच्या त्रुटी असू शकतात. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीकरिता व्यावसायिक मानवी अनुवाद शिफारसीय आहे. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थलागी आम्ही जबाबदार नाही.