<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "4319d291c9d124ecafea52b3d04bfa0e",
  "translation_date": "2025-06-23T11:06:04+00:00",
  "source_file": "09-CaseStudy/docs-mcp/README.md",
  "language_code": "pa"
}
-->
> ਸਕਰੀਨਸ਼ਾਟਸ ਅਤੇ ਕਦਮ-ਦਰ-ਕਦਮ ਮਾਰਗਦਰਸ਼ਨ ਲਈ, [`README.md`](./solution/scenario3/README.md) ਵੇਖੋ।

![Scenario 3 Overview](../../../../translated_images/step4-prompt-chat.12187bb001605efc5077992b621f0fcd1df12023c5dce0464f8eb8f3d595218f.pa.png)

ਇਹ ਤਰੀਕਾ ਉਨ੍ਹਾਂ ਲਈ ਬਹੁਤ ਵਧੀਆ ਹੈ ਜੋ ਤਕਨੀਕੀ ਕੋਰਸ ਬਣਾਉਂਦੇ ਹਨ, ਦਸਤਾਵੇਜ਼ ਲਿਖਦੇ ਹਨ, ਜਾਂ ਅਕਸਰ ਹਵਾਲੇ ਦੀ ਲੋੜ ਨਾਲ ਕੋਡ ਵਿਕਸਿਤ ਕਰ ਰਹੇ ਹਨ।

## ਮੁੱਖ ਗੱਲਾਂ

ਦਸਤਾਵੇਜ਼ ਨੂੰ ਸਿੱਧਾ ਆਪਣੇ ਟੂਲਾਂ ਵਿੱਚ ਜੋੜਨਾ ਸਿਰਫ਼ ਸੁਵਿਧਾ ਨਹੀਂ—ਇਹ ਉਤਪਾਦਕਤਾ ਲਈ ਖੇਡ ਬਦਲਣ ਵਾਲਾ ਹੈ। ਆਪਣੇ ਕਲਾਇੰਟ ਤੋਂ Microsoft Learn Docs MCP ਸਰਵਰ ਨਾਲ ਜੁੜ ਕੇ, ਤੁਸੀਂ:

- ਆਪਣੇ ਕੋਡ ਅਤੇ ਦਸਤਾਵੇਜ਼ਾਂ ਵਿਚਕਾਰ ਸੰਦਰਭ ਬਦਲਣ ਨੂੰ ਖਤਮ ਕਰ ਸਕਦੇ ਹੋ
- ਅਪ-ਟੂ-ਡੇਟ, ਸੰਦਰਭ-ਜਾਣੂ ਦਸਤਾਵੇਜ਼ਾਂ ਨੂੰ ਤੁਰੰਤ ਪ੍ਰਾਪਤ ਕਰ ਸਕਦੇ ਹੋ
- ਹੋਸ਼ਿਆਰ, ਜ਼ਿਆਦਾ ਇੰਟਰਐਕਟਿਵ ਵਿਕਾਸਕਾਰ ਟੂਲ ਬਣਾ ਸਕਦੇ ਹੋ

ਇਹ ਹੁਨਰ ਤੁਹਾਨੂੰ ਐਸੇ ਹੱਲ ਬਣਾਉਣ ਵਿੱਚ ਮਦਦ ਕਰਨਗੇ ਜੋ ਨਾ ਸਿਰਫ਼ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਹੋਣਗੇ, ਬਲਕਿ ਵਰਤੋਂ ਵਿੱਚ ਵੀ ਮਨਪਸੰਦ ਹੋਣਗੇ।

## ਵਾਧੂ ਸਰੋਤ

ਆਪਣੀ ਸਮਝ ਨੂੰ ਗਹਿਰਾ ਕਰਨ ਲਈ, ਇਹ ਅਧਿਕਾਰਕ ਸਰੋਤ ਵੇਖੋ:

- [Microsoft Learn Docs MCP Server (GitHub)](https://github.com/MicrosoftDocs/mcp)
- [Azure MCP Server ਨਾਲ ਸ਼ੁਰੂਆਤ ਕਰੋ (mcp-python)](https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server/get-started#create-the-python-app)
- [Azure MCP Server ਕੀ ਹੈ?](https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server/)
- [Model Context Protocol (MCP) ਪਰਿਚਯ](https://modelcontextprotocol.io/introduction)
- [MCP Server ਤੋਂ ਪਲੱਗਇਨ ਸ਼ਾਮਲ ਕਰੋ (Python)](https://learn.microsoft.com/en-us/semantic-kernel/concepts/plugins/adding-mcp-plugins)

**ਅਸਵੀਕਾਰੋਪੱਤਰ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਯਤਨ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚਿਤਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਹੀ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਣ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫ਼ਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਨਾਲ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਭ੍ਰਮਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।