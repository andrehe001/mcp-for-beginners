<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:28:55+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "pa"
}
-->
# Chainlit ਅਤੇ Microsoft Learn Docs MCP ਨਾਲ ਅਧਿਐਨ ਯੋਜਨਾ ਜਨਰੇਟਰ

## ਜ਼ਰੂਰੀ ਸ਼ਰਤਾਂ

- Python 3.8 ਜਾਂ ਇਸ ਤੋਂ ਉੱਪਰ
- pip (Python ਪੈਕੇਜ ਮੈਨੇਜਰ)
- Microsoft Learn Docs MCP ਸਰਵਰ ਨਾਲ ਜੁੜਨ ਲਈ ਇੰਟਰਨੈੱਟ ਕਨੈਕਸ਼ਨ

## ਇੰਸਟਾਲੇਸ਼ਨ

1. ਇਸ ਰਿਪੋਜ਼ਿਟਰੀ ਨੂੰ ਕਲੋਨ ਕਰੋ ਜਾਂ ਪ੍ਰੋਜੈਕਟ ਫਾਈਲਾਂ ਡਾਊਨਲੋਡ ਕਰੋ।
2. ਲੋੜੀਂਦੇ ਡਿਪੈਂਡੈਂਸੀਜ਼ ਇੰਸਟਾਲ ਕਰੋ:

   ```bash
   pip install -r requirements.txt
   ```

## ਵਰਤੋਂ

### ਸਿਨਾਰੀਓ 1: ਸਧਾਰਣ ਕਵੈਰੀ Docs MCP ਨੂੰ  
ਇੱਕ ਕਮਾਂਡ-ਲਾਈਨ ਕਲਾਇੰਟ ਜੋ Docs MCP ਸਰਵਰ ਨਾਲ ਜੁੜਦਾ ਹੈ, ਕਵੈਰੀ ਭੇਜਦਾ ਹੈ ਅਤੇ ਨਤੀਜਾ ਪ੍ਰਿੰਟ ਕਰਦਾ ਹੈ।

1. ਸਕ੍ਰਿਪਟ ਚਲਾਓ:  
   ```bash
   python scenario1.py
   ```  
2. ਪ੍ਰਾਂਪਟ 'ਤੇ ਆਪਣਾ ਦਸਤਾਵੇਜ਼ੀ ਸਵਾਲ ਦਿਓ।

### ਸਿਨਾਰੀਓ 2: ਅਧਿਐਨ ਯੋਜਨਾ ਜਨਰੇਟਰ (Chainlit ਵੈੱਬ ਐਪ)  
ਇੱਕ ਵੈੱਬ-ਆਧਾਰਿਤ ਇੰਟਰਫੇਸ (Chainlit ਵਰਤ ਕੇ) ਜੋ ਯੂਜ਼ਰਾਂ ਨੂੰ ਕਿਸੇ ਵੀ ਤਕਨੀਕੀ ਵਿਸ਼ੇ ਲਈ ਹਫ਼ਤੇ-ਦਰ-ਹਫ਼ਤਾ ਨਿੱਜੀ ਅਧਿਐਨ ਯੋਜਨਾ ਬਣਾਉਣ ਦੀ ਆਗਿਆ ਦਿੰਦਾ ਹੈ।

1. Chainlit ਐਪ ਸ਼ੁਰੂ ਕਰੋ:  
   ```bash
   chainlit run scenario2.py
   ```  
