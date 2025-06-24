<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5384bbb2a92d00d5d7e66274dbe0331d",
  "translation_date": "2025-06-20T18:32:34+00:00",
  "source_file": "04-PracticalImplementation/README.md",
  "language_code": "pa"
}
-->
# Practical Implementation

ਪ੍ਰਯੋਗਾਤਮਕ ਲਾਗੂ ਕਰਨ ਦਾ ਮਤਲਬ ਹੈ ਜਿੱਥੇ Model Context Protocol (MCP) ਦੀ ਤਾਕਤ ਹਕੀਕਤ ਵਿੱਚ ਪਰਗਟ ਹੁੰਦੀ ਹੈ। ਜਦੋਂ ਕਿ MCP ਦੇ ਸਿਧਾਂਤ ਅਤੇ ਢਾਂਚੇ ਨੂੰ ਸਮਝਣਾ ਜਰੂਰੀ ਹੈ, ਅਸਲੀ ਮੁੱਲ ਉਸ ਸਮੇਂ ਉਭਰਦਾ ਹੈ ਜਦੋਂ ਤੁਸੀਂ ਇਹ ਧਾਰਣਾਵਾਂ ਵਰਤ ਕੇ ਅਜਿਹੇ ਹੱਲ ਤਿਆਰ, ਟੈਸਟ ਅਤੇ ਡਿਪਲੋਇ ਕਰਦੇ ਹੋ ਜੋ ਅਸਲੀ ਦੁਨੀਆ ਦੀਆਂ ਸਮੱਸਿਆਵਾਂ ਨੂੰ ਹੱਲ ਕਰਦੇ ਹਨ। ਇਹ ਅਧਿਆਇ ਸਿਧਾਂਤਕ ਗਿਆਨ ਅਤੇ ਹੱਥੋਂ-ਹੱਥ ਵਿਕਾਸ ਦਰਮਿਆਨ ਦਾ ਫਰਕ ਪੂਰਾ ਕਰਦਾ ਹੈ, ਅਤੇ ਤੁਹਾਨੂੰ MCP ਅਧਾਰਿਤ ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ ਜੀਵੰਤ ਬਣਾਉਣ ਦੀ ਪ੍ਰਕਿਰਿਆ ਵਿੱਚ ਮਦਦ ਕਰਦਾ ਹੈ।

ਚਾਹੇ ਤੁਸੀਂ ਬੁੱਧੀਮਾਨ ਸਹਾਇਕਾਂ ਨੂੰ ਵਿਕਸਿਤ ਕਰ ਰਹੇ ਹੋ, ਕਾਰੋਬਾਰੀ ਕਾਰਜ ਪ੍ਰਵਾਹ ਵਿੱਚ AI ਨੂੰ ਜੋੜ ਰਹੇ ਹੋ, ਜਾਂ ਡੇਟਾ ਪ੍ਰੋਸੈਸਿੰਗ ਲਈ ਕਸਟਮ ਟੂਲ ਤਿਆਰ ਕਰ ਰਹੇ ਹੋ, MCP ਇੱਕ ਲਚਕੀਲਾ ਬੁਨਿਆਦ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ। ਇਸ ਦੀ ਭਾਸ਼ਾ-ਅਗਨੋਸਟਿਕ ਡਿਜ਼ਾਇਨ ਅਤੇ ਪ੍ਰਸਿੱਧ ਪ੍ਰੋਗ੍ਰਾਮਿੰਗ ਭਾਸ਼ਾਵਾਂ ਲਈ ਅਧਿਕਾਰਿਕ SDKs ਇਸਨੂੰ ਵਿਸ਼ਾਲ ਡਿਵੈਲਪਰ ਗਰੁੱਪ ਲਈ ਪਹੁੰਚਯੋਗ ਬਣਾਉਂਦੇ ਹਨ। ਇਹ SDKs ਵਰਤ ਕੇ, ਤੁਸੀਂ ਤੇਜ਼ੀ ਨਾਲ ਪ੍ਰੋਟੋਟਾਈਪ ਤਿਆਰ ਕਰ ਸਕਦੇ ਹੋ, ਦੁਹਰਾਉਂ ਕਰ ਸਕਦੇ ਹੋ, ਅਤੇ ਵੱਖ-ਵੱਖ ਪਲੇਟਫਾਰਮਾਂ ਅਤੇ ਵਾਤਾਵਰਣਾਂ ਵਿੱਚ ਆਪਣੇ ਹੱਲਾਂ ਨੂੰ ਵਧਾ ਸਕਦੇ ਹੋ।

