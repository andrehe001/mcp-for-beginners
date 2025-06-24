<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:33:10+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "hr"
}
-->
# Generator plana učenja s Chainlit i Microsoft Learn Docs MCP

## Preduvjeti

- Python 3.8 ili noviji
- pip (Python upravitelj paketa)
- Pristup internetu za povezivanje s Microsoft Learn Docs MCP serverom

## Instalacija

1. Klonirajte ovaj repozitorij ili preuzmite datoteke projekta.
2. Instalirajte potrebne ovisnosti:

   ```bash
   pip install -r requirements.txt
   ```

## Korištenje

### Scenarij 1: Jednostavan upit prema Docs MCP
Klijent iz naredbenog retka koji se povezuje na Docs MCP server, šalje upit i ispisuje rezultat.

1. Pokrenite skriptu:
   ```bash
   python scenario1.py
   ```
2. Na upit unesite svoje pitanje vezano uz dokumentaciju.

### Scenarij 2: Generator plana učenja (Chainlit web aplikacija)
Web sučelje (koristeći Chainlit) koje korisnicima omogućuje izradu personaliziranog plana učenja tjedan po tjedan za bilo koju tehničku temu.

1. Pokrenite Chainlit aplikaciju:
   ```bash
   chainlit run scenario2.py
   ```
2. Otvorite lokalnu URL adresu prikazanu u terminalu (npr. http://localhost:8000) u pregledniku.
3. U chat prozoru unesite temu učenja i broj tjedana za koje želite učiti (npr. "AI-900 certification, 8 weeks").
4. Aplikacija će odgovoriti planom učenja tjedan po tjedan, uključujući poveznice na relevantnu Microsoft Learn dokumentaciju.

**Potrebne varijable okoline:**

Za korištenje Scenarija 2 (Chainlit web aplikacije s Azure OpenAI) potrebno je postaviti sljedeće varijable okoline u `.env` file in the `python` direktoriju:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Prije pokretanja aplikacije unesite svoje podatke o Azure OpenAI resursu.

> **[!TIP]** Lako možete implementirati vlastite modele koristeći [Azure AI Foundry](https://ai.azure.com/).

### Scenarij 3: Dokumentacija u editoru s MCP serverom u VS Code

Umjesto prebacivanja između kartica u pregledniku za pretraživanje dokumentacije, možete integrirati Microsoft Learn Docs izravno u VS Code koristeći MCP server. Ovo vam omogućuje da:
- Pretražujete i čitate dokumentaciju unutar VS Code bez napuštanja radnog okruženja.
- Referencirate dokumentaciju i umetnete poveznice direktno u README ili datoteke tečaja.
- Koristite GitHub Copilot i MCP zajedno za besprijekoran AI-podržan tijek rada s dokumentacijom.

**Primjeri korištenja:**
- Brzo dodajte referentne poveznice u README dok pišete dokumentaciju za tečaj ili projekt.
- Koristite Copilot za generiranje koda i MCP za trenutno pronalaženje i citiranje relevantne dokumentacije.
- Ostanite fokusirani u editoru i povećajte produktivnost.

> [!IMPORTANT]
> Provjerite imate li valjanu [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

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

Ovi primjeri pokazuju fleksibilnost aplikacije za različite ciljeve učenja i vremenske okvire.

## Reference

- [Chainlit dokumentacija](https://docs.chainlit.io/)
- [MCP dokumentacija](https://github.com/MicrosoftDocs/mcp)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću AI prevoditeljskog servisa [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za važne informacije preporučuje se profesionalni ljudski prijevod. Nismo odgovorni za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.