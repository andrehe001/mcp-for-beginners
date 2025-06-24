<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "36de9fae488d6de554d969fe8e0801a8",
  "translation_date": "2025-06-20T19:18:01+00:00",
  "source_file": "09-CaseStudy/apimsample.md",
  "language_code": "pa"
}
-->
# ਕੇਸ ਸਟੱਡੀ: API Management ਵਿੱਚ REST API ਨੂੰ MCP ਸਰਵਰ ਵਜੋਂ ਖੋਲ੍ਹਣਾ

Azure API Management ਇੱਕ ਸੇਵਾ ਹੈ ਜੋ ਤੁਹਾਡੇ API Endpoints ਦੇ ਉੱਪਰ ਗੇਟਵੇ ਪ੍ਰਦਾਨ ਕਰਦੀ ਹੈ। ਇਹ ਇਸ ਤਰ੍ਹਾਂ ਕੰਮ ਕਰਦੀ ਹੈ ਕਿ Azure API Management ਤੁਹਾਡੇ APIs ਦੇ ਸਾਹਮਣੇ ਪ੍ਰਾਕਸੀ ਵਾਂਗ ਕੰਮ ਕਰਦਾ ਹੈ ਅਤੇ ਆ ਰਹੀਆਂ ਬੇਨਤੀਆਂ ਨਾਲ ਕੀ ਕਰਨਾ ਹੈ, ਇਹ ਫੈਸਲਾ ਕਰ ਸਕਦਾ ਹੈ।

ਇਸਦਾ ਉਪਯੋਗ ਕਰਕੇ, ਤੁਸੀਂ ਕਈ ਫੀਚਰ ਜੋੜ ਸਕਦੇ ਹੋ ਜਿਵੇਂ ਕਿ:

- **ਸੁਰੱਖਿਆ**, ਤੁਸੀਂ API keys, JWT ਤੋਂ ਲੈ ਕੇ managed identity ਤੱਕ ਹਰ ਚੀਜ਼ ਵਰਤ ਸਕਦੇ ਹੋ।
- **ਰੇਟ ਲਿਮਿਟਿੰਗ**, ਇਹ ਬਹੁਤ ਵਧੀਆ ਫੀਚਰ ਹੈ ਜਿਸ ਨਾਲ ਤੁਸੀਂ ਨਿਰਧਾਰਿਤ ਸਮੇਂ ਵਿੱਚ ਕਿੰਨੀ ਕਾਲਾਂ ਹੋਣੀਆਂ ਚਾਹੀਦੀਆਂ ਹਨ, ਇਹ ਨਿਰਧਾਰਿਤ ਕਰ ਸਕਦੇ ਹੋ। ਇਹ ਯਕੀਨੀ ਬਣਾਉਂਦਾ ਹੈ ਕਿ ਸਾਰੇ ਉਪਭੋਗਤਾਵਾਂ ਦਾ ਤਜਰਬਾ ਵਧੀਆ ਰਹੇ ਅਤੇ ਤੁਹਾਡੀ ਸੇਵਾ ਬੇਨਤੀਆਂ ਨਾਲ ਓਵਰਲੋਡ ਨਾ ਹੋਵੇ।
- **ਸਕੇਲਿੰਗ ਅਤੇ ਲੋਡ ਬੈਲੈਂਸਿੰਗ**। ਤੁਸੀਂ ਕਈ endpoints ਸੈੱਟ ਕਰਕੇ ਲੋਡ ਬੈਲੈਂਸ ਕਰ ਸਕਦੇ ਹੋ ਅਤੇ ਇਹ ਵੀ ਫੈਸਲਾ ਕਰ ਸਕਦੇ ਹੋ ਕਿ "ਲੋਡ ਬੈਲੈਂਸ" ਕਿਵੇਂ ਕਰਨਾ ਹੈ।
- **AI ਫੀਚਰ ਜਿਵੇਂ semantic caching**, token limit ਅਤੇ token monitoring ਆਦਿ। ਇਹ ਵਧੀਆ ਫੀਚਰ ਹਨ ਜੋ ਜਵਾਬਦੇਹੀ ਨੂੰ ਬਿਹਤਰ ਬਣਾਉਂਦੇ ਹਨ ਅਤੇ ਤੁਹਾਡੇ token ਖਰਚ 'ਤੇ ਨਜ਼ਰ ਰੱਖਣ ਵਿੱਚ ਮਦਦ ਕਰਦੇ ਹਨ। [ਹੋਰ ਪੜ੍ਹੋ ਇੱਥੇ](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities)।

