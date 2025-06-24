<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:31:11+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "he"
}
-->
# מחולל תוכנית לימודים עם Chainlit ומסמכי Microsoft Learn Docs MCP

## דרישות מוקדמות

- Python 3.8 ומעלה  
- pip (מנהל חבילות של Python)  
- חיבור לאינטרנט כדי להתחבר לשרת Microsoft Learn Docs MCP  

## התקנה

1. שכפל את המאגר הזה או הורד את קבצי הפרויקט.  
2. התקן את התלויות הנדרשות:  

   ```bash
   pip install -r requirements.txt
   ```  

## שימוש

### תרחיש 1: שאילתה פשוטה ל-Docs MCP  
לקוח שורת פקודה שמתחבר לשרת Docs MCP, שולח שאילתה ומדפיס את התוצאה.  

1. הרץ את הסקריפט:  
   ```bash
   python scenario1.py
   ```  
2. הזן את שאלת התיעוד שלך בהנחיה.  

### תרחיש 2: מחולל תוכנית לימודים (אפליקציית ווב Chainlit)  
ממשק ווב (בשימוש Chainlit) המאפשר למשתמשים ליצור תוכנית לימודים אישית שבוע-אחר-שבוע לכל נושא טכני.  

1. הפעל את אפליקציית Chainlit:  
   ```bash
   chainlit run scenario2.py
   ```  
2. פתח את כתובת ה-URL המקומית שמופיעה במסוף שלך (למשל http://localhost:8000) בדפדפן.  
3. בחלון הצ'אט, הזן את נושא הלימוד שלך ואת מספר השבועות שברצונך ללמוד (למשל "AI-900 certification, 8 weeks").  
4. האפליקציה תחזיר תוכנית לימודים שבועית, כולל קישורים לתיעוד הרלוונטי של Microsoft Learn.  

**משתני סביבה נדרשים:**  

כדי להשתמש בתרחיש 2 (אפליקציית ווב Chainlit עם Azure OpenAI), יש להגדיר את משתני הסביבה הבאים בתיקיית `.env` file in the `python`:  

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```  

מלא את הערכים האלה בפרטי המשאבים שלך ב-Azure OpenAI לפני הרצת האפליקציה.  

> **[!TIP]** ניתן לפרוס בקלות מודלים משלך באמצעות [Azure AI Foundry](https://ai.azure.com/).  

### תרחיש 3: תיעוד בתוך עורך עם שרת MCP ב-VS Code  

במקום לעבור בין לשוניות בדפדפן כדי לחפש תיעוד, ניתן להביא את Microsoft Learn Docs ישירות ל-VS Code שלך באמצעות שרת MCP. זה מאפשר לך:  
- לחפש ולקרוא תיעוד בתוך VS Code מבלי לצאת מסביבת הפיתוח שלך.  
- להפנות לתיעוד ולהכניס קישורים ישירות לקבצי README או קורסים.  
- להשתמש ב-GitHub Copilot וב-MCP יחד לעבודה חלקה ומונעת בינה מלאכותית עם תיעוד.  

**דוגמאות לשימוש:**  
- להוסיף במהירות קישורי הפניה ל-README בזמן כתיבת תיעוד לקורס או לפרויקט.  
- להשתמש ב-Copilot ליצירת קוד ו-MCP למציאת תיעוד רלוונטי וציטוטו מיד.  
- להישאר מרוכז בעורך ולהגביר את הפרודוקטיביות.  

> [!IMPORTANT]  
> ודא שיש לך קובץ [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

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
- `Cloud architecture, 9 weeks`] תקין.  

דוגמאות אלו ממחישות את הגמישות של האפליקציה למטרות ולמסגרות זמן שונות ללמידה.  

## מקורות  

- [תיעוד Chainlit](https://docs.chainlit.io/)  
- [תיעוד MCP](https://github.com/MicrosoftDocs/mcp)

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתירגומים אוטומטיים עלולים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפת המקור שלו יש להיחשב כמקור הסמכותי. עבור מידע קריטי, מומלץ להיעזר בתרגום מקצועי על ידי אדם. איננו אחראים לכל אי-הבנות או פרשנויות שגויות הנובעות משימוש בתרגום זה.