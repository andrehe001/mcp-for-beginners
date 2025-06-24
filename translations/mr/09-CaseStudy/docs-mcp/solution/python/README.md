<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:28:25+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "mr"
}
-->
# Chainlit आणि Microsoft Learn Docs MCP सह अभ्यास योजना जनरेटर

## आवश्यक पूर्वतयारी

- Python 3.8 किंवा त्याहून अधिक आवृत्ती
- pip (Python पॅकेज मॅनेजर)
- Microsoft Learn Docs MCP सर्व्हरशी कनेक्ट होण्यासाठी इंटरनेट कनेक्शन

## स्थापना

1. हा रेपॉजिटरी क्लोन करा किंवा प्रोजेक्ट फाइल्स डाउनलोड करा.
2. आवश्यक असलेल्या अवलंबनांची स्थापना करा:

   ```bash
   pip install -r requirements.txt
   ```

## वापर

### परिस्थिती 1: Docs MCP साठी सोपा प्रश्न
एक कमांड-लाइन क्लायंट जो Docs MCP सर्व्हरशी कनेक्ट होतो, प्रश्न पाठवतो आणि निकाल दाखवतो.

1. स्क्रिप्ट चालवा:
   ```bash
   python scenario1.py
   ```
2. प्रॉम्प्टवर तुमचा दस्तऐवज प्रश्न टाका.

### परिस्थिती 2: अभ्यास योजना जनरेटर (Chainlit वेब अ‍ॅप)
Chainlit वापरून वेब-आधारित इंटरफेस जे वापरकर्त्यांना कोणत्याही तांत्रिक विषयासाठी वैयक्तिकृत, आठवड्यांनिहाय अभ्यास योजना तयार करण्याची परवानगी देते.

1. Chainlit अ‍ॅप सुरू करा:
   ```bash
   chainlit run scenario2.py
   ```
2. तुमच्या टर्मिनलमध्ये दिलेला स्थानिक URL (उदा., http://localhost:8000) तुमच्या ब्राउझरमध्ये उघडा.
3. चॅट विंडोमध्ये तुमचा अभ्यास विषय आणि तुम्हाला किती आठवडे अभ्यास करायचा आहे ते लिहा (उदा., "AI-900 certification, 8 weeks").
4. अ‍ॅप आठवड्यांनिहाय अभ्यास योजना तयार करेल, ज्यात संबंधित Microsoft Learn दस्तऐवजांचे दुवे असतील.

**आवश्यक पर्यावरणीय चल:**

परिस्थिती 2 (Azure OpenAI सह Chainlit वेब अ‍ॅप) वापरण्यासाठी, तुम्हाला `.env` file in the `python` फोल्डरमध्ये खालील पर्यावरणीय चल सेट करावे लागतील:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

अ‍ॅप चालवण्यापूर्वी या मूल्यांमध्ये तुमचे Azure OpenAI संसाधन तपशील भरा.

> **टीप:** तुम्ही सहजपणे [Azure AI Foundry](https://ai.azure.com/) वापरून तुमची स्वतःची मॉडेल्स डिप्लॉय करू शकता.

### परिस्थिती 3: VS Code मध्ये MCP सर्व्हरसह इन-एडिटर Docs

ब्राउझर टॅब स्विच न करता, तुम्ही Microsoft Learn Docs थेट तुमच्या VS Code मध्ये MCP सर्व्हर वापरून आणू शकता. यामुळे तुम्हाला:
- VS Code मध्येच डॉक्युमेंटेशन शोधणे आणि वाचणे शक्य होते, कोडिंग वातावरण सोडण्याची गरज नाही.
- README किंवा कोर्स फाइल्समध्ये थेट संदर्भ दुवे समाविष्ट करता येतात.
- GitHub Copilot आणि MCP एकत्र वापरून एक अखंड, AI-शक्तीने चालणारा डॉक्युमेंटेशन वर्कफ्लो मिळतो.

**उदाहरण वापर:**
- कोर्स किंवा प्रोजेक्ट डॉक्युमेंटेशन लिहिताना README मध्ये जलद संदर्भ दुवे जोडणे.
- Copilot वापरून कोड जनरेट करा आणि MCP वापरून तत्काळ संबंधित डॉक्युमेंटेशन शोधा आणि उद्धृत करा.
- तुमच्या एडिटरमध्ये लक्ष केंद्रित ठेवा आणि उत्पादनक्षमता वाढवा.

> [!IMPORTANT]
> सुनिश्चित करा की तुमच्याकडे वैध [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

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

हे उदाहरण वेगवेगळ्या शिकण्याच्या उद्दिष्टांसाठी आणि कालावधींसाठी अ‍ॅपची लवचीकता दर्शवितात.

## संदर्भ

- [Chainlit Documentation](https://docs.chainlit.io/)
- [MCP Documentation](https://github.com/MicrosoftDocs/mcp)

**अस्वीकरण**:  
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) चा वापर करून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये चुका किंवा असमर्थता असू शकते. मूळ दस्तऐवज त्याच्या स्थानिक भाषेत अधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानवी अनुवाद करण्याची शिफारस केली जाते. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुती किंवा चुकीच्या अर्थ लावण्याबद्दल आम्ही जबाबदार नाही.