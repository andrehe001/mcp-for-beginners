<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "36de9fae488d6de554d969fe8e0801a8",
  "translation_date": "2025-06-20T19:14:28+00:00",
  "source_file": "09-CaseStudy/apimsample.md",
  "language_code": "ur"
}
-->
# کیس اسٹڈی: API Management میں REST API کو MCP سرور کے طور پر ظاہر کرنا

Azure API Management ایک ایسی سروس ہے جو آپ کے API Endpoints کے اوپر ایک گیٹ وے فراہم کرتی ہے۔ یہ اس طرح کام کرتی ہے کہ Azure API Management آپ کے APIs کے سامنے ایک پراکسی کی طرح کام کرتی ہے اور آنے والی درخواستوں کے ساتھ کیا کرنا ہے یہ فیصلہ کر سکتی ہے۔

اس کا استعمال کرتے ہوئے، آپ بہت سی خصوصیات شامل کر سکتے ہیں جیسے:

- **سیکیورٹی**، آپ API keys، JWT سے لے کر managed identity تک سب کچھ استعمال کر سکتے ہیں۔
- **ریٹ لمیٹنگ**، ایک بہترین خصوصیت یہ ہے کہ آپ یہ فیصلہ کر سکتے ہیں کہ ایک مخصوص وقت کی مدت میں کتنی کالز گزر سکتی ہیں۔ یہ یقینی بناتا ہے کہ تمام صارفین کو بہترین تجربہ ملے اور آپ کی سروس درخواستوں سے زیادہ بوجھل نہ ہو۔
- **اسکیلنگ اور لوڈ بیلنسنگ**۔ آپ کئی endpoints سیٹ اپ کر سکتے ہیں تاکہ لوڈ متوازن ہو اور آپ یہ بھی فیصلہ کر سکتے ہیں کہ "load balance" کیسے کرنا ہے۔
- **AI خصوصیات جیسے semantic caching، token limit اور token monitoring وغیرہ**۔ یہ زبردست خصوصیات ہیں جو ردعمل کو بہتر بناتی ہیں اور آپ کو اپنے token کے استعمال پر قابو پانے میں مدد دیتی ہیں۔ [مزید پڑھیں یہاں](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities)۔

## MCP + Azure API Management کیوں؟

Model Context Protocol جلد ہی agentic AI ایپس کے لیے ایک معیار بنتا جا رہا ہے اور ٹولز اور ڈیٹا کو ایک مستقل انداز میں ظاہر کرنے کا طریقہ ہے۔ جب آپ کو APIs کو "manage" کرنا ہو تو Azure API Management ایک فطری انتخاب ہے۔ MCP Servers اکثر دوسرے APIs کے ساتھ انٹیگریٹ ہوتے ہیں تاکہ مثال کے طور پر کسی ٹول کے لیے درخواستوں کو حل کیا جا سکے۔ اس لیے Azure API Management اور MCP کو ملانا بہت معقول بات ہے۔

## جائزہ

اس مخصوص استعمال کے کیس میں ہم سیکھیں گے کہ API endpoints کو MCP Server کے طور پر کیسے ظاہر کیا جائے۔ اس طرح، ہم آسانی سے ان endpoints کو ایک agentic ایپ کا حصہ بنا سکتے ہیں اور ساتھ ہی Azure API Management کی خصوصیات سے فائدہ اٹھا سکتے ہیں۔

## اہم خصوصیات

- آپ وہ endpoint طریقے منتخب کرتے ہیں جنہیں آپ ٹولز کے طور پر ظاہر کرنا چاہتے ہیں۔
- اضافی خصوصیات اس بات پر منحصر ہیں کہ آپ اپنی API کے لیے پالیسی سیکشن میں کیا ترتیب دیتے ہیں۔ لیکن یہاں ہم آپ کو دکھائیں گے کہ ریٹ لمیٹنگ کیسے شامل کی جا سکتی ہے۔

## پیشگی قدم: API کو امپورٹ کرنا

اگر آپ کے پاس پہلے سے Azure API Management میں API موجود ہے تو بہت اچھا، آپ یہ قدم چھوڑ سکتے ہیں۔ اگر نہیں، تو اس لنک کو دیکھیں، [Azure API Management میں API امپورٹ کرنا](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api)۔

## API کو MCP Server کے طور پر ظاہر کرنا

API endpoints کو ظاہر کرنے کے لیے، درج ذیل مراحل پر عمل کریں:

1. Azure پورٹل پر جائیں اور اس پتہ پر جائیں <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
اپنے API Management انسٹینس پر جائیں۔

1. بائیں مینو میں، APIs > MCP Servers > + Create new MCP Server منتخب کریں۔

1. API میں، ایک REST API منتخب کریں جسے MCP سرور کے طور پر ظاہر کرنا ہو۔

1. ایک یا زیادہ API Operations منتخب کریں جنہیں ٹولز کے طور پر ظاہر کرنا ہو۔ آپ تمام آپریشنز یا صرف مخصوص آپریشنز منتخب کر سکتے ہیں۔

    ![Select methods to expose](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. **Create** منتخب کریں۔

1. مینو آپشن **APIs** اور **MCP Servers** پر جائیں، آپ کو درج ذیل نظر آئے گا:

    ![See the MCP Server in the main pane](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP سرور بن چکا ہے اور API آپریشنز ٹولز کے طور پر ظاہر ہو گئے ہیں۔ MCP سرور MCP Servers پین میں فہرست میں شامل ہے۔ URL کالم MCP سرور کے endpoint کو دکھاتا ہے جسے آپ ٹیسٹ کرنے یا کلائنٹ ایپلیکیشن میں کال کر سکتے ہیں۔

## اختیاری: پالیسیز ترتیب دینا

Azure API Management میں پالیسیز کا بنیادی تصور ہے جہاں آپ اپنے endpoints کے لیے مختلف قواعد مرتب کرتے ہیں، جیسے کہ ریٹ لمیٹنگ یا semantic caching۔ یہ پالیسیاں XML میں تحریر کی جاتی ہیں۔

یہاں بتایا گیا ہے کہ آپ MCP Server کی ریٹ لمیٹنگ کے لیے پالیسی کیسے سیٹ اپ کر سکتے ہیں:

1. پورٹل میں، APIs کے تحت، **MCP Servers** منتخب کریں۔

1. وہ MCP سرور منتخب کریں جو آپ نے بنایا ہے۔

1. بائیں مینو میں، MCP کے تحت، **Policies** منتخب کریں۔

1. پالیسی ایڈیٹر میں، وہ پالیسیاں شامل یا ترمیم کریں جو آپ MCP سرور کے ٹولز پر لاگو کرنا چاہتے ہیں۔ پالیسیاں XML فارمیٹ میں ہوتی ہیں۔ مثال کے طور پر، آپ ایک پالیسی شامل کر سکتے ہیں جو MCP سرور کے ٹولز کی کالز کو محدود کرے (اس مثال میں، ہر کلائنٹ IP ایڈریس کے لیے 30 سیکنڈ میں 5 کالز)۔ یہاں XML ہے جو ریٹ لمیٹنگ کرے گا:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    پالیسی ایڈیٹر کی تصویر:

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## آزما کر دیکھیں

آئیے یقینی بنائیں کہ ہمارا MCP Server جیسا کہ توقع ہے کام کر رہا ہے۔

اس کے لیے ہم Visual Studio Code اور GitHub Copilot اور اس کے Agent موڈ کا استعمال کریں گے۔ ہم MCP سرور کو *mcp.json* میں شامل کریں گے۔ اس طرح، Visual Studio Code ایک کلائنٹ کے طور پر کام کرے گا جس میں agentic صلاحیتیں ہوں گی اور آخری صارفین ایک پرامپٹ لکھ کر اس سرور کے ساتھ بات چیت کر سکیں گے۔

Visual Studio Code میں MCP سرور شامل کرنے کا طریقہ:

1. Command Palette سے MCP: **Add Server کمانڈ** استعمال کریں۔

1. جب پوچھا جائے، سرور کی قسم منتخب کریں: **HTTP (HTTP یا Server Sent Events)**۔

1. API Management میں MCP سرور کا URL درج کریں۔ مثال: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (SSE endpoint کے لیے) یا **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (MCP endpoint کے لیے)، نوٹ کریں کہ ٹرانسپورٹس میں فرق `/sse` or `/mcp` ہے۔

1. اپنی پسند کا سرور ID درج کریں۔ یہ کوئی اہم قدر نہیں ہے لیکن یہ آپ کو یاد دلانے میں مدد دے گا کہ یہ سرور انسٹینس کون سا ہے۔

1. منتخب کریں کہ کنفیگریشن کو workspace settings یا user settings میں محفوظ کرنا ہے۔

  - **Workspace settings** - سرور کنفیگریشن صرف موجودہ ورک اسپیس میں دستیاب .vscode/mcp.json فائل میں محفوظ ہوگی۔

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    یا اگر آپ streaming HTTP کو بطور ٹرانسپورٹ منتخب کریں تو یہ تھوڑا مختلف ہوگا:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **User settings** - سرور کنفیگریشن آپ کی عالمی *settings.json* فائل میں شامل کی جاتی ہے اور تمام ورک اسپیسز میں دستیاب ہوتی ہے۔ کنفیگریشن کچھ یوں دکھائی دیتی ہے:

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. آپ کو کنفیگریشن میں ایک ہیڈر بھی شامل کرنا ہوگا تاکہ یہ Azure API Management کی طرف صحیح طریقے سے تصدیق کرے۔ یہ **Ocp-Apim-Subscription-Key** نامی ہیڈر استعمال کرتا ہے۔

    - یہاں دکھایا گیا ہے کہ اسے سیٹنگز میں کیسے شامل کریں:

    ![Adding header for authentication](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png)  
    اس سے ایک پرامپٹ ظاہر ہوگا جو آپ سے API key کی ویلیو مانگے گا جو آپ Azure پورٹل میں اپنے Azure API Management انسٹینس کے لیے حاصل کر سکتے ہیں۔

   - *mcp.json* میں شامل کرنے کے لیے، آپ اسے اس طرح شامل کر سکتے ہیں:

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

### Agent موڈ استعمال کریں

اب ہم یا تو سیٹنگز میں یا *.vscode/mcp.json* میں سب کچھ ترتیب دے چکے ہیں۔ آئیے اسے آزما کر دیکھیں۔

آپ کو ایک Tools آئیکن نظر آنا چاہیے، جہاں آپ کے سرور کے ظاہر کیے گئے ٹولز کی فہرست ہوگی:

![Tools from the server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Tools آئیکن پر کلک کریں اور آپ کو ٹولز کی فہرست نظر آئے گی:

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. چیٹ میں ایک پرامپٹ درج کریں تاکہ ٹول کو کال کیا جا سکے۔ مثال کے طور پر، اگر آپ نے کسی آرڈر کی معلومات حاصل کرنے کے لیے ٹول منتخب کیا ہے، تو آپ ایجنٹ سے آرڈر کے بارے میں پوچھ سکتے ہیں۔ یہاں ایک مثال کا پرامپٹ ہے:

    ```text
    get information from order 2
    ```

    اب آپ کو ایک tools آئیکن نظر آئے گا جو آپ سے ٹول کال کرنے کی اجازت طلب کرے گا۔ جاری رکھنے کے لیے منتخب کریں، آپ کو اب مندرجہ ذیل جیسا آؤٹ پٹ نظر آئے گا:

    ![Result from prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **جو کچھ آپ اوپر دیکھ رہے ہیں وہ اس بات پر منحصر ہے کہ آپ نے کون سے ٹولز سیٹ اپ کیے ہیں، لیکن مقصد یہ ہے کہ آپ کو ایک متنی جواب ملے جیسا کہ اوپر دکھایا گیا ہے۔**


## حوالہ جات

یہاں سے آپ مزید سیکھ سکتے ہیں:

- [Azure API Management اور MCP پر ٹیوٹوریل](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python نمونہ: Azure API Management کے ذریعے محفوظ ریموٹ MCP سرورز (تجرباتی)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP کلائنٹ اجازت نامہ لیب](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [VS Code کے لیے Azure API Management ایکسٹینشن کا استعمال کرتے ہوئے APIs کو امپورٹ اور منظم کرنا](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Azure API Center میں ریموٹ MCP سرورز کو رجسٹر اور دریافت کریں](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway)  
ایک زبردست ریپو جو Azure API Management کے ساتھ کئی AI صلاحیتیں دکھاتا ہے
- [AI Gateway ورکشاپس](https://azure-samples.github.io/AI-Gateway/)  
Azure پورٹل کا استعمال کرتے ہوئے ورکشاپس، جو AI صلاحیتوں کا جائزہ لینے کا ایک بہترین طریقہ ہیں۔

**ڈس کلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم صحت ہو سکتی ہے۔ اصل دستاویز اپنی مادری زبان میں معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ تجویز کیا جاتا ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