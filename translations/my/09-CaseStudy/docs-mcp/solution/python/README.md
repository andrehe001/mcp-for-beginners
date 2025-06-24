<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:33:29+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "my"
}
-->
# Chainlit နှင့် Microsoft Learn Docs MCP ဖြင့် သင်ယူအစီအစဉ် ထုတ်လုပ်သူ

## မတိုင်မီလိုအပ်ချက်များ

- Python 3.8 သို့မဟုတ် အထက်
- pip (Python package များစီမံခန့်ခွဲသူ)
- Microsoft Learn Docs MCP ဆာဗာနှင့် ချိတ်ဆက်ရန် အင်တာနက် ချိတ်ဆက်မှု

## ထည့်သွင်းခြင်း

1. ဒီ repository ကို clone လုပ်ပါ သို့မဟုတ် project ဖိုင်များကို ဒေါင်းလုပ်လုပ်ပါ။
2. လိုအပ်သော dependencies များကို ထည့်သွင်းပါ။

   ```bash
   pip install -r requirements.txt
   ```

## အသုံးပြုမှု

### နမူနာ ၁: Docs MCP သို့ ရိုးရှင်းသော မေးခွန်းတစ်ခု

Docs MCP ဆာဗာနှင့် ချိတ်ဆက်ပြီး မေးခွန်းတစ်ခု ပို့၍ ရလဒ်ကို ပရင့်ထုတ်ပေးသော command-line client ဖြစ်သည်။

1. script ကို run ပါ။
   ```bash
   python scenario1.py
   ```
2. prompt တွင် သင်၏ documentation မေးခွန်းကို ထည့်ပါ။

### နမူနာ ၂: သင်ယူအစီအစဉ် ထုတ်လုပ်သူ (Chainlit Web App)

Chainlit ကို အသုံးပြုထားသော web interface တစ်ခုဖြစ်ပြီး၊ အသုံးပြုသူများအား နည်းပညာဆိုင်ရာ ခေါင်းစဉ်တစ်ခုအတွက် အပတ်စဉ် သင်ယူအစီအစဉ် ကို ကိုယ်ပိုင်ပြုလုပ်နိုင်စေသည်။

1. Chainlit app ကို စတင်ပါ။
   ```bash
   chainlit run scenario2.py
   ```
2. terminal တွင် ပြသသော local URL (ဥပမာ - http://localhost:8000) ကို browser မှာ ဖွင့်ပါ။
3. chat ပြတင်းပေါ်တွင် သင်ယူလိုသော ခေါင်းစဉ်နှင့် သင်ယူလိုသော အပတ်အရေအတွက် (ဥပမာ - "AI-900 certification, 8 weeks") ကို ထည့်ပါ။
4. app သည် အပတ်စဉ် သင်ယူအစီအစဉ်ကို Microsoft Learn documentation လင့်ခ်များနှင့်အတူ ပြန်လည်တုံ့ပြန်ပေးပါမည်။

**လိုအပ်သော Environment Variables:**

Scenario 2 (Azure OpenAI နှင့် Chainlit web app) ကို အသုံးပြုရန် `.env` file in the `python` ဖိုင်အတွင်း အောက်ပါ environment variables များကို သတ်မှတ်ထားရမည်။

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

app ကို run မပြုမီ သင့် Azure OpenAI resource အသေးစိတ်များဖြင့် တန်ဖိုးများကို ဖြည့်သွင်းပါ။

> **Tip:** [Azure AI Foundry](https://ai.azure.com/) ကို အသုံးပြု၍ မိမိအပေါ် မော်ဒယ်များကို လွယ်ကူစွာ တပ်ဆင်နိုင်ပါသည်။

### နမူနာ ၃: VS Code တွင် MCP ဆာဗာဖြင့် အတွင်းရေးဆွဲသူ Docs

Browser tab မပြောင်းလဲဘဲ Microsoft Learn Docs ကို တိုက်ရိုက် VS Code ထဲသို့ ယူဆောင်နိုင်သည်။ ၎င်းဖြင့် -
- VS Code အတွင်းမှ တိုက်ရိုက် Docs ရှာဖွေဖတ်ရှုနိုင်ခြင်း။
- README သို့မဟုတ် သင်တန်းဖိုင်များထဲတွင် တိုက်ရိုက် link များ ထည့်သွင်းနိုင်ခြင်း။
- GitHub Copilot နှင့် MCP ကို တွဲဖက်အသုံးပြု၍ AI အားဖြင့် စနစ်တကျ documentation workflow တည်ဆောက်နိုင်ခြင်း။

**အသုံးပြုရန် နမူနာများ:**
- သင်တန်း သို့မဟုတ် project documentation ရေးစဉ် README တွင် အမြန် reference links ထည့်ရန်။
- Copilot ဖြင့် code ထုတ်လုပ်ပြီး MCP ဖြင့် ဆက်စပ် docs များကို အမြန် ရှာဖွေနိုင်ရန်။
- editor ထဲတွင် အာရုံစူးစိုက်ပြီး ထုတ်လုပ်မှု တိုးတက်စေခြင်း။

> [!IMPORTANT]
> သင့်တွင် သက်ဆိုင်ရာ [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

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
- `Cloud architecture, 9 weeks`] ဖိုင်ရှိကြောင်း သေချာစေပါ။

ဤနမူနာများသည် အမျိုးမျိုးသော သင်ယူရည်ရွယ်ချက်များနှင့် အချိန်ကာလများအတွက် app ၏ သက်တမ်းကို ပြသသည်။

## ရင်းမြစ်များ

- [Chainlit Documentation](https://docs.chainlit.io/)
- [MCP Documentation](https://github.com/MicrosoftDocs/mcp)

**အကြောင်းကြားချက်**  
ဤစာရွက်စာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှုဖြစ်သည့် [Co-op Translator](https://github.com/Azure/co-op-translator) ကို အသုံးပြု၍ ဘာသာပြန်ထားပါသည်။ တိကျမှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်မှုများတွင် အမှားများ သို့မဟုတ် တိကျမှုလျော့နည်းမှုများ ဖြစ်နိုင်ပါကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူလစာရွက်စာတမ်းသည် မိခင်ဘာသာဖြင့် ရေးသားထားသည့် အတည်ပြုအရင်းအမြစ်အဖြစ် သတ်မှတ်ရန် လိုအပ်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် ကျွမ်းကျင်သော လူ့ဘာသာပြန်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်မှုကို အသုံးပြုခြင်းကြောင့် ဖြစ်ပေါ်လာနိုင်သည့် မမှန်ကန်သော နားလည်မှုများ သို့မဟုတ် မှားယွင်းသည့် အဓိပ္ပာယ်ဖွင့်ဆိုမှုများအတွက် ကျွန်ုပ်တို့သည် တာဝန်မယူပါ။