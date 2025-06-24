<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "36de9fae488d6de554d969fe8e0801a8",
  "translation_date": "2025-06-20T19:17:41+00:00",
  "source_file": "09-CaseStudy/apimsample.md",
  "language_code": "ne"
}
-->
# केस स्टडी: API Management मा REST API लाई MCP सर्भरको रूपमा एक्स्पोज गर्नुहोस्

Azure API Management एउटा सेवा हो जसले तपाईंको API Endpoints माथि गेटवे प्रदान गर्छ। यसको काम Azure API Management ले तपाईंको APIs को अगाडि प्रोक्सी जस्तै काम गर्छ र आउने अनुरोधहरूसँग के गर्ने भनेर निर्णय गर्न सक्छ।

यसलाई प्रयोग गरेर, तपाईं धेरै सुविधाहरू थप्न सक्नुहुन्छ जस्तै:

- **सुरक्षा**, तपाईं API कुञ्जीहरू, JWT देखि Managed Identity सम्म सबै कुरा प्रयोग गर्न सक्नुहुन्छ।
- **रेट लिमिटिङ**, एउटा राम्रो सुविधा हो जुन तपाईंले कति कलहरू एक निश्चित समय एकाइमा जान पाउने निर्धारण गर्न सक्नुहुन्छ। यसले सबै प्रयोगकर्ताहरूलाई राम्रो अनुभव सुनिश्चित गर्न मद्दत गर्छ र तपाईंको सेवा अनुरोधहरूले ओभरलोड नहोस भनेर पनि सुनिश्चित गर्छ।
- **स्केलिङ र लोड बैलेन्सिङ**। तपाईं धेरै endpoints सेटअप गरेर लोड सन्तुलन गर्न सक्नुहुन्छ र "लोड बैलेन्स" कसरी गर्ने पनि निर्धारण गर्न सक्नुहुन्छ।
- **AI सुविधाहरू जस्तै सेम्यान्टिक क्याचिङ**, टोकन सीमा र टोकन निगरानी आदि। यी उत्कृष्ट सुविधाहरूले प्रतिक्रिया समय सुधार्छन् र तपाईंलाई टोकन खर्चको व्यवस्थापनमा मद्दत गर्छन्। [यहाँ थप पढ्नुहोस्](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities)।

## किन MCP + Azure API Management?

Model Context Protocol छिट्टै एजेन्टिक AI एपहरूको लागि मानक बन्ने क्रममा छ र उपकरणहरू र डाटालाई सुसंगत तरिकाले एक्स्पोज गर्ने तरिका हो। Azure API Management API हरूलाई "व्यवस्थापन" गर्नको लागि स्वाभाविक विकल्प हो। MCP सर्भरहरू प्रायः अन्य APIs सँग एकीकृत हुन्छन् ताकि अनुरोधहरूलाई उपकरणसम्म समाधान गर्न सकियोस्। त्यसैले Azure API Management र MCP लाई मिलाएर प्रयोग गर्नु धेरै अर्थपूर्ण छ।

## अवलोकन

यस विशेष केसमा हामी API endpoints लाई MCP सर्भरको रूपमा एक्स्पोज गर्न सिक्नेछौं। यसले हामीलाई यी endpoints लाई एजेन्टिक एपको हिस्सा बनाउन सजिलो बनाउँछ र Azure API Management का सुविधाहरू पनि उपयोग गर्न सकिन्छ।

## मुख्य सुविधाहरू

- तपाईंले कुन endpoint मेथडहरूलाई उपकरणको रूपमा एक्स्पोज गर्न चाहनुहुन्छ चयन गर्नुहुन्छ।
- थप सुविधाहरू तपाईंले API को नीति सेक्सनमा के कन्फिगर गर्नुभयो त्यसमा निर्भर हुन्छ। यहाँ हामी कसरी रेट लिमिटिङ थप्ने देखाउनेछौं।

## पूर्व-चरण: API आयात गर्नुहोस्

यदि तपाईंको Azure API Management मा पहिले नै API छ भने यो चरण छोड्न सक्नुहुन्छ। छैन भने, यो लिंक हेर्नुहोस्, [Azure API Management मा API आयात गर्ने](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api)।

## API लाई MCP सर्भरको रूपमा एक्स्पोज गर्नुहोस्

API endpoints एक्स्पोज गर्न तलका चरणहरू पालना गरौं:

1. Azure Portal मा जानुहोस् र यो ठेगाना खोल्नुहोस् <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
तपाईंको API Management इन्स्ट्यान्समा जानुहोस्।

1. बायाँ मेनुमा, APIs > MCP Servers > + Create new MCP Server चयन गर्नुहोस्।

1. API मा, REST API चयन गर्नुहोस् जुन MCP सर्भरको रूपमा एक्स्पोज गर्न चाहनुहुन्छ।

1. एक वा बढी API अपरेशन्स चयन गर्नुहोस् जुन उपकरणको रूपमा एक्स्पोज गर्ने। तपाईं सबै अपरेशन्स वा केही मात्र चयन गर्न सक्नुहुन्छ।

    ![Select methods to expose](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. **Create** मा क्लिक गर्नुहोस्।

1. मेनु विकल्प **APIs** र **MCP Servers** मा जानुहोस्, तपाईंले तलको देख्नुहुनेछ:

    ![See the MCP Server in the main pane](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP सर्भर सिर्जना भइसकेको छ र API अपरेशन्स उपकरणको रूपमा एक्स्पोज गरिएको छ। MCP सर्भर MCP Servers पेनमा सूचीबद्ध छ। URL स्तम्भले MCP सर्भरको endpoint देखाउँछ जुन तपाईं परीक्षण वा क्लाइन्ट एप्लिकेशन भित्र कल गर्न सक्नुहुन्छ।

## वैकल्पिक: नीतिहरू कन्फिगर गर्नुहोस्

Azure API Management मा नीतिहरूको मूल अवधारणा हुन्छ जहाँ तपाईं विभिन्न नियमहरू सेटअप गर्न सक्नुहुन्छ, जस्तै रेट लिमिटिङ वा सेम्यान्टिक क्याचिङ। यी नीतिहरू XML मा लेखिन्छन्।

यहाँ कसरी तपाईं आफ्नो MCP सर्भरको रेट लिमिट गर्न नीति सेटअप गर्ने देखाइएको छ:

1. पोर्टलमा, APIs अन्तर्गत, **MCP Servers** चयन गर्नुहोस्।

1. तपाईंले सिर्जना गरेको MCP सर्भर चयन गर्नुहोस्।

1. बायाँ मेनुमा, MCP अन्तर्गत **Policies** चयन गर्नुहोस्।

1. नीति सम्पादकमा, तपाईंले MCP सर्भरका उपकरणहरूमा लागू गर्न चाहने नीतिहरू थप्नुहोस् वा सम्पादन गर्नुहोस्। नीतिहरू XML ढाँचामा परिभाषित हुन्छन्। उदाहरणका लागि, तपाईं MCP सर्भरका उपकरणहरूमा कलहरू सीमित गर्ने नीति थप्न सक्नुहुन्छ (यस उदाहरणमा, प्रत्येक क्लाइन्ट IP ठेगानाका लागि ३० सेकेन्डमा ५ कलहरू)। यसले रेट लिमिट गर्ने XML कोड यस्तो हुनेछ:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    नीति सम्पादकको तस्वीर:

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## प्रयास गर्नुहोस्

हामीले बनाएको MCP सर्भर ठीकसँग काम गरिरहेको छ कि छैन जाँचौं।

यसका लागि हामी Visual Studio Code र GitHub Copilot को Agent मोड प्रयोग गर्नेछौं। हामी MCP सर्भरलाई *mcp.json* मा थप्नेछौं। यसरी गर्दा, Visual Studio Code एजेन्टिक क्षमताहरू भएको क्लाइन्टको रूपमा काम गर्नेछ र अन्तिम प्रयोगकर्ताहरूले प्रॉम्प्ट टाइप गरेर उक्त सर्भरसँग अन्तरक्रिया गर्न सक्नेछन्।

Visual Studio Code मा MCP सर्भर कसरी थप्ने:

1. Command Palette बाट MCP: **Add Server कमाण्ड प्रयोग गर्नुहोस्**।

1. जब सोधिन्छ, सर्भर प्रकार चयन गर्नुहोस्: **HTTP (HTTP वा Server Sent Events)**।

1. API Management मा रहेको MCP सर्भरको URL प्रविष्ट गर्नुहोस्। उदाहरण: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (SSE endpoint का लागि) वा **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (MCP endpoint का लागि), यहाँ ट्रान्सपोर्ट बीचको फरक `/sse` or `/mcp` हो।

1. आफ्नो रोजाइको सर्भर ID प्रविष्ट गर्नुहोस्। यो महत्वपूर्ण मान होइन तर यसले तपाईंलाई सर्भर इन्स्ट्यान्स सम्झन मद्दत गर्छ।

1. कन्फिगरेसन तपाईँको workspace सेटिङ्स वा user सेटिङ्समा सेभ गर्ने विकल्प चयन गर्नुहोस्।

  - **Workspace सेटिङ्स** - सर्भर कन्फिगरेसन केवल वर्तमान workspace मा उपलब्ध .vscode/mcp.json फाइलमा सेभ हुन्छ।

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    वा यदि तपाईंले स्ट्रिमिङ HTTP ट्रान्सपोर्ट चयन गर्नुभयो भने यो अलिक फरक हुनेछ:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **User सेटिङ्स** - सर्भर कन्फिगरेसन तपाईंको ग्लोबल *settings.json* फाइलमा थपिन्छ र सबै workspace हरूमा उपलब्ध हुन्छ। कन्फिगरेसन यस्तो देखिन्छ:

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. तपाईंले Azure API Management तर्फ सही प्रमाणिकरण सुनिश्चित गर्न हेडर पनि थप्नुपर्नेछ। यसका लागि **Ocp-Apim-Subscription-Key** नामक हेडर प्रयोग हुन्छ।

    - यसलाई सेटिङ्समा थप्ने तरिका:

    ![Adding header for authentication](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), यसले API कुञ्जीको मान सोध्ने प्रॉम्प्ट देखाउनेछ जुन तपाईं Azure Portal मा आफ्नो Azure API Management इन्स्ट्यान्सका लागि पाउन सक्नुहुन्छ।

   - *mcp.json* मा थप्न चाहनुहुन्छ भने यसरी थप्न सक्नुहुन्छ:

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

### Agent मोड प्रयोग गर्नुहोस्

अब हामी सेटिङ्स वा *.vscode/mcp.json* मा सबै तयार छौं। प्रयास गरौं।

त्यहाँ यस्तो Tools आइकन देखिनुपर्छ, जहाँ तपाईंको सर्भरबाट एक्स्पोज गरिएका उपकरणहरू सूचीबद्ध हुन्छन्:

![Tools from the server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Tools आइकनमा क्लिक गर्नुहोस् र तपाईंलाई उपकरणहरूको सूची देखिनेछ:

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. उपकरण चलाउन च्याटमा प्रॉम्प्ट टाइप गर्नुहोस्। उदाहरणका लागि, यदि तपाईंले अर्डरको बारेमा जानकारी लिन उपकरण चयन गर्नुभयो भने, एजेन्टलाई अर्डरको बारेमा सोध्न सक्नुहुन्छ। यहाँ एउटा उदाहरण प्रॉम्प्ट छ:

    ```text
    get information from order 2
    ```

    अब तपाईंलाई उपकरण कल गर्न जारी राख्न उपकरण आइकन देखाइनेछ। चलाउन चयन गर्नुहोस्, तपाईंले यस्तो आउटपुट देख्नुहुनेछ:

    ![Result from prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **माथि देखाइएको कुरा तपाईंले सेटअप गरेको उपकरणहरूमा निर्भर गर्छ, तर उद्देश्य भनेको तपाईंलाई पाठ आधारित प्रतिक्रिया प्राप्त गर्नु हो।**


## सन्दर्भहरू

यहाँबाट थप सिक्न सक्नुहुन्छ:

- [Azure API Management र MCP मा ट्युटोरियल](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python नमूना: Azure API Management प्रयोग गरी सुरक्षित रिमोट MCP सर्भरहरू (प्रयोगात्मक)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP क्लाइन्ट अधिकार प्रयोगशाला](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [VS Code का लागि Azure API Management एक्सटेन्सन प्रयोग गरेर API आयात र व्यवस्थापन](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Azure API Center मा रिमोट MCP सर्भरहरू दर्ता र पत्ता लगाउने](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Azure API Management सँग धेरै AI क्षमताहरू देखाउने उत्कृष्ट रिपो
- [AI Gateway कार्यशालाहरू](https://azure-samples.github.io/AI-Gateway/) Azure Portal प्रयोग गरेर कार्यशालाहरू, AI क्षमताहरूको मूल्यांकन सुरु गर्न राम्रो तरिका।

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयासरत छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुनसक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनु पर्छ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याको लागि हामी जिम्मेवार हुने छैनौं।