<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "36de9fae488d6de554d969fe8e0801a8",
  "translation_date": "2025-06-20T19:17:01+00:00",
  "source_file": "09-CaseStudy/apimsample.md",
  "language_code": "bn"
}
-->
# কেস স্টাডি: API Management-এ MCP সার্ভার হিসেবে REST API প্রকাশ করা

Azure API Management হলো একটি সার্ভিস যা আপনার API Endpoints-এর উপরে একটি গেটওয়ে প্রদান করে। এটি কাজ করে এমনভাবে যে Azure API Management আপনার API গুলোর সামনে একটি প্রক্সি হিসেবে কাজ করে এবং আসা অনুরোধগুলো নিয়ে কী করা হবে তা নির্ধারণ করে।

এটি ব্যবহারের মাধ্যমে আপনি অনেক ধরনের ফিচার পেতে পারেন, যেমন:

- **সুরক্ষা**, আপনি API কী, JWT থেকে শুরু করে managed identity পর্যন্ত সব কিছু ব্যবহার করতে পারেন।
- **রেট লিমিটিং**, একটি অসাধারণ ফিচার হল আপনি নির্ধারণ করতে পারবেন কতগুলো কল একটি নির্দিষ্ট সময় এককে পার হবে। এটি নিশ্চিত করে যে সকল ব্যবহারকারীর অভিজ্ঞতা ভালো থাকবে এবং আপনার সার্ভিস অনুরোধে অতিরিক্ত চাপের মুখোমুখি হবে না।
- **স্কেলিং ও লোড ব্যালান্সিং**। আপনি অনেকগুলো এন্ডপয়েন্ট সেটআপ করতে পারেন লোড ভাগ করার জন্য এবং আপনি লোড ব্যালান্স করার পদ্ধতিও নির্ধারণ করতে পারবেন।
- **AI ফিচার যেমন সেমান্টিক ক্যাশিং**, টোকেন সীমা এবং টোকেন মনিটরিং ইত্যাদি। এগুলো দুর্দান্ত ফিচার যা প্রতিক্রিয়াশীলতা উন্নত করে এবং টোকেন ব্যবহারের উপর নিয়ন্ত্রণ রাখতে সাহায্য করে। [আরও পড়ুন এখানে](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities)।

## কেন MCP + Azure API Management?

Model Context Protocol দ্রুত এজেন্টিক AI অ্যাপ্লিকেশনের জন্য একটি স্ট্যান্ডার্ড হয়ে উঠছে এবং কীভাবে টুলস ও ডেটা ধারাবাহিকভাবে প্রকাশ করা যায় তা নির্ধারণ করছে। Azure API Management একটি স্বাভাবিক পছন্দ যখন আপনাকে API গুলো "ম্যানেজ" করতে হয়। MCP সার্ভার প্রায়শই অন্যান্য API গুলোর সাথে ইন্টিগ্রেট করে যেমন টুলের অনুরোধ সমাধান করার জন্য। তাই Azure API Management এবং MCP একসাথে ব্যবহার করা বেশ যুক্তিযুক্ত।

## ওভারভিউ

এই নির্দিষ্ট ব্যবহার কেসে আমরা শিখব কীভাবে API এন্ডপয়েন্টগুলো MCP সার্ভার হিসেবে প্রকাশ করতে হয়। এর মাধ্যমে, আমরা সহজেই এই এন্ডপয়েন্টগুলোকে একটি এজেন্টিক অ্যাপের অংশ করতে পারব এবং Azure API Management এর ফিচারগুলোও ব্যবহার করতে পারব।

## মূল ফিচারসমূহ

- আপনি যেই এন্ডপয়েন্ট মেথডগুলো টুল হিসেবে প্রকাশ করতে চান সেগুলো নির্বাচন করবেন।
- অতিরিক্ত ফিচারগুলো নির্ভর করে আপনি API এর পলিসি সেকশনে কী কনফিগার করেন তার ওপর। এখানে আমরা দেখাবো কীভাবে রেট লিমিটিং যোগ করবেন।

## প্রাক-ধাপ: একটি API ইম্পোর্ট করা

যদি আপনার Azure API Management-এ ইতিমধ্যেই একটি API থাকে, তাহলে এই ধাপটি এড়িয়ে যেতে পারেন। না থাকলে, এই লিঙ্কটি দেখুন, [Azure API Management-এ API ইম্পোর্ট করা](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api)।

## API MCP সার্ভার হিসেবে প্রকাশ করা

API এন্ডপয়েন্টগুলো প্রকাশ করতে নিম্নলিখিত ধাপগুলো অনুসরণ করুন:

