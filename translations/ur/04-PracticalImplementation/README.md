<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5384bbb2a92d00d5d7e66274dbe0331d",
  "translation_date": "2025-06-20T18:21:53+00:00",
  "source_file": "04-PracticalImplementation/README.md",
  "language_code": "ur"
}
-->
# عملی نفاذ

عملی نفاذ وہ جگہ ہے جہاں Model Context Protocol (MCP) کی طاقت حقیقت میں ظاہر ہوتی ہے۔ اگرچہ MCP کے نظریہ اور فن تعمیر کو سمجھنا اہم ہے، حقیقی قدر اس وقت سامنے آتی ہے جب آپ ان تصورات کو استعمال کر کے ایسے حل تیار کرتے ہیں، ٹیسٹ کرتے ہیں اور تعینات کرتے ہیں جو حقیقی دنیا کے مسائل کو حل کرتے ہیں۔ یہ باب تصوری علم اور عملی ترقی کے درمیان پل کا کام کرتا ہے، اور آپ کو MCP پر مبنی ایپلیکیشنز کو عملی جامہ پہنانے کے عمل میں رہنمائی فراہم کرتا ہے۔

چاہے آپ ذہین اسسٹنٹس تیار کر رہے ہوں، کاروباری ورک فلو میں AI کو ضم کر رہے ہوں، یا ڈیٹا پروسیسنگ کے لیے حسب ضرورت آلات بنا رہے ہوں، MCP ایک لچکدار بنیاد فراہم کرتا ہے۔ اس کا زبان سے آزاد ڈیزائن اور مقبول پروگرامنگ زبانوں کے لیے سرکاری SDKs اسے وسیع پیمانے پر ڈویلپرز کے لیے قابل رسائی بناتے ہیں۔ ان SDKs کا فائدہ اٹھا کر، آپ جلدی سے پروٹو ٹائپ بنا سکتے ہیں، بار بار بہتر کر سکتے ہیں، اور اپنے حل کو مختلف پلیٹ فارمز اور ماحول میں اسکیل کر سکتے ہیں۔

اگلے حصوں میں، آپ کو عملی مثالیں، نمونہ کوڈ، اور تعیناتی کی حکمت عملیاں ملیں گی جو دکھاتی ہیں کہ MCP کو C#, Java, TypeScript, JavaScript، اور Python میں کیسے نافذ کیا جائے۔ آپ یہ بھی سیکھیں گے کہ MCP سرورز کو کیسے ڈیبگ اور ٹیسٹ کیا جائے، APIs کا انتظام کیسے کیا جائے، اور Azure کا استعمال کرتے ہوئے کلاؤڈ پر حل کیسے تعینات کیے جائیں۔ یہ عملی وسائل آپ کی سیکھنے کی رفتار کو تیز کرنے اور آپ کو مضبوط، پروڈکشن کے قابل MCP ایپلیکیشنز بنانے میں اعتماد دینے کے لیے تیار کیے گئے ہیں۔

## جائزہ

یہ سبق MCP کے عملی نفاذ کے پہلوؤں پر مختلف پروگرامنگ زبانوں میں توجہ دیتا ہے۔ ہم دیکھیں گے کہ C#, Java, TypeScript, JavaScript، اور Python میں MCP SDKs کو کیسے استعمال کیا جائے تاکہ مضبوط ایپلیکیشنز بنائی جا سکیں، MCP سرورز کو ڈیبگ اور ٹیسٹ کیا جا سکے، اور قابلِ استعمال وسائل، پرامپٹس، اور ٹولز تیار کیے جا سکیں۔

## سیکھنے کے مقاصد

اس سبق کے اختتام تک، آپ قابلِ عمل ہوں گے کہ آپ:
- مختلف پروگرامنگ زبانوں میں سرکاری SDKs کا استعمال کرتے ہوئے MCP حل نافذ کر سکیں
- MCP سرورز کو منظم طریقے سے ڈیبگ اور ٹیسٹ کر سکیں
- سرور کی خصوصیات (وسائل، پرامپٹس، اور ٹولز) تخلیق اور استعمال کر سکیں
- پیچیدہ کاموں کے لیے موثر MCP ورک فلو ڈیزائن کر سکیں
- کارکردگی اور قابلِ اعتماد ہونے کے لیے MCP نفاذ کو بہتر بنا سکیں

## سرکاری SDK وسائل

Model Context Protocol مختلف زبانوں کے لیے سرکاری SDKs فراہم کرتا ہے:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) 
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

## MCP SDKs کے ساتھ کام کرنا