ਅਗਲੇ ਭਾਗਾਂ ਵਿੱਚ, ਤੁਸੀਂ MCP ਨੂੰ C#, Java, TypeScript, JavaScript ਅਤੇ Python ਵਿੱਚ ਲਾਗੂ ਕਰਨ ਦੇ ਪ੍ਰਯੋਗਾਤਮਕ ਉਦਾਹਰਣ, ਨਮੂਨਾ ਕੋਡ ਅਤੇ ਡਿਪਲੋਇਮੈਂਟ ਰਣਨੀਤੀਆਂ ਪਾਓਗੇ। ਤੁਸੀਂ ਇਹ ਵੀ ਸਿੱਖੋਗੇ ਕਿ ਕਿਵੇਂ MCP ਸਰਵਰਾਂ ਨੂੰ ਡਿਬੱਗ ਅਤੇ ਟੈਸਟ ਕਰਨਾ ਹੈ, APIs ਦਾ ਪ੍ਰਬੰਧਨ ਕਰਨਾ ਹੈ, ਅਤੇ Azure ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਹੱਲਾਂ ਨੂੰ ਕਲਾਉਡ 'ਤੇ ਡਿਪਲੋਇ ਕਰਨਾ ਹੈ। ਇਹ ਹੱਥ-ਵੱਲ ਦੇ ਸਰੋਤ ਤੁਹਾਡੇ ਸਿੱਖਣ ਦੀ ਗਤੀ ਤੇਜ਼ ਕਰਨ ਅਤੇ ਮਜ਼ਬੂਤ, ਪ੍ਰੋਡਕਸ਼ਨ-ਤਿਆਰ MCP ਐਪਲੀਕੇਸ਼ਨਾਂ ਨੂੰ ਵਿਸ਼ਵਾਸਯੋਗ ਤਰੀਕੇ ਨਾਲ ਬਣਾਉਣ ਵਿੱਚ ਮਦਦ ਲਈ ਬਣਾਏ ਗਏ ਹਨ।

## Overview

ਇਸ ਪਾਠ ਦਾ ਕੇਂਦਰ MCP ਦੀ ਲਾਗੂ ਕਰਨ ਦੇ ਪ੍ਰਯੋਗਾਤਮਕ ਪੱਖਾਂ 'ਤੇ ਹੈ ਜੋ ਕਈ ਪ੍ਰੋਗ੍ਰਾਮਿੰਗ ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਫੈਲਿਆ ਹੋਇਆ ਹੈ। ਅਸੀਂ ਵੇਖਾਂਗੇ ਕਿ ਕਿਵੇਂ MCP SDKs ਨੂੰ C#, Java, TypeScript, JavaScript ਅਤੇ Python ਵਿੱਚ ਵਰਤ ਕੇ ਮਜ਼ਬੂਤ ਐਪਲੀਕੇਸ਼ਨ ਬਣਾਈਆਂ ਜਾ ਸਕਦੀਆਂ ਹਨ, MCP ਸਰਵਰਾਂ ਨੂੰ ਡਿਬੱਗ ਅਤੇ ਟੈਸਟ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ, ਅਤੇ ਦੁਹਰਾਉਣਯੋਗ ਸਰੋਤ, ਪ੍ਰਾਂਪਟ ਅਤੇ ਟੂਲ ਤਿਆਰ ਕੀਤੇ ਜਾ ਸਕਦੇ ਹਨ।

## Learning Objectives

ਇਸ ਪਾਠ ਦੇ ਅੰਤ ਤੱਕ, ਤੁਸੀਂ ਸਮਰੱਥ ਹੋਵੋਗੇ:

