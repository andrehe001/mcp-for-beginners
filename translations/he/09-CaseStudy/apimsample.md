<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "36de9fae488d6de554d969fe8e0801a8",
  "translation_date": "2025-06-20T19:22:15+00:00",
  "source_file": "09-CaseStudy/apimsample.md",
  "language_code": "he"
}
-->
# מחקר מקרה: חשיפת REST API ב-API Management כשרת MCP

Azure API Management היא שירות שמספק שער (Gateway) מעל נקודות הקצה של ה-API שלך. האופן שבו זה עובד הוא ש-Azure API Management מתפקד כפרוקסי מול ה-APIs שלך ויכול להחליט מה לעשות עם הבקשות הנכנסות.

על ידי השימוש בו, אתה מוסיף מגוון רחב של תכונות כמו:

- **אבטחה**, ניתן להשתמש בכל דבר ממפתחות API, JWT ועד זהות מנוהלת.
- **הגבלת תעבורה**, תכונה מצוינת היא היכולת להחליט כמה קריאות יעברו בפרק זמן מסוים. זה עוזר לוודא שלכל המשתמשים תהיה חווית שימוש טובה וגם שהשירות שלך לא יעמוס בבקשות.
- **קנה מידה ואיזון עומסים**. ניתן להגדיר מספר נקודות קצה לאיזון העומס וגם להחליט איך לבצע את "איזון העומס".
- **תכונות AI כמו semantic caching**, הגבלת טוקנים ומעקב אחר טוקנים ועוד. אלו תכונות מצוינות שמשפרות את התגובה וגם עוזרות לך לשלוט בהוצאות הטוקנים שלך. [קרא עוד כאן](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## למה MCP + Azure API Management?

Model Context Protocol הופך במהירות לסטנדרט עבור אפליקציות AI אגנטיות ואופן החשיפה של כלים ונתונים בצורה עקבית. Azure API Management היא הבחירה הטבעית כשצריך "לנהל" APIs. שרתי MCP משתלבים לעיתים קרובות עם APIs אחרים כדי לפתור בקשות לכלי מסוים, למשל. לכן, שילוב בין Azure API Management ל-MCP הוא הגיוני מאוד.

## סקירה כללית

במקרה השימוש הספציפי הזה נלמד כיצד לחשוף נקודות קצה של API כשרת MCP. באמצעות זאת, נוכל להפוך את נקודות הקצה הללו לחלק מאפליקציה אגנטית תוך ניצול התכונות של Azure API Management.

## תכונות עיקריות

- אתה בוחר את שיטות נקודת הקצה שברצונך לחשוף ככלים.
- התכונות הנוספות שתקבל תלויות במה שתגדיר במדור המדיניות של ה-API שלך. כאן נראה כיצד ניתן להוסיף הגבלת תעבורה.

## שלב מקדים: ייבוא API

אם כבר יש לך API ב-Azure API Management, מצוין, תוכל לדלג על שלב זה. אם לא, עיין בקישור הבא, [ייבוא API ל-Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## חשיפת API כשרת MCP

כדי לחשוף את נקודות הקצה של ה-API, נעקוב אחרי השלבים הבאים:

1. עבור ל-Azure Portal בכתובת <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
נווט למופע של API Management שלך.

1. בתפריט השמאלי, בחר APIs > MCP Servers > + Create new MCP Server.

1. ב-API, בחר REST API שברצונך לחשוף כשרת MCP.

1. בחר פעולה או יותר של API שברצונך לחשוף ככלים. ניתן לבחור את כל הפעולות או רק פעולות ספציפיות.

    ![בחר שיטות לחשיפה](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. בחר **Create**.

1. עבור לתפריט **APIs** ו-**MCP Servers**, תראה את המסך הבא:

    ![ראה את שרת MCP בחלונית הראשית](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    שרת MCP נוצר ופעולות ה-API נחשפות ככלים. שרת ה-MCP מופיע בחלונית MCP Servers. עמודת ה-URL מציגה את נקודת הקצה של שרת MCP שניתן לקרוא לה לצורך בדיקות או בתוך אפליקציית לקוח.

## אופציונלי: הגדרת מדיניות

ל-Azure API Management יש את המושג המרכזי של מדיניות (policies) שבהן מגדירים כללים שונים לנקודות הקצה, כמו הגבלת תעבורה או semantic caching. המדיניות נכתבת בפורמט XML.

כך ניתן להגדיר מדיניות להגבלת תעבורה לשרת MCP שלך:

1. בפורטל, תחת APIs, בחר **MCP Servers**.

1. בחר את שרת MCP שיצרת.

1. בתפריט השמאלי, תחת MCP, בחר **Policies**.

1. בעורך המדיניות, הוסף או ערוך את המדיניות שברצונך להחיל על כלים של שרת MCP. המדיניות מוגדרת בפורמט XML. לדוגמה, ניתן להוסיף מדיניות להגבלת קריאות לכלים של שרת MCP (בדוגמה זו, 5 קריאות כל 30 שניות לכתובת IP של לקוח). כך נראה קוד XML שיגביל את התעבורה:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    הנה תמונה של עורך המדיניות:

    ![עורך מדיניות](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## נסה את זה

בואו נוודא ששרת MCP שלנו פועל כמתוכנן.

לשם כך, נשתמש ב-Visual Studio Code וב-GitHub Copilot במצב Agent. נוסיף את שרת MCP לקובץ *mcp.json*. כך, Visual Studio Code יתפקד כלקוח עם יכולות אגנטיות והמשתמשים יוכלו להקליד בקשה ולתקשר עם השרת.

כך מוסיפים את שרת MCP ב-Visual Studio Code:

1. השתמש בפקודה MCP: **Add Server מה-Command Palette**.

1. כאשר תתבקש, בחר את סוג השרת: **HTTP (HTTP or Server Sent Events)**.

1. הזן את ה-URL של שרת MCP ב-API Management. לדוגמה: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (לנקודת קצה SSE) או **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (לנקודת קצה MCP), שים לב להבדל בין הפרוטוקולים `/sse` or `/mcp`.

1. הזן מזהה שרת לפי בחירתך. ערך זה אינו קריטי אך יעזור לך לזכור מהו מופע השרת.

1. בחר אם לשמור את ההגדרות בהגדרות סביבת העבודה או בהגדרות המשתמש.

  - **הגדרות סביבת עבודה** - תצורת השרת נשמרת בקובץ .vscode/mcp.json הזמין רק בסביבת העבודה הנוכחית.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    או אם בחרת ב-HTTP Streaming כפרוטוקול, זה יהיה מעט שונה:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **הגדרות משתמש** - תצורת השרת מתווספת לקובץ הגדרות הגלובלי *settings.json* וזמינה בכל סביבת עבודה. התצורה נראית כך:

    ![הגדרת משתמש](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. בנוסף, יש להוסיף הגדרה של כותרת (header) לוודא אימות תקין מול Azure API Management. הכותרת נקראת **Ocp-Apim-Subscription-Key**.

    - כך מוסיפים אותה להגדרות:

    ![הוספת כותרת לאימות](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), זה יגרום להופעת תיבת שאלה להזנת מפתח ה-API שניתן למצוא ב-Azure Portal במופע Azure API Management שלך.

   - להוספה ל-*mcp.json* במקום זאת, ניתן להוסיף כך:

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

### שימוש במצב Agent

כעת הכל מוכן, בין אם בהגדרות המשתמש או בקובץ *.vscode/mcp.json*. בואו ננסה.

צריכה להופיע אייקון כלים (Tools) כך, שבו מופיעים הכלים החשופים מהשרת שלך:

![כלים מהשרת](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. לחץ על אייקון הכלים ותראה רשימת כלים כך:

    ![כלים](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. הזן בקשה בצ'אט כדי להפעיל את הכלי. לדוגמה, אם בחרת כלי לקבלת מידע על הזמנה, תוכל לשאול את האגנט לגבי הזמנה. הנה דוגמת בקשה:

    ```text
    get information from order 2
    ```

    כעת תוצג לך אייקון כלים שיבקש להמשיך ולהפעיל את הכלי. בחר להמשיך בהרצת הכלי, כעת תראה פלט כך:

    ![תוצאה מהבקשה](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **מה שאתה רואה למעלה תלוי בכלים שהגדרת, אבל הרעיון הוא שתקבל תגובה טקסטואלית כזו**

## מקורות

כך תוכל ללמוד עוד:

- [מדריך על Azure API Management ו-MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [דוגמת Python: אבטחת שרתי MCP מרוחקים באמצעות Azure API Management (ניסיוני)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [מעבדת הרשאות לקוח MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [שימוש בתוסף Azure API Management ל-VS Code לייבוא וניהול APIs](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [רישום וגילוי שרתי MCP מרוחקים ב-Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) מאגר מצוין שמציג יכולות AI רבות עם Azure API Management
- [סדנאות AI Gateway](https://azure-samples.github.io/AI-Gateway/) מכיל סדנאות בשימוש ב-Azure Portal, דרך מצוינת להתחיל להעריך יכולות AI.

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון כי תרגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית נחשב למקור הסמכותי. למידע קריטי מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. איננו אחראים לכל אי-הבנות או פרשנויות שגויות הנובעות משימוש בתרגום זה.