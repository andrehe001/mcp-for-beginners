<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "36de9fae488d6de554d969fe8e0801a8",
  "translation_date": "2025-06-20T19:16:40+00:00",
  "source_file": "09-CaseStudy/apimsample.md",
  "language_code": "hi"
}
-->
# केस स्टडी: API Management में REST API को MCP सर्वर के रूप में एक्सपोज़ करें

Azure API Management एक सेवा है जो आपके API Endpoints के ऊपर एक Gateway प्रदान करती है। इसका काम इस तरह होता है कि Azure API Management आपके APIs के सामने एक प्रॉक्सी की तरह काम करता है और यह तय कर सकता है कि आने वाले अनुरोधों के साथ क्या करना है।

इसे इस्तेमाल करके, आप कई सुविधाएँ जोड़ सकते हैं जैसे:

- **सुरक्षा**, आप API keys, JWT से लेकर managed identity तक सब कुछ इस्तेमाल कर सकते हैं।
- **रेट लिमिटिंग**, एक बेहतरीन फीचर जो यह तय करने में मदद करता है कि एक निश्चित समय में कितने कॉल्स गुजर सकते हैं। इससे सभी उपयोगकर्ताओं को बेहतर अनुभव मिलता है और आपकी सेवा पर अत्यधिक अनुरोधों का दबाव नहीं पड़ता।
- **स्केलिंग और लोड बैलेंसिंग**। आप कई endpoints सेट कर सकते हैं ताकि लोड बैलेंस हो सके और यह भी तय कर सकते हैं कि "लोड बैलेंस" कैसे होगा।
- **AI फीचर्स जैसे semantic caching**, टोकन लिमिट और टोकन मॉनिटरिंग आदि। ये शानदार फीचर्स प्रतिक्रियाशीलता बढ़ाते हैं और आपके टोकन खर्च पर नियंत्रण रखने में मदद करते हैं। [यहाँ और पढ़ें](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities)।

## MCP + Azure API Management क्यों?

Model Context Protocol तेजी से एजेंटिक AI ऐप्स के लिए एक मानक बनता जा रहा है और टूल्स तथा डेटा को एक सुसंगत तरीके से एक्सपोज़ करने का तरीका है। जब आपको APIs को "मैनेज" करना होता है तो Azure API Management एक स्वाभाविक विकल्प है। MCP Servers अक्सर अन्य APIs के साथ इंटीग्रेट होते हैं ताकि टूल के लिए अनुरोधों को हल किया जा सके। इसलिए Azure API Management और MCP को मिलाना बहुत तार्किक है।

## अवलोकन

इस खास उपयोग मामले में हम सीखेंगे कि API endpoints को MCP Server के रूप में कैसे एक्सपोज़ किया जाए। ऐसा करके, हम इन endpoints को आसानी से एक एजेंटिक ऐप का हिस्सा बना सकते हैं और साथ ही Azure API Management की सुविधाओं का भी लाभ उठा सकते हैं।

## मुख्य विशेषताएँ

- आप उन endpoint मेथड्स को चुनते हैं जिन्हें आप टूल्स के रूप में एक्सपोज़ करना चाहते हैं।
- आपको जो अतिरिक्त सुविधाएँ मिलती हैं वह इस बात पर निर्भर करती हैं कि आप अपनी API के पॉलिसी सेक्शन में क्या कॉन्फ़िगर करते हैं। लेकिन यहाँ हम आपको दिखाएंगे कि आप रेट लिमिटिंग कैसे जोड़ सकते हैं।

## पूर्व-चरण: API इम्पोर्ट करें

अगर आपके पास पहले से Azure API Management में API है तो बहुत अच्छा, आप यह चरण छोड़ सकते हैं। यदि नहीं, तो इस लिंक को देखें, [Azure API Management में API इम्पोर्ट करना](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api)।

## API को MCP Server के रूप में एक्सपोज़ करें

API endpoints को एक्सपोज़ करने के लिए, निम्न चरणों का पालन करें:

