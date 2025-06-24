<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5384bbb2a92d00d5d7e66274dbe0331d",
  "translation_date": "2025-06-20T18:22:19+00:00",
  "source_file": "04-PracticalImplementation/README.md",
  "language_code": "zh"
}
-->
# 实践应用

实践应用是 Model Context Protocol (MCP) 威力真正体现的地方。虽然理解 MCP 的理论和架构很重要，但真正的价值在于将这些概念应用到构建、测试和部署解决方案中，以解决现实世界的问题。本章弥合了概念知识与实际开发之间的差距，指导你完成基于 MCP 的应用从无到有的过程。

无论你是在开发智能助手、将 AI 集成到业务流程中，还是构建用于数据处理的定制工具，MCP 都提供了灵活的基础。它的语言无关设计和针对主流编程语言的官方 SDK，使其对广泛的开发者都很友好。通过利用这些 SDK，你可以快速进行原型设计、迭代开发，并在不同平台和环境中扩展你的解决方案。

在接下来的章节中，你将看到实用示例、示范代码以及部署策略，展示如何在 C#、Java、TypeScript、JavaScript 和 Python 中实现 MCP。你还将学习如何调试和测试 MCP 服务器、管理 API，并使用 Azure 将解决方案部署到云端。这些动手资源旨在加速你的学习，帮助你自信地构建健壮且适合生产环境的 MCP 应用。

## 概述

本课聚焦于 MCP 在多种编程语言中的实际应用。我们将探讨如何使用 C#、Java、TypeScript、JavaScript 和 Python 的 MCP SDK 构建稳健的应用，调试和测试 MCP 服务器，以及创建可复用的资源、提示和工具。

## 学习目标

完成本课后，你将能够：
- 使用官方 SDK 在多种编程语言中实现 MCP 解决方案
- 系统地调试和测试 MCP 服务器
- 创建并使用服务器功能（资源、提示和工具）
- 设计有效的 MCP 工作流以处理复杂任务
- 优化 MCP 实现以提升性能和可靠性

## 官方 SDK 资源

Model Context Protocol 提供了多种语言的官方 SDK：

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

## 使用 MCP SDK

本节提供了多种编程语言中实现 MCP 的实用示例。你可以在 `samples` 目录中按语言查找示范代码。

### 可用示例

仓库包含以下语言的[示例实现](../../../04-PracticalImplementation/samples)：

