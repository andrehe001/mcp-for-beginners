<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6940b1e931e51821b219aa9dcfe8c4ee",
  "translation_date": "2025-06-23T11:01:19+00:00",
  "source_file": "09-CaseStudy/README.md",
  "language_code": "hk"
}
-->
# MCP 實戰：真實案例研究

Model Context Protocol（MCP）正改變 AI 應用與數據、工具及服務的互動方式。本章節展示多個真實案例，說明 MCP 在不同企業場景中的實際應用。

## 概覽

本章節呈現 MCP 實作的具體範例，突顯組織如何運用此協議解決複雜的商業問題。透過這些案例，你將了解 MCP 在真實場景中的多樣性、可擴展性及實際效益。

## 主要學習目標

透過探索這些案例，你將能：

- 理解 MCP 如何應用於解決特定商業問題
- 學習不同的整合模式及架構方法
- 掌握企業環境中實施 MCP 的最佳實踐
- 獲得真實實作中遇到的挑戰及解決方案的見解
- 辨識在自身專案中應用類似模式的機會

## 精選案例研究

### 1. [Azure AI 旅遊代理 – 參考實作](./travelagentsample.md)

本案例研究探討微軟的完整參考解決方案，展示如何利用 MCP、Azure OpenAI 與 Azure AI Search 建立多代理的 AI 驅動旅遊規劃應用。專案重點包括：

- 透過 MCP 進行多代理協調
- 利用 Azure AI Search 整合企業數據
- 使用 Azure 服務打造安全且具可擴展性的架構
- 可擴充且可重複使用的 MCP 元件工具
- 由 Azure OpenAI 支援的對話式使用者體驗

架構與實作細節提供了寶貴的洞見，助你理解如何以 MCP 作為協調層建構複雜的多代理系統。

### 2. [從 YouTube 數據更新 Azure DevOps 項目](./UpdateADOItemsFromYT.md)

本案例展示 MCP 在自動化工作流程中的實際應用，說明如何利用 MCP 工具：

- 從線上平台（YouTube）擷取資料
- 更新 Azure DevOps 系統中的工作項目
- 建立可重複使用的自動化流程
- 跨不同系統整合資料

此範例說明即使是相對簡單的 MCP 實作，也能透過自動化例行任務及提升系統間資料一致性，帶來顯著效率提升。

### 3. [使用 MCP 實現即時文件檢索](./docs-mcp/README.md)

本案例引導你如何將 Python 控制台客戶端連接到 Model Context Protocol（MCP）伺服器，取得並記錄即時且具上下文感知的 Microsoft 文件。你將學會：

- 使用 Python 客戶端及官方 MCP SDK 連接 MCP 伺服器
- 利用串流 HTTP 客戶端進行高效即時資料擷取
- 呼叫伺服器上的文件工具，並直接在控制台記錄回應
- 將最新 Microsoft 文件整合到工作流程中，無需離開終端機

本章包含實作練習、最小可行程式碼範例及更多資源連結。詳見連結章節的完整教學與程式碼，了解 MCP 如何在終端機環境中革新文件存取及提升開發者生產力。

### 4. [使用 MCP 的互動式學習計劃生成器網頁應用](./docs-mcp/README.md)

本案例展示如何利用 Chainlit 與 Model Context Protocol（MCP）打造互動式網頁應用，為任意主題生成個人化學習計劃。使用者可指定主題（例如「AI-900 證照」）及學習週期（例如 8 週），應用將提供逐週推薦內容。Chainlit 提供對話式聊天介面，讓體驗更具互動性與彈性。

- 由 Chainlit 驅動的對話式網頁應用
- 使用者主導的主題與時長輸入
- 利用 MCP 提供逐週內容建議
- 聊天介面中即時且彈性的回應

此專案示範對話式 AI 與 MCP 如何結合，打造現代網頁環境下動態且使用者驅動的教育工具。

### 5. [在 VS Code 中使用 MCP 伺服器實現內嵌文件](./docs-mcp/README.md)

本案例展示如何利用 MCP 伺服器將 Microsoft Learn 文件直接帶入 VS Code，無需切換瀏覽器分頁！你將看到如何：

- 在 VS Code 中透過 MCP 面板或命令面板即時搜尋與閱讀文件
- 直接在 README 或課程 Markdown 文件中引用文件並插入連結
- 結合 GitHub Copilot 與 MCP，實現無縫的 AI 文件與程式碼工作流程
- 利用即時反饋與微軟來源的準確性驗證並強化文件內容
- 將 MCP 與 GitHub 工作流程整合，持續驗證文件品質

實作內容包括：
- `.vscode/mcp.json` 範例配置，簡化設定流程
- 內嵌體驗的截圖導覽
- 結合 Copilot 與 MCP 提升生產力的技巧

此情境非常適合課程作者、文件撰寫者及開發者，在編輯器內專注工作，同時使用文件、Copilot 及驗證工具，全部由 MCP 驅動。

### 6. [APIM MCP 伺服器建立](./apimsample.md)

本案例提供如何利用 Azure API Management (APIM) 建立 MCP 伺服器的逐步指南，內容涵蓋：

- 在 Azure API Management 中設置 MCP 伺服器
- 將 API 操作公開為 MCP 工具
- 配置速率限制與安全性政策
- 使用 Visual Studio Code 與 GitHub Copilot 測試 MCP 伺服器

此範例展示如何運用 Azure 能力打造穩健的 MCP 伺服器，提升 AI 系統與企業 API 的整合。

## 結語

這些案例突顯了 Model Context Protocol 在真實世界中的多樣性與實用性。從複雜的多代理系統到針對性自動化流程，MCP 提供了一種標準化方式，連結 AI 系統與所需的工具及數據，創造價值。

透過研究這些實作，你能掌握架構模式、實施策略及最佳實踐，應用於自己的 MCP 專案。這些範例證明 MCP 不僅是理論框架，更是解決實際商業挑戰的實用方案。

## 附加資源

- [Azure AI Travel Agents GitHub Repository](https://github.com/Azure-Samples/azure-ai-travel-agents)
- [Azure DevOps MCP Tool](https://github.com/microsoft/azure-devops-mcp)
- [Playwright MCP Tool](https://github.com/microsoft/playwright-mcp)
- [Microsoft Docs MCP Server](https://github.com/MicrosoftDocs/mcp)
- [MCP Community Examples](https://github.com/microsoft/mcp)

**免責聲明**：  
本文件乃使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 所翻譯。雖然我們致力於確保準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件之母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。對於因使用本翻譯而引起的任何誤解或誤釋，本公司概不負責。