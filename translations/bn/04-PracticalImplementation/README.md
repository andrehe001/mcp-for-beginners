<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5384bbb2a92d00d5d7e66274dbe0331d",
  "translation_date": "2025-06-20T18:25:59+00:00",
  "source_file": "04-PracticalImplementation/README.md",
  "language_code": "bn"
}
-->
# Practical Implementation

প্র্যাকটিক্যাল ইমপ্লিমেন্টেশন হল যেখানে Model Context Protocol (MCP)-এর শক্তি স্পষ্ট হয়ে ওঠে। MCP-এর তত্ত্ব ও আর্কিটেকচার বোঝা অবশ্যই গুরুত্বপূর্ণ, তবে প্রকৃত মূল্য তখনই আসে যখন আপনি এই ধারণাগুলো ব্যবহার করে বাস্তব সমস্যার সমাধান করতে সক্ষম হন। এই অধ্যায়টি ধারণাগত জ্ঞানের সাথে হাতে-কলমে উন্নয়নের ফাঁক পূরণ করে, MCP-ভিত্তিক অ্যাপ্লিকেশন তৈরি করার প্রক্রিয়ায় আপনাকে পথপ্রদর্শন করবে।

আপনি যদি বুদ্ধিমান সহকারী তৈরি করেন, ব্যবসায়িক ওয়ার্কফ্লোতে AI সংযুক্ত করেন, অথবা ডেটা প্রসেসিংয়ের জন্য কাস্টম টুল তৈরি করেন, MCP একটি নমনীয় ভিত্তি প্রদান করে। এর ভাষা-নিরপেক্ষ ডিজাইন এবং জনপ্রিয় প্রোগ্রামিং ভাষার জন্য অফিসিয়াল SDK গুলো বিভিন্ন ধরনের ডেভেলপারদের জন্য সহজলভ্য করে তোলে। এই SDK গুলো ব্যবহার করে আপনি দ্রুত প্রোটোটাইপ তৈরি, পুনরাবৃত্তি, এবং বিভিন্ন প্ল্যাটফর্ম ও পরিবেশে আপনার সমাধানগুলি স্কেল করতে পারবেন।

পরবর্তী অংশগুলোতে আপনি প্র্যাকটিক্যাল উদাহরণ, নমুনা কোড, এবং ডিপ্লয়মেন্ট কৌশল পাবেন যা C#, Java, TypeScript, JavaScript, এবং Python-এ MCP কিভাবে ইমপ্লিমেন্ট করবেন তা দেখাবে। এছাড়াও আপনি শিখবেন কিভাবে MCP সার্ভার ডিবাগ ও টেস্ট করবেন, API গুলো ম্যানেজ করবেন, এবং Azure ব্যবহার করে ক্লাউডে সমাধান ডিপ্লয় করবেন। এই হাতে-কলমে সম্পদগুলো আপনার শেখার গতি বাড়াতে এবং আত্মবিশ্বাসের সাথে শক্তিশালী, প্রোডাকশন-রেডি MCP অ্যাপ্লিকেশন তৈরি করতে সাহায্য করবে।

## Overview

এই পাঠে MCP ইমপ্লিমেন্টেশনের প্র্যাকটিক্যাল দিকগুলো বিভিন্ন প্রোগ্রামিং ভাষায় আলোচনা করা হবে। আমরা দেখব কিভাবে C#, Java, TypeScript, JavaScript, এবং Python-এ MCP SDK ব্যবহার করে শক্তিশালী অ্যাপ্লিকেশন তৈরি করবেন, MCP সার্ভার ডিবাগ ও টেস্ট করবেন, এবং পুনঃব্যবহারযোগ্য রিসোর্স, প্রম্পট এবং টুল তৈরি করবেন।

## Learning Objectives

