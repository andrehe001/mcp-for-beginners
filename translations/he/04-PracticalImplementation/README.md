<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5384bbb2a92d00d5d7e66274dbe0331d",
  "translation_date": "2025-06-20T18:39:28+00:00",
  "source_file": "04-PracticalImplementation/README.md",
  "language_code": "he"
}
-->
# יישום מעשי

היישום המעשי הוא המקום שבו כוחו של Model Context Protocol (MCP) מתגלם במציאות. בעוד שהבנת התיאוריה והארכיטקטורה שמאחורי MCP חשובה, הערך האמיתי מתגלה כאשר אתה מיישם את המושגים האלה כדי לבנות, לבדוק ולפרוס פתרונות הפותרים בעיות אמיתיות. פרק זה גשר בין הידע התיאורטי לפיתוח מעשי, ומנחה אותך בתהליך הבאת יישומים מבוססי MCP לחיים.

בין אם אתה מפתח עוזרים חכמים, משלב AI בתהליכי עבודה עסקיים, או בונה כלים מותאמים לעיבוד נתונים, MCP מספקת בסיס גמיש. העיצוב הנייטרלי לשפה וה-SDKs הרשמיים לשפות תכנות פופולריות הופכים אותו לנגיש למגוון רחב של מפתחים. באמצעות ניצול SDKs אלה, תוכל במהירות ליצור אב-טיפוס, לחזור על תהליכים ולסקייל פתרונות בפלטפורמות וסביבות שונות.

בקטעים הבאים תמצא דוגמאות מעשיות, קודי דוגמה ואסטרטגיות פריסה המדגימות כיצד ליישם MCP ב-C#, Java, TypeScript, JavaScript ו-Python. תלמד גם כיצד לנפות שגיאות ולבדוק את שרתי MCP, לנהל APIs ולפרוס פתרונות לענן באמצעות Azure. המשאבים המעשיים הללו מיועדים להאיץ את הלמידה שלך ולעזור לך לבנות בביטחון יישומי MCP חזקים ומוכנים לפרודקשן.

## סקירה כללית

השיעור מתמקד בהיבטים מעשיים של יישום MCP בשפות תכנות שונות. נבחן כיצד להשתמש ב-SDKs של MCP ב-C#, Java, TypeScript, JavaScript ו-Python כדי לבנות יישומים יציבים, לנפות שגיאות ולבדוק שרתי MCP, וליצור משאבים, פרומפטים וכלים שניתן להשתמש בהם שוב.

## מטרות הלמידה

בסיום השיעור תוכל:
- ליישם פתרונות MCP באמצעות SDKs רשמיים בשפות תכנות שונות
- לנפות שגיאות ולבדוק שרתי MCP באופן שיטתי
- ליצור ולהשתמש בתכונות שרת (משאבים, פרומפטים וכלים)
- לתכנן תהליכי עבודה יעילים ב-MCP למשימות מורכבות
- לאופטם יישומי MCP לביצועים ואמינות

## משאבי SDK רשמיים

Model Context Protocol מציע SDKs רשמיים למספר שפות:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

## עבודה עם SDKs של MCP

בקטע זה מוצגים דוגמאות מעשיות ליישום MCP בשפות תכנות שונות. ניתן למצוא קוד לדוגמה בתיקיית `samples` הממוינת לפי שפה.

### דוגמאות זמינות

הריפוזיטורי כולל [יישומים לדוגמה](../../../04-PracticalImplementation/samples) בשפות הבאות:

- [C#](./samples/csharp/README.md)
- [Java](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

כל דוגמה מדגימה מושגים מרכזיים ודפוסי יישום של MCP בשפה ובאקוסיסטם הספציפיים.

## תכונות מרכזיות של השרת

שרתי MCP יכולים ליישם כל שילוב מהתכונות הבאות:

### משאבים  
משאבים מספקים הקשר ונתונים לשימוש המשתמש או מודל ה-AI:  
- מאגרי מסמכים  
- בסיסי ידע  
- מקורות נתונים מובנים  
- מערכות קבצים  

### פרומפטים  
פרומפטים הם תבניות הודעות ותהליכי עבודה למשתמשים:  
- תבניות שיחה מוגדרות מראש  
- דפוסי אינטראקציה מונחים  
- מבני דיאלוג מיוחדים  

### כלים  
כלים הם פונקציות שהמודל מבצע:  
- כלי עיבוד נתונים  
- אינטגרציות API חיצוניות  
- יכולות חישוביות  
- פונקציות חיפוש  

## דוגמאות ליישום: C#

ריפוזיטורי ה-C# הרשמי כולל מספר דוגמאות ליישום המדגימות היבטים שונים של MCP:

- **לקוח MCP בסיסי**: דוגמה פשוטה שמראה כיצד ליצור לקוח MCP ולהפעיל כלים  
- **שרת MCP בסיסי**: יישום שרת מינימלי עם רישום כלים בסיסי  
- **שרת MCP מתקדם**: שרת מלא עם רישום כלים, אימות וטיפול בשגיאות  
- **אינטגרציה עם ASP.NET**: דוגמאות הממחישות אינטגרציה עם ASP.NET Core  
- **דפוסי יישום כלים**: דפוסים שונים ליישום כלים ברמות מורכבות שונות  

ה-SDK של MCP ל-C# נמצא בבטא וייתכנו שינויים ב-APIs. נמשיך לעדכן את הבלוג ככל שה-SDK יתפתח.

### תכונות מרכזיות  
- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)  
- בניית [שרת MCP ראשון שלך](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).  

למימושים מלאים ב-C#, בקר ב-[ריפוזיטורי דוגמאות ה-C# הרשמי](https://github.com/modelcontextprotocol/csharp-sdk)

## דוגמת יישום: Java

ה-SDK של Java מציע אפשרויות יישום MCP מתקדמות עם תכונות ברמת ארגונית.

### תכונות מרכזיות

- אינטגרציה עם Spring Framework  
- בטיחות טיפוסים גבוהה  
- תמיכה בתכנות ריאקטיבי  
- טיפול שגיאות מקיף  

לדוגמה מלאה של יישום Java, ראה [דוגמת Java](samples/java/containerapp/README.md) בתיקיית הדוגמאות.

## דוגמת יישום: JavaScript

ה-SDK של JavaScript מספק גישה קלה וגמישה ליישום MCP.

### תכונות מרכזיות

- תמיכה ב-Node.js ודפדפן  
- API מבוסס Promises  
- אינטגרציה פשוטה עם Express ומסגרות נוספות  
- תמיכה ב-WebSocket לזרימה  

לדוגמה מלאה של יישום JavaScript, ראה [דוגמת JavaScript](samples/javascript/README.md) בתיקיית הדוגמאות.

## דוגמת יישום: Python

ה-SDK של Python מציע גישה פייתונית ליישום MCP עם אינטגרציות מצוינות למסגרות ML.

### תכונות מרכזיות

- תמיכה ב-async/await עם asyncio  
- אינטגרציה עם Flask ו-FastAPI  
- רישום כלים פשוט  
- אינטגרציה טבעית עם ספריות ML פופולריות  

לדוגמה מלאה של יישום Python, ראה [דוגמת Python](samples/python/README.md) בתיקיית הדוגמאות.

## ניהול API

Azure API Management היא פתרון מצוין לאבטחת שרתי MCP. הרעיון הוא להניח מופע של Azure API Management מול שרת MCP שלך ולתת לו לטפל בתכונות שאתה צפוי לרצות, כגון:

- הגבלת קצב  
- ניהול טוקנים  
- ניטור  
- איזון עומסים  
- אבטחה  

### דוגמת Azure

זוהי דוגמת Azure שעושה בדיוק את זה, כלומר [יצירת שרת MCP ואבטחתו באמצעות Azure API Management](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

ראה כיצד מתבצע תהליך האישור בתמונה הבאה:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

בתמונה שלמעלה מתרחשים הדברים הבאים:

- אימות/אישור מתבצע באמצעות Microsoft Entra.  
- Azure API Management משמש כשער ומנהל תעבורה באמצעות מדיניות.  
- Azure Monitor רושם את כל הבקשות לניתוח נוסף.  

#### תהליך האישור

נבחן את תהליך האישור בפירוט רב יותר:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### מפרט האישור של MCP

למידע נוסף על [מפרט האישור של MCP](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization#2-10-third-party-authorization-flow)

## פריסת שרת MCP מרוחק ב-Azure

בוא נראה אם נוכל לפרוס את הדוגמה שהזכרנו קודם:

1. שיבוט הריפוזיטורי

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

2. רישום ספק השירות `Microsoft.App`  
   
    `` resource provider.
    * If you are using Azure CLI, run `az provider register --namespace Microsoft.App --wait`.
    * If you are using Azure PowerShell, run `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Then run `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState`  
   
    לאחר זמן מה, בדוק אם הרישום הושלם.

3. הרץ את הפקודה [azd](https://aka.ms/azd) כדי להקצות את שירות ניהול ה-API, אפליקציית פונקציות (עם קוד) ואת כל משאבי Azure הנדרשים

    ```shell
    azd up
    ```

    פקודה זו אמורה לפרוס את כל משאבי הענן ב-Azure

### בדיקת השרת שלך עם MCP Inspector

1. בחלון טרמינל חדש, התקן והפעל את MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    תראה ממשק דומה ל:

    ![Connect to Node inspector](../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.he.png)

2. לחץ עם CTRL כדי לטעון את אפליקציית הווב של MCP Inspector מה-URL שמוצג על ידי האפליקציה (למשל http://127.0.0.1:6274/#resources)  
3. הגדר את סוג התעבורה ל-`SSE`
1. Set the URL to your running API Management SSE endpoint displayed after `azd up` ולחץ על **Connect**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

5. **רשום כלים**. לחץ על כלי ובצע **Run Tool**.

אם כל השלבים עברו בהצלחה, כעת אתה מחובר לשרת MCP והצלחת להפעיל כלי.

## שרתי MCP ל-Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): אוסף ריפוזיטורים זה הוא תבנית התחלה מהירה לבניית ופריסת שרתי MCP מרוחקים מותאמים אישית באמצעות Azure Functions ב-Python, C# .NET או Node/TypeScript.

הדוגמאות מספקות פתרון שלם המאפשר למפתחים:

- לבנות ולהריץ מקומית: לפתח ולנטרל שרת MCP במחשב מקומי  
- לפרוס ל-Azure: לפרוס בקלות לענן באמצעות פקודת azd up פשוטה  
- להתחבר מלקוחות: להתחבר לשרת MCP מלקוחות שונים כולל מצב סוכן Copilot ב-VS Code וכלי MCP Inspector  

### תכונות מרכזיות:

- אבטחה מובנית: שרת MCP מאובטח באמצעות מפתחות ו-HTTPS  
- אפשרויות אימות: תומך ב-OAuth באמצעות אימות מובנה ו/או API Management  
- בידוד רשת: מאפשר בידוד רשת באמצעות Azure Virtual Networks (VNET)  
- ארכיטקטורה ללא שרת: מנצל Azure Functions לביצוע סקלאבילי ומונחה אירועים  
- פיתוח מקומי: תמיכה מקיפה בפיתוח וניפוי שגיאות מקומי  
- פריסה פשוטה: תהליך פריסה חלק לענן Azure  

הריפוזיטורי כולל את כל קבצי התצורה, קוד המקור והגדרות התשתית הדרושים כדי להתחיל במהירות עם יישום שרת MCP מוכן לפרודקשן.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - דוגמת יישום MCP באמצעות Azure Functions עם Python  
- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - דוגמת יישום MCP באמצעות Azure Functions עם C# .NET  
- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - דוגמת יישום MCP באמצעות Azure Functions עם Node/TypeScript  

## נקודות מרכזיות לזכור

- SDKs של MCP מספקים כלים ספציפיים לשפות ליישום פתרונות MCP יציבים  
- תהליך ניפוי השגיאות והבדיקות קריטי לאמינות יישומי MCP  
- תבניות פרומפט שניתנות לשימוש חוזר מאפשרות אינטראקציות עקביות עם ה-AI  
- תהליכי עבודה מתוכננים היטב יכולים לתזמר משימות מורכבות באמצעות כלים שונים  
- יישום פתרונות MCP דורש התייחסות לאבטחה, ביצועים וטיפול בשגיאות  

## תרגיל

עצב תהליך עבודה מעשי ב-MCP המתמודד עם בעיה אמיתית בתחום שלך:

1. זהה 3-4 כלים שיהיו שימושיים לפתרון הבעיה  
2. צור דיאגרמת תהליך עבודה שמראה כיצד הכלים האלה מתקשרים  
3. יישם גרסה בסיסית של אחד הכלים בשפת התכנות המועדפת עליך  
4. עצב תבנית פרומפט שתעזור למודל להשתמש בכלי שלך בצורה יעילה  

## משאבים נוספים


---

הבא: [נושאים מתקדמים](../05-AdvancedTopics/README.md)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. יש להתייחס למסמך המקורי בשפתו המקורית כמקור הסמכות. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. אנו לא נושאים באחריות לכל אי-הבנה או פרשנות שגויה הנובעת משימוש בתרגום זה.