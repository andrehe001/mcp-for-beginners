<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:27:08+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "zh"
}
-->
# 使用 Chainlit 和 Microsoft Learn Docs MCP 的学习计划生成器

## 前提条件

- Python 3.8 及以上版本
- pip（Python 包管理器）
- 可连接 Microsoft Learn Docs MCP 服务器的网络

## 安装

1. 克隆此仓库或下载项目文件。
2. 安装所需依赖：

   ```bash
   pip install -r requirements.txt
   ```

## 使用方法

### 场景 1：简单查询 Docs MCP  
一个命令行客户端，连接到 Docs MCP 服务器，发送查询并打印结果。

1. 运行脚本：  
   ```bash
   python scenario1.py
   ```
2. 在提示符下输入你的文档问题。

### 场景 2：学习计划生成器（Chainlit Web 应用）  
基于网页的界面（使用 Chainlit），允许用户为任何技术主题生成个性化的按周学习计划。

1. 启动 Chainlit 应用：  
   ```bash
   chainlit run scenario2.py
   ```
2. 在浏览器中打开终端提供的本地 URL（例如 http://localhost:8000）。
3. 在聊天窗口输入你的学习主题和计划学习的周数（例如，“AI-900 认证，8 周”）。
4. 应用会返回按周划分的学习计划，包括相关 Microsoft Learn 文档的链接。

**所需环境变量：**

使用场景 2（带有 Azure OpenAI 的 Chainlit Web 应用）时，必须在 `.env` file in the `python` 目录下设置以下环境变量：

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

在运行应用前，请填写你的 Azure OpenAI 资源信息。

> **提示：** 你可以通过 [Azure AI Foundry](https://ai.azure.com/) 轻松部署自己的模型。

### 场景 3：在 VS Code 编辑器内使用 MCP 服务器查看文档

无需切换浏览器标签页搜索文档，可以直接在 VS Code 中使用 Microsoft Learn Docs MCP 服务器，实现：

- 在 VS Code 内搜索和阅读文档，无需离开编码环境。
- 直接引用文档并插入链接到 README 或课程文件中。
- 结合 GitHub Copilot 和 MCP，实现无缝的 AI 驱动文档工作流。

**示例用例：**  
- 在编写课程或项目文档时快速添加引用链接到 README。  
- 使用 Copilot 生成代码，同时用 MCP 即时查找并引用相关文档。  
- 保持专注于编辑器，提高工作效率。

> [!IMPORTANT]  
> 确保你有一个有效的 [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

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

这些示例展示了该应用在不同学习目标和时间安排上的灵活性。

## 参考资料

- [Chainlit 文档](https://docs.chainlit.io/)
- [MCP 文档](https://github.com/MicrosoftDocs/mcp)

**免责声明**：  
本文件使用AI翻译服务[Co-op Translator](https://github.com/Azure/co-op-translator)进行翻译。尽管我们力求准确，但请注意，自动翻译可能存在错误或不准确之处。原始文件的原文版本应被视为权威来源。对于重要信息，建议使用专业人工翻译。对于因使用本翻译而产生的任何误解或误释，我们不承担任何责任。