یہ سیکشن مختلف پروگرامنگ زبانوں میں MCP کے عملی نفاذ کی مثالیں فراہم کرتا ہے۔ آپ `samples` ڈائریکٹری میں زبان کے مطابق منظم نمونہ کوڈ تلاش کر سکتے ہیں۔

### دستیاب نمونے

ریپوزیٹری میں درج ذیل زبانوں میں [نمونہ نفاذ](../../../04-PracticalImplementation/samples) شامل ہیں:

- [C#](./samples/csharp/README.md)
- [Java](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

ہر نمونہ مخصوص زبان اور ماحولیاتی نظام کے لیے MCP کے کلیدی تصورات اور نفاذ کے نمونے دکھاتا ہے۔

## بنیادی سرور خصوصیات

MCP سرورز ان خصوصیات کے کسی بھی امتزاج کو نافذ کر سکتے ہیں:

### وسائل
وسائل صارف یا AI ماڈل کے لیے سیاق و سباق اور ڈیٹا فراہم کرتے ہیں:
- دستاویزی ذخیرے
- علم کے بنیادی مراکز
- منظم ڈیٹا ذرائع
- فائل سسٹمز

### پرامپٹس
پرامپٹس صارفین کے لیے ٹیمپلیٹ شدہ پیغامات اور ورک فلو ہوتے ہیں:
- پہلے سے متعین گفتگو کے ٹیمپلیٹس
- رہنمائی شدہ تعامل کے نمونے
- مخصوص مکالماتی ڈھانچے

### ٹولز
ٹولز AI ماڈل کے لیے انجام دینے والے فنکشنز ہوتے ہیں:
- ڈیٹا پروسیسنگ کی سہولیات
- بیرونی API انضمام
- حسابی صلاحیتیں
- تلاش کی فعالیت

## نمونہ نفاذ: C#

سرکاری C# SDK ریپوزیٹری میں مختلف MCP کے پہلوؤں کو دکھانے والے کئی نمونہ نفاذ شامل ہیں:

- **بنیادی MCP کلائنٹ**: ایک سادہ مثال جو دکھاتی ہے کہ MCP کلائنٹ کیسے بنایا جائے اور ٹولز کو کال کیا جائے
- **بنیادی MCP سرور**: کم سے کم سرور نفاذ جس میں بنیادی ٹول رجسٹریشن شامل ہے
- **جدید MCP سرور**: مکمل خصوصیات والا سرور جس میں ٹول رجسٹریشن، تصدیق، اور خرابی ہینڈلنگ شامل ہے
- **ASP.NET انضمام**: ASP.NET Core کے ساتھ انضمام دکھانے والی مثالیں
- **ٹول نفاذ کے نمونے**: مختلف پیچیدگی کی سطحوں کے ساتھ ٹولز کو نافذ کرنے کے مختلف نمونے

MCP C# SDK ابھی پیش نظارہ میں ہے اور APIs میں تبدیلیاں آ سکتی ہیں۔ ہم اس بلاگ کو SDK کی ترقی کے ساتھ مسلسل اپ ڈیٹ کرتے رہیں گے۔

### کلیدی خصوصیات 
- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)

- اپنا [پہلا MCP سرور بنائیں](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/)۔

مکمل C# نفاذ کے نمونوں کے لیے، سرکاری C# SDK نمونہ ریپوزیٹری ملاحظہ کریں: [https://github.com/modelcontextprotocol/csharp-sdk](https://github.com/modelcontextprotocol/csharp-sdk)

## نمونہ نفاذ: Java نفاذ

Java SDK MCP کے مضبوط نفاذ کے اختیارات فراہم کرتا ہے جن میں انٹرپرائز معیار کی خصوصیات شامل ہیں۔

### کلیدی خصوصیات

- Spring Framework انضمام
- مضبوط ٹائپ سیفٹی
- Reactive پروگرامنگ کی حمایت
- جامع خرابی ہینڈلنگ

مکمل Java نفاذ کے نمونے کے لیے، نمونہ ڈائریکٹری میں [Java sample](samples/java/containerapp/README.md) دیکھیں۔

## نمونہ نفاذ: JavaScript نفاذ

JavaScript SDK MCP نفاذ کے لیے ہلکا پھلکا اور لچکدار طریقہ فراہم کرتا ہے۔

### کلیدی خصوصیات

- Node.js اور براؤزر کی حمایت
- Promise-based API
- Express اور دیگر فریم ورکس کے ساتھ آسان انضمام
- سٹریمنگ کے لیے WebSocket کی حمایت

مکمل JavaScript نفاذ کے نمونے کے لیے، نمونہ ڈائریکٹری میں [JavaScript sample](samples/javascript/README.md) دیکھیں۔

## نمونہ نفاذ: Python نفاذ

Python SDK MCP نفاذ کے لیے Pythonic طریقہ فراہم کرتا ہے جس میں بہترین ML فریم ورک انضمام شامل ہیں۔

### کلیدی خصوصیات

- asyncio کے ساتھ async/await کی حمایت
- Flask اور FastAPI انضمام
- آسان ٹول رجسٹریشن
- مقبول ML لائبریریز کے ساتھ مقامی انضمام

مکمل Python نفاذ کے نمونے کے لیے، نمونہ ڈائریکٹری میں [Python sample](samples/python/README.md) دیکھیں۔

## API مینجمنٹ

Azure API Management ایک بہترین حل ہے جس سے ہم MCP سرورز کو محفوظ بنا سکتے ہیں۔ خیال یہ ہے کہ آپ اپنے MCP سرور کے سامنے Azure API Management کا ایک انسٹانس رکھیں اور اسے ایسی خصوصیات سنبھالنے دیں جو آپ چاہتے ہیں، جیسے:

- ریٹ لمیٹنگ
- ٹوکن مینجمنٹ
- مانیٹرنگ
- لوڈ بیلنسنگ
- سیکیورٹی

### Azure نمونہ

یہاں ایک Azure نمونہ ہے جو بالکل یہی کرتا ہے، یعنی MCP سرور بنانا اور اسے Azure API Management کے ذریعے محفوظ کرنا: [https://github.com/Azure-Samples/remote-mcp-apim-functions-python](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

نیچے تصویر میں دیکھیں کہ اجازت کا عمل کیسے ہوتا ہے:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true) 

مندرجہ بالا تصویر میں درج ذیل ہوتا ہے:

- Microsoft Entra کے ذریعے تصدیق/اجازت دی جاتی ہے۔
- Azure API Management گیٹ وے کے طور پر کام کرتا ہے اور پالیسیز کے ذریعے ٹریفک کو ہدایت اور منظم کرتا ہے۔
- Azure Monitor تمام درخواستوں کو لاگ کرتا ہے تاکہ بعد میں تجزیہ کیا جا سکے۔

#### اجازت کا عمل

آئیے اجازت کے عمل کو مزید تفصیل سے دیکھتے ہیں:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP اجازت کی وضاحت

MCP اجازت کی وضاحت کے بارے میں مزید جانیں: [MCP Authorization specification](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization#2-10-third-party-authorization-flow)

## ریموٹ MCP سرور کو Azure پر تعینات کریں

آئیے دیکھتے ہیں کہ کیا ہم پہلے ذکر کردہ نمونہ تعینات کر سکتے ہیں:

1. ریپو کلون کریں

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

2. `Microsoft.App` رجسٹر کریں

    `` resource provider.
    * If you are using Azure CLI, run `az provider register --namespace Microsoft.App --wait`.
    * If you are using Azure PowerShell, run `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Then run `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState`

    کچھ وقت بعد چیک کریں کہ رجسٹریشن مکمل ہوئی ہے یا نہیں۔

3. اس [azd](https://aka.ms/azd) کمانڈ کو چلائیں تاکہ api management سروس، function app (کوڈ کے ساتھ)، اور دیگر تمام ضروری Azure وسائل فراہم کیے جائیں

    ```shell
    azd up
    ```

    یہ کمانڈز Azure پر تمام کلاؤڈ وسائل تعینات کریں گی۔

### MCP Inspector کے ساتھ اپنے سرور کی جانچ

1. **نئی ٹرمینل ونڈو** میں MCP Inspector انسٹال کریں اور چلائیں

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    آپ کو ایک ایسا انٹرفیس نظر آئے گا:

    ![Connect to Node inspector](../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.ur.png) 

2. CTRL کلک کریں تاکہ MCP Inspector ویب ایپ کو URL سے لوڈ کیا جا سکے (مثلاً http://127.0.0.1:6274/#resources)
3. ٹرانسپورٹ ٹائپ کو `SSE` پر سیٹ کریں اور **Connect** کریں:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

5. **ٹولز کی فہرست** دیکھیں۔ کسی ٹول پر کلک کریں اور **Run Tool** کریں۔  

اگر تمام مراحل کامیابی سے مکمل ہوئے ہیں، تو آپ MCP سرور سے منسلک ہو چکے ہیں اور ٹول کال کرنے میں کامیاب رہے ہیں۔

## Azure کے لیے MCP سرورز

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): یہ ریپوزیٹریز Azure Functions کے ساتھ Python، C# .NET، یا Node/TypeScript استعمال کرتے ہوئے کسٹم ریموٹ MCP سرورز بنانے اور تعینات کرنے کے لیے کوئیک اسٹارٹ ٹیمپلیٹس ہیں۔

یہ نمونے ایک مکمل حل فراہم کرتے ہیں جو ڈویلپرز کو اجازت دیتا ہے کہ وہ:

- مقامی طور پر بنائیں اور چلائیں: ایک MCP سرور کو مقامی مشین پر تیار کریں اور ڈیبگ کریں
- Azure پر تعینات کریں: آسانی سے کلاؤڈ پر تعینات کرنے کے لیے ایک سادہ azd up کمانڈ استعمال کریں
- کلائنٹس سے کنیکٹ کریں: مختلف کلائنٹس سے MCP سرور سے منسلک ہوں، بشمول VS Code کے Copilot ایجنٹ موڈ اور MCP Inspector ٹول

### کلیدی خصوصیات:

- ڈیزائن کے لحاظ سے سیکیورٹی: MCP سرور کو کیز اور HTTPS کے ذریعے محفوظ کیا گیا ہے
- تصدیقی اختیارات: بلٹ ان آتھنٹیکیشن اور/یا API مینجمنٹ کے ذریعے OAuth کی حمایت
- نیٹ ورک تنہائی: Azure Virtual Networks (VNET) کے ذریعے نیٹ ورک تنہائی کی اجازت
- سرور لیس فن تعمیر: Azure Functions کا استعمال کرتے ہوئے اسکیل ایبل، ایونٹ ڈریون ایگزیکیوشن
- مقامی ترقی: مکمل مقامی ترقی اور ڈیبگنگ کی حمایت
- آسان تعیناتی: Azure پر تعیناتی کا آسان عمل

ریپوزیٹری میں تمام ضروری کنفیگریشن فائلیں، سورس کوڈ، اور انفراسٹرکچر کی تعریفیں شامل ہیں تاکہ آپ تیزی سے پروڈکشن کے قابل MCP سرور نفاذ شروع کر سکیں۔

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Python کے ساتھ Azure Functions کا استعمال کرتے ہوئے MCP کا نمونہ نفاذ

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - C# .NET کے ساتھ Azure Functions کا استعمال کرتے ہوئے MCP کا نمونہ نفاذ

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Node/TypeScript کے ساتھ Azure Functions کا استعمال کرتے ہوئے MCP کا نمونہ نفاذ

## اہم نکات

- MCP SDKs زبان کے مخصوص ٹولز فراہم کرتے ہیں جو مضبوط MCP حل بنانے میں مدد دیتے ہیں
- ڈیبگنگ اور ٹیسٹنگ کا عمل قابلِ اعتماد MCP ایپلیکیشنز کے لیے انتہائی اہم ہے
- قابلِ استعمال پرامپٹ ٹیمپلیٹس AI تعاملات کو مستقل بناتے ہیں
- اچھی طرح ڈیزائن شدہ ورک فلو پیچیدہ کاموں کو مختلف ٹولز کے ذریعے منظم کر سکتے ہیں
- MCP حل نافذ کرنے کے لیے سیکیورٹی، کارکردگی، اور خرابی ہینڈلنگ پر غور کرنا ضروری ہے

## مشق

اپنے میدان میں ایک حقیقی مسئلہ حل کرنے والا عملی MCP ورک فلو ڈیزائن کریں:

1. 3-4 ایسے ٹولز کی نشاندہی کریں جو اس مسئلے کو حل کرنے میں مددگار ہوں
2. ایک ورک فلو ڈایاگرام بنائیں جو دکھائے کہ یہ ٹولز کیسے باہم تعامل کرتے ہیں
3. اپنی پسندیدہ زبان میں ان میں سے ایک ٹول کا بنیادی ورژن نافذ کریں
4. ایک پرامپٹ ٹیمپلیٹ بنائیں جو ماڈل کو آپ کا ٹول مؤثر طریقے سے استعمال کرنے میں مدد دے

## اضافی وسائل


---

اگلا: [Advanced Topics](../05-AdvancedTopics/README.md)

**ڈس کلیمر**:  
یہ دستاویز AI ترجمہ سروس [Co-op Translator](https://github.com/Azure/co-op-translator) کے ذریعے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم نوٹ کریں کہ خودکار ترجموں میں غلطیاں یا نقائص ہو سکتے ہیں۔ اصل دستاویز اپنی مادری زبان میں ہی معتبر ماخذ سمجھی جانی چاہیے۔ اہم معلومات کے لیے پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کی ذمہ داری ہم پر عائد نہیں ہوتی۔