- ਵੱਖ-ਵੱਖ ਪ੍ਰੋਗ੍ਰਾਮਿੰਗ ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਅਧਿਕਾਰਿਕ SDKs ਦੀ ਵਰਤੋਂ ਕਰਕੇ MCP ਹੱਲ ਲਾਗੂ ਕਰਨਾ  
- MCP ਸਰਵਰਾਂ ਨੂੰ ਸੁਚੱਜੀ ਤਰ੍ਹਾਂ ਡਿਬੱਗ ਅਤੇ ਟੈਸਟ ਕਰਨਾ  
- ਸਰਵਰ ਫੀਚਰ (Resources, Prompts, ਅਤੇ Tools) ਬਣਾਉਣਾ ਅਤੇ ਵਰਤਣਾ  
- ਜਟਿਲ ਕਾਰਜਾਂ ਲਈ ਪ੍ਰਭਾਵਸ਼ਾਲੀ MCP ਵਰਕਫਲੋ ਡਿਜ਼ਾਇਨ ਕਰਨਾ  
- ਕਾਰਗੁਜ਼ਾਰੀ ਅਤੇ ਭਰੋਸੇਯੋਗਤਾ ਲਈ MCP ਲਾਗੂ ਕਰਨ ਦੀਆਂ ਪ੍ਰਕਿਰਿਆਵਾਂ ਨੂੰ ਸੁਧਾਰਨਾ  

## Official SDK Resources

Model Context Protocol ਵੱਖ-ਵੱਖ ਭਾਸ਼ਾਵਾਂ ਲਈ ਅਧਿਕਾਰਿਕ SDKs ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)  
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk)  
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)  
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)  
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)  

## Working with MCP SDKs

ਇਸ ਭਾਗ ਵਿੱਚ MCP ਨੂੰ ਕਈ ਪ੍ਰੋਗ੍ਰਾਮਿੰਗ ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ ਲਾਗੂ ਕਰਨ ਦੇ ਪ੍ਰਯੋਗਾਤਮਕ ਉਦਾਹਰਣ ਦਿੱਤੇ ਗਏ ਹਨ। ਤੁਸੀਂ `samples` ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ ਭਾਸ਼ਾ ਅਨੁਸਾਰ ਸਜਾਇਆ ਗਿਆ ਨਮੂਨਾ ਕੋਡ ਲੱਭ ਸਕਦੇ ਹੋ।

### Available Samples

ਇਸ ਰਿਪੋਜ਼ਟਰੀ ਵਿੱਚ ਹੇਠ ਲਿਖੀਆਂ ਭਾਸ਼ਾਵਾਂ ਵਿੱਚ [ਨਮੂਨਾ ਲਾਗੂ ਕਰਨ ਵਾਲੇ ਕੋਡ](../../../04-PracticalImplementation/samples) ਸ਼ਾਮਲ ਹਨ:

- [C#](./samples/csharp/README.md)  
- [Java](./samples/java/containerapp/README.md)  
- [TypeScript](./samples/typescript/README.md)  
- [JavaScript](./samples/javascript/README.md)  
- [Python](./samples/python/README.md)  

ਹਰ ਨਮੂਨਾ ਉਸ ਭਾਸ਼ਾ ਅਤੇ ਪਰਿਵਾਰ ਲਈ MCP ਦੇ ਮੁੱਖ ਸਿਧਾਂਤ ਅਤੇ ਲਾਗੂ ਕਰਨ ਦੇ ਪੈਟਰਨ ਦਿਖਾਉਂਦਾ ਹੈ।

## Core Server Features

MCP ਸਰਵਰ ਇਹਨਾਂ ਫੀਚਰਾਂ ਦਾ ਕੋਈ ਵੀ ਸੰਗਮ ਲਾਗੂ ਕਰ ਸਕਦਾ ਹੈ:

### Resources  
Resources ਉਪਭੋਗਤਾ ਜਾਂ AI ਮਾਡਲ ਲਈ ਸੰਦਰਭ ਅਤੇ ਡੇਟਾ ਮੁਹੱਈਆ ਕਰਵਾਉਂਦੇ ਹਨ:  
- ਦਸਤਾਵੇਜ਼ ਸੰਗ੍ਰਹਿ  
- ਗਿਆਨ ਅਧਾਰ  
- ਸੰਰਚਿਤ ਡੇਟਾ ਸਰੋਤ  
- ਫਾਇਲ ਸਿਸਟਮ  

### Prompts  
Prompts ਉਪਭੋਗਤਾਵਾਂ ਲਈ ਟੈਂਪਲੇਟ ਕੀਤੇ ਸੁਨੇਹੇ ਅਤੇ ਵਰਕਫਲੋ ਹੁੰਦੇ ਹਨ:  
- ਪਹਿਲਾਂ ਤਿਆਰ ਕੀਤੇ ਗਏ ਗੱਲਬਾਤ ਦੇ ਟੈਂਪਲੇਟ  
- ਮਦਦਗਾਰ ਇੰਟਰੈਕਸ਼ਨ ਪੈਟਰਨ  
- ਵਿਸ਼ੇਸ਼ਕਰਿਤ ਸੰਵਾਦ ਰਚਨਾ  

### Tools  
Tools AI ਮਾਡਲ ਲਈ ਕਾਰਜ ਕਰਨ ਵਾਲੇ ਫੰਕਸ਼ਨ ਹਨ:  
- ਡੇਟਾ ਪ੍ਰੋਸੈਸਿੰਗ ਸਹੂਲਤਾਂ  
- ਬਾਹਰੀ API ਇੰਟੀਗ੍ਰੇਸ਼ਨ  
- ਗਣਨਾਤਮਕ ਯੋਗਤਾਵਾਂ  
- ਖੋਜ ਕਾਰਜਸ਼ੀਲਤਾ  

## Sample Implementations: C#

ਅਧਿਕਾਰਿਕ C# SDK ਰਿਪੋਜ਼ਟਰੀ ਵਿੱਚ MCP ਦੇ ਵੱਖ-ਵੱਖ ਪਹਲੂਆਂ ਨੂੰ ਦਰਸਾਉਂਦੇ ਕਈ ਨਮੂਨਾ ਲਾਗੂ ਕਰਨ ਵਾਲੇ ਕੋਡ ਹਨ:

- **Basic MCP Client**: MCP ਕਲਾਇੰਟ ਬਣਾਉਣ ਅਤੇ ਟੂਲ ਕਾਲ ਕਰਨ ਦੀ ਸਧਾਰਣ ਉਦਾਹਰਣ  
- **Basic MCP Server**: ਬੁਨਿਆਦੀ ਟੂਲ ਰਜਿਸਟਰੇਸ਼ਨ ਨਾਲ ਨਿਊਨਤਮ ਸਰਵਰ ਲਾਗੂ ਕਰਨ ਵਾਲਾ  
- **Advanced MCP Server**: ਪੂਰਨ ਫੀਚਰਾਂ ਵਾਲਾ ਸਰਵਰ ਜਿਸ ਵਿੱਚ ਟੂਲ ਰਜਿਸਟਰੇਸ਼ਨ, ਪ੍ਰਮਾਣਿਕਤਾ ਅਤੇ ਗਲਤੀ ਸੰਭਾਲ ਸ਼ਾਮਲ ਹੈ  
- **ASP.NET Integration**: ASP.NET Core ਨਾਲ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਦੇ ਉਦਾਹਰਣ  
- **Tool Implementation Patterns**: ਵੱਖ-ਵੱਖ ਜਟਿਲਤਾ ਵਾਲੇ ਟੂਲ ਲਾਗੂ ਕਰਨ ਦੇ ਪੈਟਰਨ  

MCP C# SDK ਪ੍ਰੀਵਿਊ ਵਿੱਚ ਹੈ ਅਤੇ APIs ਵਿੱਚ ਬਦਲਾਅ ਹੋ ਸਕਦੇ ਹਨ। ਜਿਵੇਂ SDK ਵਿਕਸਤ ਹੁੰਦਾ ਰਹੇਗਾ, ਅਸੀਂ ਇਸ ਬਲੌਗ ਨੂੰ ਅਪਡੇਟ ਕਰਦੇ ਰਹਾਂਗੇ।

### Key Features  
- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)  
- ਆਪਣਾ [ਪਹਿਲਾ MCP ਸਰਵਰ ਬਣਾਉਣਾ](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/)  

