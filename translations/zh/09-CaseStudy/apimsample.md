<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "36de9fae488d6de554d969fe8e0801a8",
  "translation_date": "2025-06-20T19:14:48+00:00",
  "source_file": "09-CaseStudy/apimsample.md",
  "language_code": "zh"
}
-->
# 案例研究：在 API 管理中以 MCP 服务器形式暴露 REST API

Azure API Management 是一项在您的 API 端点之上提供网关服务的产品。其工作原理是充当您 API 之前的代理，能够决定如何处理传入请求。

使用它，您可以获得一系列功能，例如：

- **安全性**，支持从 API 密钥、JWT 到托管身份的多种认证方式。
- **速率限制**，可以控制在特定时间单位内允许通过的调用次数。这有助于确保所有用户获得良好体验，同时避免服务被请求淹没。
- **扩展与负载均衡**。您可以设置多个端点以分散负载，还可以自定义“负载均衡”策略。
- **AI 功能，如语义缓存、令牌限制和令牌监控等**。这些功能提升响应速度，同时帮助您掌握令牌的使用情况。[详情请见](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities)。

## 为什么选择 MCP + Azure API Management？

Model Context Protocol 正迅速成为智能代理 AI 应用暴露工具和数据的标准方式。Azure API Management 是管理 API 的自然选择。MCP 服务器通常会集成其他 API 来处理工具请求，因此将 Azure API Management 与 MCP 结合使用非常合理。

## 概述

在本案例中，我们将学习如何将 API 端点作为 MCP 服务器暴露。这样，我们可以轻松将这些端点集成到智能代理应用中，同时利用 Azure API Management 的强大功能。

## 主要功能

- 您可以选择希望作为工具暴露的端点方法。
- 您获得的额外功能取决于 API 策略部分的配置。这里我们将演示如何添加速率限制。

## 前置步骤：导入 API

如果您已经在 Azure API Management 中有 API，可以跳过此步骤。否则，请参考此链接，[导入 API 到 Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api)。

## 将 API 作为 MCP 服务器暴露

按照以下步骤暴露 API 端点：

1. 进入 Azure 门户，访问地址 <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> ，并导航到您的 API 管理实例。

2. 在左侧菜单选择 APIs > MCP Servers > + 创建新的 MCP 服务器。

3. 在 API 中选择一个 REST API 作为 MCP 服务器暴露。

4. 选择一个或多个 API 操作作为工具暴露。您可以选择全部操作或特定操作。

    ![选择要暴露的方法](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

5. 点击 **创建**。

6. 进入菜单选项 **APIs** 和 **MCP Servers**，您应该能看到如下界面：

    ![主面板中的 MCP 服务器](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP 服务器已创建，API 操作已作为工具暴露。MCP 服务器会显示在 MCP Servers 面板中。URL 列显示 MCP 服务器的端点，您可以用于测试或客户端应用调用。

## 可选：配置策略

Azure API Management 的核心概念之一是策略，您可以为端点设置不同规则，比如速率限制或语义缓存。策略以 XML 格式编写。

下面介绍如何为 MCP 服务器设置速率限制策略：

1. 在门户中，选择 APIs 下的 **MCP Servers**。

2. 选择您创建的 MCP 服务器。

3. 在左侧菜单 MCP 下选择 **Policies**。

4. 在策略编辑器中添加或编辑您想应用于 MCP 服务器工具的策略。策略以 XML 格式定义。例如，您可以添加一个策略限制 MCP 服务器工具的调用次数（本例中为每个客户端 IP 地址每 30 秒最多 5 次调用）。以下是实现速率限制的 XML：

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    策略编辑器界面示例如下：

    ![策略编辑器](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## 试用

让我们确认 MCP 服务器正常工作。

这里我们使用 Visual Studio Code 和 GitHub Copilot 的 Agent 模式。我们会将 MCP 服务器添加到 *mcp.json* 文件中。这样，Visual Studio Code 就能作为具备代理功能的客户端，终端用户可以输入提示并与服务器交互。

在 Visual Studio Code 中添加 MCP 服务器的步骤如下：

1. 在命令面板中使用 MCP: **Add Server 命令**。

2. 提示时选择服务器类型：**HTTP（HTTP 或 Server Sent Events）**。

3. 输入 Azure API Management 中 MCP 服务器的 URL。例如：**https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse**（SSE 端点）或 **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp**（MCP 端点），注意两种传输方式的区别是 `/sse` or `/mcp`。

4. 输入一个服务器 ID，您可以自定义，这有助于记忆该服务器实例。

5. 选择将配置保存到工作区设置还是用户设置。

  - **工作区设置** - 配置保存到当前工作区的 .vscode/mcp.json 文件中。

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    如果选择流式 HTTP 传输，配置稍有不同：

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **用户设置** - 配置添加到全局 *settings.json* 文件，适用于所有工作区。配置示例如下：

    ![用户设置](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

6. 您还需要添加配置头，确保正确认证 Azure API Management。使用名为 **Ocp-Apim-Subscription-Key** 的头。

    - 下面是如何添加到设置中的示例：

    ![添加认证头](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png)，这会弹出提示，要求输入您在 Azure 门户中 API 管理实例的 API 密钥。

    - 如果要添加到 *mcp.json*，可以这样写：

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

现在无论是在设置中还是 *.vscode/mcp.json* 中配置完成，我们来试用一下。

工具图标会显示如下，列出服务器暴露的工具：

![服务器工具](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. 点击工具图标，您会看到工具列表：

    ![工具列表](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

2. 在聊天中输入提示以调用工具。例如，如果您选择了一个查询订单信息的工具，可以向代理询问订单。示例提示：

    ```text
    get information from order 2
    ```

    之后您会看到工具图标，提示是否继续调用工具。选择继续，您将看到类似如下的输出：

    ![提示结果](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **以上显示内容取决于您配置的工具，但核心是您会得到类似的文本响应。**


## 参考资料

您可以通过以下资源了解更多：

- [Azure API Management 和 MCP 教程](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python 示例：使用 Azure API Management 保护远程 MCP 服务器（实验性）](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP 客户端授权实验](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [使用 Azure API Management VS Code 扩展导入和管理 API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [在 Azure API Center 注册和发现远程 MCP 服务器](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) 优秀的仓库，展示了许多 Azure API Management 的 AI 功能
- [AI Gateway 研讨会](https://azure-samples.github.io/AI-Gateway/) 包含使用 Azure 门户的研讨会，是评估 AI 功能的好方法。

**免责声明**：  
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意，自动翻译可能存在错误或不准确之处。原始语言的原文应被视为权威来源。对于重要信息，建议使用专业人工翻译。因使用本翻译内容而产生的任何误解或误释，我们概不负责。