এই পাঠ শেষ হলে আপনি সক্ষম হবেন:
- বিভিন্ন প্রোগ্রামিং ভাষায় অফিসিয়াল SDK ব্যবহার করে MCP সমাধান ইমপ্লিমেন্ট করতে
- MCP সার্ভারগুলো পদ্ধতিগতভাবে ডিবাগ ও টেস্ট করতে
- সার্ভার ফিচার (Resources, Prompts, এবং Tools) তৈরি ও ব্যবহার করতে
- জটিল কাজের জন্য কার্যকর MCP ওয়ার্কফ্লো ডিজাইন করতে
- পারফরম্যান্স এবং নির্ভরযোগ্যতার জন্য MCP ইমপ্লিমেন্টেশন অপ্টিমাইজ করতে

## Official SDK Resources

Model Context Protocol বিভিন্ন ভাষার জন্য অফিসিয়াল SDK প্রদান করে:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) 
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

## Working with MCP SDKs

এই অংশে MCP বিভিন্ন প্রোগ্রামিং ভাষায় ইমপ্লিমেন্ট করার প্র্যাকটিক্যাল উদাহরণ দেওয়া হয়েছে। আপনি `samples` ডিরেক্টরিতে ভাষাভিত্তিক স্যাম্পল কোড পেতে পারেন।

### Available Samples

রিপোজিটরিতে নিম্নলিখিত ভাষায় [স্যাম্পল ইমপ্লিমেন্টেশন](../../../04-PracticalImplementation/samples) অন্তর্ভুক্ত রয়েছে:

- [C#](./samples/csharp/README.md)
- [Java](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

প্রত্যেকটি স্যাম্পল নির্দিষ্ট ভাষা ও ইকোসিস্টেমের জন্য MCP-এর মূল ধারণা এবং ইমপ্লিমেন্টেশন প্যাটার্ন প্রদর্শন করে।

## Core Server Features

MCP সার্ভার নিম্নলিখিত ফিচারগুলোর যেকোনো সংমিশ্রণ ইমপ্লিমেন্ট করতে পারে:

### Resources
Resources ব্যবহারকারী বা AI মডেলের জন্য প্রাসঙ্গিক তথ্য এবং ডেটা প্রদান করে:
- ডকুমেন্ট সংগ্রহস্থল
- জ্ঞানভিত্তিক ডাটাবেস
- গঠনবদ্ধ ডেটা উৎস
- ফাইল সিস্টেম

### Prompts
Prompts হল ব্যবহারকারীর জন্য টেমপ্লেট করা বার্তা এবং ওয়ার্কফ্লো:
- পূর্বনির্ধারিত কথোপকথন টেমপ্লেট
- নির্দেশিত ইন্টারঅ্যাকশন প্যাটার্ন
- বিশেষায়িত সংলাপ কাঠামো

### Tools
Tools হল AI মডেলের জন্য কার্যকরী ফাংশন:
- ডেটা প্রক্রিয়াকরণ ইউটিলিটি
- বাহ্যিক API ইন্টিগ্রেশন
- গণনামূলক ক্ষমতা
- সার্চ ফাংশনালিটি

## Sample Implementations: C#

অফিসিয়াল C# SDK রিপোজিটরিতে MCP-এর বিভিন্ন দিক প্রদর্শন করে বেশ কয়েকটি স্যাম্পল ইমপ্লিমেন্টেশন রয়েছে:

- **Basic MCP Client**: MCP ক্লায়েন্ট তৈরি এবং টুল কল করার সহজ উদাহরণ
- **Basic MCP Server**: মৌলিক টুল রেজিস্ট্রেশন সহ একটি মিনি সার্ভার ইমপ্লিমেন্টেশন
- **Advanced MCP Server**: টুল রেজিস্ট্রেশন, অথেন্টিকেশন, এবং এরর হ্যান্ডলিংসহ সম্পূর্ণ ফিচারযুক্ত সার্ভার
- **ASP.NET Integration**: ASP.NET Core-র সাথে ইন্টিগ্রেশন প্রদর্শন করে উদাহরণসমূহ
- **Tool Implementation Patterns**: বিভিন্ন জটিলতার টুল ইমপ্লিমেন্টেশনের প্যাটার্নসমূহ

MCP C# SDK এখনও প্রিভিউ পর্যায়ে আছে এবং API পরিবর্তিত হতে পারে। SDK উন্নয়নের সাথে সাথে আমরা এই ব্লগ নিয়মিত আপডেট করব।

### Key Features 
- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)

- আপনার [প্রথম MCP সার্ভার তৈরি করা](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/)।

সম্পূর্ণ C# ইমপ্লিমেন্টেশন স্যাম্পল দেখতে [অফিসিয়াল C# SDK স্যাম্পল রিপোজিটরি](https://github.com/modelcontextprotocol/csharp-sdk) দেখুন।

## Sample implementation: Java Implementation

Java SDK এন্টারপ্রাইজ-গ্রেড ফিচারসহ শক্তিশালী MCP ইমপ্লিমেন্টেশন অপশন প্রদান করে।

### Key Features

- Spring Framework ইন্টিগ্রেশন
- শক্তিশালী টাইপ সেফটি
- রিয়েক্টিভ প্রোগ্রামিং সাপোর্ট
- ব্যাপক এরর হ্যান্ডলিং

সম্পূর্ণ Java ইমপ্লিমেন্টেশন স্যাম্পলের জন্য samples ডিরেক্টরির [Java sample](samples/java/containerapp/README.md) দেখুন।

## Sample implementation: JavaScript Implementation

JavaScript SDK MCP ইমপ্লিমেন্টেশনের জন্য হালকা ও নমনীয় পদ্ধতি প্রদান করে।

### Key Features

- Node.js এবং ব্রাউজার সাপোর্ট
- Promise ভিত্তিক API
- Express এবং অন্যান্য ফ্রেমওয়ার্কের সাথে সহজ ইন্টিগ্রেশন
- স্ট্রিমিংয়ের জন্য WebSocket সাপোর্ট

সম্পূর্ণ JavaScript ইমপ্লিমেন্টেশন স্যাম্পলের জন্য samples ডিরেক্টরির [JavaScript sample](samples/javascript/README.md) দেখুন।

## Sample implementation: Python Implementation

Python SDK MCP ইমপ্লিমেন্টেশনের জন্য Pythonic পদ্ধতি এবং চমৎকার ML ফ্রেমওয়ার্ক ইন্টিগ্রেশন প্রদান করে।

### Key Features

- asyncio সহ Async/await সাপোর্ট
- Flask এবং FastAPI ইন্টিগ্রেশন
- সহজ টুল রেজিস্ট্রেশন
- জনপ্রিয় ML লাইব্রেরির সাথে নেটিভ ইন্টিগ্রেশন

সম্পূর্ণ Python ইমপ্লিমেন্টেশন স্যাম্পলের জন্য samples ডিরেক্টরির [Python sample](samples/python/README.md) দেখুন।

## API management 

Azure API Management MCP সার্ভারগুলোকে সুরক্ষিত করার জন্য একটি চমৎকার সমাধান। ধারণাটি হল MCP সার্ভারের সামনে একটি Azure API Management ইন্সট্যান্স রাখা এবং এটি এমন ফিচারগুলো পরিচালনা করবে যা আপনি চাইতে পারেন, যেমন:

- রেট লিমিটিং
- টোকেন ম্যানেজমেন্ট
- মনিটরিং
- লোড ব্যালান্সিং
- সিকিউরিটি

### Azure Sample

এখানে একটি Azure Sample রয়েছে যা ঠিক এটি করে, অর্থাৎ MCP সার্ভার তৈরি এবং Azure API Management দিয়ে সুরক্ষিত করা: [creating an MCP Server and securing it with Azure API Management](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)।

নিচের ছবিতে দেখানো হয়েছে অথরাইজেশন ফ্লো কিভাবে ঘটে:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true) 

