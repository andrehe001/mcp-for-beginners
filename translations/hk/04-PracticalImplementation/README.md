<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5384bbb2a92d00d5d7e66274dbe0331d",
  "translation_date": "2025-06-20T18:23:04+00:00",
  "source_file": "04-PracticalImplementation/README.md",
  "language_code": "hk"
}
-->
# 實務應用

實務應用是讓 Model Context Protocol (MCP) 的威力具體展現的階段。雖然理解 MCP 的理論與架構很重要，但真正的價值在於你如何運用這些概念來建構、測試並部署解決現實問題的方案。本章將彌補概念知識與實作開發之間的鴻溝，帶領你完成基於 MCP 的應用程式實際落地的過程。

無論你是在開發智慧助理、將 AI 整合進商業流程，還是打造自訂的資料處理工具，MCP 都提供了彈性的基礎。它的語言無關設計以及針對熱門程式語言的官方 SDK，使各種開發者都能輕鬆上手。透過這些 SDK，你可以快速進行原型設計、迭代改進，並將方案擴展到不同平台與環境。

接下來的章節中，你會看到實務範例、示範程式碼以及部署策略，展示如何在 C#、Java、TypeScript、JavaScript 和 Python 中實作 MCP。你也會學到如何除錯與測試 MCP 伺服器、管理 API，以及使用 Azure 部署解決方案。這些實作資源旨在加速你的學習，讓你能自信地建構穩健且可投入生產的 MCP 應用。

## 概覽

本課程聚焦於多種程式語言中 MCP 的實務實作。我們將探討如何使用 C#、Java、TypeScript、JavaScript 及 Python 的 MCP SDK 來建構穩健的應用程式，除錯與測試 MCP 伺服器，以及建立可重複使用的資源、提示與工具。

## 學習目標

完成本課程後，你將能夠：
- 使用官方 SDK 於多種程式語言中實作 MCP 解決方案
- 系統性地除錯與測試 MCP 伺服器
- 建立並使用伺服器功能（資源、提示與工具）
- 設計有效的 MCP 工作流程以處理複雜任務
- 優化 MCP 實作的效能與可靠性

## 官方 SDK 資源

Model Context Protocol 提供多種語言的官方 SDK：

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) 
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

## 使用 MCP SDK

本節提供多種程式語言中實作 MCP 的實務範例。你可以在 `samples` 目錄中依語言分類找到示範程式碼。

### 可用範例

此倉庫包含以下語言的[範例實作](../../../04-PracticalImplementation/samples)：

- [C#](./samples/csharp/README.md)
- [Java](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

每個範例都展示了該語言及生態系統中 MCP 的核心概念與實作模式。

## 核心伺服器功能

MCP 伺服器可以實作以下任意組合的功能：

### 資源
資源提供使用者或 AI 模型可用的上下文與資料：
- 文件庫
- 知識庫
- 結構化資料來源
- 檔案系統

### 提示
提示是為使用者設計的模板訊息與工作流程：
- 預設對話模板
- 引導式互動模式
- 專門設計的對話結構

### 工具
工具是 AI 模型可執行的功能：
- 資料處理工具
- 外部 API 整合
- 計算能力
- 搜尋功能

## 範例實作：C#

官方 C# SDK 倉庫包含多個示範不同 MCP 面向的範例：

- **基礎 MCP 用戶端**：簡單示範如何建立 MCP 用戶端並呼叫工具
- **基礎 MCP 伺服器**：基本工具註冊的最小伺服器實作
- **進階 MCP 伺服器**：具備工具註冊、認證與錯誤處理的完整伺服器
- **ASP.NET 整合**：示範與 ASP.NET Core 整合的範例
- **工具實作模式**：不同複雜度的工具實作模式範例

MCP C# SDK 目前處於預覽階段，API 可能會變動。我們會持續更新本部落格以反映 SDK 的最新進展。

### 主要功能
- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)

- 建立你的[第一個 MCP 伺服器](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/)。

完整的 C# 實作範例，請參考[官方 C# SDK 範例倉庫](https://github.com/modelcontextprotocol/csharp-sdk)

## 範例實作：Java 實作

Java SDK 提供企業級的強大 MCP 實作選項。

### 主要功能

- Spring Framework 整合
- 強型別安全
- 支援反應式編程
- 完善的錯誤處理

完整的 Java 實作範例請參考 samples 目錄中的 [Java 範例](samples/java/containerapp/README.md)。

## 範例實作：JavaScript 實作

JavaScript SDK 提供輕量且靈活的 MCP 實作方式。

### 主要功能

- 支援 Node.js 與瀏覽器環境
- 基於 Promise 的 API
- 容易與 Express 及其他框架整合
- 支援 WebSocket 串流

完整的 JavaScript 實作範例請參考 samples 目錄中的 [JavaScript 範例](samples/javascript/README.md)。

## 範例實作：Python 實作

Python SDK 提供 Python 風格的 MCP 實作，並與主流機器學習框架有良好整合。

### 主要功能

- 支援 asyncio 的 async/await
- 整合 Flask 與 FastAPI
- 簡單的工具註冊機制
- 原生整合流行的機器學習函式庫

完整的 Python 實作範例請參考 samples 目錄中的 [Python 範例](samples/python/README.md)。

## API 管理

Azure API Management 是保障 MCP 伺服器安全的絕佳解決方案。其概念是將 Azure API Management 實例放在 MCP 伺服器前端，負責處理你可能需要的功能，例如：

- 流量限制
- 令牌管理
- 監控
- 負載平衡
- 安全性

### Azure 範例

這裡有一個 Azure 範例，正是實現上述功能，即[建立 MCP 伺服器並用 Azure API Management 保障安全](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)。

以下圖片展示了授權流程：

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true) 