## ਕਿਉਂ MCP + Azure API Management?

Model Context Protocol ਤੇਜ਼ੀ ਨਾਲ agentic AI ਐਪਸ ਲਈ ਇੱਕ ਮਿਆਰੀ ਤਰੀਕੇ ਵਜੋਂ ਵਧ ਰਿਹਾ ਹੈ ਅਤੇ ਟੂਲਜ਼ ਅਤੇ ਡੇਟਾ ਨੂੰ ਇੱਕ ਸੰਗਠਿਤ ਤਰੀਕੇ ਨਾਲ ਪ੍ਰਗਟ ਕਰਨ ਦਾ ਤਰੀਕਾ ਬਣ ਰਿਹਾ ਹੈ। ਜਦੋਂ ਤੁਹਾਨੂੰ APIs "ਮੈਨੇਜ" ਕਰਨੇ ਹੁੰਦੇ ਹਨ ਤਾਂ Azure API Management ਇੱਕ ਕੁਦਰਤੀ ਚੋਣ ਹੈ। MCP Servers ਅਕਸਰ ਹੋਰ APIs ਨਾਲ ਇੰਟੀਗ੍ਰੇਟ ਹੁੰਦੇ ਹਨ ਜਿਵੇਂ ਕਿ ਕਿਸੇ ਟੂਲ ਲਈ ਬੇਨਤੀ ਹੱਲ ਕਰਨ ਲਈ। ਇਸ ਲਈ Azure API Management ਅਤੇ MCP ਦਾ ਮਿਲਾਪ ਬਹੁਤ ਮਾਨਯੂਕ ਹੈ।

## ਓਵਰਵਿਊ

ਇਸ ਖਾਸ ਉਪਯੋਗ ਮਾਮਲੇ ਵਿੱਚ ਅਸੀਂ ਸਿੱਖਾਂਗੇ ਕਿ API endpoints ਨੂੰ MCP Server ਵਜੋਂ ਕਿਵੇਂ ਖੋਲ੍ਹਣਾ ਹੈ। ਇਸ ਤਰ੍ਹਾਂ, ਅਸੀਂ ਇਹ endpoints ਅਸਾਨੀ ਨਾਲ ਇੱਕ agentic ਐਪ ਦਾ ਹਿੱਸਾ ਬਣਾ ਸਕਦੇ ਹਾਂ ਅਤੇ ਨਾਲ ਹੀ Azure API Management ਦੇ ਫੀਚਰਾਂ ਦਾ ਲਾਭ ਵੀ ਉਠਾ ਸਕਦੇ ਹਾਂ।

## ਮੁੱਖ ਫੀਚਰ

- ਤੁਸੀਂ ਉਹ endpoint methods ਚੁਣਦੇ ਹੋ ਜੋ ਤੁਸੀਂ ਟੂਲ ਵਜੋਂ ਖੋਲ੍ਹਣਾ ਚਾਹੁੰਦੇ ਹੋ।
- ਹੋਰ ਫੀਚਰ ਜੋ ਤੁਹਾਨੂੰ ਮਿਲਦੇ ਹਨ, ਉਹ ਤੁਹਾਡੇ API ਲਈ policy ਸੈਕਸ਼ਨ ਵਿੱਚ ਕੀ ਕਨਫਿਗਰ ਕੀਤਾ ਹੈ, ਇਸ 'ਤੇ ਨਿਰਭਰ ਕਰਦੇ ਹਨ। ਪਰ ਇੱਥੇ ਅਸੀਂ ਦਿਖਾਵਾਂਗੇ ਕਿ ਤੁਸੀਂ ਰੇਟ ਲਿਮਿਟਿੰਗ ਕਿਵੇਂ ਜੋੜ ਸਕਦੇ ਹੋ।

## ਪਹਿਲਾ ਕਦਮ: API ਇੰਪੋਰਟ ਕਰੋ

ਜੇ ਤੁਹਾਡੇ ਕੋਲ ਪਹਿਲਾਂ ਹੀ Azure API Management ਵਿੱਚ API ਹੈ, ਤਾਂ ਇਹ ਕਦਮ ਛੱਡ ਸਕਦੇ ਹੋ। ਨਹੀਂ ਤਾਂ, ਇਸ ਲਿੰਕ ਨੂੰ ਵੇਖੋ, [Azure API Management ਵਿੱਚ API ਇੰਪੋਰਟ ਕਰਨਾ](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api)।

