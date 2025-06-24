<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:32:33+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "sk"
}
-->
# Generátor študijného plánu s Chainlit & Microsoft Learn Docs MCP

## Požiadavky

- Python 3.8 alebo novší
- pip (správca balíčkov pre Python)
- Pripojenie na internet na prístup k serveru Microsoft Learn Docs MCP

## Inštalácia

1. Naklonujte si tento repozitár alebo si stiahnite súbory projektu.
2. Nainštalujte potrebné závislosti:

   ```bash
   pip install -r requirements.txt
   ```

## Použitie

### Scenár 1: Jednoduchý dopyt do Docs MCP  
Klient príkazového riadku, ktorý sa pripojí k serveru Docs MCP, odošle dopyt a vypíše výsledok.

1. Spustite skript:  
   ```bash
   python scenario1.py
   ```  
2. Zadajte svoju otázku ohľadom dokumentácie do výzvy.

### Scenár 2: Generátor študijného plánu (Chainlit webová aplikácia)  
Webové rozhranie (pomocou Chainlit), ktoré umožňuje používateľom vytvoriť si personalizovaný študijný plán na týždeň po týždni pre akúkoľvek technickú tému.

1. Spustite Chainlit aplikáciu:  
   ```bash
   chainlit run scenario2.py
   ```  
2. Otvorte lokálnu URL adresu, ktorá sa zobrazí v termináli (napr. http://localhost:8000), vo vašom prehliadači.  
3. V chatovacom okne zadajte tému štúdia a počet týždňov, počas ktorých chcete študovať (napr. „AI-900 certifikácia, 8 týždňov“).  
4. Aplikácia vám vráti študijný plán rozdelený po týždňoch vrátane odkazov na relevantnú dokumentáciu Microsoft Learn.

**Požadované premenné prostredia:**  

Na použitie Scenára 2 (Chainlit webová aplikácia s Azure OpenAI) musíte nastaviť nasledujúce premenné prostredia v súbore `.env` file in the `python`:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Vyplňte tieto hodnoty podľa údajov vášho Azure OpenAI zdroja pred spustením aplikácie.

> **Tip:** Jednoducho si môžete nasadiť vlastné modely pomocou [Azure AI Foundry](https://ai.azure.com/).

### Scenár 3: Dokumentácia v editore s MCP serverom vo VS Code

Namiesto prepínania kariet v prehliadači na vyhľadávanie dokumentácie môžete mať Microsoft Learn Docs priamo vo VS Code pomocou MCP servera. To vám umožní:  
- Vyhľadávať a čítať dokumentáciu priamo vo VS Code bez opustenia vývojového prostredia.  
- Odkazovať na dokumentáciu a vkladať odkazy priamo do README alebo súborov kurzu.  
- Používať GitHub Copilot a MCP spoločne pre plynulý, AI podporený pracovný tok s dokumentáciou.

**Príklady použitia:**  
- Rýchlo pridať referenčné odkazy do README počas písania kurzu alebo projektovej dokumentácie.  
- Použiť Copilot na generovanie kódu a MCP na okamžité vyhľadanie a citovanie relevantnej dokumentácie.  
- Zostať sústredený v editore a zvýšiť svoju produktivitu.

> [!IMPORTANT]  
> Uistite sa, že máte platný [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

## Why Chainlit for Scenario 2?

Chainlit is a modern open-source framework for building conversational web applications. It makes it easy to create chat-based user interfaces that connect to backend services like the Microsoft Learn Docs MCP server. This project uses Chainlit to provide a simple, interactive way to generate personalized study plans in real time. By leveraging Chainlit, you can quickly build and deploy chat-based tools that enhance productivity and learning.

## What This Does

This app allows users to create a personalized study plan by simply entering a topic and a duration. The app parses your input, queries the Microsoft Learn Docs MCP server for relevant content, and organizes the results into a structured, week-by-week plan. Each week’s recommendations are displayed in the chat, making it easy to follow and track your progress. The integration ensures you always get the latest, most relevant learning resources.

## Sample Queries

Try these queries in the chat window to see how the app responds:

- `AI-900 certifikácia, 8 týždňov`
- `Learn Azure Functions, 4 týždne`
- `Azure DevOps, 6 týždňov`
- `Data engineering on Azure, 10 týždňov`
- `Microsoft security fundamentals, 5 týždňov`
- `Power Platform, 7 týždňov`
- `Azure AI services, 12 týždňov`
- `Cloud architecture, 9 týždňov`

Tieto príklady ukazujú flexibilitu aplikácie pre rôzne študijné ciele a časové rámce.

## Referencie

- [Chainlit dokumentácia](https://docs.chainlit.io/)  
- [MCP dokumentácia](https://github.com/MicrosoftDocs/mcp)

**Vyhlásenie o zodpovednosti**:  
Tento dokument bol preložený pomocou AI prekladateľskej služby [Co-op Translator](https://github.com/Azure/co-op-translator). Aj keď sa snažíme o presnosť, majte prosím na pamäti, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Originálny dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nie sme zodpovední za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.