1. Azure पोर्टल पर जाएं और इस पते पर जाएं <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
अपने API Management इंस्टेंस पर जाएं।

1. बाएं मेनू में, APIs > MCP Servers > + Create new MCP Server चुनें।

1. API में, एक REST API चुनें जिसे MCP सर्वर के रूप में एक्सपोज़ करना है।

1. एक या अधिक API Operations चुनें जिन्हें टूल्स के रूप में एक्सपोज़ करना है। आप सभी ऑपरेशन्स या केवल कुछ विशेष ऑपरेशन्स चुन सकते हैं।

    ![Select methods to expose](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. **Create** पर क्लिक करें।

1. मेनू विकल्प **APIs** और **MCP Servers** पर जाएं, आपको निम्न दिखाई देगा:

    ![See the MCP Server in the main pane](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP सर्वर बन गया है और API ऑपरेशन्स टूल्स के रूप में एक्सपोज़ हो गए हैं। MCP सर्वर MCP Servers पेन में सूचीबद्ध है। URL कॉलम में MCP सर्वर का endpoint दिखाया गया है जिसे आप परीक्षण या क्लाइंट एप्लिकेशन में कॉल कर सकते हैं।

## वैकल्पिक: पॉलिसी कॉन्फ़िगर करें

Azure API Management में पॉलिसी की मुख्य अवधारणा होती है जहाँ आप अपने endpoints के लिए विभिन्न नियम सेट करते हैं, जैसे कि रेट लिमिटिंग या semantic caching। ये पॉलिसी XML में लिखी जाती हैं।

यहाँ बताया गया है कि आप MCP Server के लिए रेट लिमिटिंग पॉलिसी कैसे सेट कर सकते हैं:

1. पोर्टल में, APIs के अंतर्गत, **MCP Servers** चुनें।

1. अपने बनाए हुए MCP सर्वर को चुनें।

1. बाएं मेनू में, MCP के अंतर्गत, **Policies** चुनें।

1. पॉलिसी एडिटर में, वे पॉलिसी जोड़ें या संपादित करें जिन्हें आप MCP सर्वर के टूल्स पर लागू करना चाहते हैं। पॉलिसी XML फॉर्मेट में होती हैं। उदाहरण के लिए, आप एक पॉलिसी जोड़ सकते हैं जो MCP सर्वर के टूल्स के कॉल्स को सीमित करती है (इस उदाहरण में, प्रति क्लाइंट IP पते 30 सेकंड में 5 कॉल)। यह XML रेट लिमिट लागू करेगा:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    पॉलिसी एडिटर का एक चित्र यहाँ है:

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## इसे आज़माएं

आइए सुनिश्चित करें कि हमारा MCP Server सही तरीके से काम कर रहा है।

इसके लिए, हम Visual Studio Code और GitHub Copilot के Agent मोड का उपयोग करेंगे। हम MCP सर्वर को *mcp.json* में जोड़ेंगे। ऐसा करने से, Visual Studio Code एजेंटिक क्षमताओं वाला एक क्लाइंट के रूप में काम करेगा और अंतिम उपयोगकर्ता प्रॉम्प्ट टाइप करके सर्वर के साथ इंटरैक्ट कर सकेंगे।

Visual Studio Code में MCP सर्वर जोड़ने का तरीका:

1. कमांड पैलेट से MCP: **Add Server कमांड** का उपयोग करें।

1. जब पूछा जाए, तो सर्वर प्रकार चुनें: **HTTP (HTTP या Server Sent Events)**।

1. API Management में MCP सर्वर का URL दर्ज करें। उदाहरण: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (SSE endpoint के लिए) या **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (MCP endpoint के लिए), ध्यान दें कि ट्रांसपोर्ट में अंतर `/sse` or `/mcp` है।

1. अपनी पसंद का एक सर्वर ID दर्ज करें। यह कोई महत्वपूर्ण मान नहीं है लेकिन इससे आपको यह याद रखने में मदद मिलेगी कि यह सर्वर इंस्टेंस क्या है।

1. चुनें कि आप कॉन्फ़िगरेशन को वर्कस्पेस सेटिंग्स में सेव करना चाहते हैं या यूजर सेटिंग्स में।

  - **वर्कस्पेस सेटिंग्स** - सर्वर कॉन्फ़िगरेशन केवल वर्तमान वर्कस्पेस में उपलब्ध .vscode/mcp.json फ़ाइल में सेव होती है।

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    या अगर आप स्ट्रीमिंग HTTP को ट्रांसपोर्ट के रूप में चुनते हैं तो यह थोड़ा अलग होगा:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **यूजर सेटिंग्स** - सर्वर कॉन्फ़िगरेशन आपकी ग्लोबल *settings.json* फ़ाइल में जुड़ जाती है और सभी वर्कस्पेस में उपलब्ध होती है। कॉन्फ़िगरेशन कुछ इस तरह दिखती है:

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. आपको एक हेडर भी जोड़ना होगा ताकि यह सही तरीके से Azure API Management के साथ प्रमाणीकरण कर सके। यह एक हेडर का उपयोग करता है जिसका नाम **Ocp-Apim-Subscription-Key** है।

    - इसे सेटिंग्स में जोड़ने का तरीका:

    ![Adding header for authentication](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), इससे एक प्रॉम्प्ट आएगा जो आपसे API key का मान पूछेगा जिसे आप Azure Portal में अपने Azure API Management इंस्टेंस के लिए पा सकते हैं।

   - इसे *mcp.json* में जोड़ने के लिए, आप इसे इस तरह जोड़ सकते हैं:

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

### एजेंट मोड का उपयोग करें

अब हम सेटिंग्स में या *.vscode/mcp.json* में तैयार हैं। आइए इसे आज़माएं।

टूल्स आइकन ऐसा दिखना चाहिए, जहाँ आपके सर्वर के एक्सपोज़ किए गए टूल्स सूचीबद्ध होंगे:

![Tools from the server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. टूल्स आइकन पर क्लिक करें और आपको टूल्स की सूची दिखेगी:

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. चैट में प्रॉम्प्ट दर्ज करें ताकि टूल को कॉल किया जा सके। उदाहरण के लिए, अगर आपने एक टूल चुना है जो किसी ऑर्डर की जानकारी देता है, तो आप एजेंट से ऑर्डर के बारे में पूछ सकते हैं। यहाँ एक उदाहरण प्रॉम्प्ट है:

    ```text
    get information from order 2
    ```

    अब आपको टूल्स आइकन दिखाई देगा जो आपसे टूल कॉल करने के लिए पूछेगा। जारी रखने के लिए चुनें, आपको आउटपुट कुछ इस तरह दिखेगा:

    ![Result from prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **आप जो ऊपर देख रहे हैं वह इस बात पर निर्भर करता है कि आपने कौन से टूल्स सेटअप किए हैं, लेकिन मूल विचार यह है कि आपको ऊपर की तरह टेक्स्टुअल प्रतिक्रिया मिले।**

## संदर्भ

यहाँ से आप और अधिक सीख सकते हैं:

- [Azure API Management और MCP पर ट्यूटोरियल](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python नमूना: Azure API Management का उपयोग करके सुरक्षित रिमोट MCP सर्वर (प्रायोगिक)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP क्लाइंट ऑथराइजेशन लैब](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [VS Code के लिए Azure API Management एक्सटेंशन का उपयोग करके APIs इम्पोर्ट और मैनेज करें](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Azure API Center में रिमोट MCP सर्वर रजिस्टर और डिस्कवर करें](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) एक शानदार रिपोज़िटरी जो Azure API Management के साथ कई AI क्षमताएं दिखाती है
- [AI Gateway वर्कशॉप्स](https://azure-samples.github.io/AI-Gateway/) Azure Portal का उपयोग करते हुए वर्कशॉप्स, जो AI क्षमताओं का मूल्यांकन शुरू करने का एक बढ़िया तरीका है।

**अस्वीकरण**:  
इस दस्तावेज़ का अनुवाद एआई अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।