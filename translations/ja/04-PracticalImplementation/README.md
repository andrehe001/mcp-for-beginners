<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5384bbb2a92d00d5d7e66274dbe0331d",
  "translation_date": "2025-06-20T18:24:10+00:00",
  "source_file": "04-PracticalImplementation/README.md",
  "language_code": "ja"
}
-->
# 実践的な実装

実践的な実装は、Model Context Protocol（MCP）の力が実感できる場です。MCPの理論やアーキテクチャを理解することは重要ですが、実際にこれらの概念を応用して、現実の問題を解決するソリューションを構築、テスト、デプロイすることで真の価値が生まれます。本章では、概念的な知識と実践的な開発の橋渡しを行い、MCPベースのアプリケーションを実際に動かすプロセスを案内します。

インテリジェントアシスタントの開発、ビジネスワークフローへのAI統合、データ処理のためのカスタムツール構築など、MCPは柔軟な基盤を提供します。言語に依存しない設計と主要なプログラミング言語向けの公式SDKにより、幅広い開発者が利用可能です。これらのSDKを活用することで、さまざまなプラットフォームや環境で迅速にプロトタイプを作成し、反復し、スケールさせることができます。

以下のセクションでは、C#、Java、TypeScript、JavaScript、PythonでのMCP実装例、サンプルコード、デプロイ戦略を紹介します。また、MCPサーバーのデバッグとテスト、API管理、Azureを使ったクラウドへのデプロイ方法も学べます。これらの実践的なリソースは学習を加速し、堅牢で本番環境対応のMCPアプリケーションを自信を持って構築する手助けとなるでしょう。

## 概要

本レッスンでは、複数のプログラミング言語にわたるMCP実装の実践的側面に焦点を当てます。C#、Java、TypeScript、JavaScript、PythonのMCP SDKを使って堅牢なアプリケーションを構築し、MCPサーバーのデバッグとテスト、再利用可能なリソース、プロンプト、ツールの作成方法を探ります。

## 学習目標

このレッスンの終了時には、以下ができるようになります：
- 公式SDKを使ってさまざまなプログラミング言語でMCPソリューションを実装する
- MCPサーバーを体系的にデバッグおよびテストする
- サーバー機能（リソース、プロンプト、ツール）を作成し利用する
- 複雑なタスク向けに効果的なMCPワークフローを設計する
- パフォーマンスと信頼性を考慮したMCP実装を最適化する

## 公式SDKリソース

Model Context Protocolは複数の言語向けに公式SDKを提供しています：

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) 
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

## MCP SDKの利用

このセクションでは、複数のプログラミング言語でのMCP実装の実例を示します。言語別に整理された`samples`ディレクトリ内にサンプルコードがあります。

### 利用可能なサンプル

リポジトリには以下の言語での[サンプル実装](../../../04-PracticalImplementation/samples)が含まれています：

