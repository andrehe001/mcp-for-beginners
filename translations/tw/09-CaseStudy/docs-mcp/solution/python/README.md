<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:27:36+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "tw"
}
-->
# 使用 Chainlit 與 Microsoft Learn Docs MCP 的學習計畫產生器

## 先決條件

- Python 3.8 或更新版本
- pip（Python 套件管理工具）
- 可連線至 Microsoft Learn Docs MCP 伺服器的網路連線

## 安裝

1. 將此倉庫克隆或下載專案檔案。
2. 安裝所需的相依套件：

   ```bash
   pip install -r requirements.txt
   ```

## 使用說明

### 情境一：簡單查詢 Docs MCP  
一個命令列用戶端，連接到 Docs MCP 伺服器，傳送查詢並印出結果。

1. 執行腳本：  
   ```bash
   python scenario1.py
   ```  
2. 在提示符號輸入你的文件問題。

### 情境二：學習計畫產生器（Chainlit 網頁應用）  
一個基於網頁的介面（使用 Chainlit），讓使用者能夠為任何技術主題產生個人化的逐週學習計畫。

1. 啟動 Chainlit 應用：  
   ```bash
   chainlit run scenario2.py
   ```  
2. 在瀏覽器中開啟終端機提供的本機網址（例如 http://localhost:8000）。
3. 在聊天視窗輸入你的學習主題與預計學習週數（例如「AI-900 認證，8 週」）。
4. 應用會回覆逐週的學習計畫，並包含相關 Microsoft Learn 文件的連結。

**需要設定的環境變數：**

要使用情境二（搭配 Azure OpenAI 的 Chainlit 網頁應用），必須在 `.env` file in the `python` 目錄中設定以下環境變數：

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

請在執行應用前，填入你的 Azure OpenAI 資源資訊。

> **小提示：** 你可以透過 [Azure AI Foundry](https://ai.azure.com/) 輕鬆部署自己的模型。

### 情境三：在 VS Code 編輯器內使用 MCP 伺服器的文件功能

不必切換瀏覽器分頁搜尋文件，你可以直接在 VS Code 中使用 Microsoft Learn Docs，透過 MCP 伺服器實現以下功能：  
- 在 VS Code 內搜尋和閱讀文件，無需離開開發環境。  
- 直接引用文件並插入連結到 README 或課程檔案中。  
- 結合 GitHub Copilot 與 MCP，打造無縫且 AI 驅動的文件工作流程。

**範例應用場景：**  
- 撰寫課程或專案文件時，快速新增參考連結到 README。  
- 使用 Copilot 產生程式碼，同時利用 MCP 即時找到並引用相關文件。  
- 保持專注於編輯器，提高工作效率。

> [!IMPORTANT]  
> 請確保你擁有有效的 [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

## Why Chainlit for Scenario 2?

Chainlit is a modern open-source framework for building conversational web applications. It makes it easy to create chat-based user interfaces that connect to backend services like the Microsoft Learn Docs MCP server. This project uses Chainlit to provide a simple, interactive way to generate personalized study plans in real time. By leveraging Chainlit, you can quickly build and deploy chat-based tools that enhance productivity and learning.

## What This Does

This app allows users to create a personalized study plan by simply entering a topic and a duration. The app parses your input, queries the Microsoft Learn Docs MCP server for relevant content, and organizes the results into a structured, week-by-week plan. Each week’s recommendations are displayed in the chat, making it easy to follow and track your progress. The integration ensures you always get the latest, most relevant learning resources.

## Sample Queries

Try these queries in the chat window to see how the app responds:

- `AI-900 認證，8 週`
- `Learn Azure Functions，4 週`
- `Azure DevOps，6 週`
- `Data engineering on Azure，10 週`
- `Microsoft security fundamentals，5 週`
- `Power Platform，7 週`
- `Azure AI services，12 週`
- `Cloud architecture，9 週`

這些範例展示了此應用在不同學習目標與時間安排上的彈性。

## 參考資料

- [Chainlit 文件](https://docs.chainlit.io/)  
- [MCP 文件](https://github.com/MicrosoftDocs/mcp)

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們對因使用本翻譯所產生的任何誤解或誤譯概不負責。