ਪੂਰੇ C# ਲਾਗੂ ਕਰਨ ਦੇ ਨਮੂਨੇ ਲਈ, [ਅਧਿਕਾਰਿਕ C# SDK ਨਮੂਨਾ ਰਿਪੋਜ਼ਟਰੀ](https://github.com/modelcontextprotocol/csharp-sdk) 'ਤੇ ਜਾਓ।

## Sample implementation: Java Implementation

Java SDK MCP ਨੂੰ ਲਾਗੂ ਕਰਨ ਲਈ ਮਜ਼ਬੂਤ ਵਿਕਲਪ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ ਜੋ ਐਂਟਰਪ੍ਰਾਈਜ਼-ਗ੍ਰੇਡ ਫੀਚਰਾਂ ਨਾਲ ਭਰਪੂਰ ਹੈ।

### Key Features

- Spring Framework ਇੰਟੀਗ੍ਰੇਸ਼ਨ  
- ਮਜ਼ਬੂਤ ਟਾਈਪ ਸੁਰੱਖਿਆ  
- ਰੀਐਕਟਿਵ ਪ੍ਰੋਗ੍ਰਾਮਿੰਗ ਸਹਾਇਤਾ  
- ਵਿਸ਼ਤ੍ਰਿਤ ਗਲਤੀ ਸੰਭਾਲ  

ਪੂਰੇ Java ਲਾਗੂ ਕਰਨ ਦੇ ਨਮੂਨੇ ਲਈ, ਸੈਂਪਲ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ [Java sample](samples/java/containerapp/README.md) ਵੇਖੋ।

## Sample implementation: JavaScript Implementation

JavaScript SDK MCP ਲਾਗੂ ਕਰਨ ਲਈ ਹਲਕਾ-ਫੁਲਕਾ ਅਤੇ ਲਚਕੀਲਾ ਤਰੀਕਾ ਦਿੰਦਾ ਹੈ।

### Key Features

- Node.js ਅਤੇ ਬ੍ਰਾਉਜ਼ਰ ਸਹਾਇਤਾ  
- ਪ੍ਰੋਮਿਸ-ਅਧਾਰਿਤ API  
- Express ਅਤੇ ਹੋਰ ਫਰੇਮਵਰਕਸ ਨਾਲ ਆਸਾਨ ਇੰਟੀਗ੍ਰੇਸ਼ਨ  
- ਸਟ੍ਰੀਮਿੰਗ ਲਈ WebSocket ਸਹਾਇਤਾ  

ਪੂਰੇ JavaScript ਲਾਗੂ ਕਰਨ ਦੇ ਨਮੂਨੇ ਲਈ, ਸੈਂਪਲ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ [JavaScript sample](samples/javascript/README.md) ਵੇਖੋ।

## Sample implementation: Python Implementation

Python SDK MCP ਲਾਗੂ ਕਰਨ ਲਈ ਇੱਕ Pythonic ਅਪ੍ਰੋਚ ਦਿੰਦਾ ਹੈ ਜਿਸ ਵਿੱਚ ਬਹੁਤ ਵਧੀਆ ML ਫਰੇਮਵਰਕ ਇੰਟੀਗ੍ਰੇਸ਼ਨ ਹਨ।

### Key Features

- asyncio ਨਾਲ async/await ਸਹਾਇਤਾ  
- Flask ਅਤੇ FastAPI ਇੰਟੀਗ੍ਰੇਸ਼ਨ  
- ਸਧਾਰਣ ਟੂਲ ਰਜਿਸਟਰੇਸ਼ਨ  
- ਪ੍ਰਸਿੱਧ ML ਲਾਇਬ੍ਰੇਰੀਜ਼ ਨਾਲ ਮੂਲ ਇੰਟੀਗ੍ਰੇਸ਼ਨ  

ਪੂਰੇ Python ਲਾਗੂ ਕਰਨ ਦੇ ਨਮੂਨੇ ਲਈ, ਸੈਂਪਲ ਡਾਇਰੈਕਟਰੀ ਵਿੱਚ [Python sample](samples/python/README.md) ਵੇਖੋ।