- [C#](./samples/csharp/README.md)
- [Java](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

各サンプルは、その言語やエコシステムにおける主要なMCPの概念と実装パターンを示しています。

## コアサーバー機能

MCPサーバーは以下の機能の組み合わせを実装できます：

### リソース
リソースはユーザーやAIモデルが利用するためのコンテキストやデータを提供します：
- ドキュメントリポジトリ
- ナレッジベース
- 構造化データソース
- ファイルシステム

### プロンプト
プロンプトはユーザー向けのテンプレート化されたメッセージやワークフローです：
- 事前定義された会話テンプレート
- ガイド付きのインタラクションパターン
- 専門的な対話構造

### ツール
ツールはAIモデルが実行する関数です：
- データ処理ユーティリティ
- 外部API連携
- 計算機能
- 検索機能

## サンプル実装：C#

公式C# SDKリポジトリには、MCPのさまざまな側面を示す複数のサンプル実装が含まれています：

- **Basic MCP Client**：MCPクライアントの作成とツール呼び出しの簡単な例
- **Basic MCP Server**：基本的なツール登録を含む最小限のサーバー実装
- **Advanced MCP Server**：ツール登録、認証、エラーハンドリングを備えたフル機能サーバー
- **ASP.NET統合**：ASP.NET Coreとの統合例
- **ツール実装パターン**：異なる複雑さのツール実装パターン

C# MCP SDKはプレビュー版であり、APIは変更される可能性があります。SDKの進化に伴い、このブログは継続的に更新されます。

### 主な機能
- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)

- [最初のMCPサーバー構築](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/)

完全なC#実装サンプルは[公式C# SDKサンプルリポジトリ](https://github.com/modelcontextprotocol/csharp-sdk)をご覧ください。

## サンプル実装：Java実装

Java SDKはエンタープライズグレードの機能を備えた堅牢なMCP実装オプションを提供します。

### 主な機能

- Spring Framework統合
- 強力な型安全性
- リアクティブプログラミング対応
- 包括的なエラーハンドリング

完全なJava実装サンプルは、サンプルディレクトリの[Javaサンプル](samples/java/containerapp/README.md)をご覧ください。

## サンプル実装：JavaScript実装

JavaScript SDKは軽量で柔軟なMCP実装を提供します。

### 主な機能

- Node.jsおよびブラウザ対応
- PromiseベースのAPI
- Expressなどのフレームワークとの簡単な統合
- ストリーミング用のWebSocket対応

完全なJavaScript実装サンプルは、サンプルディレクトリの[JavaScriptサンプル](samples/javascript/README.md)をご覧ください。

## サンプル実装：Python実装

Python SDKはPythonらしいアプローチでMCPを実装し、優れたMLフレームワーク統合を提供します。

### 主な機能

- asyncioによるasync/awaitサポート
- FlaskおよびFastAPI統合
- シンプルなツール登録
- 人気のMLライブラリとのネイティブ統合

完全なPython実装サンプルは、サンプルディレクトリの[Pythonサンプル](samples/python/README.md)をご覧ください。

## API管理

Azure API ManagementはMCPサーバーを保護するための優れたソリューションです。MCPサーバーの前にAzure API Managementインスタンスを配置し、以下のような必要な機能を担当させます：

- レート制限
- トークン管理
- モニタリング
- ロードバランシング
- セキュリティ

### Azureサンプル

以下は、MCPサーバーを作成しAzure API Managementで保護するサンプルです：[Azureサンプル](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)。

認証フローは以下の画像のように行われます：

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

上記画像の流れ：

- Microsoft Entraを使った認証／認可が行われる
- Azure API Managementがゲートウェイとして機能し、ポリシーを使ってトラフィックを管理
- Azure Monitorがすべてのリクエストをログに記録し、分析に活用

#### 認可フロー

認可フローを詳細に見てみましょう：

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP認可仕様

[MCP認可仕様](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization#2-10-third-party-authorization-flow)について詳しく学べます。

## AzureへのリモートMCPサーバーのデプロイ

先ほど紹介したサンプルをデプロイしてみましょう：

1. リポジトリをクローン

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

2. `Microsoft.App`プロバイダーを登録し、登録完了を確認します

    `az provider register --namespace Microsoft.App --wait`  
    または  
    `Register-AzResourceProvider -ProviderNamespace Microsoft.App`  
    しばらく待ってから、`(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState`で状態を確認します。

3. 以下の[azd](https://aka.ms/azd)コマンドを実行し、API Managementサービス、Function App（コード付き）、その他必要なAzureリソースをプロビジョニングします

    ```shell
    azd up
    ```

    このコマンドでAzure上のすべてのクラウドリソースがデプロイされます。

### MCP Inspectorを使ったサーバーのテスト

1. **新しいターミナルウィンドウ**でMCP Inspectorをインストールし実行

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    以下のようなインターフェースが表示されます：

    ![Connect to Node inspector](../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.ja.png)

2. 表示されたURL（例：http://127.0.0.1:6274/#resources）をCTRLクリックしてMCP InspectorのWebアプリを開く
3. トランスポートタイプを`SSE`に設定し、**接続**：

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

5. **ツールの一覧表示**。ツールをクリックし、**ツールを実行**。

すべての手順が成功すれば、MCPサーバーに接続され、ツールを呼び出すことができています。

## Azure向けMCPサーバー

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet)：このリポジトリ群は、Azure Functionsを使ってPython、C# .NET、Node/TypeScriptでカスタムリモートMCPサーバーを構築・デプロイするためのクイックスタートテンプレートです。

サンプルは開発者に以下の完全なソリューションを提供します：

- ローカルでの構築と実行：ローカル環境でMCPサーバーを開発・デバッグ
- Azureへのデプロイ：シンプルな`azd up`コマンドでクラウドに簡単デプロイ
- クライアントからの接続：VS CodeのCopilotエージェントモードやMCP Inspectorツールなど、多様なクライアントから接続可能

### 主な機能

- セキュリティ設計：MCPサーバーはキーとHTTPSで保護
- 認証オプション：組み込み認証およびAPI Managementを使ったOAuth対応
- ネットワーク分離：Azure Virtual Networks（VNET）によるネットワーク分離
- サーバーレスアーキテクチャ：スケーラブルなイベント駆動実行をAzure Functionsで実現
- ローカル開発：包括的なローカル開発とデバッグサポート
- 簡単なデプロイ：Azureへのスムーズなデプロイプロセス

このリポジトリには、プロダクション対応のMCPサーバー実装を迅速に開始するためのすべての設定ファイル、ソースコード、インフラ定義が含まれています。

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - PythonでAzure Functionsを使ったMCPのサンプル実装
- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - C# .NETでAzure Functionsを使ったMCPのサンプル実装
- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Node/TypeScriptでAzure Functionsを使ったMCPのサンプル実装

## まとめ

- MCP SDKは言語ごとに堅牢なMCPソリューションを実装するためのツールを提供する
- デバッグとテストのプロセスは信頼性の高いMCPアプリケーションに不可欠
- 再利用可能なプロンプトテンプレートは一貫したAIインタラクションを実現
- よく設計されたワークフローは複数のツールを使った複雑なタスクをオーケストレーションできる
- MCPソリューションの実装にはセキュリティ、パフォーマンス、エラーハンドリングを考慮する必要がある

## 演習

あなたの分野の現実的な問題に対応する実践的なMCPワークフローを設計してください：

1. 問題解決に役立つ3〜4のツールを特定する
2. これらのツールがどのように連携するかを示すワークフローダイアグラムを作成する
3. 好みの言語でツールの基本バージョンを実装する
4. モデルが効果的にツールを使うためのプロンプトテンプレートを作成する

## 追加リソース


---

次へ：[高度なトピック](../05-AdvancedTopics/README.md)

**免責事項**：  
本書類はAI翻訳サービス[Co-op Translator](https://github.com/Azure/co-op-translator)を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご了承ください。原文は原言語の文書が正式な情報源とみなされます。重要な情報については、専門の人間による翻訳を推奨いたします。本翻訳の利用により生じた誤解や誤訳について、当方は一切の責任を負いかねます。