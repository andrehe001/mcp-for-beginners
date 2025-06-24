<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "36de9fae488d6de554d969fe8e0801a8",
  "translation_date": "2025-06-20T19:16:04+00:00",
  "source_file": "09-CaseStudy/apimsample.md",
  "language_code": "ja"
}
-->
# ケーススタディ：API ManagementでREST APIをMCPサーバーとして公開する

Azure API Managementは、APIエンドポイントの上にゲートウェイを提供するサービスです。仕組みとしては、Azure API ManagementがAPIの前にプロキシとして機能し、受信リクエストに対してどのように処理するかを決定します。

これを使うことで、以下のような多くの機能を追加できます：

- **セキュリティ**：APIキー、JWT、マネージドIDなど幅広い認証方法を利用可能です。
- **レート制限**：一定時間あたりに通過できる呼び出し回数を制御できる優れた機能です。これにより、すべてのユーザーが快適に利用でき、サービスがリクエスト過多になるのを防げます。
- **スケーリング＆ロードバランシング**：複数のエンドポイントを設定して負荷を分散でき、ロードバランスの方法も選択可能です。
- **AI機能（セマンティックキャッシュ、トークン制限、トークン監視など）**：応答速度の向上やトークン使用状況の管理に役立つ便利な機能です。[詳細はこちら](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities)。

## なぜMCP＋Azure API Managementなのか？

Model Context Protocolは、エージェント型AIアプリやツール・データを一貫した方法で公開するための標準として急速に普及しています。APIを「管理」する必要がある場合、Azure API Managementは自然な選択肢です。MCPサーバーは他のAPIと連携してツールのリクエストを解決することが多いため、Azure API ManagementとMCPを組み合わせるのは非常に理にかなっています。

## 概要

このユースケースでは、APIエンドポイントをMCPサーバーとして公開する方法を学びます。これにより、これらのエンドポイントをエージェント型アプリの一部として簡単に利用でき、Azure API Managementの機能も活用できます。

## 主な機能

- 公開したいエンドポイントのメソッドをツールとして選択できます。
- 追加機能はAPIのポリシー設定に依存しますが、ここではレート制限の追加方法を紹介します。

## 事前準備：APIのインポート

すでにAzure API ManagementにAPIがある場合は、このステップはスキップして構いません。まだの場合は、こちらを参照してください：[Azure API ManagementへのAPIインポート](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api)。

## APIをMCPサーバーとして公開する

APIエンドポイントを公開するには、以下の手順を実行します：

1. Azureポータルにアクセスし、次のURLへ移動します <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
   API Managementインスタンスに移動します。

1. 左メニューで「APIs」＞「MCP Servers」＞「+ Create new MCP Server」を選択します。

1. 「API」から、MCPサーバーとして公開したいREST APIを選択します。

