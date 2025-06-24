<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:27:27+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "hk"
}
-->
# Study Plan Generator with Chainlit & Microsoft Learn Docs MCP

## 前置條件

- Python 3.8 或以上版本
- pip（Python 套件管理工具）
- 可連接 Microsoft Learn Docs MCP 伺服器的網絡

## 安裝

1. 克隆此儲存庫或下載專案檔案。
2. 安裝所需的依賴：

   ```bash
   pip install -r requirements.txt
   ```

## 使用方法

### 情境 1：簡單查詢 Docs MCP  
一個命令行客戶端，連接到 Docs MCP 伺服器，發送查詢並列印結果。

1. 執行腳本：  
   ```bash
   python scenario1.py
   ```  
2. 在提示符輸入你的文件問題。

### 情境 2：學習計劃生成器（Chainlit 網頁應用）  
一個基於網頁的介面（使用 Chainlit），讓使用者為任何技術主題生成個人化的逐週學習計劃。

1. 啟動 Chainlit 應用：  
   ```bash
   chainlit run scenario2.py
   ```  
2. 在瀏覽器打開終端機中提供的本地 URL（例如 http://localhost:8000）。  
3. 在聊天視窗輸入你的學習主題及學習週數（例如「AI-900 認證，8 週」）。  
4. 應用會回應逐週的學習計劃，並附上相關 Microsoft Learn 文件的連結。

**所需環境變數：**

使用情境 2（帶 Azure OpenAI 的 Chainlit 網頁應用）時，必須在 `.env` file in the `python` 目錄中設定以下環境變數：

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

請在執行應用前填入你的 Azure OpenAI 資源詳情。

> **提示：** 你可以輕鬆地使用 [Azure AI Foundry](https://ai.azure.com/) 部署自己的模型。

### 情境 3：在 VS Code 編輯器內使用 MCP 伺服器的文件

不用切換瀏覽器分頁搜尋文件，你可以直接在 VS Code 中使用 MCP 伺服器帶來的 Microsoft Learn Docs。這能讓你：  
- 在 VS Code 內搜尋及閱讀文件，不用離開編碼環境。  
- 參考文件並直接插入連結到 README 或課程檔案。  
- 同時使用 GitHub Copilot 與 MCP，打造無縫的 AI 驅動文件工作流程。

**範例使用情境：**  
- 在撰寫課程或專案文件時，快速新增參考連結到 README。  
- 使用 Copilot 生成程式碼，並用 MCP 即時找到及引用相關文件。  
- 保持專注在編輯器內，提高工作效率。

> [!IMPORTANT]  
> 確保你有有效的 [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

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
- `Cloud architecture, 9 weeks`

這些範例展示了此應用在不同學習目標和時間安排上的彈性。

## 參考資料

- [Chainlit Documentation](https://docs.chainlit.io/)  
- [MCP Documentation](https://github.com/MicrosoftDocs/mcp)

**免責聲明**：  
本文件由 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻譯而成。雖然我們致力於確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議使用專業人工翻譯。對於因使用本翻譯而引起的任何誤解或誤譯，我們概不負責。