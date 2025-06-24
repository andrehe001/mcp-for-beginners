<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6940b1e931e51821b219aa9dcfe8c4ee",
  "translation_date": "2025-06-23T11:01:44+00:00",
  "source_file": "09-CaseStudy/README.md",
  "language_code": "tw"
}
-->
# MCP 實戰：真實案例研究

Model Context Protocol (MCP) 正在改變 AI 應用程式與資料、工具及服務的互動方式。本節將介紹多個真實案例，展示 MCP 在各種企業場景中的實際應用。

## 概述

本節展示 MCP 實作的具體範例，強調組織如何運用此協議解決複雜的商業挑戰。透過這些案例研究，你將深入了解 MCP 在現實場景中的多樣性、可擴展性及實際效益。

## 主要學習目標

透過探索這些案例，你將能夠：

- 理解 MCP 如何應用於解決特定商業問題
- 學習不同的整合模式與架構方法
- 掌握在企業環境中實施 MCP 的最佳實踐
- 瞭解真實實作中遇到的挑戰與解決方案
- 發掘在自身專案中應用類似模式的機會

## 精選案例研究

### 1. [Azure AI 旅遊代理人 – 參考實作](./travelagentsample.md)

此案例探討微軟的完整參考解決方案，展示如何利用 MCP、Azure OpenAI 與 Azure AI Search 建立多代理人、AI 驅動的旅遊規劃應用程式。專案重點包括：

- 透過 MCP 進行多代理人協調
- 利用 Azure AI Search 整合企業資料
- 使用 Azure 服務打造安全且具擴展性的架構
- 以可重用的 MCP 元件擴充工具功能
- 由 Azure OpenAI 支持的對話式使用者體驗

架構與實作細節提供了建立以 MCP 作為協調層的複雜多代理人系統的寶貴見解。

### 2. [從 YouTube 資料更新 Azure DevOps 項目](./UpdateADOItemsFromYT.md)

本案例展示 MCP 在自動化工作流程上的實際應用，說明如何利用 MCP 工具：

- 從線上平台（YouTube）擷取資料
- 更新 Azure DevOps 系統中的工作項目
- 建立可重複使用的自動化流程
- 跨不同系統整合資料

此範例說明即使是相對簡單的 MCP 實作，也能透過自動化例行任務與提升系統間資料一致性，大幅提升效率。

### 3. [使用 MCP 的即時文件檢索](./docs-mcp/README.md)

本案例引導你如何連接 Python 主控台客戶端到 Model Context Protocol (MCP) 伺服器，檢索並記錄即時、具上下文感知的 Microsoft 文件。你將學會：

- 使用 Python 客戶端與官方 MCP SDK 連接 MCP 伺服器
- 利用串流 HTTP 客戶端有效率地進行即時資料檢索
- 呼叫伺服器上的文件工具並直接將回應記錄至主控台
- 在工作流程中整合最新 Microsoft 文件，無需離開終端機

本章包含實作練習、最小可用程式碼範例及深入學習資源連結。詳見相關章節的完整操作流程與程式碼，了解 MCP 如何革新基於主控台的文件存取與開發者生產力。

### 4. [使用 MCP 的互動式學習計畫生成網頁應用程式](./docs-mcp/README.md)

此案例展示如何利用 Chainlit 與 Model Context Protocol (MCP) 建立互動式網頁應用，為任何主題生成個人化學習計畫。使用者可指定主題（例如「AI-900 認證」）與學習時長（例如 8 週），應用程式將提供逐週的推薦內容。Chainlit 支援對話式聊天介面，使體驗更具互動性與適應性。

- 由 Chainlit 支持的對話式網頁應用
- 使用者主導的主題與時長輸入
- 透過 MCP 提供逐週內容推薦
- 聊天介面中的即時、動態回應

該專案展示如何結合對話式 AI 與 MCP，打造現代網頁環境中動態且以使用者為中心的教育工具。

### 5. [VS Code 中的 MCP 伺服器內建文件](./docs-mcp/README.md)

本案例示範如何利用 MCP 伺服器將 Microsoft Learn 文件直接帶入 VS Code 環境，無需切換瀏覽器分頁！你將看到如何：

- 使用 MCP 面板或命令面板在 VS Code 內即時搜尋與閱讀文件
- 直接在 README 或課程 Markdown 檔案中參考文件並插入連結
- 結合 GitHub Copilot 與 MCP，實現無縫的 AI 文件與程式碼工作流程
- 利用即時回饋與 Microsoft 原廠資料提升文件品質
- 將 MCP 與 GitHub 工作流程整合，持續驗證文件內容

實作內容包含：
- 方便設定的 `.vscode/mcp.json` 範例配置
- 以截圖說明的內建編輯體驗導覽
- 結合 Copilot 與 MCP 提升生產力的技巧

此場景非常適合課程作者、文件撰寫者及開發者，在編輯器中專注工作，同時利用 MCP 支援的文件、Copilot 與驗證工具。

### 6. [APIM MCP 伺服器建立](./apimsample.md)

本案例提供如何使用 Azure API Management (APIM) 建立 MCP 伺服器的逐步指南，涵蓋：

- 在 Azure API Management 中設定 MCP 伺服器
- 將 API 操作公開為 MCP 工具
- 配置速率限制與安全性政策
- 使用 Visual Studio Code 與 GitHub Copilot 測試 MCP 伺服器

此範例展示如何利用 Azure 能力打造強健的 MCP 伺服器，促進 AI 系統與企業 API 的整合。

## 結論

這些案例強調了 Model Context Protocol 在真實世界中的多樣應用與實用價值。從複雜的多代理人系統到針對性的自動化工作流程，MCP 提供了標準化的方式，將 AI 系統與所需工具及資料連結，創造價值。

透過學習這些實作，你可以獲得架構模式、實施策略與最佳實踐的寶貴見解，並應用於自己的 MCP 專案中。這些範例證明 MCP 不僅是理論框架，更是解決實際商業挑戰的實用方案。

## 其他資源

- [Azure AI Travel Agents GitHub Repository](https://github.com/Azure-Samples/azure-ai-travel-agents)
- [Azure DevOps MCP Tool](https://github.com/microsoft/azure-devops-mcp)
- [Playwright MCP Tool](https://github.com/microsoft/playwright-mcp)
- [Microsoft Docs MCP Server](https://github.com/MicrosoftDocs/mcp)
- [MCP Community Examples](https://github.com/microsoft/mcp)

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於確保翻譯的準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威依據。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯所產生的任何誤解或誤譯承擔責任。