1. ツールとして公開したいAPI操作を1つ以上選択します。すべての操作を選択しても特定の操作だけ選んでも構いません。

    ![Select methods to expose](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. **Create**を選択します。

1. メニューの**APIs**と**MCP Servers**に移動すると、以下のように表示されます：

    ![See the MCP Server in the main pane](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCPサーバーが作成され、API操作がツールとして公開されます。MCP Serversの一覧に表示され、URL列にはテストやクライアントアプリケーションから呼び出すためのMCPサーバーのエンドポイントが示されます。

## 任意：ポリシーの設定

Azure API Managementにはポリシーという概念があり、レート制限やセマンティックキャッシュなど、エンドポイントに対する様々なルールを設定できます。これらのポリシーはXMLで記述されます。

MCPサーバーにレート制限のポリシーを設定する方法は以下の通りです：

1. ポータルで「APIs」＞「MCP Servers」を選択します。

1. 作成したMCPサーバーを選択します。

1. 左メニューのMCPの下にある「Policies」を選択します。

1. ポリシーエディターで、MCPサーバーのツールに適用したいポリシーを追加または編集します。ポリシーはXML形式で定義します。例えば、クライアントIPアドレスごとに30秒あたり5回の呼び出しに制限するポリシーは以下のようになります：

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    ポリシーエディターの画面例：

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## 試してみる

MCPサーバーが正しく動作しているか確認しましょう。

今回はVisual Studio CodeとGitHub CopilotのAgentモードを使います。MCPサーバーを*mcp.json*に追加することで、Visual Studio Codeがエージェント機能を持つクライアントとなり、エンドユーザーはプロンプトを入力してサーバーと対話できるようになります。

Visual Studio CodeにMCPサーバーを追加する手順：

1. コマンドパレットからMCPの**Add Serverコマンド**を実行します。

1. サーバータイプの選択を求められたら、**HTTP (HTTP or Server Sent Events)**を選択します。

1. API ManagementのMCPサーバーのURLを入力します。例：  
   **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse**（SSEエンドポイント）または  
   **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp**（MCPエンドポイント）  
   トランスポートの違いは`/sse`と`/mcp`の部分です。

1. 任意のサーバーIDを入力します。重要な値ではありませんが、サーバーインスタンスの識別に役立ちます。

1. 設定をワークスペース設定かユーザー設定のどちらに保存するか選択します。

  - **ワークスペース設定** - サーバー設定は現在のワークスペース内の.vscode/mcp.jsonファイルに保存されます。

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    またはストリーミングHTTPをトランスポートに選択した場合は以下のようになります：

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **ユーザー設定** - サーバー設定はグローバルな*settings.json*に追加され、すべてのワークスペースで利用可能です。設定は以下のようになります：

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Azure API Managementに正しく認証するために、**Ocp-Apim-Subscription-Key**というヘッダーを設定に追加する必要があります。

    - 設定への追加例：

    ![Adding header for authentication](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png)  
    これにより、APIキーの入力を求めるプロンプトが表示されます。APIキーはAzureポータルのAPI Managementインスタンスから取得できます。

    - *mcp.json*に直接追加する場合は以下のように記述します：

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

### Agentモードの利用

設定が完了したので、実際に試してみましょう。

ツールアイコンが表示され、サーバーから公開されたツールの一覧が確認できます：

![Tools from the server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. ツールアイコンをクリックすると、以下のようにツール一覧が表示されます：

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. チャットにプロンプトを入力してツールを呼び出します。例えば、注文情報を取得するツールを選択している場合、注文についてエージェントに質問できます。例：

    ```text
    get information from order 2
    ```

    すると、ツールの呼び出しを進めるかどうかのツールアイコンが表示されます。続行を選択すると、以下のように結果が表示されます：

    ![Result from prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **上記の表示は設定したツールによって異なりますが、基本的にはこのようにテキストで応答が返ってきます。**

## 参考資料

さらに詳しく学ぶには以下を参照してください：

- [Azure API ManagementとMCPのチュートリアル](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Pythonサンプル：Azure API Managementを使った安全なリモートMCPサーバー（実験的）](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)
- [MCPクライアント認証ラボ](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)
- [VS Code用Azure API Management拡張機能でAPIのインポートと管理](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)
- [Azure API CenterでリモートMCPサーバーを登録・検出する](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway)  
  Azure API Managementの多彩なAI機能を紹介する優れたリポジトリ
- [AI Gatewayワークショップ](https://azure-samples.github.io/AI-Gateway/)  
  Azureポータルを使ったワークショップが含まれており、AI機能の評価を始めるのに最適です

**免責事項**：  
本書類はAI翻訳サービス「[Co-op Translator](https://github.com/Azure/co-op-translator)」を使用して翻訳されました。正確性には努めておりますが、自動翻訳には誤りや不正確な箇所が含まれる可能性があります。原文の言語による文書が正式な情報源とみなされるべきです。重要な情報については、専門の人間翻訳をご利用いただくことを推奨します。本翻訳の使用により生じた誤解や解釈の相違について、一切の責任を負いかねますのでご了承ください。