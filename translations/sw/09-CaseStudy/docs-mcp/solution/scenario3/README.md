<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "db532b1ec386c9ce38c791653dc3c881",
  "translation_date": "2025-06-21T14:42:41+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/scenario3/README.md",
  "language_code": "sw"
}
-->
# Scenario 3: Nyaraka Ndani ya Mhariri kwa kutumia MCP Server katika VS Code

## Muhtasari

Katika hali hii, utajifunza jinsi ya kuleta Microsoft Learn Docs moja kwa moja ndani ya mazingira yako ya Visual Studio Code kwa kutumia server ya MCP. Badala ya kubadili tabo za kivinjari kila mara kutafuta nyaraka, unaweza kufikia, kutafuta, na kurejelea nyaraka rasmi moja kwa moja ndani ya mhariri wako. Njia hii huondoa usumbufu katika kazi zako, inakuweka makini, na inaruhusu muunganisho rahisi na zana kama GitHub Copilot.

- Tafuta na soma nyaraka ndani ya VS Code bila kuondoka kwenye mazingira ya uandishi wa msimbo.
- Rejelea nyaraka na weka viungo moja kwa moja kwenye README au faili za kozi.
- Tumia GitHub Copilot na MCP pamoja kwa mtiririko wa kazi ulio rahisi na unaotumia AI.

## Malengo ya Kujifunza

Mwisho wa sura hii, utakuwa umeelewa jinsi ya kusanidi na kutumia server ya MCP ndani ya VS Code ili kuboresha mtiririko wako wa nyaraka na maendeleo. Utaweza:

- Kusanidi eneo lako la kazi kutumia server ya MCP kwa ajili ya kutafuta nyaraka.
- Kutafuta na kuingiza nyaraka moja kwa moja kutoka ndani ya VS Code.
- Kuchanganya nguvu za GitHub Copilot na MCP kwa mtiririko wa kazi wenye tija zaidi unaosaidiwa na AI.

Ujuzi huu utakusaidia kubaki makini, kuboresha ubora wa nyaraka, na kuongeza ufanisi wako kama mtaalamu wa maendeleo au mwandishi wa kiufundi.

## Suluhisho

Ili kufanikisha upatikanaji wa nyaraka ndani ya mhariri, utafuata hatua kadhaa zinazochanganya server ya MCP na VS Code pamoja na GitHub Copilot. Suluhisho hili ni bora kwa waandishi wa kozi, waandishi wa nyaraka, na watengenezaji wanaotaka kubaki makini ndani ya mhariri wakati wakifanya kazi na nyaraka na Copilot.

- Ongeza viungo vya rejea haraka kwenye README wakati wa kuandika nyaraka za kozi au mradi.
- Tumia Copilot kuunda msimbo na MCP kupata na kutaja nyaraka zinazohusiana mara moja.
- Bakia makini ndani ya mhariri wako na ongeza tija.

### Mwongozo wa Hatua kwa Hatua

Ili kuanza, fuata hatua hizi. Kwa kila hatua, unaweza kuongeza picha kutoka kwenye folda ya mali ili kuonyesha mchakato kwa njia ya kuona.

