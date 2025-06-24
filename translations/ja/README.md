<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5dc09d7099d2f09f3e472bc8f073622d",
  "translation_date": "2025-06-23T14:21:20+00:00",
  "source_file": "README.md",
  "language_code": "ja"
}
-->
![MCP-for-beginners](../../translated_images/mcp-beginners.2ce2b317996369ff66c5b72e25eff9d4288ab2741fc70c0b4e523d1ae1e249fd.ja.png) 

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/mcp-for-beginners.svg)](https://GitHub.com/microsoft/mcp-for-beginners/graphs/contributors)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/mcp-for-beginners.svg)](https://GitHub.com/microsoft/mcp-for-beginners/issues)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/mcp-for-beginners.svg)](https://GitHub.com/microsoft/mcp-for-beginners/pulls)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/mcp-for-beginners.svg?style=social&label=Watch)](https://GitHub.com/microsoft/mcp-for-beginners/watchers)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/mcp-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/mcp-for-beginners/fork)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/mcp-for-beginners?style=social&label=Star)](https://GitHub.com/microsoft/mcp-for-beginners/stargazers)


[![Microsoft Azure AI Foundry Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4)


これらのリソースを使い始めるには、以下の手順に従ってください：
1. **リポジトリをフォークする**: クリック [![GitHub forks](https://img.shields.io/github/forks/microsoft/mcp-for-beginners.svg?style=social&label=Fork)](https://GitHub.com/microsoft/mcp-for-beginners/fork)
2. **リポジトリをクローンする**:   `git clone https://github.com/microsoft/mcp-for-beginners.git`
3. [**Azure AI Foundry Discordに参加して、専門家や他の開発者と交流しましょう**](https://discord.com/invite/ByRwuEEgH4)


### 🌐 多言語対応

#### GitHub Actionによるサポート（自動化＆常に最新）

# 🚀 Model Context Protocol (MCP) 初心者向けカリキュラム

## **C#, Java, JavaScript, Python, TypeScriptで学ぶMCPの実践コード例**

## 🧠 Model Context Protocolカリキュラムの概要

**Model Context Protocol (MCP)** は、AIモデルとクライアントアプリケーション間のやり取りを標準化するために設計された最先端のフレームワークです。このオープンソースのカリキュラムは、C#, Java, JavaScript, TypeScript, Pythonなどの主要なプログラミング言語での実践的なコード例や実際のユースケースを通じて、体系的な学習ルートを提供します。

AI開発者、システムアーキテクト、ソフトウェアエンジニアのいずれであっても、このガイドはMCPの基本と実装戦略を習得するための総合的なリソースです。

## 🔗 公式MCPリソース

- 📘 [MCP Documentation](https://modelcontextprotocol.io/) – 詳細なチュートリアルとユーザーガイド  
- 📜 [MCP Specification](https://spec.modelcontextprotocol.io/) – プロトコルの構造と技術資料  
- 🧑‍💻 [MCP GitHub Repository](https://github.com/modelcontextprotocol) – オープンソースSDK、ツール、コードサンプル  

## 🧭 MCPカリキュラム概要

<details>
  <summary><strong>00-03: 基礎</strong></summary>

- **00. MCPの紹介**  
  Model Context Protocolの概要とAIパイプラインにおける重要性について。 [続きを読む](./00-Introduction/README.md)
- **01. コアコンセプトの解説**  
  MCPの基本概念を詳しく掘り下げます。 [続きを読む](./01-CoreConcepts/README.md)
- **02. MCPのセキュリティ**  
  セキュリティ上の脅威とベストプラクティス。 [続きを読む](./02-Security/README.md)
- **03. MCPの始め方**  
  環境設定、基本的なサーバー/クライアント、統合方法。 [続きを読む](./03-GettingStarted/README.md)
</details>

<details>
  <summary><strong>03.x: ハンズオンラボ</strong></summary>

- **3.1. 最初のサーバー** – [ガイド](./03-GettingStarted/01-first-server/README.md)
- **3.2. 最初のクライアント** – [ガイド](./03-GettingStarted/02-client/README.md)
- **3.3. LLMを使ったクライアント** – [ガイド](./03-GettingStarted/03-llm-client/README.md)
- **3.4. Visual Studio Codeでサーバーを利用する** – [ガイド](./03-GettingStarted/04-vscode/README.md)
- **3.5. SSEを使ったサーバーの作成** – [ガイド](./03-GettingStarted/05-sse-server/README.md)
- **3.6. HTTPストリーミング** – [ガイド](./03-GettingStarted/06-http-streaming/README.md)
- **3.7. AIツールキットの利用** – [ガイド](./03-GettingStarted/07-aitk/README.md)
- **3.8. サーバーのテスト** – [ガイド](./03-GettingStarted/08-testing/README.md)
- **3.9. サーバーのデプロイ** – [ガイド](./03-GettingStarted/09-deployment/README.md)
</details>

<details>
  <summary><strong>04-05: 実践＆応用</strong></summary>

- **04. 実践的な実装**  
  SDK、デバッグ、テスト、再利用可能なプロンプトテンプレート。 [続きを読む](./04-PracticalImplementation/README.md)
- **05. MCPの高度なトピック**  
  マルチモーダルAI、スケーリング、エンタープライズ利用。 [続きを読む](./05-AdvancedTopics/README.md)
- **5.1. AzureとのMCP統合** – [ガイド](./05-AdvancedTopics/mcp-integration/README.md)
- **5.2. マルチモダリティ** – [ガイド](./05-AdvancedTopics/mcp-multi-modality/README.md)
- **5.3. MCP OAuth2デモ** – [ガイド](./05-AdvancedTopics/mcp-oauth2-demo/README.md)
- **5.4. ルートコンテキスト** – [ガイド](./05-AdvancedTopics/mcp-root-contexts/README.md)
- **5.5. ルーティング** – [ガイド](./05-AdvancedTopics/mcp-routing/README.md)
- **5.6. サンプリング** – [ガイド](./05-AdvancedTopics/mcp-sampling/README.md)
- **5.7. スケーリング** – [ガイド](./05-AdvancedTopics/mcp-scaling/README.md)
- **5.8. セキュリティ** – [ガイド](./05-AdvancedTopics/mcp-security/README.md)
- **5.9. Web検索MCP** – [ガイド](./05-AdvancedTopics/web-search-mcp/README.md)
- **5.10. リアルタイムストリーミング** – [ガイド](./05-AdvancedTopics/mcp-realtimestreaming/README.md)
- **5.11. リアルタイムWeb検索** – [ガイド](./05-AdvancedTopics/mcp-realtimesearch/README.md)
</details>

<details>
  <summary><strong>06-10: コミュニティ、ベストプラクティス＆ラボ</strong></summary>

- **06. コミュニティへの貢献** – [ガイド](./06-CommunityContributions/README.md)
- **07. 早期導入からの洞察** – [Guide](./07-LessonsFromEarlyAdoption/README.md)
- **08. MCPのベストプラクティス** – [Guide](./08-BestPractices/README.md)
- **09. MCPケーススタディ** – [Guide](./09-CaseStudy/README.md)
- **10. AIワークフローの効率化：AI ToolkitでMCPサーバーを構築する** – [Hands On Lab](./10-StreamliningAIWorkflowsBuildingAnMCPServerWithAIToolkit/README.md)
</details>

## サンプルプロジェクト

### 🧮 MCP計算機サンプルプロジェクト：
<details>
  <summary><strong>言語別コード実装を確認する</strong></summary>

  - [C# MCPサーバーの例](./03-GettingStarted/samples/csharp/README.md)
  - [Java MCP計算機](./03-GettingStarted/samples/java/calculator/README.md)
  - [JavaScript MCPデモ](./03-GettingStarted/samples/javascript/README.md)
  - [Python MCPサーバー](../../03-GettingStarted/samples/python/mcp_calculator_server.py)
  - [TypeScript MCP例](./03-GettingStarted/samples/typescript/README.md)

</details>

### 💡 MCP高度計算機プロジェクト：
<details>
  <summary><strong>高度なサンプルを探る</strong></summary>

  - [高度なC#サンプル](./04-PracticalImplementation/samples/csharp/README.md)
  - [Javaコンテナアプリの例](./04-PracticalImplementation/samples/java/containerapp/README.md)
  - [JavaScript高度サンプル](./04-PracticalImplementation/samples/javascript/README.md)
  - [Python複雑な実装](../../04-PracticalImplementation/samples/python/mcp_sample.py)
  - [TypeScriptコンテナサンプル](./04-PracticalImplementation/samples/typescript/README.md)

</details>


## 🎯 MCP学習の前提条件

このカリキュラムを最大限に活用するには、以下が必要です：

- C#、Java、またはPythonの基本知識
- クライアント・サーバーモデルとAPIの理解
- （任意）機械学習の基本概念への親しみ

## 📚 学習ガイド

効果的にリポジトリを活用できる包括的な[学習ガイド](./study_guide.md)があります。ガイドには以下が含まれます：

- すべてのトピックを示すビジュアルカリキュラムマップ
- 各リポジトリセクションの詳細な内訳
- サンプルプロジェクトの活用方法の案内
- スキルレベル別の推奨学習パス
- 学習を補完する追加リソース

## 🛠️ このカリキュラムの効果的な使い方

各レッスンには以下が含まれます：

1. MCPの概念の明確な説明  
2. 複数言語によるライブコード例  
3. 実際のMCPアプリケーションを構築する演習  
4. 上級者向けの追加リソース  

## 📜 ライセンス情報

このコンテンツは**MITライセンス**のもとで提供されています。利用条件については[LICENSE](../../LICENSE)をご覧ください。

## 🤝 コントリビューションガイドライン

このプロジェクトは貢献や提案を歓迎しています。ほとんどの貢献には、あなたが貢献物の使用権を実際に持ち、付与する権利があることを宣言するContributor License Agreement（CLA）への同意が必要です。詳細は<https://cla.opensource.microsoft.com>をご覧ください。

プルリクエストを送ると、CLAボットが自動的にCLAの提出が必要かどうかを判断し、PRに適切な表示（ステータスチェックやコメントなど）を行います。ボットの指示に従ってください。CLAは当社のCLAを利用するすべてのリポジトリで一度だけ行えば十分です。

このプロジェクトは[Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/)を採用しています。詳しくは[Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/)をご覧いただくか、ご質問やご意見は[opencode@microsoft.com](mailto:opencode@microsoft.com)までお問い合わせください。

## 🎒 その他のコース
当チームでは他にもコースを提供しています！ぜひご覧ください：

- [AI Agents For Beginners](https://github.com/microsoft/ai-agents-for-beginners?WT.mc_id=academic-105485-koreyst)
- [.NETを使った初心者向け生成AI](https://github.com/microsoft/Generative-AI-for-beginners-dotnet?WT.mc_id=academic-105485-koreyst)
- [JavaScriptを使った初心者向け生成AI](https://github.com/microsoft/generative-ai-with-javascript?WT.mc_id=academic-105485-koreyst)
- [初心者向け生成AI](https://github.com/microsoft/generative-ai-for-beginners?WT.mc_id=academic-105485-koreyst)
- [初心者向け機械学習](https://aka.ms/ml-beginners?WT.mc_id=academic-105485-koreyst)
- [初心者向けデータサイエンス](https://aka.ms/datascience-beginners?WT.mc_id=academic-105485-koreyst)
- [初心者向けAI](https://aka.ms/ai-beginners?WT.mc_id=academic-105485-koreyst)
- [初心者向けサイバーセキュリティ](https://github.com/microsoft/Security-101??WT.mc_id=academic-96948-sayoung)
- [初心者向けWeb開発](https://aka.ms/webdev-beginners?WT.mc_id=academic-105485-koreyst)
- [初心者向けIoT](https://aka.ms/iot-beginners?WT.mc_id=academic-105485-koreyst)
- [初心者向けXR開発](https://github.com/microsoft/xr-development-for-beginners?WT.mc_id=academic-105485-koreyst)
- [Mastering GitHub Copilot for AI Paired Programming](https://aka.ms/GitHubCopilotAI?WT.mc_id=academic-105485-koreyst)
- [Mastering GitHub Copilot for C#/.NET Developers](https://github.com/microsoft/mastering-github-copilot-for-dotnet-csharp-developers?WT.mc_id=academic-105485-koreyst)
- [Choose Your Own Copilot Adventure](https://github.com/microsoft/CopilotAdventures?WT.mc_id=academic-105485-koreyst)


## ™️ 商標に関する注意

このプロジェクトには、プロジェクト、製品、またはサービスの商標やロゴが含まれている場合があります。Microsoftの商標やロゴの正当な使用は、[Microsoftの商標およびブランドガイドライン](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)に従う必要があります。
このプロジェクトの改変版でMicrosoftの商標やロゴを使用する場合、混乱を招いたりMicrosoftの後援を示唆したりしてはなりません。
第三者の商標やロゴの使用は、それら第三者のポリシーに従います。

**免責事項**：  
本書類はAI翻訳サービス「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用して翻訳されました。正確性の向上に努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文（原言語の文書）が正式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用により生じた誤解や解釈の相違について、当方は一切の責任を負いかねます。