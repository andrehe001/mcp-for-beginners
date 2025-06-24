<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "36de9fae488d6de554d969fe8e0801a8",
  "translation_date": "2025-06-20T19:15:42+00:00",
  "source_file": "09-CaseStudy/apimsample.md",
  "language_code": "tw"
}
-->
# 案例研究：在 API Management 中將 REST API 揭露為 MCP 伺服器

Azure API Management 是一項服務，可在您的 API 端點之上提供一個閘道。它的運作方式是 Azure API Management 作為您的 API 之前的代理，能夠決定如何處理進來的請求。

透過使用它，您可以獲得一系列功能，例如：

- **安全性**，您可以使用從 API 金鑰、JWT 到託管身分識別的各種機制。
- **速率限制**，一個很棒的功能是能夠決定在特定時間內允許多少呼叫通過。這有助於確保所有使用者都有良好的體驗，同時避免服務被過度請求淹沒。
- **擴展與負載平衡**。您可以設定多個端點來分散負載，也可以決定如何「負載平衡」。
- **AI 功能，如語意快取、令牌限制與令牌監控等**。這些功能能提升回應速度，同時幫助您掌控令牌使用情況。[詳細閱讀](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities)。

## 為什麼選擇 MCP + Azure API Management？

Model Context Protocol 正迅速成為智能代理 AI 應用程式的標準，以及如何以一致的方式揭露工具和資料。當您需要「管理」API 時，Azure API Management 是自然的選擇。MCP 伺服器通常會與其他 API 整合，例如將請求解析到某個工具。因此，結合 Azure API Management 與 MCP 非常合理。

## 概覽

在此特定案例中，我們將學習如何將 API 端點揭露為 MCP 伺服器。透過此方式，我們能輕鬆將這些端點整合到智能代理應用程式中，同時利用 Azure API Management 的功能。

## 主要功能

- 您可選擇想要揭露為工具的端點方法。
- 您可獲得的額外功能取決於您在 API 的策略區段中所配置的內容。在此，我們將示範如何新增速率限制。

## 前置步驟：匯入 API

如果您已在 Azure API Management 中有 API，太好了，可以跳過這一步。如果沒有，請參考此連結，[將 API 匯入 Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api)。

## 將 API 揭露為 MCP 伺服器

要揭露 API 端點，請依照以下步驟操作：

1. 前往 Azure 入口網站，並至以下網址 <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
進入您的 API Management 實例。

2. 在左側選單中，選擇 APIs > MCP Servers > + 建立新的 MCP Server。

3. 在 API 中，選擇一個 REST API 以揭露為 MCP 伺服器。

4. 選擇一個或多個 API 操作來揭露為工具。您可以選擇所有操作或僅特定操作。

    ![選擇要揭露的方法](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

5. 選擇 **建立**。

6. 前往選單中的 **APIs** 與 **MCP Servers**，您應該會看到如下畫面：

    ![在主視窗中看到 MCP 伺服器](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP 伺服器已建立，且 API 操作已揭露為工具。該 MCP 伺服器會列在 MCP Servers 面板中。URL 欄位顯示 MCP 伺服器的端點，您可以用來測試或在用戶端應用程式中呼叫。

## 選擇性：配置策略

Azure API Management 的核心概念之一是策略，您可以為端點設定各種規則，例如速率限制或語意快取。這些策略是以 XML 撰寫。

以下示範如何為 MCP 伺服器設定速率限制策略：

1. 在入口網站中，於 APIs 下選擇 **MCP Servers**。

2. 選擇您建立的 MCP 伺服器。

3. 在左側選單中，MCP 區段下選擇 **Policies**。

4. 在策略編輯器中，新增或編輯您想套用於 MCP 伺服器工具的策略。策略以 XML 格式定義。例如，您可以新增一個策略，限制對 MCP 伺服器工具的呼叫次數（此範例為每個客戶端 IP 地址每 30 秒限制 5 次呼叫）。以下是會啟用速率限制的 XML：

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    以下為策略編輯器畫面：

    ![策略編輯器](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## 試用看看

讓我們確認 MCP 伺服器運作正常。

這裡我們將使用 Visual Studio Code 與 GitHub Copilot 的 Agent 模式。我們會將 MCP 伺服器新增到 *mcp.json* 中。如此一來，Visual Studio Code 將作為具備代理能力的用戶端，最終使用者即可輸入提示並與該伺服器互動。

以下示範如何在 Visual Studio Code 中新增 MCP 伺服器：

1. 使用指令面板的 MCP: **Add Server** 指令。

2. 當系統提示時，選擇伺服器類型：**HTTP (HTTP 或 Server Sent Events)**。

3. 輸入 Azure API Management 中 MCP 伺服器的 URL。範例：**https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse**（SSE 端點）或 **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp**（MCP 端點），注意兩者傳輸方式的差異是 `/sse` or `/mcp`。

4. 輸入您選擇的伺服器 ID。這不是重要的值，但有助於您記住該伺服器實例。

5. 選擇將設定儲存到工作區設定或使用者設定。

  - **工作區設定** - 伺服器設定會儲存至當前工作區的 .vscode/mcp.json 檔案中。

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    若您選擇使用串流 HTTP 作為傳輸方式，設定會稍有不同：

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **使用者設定** - 伺服器設定會加入到您的全域 *settings.json* 檔案中，並在所有工作區可用。設定格式如下：

    ![使用者設定](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

6. 您還需要新增一個標頭以確保能正確驗證 Azure API Management，使用的標頭名稱為 **Ocp-Apim-Subscription-Key**。

    - 以下示範如何將它加入設定：

    ![新增驗證標頭](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png)，系統會提示您輸入 API 金鑰，您可以在 Azure 入口網站的 Azure API Management 實例中找到該金鑰。

   - 若要改為加入 *mcp.json*，可如下新增：

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

### 使用 Agent 模式

現在我們已在設定檔或 *.vscode/mcp.json* 中完成設定。讓我們試試看。

應該會有一個工具圖示，列出您伺服器揭露的工具：

![伺服器工具](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. 點選工具圖示，您會看到工具清單如下：

    ![工具清單](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

2. 在聊天視窗輸入提示以呼叫工具。例如，若您選擇了一個用來取得訂單資訊的工具，您可以向代理詢問訂單狀況。以下為示範提示：

    ```text
    get information from order 2
    ```

    接著會顯示工具圖示，詢問您是否要繼續呼叫該工具。選擇繼續執行後，您應該會看到如下輸出結果：

    ![提示結果](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **上述畫面會依您設定的工具而異，但概念是您會得到如上所示的文字回應。**

## 參考資料

您可以透過以下資源進一步了解：

- [Azure API Management 與 MCP 教學](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python 範例：使用 Azure API Management 保護遠端 MCP 伺服器（實驗性）](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP 用戶端授權實驗室](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [使用 Azure API Management 擴充功能於 VS Code 匯入與管理 API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [在 Azure API Center 註冊與發現遠端 MCP 伺服器](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) 優秀的資源庫，展示 Azure API Management 的多種 AI 能力
- [AI Gateway 工作坊](https://azure-samples.github.io/AI-Gateway/) 包含使用 Azure 入口網站的工作坊，是評估 AI 功能的絕佳起點

**免責聲明**：  
本文件係使用 AI 翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 所翻譯。雖然我們致力於翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用本翻譯所產生的任何誤解或誤譯負責。