圖片中發生的流程包括：

- 使用 Microsoft Entra 進行身份驗證與授權。
- Azure API Management 作為閘道，並利用策略導向與管理流量。
- Azure Monitor 記錄所有請求以供後續分析。

#### 授權流程

讓我們更詳細地看看授權流程：

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP 授權規範

了解更多關於[MCP 授權規範](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization#2-10-third-party-authorization-flow)

## 部署遠端 MCP 伺服器到 Azure

讓我們嘗試部署前面提到的範例：

1. 複製倉庫

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. 註冊 `Microsoft.App` 提供者

    ` resource provider.
    * If you are using Azure CLI, run `az provider register --namespace Microsoft.App --wait`.
    * If you are using Azure PowerShell, run `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Then run `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState

    等待一段時間後確認註冊是否完成。

2. 執行此 [azd](https://aka.ms/azd) 指令來佈署 API 管理服務、含程式碼的 Function App 以及其他所需 Azure 資源

    ```shell
    azd up
    ```

    此指令會在 Azure 上部署所有雲端資源。

### 使用 MCP Inspector 測試你的伺服器

1. 在**新終端機視窗**中安裝並執行 MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    你應該會看到類似以下介面：

    ![Connect to Node inspector](../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.hk.png) 

1. 按住 CTRL 點擊以從應用程式顯示的 URL (例如 http://127.0.0.1:6274/#resources) 開啟 MCP Inspector 網頁應用
1. 將傳輸類型設定為 `SSE`
1. Set the URL to your running API Management SSE endpoint displayed after `azd up`，並**連線**：

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

5. **列出工具**。點選一個工具並**執行工具**。

如果所有步驟順利完成，現在你應該已成功連接 MCP 伺服器，並能呼叫工具。

## Azure 專用 MCP 伺服器

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)：這組倉庫是使用 Azure Functions 搭配 Python、C# .NET 或 Node/TypeScript 快速啟動並部署自訂遠端 MCP (Model Context Protocol) 伺服器的範本。

這些範例提供完整解決方案，讓開發者能：

- 本地建置與執行：在本機開發與除錯 MCP 伺服器
- 部署到 Azure：使用簡單的 azd up 指令輕鬆部署至雲端
- 從用戶端連接：可從多種用戶端連接 MCP 伺服器，包括 VS Code 的 Copilot 代理模式與 MCP Inspector 工具

### 主要特色：

- 安全設計：MCP 伺服器採用金鑰與 HTTPS 保護
- 認證選項：支援內建 OAuth 認證及/或 API Management
- 網路隔離：支援使用 Azure 虛擬網路 (VNET) 進行網路隔離
- 無伺服器架構：利用 Azure Functions 實現可擴展、事件驅動的執行
- 本地開發：完善的本地開發與除錯支援
- 簡易部署：簡化的 Azure 部署流程

倉庫包含所有必要的設定檔、原始碼與基礎架構定義，讓你快速啟動生產級 MCP 伺服器實作。

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - 使用 Azure Functions 與 Python 實作的 MCP 範例
- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - 使用 Azure Functions 與 C# .NET 實作的 MCP 範例
- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - 使用 Azure Functions 與 Node/TypeScript 實作的 MCP 範例

## 主要重點整理

- MCP SDK 提供針對各語言的工具，方便實作穩健的 MCP 解決方案
- 除錯與測試流程對於可靠的 MCP 應用至關重要
- 可重複使用的提示模板能確保 AI 互動的一致性
- 良好設計的工作流程可協調多個工具完成複雜任務
- 實作 MCP 解決方案時需考量安全性、效能與錯誤處理

## 練習

設計一個實務 MCP 工作流程，解決你所在領域的真實問題：

1. 確認 3-4 個對解決此問題有幫助的工具
2. 繪製一張工作流程圖，展示這些工具如何互動
3. 使用你偏好的程式語言實作其中一個工具的基礎版本
4. 建立一個提示模板，幫助模型有效利用你的工具

## 其他資源


---

下一章：[進階主題](../05-AdvancedTopics/README.md)

**免責聲明**：  
本文件乃使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 進行翻譯。雖然我們致力於準確性，但請注意自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應視為權威來源。對於重要資訊，建議採用專業人工翻譯。因使用本翻譯而引起的任何誤解或誤釋，我們概不負責。