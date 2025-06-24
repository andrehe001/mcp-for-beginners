<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6940b1e931e51821b219aa9dcfe8c4ee",
  "translation_date": "2025-06-23T11:00:46+00:00",
  "source_file": "09-CaseStudy/README.md",
  "language_code": "mo"
}
-->
# MCP 實戰：真實案例研究

Model Context Protocol (MCP) 正在改變 AI 應用程式與資料、工具及服務互動的方式。本節介紹多個真實案例，展示 MCP 在各種企業場景中的實際應用。

## 概述

本節展示 MCP 實作的具體範例，突顯組織如何利用此協議解決複雜的商業挑戰。透過這些案例，您將了解 MCP 在真實場景中的多樣性、可擴展性及實用效益。

## 主要學習目標

透過探索這些案例，您將能：

- 了解 MCP 如何應用於解決特定商業問題
- 學習不同的整合模式與架構方法
- 掌握企業環境中實施 MCP 的最佳實踐
- 獲得真實案例中遇到的挑戰與解決方案的見解
- 發掘在自身專案中應用類似模式的機會

## 精選案例研究

### 1. [Azure AI 旅遊代理 – 參考實作](./travelagentsample.md)

本案例研究探討微軟的完整參考解決方案，展示如何利用 MCP、Azure OpenAI 與 Azure AI Search 建構多代理、AI 驅動的旅遊規劃應用。專案重點包括：

- 透過 MCP 實現多代理協調
- 與 Azure AI Search 整合企業資料
- 使用 Azure 服務打造安全且可擴展的架構
- 利用可重複使用的 MCP 元件擴充工具
- 由 Azure OpenAI 支援的對話式使用者體驗

架構與實作細節提供了寶貴見解，有助於建置以 MCP 作為協調層的複雜多代理系統。

### 2. [從 YouTube 資料更新 Azure DevOps 項目](./UpdateADOItemsFromYT.md)

此案例展示 MCP 在自動化工作流程中的實際應用，說明如何利用 MCP 工具：

- 從線上平台（YouTube）擷取資料
- 更新 Azure DevOps 系統中的工作項目
- 建立可重複執行的自動化流程
- 跨異質系統整合資料

此範例說明即使是相對簡單的 MCP 實作，也能透過自動化例行任務與提升資料一致性，帶來顯著效率提升。

### 3. [使用 MCP 即時取得文件](./docs-mcp/README.md)

本案例引導您如何使用 Python 控制台客戶端連接 Model Context Protocol (MCP) 伺服器，檢索並記錄即時且具上下文感知的 Microsoft 文件。您將學到：

- 使用 Python 客戶端與官方 MCP SDK 連接 MCP 伺服器
- 使用串流 HTTP 客戶端高效即時取得資料
- 呼叫伺服器上的文件工具，並將回應直接記錄到控制台
- 在終端機內整合最新 Microsoft 文件，無需離開工作環境

本章包含實作練習、最小可行程式碼範例及進階資源連結。請參閱連結章節的完整教學與程式碼，了解 MCP 如何改變基於控制台的文件存取與開發者生產力。

### 4. [使用 MCP 的互動式學習計畫產生器網頁應用](./docs-mcp/README.md)

本案例示範如何利用 Chainlit 與 Model Context Protocol (MCP) 建構互動式網頁應用，為任何主題生成個人化學習計畫。使用者可指定主題（如「AI-900 認證」）及學習週期（例如 8 週），應用會提供逐週的推薦內容。Chainlit 創造對話式聊天介面，使體驗更生動且具適應性。

- 由 Chainlit 支援的對話式網頁應用
- 使用者主導的主題與時間輸入
- 利用 MCP 提供逐週內容建議
- 聊天介面中即時且具適應性的回應

專案展示對話式 AI 與 MCP 如何結合，打造現代網頁環境中動態且以使用者為中心的教育工具。

### 5. [VS Code 中的 MCP 伺服器內嵌文件](./docs-mcp/README.md)

本案例展示如何利用 MCP 伺服器將 Microsoft Learn 文件直接帶入 VS Code 環境，無需切換瀏覽器分頁！您將看到如何：

- 使用 MCP 面板或命令面板在 VS Code 內即時搜尋與閱讀文件
- 直接在 README 或課程 Markdown 檔案中引用文件並插入連結
- 結合 GitHub Copilot 與 MCP，實現無縫 AI 支援的文件與程式碼工作流程
- 透過即時回饋與微軟官方準確度驗證並強化文件
- 將 MCP 整合至 GitHub 工作流程，持續驗證文件品質

實作包含：
- 簡易設定的 `.vscode/mcp.json` 範例配置
- 以截圖呈現的編輯器內體驗導覽
- 結合 Copilot 與 MCP 的效率提升秘訣

此情境非常適合課程作者、文件撰寫者及開發者，讓他們在編輯器內專注工作，同時使用文件、Copilot 與驗證工具，全由 MCP 驅動。

### 6. [APIM MCP 伺服器建立](./apimsample.md)

本案例提供如何使用 Azure API Management (APIM) 建立 MCP 伺服器的逐步指南，涵蓋：

- 在 Azure API Management 中設置 MCP 伺服器
- 將 API 操作暴露為 MCP 工具
- 配置限流與安全性政策
- 使用 Visual Studio Code 與 GitHub Copilot 測試 MCP 伺服器

此範例展示如何利用 Azure 的能力打造穩健的 MCP 伺服器，強化 AI 系統與企業 API 的整合。

## 結論

這些案例突顯 Model Context Protocol 在真實場景中的多樣性與實際應用價值。從複雜的多代理系統到針對性的自動化工作流程，MCP 提供標準化的方式，連結 AI 系統與所需工具及資料，實現價值交付。

透過研究這些實作，您可以獲得架構模式、實施策略與最佳實踐的洞見，應用於自身 MCP 專案。這些範例證明 MCP 不僅是理論框架，更是解決實際商業挑戰的實用方案。

## 其他資源

- [Azure AI Travel Agents GitHub Repository](https://github.com/Azure-Samples/azure-ai-travel-agents)
- [Azure DevOps MCP Tool](https://github.com/microsoft/azure-devops-mcp)
- [Playwright MCP Tool](https://github.com/microsoft/playwright-mcp)
- [Microsoft Docs MCP Server](https://github.com/MicrosoftDocs/mcp)
- [MCP Community Examples](https://github.com/microsoft/mcp)

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件之母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。因使用本翻譯所引起之任何誤解或誤譯，我們概不負責。