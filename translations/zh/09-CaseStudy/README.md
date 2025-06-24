<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6940b1e931e51821b219aa9dcfe8c4ee",
  "translation_date": "2025-06-23T11:00:18+00:00",
  "source_file": "09-CaseStudy/README.md",
  "language_code": "zh"
}
-->
# MCP 实战：真实案例分析

Model Context Protocol（MCP）正在改变 AI 应用与数据、工具和服务的交互方式。本节展示了多个真实案例，演示了 MCP 在各种企业场景中的实际应用。

## 概述

本节通过具体的 MCP 实现案例，展示了组织如何利用该协议解决复杂的业务难题。通过这些案例，你将深入了解 MCP 在现实环境中的多样性、可扩展性及实际优势。

## 主要学习目标

通过探索这些案例，你将能够：

- 理解 MCP 如何应用于解决具体的业务问题
- 了解不同的集成模式和架构方案
- 掌握在企业环境中实施 MCP 的最佳实践
- 了解现实应用中遇到的挑战及解决方案
- 发现将类似模式应用于自身项目的机会

## 重点案例分析

### 1. [Azure AI 旅行代理——参考实现](./travelagentsample.md)

本案例分析微软的综合参考解决方案，展示如何使用 MCP、Azure OpenAI 和 Azure AI Search 构建多代理的 AI 驱动旅行规划应用。项目亮点包括：

- 通过 MCP 实现多代理编排
- 与 Azure AI Search 的企业数据集成
- 使用 Azure 服务构建安全且可扩展的架构
- 采用可复用的 MCP 组件实现工具扩展
- 利用 Azure OpenAI 提供的对话式用户体验

架构和实现细节为构建以 MCP 作为协调层的复杂多代理系统提供了宝贵的参考。

### 2. [利用 YouTube 数据更新 Azure DevOps 事项](./UpdateADOItemsFromYT.md)

本案例展示了 MCP 在自动化工作流程中的实际应用，演示了如何：

- 从在线平台（YouTube）提取数据
- 更新 Azure DevOps 系统中的工作项
- 创建可重复的自动化流程
- 实现跨异构系统的数据整合

该示例说明了即使是相对简单的 MCP 实现，也能通过自动化日常任务和提升系统间数据一致性带来显著的效率提升。

### 3. [基于 MCP 的实时文档检索](./docs-mcp/README.md)

本案例指导你如何将 Python 控制台客户端连接到 Model Context Protocol（MCP）服务器，实现实时且上下文相关的 Microsoft 文档检索和日志记录。你将学会：

- 使用 Python 客户端和官方 MCP SDK 连接 MCP 服务器
- 利用流式 HTTP 客户端高效实时获取数据
- 调用服务器上的文档工具并将响应直接记录到控制台
- 在终端中集成最新的 Microsoft 文档，无需离开工作环境

章节中包含动手练习、最小可运行代码示例及深入学习的资源链接。请参阅完整章节和代码，了解 MCP 如何革新基于控制台的文档访问和开发者效率。

### 4. [基于 MCP 的交互式学习计划生成 Web 应用](./docs-mcp/README.md)

本案例展示如何使用 Chainlit 和 Model Context Protocol（MCP）构建一个交互式 Web 应用，为任意主题生成个性化学习计划。用户可指定主题（如“AI-900 认证”）和学习周期（如 8 周），应用将提供逐周推荐内容。Chainlit 提供对话式聊天界面，使体验更具互动性和适应性。

- 由 Chainlit 支持的对话式 Web 应用
- 用户驱动的主题和周期输入
- 通过 MCP 提供逐周内容推荐
- 聊天界面中的实时适应响应

该项目展示了如何结合对话式 AI 与 MCP，打造现代 Web 环境下动态且用户驱动的教育工具。

### 5. [VS Code 中基于 MCP 服务器的编辑器内文档](./docs-mcp/README.md)

本案例展示如何通过 MCP 服务器将 Microsoft Learn 文档直接带入 VS Code 环境，避免频繁切换浏览器标签页。你将看到如何：

- 利用 MCP 面板或命令面板在 VS Code 内即时搜索和阅读文档
- 直接引用文档并插入链接到 README 或课程 Markdown 文件中
- 结合 GitHub Copilot 与 MCP 实现无缝的 AI 驱动文档和代码工作流
- 通过实时反馈和微软权威内容验证并提升文档质量
- 将 MCP 集成到 GitHub 工作流，实现持续文档验证

实现内容包括：
- 简易配置示例 `.vscode/mcp.json`
- 基于截图的编辑器内体验演示
- 结合 Copilot 和 MCP 提升生产力的技巧

该场景非常适合课程作者、文档编写者和开发者，帮助他们专注于编辑器内的文档、Copilot 和验证工具工作，全部由 MCP 驱动。

### 6. [APIM MCP 服务器创建](./apimsample.md)

本案例提供了使用 Azure API Management (APIM) 创建 MCP 服务器的分步指南，涵盖：

- 在 Azure API Management 中设置 MCP 服务器
- 将 API 操作暴露为 MCP 工具
- 配置限流和安全策略
- 使用 Visual Studio Code 和 GitHub Copilot 测试 MCP 服务器

该示例展示了如何利用 Azure 能力构建稳健的 MCP 服务器，增强 AI 系统与企业 API 的集成。

## 结论

这些案例凸显了 Model Context Protocol 在现实场景中的多样性和实用性。从复杂的多代理系统到针对性的自动化工作流，MCP 提供了一种标准化方式，将 AI 系统与所需工具和数据连接起来，实现价值交付。

通过学习这些实现，你可以获得架构模式、实施策略和最佳实践的宝贵经验，应用于自身的 MCP 项目。这些示例表明，MCP 不仅是理论框架，更是解决实际业务难题的有效方案。

## 额外资源

- [Azure AI Travel Agents GitHub 仓库](https://github.com/Azure-Samples/azure-ai-travel-agents)
- [Azure DevOps MCP Tool](https://github.com/microsoft/azure-devops-mcp)
- [Playwright MCP Tool](https://github.com/microsoft/playwright-mcp)
- [Microsoft Docs MCP Server](https://github.com/MicrosoftDocs/mcp)
- [MCP Community Examples](https://github.com/microsoft/mcp)

**免责声明**：  
本文件由 AI 翻译服务 [Co-op Translator](https://github.com/Azure/co-op-translator) 翻译而成。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。原始语言的文档应被视为权威来源。对于重要信息，建议使用专业人工翻译。我们不对因使用本翻译而产生的任何误解或曲解承担责任。