1. Azure Portal-এ যান এবং এই ঠিকানায় যান <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
   আপনার API Management ইনস্ট্যান্সে নেভিগেট করুন।

2. বাম মেনু থেকে নির্বাচন করুন APIs > MCP Servers > + Create new MCP Server।

3. API-তে একটি REST API নির্বাচন করুন যা MCP সার্ভার হিসেবে প্রকাশ করবেন।

4. একটি বা একাধিক API অপারেশন নির্বাচন করুন যেগুলো টুল হিসেবে প্রকাশ করতে চান। আপনি সব অপারেশন বা নির্দিষ্ট কিছু অপারেশনই নির্বাচন করতে পারেন।

    ![Select methods to expose](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

5. **Create** নির্বাচন করুন।

6. মেনু থেকে **APIs** এবং **MCP Servers**-এ যান, আপনি নিচের মতো দেখতে পাবেন:

    ![See the MCP Server in the main pane](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP সার্ভার তৈরি হয়েছে এবং API অপারেশনগুলো টুল হিসেবে প্রকাশ করা হয়েছে। MCP সার্ভার MCP Servers প্যানেলে তালিকাভুক্ত থাকবে। URL কলামটি MCP সার্ভারের এন্ডপয়েন্ট দেখায় যা আপনি টেস্টিং বা ক্লায়েন্ট অ্যাপ্লিকেশনে কল করতে পারবেন।

## ঐচ্ছিক: পলিসি কনফিগার করা

Azure API Management-এ পলিসি একটি মূল ধারণা, যেখানে আপনি বিভিন্ন নিয়ম সেট করেন যেমন রেট লিমিটিং বা সেমান্টিক ক্যাশিং। এই পলিসিগুলো XML ফরম্যাটে লেখা হয়।

আপনার MCP সার্ভারের জন্য রেট লিমিটিং পলিসি কনফিগার করার পদ্ধতি:

1. পোর্টালে APIs এর অধীনে **MCP Servers** নির্বাচন করুন।

2. আপনি যে MCP সার্ভার তৈরি করেছেন সেটি নির্বাচন করুন।

3. বাম মেনু থেকে MCP এর অধীনে **Policies** নির্বাচন করুন।

4. পলিসি এডিটরে MCP সার্ভারের টুলসের জন্য প্রযোজ্য পলিসি যোগ বা সম্পাদনা করুন। পলিসিগুলো XML ফরম্যাটে থাকে। উদাহরণস্বরূপ, আপনি একটি পলিসি যোগ করতে পারেন যা MCP সার্ভারের টুলসের কল সীমাবদ্ধ করবে (এই উদাহরণে, প্রতি ক্লায়েন্ট IP ঠিকানায় ৩০ সেকেন্ডে ৫টি কল)। নিচে XML কোড রয়েছে যা এটি করবে:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    পলিসি এডিটরের একটি ছবি:

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## চেষ্টা করে দেখুন

চলুন নিশ্চিত করি আমাদের MCP সার্ভার ঠিকমতো কাজ করছে।

এ জন্য আমরা Visual Studio Code এবং GitHub Copilot এর Agent মোড ব্যবহার করব। আমরা MCP সার্ভারটি *mcp.json* এ যোগ করব। এর ফলে Visual Studio Code একটি এজেন্টিক ক্ষমতাসম্পন্ন ক্লায়েন্ট হিসেবে কাজ করবে এবং শেষ ব্যবহারকারীরা প্রম্পট টাইপ করে সার্ভারের সাথে ইন্টারঅ্যাক্ট করতে পারবে।

Visual Studio Code-এ MCP সার্ভার যোগ করার পদ্ধতি:

1. Command Palette থেকে MCP: **Add Server কমান্ড** ব্যবহার করুন।

2. প্রম্পট এ সার্ভার টাইপ নির্বাচন করুন: **HTTP (HTTP or Server Sent Events)**।

3. API Management-এ MCP সার্ভারের URL দিন। উদাহরণ: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (SSE এন্ডপয়েন্টের জন্য) অথবা **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (MCP এন্ডপয়েন্টের জন্য), লক্ষ্য করুন ট্রান্সপোর্টের পার্থক্য `/sse` or `/mcp`।

4. একটি সার্ভার ID দিন আপনার পছন্দমতো। এটি একটি গুরুত্বপূর্ণ মান নয়, তবে এটি সার্ভার ইনস্ট্যান্সটি চিনতে সাহায্য করবে।

5. নির্বাচন করুন কনফিগারেশনটি আপনার ওয়ার্কস্পেস সেটিংসে সংরক্ষণ করবেন নাকি ইউজার সেটিংসে।

  - **ওয়ার্কস্পেস সেটিংস** - সার্ভার কনফিগারেশন .vscode/mcp.json ফাইলে সংরক্ষিত হয়, যা শুধুমাত্র বর্তমান ওয়ার্কস্পেসে উপলব্ধ।

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    অথবা যদি আপনি স্ট্রিমিং HTTP ট্রান্সপোর্ট নির্বাচন করেন, তাহলে এটি কিছুটা আলাদা হবে:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **ইউজার সেটিংস** - সার্ভার কনফিগারেশন আপনার গ্লোবাল *settings.json* ফাইলে যোগ হয় এবং সব ওয়ার্কস্পেসে উপলব্ধ থাকে। কনফিগারেশন নিচের মতো দেখায়:

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

6. এছাড়াও আপনাকে একটি হেডার যোগ করতে হবে যাতে এটি সঠিকভাবে Azure API Management-এর সাথে প্রমাণীকরণ করে। এটি একটি হেডার ব্যবহার করে যার নাম **Ocp-Apim-Subscription-Key**।

    - সেটিংসে এটি যোগ করার পদ্ধতি:

    ![Adding header for authentication](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png)  
      এটি একটি প্রম্পট দেখাবে যেখানে আপনাকে API কী এর মান দিতে হবে যা আপনি Azure Portal থেকে আপনার API Management ইনস্ট্যান্সে পেতে পারেন।

    - *mcp.json* এ যোগ করতে চাইলে এরকম করবেন:

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

### Agent মোড ব্যবহার করুন

এখন আমরা সেটিংস বা *.vscode/mcp.json* এ সব কনফিগার করেছি। চলুন পরীক্ষা করি।

একটি Tools আইকন থাকবে যেখান থেকে আপনার সার্ভার থেকে প্রকাশিত টুলগুলো দেখা যাবে:

![Tools from the server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Tools আইকনে ক্লিক করুন, আপনি টুলগুলোর একটি তালিকা দেখতে পাবেন:

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

2. চ্যাটে একটি প্রম্পট লিখুন টুল চালানোর জন্য। উদাহরণস্বরূপ, যদি আপনি একটি অর্ডারের তথ্য পাওয়ার টুল নির্বাচন করে থাকেন, তাহলে এজেন্টকে অর্ডার সম্পর্কে জিজ্ঞাসা করতে পারেন। উদাহরণ প্রম্পট:

    ```text
    get information from order 2
    ```

    এরপর আপনাকে একটি টুলস আইকন দেখানো হবে যা আপনাকে টুল কল চালিয়ে যেতে বলবে। চালিয়ে যান, আপনি নিচের মতো আউটপুট দেখতে পাবেন:

    ![Result from prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **উপরের আউটপুট আপনি যে টুলগুলো সেটআপ করেছেন তার ওপর নির্ভর করবে, তবে মূল ধারণা হল আপনি একটি টেক্সট ভিত্তিক প্রতিক্রিয়া পাবেন।**

## রেফারেন্সসমূহ

আরও জানতে পারেন:

- [Azure API Management এবং MCP এর টিউটোরিয়াল](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python স্যাম্পল: Azure API Management ব্যবহার করে নিরাপদ রিমোট MCP সার্ভার (প্রায়োগিক)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP ক্লায়েন্ট অথরাইজেশন ল্যাব](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Visual Studio Code এর জন্য Azure API Management এক্সটেনশন ব্যবহার করে API ইম্পোর্ট ও ম্যানেজ করা](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Azure API Center-এ রিমোট MCP সার্ভার রেজিস্টার ও ডিসকভার করা](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) - একটি অসাধারণ রিপোজিটরি যা Azure API Management এর সাথে অনেক AI ক্ষমতা প্রদর্শন করে
- [AI Gateway ওয়ার্কশপসমূহ](https://azure-samples.github.io/AI-Gateway/) - Azure Portal ব্যবহার করে ওয়ার্কশপ রয়েছে, যা AI ক্ষমতা মূল্যায়নের জন্য একটি চমৎকার শুরু।

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতার জন্য চেষ্টা করি, তবে দয়া করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল নথিটি তার নিজস্ব ভাষায়ই কর্তৃত্বপূর্ণ উৎস হিসেবে বিবেচিত হওয়া উচিত। গুরুত্বপূর্ণ তথ্যের জন্য পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হয়। এই অনুবাদের ব্যবহারে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।