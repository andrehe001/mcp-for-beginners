<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "36de9fae488d6de554d969fe8e0801a8",
  "translation_date": "2025-06-20T19:15:22+00:00",
  "source_file": "09-CaseStudy/apimsample.md",
  "language_code": "hk"
}
-->
# 案例研究：在 API Management 中將 REST API 作為 MCP 伺服器公開

Azure API Management 是一項服務，提供您 API 端點之上的閘道功能。它的運作方式是作為您的 API 前端代理，並能決定如何處理進來的請求。

透過使用它，您可以獲得一系列功能，例如：

- **安全性**，您可以使用從 API 金鑰、JWT 到受管理身分識別的各種方式。
- **速率限制**，這個功能可以讓您決定在特定時間內允許多少呼叫通過。這有助於確保所有使用者都有良好的體驗，同時避免您的服務被大量請求淹沒。
- **擴展與負載平衡**。您可以設定多個端點來分攤負載，也可以決定如何進行「負載平衡」。
- **AI 功能，如語意快取、令牌限制與令牌監控等**。這些功能能提升回應速度，同時幫助您掌握令牌的使用狀況。[詳情請見這裡](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities)。

## 為什麼選擇 MCP + Azure API Management？

Model Context Protocol 正快速成為代理式 AI 應用的標準，並提供一種一致的方式來公開工具和資料。當您需要「管理」API 時，Azure API Management 是自然的選擇。MCP 伺服器通常會整合其他 API，以便解析對工具的請求。因此，結合 Azure API Management 與 MCP 是非常合理的做法。

## 概覽

在這個特定的使用案例中，我們將學習如何將 API 端點公開為 MCP 伺服器。透過這樣做，我們可以輕鬆地將這些端點納入代理式應用，同時利用 Azure API Management 的各種功能。

## 主要功能

- 您可以選擇想要公開為工具的端點方法。
- 額外功能取決於您在 API 的政策區段中所設定的內容。但這裡我們會示範如何新增速率限制。

## 預備步驟：匯入 API

如果您已經在 Azure API Management 中有 API，可以跳過這一步。若沒有，請參考這個連結，[匯入 API 至 Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api)。

## 將 API 公開為 MCP 伺服器

要公開 API 端點，請依照以下步驟：

1. 前往 Azure 入口網站，地址為 <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>，並導航至您的 API Management 實例。

2. 在左側選單中，選擇 APIs > MCP Servers > + 建立新的 MCP 伺服器。

3. 在 API 中，選擇要公開為 MCP 伺服器的 REST API。

4. 選擇一個或多個 API 操作作為工具公開。您可以選擇全部操作或特定操作。

    ![Select methods to expose](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

5. 選擇 **建立**。

6. 前往選單中的 **APIs** 與 **MCP Servers**，您應該會看到以下畫面：

    ![See the MCP Server in the main pane](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP 伺服器已建立，且 API 操作已作為工具公開。MCP 伺服器會列在 MCP Servers 面板中。URL 欄位顯示 MCP 伺服器的端點，您可以用來進行測試或在用戶端應用程式中呼叫。

## 選用：設定政策

Azure API Management 的核心概念是政策，您可以針對端點設定不同規則，例如速率限制或語意快取。這些政策是以 XML 格式撰寫。

以下說明如何設定政策來限制 MCP 伺服器的速率：

1. 在入口網站中，於 APIs 底下選擇 **MCP Servers**。

2. 選取您建立的 MCP 伺服器。

3. 在左側選單中，於 MCP 下選擇 **Policies**。

4. 在政策編輯器中，新增或編輯您想套用到 MCP 伺服器工具的政策。政策以 XML 格式定義。例如，您可以新增一個政策，限制對 MCP 伺服器工具的呼叫（此範例為每個客戶端 IP 地址每 30 秒最多 5 次呼叫）。以下是會啟動速率限制的 XML：

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    以下是政策編輯器的畫面：

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## 實際試用

讓我們確保 MCP 伺服器如預期運作。

為此，我們會使用 Visual Studio Code 以及 GitHub Copilot 的 Agent 模式。我們會將 MCP 伺服器加入 *mcp.json* 中。如此一來，Visual Studio Code 就能作為具有代理能力的客戶端，最終用戶可以輸入提示並與該伺服器互動。

以下示範如何在 Visual Studio Code 中新增 MCP 伺服器：

1. 從命令面板使用 MCP: **Add Server 指令**。

2. 提示時，選擇伺服器類型：**HTTP (HTTP 或 Server Sent Events)**。

3. 輸入 Azure API Management 中 MCP 伺服器的 URL。例如：**https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse**（SSE 端點）或 **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp**（MCP 端點），注意傳輸協定的差異為 `/sse` or `/mcp`。

4. 輸入您選擇的伺服器 ID。這不是關鍵值，但有助於您記住該伺服器實例的用途。

5. 選擇將設定儲存到工作區設定或使用者設定。

  - **工作區設定** - 伺服器設定會儲存在當前工作區專屬的 .vscode/mcp.json 檔案中。

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    若選擇使用串流 HTTP 作為傳輸，設定會略有不同：

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **使用者設定** - 伺服器設定會加入至全域 *settings.json*，並在所有工作區中可用。設定格式如下：

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

6. 您還需要新增設定標頭，以確保能正確驗證 Azure API Management。它使用名為 **Ocp-Apim-Subscription-Key** 的標頭。

    - 以下示範如何將它加入設定：

    ![Adding header for authentication](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png)，此舉會顯示提示，要求您輸入 API 金鑰值，該金鑰可在 Azure 入口網站中找到您的 Azure API Management 實例。

    - 若要直接加入 *mcp.json*，可依下方方式設定：

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

現在不論是在設定檔還是 *.vscode/mcp.json* 中，我們都已完成設定。讓我們試試看。

應該會看到一個工具圖示，列出您伺服器公開的工具：

![Tools from the server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. 點擊工具圖示，您會看到如下的工具清單：

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

2. 在聊天視窗輸入提示以呼叫工具。例如，如果您選擇了一個用來查詢訂單資訊的工具，可以向代理詢問訂單狀況。以下是一個範例提示：

    ```text
    get information from order 2
    ```

    您將會看到一個工具圖示，提示您是否要繼續呼叫該工具。選擇繼續執行工具後，您應該會看到如下輸出：

    ![Result from prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **上述結果會依您設定的工具而異，重點是您會收到類似的文字回應。**


## 參考資料

以下資源可以讓您進一步了解：

- [Azure API Management 與 MCP 教學](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python 範例：使用 Azure API Management 保護遠端 MCP 伺服器（實驗性）](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP 用戶端授權實驗室](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [使用 Azure API Management 擴充套件於 VS Code 匯入與管理 API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [在 Azure API Center 註冊並發現遠端 MCP 伺服器](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) 優秀的程式庫，展示 Azure API Management 的多項 AI 功能
- [AI Gateway 工作坊](https://azure-samples.github.io/AI-Gateway/) 包含使用 Azure 入口網站的工作坊，是開始評估 AI 功能的好方法。

**免責聲明**：  
本文件由人工智能翻譯服務 [Co-op Translator](https://github.com/Azure/co-op-translator) 所翻譯。雖然我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。原始文件的母語版本應被視為權威來源。對於重要資訊，建議採用專業人工翻譯。我們不對因使用此翻譯而引起的任何誤解或誤釋負責。