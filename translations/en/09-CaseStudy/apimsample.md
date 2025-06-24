<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "36de9fae488d6de554d969fe8e0801a8",
  "translation_date": "2025-06-20T19:12:21+00:00",
  "source_file": "09-CaseStudy/apimsample.md",
  "language_code": "en"
}
-->
# Case Study: Expose REST API in API Management as an MCP server

Azure API Management is a service that provides a Gateway on top of your API Endpoints. It works by acting as a proxy in front of your APIs and deciding how to handle incoming requests.

By using it, you gain a wide range of features like:

- **Security**: You can use everything from API keys and JWT to managed identity.
- **Rate limiting**: A useful feature that lets you control how many calls are allowed per time unit. This ensures a great experience for all users and prevents your service from being overwhelmed.
- **Scaling & Load balancing**: You can set up multiple endpoints to distribute the load and choose how to balance it.
- **AI features like semantic caching**, token limits, token monitoring, and more. These features improve responsiveness and help you keep track of your token usage. [Read more here](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Why MCP + Azure API Management?

Model Context Protocol is rapidly becoming a standard for agentic AI apps, providing a consistent way to expose tools and data. Azure API Management is a natural fit when you need to "manage" APIs. MCP Servers often integrate with other APIs to fulfill requests to a tool, for example. So combining Azure API Management and MCP makes a lot of sense.

## Overview

In this use case, we’ll learn how to expose API endpoints as an MCP Server. This allows you to easily include these endpoints in an agentic app while also taking advantage of Azure API Management’s features.

## Key Features

- You choose which endpoint methods you want to expose as tools.
- Additional features depend on what you configure in the policy section for your API. Here, we’ll show you how to add rate limiting.

## Pre-step: import an API

If you already have an API in Azure API Management, great—you can skip this step. Otherwise, check out this link: [importing an API to Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Expose API as MCP Server

To expose the API endpoints, follow these steps:

1. Go to the Azure Portal at <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> and navigate to your API Management instance.

2. In the left menu, select APIs > MCP Servers > + Create new MCP Server.

3. Under API, select a REST API to expose as an MCP server.

4. Choose one or more API Operations to expose as tools. You can select all operations or just specific ones.

    ![Select methods to expose](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

5. Click **Create**.

6. Go to the **APIs** menu, then **MCP Servers**. You should see this:

    ![See the MCP Server in the main pane](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    The MCP server is created and the API operations are exposed as tools. The MCP server is listed in the MCP Servers pane. The URL column shows the MCP server endpoint you can call for testing or within a client app.

## Optional: Configure policies

Azure API Management uses policies to set rules for your endpoints, such as rate limiting or semantic caching. Policies are defined in XML.

Here’s how to set a policy to rate limit your MCP Server:

1. In the portal, under APIs, select **MCP Servers**.

2. Select the MCP server you created.

3. In the left menu, under MCP, select **Policies**.

4. In the policy editor, add or modify policies for the MCP server’s tools. Policies are written in XML. For example, you can add a policy to limit calls to the MCP server’s tools to 5 calls per 30 seconds per client IP. Here’s the XML that enforces this:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Here’s a screenshot of the policy editor:

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Try it out

Let’s verify that our MCP Server is working properly.

We’ll use Visual Studio Code with GitHub Copilot in Agent mode. We will add the MCP server to a *mcp.json* file. This allows Visual Studio Code to act as a client with agentic capabilities, letting end users type prompts and interact with the server.

Here’s how to add the MCP server in Visual Studio Code:

1. Use the MCP: **Add Server** command from the Command Palette.

2. When prompted, select the server type: **HTTP (HTTP or Server Sent Events)**.

3. Enter the URL of the MCP server in API Management. For example:  
   **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (for SSE endpoint) or  
   **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (for MCP endpoint).  
   Note the difference between transports is `/sse` or `/mcp`.

4. Enter a server ID of your choice. This is not critical but helps you remember this server instance.

5. Choose whether to save the configuration to your workspace settings or user settings.

  - **Workspace settings** - The server configuration is saved in a .vscode/mcp.json file available only in the current workspace.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    If you choose streaming HTTP as the transport, it looks slightly different:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **User settings** - The server configuration is added to your global *settings.json* file and is available in all workspaces. The configuration looks like this:

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

6. You also need to add a header to authenticate properly with Azure API Management. It uses a header called **Ocp-Apim-Subscription-Key**.

    - Here’s how to add it in settings:

    ![Adding header for authentication](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png)  
    This will prompt you to enter your API key, which you can find in the Azure Portal for your Azure API Management instance.

    - To add it to *mcp.json* instead, add it like this:

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

### Use Agent mode

Now that you’re set up in either the settings or *.vscode/mcp.json*, let’s try it out.

There should be a Tools icon like this, listing the exposed tools from your server:

![Tools from the server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Click the tools icon to see a list of tools:

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

2. Enter a prompt in the chat to invoke a tool. For example, if you selected a tool to get order information, you can ask the agent about an order. Here’s a sample prompt:

    ```text
    get information from order 2
    ```

    You’ll see a tools icon asking you to confirm calling the tool. Select to continue running the tool, and you should see output like this:

    ![Result from prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **What you see depends on the tools you set up, but the idea is that you get a textual response like this.**

## References

Here’s where you can learn more:

- [Tutorial on Azure API Management and MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python sample: Secure remote MCP servers using Azure API Management (experimental)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)
- [MCP client authorization lab](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)
- [Use the Azure API Management extension for VS Code to import and manage APIs](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)
- [Register and discover remote MCP servers in Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) — A great repo showcasing many AI capabilities with Azure API Management
- [AI Gateway workshops](https://azure-samples.github.io/AI-Gateway/) — Contains workshops using Azure Portal, a great way to start exploring AI capabilities.

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.