<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:26:48+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "fa"
}
-->
# تولید برنامه مطالعه با Chainlit و Microsoft Learn Docs MCP

## پیش‌نیازها

- پایتون نسخه ۳.۸ یا بالاتر  
- pip (مدیر بسته پایتون)  
- دسترسی به اینترنت برای اتصال به سرور Microsoft Learn Docs MCP  

## نصب

۱. این مخزن را کلون کنید یا فایل‌های پروژه را دانلود کنید.  
۲. وابستگی‌های مورد نیاز را نصب کنید:

   ```bash
   pip install -r requirements.txt
   ```

## نحوه استفاده

### سناریو ۱: پرس‌وجوی ساده به Docs MCP  
یک کلاینت خط فرمان که به سرور Docs MCP متصل می‌شود، پرس‌وجو را ارسال می‌کند و نتیجه را نمایش می‌دهد.

۱. اسکریپت را اجرا کنید:  
   ```bash
   python scenario1.py
   ```  
۲. سوال مستندات خود را در خط فرمان وارد کنید.

### سناریو ۲: تولید برنامه مطالعه (اپ وب Chainlit)  
رابط کاربری تحت وب (با استفاده از Chainlit) که به کاربران امکان می‌دهد برنامه مطالعه شخصی‌سازی‌شده و هفتگی برای هر موضوع فنی ایجاد کنند.

۱. اپ Chainlit را راه‌اندازی کنید:  
   ```bash
   chainlit run scenario2.py
   ```  
۲. آدرس محلی که در ترمینال نمایش داده می‌شود (مثلاً http://localhost:8000) را در مرورگر خود باز کنید.  
۳. در پنجره چت، موضوع مطالعه و تعداد هفته‌های مورد نظر خود را وارد کنید (مثلاً "گواهینامه AI-900، ۸ هفته").  
۴. اپ پاسخ می‌دهد با برنامه مطالعه هفتگی به همراه لینک‌هایی به مستندات مرتبط Microsoft Learn.

**متغیرهای محیطی مورد نیاز:**  

برای استفاده از سناریو ۲ (اپ وب Chainlit با Azure OpenAI)، باید متغیرهای محیطی زیر را در دایرکتوری `.env` file in the `python` تنظیم کنید:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

قبل از اجرای اپ، این مقادیر را با اطلاعات منابع Azure OpenAI خود پر کنید.

> **نکته:** می‌توانید به راحتی مدل‌های خود را با استفاده از [Azure AI Foundry](https://ai.azure.com/) مستقر کنید.

### سناریو ۳: مستندات درون ویرایشگر با سرور MCP در VS Code  

به جای جابجایی بین تب‌های مرورگر برای جستجوی مستندات، می‌توانید Microsoft Learn Docs را مستقیماً داخل VS Code خود با استفاده از سرور MCP داشته باشید. این امکان به شما می‌دهد:  
- جستجو و خواندن مستندات در داخل VS Code بدون ترک محیط کدنویسی.  
- ارجاع به مستندات و درج لینک‌ها مستقیماً در فایل README یا دوره‌های آموزشی.  
- استفاده همزمان از GitHub Copilot و MCP برای جریان کاری مستندسازی هوشمند و یکپارچه.

**نمونه کاربردها:**  
- اضافه کردن سریع لینک‌های مرجع به README هنگام نوشتن مستندات دوره یا پروژه.  
- استفاده از Copilot برای تولید کد و MCP برای یافتن و ارجاع فوری به مستندات مرتبط.  
- حفظ تمرکز در ویرایشگر و افزایش بهره‌وری.

> [!IMPORTANT]  
> اطمینان حاصل کنید که فایل [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

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
- `Cloud architecture, 9 weeks`] معتبر دارید.

این مثال‌ها انعطاف‌پذیری اپ را برای اهداف یادگیری و بازه‌های زمانی مختلف نشان می‌دهند.

## منابع

- [مستندات Chainlit](https://docs.chainlit.io/)  
- [مستندات MCP](https://github.com/MicrosoftDocs/mcp)

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نادرستی‌هایی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوء تفاهم یا برداشت نادرستی که از استفاده از این ترجمه ناشی شود، نیستیم.