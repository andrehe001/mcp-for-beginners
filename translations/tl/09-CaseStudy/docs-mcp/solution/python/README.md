<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:31:49+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "tl"
}
-->
# Study Plan Generator gamit ang Chainlit at Microsoft Learn Docs MCP

## Mga Kinakailangan

- Python 3.8 o mas mataas pa
- pip (Python package manager)
- Internet connection para makakonekta sa Microsoft Learn Docs MCP server

## Pag-install

1. I-clone ang repository na ito o i-download ang mga file ng proyekto.
2. I-install ang mga kinakailangang dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Paggamit

### Senaryo 1: Simpleng Query sa Docs MCP
Isang command-line client na kumokonekta sa Docs MCP server, nagpapadala ng query, at ipinapakita ang resulta.

1. Patakbuhin ang script:
   ```bash
   python scenario1.py
   ```
2. I-type ang iyong tanong tungkol sa dokumentasyon sa prompt.

### Senaryo 2: Study Plan Generator (Chainlit Web App)
Isang web-based na interface (gamit ang Chainlit) na nagpapahintulot sa mga user na gumawa ng personalized na plano ng pag-aaral linggo-linggo para sa kahit anong teknikal na paksa.

1. Simulan ang Chainlit app:
   ```bash
   chainlit run scenario2.py
   ```
2. Buksan ang lokal na URL na ipapakita sa iyong terminal (halimbawa, http://localhost:8000) sa iyong browser.
3. Sa chat window, ilagay ang iyong paksa sa pag-aaral at ang bilang ng linggo na nais mong pag-aralan (halimbawa, "AI-900 certification, 8 weeks").
4. Sasagutin ng app ng isang linggo-linggong plano ng pag-aaral, kasama ang mga link sa kaugnay na Microsoft Learn documentation.

**Mga Kinakailangang Environment Variables:**

Para magamit ang Senaryo 2 (ang Chainlit web app na may Azure OpenAI), kailangan mong itakda ang mga sumusunod na environment variables sa isang `.env` file in the `python` na direktoryo:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Punan ang mga ito ng detalye ng iyong Azure OpenAI resource bago patakbuhin ang app.

> **Tip:** Madali kang makakapag-deploy ng sarili mong mga modelo gamit ang [Azure AI Foundry](https://ai.azure.com/).

### Senaryo 3: In-Editor Docs gamit ang MCP Server sa VS Code

Sa halip na magpalipat-lipat sa browser tabs para maghanap ng dokumentasyon, maaari mong dalhin ang Microsoft Learn Docs diretso sa iyong VS Code gamit ang MCP server. Pinapahintulutan ka nitong:
- Maghanap at magbasa ng docs sa loob ng VS Code nang hindi umaalis sa iyong coding environment.
- Mag-refer ng dokumentasyon at maglagay ng mga link diretso sa iyong README o mga course file.
- Gamitin ang GitHub Copilot at MCP nang sabay para sa isang seamless, AI-powered na workflow sa dokumentasyon.

**Mga Halimbawa ng Paggamit:**
- Mabilis na magdagdag ng reference links sa README habang nagsusulat ng course o project documentation.
- Gamitin ang Copilot para gumawa ng code at MCP para agad na maghanap at mag-cite ng kaugnay na docs.
- Manatiling naka-focus sa iyong editor at pataasin ang produktibidad.

> [!IMPORTANT]
> Siguraduhing mayroon kang valid na [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

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

Ipinapakita ng mga halimbawang ito ang kakayahan ng app para sa iba't ibang layunin at tagal ng pag-aaral.

## Mga Sanggunian

- [Chainlit Documentation](https://docs.chainlit.io/)
- [MCP Documentation](https://github.com/MicrosoftDocs/mcp)

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami na maging tumpak, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang orihinal na wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.