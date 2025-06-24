<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "36de9fae488d6de554d969fe8e0801a8",
  "translation_date": "2025-06-20T19:14:06+00:00",
  "source_file": "09-CaseStudy/apimsample.md",
  "language_code": "fa"
}
-->
# مطالعه موردی: نمایش REST API در API Management به‌عنوان سرور MCP

Azure API Management سرویسی است که یک دروازه روی نقاط انتهایی API شما فراهم می‌کند. نحوه کار آن به این صورت است که Azure API Management مانند یک پراکسی جلوی APIهای شما عمل می‌کند و می‌تواند تصمیم بگیرد با درخواست‌های ورودی چه کاری انجام دهد.

با استفاده از آن، مجموعه‌ای از ویژگی‌ها را اضافه می‌کنید مانند:

- **امنیت**، می‌توانید از همه چیز از کلیدهای API، JWT تا managed identity استفاده کنید.
- **محدودیت نرخ درخواست**، ویژگی عالی این است که بتوانید تعیین کنید در یک بازه زمانی مشخص چند تماس عبور کند. این کمک می‌کند تا همه کاربران تجربه خوبی داشته باشند و همچنین سرویس شما با درخواست‌ها بیش از حد تحت فشار قرار نگیرد.
- **مقیاس‌پذیری و تعادل بار**. می‌توانید چندین نقطه انتهایی راه‌اندازی کنید تا بار را متعادل کنید و همچنین می‌توانید تعیین کنید چگونه "تعادل بار" انجام شود.
- **ویژگی‌های هوش مصنوعی مانند semantic caching**، محدودیت توکن و مانیتورینگ توکن و موارد دیگر. این‌ها ویژگی‌های عالی‌ای هستند که پاسخگویی را بهبود می‌بخشند و همچنین به شما کمک می‌کنند هزینه‌های توکن خود را کنترل کنید. [برای اطلاعات بیشتر اینجا را بخوانید](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## چرا MCP + Azure API Management؟

Model Context Protocol به سرعت به استانداردی برای اپلیکیشن‌های هوش مصنوعی عامل‌محور تبدیل می‌شود و نحوه ارائه ابزارها و داده‌ها را به صورت یکنواخت مشخص می‌کند. Azure API Management گزینه طبیعی است وقتی نیاز به "مدیریت" APIها دارید. سرورهای MCP اغلب با APIهای دیگر یکپارچه می‌شوند تا درخواست‌ها را به یک ابزار حل کنند، برای مثال. بنابراین ترکیب Azure API Management و MCP بسیار منطقی است.

## مرور کلی

در این مورد خاص، یاد می‌گیریم چگونه نقاط انتهایی API را به‌عنوان یک سرور MCP نمایش دهیم. با انجام این کار، می‌توانیم به راحتی این نقاط انتهایی را بخشی از یک اپلیکیشن عامل‌محور کنیم و در عین حال از ویژگی‌های Azure API Management بهره ببریم.

## ویژگی‌های کلیدی

- شما متدهای نقطه انتهایی را که می‌خواهید به عنوان ابزار نمایش داده شوند انتخاب می‌کنید.
- ویژگی‌های اضافی که دریافت می‌کنید به تنظیمات شما در بخش policy برای API بستگی دارد. اما در اینجا به شما نشان می‌دهیم چگونه می‌توانید محدودیت نرخ را اضافه کنید.

## مرحله پیش‌نیاز: وارد کردن API

اگر قبلاً API در Azure API Management دارید که عالی است و می‌توانید این مرحله را رد کنید. در غیر این صورت، این لینک را ببینید، [وارد کردن API به Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## نمایش API به عنوان سرور MCP

برای نمایش نقاط انتهایی API، مراحل زیر را دنبال کنید:

1. وارد Azure Portal شده و به آدرس زیر بروید <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
به نمونه API Management خود بروید.

1. در منوی سمت چپ، APIs > MCP Servers > + Create new MCP Server را انتخاب کنید.

1. در بخش API، یک REST API را برای نمایش به عنوان سرور MCP انتخاب کنید.

1. یک یا چند عملیات API را برای نمایش به عنوان ابزار انتخاب کنید. می‌توانید همه عملیات یا فقط عملیات خاصی را انتخاب کنید.

    ![انتخاب متدها برای نمایش](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. روی **Create** کلیک کنید.

1. به منوی **APIs** و **MCP Servers** بروید، باید موارد زیر را ببینید:

    ![دیدن سرور MCP در پنل اصلی](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    سرور MCP ساخته شده و عملیات API به عنوان ابزار نمایش داده شده‌اند. سرور MCP در پنل MCP Servers فهرست شده است. ستون URL نقطه انتهایی سرور MCP را نشان می‌دهد که می‌توانید برای تست یا درون اپلیکیشن کلاینت آن را فراخوانی کنید.

## اختیاری: پیکربندی سیاست‌ها

Azure API Management مفهوم اصلی سیاست‌ها را دارد که در آن قوانین مختلفی برای نقاط انتهایی خود مانند محدودیت نرخ یا semantic caching تنظیم می‌کنید. این سیاست‌ها به صورت XML نوشته می‌شوند.

در اینجا نحوه تنظیم یک سیاست برای محدود کردن نرخ سرور MCP آورده شده است:

1. در پورتال، زیر APIs، **MCP Servers** را انتخاب کنید.

1. سرور MCP که ساخته‌اید را انتخاب کنید.

1. در منوی سمت چپ، زیر MCP، **Policies** را انتخاب کنید.

1. در ویرایشگر سیاست، سیاست‌هایی را که می‌خواهید روی ابزارهای سرور MCP اعمال شود اضافه یا ویرایش کنید. سیاست‌ها به فرمت XML تعریف می‌شوند. برای مثال، می‌توانید سیاستی اضافه کنید که تماس‌ها به ابزارهای سرور MCP را محدود کند (در این مثال، ۵ تماس در ۳۰ ثانیه برای هر آدرس IP کلاینت). XML زیر این محدودیت را اعمال می‌کند:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    تصویری از ویرایشگر سیاست:

    ![ویرایشگر سیاست](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## امتحان کنید

بیایید مطمئن شویم سرور MCP ما به درستی کار می‌کند.

برای این کار از Visual Studio Code و GitHub Copilot در حالت Agent استفاده می‌کنیم. سرور MCP را به یک *mcp.json* اضافه می‌کنیم. با این کار، Visual Studio Code به عنوان یک کلاینت با قابلیت‌های عامل‌محور عمل می‌کند و کاربران نهایی می‌توانند یک درخواست تایپ کنند و با آن سرور تعامل داشته باشند.

بیایید ببینیم چگونه سرور MCP را در Visual Studio Code اضافه کنیم:

1. از دستور MCP: **Add Server** در Command Palette استفاده کنید.

1. وقتی خواسته شد، نوع سرور را انتخاب کنید: **HTTP (HTTP or Server Sent Events)**.

1. URL سرور MCP در API Management را وارد کنید. مثال: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (برای نقطه انتهایی SSE) یا **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (برای نقطه انتهایی MCP)، توجه کنید تفاوت بین پروتکل‌ها در `/sse` or `/mcp` است.

1. یک شناسه سرور به دلخواه وارد کنید. این مقدار مهم نیست اما به شما کمک می‌کند به خاطر بسپارید این نمونه سرور چیست.

1. انتخاب کنید که پیکربندی در تنظیمات workspace ذخیره شود یا تنظیمات کاربر.

  - **تنظیمات workspace** - پیکربندی سرور فقط در فایل .vscode/mcp.json در workspace فعلی ذخیره می‌شود.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    یا اگر HTTP streaming را به عنوان پروتکل انتخاب کنید کمی متفاوت خواهد بود:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **تنظیمات کاربر** - پیکربندی سرور به فایل *settings.json* سراسری شما اضافه می‌شود و در همه workspaceها در دسترس است. پیکربندی مشابه زیر است:

    ![تنظیمات کاربر](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. همچنین باید پیکربندی هدر اضافه کنید تا مطمئن شوید به درستی به Azure API Management احراز هویت می‌شود. از هدر **Ocp-Apim-Subscription-Key** استفاده می‌کند.

    - اینجا نحوه اضافه کردن آن به تنظیمات آمده است:

    ![اضافه کردن هدر برای احراز هویت](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png)  
    این باعث می‌شود یک درخواست برای وارد کردن مقدار کلید API نمایش داده شود که می‌توانید در Azure Portal برای نمونه Azure API Management خود پیدا کنید.

   - برای اضافه کردن آن به *mcp.json* به این شکل می‌توانید اضافه کنید:

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

### استفاده از حالت Agent

حالا ما در تنظیمات یا در *.vscode/mcp.json* همه چیز را آماده کرده‌ایم. بیایید امتحان کنیم.

باید یک آیکون Tools مانند شکل زیر باشد که ابزارهای نمایش داده شده از سرور شما فهرست شده‌اند:

![ابزارهای سرور](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. روی آیکون ابزارها کلیک کنید و باید فهرستی از ابزارها را ببینید:

    ![ابزارها](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. در چت یک درخواست وارد کنید تا ابزار فراخوانی شود. برای مثال، اگر ابزاری برای گرفتن اطلاعات سفارش انتخاب کرده‌اید، می‌توانید از عامل درباره یک سفارش بپرسید. این یک نمونه درخواست است:

    ```text
    get information from order 2
    ```

    اکنون یک آیکون ابزار به شما نمایش داده می‌شود که از شما می‌خواهد برای ادامه استفاده از ابزار اجازه دهید. گزینه ادامه را انتخاب کنید، اکنون باید خروجی مشابه زیر را ببینید:

    ![نتیجه درخواست](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **آنچه بالا می‌بینید بستگی به ابزارهایی دارد که تنظیم کرده‌اید، اما ایده کلی این است که پاسخ متنی مانند نمونه بالا دریافت کنید.**

## منابع

در اینجا می‌توانید بیشتر یاد بگیرید:

- [آموزش Azure API Management و MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [نمونه پایتون: امن‌سازی سرورهای MCP از راه دور با استفاده از Azure API Management (آزمایشی)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [آزمایشگاه مجوزدهی کلاینت MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [استفاده از افزونه Azure API Management برای VS Code جهت وارد کردن و مدیریت APIها](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [ثبت و کشف سرورهای MCP از راه دور در Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) مخزن عالی که بسیاری از قابلیت‌های هوش مصنوعی با Azure API Management را نشان می‌دهد
- [کارگاه‌های AI Gateway](https://azure-samples.github.io/AI-Gateway/) شامل کارگاه‌هایی با استفاده از Azure Portal که راهی عالی برای شروع ارزیابی قابلیت‌های هوش مصنوعی است.

**سلب مسئولیت**:  
این سند با استفاده از سرویس ترجمه هوش مصنوعی [Co-op Translator](https://github.com/Azure/co-op-translator) ترجمه شده است. در حالی که ما در تلاش برای دقت هستیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی خطاها یا نواقصی باشند. سند اصلی به زبان مبدأ باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، استفاده از ترجمه حرفه‌ای انسانی توصیه می‌شود. ما مسئول هیچ گونه سوءتفاهم یا برداشت نادرستی که از استفاده این ترجمه ناشی شود، نیستیم.