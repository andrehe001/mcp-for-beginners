<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:27:44+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "ja"
}
-->
# Chainlit と Microsoft Learn Docs MCP を使った学習計画ジェネレーター

## 前提条件

- Python 3.8 以上
- pip（Python パッケージマネージャー）
- Microsoft Learn Docs MCP サーバーに接続するためのインターネット接続

## インストール

1. このリポジトリをクローンするか、プロジェクトファイルをダウンロードします。
2. 必要な依存関係をインストールします：

   ```bash
   pip install -r requirements.txt
   ```

## 使い方

### シナリオ 1: Docs MCP へのシンプルなクエリ
Docs MCP サーバーに接続し、クエリを送信して結果を表示するコマンドラインクライアントです。

1. スクリプトを実行します：
   ```bash
   python scenario1.py
   ```
2. プロンプトでドキュメントに関する質問を入力します。

### シナリオ 2: 学習計画ジェネレーター（Chainlit Web アプリ）
Chainlit を使ったウェブベースのインターフェースで、任意の技術トピックに対して週ごとのパーソナライズされた学習計画を生成します。

1. Chainlit アプリを起動します：
   ```bash
   chainlit run scenario2.py
   ```
2. ターミナルに表示されるローカル URL（例：http://localhost:8000）をブラウザで開きます。
3. チャットウィンドウに学習したいトピックと期間（例：「AI-900 certification, 8 weeks」）を入力します。
4. アプリが週ごとの学習計画を返し、関連する Microsoft Learn のドキュメントへのリンクも表示します。

**必要な環境変数：**

シナリオ 2（Azure OpenAI を使った Chainlit Web アプリ）を利用するには、`.env` file in the `python` ディレクトリに以下の環境変数を設定してください：

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

アプリを実行する前に、これらの値をあなたの Azure OpenAI リソースの情報で埋めてください。

> **ヒント：** [Azure AI Foundry](https://ai.azure.com/) を使えば、自分のモデルを簡単にデプロイできます。

### シナリオ 3: VS Code で MCP サーバーを使ったエディター内ドキュメント

ブラウザのタブを切り替えてドキュメントを検索する代わりに、VS Code 内に Microsoft Learn Docs を直接取り込むことができます。これにより以下が可能になります：
- コーディング環境を離れずに VS Code 内でドキュメントを検索・閲覧できる
- ドキュメントを参照し、README やコースファイルにリンクを直接挿入できる
- GitHub Copilot と MCP を組み合わせて、AI を活用したシームレスなドキュメントワークフローを実現できる

**活用例：**
- コースやプロジェクトのドキュメントを書きながら、README に素早く参照リンクを追加する
- Copilot でコードを生成しつつ、MCP で関連ドキュメントを即座に検索・引用する
- エディターに集中して生産性を高める

> [!IMPORTANT]
> 有効な [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

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

これらの例は、さまざまな学習目標や期間に応じたアプリの柔軟性を示しています。

## 参考資料

- [Chainlit ドキュメント](https://docs.chainlit.io/)
- [MCP ドキュメント](https://github.com/MicrosoftDocs/mcp)

**免責事項**：  
本書類はAI翻訳サービス「Co-op Translator」（https://github.com/Azure/co-op-translator）を使用して翻訳されました。正確性を期しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があることをご承知おきください。原文の言語によるオリジナル文書が正式な情報源とみなされます。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用により生じたいかなる誤解や解釈の相違についても、当方は責任を負いかねます。