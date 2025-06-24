<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:26:57+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "ur"
}
-->
# Study Plan Generator with Chainlit & Microsoft Learn Docs MCP

## ضروریات

- Python 3.8 یا اس سے جدید ورژن
- pip (Python پیکیج مینیجر)
- Microsoft Learn Docs MCP سرور سے کنیکٹ ہونے کے لیے انٹرنیٹ کی سہولت

## تنصیب

1. اس repository کو کلون کریں یا پروجیکٹ فائلز ڈاؤن لوڈ کریں۔
2. مطلوبہ dependencies انسٹال کریں:

   ```bash
   pip install -r requirements.txt
   ```

## استعمال

### منظر نامہ 1: Docs MCP کے لیے سادہ سوال
ایک کمانڈ لائن کلائنٹ جو Docs MCP سرور سے جڑتا ہے، سوال بھیجتا ہے، اور نتیجہ پرنٹ کرتا ہے۔

1. اسکرپٹ چلائیں:
   ```bash
   python scenario1.py
   ```
2. پرامپٹ پر اپنی ڈاکیومنٹیشن کا سوال درج کریں۔

### منظر نامہ 2: اسٹڈی پلان جنریٹر (Chainlit ویب ایپ)
ایک ویب بیسڈ انٹرفیس (Chainlit استعمال کرتے ہوئے) جو صارفین کو کسی بھی تکنیکی موضوع کے لیے ہفتہ بہ ہفتہ ذاتی نوعیت کا مطالعہ پلان بنانے کی سہولت دیتا ہے۔

1. Chainlit ایپ شروع کریں:
   ```bash
   chainlit run scenario2.py
   ```
2. اپنے ٹرمینل میں دی گئی لوکل URL (مثلاً http://localhost:8000) کو اپنے براؤزر میں کھولیں۔
3. چیٹ ونڈو میں اپنا مطالعہ موضوع اور مطالعہ کے ہفتوں کی تعداد درج کریں (مثلاً "AI-900 certification, 8 weeks")۔
4. ایپ ہفتہ بہ ہفتہ مطالعہ پلان کے ساتھ جواب دے گی، جس میں متعلقہ Microsoft Learn ڈاکیومنٹیشن کے لنکس شامل ہوں گے۔

**ضروری ماحول کے متغیرات:**

منظر نامہ 2 (Azure OpenAI کے ساتھ Chainlit ویب ایپ) استعمال کرنے کے لیے، آپ کو `.env` file in the `python` ڈائریکٹری میں درج ذیل ماحول کے متغیرات سیٹ کرنے ہوں گے:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

ایپ چلانے سے پہلے ان اقدار کو اپنے Azure OpenAI resource کی تفصیلات سے بھر دیں۔

> **Tip:** آپ آسانی سے اپنے ماڈلز کو [Azure AI Foundry](https://ai.azure.com/) کے ذریعے ڈیپلائے کر سکتے ہیں۔

### منظر نامہ 3: VS Code میں MCP سرور کے ساتھ In-Editor Docs

براؤزر کے ٹیبز تبدیل کرنے کی بجائے، آپ Microsoft Learn Docs کو براہ راست VS Code میں MCP سرور کے ذریعے لاسکتے ہیں۔ اس سے آپ کو یہ سہولیات ملتی ہیں:
- VS Code کے اندر ہی ڈاکیومنٹیشن تلاش کریں اور پڑھیں، اپنے کوڈنگ ماحول سے باہر نکلے بغیر۔
- ڈاکیومنٹیشن کا حوالہ دیں اور لنکس براہ راست اپنے README یا کورس فائلز میں شامل کریں۔
- GitHub Copilot اور MCP کو ایک ساتھ استعمال کریں تاکہ ایک مربوط، AI سے چلنے والا ڈاکیومنٹیشن ورک فلو حاصل ہو۔

**مثال کے استعمال کے کیسز:**
- کورس یا پروجیکٹ ڈاکیومنٹیشن لکھتے ہوئے جلدی سے README میں حوالہ جات کے لنکس شامل کریں۔
- کوڈ جنریٹ کرنے کے لیے Copilot استعمال کریں اور MCP کے ذریعے فوری طور پر متعلقہ ڈاکس تلاش کر کے حوالہ دیں۔
- اپنے ایڈیٹر میں توجہ مرکوز رکھیں اور اپنی پیداواریت بڑھائیں۔

> [!IMPORTANT]
> یقینی بنائیں کہ آپ کے پاس ایک درست [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

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
- `Cloud architecture, 9 weeks` موجود ہو۔

یہ مثالیں ایپ کی مختلف تعلیمی مقاصد اور وقت کے فریم کے لیے لچک کو ظاہر کرتی ہیں۔

## حوالہ جات

- [Chainlit Documentation](https://docs.chainlit.io/)
- [MCP Documentation](https://github.com/MicrosoftDocs/mcp)

**ڈسکلیمَر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا نقائص ہو سکتے ہیں۔ اصل دستاویز اپنی مادری زبان میں معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ تجویز کیا جاتا ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تعبیر کی ذمہ داری ہم پر عائد نہیں ہوگی۔