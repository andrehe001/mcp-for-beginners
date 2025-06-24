<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "36de9fae488d6de554d969fe8e0801a8",
  "translation_date": "2025-06-20T19:13:50+00:00",
  "source_file": "09-CaseStudy/apimsample.md",
  "language_code": "ar"
}
-->
# دراسة حالة: كشف واجهة REST API في إدارة واجهات برمجة التطبيقات كخادم MCP

تُعد Azure API Management خدمة توفر بوابة فوق نقاط نهاية واجهات برمجة التطبيقات الخاصة بك. طريقة عملها هي أن Azure API Management تعمل كوكيل أمام واجهات برمجة التطبيقات الخاصة بك ويمكنها اتخاذ قرار بشأن كيفية التعامل مع الطلبات الواردة.

باستخدامها، تضيف مجموعة كاملة من الميزات مثل:

- **الأمان**، يمكنك استخدام كل شيء من مفاتيح API، JWT إلى الهوية المدارة.
- **تحديد معدل الطلبات**، ميزة رائعة تمكنك من تحديد عدد المكالمات التي تمر خلال وحدة زمنية معينة. هذا يساعد في ضمان تجربة ممتازة لجميع المستخدمين وأيضًا في منع إغراق خدمتك بالطلبات.
- **التحجيم وتوزيع الحمل**. يمكنك إعداد عدة نقاط نهاية لتوزيع الحمل ويمكنك أيضًا تحديد كيفية "توزيع الحمل".
- **ميزات الذكاء الاصطناعي مثل التخزين المؤقت الدلالي**، حد الرموز ومراقبة الرموز والمزيد. هذه ميزات رائعة تحسن سرعة الاستجابة وتساعدك أيضًا في مراقبة استهلاك الرموز لديك. [اقرأ المزيد هنا](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## لماذا MCP + Azure API Management؟

بروتوكول سياق النموذج (Model Context Protocol) أصبح بسرعة معيارًا لتطبيقات الذكاء الاصطناعي الوكيلة وكيفية كشف الأدوات والبيانات بطريقة متسقة. Azure API Management هو خيار طبيعي عندما تحتاج إلى "إدارة" واجهات برمجة التطبيقات. غالبًا ما تتكامل خوادم MCP مع واجهات برمجة تطبيقات أخرى لحل الطلبات لأداة معينة، على سبيل المثال. لذلك، يجمع دمج Azure API Management و MCP بين أفضل الميزات.

## نظرة عامة

في هذه الحالة الخاصة، سنتعلم كيفية كشف نقاط نهاية API كخادم MCP. من خلال ذلك، يمكننا بسهولة جعل هذه النقاط جزءًا من تطبيق وكيل بالإضافة إلى الاستفادة من ميزات Azure API Management.

## الميزات الرئيسية

- تختار طرق النقاط النهائية التي تريد كشفها كأدوات.
- الميزات الإضافية التي تحصل عليها تعتمد على ما تقوم بتكوينه في قسم السياسة لواجهة برمجة التطبيقات الخاصة بك. لكن هنا سنوضح لك كيفية إضافة تحديد معدل الطلبات.

## خطوة تمهيدية: استيراد API

إذا كان لديك API في Azure API Management بالفعل، فهذا رائع، يمكنك تخطي هذه الخطوة. إذا لم يكن كذلك، اطلع على هذا الرابط، [استيراد API إلى Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## كشف API كخادم MCP

لكشف نقاط نهاية API، دعنا نتبع الخطوات التالية:

1. انتقل إلى بوابة Azure والعنوان التالي <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
انتقل إلى مثيل إدارة API الخاص بك.

1. في القائمة اليسرى، اختر APIs > MCP Servers > + إنشاء خادم MCP جديد.

1. في API، اختر REST API للكشف عنه كخادم MCP.

1. اختر عملية أو أكثر من عمليات API للكشف عنها كأدوات. يمكنك اختيار جميع العمليات أو عمليات محددة فقط.

    ![اختر الطرق للكشف](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. اختر **إنشاء**.

1. انتقل إلى خيار القائمة **APIs** و**MCP Servers**، يجب أن ترى التالي:

    ![رؤية خادم MCP في اللوحة الرئيسية](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    تم إنشاء خادم MCP وتم كشف عمليات API كأدوات. يظهر خادم MCP في لوحة MCP Servers. يعرض عمود URL نقطة نهاية خادم MCP التي يمكنك الاتصال بها للاختبار أو ضمن تطبيق عميل.

## اختياري: تكوين السياسات

تحتوي Azure API Management على مفهوم أساسي يسمى السياسات حيث تقوم بإعداد قواعد مختلفة لنقاط النهاية الخاصة بك مثل تحديد معدل الطلبات أو التخزين المؤقت الدلالي. تُكتب هذه السياسات بصيغة XML.

إليك كيفية إعداد سياسة لتحديد معدل طلبات خادم MCP الخاص بك:

1. في البوابة، تحت APIs، اختر **MCP Servers**.

1. اختر خادم MCP الذي أنشأته.

1. في القائمة اليسرى، تحت MCP، اختر **Policies**.

1. في محرر السياسات، أضف أو حرر السياسات التي تريد تطبيقها على أدوات خادم MCP. تُعرف السياسات بصيغة XML. على سبيل المثال، يمكنك إضافة سياسة لتحديد عدد المكالمات إلى أدوات خادم MCP (في هذا المثال، 5 مكالمات لكل 30 ثانية لكل عنوان IP عميل). هذا هو XML الذي سيؤدي إلى تحديد معدل الطلبات:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    هذه صورة لمحرر السياسات:

    ![محرر السياسات](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## جربها

لنتأكد من أن خادم MCP يعمل كما هو متوقع.

لهذا، سنستخدم Visual Studio Code و GitHub Copilot ووضع الوكيل الخاص به. سنضيف خادم MCP إلى *mcp.json*. من خلال ذلك، سيعمل Visual Studio Code كعميل بقدرات وكيلة وسيتمكن المستخدمون النهائيون من كتابة مطالبات والتفاعل مع هذا الخادم.

لنر كيف نضيف خادم MCP في Visual Studio Code:

1. استخدم أمر MCP: **Add Server من لوحة الأوامر**.

1. عند الطلب، اختر نوع الخادم: **HTTP (HTTP أو Server Sent Events)**.

1. أدخل عنوان URL الخاص بخادم MCP في إدارة API. مثال: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (لنقطة نهاية SSE) أو **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (لنقطة نهاية MCP)، لاحظ الفرق بين وسائل النقل هو `/sse` or `/mcp`.

1. أدخل معرف خادم من اختيارك. هذه القيمة ليست مهمة لكنها ستساعدك على تذكر هذه النسخة من الخادم.

1. اختر ما إذا كنت تريد حفظ التكوين في إعدادات مساحة العمل أو إعدادات المستخدم.

  - **إعدادات مساحة العمل** - يتم حفظ تكوين الخادم في ملف .vscode/mcp.json المتاح فقط في مساحة العمل الحالية.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    أو إذا اخترت HTTP التدفق كوسيلة نقل، سيكون مختلفًا قليلاً:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **إعدادات المستخدم** - يتم إضافة تكوين الخادم إلى ملف *settings.json* العام الخاص بك ومتاحة في جميع مساحات العمل. يبدو التكوين مشابهًا لما يلي:

    ![إعداد المستخدم](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. تحتاج أيضًا إلى إضافة تكوين، رأس للتأكد من المصادقة بشكل صحيح تجاه Azure API Management. يستخدم رأسًا يسمى **Ocp-Apim-Subscription-Key**.

    - إليك كيفية إضافته إلى الإعدادات:

    ![إضافة رأس للمصادقة](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png)، هذا سيؤدي إلى عرض مطالبة تطلب منك قيمة مفتاح API التي يمكنك العثور عليها في بوابة Azure لمثيل Azure API Management الخاص بك.

    - لإضافته إلى *mcp.json* بدلاً من ذلك، يمكنك إضافته كما يلي:

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

### استخدام وضع الوكيل

الآن نحن جاهزون في الإعدادات أو في *.vscode/mcp.json*. لنجرّبها.

يجب أن يكون هناك أيقونة أدوات مثل هذه، حيث تُدرج الأدوات المكشوفة من خادمك:

![الأدوات من الخادم](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. اضغط على أيقونة الأدوات ويجب أن ترى قائمة بالأدوات مثل هذه:

    ![الأدوات](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. أدخل مطالبة في الدردشة لاستدعاء الأداة. على سبيل المثال، إذا اخترت أداة للحصول على معلومات حول طلب، يمكنك سؤال الوكيل عن طلب. إليك مثالًا على مطالبة:

    ```text
    get information from order 2
    ```

    ستُعرض لك الآن أيقونة أدوات تطلب منك المتابعة لاستدعاء أداة. اختر المتابعة لتشغيل الأداة، يجب أن ترى الآن ناتجًا مثل هذا:

    ![النتيجة من المطالبة](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **ما تراه أعلاه يعتمد على الأدوات التي قمت بإعدادها، لكن الفكرة هي أنك تحصل على استجابة نصية كما في المثال أعلاه**

## المراجع

إليك كيف يمكنك معرفة المزيد:

- [الدليل التعليمي حول Azure API Management و MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [مثال بايثون: تأمين خوادم MCP البعيدة باستخدام Azure API Management (تجريبي)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [مختبر تفويض عميل MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [استخدام امتداد Azure API Management لـ VS Code لاستيراد وإدارة APIs](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [تسجيل واكتشاف خوادم MCP البعيدة في Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [بوابة الذكاء الاصطناعي](https://github.com/Azure-Samples/AI-Gateway) مستودع رائع يعرض العديد من قدرات الذكاء الاصطناعي مع Azure API Management
- [ورش عمل بوابة الذكاء الاصطناعي](https://azure-samples.github.io/AI-Gateway/) تحتوي على ورش عمل باستخدام بوابة Azure، وهي طريقة رائعة لبدء تقييم قدرات الذكاء الاصطناعي.

**إخلاء مسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق به. للمعلومات الهامة، يُنصح بالاعتماد على الترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير خاطئ ناتج عن استخدام هذه الترجمة.