- [C#](./samples/csharp/README.md)
- [Java](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

每个示例展示了该语言及生态系统中 MCP 的关键概念和实现模式。

## 核心服务器功能

MCP 服务器可以实现以下任意组合的功能：

### 资源
资源为用户或 AI 模型提供上下文和数据：
- 文档库
- 知识库
- 结构化数据源
- 文件系统

### 提示
提示是为用户准备的模板化消息和工作流：
- 预定义的对话模板
- 引导式交互模式
- 专门设计的对话结构

### 工具
工具是 AI 模型可执行的函数：
- 数据处理工具
- 外部 API 集成
- 计算能力
- 搜索功能

## 示例实现：C#

官方 C# SDK 仓库包含多个示例，展示 MCP 的不同方面：

- **基础 MCP 客户端**：简单示例，展示如何创建 MCP 客户端并调用工具
- **基础 MCP 服务器**：最小化服务器实现，包含基础工具注册
- **高级 MCP 服务器**：功能齐全的服务器，支持工具注册、身份验证和错误处理
- **ASP.NET 集成**：展示与 ASP.NET Core 集成的示例
- **工具实现模式**：展示不同复杂度工具实现的多种模式

MCP C# SDK 处于预览阶段，API 可能会变动。我们将持续更新博客以跟进 SDK 的演进。

### 主要特性
- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)

- 构建你的[第一个 MCP 服务器](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/)。

完整的 C# 实现示例，请访问[官方 C# SDK 示例仓库](https://github.com/modelcontextprotocol/csharp-sdk)

## 示例实现：Java 实现

Java SDK 提供了企业级功能的稳健 MCP 实现选项。

### 主要特性

- Spring Framework 集成
- 强类型安全
- 响应式编程支持
- 全面错误处理

完整的 Java 实现示例，请参见示例目录中的 [Java 示例](samples/java/containerapp/README.md)。

## 示例实现：JavaScript 实现

JavaScript SDK 提供轻量且灵活的 MCP 实现方案。

### 主要特性

- 支持 Node.js 和浏览器环境
- 基于 Promise 的 API
- 易于与 Express 及其他框架集成
- 支持 WebSocket 流式传输

完整的 JavaScript 实现示例，请参见示例目录中的 [JavaScript 示例](samples/javascript/README.md)。

## 示例实现：Python 实现

Python SDK 采用 Python 风格实现 MCP，且与主流机器学习框架集成良好。

### 主要特性

- 支持 asyncio 的 async/await
- 集成 Flask 和 FastAPI
- 简单的工具注册
- 与流行机器学习库的原生集成

完整的 Python 实现示例，请参见示例目录中的 [Python 示例](samples/python/README.md)。

## API 管理

Azure API Management 是保护 MCP 服务器的有效方案。思路是在 MCP 服务器前端放置一个 Azure API Management 实例，让它处理你可能需要的功能，如：

- 限流
- 令牌管理
- 监控
- 负载均衡
- 安全性

### Azure 示例

这里有一个 Azure 示例，正是实现了上述功能，即[创建 MCP 服务器并用 Azure API Management 保护它](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)。

下面的图片展示了授权流程：

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

图中发生了以下流程：

- 使用 Microsoft Entra 进行身份验证/授权。
- Azure API Management 作为网关，使用策略来引导和管理流量。
- Azure Monitor 记录所有请求以供进一步分析。

#### 授权流程

我们来详细看看授权流程：

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP 授权规范

了解更多关于[MCP 授权规范](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization#2-10-third-party-authorization-flow)

## 将远程 MCP 服务器部署到 Azure

让我们尝试部署之前提到的示例：

1. 克隆仓库

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

2. 注册 `Microsoft.App` resource provider.
    * If you are using Azure CLI, run `az provider register --namespace Microsoft.App --wait`.
    * If you are using Azure PowerShell, run `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Then run `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState`，稍等片刻后检查注册是否完成。

3. 运行此 [azd](https://aka.ms/azd) 命令，预配 API 管理服务、函数应用（含代码）以及其他所需的 Azure 资源

    ```shell
    azd up
    ```

    此命令将部署所有 Azure 云资源

### 使用 MCP Inspector 测试你的服务器

1. 在**新终端窗口**中，安装并运行 MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    你应该会看到类似的界面：

    ![Connect to Node inspector](../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.zh.png)

2. 按住 CTRL 点击，使用应用显示的 URL（例如 http://127.0.0.1:6274/#resources）加载 MCP Inspector Web 应用
3. 将传输类型设置为 `SSE`
1. Set the URL to your running API Management SSE endpoint displayed after `azd up`，然后**连接**：

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

5. **列出工具**。点击某个工具并**运行工具**。

如果所有步骤顺利完成，你现在应该已连接到 MCP 服务器，并成功调用了一个工具。

## Azure 上的 MCP 服务器

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)：这一系列仓库是使用 Azure Functions 结合 Python、C# .NET 或 Node/TypeScript 快速构建和部署自定义远程 MCP（Model Context Protocol）服务器的模板。

这些示例提供了完整解决方案，允许开发者：

- 本地构建和运行：在本地机器上开发和调试 MCP 服务器
- 部署到 Azure：通过简单的 azd up 命令轻松部署到云端
- 从客户端连接：支持包括 VS Code 的 Copilot 代理模式和 MCP Inspector 工具在内的多种客户端连接 MCP 服务器

### 主要特性：

- 安全设计：MCP 服务器通过密钥和 HTTPS 保障安全
- 身份验证选项：支持内置身份验证和/或 API 管理的 OAuth
- 网络隔离：支持通过 Azure 虚拟网络（VNET）实现网络隔离
- 无服务器架构：利用 Azure Functions 实现可扩展的事件驱动执行
- 本地开发：全面支持本地开发和调试
- 简单部署：简化的 Azure 部署流程

仓库包含所有必要的配置文件、源代码和基础设施定义，助你快速启动生产级 MCP 服务器实现。

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - 使用 Azure Functions 和 Python 实现的 MCP 示例

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - 使用 Azure Functions 和 C# .NET 实现的 MCP 示例

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - 使用 Azure Functions 和 Node/TypeScript 实现的 MCP 示例

## 关键要点

- MCP SDK 提供针对不同语言的工具，助力实现稳健的 MCP 解决方案
- 调试和测试过程对 MCP 应用的可靠性至关重要
- 可复用的提示模板保障 AI 交互的一致性
- 精心设计的工作流可协调多工具完成复杂任务
- 实现 MCP 解决方案需考虑安全性、性能和错误处理

## 练习

设计一个实用的 MCP 工作流，解决你所在领域的实际问题：

1. 确定 3-4 个对解决该问题有用的工具
2. 绘制工作流图，展示这些工具如何协同工作
3. 使用你偏好的语言实现其中一个工具的基础版本
4. 创建一个提示模板，帮助模型高效使用你的工具

## 额外资源


---

下一章：[高级主题](../05-AdvancedTopics/README.md)

**免责声明**：  
本文件使用 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 进行翻译。虽然我们力求准确，但请注意自动翻译可能存在错误或不准确之处。原始文件的原文应被视为权威来源。对于重要信息，建议采用专业人工翻译。因使用本翻译而产生的任何误解或误释，我们概不负责。