## API ਨੂੰ MCP ਸਰਵਰ ਵਜੋਂ ਖੋਲ੍ਹਣਾ

API endpoints ਨੂੰ ਖੋਲ੍ਹਣ ਲਈ, ਇਹ ਕਦਮ ਫਾਲੋ ਕਰੋ:

1. Azure Portal ਤੇ ਜਾਓ ਅਤੇ ਇਸ ਪਤੇ ਤੇ ਜਾਓ <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
ਆਪਣੇ API Management ਇੰਸਟੈਂਸ ਤੇ ਜਾਓ।

1. ਖੱਬੇ ਮੈਨੂ ਵਿੱਚ, APIs > MCP Servers > + Create new MCP Server ਚੁਣੋ।

1. API ਵਿੱਚ, ਇੱਕ REST API ਚੁਣੋ ਜੋ MCP ਸਰਵਰ ਵਜੋਂ ਖੋਲ੍ਹਣਾ ਹੈ।

1. ਇੱਕ ਜਾਂ ਵਧੇਰੇ API Operations ਚੁਣੋ ਜੋ ਟੂਲ ਵਜੋਂ ਖੋਲ੍ਹਣੇ ਹਨ। ਤੁਸੀਂ ਸਾਰੇ operations ਜਾਂ ਕੁਝ ਖਾਸ operations ਚੁਣ ਸਕਦੇ ਹੋ।

    ![Select methods to expose](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. **Create** ਚੁਣੋ।

1. ਮੈਨੂ ਵਿੱਚ APIs ਅਤੇ MCP Servers ਤੇ ਜਾਓ, ਤੁਹਾਨੂੰ ਇਹ ਦਿਖਾਈ ਦੇਵੇਗਾ:

    ![See the MCP Server in the main pane](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP ਸਰਵਰ ਬਣਾਇਆ ਗਿਆ ਹੈ ਅਤੇ API operations ਟੂਲ ਵਜੋਂ ਖੋਲ੍ਹੇ ਗਏ ਹਨ। MCP ਸਰਵਰ MCP Servers ਪੈਨ ਵਿੱਚ ਲਿਸਟ ਹੈ। URL ਕਾਲਮ MCP ਸਰਵਰ ਦਾ endpoint ਦਿਖਾਉਂਦਾ ਹੈ ਜਿਸਨੂੰ ਤੁਸੀਂ ਟੈਸਟਿੰਗ ਜਾਂ ਕਲਾਇੰਟ ਐਪਲੀਕੇਸ਼ਨ ਵਿੱਚ ਕਾਲ ਕਰ ਸਕਦੇ ਹੋ।

## ਵਿਕਲਪਿਕ: ਨੀਤੀਆਂ (policies) ਕਨਫਿਗਰ ਕਰੋ

Azure API Management ਵਿੱਚ ਨੀਤੀਆਂ ਦਾ ਮੁੱਖ ਧਾਰਣਾ ਹੁੰਦੀ ਹੈ ਜਿੱਥੇ ਤੁਸੀਂ ਆਪਣੇ endpoints ਲਈ ਵੱਖ-ਵੱਖ ਨਿਯਮ ਸੈੱਟ ਕਰਦੇ ਹੋ, ਜਿਵੇਂ ਕਿ ਰੇਟ ਲਿਮਿਟਿੰਗ ਜਾਂ semantic caching। ਇਹ ਨੀਤੀਆਂ XML ਵਿੱਚ ਲਿਖੀਆਂ ਜਾਂਦੀਆਂ ਹਨ।

ਇੱਥੇ ਦਿੱਤਾ ਹੈ ਕਿ ਤੁਸੀਂ MCP Server ਲਈ ਰੇਟ ਲਿਮਿਟ ਕਿਵੇਂ ਸੈੱਟ ਕਰ ਸਕਦੇ ਹੋ:

1. ਪੋਰਟਲ ਵਿੱਚ, APIs ਹੇਠਾਂ **MCP Servers** ਚੁਣੋ।

1. ਉਹ MCP ਸਰਵਰ ਚੁਣੋ ਜੋ ਤੁਸੀਂ ਬਣਾਇਆ ਸੀ।

1. ਖੱਬੇ ਮੈਨੂ ਵਿੱਚ MCP ਹੇਠਾਂ **Policies** ਚੁਣੋ।

1. ਨੀਤੀ ਸੰਪਾਦਕ (policy editor) ਵਿੱਚ, ਉਹ ਨੀਤੀਆਂ ਜੋ ਤੁਸੀਂ MCP ਸਰਵਰ ਦੇ ਟੂਲਜ਼ 'ਤੇ ਲਾਗੂ ਕਰਨਾ ਚਾਹੁੰਦੇ ਹੋ, ਜੋੜੋ ਜਾਂ ਸੋਧੋ। ਨੀਤੀਆਂ XML ਫਾਰਮੈਟ ਵਿੱਚ ਹੁੰਦੀਆਂ ਹਨ। ਉਦਾਹਰਨ ਵਜੋਂ, ਤੁਸੀਂ MCP ਸਰਵਰ ਦੇ ਟੂਲਜ਼ ਨੂੰ ਕਾਲਾਂ ਦੀ ਗਿਣਤੀ ਸੀਮਤ ਕਰਨ ਲਈ ਨੀਤੀ ਜੋੜ ਸਕਦੇ ਹੋ (ਇਸ ਉਦਾਹਰਨ ਵਿੱਚ, 30 ਸਕਿੰਟ ਵਿੱਚ ਹਰ ਕਲਾਇੰਟ IP ਲਈ 5 ਕਾਲਾਂ)। ਇਹ XML ਨੀਤੀ ਰੇਟ ਲਿਮਿਟ ਕਰੇਗੀ:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    ਨੀਤੀ ਸੰਪਾਦਕ ਦੀ ਇੱਕ ਤਸਵੀਰ:

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## ਇਸਨੂੰ ਅਜ਼ਮਾਓ

ਆਓ ਯਕੀਨੀ ਬਣਾਈਏ ਕਿ ਸਾਡਾ MCP Server ਠੀਕ ਤਰ੍ਹਾਂ ਕੰਮ ਕਰ ਰਿਹਾ ਹੈ।

ਇਸ ਲਈ ਅਸੀਂ Visual Studio Code ਅਤੇ GitHub Copilot ਦੇ Agent ਮੋਡ ਦੀ ਵਰਤੋਂ ਕਰਾਂਗੇ। ਅਸੀਂ MCP ਸਰਵਰ ਨੂੰ *mcp.json* ਵਿੱਚ ਜੋੜਾਂਗੇ। ਇਸ ਤਰ੍ਹਾਂ, Visual Studio Code ਇੱਕ agentic ਸਮਰੱਥਾ ਵਾਲਾ ਕਲਾਇੰਟ ਵਜੋਂ ਕੰਮ ਕਰੇਗਾ ਅਤੇ ਅੰਤ ਉਪਭੋਗਤਾ ਪ੍ਰਾਂਪਟ ਲਿਖ ਕੇ ਇਸ ਸਰਵਰ ਨਾਲ ਇੰਟਰੈਕਟ ਕਰ ਸਕਣਗੇ।

Visual Studio Code ਵਿੱਚ MCP ਸਰਵਰ ਜੋੜਨ ਦਾ ਤਰੀਕਾ:

1. Command Palette ਤੋਂ MCP: **Add Server command** ਚਲਾਓ।

1. ਪੁੱਛੇ ਜਾਣ 'ਤੇ, ਸਰਵਰ ਟਾਈਪ ਚੁਣੋ: **HTTP (HTTP or Server Sent Events)**।

1. MCP ਸਰਵਰ ਦਾ URL ਦਿਓ ਜੋ API Management ਵਿੱਚ ਹੈ। ਉਦਾਹਰਨ:  
**https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (SSE endpoint ਲਈ) ਜਾਂ  
**https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (MCP endpoint ਲਈ), ਧਿਆਨ ਦਿਓ ਕਿ ਟ੍ਰਾਂਸਪੋਰਟ ਵਿੱਚ ਫਰਕ `/sse` or `/mcp` ਹੈ।

1. ਆਪਣੇ ਚੋਣ ਦਾ ਸਰਵਰ ID ਦਿਓ। ਇਹ ਕੋਈ ਮਹੱਤਵਪੂਰਨ ਮੁੱਲ ਨਹੀਂ ਹੈ ਪਰ ਇਹ ਤੁਹਾਨੂੰ ਯਾਦ ਰੱਖਣ ਵਿੱਚ ਮਦਦ ਕਰੇਗਾ ਕਿ ਇਹ ਸਰਵਰ ਕਿਹੜਾ ਹੈ।

1. ਫੈਸਲਾ ਕਰੋ ਕਿ ਤੁਸੀਂ ਕਨਫਿਗਰੇਸ਼ਨ ਆਪਣੇ ਵਰਕਸਪੇਸ ਸੈਟਿੰਗਜ਼ ਵਿੱਚ ਸੇਵ ਕਰਨਾ ਹੈ ਜਾਂ ਯੂਜ਼ਰ ਸੈਟਿੰਗਜ਼ ਵਿੱਚ।

  - **ਵਰਕਸਪੇਸ ਸੈਟਿੰਗਜ਼** - ਸਰਵਰ ਕਨਫਿਗਰੇਸ਼ਨ ਇੱਕ .vscode/mcp.json ਫਾਈਲ ਵਿੱਚ ਸੇਵ ਹੁੰਦੀ ਹੈ ਜੋ ਸਿਰਫ ਮੌਜੂਦਾ ਵਰਕਸਪੇਸ ਵਿੱਚ ਉਪਲਬਧ ਹੁੰਦੀ ਹੈ।

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    ਜਾਂ ਜੇ ਤੁਸੀਂ HTTP streaming ਟ੍ਰਾਂਸਪੋਰਟ ਚੁਣਦੇ ਹੋ ਤਾਂ ਇਹ ਕੁਝ ਵੱਖਰਾ ਹੋਵੇਗਾ:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **ਯੂਜ਼ਰ ਸੈਟਿੰਗਜ਼** - ਸਰਵਰ ਕਨਫਿਗਰੇਸ਼ਨ ਤੁਹਾਡੇ ਗਲੋਬਲ *settings.json* ਵਿੱਚ ਜੋੜਿਆ ਜਾਂਦਾ ਹੈ ਅਤੇ ਸਾਰੇ ਵਰਕਸਪੇਸ ਵਿੱਚ ਉਪਲਬਧ ਹੁੰਦਾ ਹੈ। ਇਹ ਕੁਝ ਇਸ ਤਰ੍ਹਾਂ ਦਿਖਾਈ ਦੇਂਦਾ ਹੈ:

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. ਤੁਹਾਨੂੰ ਇੱਕ ਕਨਫਿਗਰੇਸ਼ਨ, ਹੈਡਰ ਵੀ ਜੋੜਨਾ ਪਵੇਗਾ ਤਾਂ ਜੋ ਇਹ Azure API Management ਵੱਲ ਸਹੀ ਤਰੀਕੇ ਨਾਲ ਪ੍ਰਮਾਣਿਤ ਹੋਵੇ। ਇਹ **Ocp-Apim-Subscription-Key** ਨਾਮਕ ਹੈਡਰ ਵਰਤਦਾ ਹੈ।

    - ਇਹ ਹੈਡਰ ਸੈਟਿੰਗਜ਼ ਵਿੱਚ ਜੋੜਨ ਦਾ ਤਰੀਕਾ:

    ![Adding header for authentication](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png)  
    ਇਸ ਨਾਲ ਇੱਕ ਪ੍ਰਾਂਪਟ ਖੁਲਦਾ ਹੈ ਜੋ ਤੁਹਾਡੇ ਕੋਲ API key ਦਾ ਮੁੱਲ ਮੰਗਦਾ ਹੈ ਜੋ ਤੁਸੀਂ Azure Portal ਵਿੱਚ ਆਪਣੇ Azure API Management ਇੰਸਟੈਂਸ ਲਈ ਲੱਭ ਸਕਦੇ ਹੋ।

    - ਇਸ ਨੂੰ *mcp.json* ਵਿੱਚ ਜੋੜਨ ਲਈ, ਤੁਸੀਂ ਇਹ ਇਸ ਤਰ੍ਹਾਂ ਕਰ ਸਕਦੇ ਹੋ:

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

### Agent ਮੋਡ ਦੀ ਵਰਤੋਂ ਕਰੋ

ਹੁਣ ਅਸੀਂ ਸੈਟਿੰਗਜ਼ ਜਾਂ *.vscode/mcp.json* ਵਿੱਚ ਸੈੱਟ ਅਪ ਹੋ ਚੁੱਕੇ ਹਾਂ। ਆਓ ਇਸਨੂੰ ਅਜ਼ਮਾਈਏ।

ਤੁਹਾਡੇ ਕੋਲ ਇੱਕ Tools ਆਈਕਨ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ, ਜਿੱਥੇ ਤੁਹਾਡੇ ਸਰਵਰ ਦੇ ਖੋਲ੍ਹੇ ਟੂਲਜ਼ ਦੀ ਸੂਚੀ ਹੋਵੇਗੀ:

![Tools from the server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Tools ਆਈਕਨ 'ਤੇ ਕਲਿੱਕ ਕਰੋ ਅਤੇ ਤੁਹਾਨੂੰ ਟੂਲਜ਼ ਦੀ ਸੂਚੀ ਦਿਖਾਈ ਦੇਵੇਗੀ:

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. ਚੈਟ ਵਿੱਚ ਪ੍ਰਾਂਪਟ ਦਿਓ ਟੂਲ ਨੂੰ ਕਾਲ ਕਰਨ ਲਈ। ਉਦਾਹਰਨ ਵਜੋਂ, ਜੇ ਤੁਸੀਂ ਇੱਕ ਟੂਲ ਚੁਣਿਆ ਹੈ ਜੋ ਕਿਸੇ ਆਰਡਰ ਬਾਰੇ ਜਾਣਕਾਰੀ ਦਿੰਦਾ ਹੈ, ਤਾਂ ਤੁਸੀਂ ਏਜੰਟ ਨੂੰ ਆਰਡਰ ਬਾਰੇ ਪੁੱਛ ਸਕਦੇ ਹੋ। ਇਹ ਇੱਕ ਉਦਾਹਰਨ ਪ੍ਰਾਂਪਟ ਹੈ:

    ```text
    get information from order 2
    ```

    ਹੁਣ ਤੁਹਾਨੂੰ ਇੱਕ ਟੂਲਜ਼ ਆਈਕਨ ਮਿਲੇਗਾ ਜੋ ਤੁਹਾਨੂੰ ਟੂਲ ਚਲਾਉਣ ਲਈ ਪੁੱਛੇਗਾ। ਚਲਾਉਣ ਜਾਰੀ ਰੱਖੋ ਚੁਣੋ, ਤੁਸੀਂ ਹੁਣ ਇੱਕ ਨਤੀਜਾ ਵੇਖੋਗੇ:

    ![Result from prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **ਉੱਪਰ ਜੋ ਤੁਸੀਂ ਵੇਖਦੇ ਹੋ ਉਹ ਇਸ ਗੱਲ 'ਤੇ ਨਿਰਭਰ ਕਰਦਾ ਹੈ ਕਿ ਤੁਸੀਂ ਕਿਹੜੇ ਟੂਲਜ਼ ਸੈੱਟ ਕੀਤੇ ਹਨ, ਪਰ ਮਕਸਦ ਇਹ ਹੈ ਕਿ ਤੁਹਾਨੂੰ ਇੱਕ ਲਿਖਤੀ ਜਵਾਬ ਮਿਲੇ।**


## ਸੰਦਰਭ

ਹੋਰ ਜਾਣਨ ਲਈ:

- [Azure API Management ਅਤੇ MCP ਉੱਤੇ ਟਿਊਟੋਰਿਅਲ](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python ਨਮੂਨਾ: Azure API Management ਦੀ ਵਰਤੋਂ ਕਰਕੇ Secure remote MCP servers (ਪ੍ਰਯੋਗਾਤਮਕ)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP ਕਲਾਇੰਟ ਅਥਾਰਾਈਜ਼ੇਸ਼ਨ ਲੈਬ](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [VS Code ਲਈ Azure API Management ਐਕਸਟੈਂਸ਼ਨ ਨਾਲ APIs ਇੰਪੋਰਟ ਅਤੇ ਮੈਨੇਜ ਕਰੋ](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Azure API Center ਵਿੱਚ ਰਿਮੋਟ MCP ਸਰਵਰ ਰਜਿਸਟਰ ਅਤੇ ਡਿਸਕਵਰ ਕਰੋ](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) - ਵਧੀਆ ਰੇਪੋ ਜੋ Azure API Management ਨਾਲ ਕਈ AI ਸਮਰੱਥਾਵਾਂ ਦਿਖਾਉਂਦਾ ਹੈ
- [AI Gateway ਵਰਕਸ਼ਾਪ](https://azure-samples.github.io/AI-Gateway/) - Azure Portal ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਵਰਕਸ਼ਾਪ ਜੋ AI ਸਮਰੱਥਾਵਾਂ ਦਾ ਮੁਲਾਂਕਣ ਕਰਨ ਦਾ ਵਧੀਆ ਤਰੀਕਾ ਹੈ।

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਨਾਲ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਆਟੋਮੈਟਿਕ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਥਿਰਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜ਼ਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਉੱਪਜਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।