উপরের ছবিতে নিম্নলিখিত ঘটনা ঘটে:

- Microsoft Entra ব্যবহার করে Authentication/Authorization সম্পন্ন হয়।
- Azure API Management গেটওয়ে হিসেবে কাজ করে এবং পলিসি ব্যবহার করে ট্র্যাফিক পরিচালনা করে।
- Azure Monitor সমস্ত রিকোয়েস্ট লগ করে পরবর্তী বিশ্লেষণের জন্য।

#### Authorization flow

চলুন অথরাইজেশন ফ্লো আরও বিস্তারিত দেখি:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP authorization specification

আরও জানুন [MCP Authorization specification](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization#2-10-third-party-authorization-flow) সম্পর্কে।

## Deploy Remote MCP Server to Azure

চলুন দেখি আমরা আগের উল্লেখিত স্যাম্পলটি ডিপ্লয় করতে পারি কিনা:

1. রিপো ক্লোন করুন

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

2. `Microsoft.App` রেজিস্টার করুন

    ` resource provider.
    * If you are using Azure CLI, run `az provider register --namespace Microsoft.App --wait`.
    * If you are using Azure PowerShell, run `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Then run `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` কিছুক্ষণ পরে চেক করুন রেজিস্ট্রেশন সম্পন্ন হয়েছে কিনা।

3. নিচের [azd](https://aka.ms/azd) কমান্ডটি চালান যা API Management সার্ভিস, ফাংশন অ্যাপ (কোড সহ) এবং অন্যান্য প্রয়োজনীয় Azure রিসোর্স প্রোভিশন করবে

    ```shell
    azd up
    ```

    এই কমান্ডটি Azure-এ সমস্ত ক্লাউড রিসোর্স ডিপ্লয় করবে।

### Testing your server with MCP Inspector

1. **নতুন টার্মিনাল উইন্ডোতে**, MCP Inspector ইনস্টল ও চালান

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    আপনি একটি ইন্টারফেস দেখতে পাবেন যা এরকম হবে:

    ![Connect to Node inspector](../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.bn.png) 

2. CTRL ক্লিক করে MCP Inspector ওয়েব অ্যাপটি URL থেকে লোড করুন (যেমন: http://127.0.0.1:6274/#resources)
3. ট্রান্সপোর্ট টাইপ `SSE`
1. Set the URL to your running API Management SSE endpoint displayed after `azd up` সেট করুন এবং **Connect** করুন:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

5. **List Tools**। একটি টুলে ক্লিক করুন এবং **Run Tool** চাপুন।  

যদি সব ধাপ সঠিকভাবে সম্পন্ন হয়, তাহলে আপনি MCP সার্ভারের সাথে সংযুক্ত হয়েছেন এবং একটি টুল কল করতে সক্ষম হয়েছেন।

## MCP servers for Azure 

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): এই সেট রিপোজিটরি দ্রুত শুরু করার টেমপ্লেট সরবরাহ করে যা Azure Functions ব্যবহার করে Python, C# .NET অথবা Node/TypeScript দিয়ে কাস্টম রিমোট MCP সার্ভার তৈরি ও ডিপ্লয় করতে সাহায্য করে।

স্যাম্পলগুলো একটি পূর্ণাঙ্গ সমাধান দেয় যা ডেভেলপারদের:

- লোকালভাবে তৈরি ও চালানো: একটি MCP সার্ভার লোকাল মেশিনে ডেভেলপ এবং ডিবাগ করা
- Azure-এ ডিপ্লয়: সহজেই azd up কমান্ড দিয়ে ক্লাউডে ডিপ্লয় করা
- ক্লায়েন্ট থেকে সংযোগ: বিভিন্ন ক্লায়েন্ট থেকে MCP সার্ভারে সংযোগ করা, যেমন VS Code-এর Copilot এজেন্ট মোড এবং MCP Inspector টুল

### Key Features:

- ডিজাইনের মাধ্যমে সিকিউরিটি: MCP সার্ভার কী এবং HTTPS ব্যবহার করে সুরক্ষিত
- অথেন্টিকেশন অপশন: বিল্ট-ইন অথ এবং/অথবা API Management ব্যবহার করে OAuth সাপোর্ট
- নেটওয়ার্ক আইসোলেশন: Azure Virtual Networks (VNET) ব্যবহার করে নেটওয়ার্ক আইসোলেশন প্রদান
- সার্ভারলেস আর্কিটেকচার: স্কেলেবল, ইভেন্ট-চালিত এক্সিকিউশনের জন্য Azure Functions ব্যবহার
- লোকাল ডেভেলপমেন্ট: ব্যাপক লোকাল ডেভেলপমেন্ট ও ডিবাগিং সাপোর্ট
- সহজ ডিপ্লয়মেন্ট: Azure-এ সহজ ও দ্রুত ডিপ্লয়মেন্ট প্রসেস

রিপোজিটরিতে সমস্ত প্রয়োজনীয় কনফিগারেশন ফাইল, সোর্স কোড, এবং অবকাঠামো সংজ্ঞা অন্তর্ভুক্ত রয়েছে যা দ্রুত প্রোডাকশন-রেডি MCP সার্ভার ইমপ্লিমেন্টেশন শুরু করতে সাহায্য করে।

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Python দিয়ে Azure Functions ব্যবহার করে MCP এর স্যাম্পল ইমপ্লিমেন্টেশন

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - C# .NET দিয়ে Azure Functions ব্যবহার করে MCP এর স্যাম্পল ইমপ্লিমেন্টেশন

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Node/TypeScript দিয়ে Azure Functions ব্যবহার করে MCP এর স্যাম্পল ইমপ্লিমেন্টেশন।

## Key Takeaways

- MCP SDK গুলো ভাষা-নির্দিষ্ট টুল প্রদান করে শক্তিশালী MCP সমাধান তৈরি করার জন্য
- ডিবাগিং ও টেস্টিং প্রক্রিয়া নির্ভরযোগ্য MCP অ্যাপ্লিকেশন তৈরির জন্য অপরিহার্য
- পুনঃব্যবহারযোগ্য প্রম্পট টেমপ্লেট AI ইন্টারঅ্যাকশনকে ধারাবাহিক করে তোলে
- ভালো ডিজাইন করা ওয়ার্কফ্লো বিভিন্ন টুল ব্যবহার করে জটিল কাজগুলো সমন্বয় করতে পারে
- MCP সমাধান ইমপ্লিমেন্টেশনে সিকিউরিটি, পারফরম্যান্স, এবং এরর হ্যান্ডলিং বিবেচনা করা আবশ্যক

## Exercise

আপনার ডোমেইনে একটি বাস্তব সমস্যার সমাধান করার জন্য একটি প্র্যাকটিক্যাল MCP ওয়ার্কফ্লো ডিজাইন করুন:

1. এই সমস্যার সমাধানে সহায়ক ৩-৪টি টুল চিহ্নিত করুন
2. একটি ওয়ার্কফ্লো ডায়াগ্রাম তৈরি করুন যা দেখাবে কিভাবে এই টুলগুলো একে অপরের সাথে কাজ করবে
3. আপনার পছন্দের ভাষায় একটি টুলের মৌলিক সংস্করণ ইমপ্লিমেন্ট করুন
4. এমন একটি প্রম্পট টেমপ্লেট তৈরি করুন যা মডেলকে আপনার টুল কার্যকরভাবে ব্যবহার করতে সাহায্য করবে

## Additional Resources


---

Next: [Advanced Topics](../05-AdvancedTopics/README.md)

**বিস্তারিত বর্জন**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার জন্য চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই সর্বোত্তম এবং নির্ভরযোগ্য উৎস হিসেবে গণ্য করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদের পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।