2. ਆਪਣੇ ਟਰਮੀਨਲ ਵਿੱਚ ਦਿੱਤਾ ਹੋਇਆ ਲੋਕਲ URL (ਜਿਵੇਂ http://localhost:8000) ਆਪਣੇ ਬ੍ਰਾਊਜ਼ਰ ਵਿੱਚ ਖੋਲ੍ਹੋ।  
3. ਚੈਟ ਵਿੰਡੋ ਵਿੱਚ ਆਪਣਾ ਅਧਿਐਨ ਵਿਸ਼ਾ ਅਤੇ ਅਧਿਐਨ ਕਰਨ ਵਾਲੇ ਹਫ਼ਤਿਆਂ ਦੀ ਗਿਣਤੀ ਦਿਓ (ਜਿਵੇਂ "AI-900 certification, 8 weeks")।  
4. ਐਪ ਤੁਹਾਨੂੰ ਹਫ਼ਤੇ-ਦਰ-ਹਫ਼ਤੇ ਅਧਿਐਨ ਯੋਜਨਾ ਦੇਵੇਗਾ, ਜਿਸ ਵਿੱਚ ਸੰਬੰਧਿਤ Microsoft Learn ਦਸਤਾਵੇਜ਼ੀ ਲਿੰਕ ਸ਼ਾਮਲ ਹੋਣਗੇ।

**ਲੋੜੀਂਦੇ Environment Variables:**  

Scenario 2 (Chainlit ਵੈੱਬ ਐਪ Azure OpenAI ਨਾਲ) ਵਰਤਣ ਲਈ, ਤੁਹਾਨੂੰ `.env` file in the `python` ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਹੇਠ ਲਿਖੇ Environment Variables ਸੈੱਟ ਕਰਨੇ ਪੈਣਗੇ:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

ਐਪ ਚਲਾਉਣ ਤੋਂ ਪਹਿਲਾਂ ਇਹ ਵੈਲਯੂਜ਼ ਆਪਣੇ Azure OpenAI ਰਿਸੋਰਸ ਵੇਰਵਿਆਂ ਨਾਲ ਭਰੋ।

> **Tip:** ਤੁਸੀਂ [Azure AI Foundry](https://ai.azure.com/) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਆਪਣੇ ਮਾਡਲ ਆਸਾਨੀ ਨਾਲ ਡਿਪਲੋਏ ਕਰ ਸਕਦੇ ਹੋ।

### ਸਿਨਾਰੀਓ 3: VS Code ਵਿੱਚ MCP ਸਰਵਰ ਨਾਲ ਇੰ-ਐਡੀਟਰ Docs

ਦਸਤਾਵੇਜ਼ੀ ਖੋਜਣ ਲਈ ਬ੍ਰਾਊਜ਼ਰ ਟੈਬ ਬਦਲਣ ਦੀ ਥਾਂ, ਤੁਸੀਂ Microsoft Learn Docs ਨੂੰ ਸਿੱਧਾ VS Code ਵਿੱਚ MCP ਸਰਵਰ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਲਿਆ ਸਕਦੇ ਹੋ। ਇਸ ਨਾਲ ਤੁਸੀਂ:

- VS Code ਦੇ ਅੰਦਰ ਹੀ ਦਸਤਾਵੇਜ਼ੀ ਖੋਜ ਅਤੇ ਪੜ੍ਹ ਸਕਦੇ ਹੋ ਬਿਨਾਂ ਕੋਡਿੰਗ ਵਾਤਾਵਰਨ ਛੱਡੇ।
- ਦਸਤਾਵੇਜ਼ੀ ਦੇ ਹਵਾਲੇ ਅਤੇ ਲਿੰਕ ਆਪਣੇ README ਜਾਂ ਕੋਰਸ ਫਾਈਲਾਂ ਵਿੱਚ ਸਿੱਧਾ ਸ਼ਾਮਲ ਕਰ ਸਕਦੇ ਹੋ।
- GitHub Copilot ਅਤੇ MCP ਨੂੰ ਇਕੱਠੇ ਵਰਤ ਕੇ ਬਿਨਾਂ ਰੁਕਾਵਟ ਵਾਲਾ AI-ਚਲਿਤ ਦਸਤਾਵੇਜ਼ੀ ਕੰਮ ਕਰ ਸਕਦੇ ਹੋ।

**ਉਦਾਹਰਣ ਵਰਤੋਂ ਕੇਸ:**  
- README ਵਿੱਚ ਤੁਰੰਤ ਹਵਾਲੇ ਜੋੜੋ ਜਦੋਂ ਤੁਸੀਂ ਕੋਰਸ ਜਾਂ ਪ੍ਰੋਜੈਕਟ ਦਸਤਾਵੇਜ਼ੀ ਲਿਖ ਰਹੇ ਹੋ।  
- ਕੋਡ ਬਣਾਉਣ ਲਈ Copilot ਦੀ ਵਰਤੋਂ ਕਰੋ ਅਤੇ MCP ਨਾਲ ਸੰਬੰਧਿਤ ਦਸਤਾਵੇਜ਼ੀ ਤੁਰੰਤ ਲੱਭੋ ਅਤੇ ਹਵਾਲਾ ਦਿਓ।  
- ਆਪਣੇ ਐਡੀਟਰ ਵਿੱਚ ਧਿਆਨ ਕੇਂਦਰਿਤ ਰੱਖੋ ਅਤੇ ਉਤਪਾਦਕਤਾ ਵਧਾਓ।

> [!IMPORTANT]  
> ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਹਾਡੇ ਕੋਲ ਇੱਕ ਵੈਧ [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

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
- `Cloud architecture, 9 weeks`] ਫਾਈਲ ਹੈ।

ਇਹ ਉਦਾਹਰਣ ਐਪ ਦੀ ਲਚਕੀਲਾਪਣ ਅਤੇ ਵੱਖ-ਵੱਖ ਸਿੱਖਣ ਦੇ ਮਕਸਦਾਂ ਅਤੇ ਸਮੇਂ ਦੇ ਅਧਾਰ 'ਤੇ ਵਰਤੋਂ ਨੂੰ ਦਰਸਾਉਂਦੇ ਹਨ।

## ਸੰਦਰਭ

- [Chainlit ਦਸਤਾਵੇਜ਼ੀ](https://docs.chainlit.io/)
- [MCP ਦਸਤਾਵੇਜ਼ੀ](https://github.com/MicrosoftDocs/mcp)

**ਅਸਵੀਕਾਰੋਪਣੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ AI ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਅਤ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਰੱਖੋ ਕਿ ਆਟੋਮੇਟਿਕ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਣਸਹੀਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਜਰੂਰੀ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਨਾਲ ਪੈਦਾਂ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।