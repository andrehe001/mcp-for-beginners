<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:32:11+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "hu"
}
-->
# Tanulási Terv Generátor Chainlit-tel és Microsoft Learn Docs MCP-vel

## Előfeltételek

- Python 3.8 vagy újabb
- pip (Python csomagkezelő)
- Internetkapcsolat a Microsoft Learn Docs MCP szerverhez való csatlakozáshoz

## Telepítés

1. Klónozd ezt a tárolót, vagy töltsd le a projekt fájlokat.
2. Telepítsd a szükséges függőségeket:

   ```bash
   pip install -r requirements.txt
   ```

## Használat

### 1. Forgatókönyv: Egyszerű lekérdezés a Docs MCP-hez  
Egy parancssori kliens, amely csatlakozik a Docs MCP szerverhez, lekérdezést küld, majd kiírja az eredményt.

1. Futtasd a scriptet:  
   ```bash
   python scenario1.py
   ```  
2. Írd be a dokumentációs kérdésed a promptnál.

### 2. Forgatókönyv: Tanulási terv generátor (Chainlit webalkalmazás)  
Egy webes felület (Chainlit használatával), amely lehetővé teszi a felhasználók számára, hogy személyre szabott, hétre bontott tanulási tervet készítsenek bármilyen technikai témához.

1. Indítsd el a Chainlit alkalmazást:  
   ```bash
   chainlit run scenario2.py
   ```  
2. Nyisd meg a terminálban megadott helyi URL-t (pl. http://localhost:8000) a böngésződben.  
3. A chat ablakba írd be a tanulási témát és a tanulni kívánt hetek számát (pl. „AI-900 tanúsítvány, 8 hét”).  
4. Az alkalmazás válaszként hétre bontott tanulási tervet ad, beleértve a kapcsolódó Microsoft Learn dokumentáció linkjeit.

**Szükséges környezeti változók:**  

A 2. forgatókönyv (Chainlit webalkalmazás Azure OpenAI-val) használatához a következő környezeti változókat kell beállítani egy `.env` file in the `python` mappában:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Töltsd ki ezeket az értékeket az Azure OpenAI erőforrásod adataival, mielőtt elindítod az alkalmazást.

> **[!TIP]** Könnyedén telepítheted saját modelljeidet az [Azure AI Foundry](https://ai.azure.com/) segítségével.

### 3. Forgatókönyv: Dokumentációs keresés az MCP szerverrel VS Code-ban

Ahelyett, hogy böngészőfület váltanál a dokumentáció kereséséhez, a Microsoft Learn Docs-ot közvetlenül behozhatod a VS Code-ba az MCP szerver segítségével. Ez lehetővé teszi, hogy:  
- Keresd és olvasd a dokumentációt közvetlenül a VS Code-on belül, anélkül, hogy elhagynád a fejlesztői környezetet.  
- Hivatkozz dokumentációkra és illessz be linkeket közvetlenül a README vagy tananyag fájlokba.  
- Használd együtt a GitHub Copilot-ot és az MCP-t egy zökkenőmentes, mesterséges intelligenciával támogatott dokumentációs munkafolyamathoz.

**Példák a használatra:**  
- Gyorsan adj hozzá hivatkozásokat egy README-hez, miközben kurzus- vagy projekt dokumentációt írsz.  
- Használd a Copilot-ot kód generálásra, és az MCP-t releváns dokumentációk azonnali megtalálására és idézésére.  
- Maradj fókuszban a szerkesztődben, és növeld a termelékenységedet.

> [!IMPORTANT]  
> Győződj meg róla, hogy rendelkezel egy érvényes [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

## Why Chainlit for Scenario 2?

Chainlit is a modern open-source framework for building conversational web applications. It makes it easy to create chat-based user interfaces that connect to backend services like the Microsoft Learn Docs MCP server. This project uses Chainlit to provide a simple, interactive way to generate personalized study plans in real time. By leveraging Chainlit, you can quickly build and deploy chat-based tools that enhance productivity and learning.

## What This Does

This app allows users to create a personalized study plan by simply entering a topic and a duration. The app parses your input, queries the Microsoft Learn Docs MCP server for relevant content, and organizes the results into a structured, week-by-week plan. Each week’s recommendations are displayed in the chat, making it easy to follow and track your progress. The integration ensures you always get the latest, most relevant learning resources.

## Sample Queries

Try these queries in the chat window to see how the app responds:

- `AI-900 tanúsítvány, 8 hét`
- `Learn Azure Functions, 4 hét`
- `Azure DevOps, 6 hét`
- `Data engineering on Azure, 10 hét`
- `Microsoft security fundamentals, 5 hét`
- `Power Platform, 7 hét`
- `Azure AI services, 12 hét`
- `Cloud architecture, 9 hét`]

Ezek a példák jól mutatják az alkalmazás rugalmasságát különböző tanulási célok és időkeretek esetén.

## Hivatkozások

- [Chainlit dokumentáció](https://docs.chainlit.io/)  
- [MCP dokumentáció](https://github.com/MicrosoftDocs/mcp)

**Jogi nyilatkozat**:  
Ez a dokumentum az AI fordító szolgáltatás, a [Co-op Translator](https://github.com/Azure/co-op-translator) segítségével készült. Bár igyekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum a saját nyelvén tekintendő hivatalos forrásnak. Fontos információk esetén professzionális, emberi fordítást javaslunk. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.