## API management

Azure API Management MCP ਸਰਵਰਾਂ ਨੂੰ ਸੁਰੱਖਿਅਤ ਕਰਨ ਦਾ ਵਧੀਆ ਜਵਾਬ ਹੈ। ਖਿਆਲ ਇਹ ਹੈ ਕਿ ਤੁਸੀਂ ਆਪਣੇ MCP ਸਰਵਰ ਦੇ ਸਾਹਮਣੇ ਇੱਕ Azure API Management ਇੰਸਟੈਂਸ ਰੱਖੋ ਅਤੇ ਇਸਨੂੰ ਉਹ ਫੀਚਰ ਸੰਭਾਲਣ ਦਿਓ ਜੋ ਤੁਹਾਨੂੰ ਚਾਹੀਦੇ ਹਨ ਜਿਵੇਂ ਕਿ:

- ਰੇਟ ਲਿਮਿਟਿੰਗ  
- ਟੋਕਨ ਪ੍ਰਬੰਧਨ  
- ਮਾਨੀਟਰਿੰਗ  
- ਲੋਡ ਬੈਲੈਂਸਿੰਗ  
- ਸੁਰੱਖਿਆ  

### Azure Sample

ਇੱਥੇ ਇੱਕ Azure ਨਮੂਨਾ ਹੈ ਜੋ ਇਹੀ ਕਰਦਾ ਹੈ, ਜਿਵੇਂ ਕਿ MCP ਸਰਵਰ ਬਣਾਉਣਾ ਅਤੇ ਉਸਨੂੰ Azure API Management ਨਾਲ ਸੁਰੱਖਿਅਤ ਕਰਨਾ: [Azure Sample](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)।

ਹੇਠਾਂ ਦਿੱਤੀ ਤਸਵੀਰ ਵਿੱਚ ਦੇਖੋ ਕਿ ਪ੍ਰਮਾਣਿਕਤਾ ਦਾ ਪ੍ਰਕਿਰਿਆ ਕਿਵੇਂ ਹੁੰਦੀ ਹੈ:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)  

ਉਪਰੋਕਤ ਤਸਵੀਰ ਵਿੱਚ ਇਹ ਹੁੰਦਾ ਹੈ:

- Microsoft Entra ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਪ੍ਰਮਾਣਿਕਤਾ/ਪ੍ਰਮਾਣਿਕਰਨ ਹੁੰਦਾ ਹੈ।  
- Azure API Management ਗੇਟਵੇ ਵਜੋਂ ਕੰਮ ਕਰਦਾ ਹੈ ਅਤੇ ਟ੍ਰੈਫਿਕ ਨੂੰ ਦਿਸ਼ਾ ਦੇਣ ਅਤੇ ਪ੍ਰਬੰਧਨ ਲਈ ਨੀਤੀਆਂ ਵਰਤਦਾ ਹੈ।  
- Azure Monitor ਸਾਰੇ ਰਿਕਵੇਸਟਾਂ ਨੂੰ ਅਗਲੇ ਵਿਸ਼ਲੇਸ਼ਣ ਲਈ ਲੌਗ ਕਰਦਾ ਹੈ।  

#### Authorization flow

ਆਓ ਪ੍ਰਮਾਣਿਕਤਾ ਪ੍ਰਕਿਰਿਆ ਨੂੰ ਹੋਰ ਵਿਸਥਾਰ ਨਾਲ ਦੇਖੀਏ:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP authorization specification

