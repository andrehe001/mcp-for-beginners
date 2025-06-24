<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:33:19+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "sl"
}
-->
# Generator študijskega načrta s Chainlit in Microsoft Learn Docs MCP

## Zahteve

- Python 3.8 ali novejši
- pip (upravljalnik paketov za Python)
- Dostop do interneta za povezavo s strežnikom Microsoft Learn Docs MCP

## Namestitev

1. Klonirajte ta repozitorij ali prenesite datoteke projekta.
2. Namestite potrebne odvisnosti:

   ```bash
   pip install -r requirements.txt
   ```

## Uporaba

### Scenarij 1: Enostavno poizvedovanje v Docs MCP
Ukazna vrstica, ki se poveže s strežnikom Docs MCP, pošlje poizvedbo in izpiše rezultat.

1. Zaženite skripto:
   ```bash
   python scenario1.py
   ```
2. Vnesite vprašanje glede dokumentacije, ko vas sistem pozove.

### Scenarij 2: Generator študijskega načrta (Chainlit spletna aplikacija)
Spletni vmesnik (z uporabo Chainlit), ki uporabnikom omogoča ustvarjanje osebnega tedenskega študijskega načrta za katero koli tehnično temo.

1. Zaženite aplikacijo Chainlit:
   ```bash
   chainlit run scenario2.py
   ```
2. Odprite lokalni URL, ki ga vidite v terminalu (npr. http://localhost:8000) v svojem brskalniku.
3. V oknu klepeta vnesite temo študija in število tednov, koliko želite študirati (npr. "AI-900 certification, 8 weeks").
4. Aplikacija bo odgovorila z načrtom študija po tednih, vključno s povezavami do ustrezne Microsoft Learn dokumentacije.

**Zahtevane okoljske spremenljivke:**

Za uporabo Scenarija 2 (Chainlit spletna aplikacija z Azure OpenAI) morate v mapi `.env` file in the `python` nastaviti naslednje okoljske spremenljivke:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Izpolnite te vrednosti z vašimi podatki o Azure OpenAI viru, preden zaženete aplikacijo.

> **Namig:** Svoje modele lahko enostavno namestite z uporabo [Azure AI Foundry](https://ai.azure.com/).

### Scenarij 3: Dokumentacija v urejevalniku z MCP strežnikom v VS Code

Namesto preklapljanja med zavihki v brskalniku za iskanje dokumentacije lahko Microsoft Learn Docs neposredno vključite v VS Code s pomočjo MCP strežnika. To vam omogoča:
- Iskanje in branje dokumentacije neposredno v VS Code brez zapuščanja razvojnega okolja.
- Vstavljanje referenčnih povezav neposredno v README ali datoteke tečajev.
- Uporabo GitHub Copilot in MCP skupaj za tekoče delo z dokumentacijo, podprto z umetno inteligenco.

**Primeri uporabe:**
- Hitro dodajte referenčne povezave v README med pisanjem dokumentacije za tečaj ali projekt.
- Uporabite Copilot za generiranje kode in MCP za takojšnje iskanje in citiranje ustrezne dokumentacije.
- Osredotočite se na delo v urejevalniku in povečajte produktivnost.

> [!IMPORTANT]
> Prepričajte se, da imate veljavno [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

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

Ti primeri prikazujejo prilagodljivost aplikacije za različne učne cilje in časovne okvire.

## Viri

- [Chainlit Dokumentacija](https://docs.chainlit.io/)
- [MCP Dokumentacija](https://github.com/MicrosoftDocs/mcp)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo AI prevajalske storitve [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za morebitne nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne prevzemamo odgovornosti.