1. **Ongeza usanidi wa MCP:**
   Katika mzizi wa mradi wako, tengeneza faili la `.vscode/mcp.json` na ongeza usanidi ufuatao:
   ```json
   {
     "servers": {
       "LearnDocsMCP": {
         "url": "https://learn.microsoft.com/api/mcp"
       }
     }
   }
   ```
   Usanidi huu unaeleza VS Code jinsi ya kuunganishwa na [`Microsoft Learn Docs MCP server`](https://github.com/MicrosoftDocs/mcp).
   
   ![Hatua 1: Ongeza mcp.json kwenye folda ya .vscode](../../../../../../translated_images/step1-mcp-json.c06a007fccc3edfaf0598a31903c9ec71476d9fd3ae6c1b2b4321fd38688ca4b.sw.png)
    
2. **Fungua jopo la GitHub Copilot Chat:**
   Ikiwa bado huna ugani wa GitHub Copilot umewekwa, nenda kwenye sehemu ya Ugani katika VS Code na uweke. Unaweza kuupakua moja kwa moja kutoka [Visual Studio Code Marketplace](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat). Kisha, fungua jopo la Copilot Chat kutoka kwenye upau wa pembeni.

   ![Hatua 2: Fungua jopo la Copilot Chat](../../../../../../translated_images/step2-copilot-panel.f1cc86e9b9b8cd1a85e4df4923de8bafee4830541ab255e3c90c09777fed97db.sw.png)

3. **Washa hali ya wakala na hakiki zana:**
   Katika jopo la Copilot Chat, washa hali ya wakala.

   ![Hatua 3: Washa hali ya wakala na hakiki zana](../../../../../../translated_images/step3-agent-mode.cdc32520fd7dd1d149c3f5226763c1d85a06d3c041d4cc983447625bdbeff4d4.sw.png)

   Baada ya kuwasha hali ya wakala, hakiki kama server ya MCP iko kwenye orodha ya zana zinazopatikana. Hii inahakikisha wakala wa Copilot anaweza kufikia server ya nyaraka kupata taarifa zinazofaa.
   
   ![Hatua 3: Hakiki zana ya MCP server](../../../../../../translated_images/step3-verify-mcp-tool.76096a6329cbfecd42888780f322370a0d8c8fa003ed3eeb7ccd23f0fc50c1ad.sw.png)
4. **Anza mazungumzo mapya na muulize wakala:**
   Fungua mazungumzo mapya katika jopo la Copilot Chat. Sasa unaweza kumuuliza wakala maswali yako kuhusu nyaraka. Wakala atatumia server ya MCP kupata na kuonyesha nyaraka zinazohusiana za Microsoft Learn moja kwa moja ndani ya mhariri wako.

   - *"Najaribu kuandika mpango wa masomo kwa mada X. Nitaitumia kwa wiki 8, kwa kila wiki, pendekeza maudhui ninayopaswa kuchukua."*

   ![Hatua 4: Muulize wakala katika mazungumzo](../../../../../../translated_images/step4-prompt-chat.12187bb001605efc5077992b621f0fcd1df12023c5dce0464f8eb8f3d595218f.sw.png)

5. **Maswali ya Moja kwa Moja:**

   > Tuchukue swali la moja kwa moja kutoka sehemu ya [#get-help](https://discord.gg/D6cRhjHWSC) katika Azure AI Foundry Discord ([tazama ujumbe wa awali](https://discord.com/channels/1113626258182504448/1385498306720829572)):
   
   *"Natafuta majibu kuhusu jinsi ya kupeleka suluhisho la mawakala wengi lililotengenezwa kwa mawakala wa AI katika Azure AI Foundry. Naona hakuna njia ya moja kwa moja ya upeleka, kama vile njia za Copilot Studio. Basi, ni njia gani tofauti za kufanya upeleka huu kwa watumiaji wa kampuni ili waweze kuingiliana na kukamilisha kazi?
Kuna makala nyingi/blogu zinazosema tunaweza kutumia huduma ya Azure Bot kufanya kazi hii ambayo inaweza kuwa daraja kati ya MS Teams na Azure AI Foundry Agents, je, hii itafanya kazi kama nitasanidi bot ya Azure inayounganisha na Orchestrator Agent kwenye Azure AI Foundry kupitia Azure function kwa ajili ya kufanya orchestration au nahitaji kuunda Azure function kwa kila mmoja wa mawakala wa AI katika suluhisho la mawakala wengi kufanya orchestration kwenye Bot framework? Mapendekezo mengine yamekaribishwa sana.
"*

   ![Hatua 5: Maswali ya moja kwa moja](../../../../../../translated_images/step5-live-queries.49db3e4a50bea27327e3cb18c24d263b7d134930d78e7392f9515a1c00264a7f.sw.png)

   Wakala atajibu kwa viungo vya nyaraka zinazohusiana na muhtasari, ambavyo unaweza kisha kuingiza moja kwa moja kwenye faili zako za markdown au kutumia kama rejea katika msimbo wako.
   
### Maswali ya Mfano

Hapa kuna baadhi ya maswali ya mfano unayoweza kujaribu. Maswali haya yataonyesha jinsi server ya MCP na Copilot vinaweza kufanya kazi pamoja kutoa nyaraka na rejea za haraka, zinazojali muktadha, bila kuondoka VS Code:

- "Nionyeshe jinsi ya kutumia vichocheo vya Azure Functions."
- "Weka kiungo cha nyaraka rasmi za Azure Key Vault."
- "Ni mbinu bora zipi za kuimarisha usalama wa rasilimali za Azure?"
- "Tafuta mwongozo wa kuanza haraka kwa huduma za Azure AI."

Maswali haya yataonyesha jinsi server ya MCP na Copilot vinaweza kufanya kazi pamoja kutoa nyaraka na rejea za haraka, zinazojali muktadha, bila kuondoka VS Code.

---

**Kumbusho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kupata usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati ya awali katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu ya binadamu inapendekezwa. Hatubeba dhamana yoyote kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.