[ਹੋਰ ਜਾਣਕਾਰੀ ਲਈ MCP Authorization specification](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization#2-10-third-party-authorization-flow) ਵੇਖੋ।

## Deploy Remote MCP Server to Azure

ਚਲੋ ਵੇਖੀਏ ਕਿ ਅਸੀਂ ਪਹਿਲਾਂ ਦੱਸੇ ਨਮੂਨੇ ਨੂੰ ਕਿਵੇਂ ਡਿਪਲੋਇ ਕਰ ਸਕਦੇ ਹਾਂ:

1. ਰਿਪੋਜ਼ਟਰੀ ਕਲੋਨ ਕਰੋ

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

2. `Microsoft.App` ਨੂੰ ਰਜਿਸਟਰ ਕਰੋ:

    `` resource provider.
    * If you are using Azure CLI, run `az provider register --namespace Microsoft.App --wait`.
    * If you are using Azure PowerShell, run `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Then run `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState`  
    ਕੁਝ ਸਮਾਂ ਬਾਅਦ ਚੈੱਕ ਕਰੋ ਕਿ ਰਜਿਸਟ੍ਰੇਸ਼ਨ ਪੂਰਾ ਹੋ ਗਿਆ ਹੈ ਜਾਂ ਨਹੀਂ।  

3. ਇਹ [azd](https://aka.ms/azd) ਕਮਾਂਡ ਚਲਾਓ ਤਾਂ ਜੋ API Management ਸੇਵਾ, ਫੰਕਸ਼ਨ ਐਪ (ਕੋਡ ਸਮੇਤ) ਅਤੇ ਹੋਰ ਸਾਰੇ ਲੋੜੀਂਦੇ Azure ਸਰੋਤ ਪ੍ਰੋਵਾਈਜ਼ਨ ਹੋ ਜਾਣ:

    ```shell
    azd up
    ```

    ਇਹ ਕਮਾਂਡ Azure 'ਤੇ ਸਾਰੇ ਕਲਾਉਡ ਸਰੋਤ ਡਿਪਲੋਇ ਕਰ ਦੇਵੇਗੀ।

### Testing your server with MCP Inspector

1. ਇੱਕ **ਨਵੀਂ ਟਰਮੀਨਲ ਵਿੰਡੋ** ਵਿੱਚ MCP Inspector ਇੰਸਟਾਲ ਅਤੇ ਚਲਾਓ

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    ਤੁਹਾਨੂੰ ਕੁਝ ਇਸ ਤਰ੍ਹਾਂ ਦਾ ਇੰਟਰਫੇਸ ਵੇਖਣ ਨੂੰ ਮਿਲੇਗਾ:

    ![Connect to Node inspector](../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.pa.png)  

2. CTRL ਕਲਿੱਕ ਕਰਕੇ MCP Inspector ਵੈੱਬ ਐਪ ਨੂੰ URL ਤੋਂ ਲੋਡ ਕਰੋ (ਜਿਵੇਂ ਕਿ http://127.0.0.1:6274/#resources)  
3. ਟ੍ਰਾਂਸਪੋਰਟ ਕਿਸਮ `SSE`
1. Set the URL to your running API Management SSE endpoint displayed after `azd up` ਤੇ ਸੈੱਟ ਕਰੋ ਅਤੇ **Connect** ਕਰੋ:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

5. **List Tools** ਤੇ ਕਲਿੱਕ ਕਰੋ। ਕਿਸੇ ਟੂਲ ਨੂੰ ਚੁਣੋ ਅਤੇ **Run Tool** ਕਰੋ।  

ਜੇ ਸਾਰੇ ਕਦਮ ਸਹੀ ਤਰ੍ਹਾਂ ਹੋਏ, ਤਾਂ ਹੁਣ ਤੁਸੀਂ MCP ਸਰਵਰ ਨਾਲ ਜੁੜੇ ਹੋਵੋਗੇ ਅਤੇ ਟੂਲ ਕਾਲ ਕਰਨ ਵਿੱਚ ਸਫਲ ਰਹੋਗੇ।

## MCP servers for Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): ਇਹ ਰਿਪੋਜ਼ਟਰੀਜ਼ ਦਾ ਸੈੱਟ MCP ਸਰਵਰਾਂ ਨੂੰ Azure Functions ਨਾਲ Python, C# .NET ਜਾਂ Node/TypeScript ਵਰਤ ਕੇ ਬਣਾਉਣ ਅਤੇ ਡਿਪਲੋਇ ਕਰਨ ਲਈ ਤਿਆਰ ਕੀਤਾ ਗਿਆ ਹੈ।

ਨਮੂਨੇ ਇੱਕ ਪੂਰਾ ਹੱਲ ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਨ ਜੋ ਡਿਵੈਲਪਰਾਂ ਨੂੰ:

- ਸਥਾਨਕ ਤੌਰ 'ਤੇ ਬਣਾਉਣ ਅਤੇ ਚਲਾਉਣ: MCP ਸਰਵਰ ਨੂੰ ਲੋਕਲ ਮਸ਼ੀਨ 'ਤੇ ਵਿਕਸਿਤ ਅਤੇ ਡਿਬੱਗ ਕਰੋ  
- Azure 'ਤੇ ਡਿਪਲੋਇ ਕਰੋ: ਇੱਕ ਸਧਾਰਣ azd up ਕਮਾਂਡ ਨਾਲ ਕਲਾਉਡ 'ਤੇ ਆਸਾਨੀ ਨਾਲ ਡਿਪਲੋਇ ਕਰੋ  
- ਕਲਾਇੰਟਾਂ ਤੋਂ ਜੁੜੋ: ਵੱਖ-ਵੱਖ ਕਲਾਇੰਟਾਂ, ਜਿਵੇਂ VS Code ਦੇ Copilot ਏਜੰਟ ਮੋਡ ਅਤੇ MCP Inspector ਟੂਲ ਤੋਂ MCP ਸਰਵਰ ਨਾਲ ਜੁੜੋ  

### Key Features:

- ਡਿਜ਼ਾਇਨ ਦੁਆਰਾ ਸੁਰੱਖਿਆ: MCP ਸਰਵਰ ਕੁੰਜੀਆਂ ਅਤੇ HTTPS ਦੀ ਵਰਤੋਂ ਨਾਲ ਸੁਰੱਖਿਅਤ ਹੈ  
- ਪ੍ਰਮਾਣਿਕਤਾ ਵਿਕਲਪ: ਇੰਬਿਲਟ ਆਥ ਅਤੇ/ਜਾਂ API Management ਨਾਲ OAuth ਦਾ ਸਮਰਥਨ  
- ਨੈੱਟਵਰਕ ਅਲੱਗਾਵ: Azure Virtual Networks (VNET) ਦੀ ਵਰਤੋਂ ਨਾਲ ਨੈੱਟਵਰਕ ਅਲੱਗਾਵ ਦੀ ਆਗਿਆ  
- ਸਰਵਰਲੈੱਸ ਆਰਕੀਟੈਕਚਰ: ਮਾਪਯੋਗ, ਘਟਨਾ-ਚਾਲਿਤ ਕਾਰਜ ਲਈ Azure Functions ਦਾ ਲਾਭ  
- ਸਥਾਨਕ ਵਿਕਾਸ: ਵਿਸ਼ਤ੍ਰਿਤ ਸਥਾਨਕ ਵਿਕਾਸ ਅਤੇ ਡਿਬੱਗਿੰਗ ਸਹਾਇਤਾ  
- ਸਧਾਰਣ ਡਿਪਲੋਇਮੈਂਟ: Azure ਲਈ ਸੁਚੱਜਾ ਡਿਪਲੋਇਮੈਂਟ ਪ੍ਰਕਿਰਿਆ  

ਰਿਪੋਜ਼ਟਰੀ ਵਿੱਚ ਸਾਰੇ ਜ਼ਰੂਰੀ ਕਨਫਿਗਰੇਸ਼ਨ ਫਾਈਲਾਂ, ਸਰੋਤ ਕੋਡ, ਅਤੇ ਇੰਫ੍ਰਾਸਟਰੱਕਚਰ ਪਰਿਭਾਸ਼ਾਵਾਂ ਹਨ ਜੋ ਤੁਹਾਨੂੰ ਪ੍ਰੋਡਕਸ਼ਨ-ਤਿਆਰ MCP ਸਰਵਰ

**ਅਸਵੀਕਾਰੋਪਣ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ ਏਆਈ ਅਨੁਵਾਦ ਸੇਵਾ [Co-op Translator](https://github.com/Azure/co-op-translator) ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀਤਾ ਲਈ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸਹੀਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਆਪਣੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਹੀ ਅਧਿਕਾਰਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੀ ਵਰਤੋਂ ਨਾਲ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤਫਹਿਮੀਆਂ ਜਾਂ ਭ੍ਰਮਾਂ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।