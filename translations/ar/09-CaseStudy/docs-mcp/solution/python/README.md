<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:26:38+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "ar"
}
-->
# مولد خطة الدراسة باستخدام Chainlit و Microsoft Learn Docs MCP

## المتطلبات الأساسية

- بايثون 3.8 أو أعلى  
- pip (مدير حزم بايثون)  
- اتصال بالإنترنت للوصول إلى خادم Microsoft Learn Docs MCP  

## التثبيت

1. انسخ هذا المستودع أو قم بتنزيل ملفات المشروع.  
2. ثبّت التبعيات المطلوبة:  

   ```bash
   pip install -r requirements.txt
   ```

## الاستخدام

### السيناريو 1: استعلام بسيط إلى Docs MCP  
عميل سطر أوامر يتصل بخادم Docs MCP، يرسل استعلامًا، ويطبع النتيجة.

1. شغّل السكريبت:  
   ```bash
   python scenario1.py
   ```  
2. أدخل سؤال التوثيق عند المطالبة.

### السيناريو 2: مولد خطة الدراسة (تطبيق ويب Chainlit)  
واجهة ويب (باستخدام Chainlit) تتيح للمستخدمين إنشاء خطة دراسة شخصية أسبوعية لأي موضوع تقني.

1. ابدأ تطبيق Chainlit:  
   ```bash
   chainlit run scenario2.py
   ```  
2. افتح عنوان URL المحلي المعروض في الطرفية (مثل http://localhost:8000) في متصفحك.  
3. في نافذة الدردشة، أدخل موضوع دراستك وعدد الأسابيع التي تريد الدراسة خلالها (مثال: "AI-900 certification, 8 weeks").  
4. سيرد التطبيق بخطة دراسة أسبوعية تتضمن روابط إلى توثيقات Microsoft Learn ذات الصلة.

**المتغيرات البيئية المطلوبة:**  

لاستخدام السيناريو 2 (تطبيق ويب Chainlit مع Azure OpenAI)، يجب تعيين المتغيرات البيئية التالية في ملف `.env` file in the `python`:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

املأ هذه القيم بتفاصيل موارد Azure OpenAI الخاصة بك قبل تشغيل التطبيق.

> **نصيحة:** يمكنك بسهولة نشر نماذجك الخاصة باستخدام [Azure AI Foundry](https://ai.azure.com/).

### السيناريو 3: التوثيق داخل المحرر مع خادم MCP في VS Code

بدلاً من التنقل بين علامات التبويب في المتصفح للبحث عن التوثيق، يمكنك جلب Microsoft Learn Docs مباشرة إلى VS Code باستخدام خادم MCP. هذا يتيح لك:  
- البحث وقراءة التوثيقات داخل VS Code دون مغادرة بيئة البرمجة الخاصة بك.  
- الرجوع إلى التوثيق وإدراج الروابط مباشرة في ملفات README أو ملفات الدورة التدريبية.  
- استخدام GitHub Copilot و MCP معًا لتجربة توثيق مدعومة بالذكاء الاصطناعي بسلاسة.

**أمثلة على حالات الاستخدام:**  
- إضافة روابط مرجعية بسرعة إلى README أثناء كتابة توثيق دورة أو مشروع.  
- استخدام Copilot لتوليد الكود وMCP للعثور على التوثيقات ذات الصلة والاستشهاد بها فورًا.  
- البقاء مركزًا في المحرر وزيادة الإنتاجية.

> [!IMPORTANT]  
> تأكد من أن لديك ملف صالح [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

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

توضح هذه الأمثلة مرونة التطبيق لأهداف ومدة تعلم مختلفة.

## المراجع

- [توثيق Chainlit](https://docs.chainlit.io/)  
- [توثيق MCP](https://github.com/MicrosoftDocs/mcp)

**تنويه**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر المعتمد. للمعلومات الحساسة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.