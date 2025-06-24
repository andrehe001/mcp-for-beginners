<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:31:59+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "sw"
}
-->
# Kizazi cha Mpango wa Masomo kwa Chainlit & Microsoft Learn Docs MCP

## Mahitaji

- Python 3.8 au zaidi
- pip (msimamizi wa vifurushi vya Python)
- Muunganisho wa intaneti kuweza kuungana na seva ya Microsoft Learn Docs MCP

## Usanidi

1. Nakili (clone) hifadhi hii au pakua faili za mradi.
2. Sakinisha utegemezi unaohitajika:

   ```bash
   pip install -r requirements.txt
   ```

## Matumizi

### Hali ya 1: Utafutaji Rahisi kwa Docs MCP  
Mteja wa mstari wa amri unaounganisha na seva ya Docs MCP, kutuma swali, na kuchapisha matokeo.

1. Endesha script:  
   ```bash
   python scenario1.py
   ```  
2. Weka swali lako la nyaraka kwenye kiashiria.

### Hali ya 2: Kizazi cha Mpango wa Masomo (Programu ya Wavuti ya Chainlit)  
Kiolesura cha wavuti (kinachotumia Chainlit) kinachoruhusu watumiaji kuunda mpango wa masomo wa kibinafsi, wa wiki kwa wiki kwa mada yoyote ya kiufundi.

1. Anzisha programu ya Chainlit:  
   ```bash
   chainlit run scenario2.py
   ```  
2. Fungua URL ya ndani iliyotolewa kwenye terminal yako (mfano, http://localhost:8000) katika kivinjari chako.  
3. Katika dirisha la mazungumzo, ingiza mada yako ya masomo na idadi ya wiki unayotaka kusoma (mfano, "AI-900 certification, 8 weeks").  
4. Programu itajibu na mpango wa masomo wa wiki kwa wiki, ikiwa na viungo vya nyaraka husika za Microsoft Learn.

**Mazingira Yanayohitajika:**  

Ili kutumia Hali ya 2 (programu ya wavuti ya Chainlit na Azure OpenAI), lazima uweke mabadiliko ya mazingira yafuatayo katika saraka ya `.env` file in the `python`:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Jaza maelezo haya kwa taarifa zako za rasilimali ya Azure OpenAI kabla ya kuendesha programu.

> **Tip:** Unaweza kwa urahisi kuanzisha mifano yako mwenyewe kwa kutumia [Azure AI Foundry](https://ai.azure.com/).

### Hali ya 3: Nyaraka Ndani ya Mhariri na Seva ya MCP katika VS Code

Badala ya kubadilisha tabo za kivinjari kutafuta nyaraka, unaweza kuleta Microsoft Learn Docs moja kwa moja ndani ya VS Code yako kwa kutumia seva ya MCP. Hii inakuwezesha:  
- Kutafuta na kusoma nyaraka ndani ya VS Code bila kuondoka kwenye mazingira ya kuandika msimbo.  
- Kurejelea nyaraka na kuweka viungo moja kwa moja katika README au faili za kozi.  
- Kutumia GitHub Copilot na MCP pamoja kwa mtiririko wa kazi wa nyaraka unaoendeshwa na AI bila mshono.

**Mifano ya Matumizi:**  
- Ongeza viungo vya rejea kwa README haraka wakati wa kuandika nyaraka za kozi au mradi.  
- Tumia Copilot kuunda msimbo na MCP kupata na kutaja nyaraka husika mara moja.  
- Endelea kuzingatia mhariri wako na kuongeza tija.

> [!IMPORTANT]  
> Hakikisha una [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

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

Mifano hii inaonyesha ufanisi wa programu kwa malengo mbalimbali ya kujifunza na vipindi tofauti vya muda.

## Marejeleo

- [Chainlit Documentation](https://docs.chainlit.io/)  
- [MCP Documentation](https://github.com/MicrosoftDocs/mcp)

**Kiarifu cha Kutotegemea**:  
Nyaraka hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au upotoshaji. Nyaraka asilia katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu na ya binadamu inapendekezwa. Hatubeba dhima kwa kutoelewana au tafsiri potofu zitokanazo na matumizi ya tafsiri hii.