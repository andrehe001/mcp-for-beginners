<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:28:45+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "ne"
}
-->
# Chainlit र Microsoft Learn Docs MCP सँग अध्ययन योजना जनरेटर

## पूर्वशर्तहरू

- Python 3.8 वा माथि
- pip (Python प्याकेज व्यवस्थापक)
- Microsoft Learn Docs MCP सर्भरसँग जडान गर्न इन्टरनेट पहुँच

## स्थापना

1. यो रिपोजिटरी क्लोन गर्नुहोस् वा प्रोजेक्ट फाइलहरू डाउनलोड गर्नुहोस्।
2. आवश्यक निर्भरता स्थापना गर्नुहोस्:

   ```bash
   pip install -r requirements.txt
   ```

## प्रयोग

### परिदृश्य १: Docs MCP लाई सरल प्रश्न

एक कमाण्ड-लाइन क्लाइन्ट जुन Docs MCP सर्भरसँग जडान हुन्छ, प्रश्न पठाउँछ र परिणाम देखाउँछ।

1. स्क्रिप्ट चलाउनुहोस्:
   ```bash
   python scenario1.py
   ```
2. प्रॉम्प्टमा तपाईंको डकुमेन्टेशन प्रश्न टाइप गर्नुहोस्।

### परिदृश्य २: अध्ययन योजना जनरेटर (Chainlit वेब एप)

एक वेब-आधारित इन्टरफेस (Chainlit प्रयोग गरेर) जसले प्रयोगकर्तालाई कुनै पनि प्राविधिक विषयमा व्यक्तिगत, हप्ता-दर-हप्ता अध्ययन योजना बनाउन अनुमति दिन्छ।

1. Chainlit एप सुरु गर्नुहोस्:
   ```bash
   chainlit run scenario2.py
   ```
2. टर्मिनलमा दिइएको स्थानीय URL (जस्तै http://localhost:8000) आफ्नो ब्राउजरमा खोल्नुहोस्।
3. च्याट विन्डोमा आफ्नो अध्ययन विषय र अध्ययन गर्ने हप्ताहरूको संख्या लेख्नुहोस् (जस्तै, "AI-900 certification, 8 weeks")।
4. एपले हप्ता-दर-हप्ता अध्ययन योजना फर्काउनेछ, जसमा सम्बन्धित Microsoft Learn डकुमेन्टेशनका लिंकहरू समावेश छन्।

**आवश्यक वातावरण चरहरू:**

परिदृश्य २ (Azure OpenAI सहित Chainlit वेब एप) प्रयोग गर्न, तपाईंले `.env` file in the `python` फोल्डरमा तलका वातावरण चरहरू सेट गर्नुपर्छ:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

एप चलाउनु अघि यी मानहरू आफ्नो Azure OpenAI स्रोत विवरणहरूसँग भर्नुहोस्।

> **Tip:** तपाईं सजिलै आफ्नै मोडेलहरू [Azure AI Foundry](https://ai.azure.com/) प्रयोग गरेर तैनाथ गर्न सक्नुहुन्छ।

### परिदृश्य ३: VS Code मा MCP सर्भरसँग इन-एडिटर डकुमेन्टेशन

ब्राउजर ट्याब परिवर्तन गरेर डकुमेन्टेशन खोज्ने सट्टा, Microsoft Learn Docs सिधै VS Code मा ल्याउन सकिन्छ MCP सर्भर प्रयोग गरी। यसले तपाईंलाई:
- VS Code भित्रै डकुमेन्टेशन खोज्न र पढ्न सजिलो बनाउँछ, तपाईंको कोडिङ वातावरण छोड्न नपर्ने।
- डकुमेन्टेशन सन्दर्भ र लिंकहरू सिधै README वा कोर्स फाइलहरूमा समावेश गर्न सकिन्छ।
- GitHub Copilot र MCP सँगै प्रयोग गरी सहज, AI-समर्थित डकुमेन्टेशन कार्यप्रवाह बनाउन सकिन्छ।

**उदाहरण प्रयोगहरू:**
- कोर्स वा प्रोजेक्ट डकुमेन्टेशन लेख्दा छिटो सन्दर्भ लिंकहरू README मा थप्ने।
- Copilot प्रयोग गरी कोड जनरेट गर्ने र MCP प्रयोग गरी सम्बन्धित डकुमेन्टेशन तुरुन्त फेला पार्ने र उद्धृत गर्ने।
- सम्पादकमा ध्यान केन्द्रित राख्दै उत्पादकत्व बढाउने।

> [!IMPORTANT]
> कृपया सुनिश्चित गर्नुहोस् कि तपाईंसँग मान्य [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

## Why Chainlit for Scenario 2?

Chainlit is a modern open-source framework for building conversational web applications. It makes it easy to create chat-based user interfaces that connect to backend services like the Microsoft Learn Docs MCP server. This project uses Chainlit to provide a simple, interactive way to generate personalized study plans in real time. By leveraging Chainlit, you can quickly build and deploy chat-based tools that enhance productivity and learning.

## What This Does

This app allows users to create a personalized study plan by simply entering a topic and a duration. The app parses your input, queries the Microsoft Learn Docs MCP server for relevant content, and organizes the results into a structured, week-by-week plan. Each week’s recommendations are displayed in the chat, making it easy to follow and track your progress. The integration ensures you always get the latest, most relevant learning resources.

## Sample Queries

Try these queries in the chat window to see how the app responds:

- `AI-900 certification, 8 weeks`
- `Learn Azure Functions, 4 weeks`
- `Azure DevOps, 6 weeks`
- `Data engineering on Azure, 10 weeks`
- `Microsoft security fundamentals, 5 weeks`
- `Power Platform, 7 weeks`
- `Azure AI services, 12 weeks`
- `Cloud architecture, 9 weeks`

यी उदाहरणहरूले फरक सिकाइ लक्ष्य र समयसीमाहरूका लागि एपको लचकता देखाउँछन्।

## सन्दर्भहरू

- [Chainlit Documentation](https://docs.chainlit.io/)
- [MCP Documentation](https://github.com/MicrosoftDocs/mcp)

**अस्वीकरण**:  
यो दस्तावेज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताको प्रयास गर्छौं, तर कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुन सक्छ। मूल दस्तावेज यसको मूल भाषामा नै अधिकारिक स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीको लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार छैनौं।