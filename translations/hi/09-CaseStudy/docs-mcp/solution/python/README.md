<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:28:02+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "hi"
}
-->
# Study Plan Generator with Chainlit & Microsoft Learn Docs MCP

## आवश्यकताएँ

- Python 3.8 या उससे ऊपर का संस्करण
- pip (Python पैकेज मैनेजर)
- Microsoft Learn Docs MCP सर्वर से कनेक्ट करने के लिए इंटरनेट कनेक्शन

## इंस्टॉलेशन

1. इस रिपॉजिटरी को क्लोन करें या प्रोजेक्ट फाइलें डाउनलोड करें।
2. आवश्यक डिपेंडेंसिस इंस्टॉल करें:

   ```bash
   pip install -r requirements.txt
   ```

## उपयोग

### परिदृश्य 1: Docs MCP के लिए साधारण क्वेरी  
एक कमांड-लाइन क्लाइंट जो Docs MCP सर्वर से जुड़ता है, क्वेरी भेजता है, और परिणाम प्रिंट करता है।

1. स्क्रिप्ट चलाएं:  
   ```bash
   python scenario1.py
   ```  
2. प्रॉम्प्ट पर अपनी डॉक्यूमेंटेशन से जुड़ा सवाल दर्ज करें।

### परिदृश्य 2: स्टडी प्लान जनरेटर (Chainlit वेब ऐप)  
एक वेब-आधारित इंटरफ़ेस (Chainlit का उपयोग करके) जो उपयोगकर्ताओं को किसी भी तकनीकी विषय के लिए व्यक्तिगत, सप्ताह-दर-सप्ताह अध्ययन योजना बनाने की सुविधा देता है।

1. Chainlit ऐप शुरू करें:  
   ```bash
   chainlit run scenario2.py
   ```  
2. अपने टर्मिनल में दिखाए गए लोकल URL (जैसे http://localhost:8000) को ब्राउज़र में खोलें।  
3. चैट विंडो में अपना अध्ययन विषय और अध्ययन के सप्ताहों की संख्या दर्ज करें (जैसे, "AI-900 certification, 8 weeks")।  
4. ऐप सप्ताह-दर-सप्ताह अध्ययन योजना के साथ जवाब देगा, जिसमें संबंधित Microsoft Learn डॉक्यूमेंटेशन के लिंक शामिल होंगे।

**आवश्यक पर्यावरण चर:**  

परिदृश्य 2 (Azure OpenAI के साथ Chainlit वेब ऐप) का उपयोग करने के लिए, आपको `.env` file in the `python` डायरेक्टरी में निम्नलिखित पर्यावरण चर सेट करने होंगे:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

ऐप चलाने से पहले इन मानों को अपने Azure OpenAI रिसोर्स विवरण से भरें।

> **Tip:** आप आसानी से अपने मॉडल [Azure AI Foundry](https://ai.azure.com/) का उपयोग करके तैनात कर सकते हैं।

### परिदृश्य 3: VS Code में MCP सर्वर के साथ इन-एडिटर डॉक्यूमेंटेशन  

ब्राउज़र टैब बदलने के बजाय, आप Microsoft Learn Docs को सीधे अपने VS Code में MCP सर्वर के माध्यम से ला सकते हैं। इससे आप:  
- VS Code के अंदर ही डॉक्यूमेंटेशन खोज और पढ़ सकते हैं बिना अपने कोडिंग वातावरण छोड़े।  
- डॉक्यूमेंटेशन का संदर्भ लें और सीधे अपने README या कोर्स फाइलों में लिंक डालें।  
- GitHub Copilot और MCP का एक साथ उपयोग करके सहज, AI-संचालित डॉक्यूमेंटेशन वर्कफ़्लो का आनंद लें।

**उदाहरण उपयोग के मामले:**  
- कोर्स या प्रोजेक्ट डॉक्यूमेंटेशन लिखते समय README में जल्दी से संदर्भ लिंक जोड़ना।  
- कोड जनरेट करने के लिए Copilot और संबंधित डॉक्यूमेंटेशन खोजने के लिए MCP का उपयोग करना।  
- अपने एडिटर में ध्यान केंद्रित रहना और उत्पादकता बढ़ाना।

> [!IMPORTANT]  
> सुनिश्चित करें कि आपके पास एक वैध [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

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

ये उदाहरण ऐप की लचीलापन को विभिन्न सीखने के उद्देश्यों और समय सीमाओं के लिए दर्शाते हैं।

## संदर्भ

- [Chainlit Documentation](https://docs.chainlit.io/)  
- [MCP Documentation](https://github.com/MicrosoftDocs/mcp)

**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवादों में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़ अपनी मूल भाषा में प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।