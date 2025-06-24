<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5384bbb2a92d00d5d7e66274dbe0331d",
  "translation_date": "2025-06-20T18:20:35+00:00",
  "source_file": "04-PracticalImplementation/README.md",
  "language_code": "ar"
}
-->
# التنفيذ العملي

التنفيذ العملي هو المكان الذي يصبح فيه تأثير بروتوكول سياق النموذج (MCP) ملموسًا. بينما يعد فهم النظرية والهندسة المعمارية وراء MCP أمرًا مهمًا، تظهر القيمة الحقيقية عند تطبيق هذه المفاهيم لبناء واختبار ونشر حلول تحل مشكلات العالم الحقيقي. هذا الفصل يجسر الفجوة بين المعرفة النظرية والتطوير العملي، ويرشدك خلال عملية تحويل تطبيقات MCP إلى واقع.

سواء كنت تطور مساعدين ذكيين، أو تدمج الذكاء الاصطناعي في سير عمل الأعمال، أو تبني أدوات مخصصة لمعالجة البيانات، يوفر MCP أساسًا مرنًا. تصميمه المستقل عن اللغة وSDKs الرسمية للغات البرمجة الشائعة يجعله متاحًا لشريحة واسعة من المطورين. من خلال الاستفادة من هذه SDKs، يمكنك بسرعة إنشاء نماذج أولية، والتكرار، وتوسيع حلولك عبر منصات وبيئات مختلفة.

في الأقسام التالية، ستجد أمثلة عملية، وأكواد نموذجية، واستراتيجيات نشر توضح كيفية تنفيذ MCP في C#، وJava، وTypeScript، وJavaScript، وPython. ستتعلم أيضًا كيفية تصحيح الأخطاء واختبار خوادم MCP، وإدارة واجهات برمجة التطبيقات، ونشر الحلول على السحابة باستخدام Azure. هذه الموارد العملية مصممة لتسريع تعلمك ومساعدتك على بناء تطبيقات MCP قوية وجاهزة للإنتاج بثقة.

## نظرة عامة

يركز هذا الدرس على الجوانب العملية لتنفيذ MCP عبر عدة لغات برمجة. سنستعرض كيفية استخدام SDKs الخاصة بـ MCP في C#، وJava، وTypeScript، وJavaScript، وPython لبناء تطبيقات متينة، وتصحيح واختبار خوادم MCP، وإنشاء موارد وقوالب وأدوات قابلة لإعادة الاستخدام.

## أهداف التعلم

بنهاية هذا الدرس، ستكون قادرًا على:
- تنفيذ حلول MCP باستخدام SDKs الرسمية في لغات برمجة مختلفة
- تصحيح واختبار خوادم MCP بشكل منهجي
- إنشاء واستخدام ميزات الخادم (الموارد، والقوالب، والأدوات)
- تصميم سير عمل فعال لـ MCP للمهام المعقدة
- تحسين تنفيذ MCP من حيث الأداء والموثوقية

## الموارد الرسمية لـ SDK

يوفر بروتوكول سياق النموذج SDKs رسمية لعدة لغات:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) 
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

## العمل مع SDKs الخاصة بـ MCP

يقدم هذا القسم أمثلة عملية لتنفيذ MCP عبر عدة لغات برمجة. يمكنك العثور على أكواد نموذجية في دليل `samples` منظم حسب اللغة.

### العينات المتاحة

يحتوي المستودع على [تنفيذات نموذجية](../../../04-PracticalImplementation/samples) باللغات التالية:

- [C#](./samples/csharp/README.md)
- [Java](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

كل عينة توضح مفاهيم MCP الأساسية وأنماط التنفيذ الخاصة باللغة والنظام البيئي المعني.

## الميزات الأساسية للخادم

يمكن لخوادم MCP تنفيذ أي مزيج من هذه الميزات:

### الموارد
توفر الموارد السياق والبيانات للمستخدم أو نموذج الذكاء الاصطناعي للاستخدام:
- مستودعات الوثائق
- قواعد المعرفة
- مصادر البيانات المهيكلة
- أنظمة الملفات

### القوالب
القوالب هي رسائل وسير عمل مصممة مسبقًا للمستخدمين:
- قوالب محادثة محددة مسبقًا
- أنماط تفاعل موجهة
- هياكل حوار متخصصة

### الأدوات
الأدوات هي وظائف يمكن للنموذج الذكي تنفيذها:
- أدوات معالجة البيانات
- تكاملات واجهات برمجة التطبيقات الخارجية
- قدرات حسابية
- وظيفة البحث

## تنفيذات نموذجية: C#

يحتوي مستودع SDK الرسمي لـ C# على عدة تنفيذات نموذجية توضح جوانب مختلفة من MCP:

- **عميل MCP بسيط**: مثال بسيط يوضح كيفية إنشاء عميل MCP واستدعاء الأدوات
- **خادم MCP بسيط**: تنفيذ خادم بسيط مع تسجيل أدوات أساسي
- **خادم MCP متقدم**: خادم كامل الميزات مع تسجيل الأدوات، والمصادقة، ومعالجة الأخطاء
- **تكامل ASP.NET**: أمثلة توضح التكامل مع ASP.NET Core
- **أنماط تنفيذ الأدوات**: أنماط مختلفة لتنفيذ الأدوات بمستويات تعقيد متنوعة

SDK الخاص بـ MCP في C# في مرحلة المعاينة وقد تتغير واجهات برمجة التطبيقات. سنستمر في تحديث هذه المدونة مع تطور SDK.

### الميزات الرئيسية
- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)

- بناء [أول خادم MCP](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

للحصول على عينات تنفيذ كاملة لـ C#، قم بزيارة [مستودع عينات SDK الرسمي لـ C#](https://github.com/modelcontextprotocol/csharp-sdk)

## تنفيذ نموذجي: تنفيذ Java

يوفر SDK الخاص بـ Java خيارات تنفيذ MCP قوية مع ميزات بمستوى المؤسسات.

### الميزات الرئيسية

- تكامل مع Spring Framework
- أمان قوي للأنواع
- دعم البرمجة التفاعلية
- معالجة شاملة للأخطاء

لعينة تنفيذ Java كاملة، انظر [عينة Java](samples/java/containerapp/README.md) في دليل العينات.

## تنفيذ نموذجي: تنفيذ JavaScript

يوفر SDK الخاص بـ JavaScript نهجًا خفيف الوزن ومرنًا لتنفيذ MCP.

### الميزات الرئيسية

- دعم Node.js والمتصفحات
- واجهة برمجة تطبيقات قائمة على الوعود
- تكامل سهل مع Express وأطر عمل أخرى
- دعم WebSocket للبث المباشر

لعينة تنفيذ JavaScript كاملة، انظر [عينة JavaScript](samples/javascript/README.md) في دليل العينات.

## تنفيذ نموذجي: تنفيذ Python

يوفر SDK الخاص بـ Python نهجًا بيثونيًا لتنفيذ MCP مع تكامل ممتاز لأطر تعلم الآلة.

### الميزات الرئيسية

- دعم async/await مع asyncio
- تكامل مع Flask وFastAPI
- تسجيل أدوات بسيط
- تكامل أصلي مع مكتبات تعلم الآلة الشهيرة

لعينة تنفيذ Python كاملة، انظر [عينة Python](samples/python/README.md) في دليل العينات.

## إدارة API

تعد إدارة واجهات برمجة التطبيقات في Azure إجابة ممتازة على كيفية تأمين خوادم MCP. الفكرة هي وضع مثيل Azure API Management أمام خادم MCP الخاص بك وتركه يتولى ميزات قد تحتاجها مثل:

- تحديد معدلات الاستخدام
- إدارة الرموز
- المراقبة
- موازنة التحميل
- الأمان

### عينة Azure

إليك عينة Azure تقوم بذلك بالضبط، أي [إنشاء خادم MCP وتأمينه باستخدام Azure API Management](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

شاهد كيف تتم عملية التفويض في الصورة أدناه:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true) 

في الصورة السابقة، يحدث ما يلي:

- تتم عملية المصادقة/التفويض باستخدام Microsoft Entra.
- تعمل Azure API Management كبوابة وتستخدم السياسات لتوجيه وإدارة حركة المرور.
- يقوم Azure Monitor بتسجيل جميع الطلبات للتحليل المستقبلي.

#### تدفق التفويض

لنلق نظرة أكثر تفصيلًا على تدفق التفويض:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### مواصفة تفويض MCP

تعرف أكثر على [مواصفة تفويض MCP](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization#2-10-third-party-authorization-flow)

## نشر خادم MCP عن بُعد على Azure

لنرَ إن كان بإمكاننا نشر العينة التي ذكرناها سابقًا:

1. استنساخ المستودع

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

2. سجل `Microsoft.App` resource provider.
    * If you are using Azure CLI, run `az provider register --namespace Microsoft.App --wait`.
    * If you are using Azure PowerShell, run `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Then run `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` وبعد فترة تحقق مما إذا كانت التسجيل قد اكتمل.

3. شغّل هذا الأمر [azd](https://aka.ms/azd) لتوفير خدمة إدارة API، وتطبيق الوظائف (مع الكود) وجميع موارد Azure المطلوبة الأخرى

    ```shell
    azd up
    ```

    يجب أن تنشر هذه الأوامر جميع الموارد السحابية على Azure

### اختبار الخادم باستخدام MCP Inspector

1. في **نافذة طرفية جديدة**، قم بتثبيت وتشغيل MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    يجب أن ترى واجهة مشابهة لـ:

    ![Connect to Node inspector](../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.ar.png) 

2. اضغط CTRL وانقر لتحميل تطبيق MCP Inspector من العنوان الذي يعرضه التطبيق (مثل http://127.0.0.1:6274/#resources)
3. اضبط نوع النقل إلى `SSE`
1. Set the URL to your running API Management SSE endpoint displayed after `azd up` واضغط **Connect**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

5. **عرض الأدوات**. انقر على أداة واضغط **Run Tool**.

إذا نجحت كل الخطوات، يجب أن تكون متصلًا الآن بخادم MCP وتمكنت من استدعاء أداة.

## خوادم MCP لـ Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): مجموعة من المستودعات هي قوالب بدء سريعة لبناء ونشر خوادم MCP مخصصة عن بُعد باستخدام Azure Functions مع Python، وC# .NET، أو Node/TypeScript.

توفر العينات حلاً كاملاً يسمح للمطورين بـ:

- البناء والتشغيل محليًا: تطوير وتصحيح خادم MCP على جهاز محلي
- النشر على Azure: نشر سهل إلى السحابة بأمر azd up بسيط
- الاتصال من العملاء: الاتصال بخادم MCP من عملاء مختلفين بما في ذلك وضع وكيل Copilot في VS Code وأداة MCP Inspector

### الميزات الرئيسية:

- الأمان من التصميم: خادم MCP مؤمن باستخدام المفاتيح وHTTPS
- خيارات المصادقة: يدعم OAuth باستخدام المصادقة المدمجة و/أو إدارة API
- عزل الشبكة: يسمح بالعزل الشبكي باستخدام شبكات Azure الافتراضية (VNET)
- بنية بدون خادم: يستفيد من Azure Functions للتنفيذ القابل للتوسع والموجه بالأحداث
- تطوير محلي: دعم شامل للتطوير المحلي وتصحيح الأخطاء
- نشر بسيط: عملية نشر مبسطة إلى Azure

يحتوي المستودع على جميع ملفات التكوين اللازمة، والكود المصدري، وتعريفات البنية التحتية للبدء بسرعة بتنفيذ خادم MCP جاهز للإنتاج.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - تنفيذ نموذجي لـ MCP باستخدام Azure Functions مع Python

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - تنفيذ نموذجي لـ MCP باستخدام Azure Functions مع C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - تنفيذ نموذجي لـ MCP باستخدام Azure Functions مع Node/TypeScript.

## النقاط الرئيسية

- توفر SDKs الخاصة بـ MCP أدوات مخصصة لكل لغة لتنفيذ حلول MCP متينة
- عملية تصحيح الأخطاء والاختبار ضرورية لتطبيقات MCP موثوقة
- قوالب القوالب القابلة لإعادة الاستخدام تمكّن تفاعلات ذكاء اصطناعي متسقة
- يمكن لسير العمل المصمم جيدًا تنسيق مهام معقدة باستخدام أدوات متعددة
- يتطلب تنفيذ حلول MCP مراعاة الأمان، والأداء، ومعالجة الأخطاء

## تمرين

صمم سير عمل MCP عملي يعالج مشكلة حقيقية في مجالك:

1. حدد 3-4 أدوات ستكون مفيدة لحل هذه المشكلة
2. أنشئ مخطط سير عمل يوضح كيفية تفاعل هذه الأدوات
3. نفذ نسخة أساسية من إحدى الأدوات باستخدام لغتك المفضلة
4. أنشئ قالبًا يساعد النموذج على استخدام أداتك بفعالية

## موارد إضافية


---

التالي: [مواضيع متقدمة](../05-AdvancedTopics/README.md)

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمة الترجمة الآلية [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر المعتمد. للمعلومات الهامة، يُنصح بالترجمة البشرية المهنية. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.