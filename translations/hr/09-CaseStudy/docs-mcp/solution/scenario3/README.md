<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "db532b1ec386c9ce38c791653dc3c881",
  "translation_date": "2025-06-21T14:44:36+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/scenario3/README.md",
  "language_code": "hr"
}
-->
# Scenarij 3: Dokumentacija u uređivaču s MCP serverom u VS Code-u

## Pregled

U ovom scenariju naučit ćete kako Microsoft Learn dokumentaciju dovesti izravno u vaše Visual Studio Code okruženje pomoću MCP servera. Umjesto stalnog prebacivanja između kartica u pregledniku kako biste tražili dokumentaciju, možete pristupati, pretraživati i referencirati službene dokumente izravno unutar uređivača. Ovaj pristup pojednostavljuje vaš radni tijek, pomaže vam da ostanete usredotočeni i omogućuje besprijekornu integraciju s alatima poput GitHub Copilota.

- Pretražujte i čitajte dokumentaciju unutar VS Code-a bez napuštanja okruženja za kodiranje.
- Referencirajte dokumentaciju i umetnite poveznice izravno u README ili datoteke tečaja.
- Koristite GitHub Copilot i MCP zajedno za besprijekoran radni tijek s AI podrškom za dokumentaciju.

## Ciljevi učenja

Do kraja ovog poglavlja razumjet ćete kako postaviti i koristiti MCP server unutar VS Code-a kako biste unaprijedili svoj radni tijek dokumentacije i razvoja. Moći ćete:

- Konfigurirati svoje radno okruženje za korištenje MCP servera za pretraživanje dokumentacije.
- Pretraživati i umetati dokumentaciju izravno unutar VS Code-a.
- Kombinirati snagu GitHub Copilota i MCP-a za produktivniji radni tijek uz AI podršku.

Ove vještine pomoći će vam da ostanete usredotočeni, poboljšate kvalitetu dokumentacije i povećate produktivnost kao programer ili tehnički pisac.

## Rješenje

Da biste omogućili pristup dokumentaciji u uređivaču, slijedit ćete niz koraka koji integriraju MCP server s VS Code-om i GitHub Copilotom. Ovo rješenje je idealno za autore tečajeva, pisce dokumentacije i programere koji žele zadržati fokus u uređivaču dok rade s dokumentima i Copilotom.

- Brzo dodajte referentne poveznice u README dok pišete dokumentaciju za tečaj ili projekt.
- Koristite Copilot za generiranje koda i MCP za trenutno pronalaženje i citiranje relevantne dokumentacije.
- Ostanite usredotočeni u uređivaču i povećajte produktivnost.

### Vodič korak po korak

Za početak slijedite ove korake. Za svaki korak možete dodati snimku zaslona iz mape assets kako biste vizualno ilustrirali postupak.

1. **Dodajte MCP konfiguraciju:**  
   U korijenu projekta kreirajte datoteku `.vscode/mcp.json` i dodajte sljedeću konfiguraciju:  
   ```json
   {
     "servers": {
       "LearnDocsMCP": {
         "url": "https://learn.microsoft.com/api/mcp"
       }
     }
   }
   ```  
   Ova konfiguracija govori VS Code-u kako se povezati s [`Microsoft Learn Docs MCP serverom`](https://github.com/MicrosoftDocs/mcp).

   ![Korak 1: Dodajte mcp.json u .vscode mapu](../../../../../../translated_images/step1-mcp-json.c06a007fccc3edfaf0598a31903c9ec71476d9fd3ae6c1b2b4321fd38688ca4b.hr.png)
    
2. **Otvorite GitHub Copilot Chat panel:**  
   Ako još nemate instaliran GitHub Copilot dodatak, otvorite pregled dodataka u VS Code-u i instalirajte ga. Možete ga preuzeti izravno s [Visual Studio Code Marketplacea](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat). Zatim otvorite Copilot Chat panel sa bočne trake.

   ![Korak 2: Otvorite Copilot Chat panel](../../../../../../translated_images/step2-copilot-panel.f1cc86e9b9b8cd1a85e4df4923de8bafee4830541ab255e3c90c09777fed97db.hr.png)

3. **Omogućite agent mode i provjerite alate:**  
   U Copilot Chat panelu uključite agent mode.

   ![Korak 3: Omogućite agent mode i provjerite alate](../../../../../../translated_images/step3-agent-mode.cdc32520fd7dd1d149c3f5226763c1d85a06d3c041d4cc983447625bdbeff4d4.hr.png)

   Nakon uključivanja agent mode, provjerite je li MCP server naveden kao jedan od dostupnih alata. Time se osigurava da Copilot agent može pristupiti dokumentacijskom serveru i dohvatiti relevantne informacije.

   ![Korak 3: Provjerite MCP server alat](../../../../../../translated_images/step3-verify-mcp-tool.76096a6329cbfecd42888780f322370a0d8c8fa003ed3eeb7ccd23f0fc50c1ad.hr.png)

4. **Započnite novi chat i postavite upit agentu:**  
   Otvorite novi chat u Copilot Chat panelu. Sada možete postavljati agentu pitanja vezana uz dokumentaciju. Agent će koristiti MCP server za dohvat i prikaz relevantne Microsoft Learn dokumentacije izravno u vašem uređivaču.

   - *"Pokušavam napisati plan učenja za temu X. Planiram učiti 8 tjedana, za svaki tjedan predloži sadržaj koji bih trebao obraditi."*

   ![Korak 4: Postavite upit agentu u chatu](../../../../../../translated_images/step4-prompt-chat.12187bb001605efc5077992b621f0fcd1df12023c5dce0464f8eb8f3d595218f.hr.png)

5. **Live Query:**  

   > Pogledajmo jedan stvarni upit iz [#get-help](https://discord.gg/D6cRhjHWSC) sekcije u Azure AI Foundry Discordu ([pogledaj originalnu poruku](https://discord.com/channels/1113626258182504448/1385498306720829572)):

   *"Tražim odgovore kako implementirati multi-agent rješenje s AI agentima razvijenim na Azure AI Foundry platformi. Vidim da ne postoji direktna metoda implementacije, poput Copilot Studio kanala. Koji su različiti načini za ovu implementaciju kako bi korisnici u poduzeću mogli međusobno surađivati i obaviti posao?  
Postoji mnogo članaka/blogova koji tvrde da se može koristiti Azure Bot servis kao most između MS Teamsa i Azure AI Foundry agenata. Hoće li to funkcionirati ako postavim Azure bota koji se povezuje na Orchestrator Agenta u Azure AI Foundry preko Azure funkcije za orkestraciju ili trebam kreirati Azure funkciju za svakog AI agenta unutar multi-agent rješenja da bi orkestracija funkcionirala u Bot frameworku? Svaki drugi prijedlog je dobrodošao."*

   ![Korak 5: Live upiti](../../../../../../translated_images/step5-live-queries.49db3e4a50bea27327e3cb18c24d263b7d134930d78e7392f9515a1c00264a7f.hr.png)

   Agent će odgovoriti s relevantnim poveznicama na dokumentaciju i sažecima koje zatim možete izravno umetnuti u svoje markdown datoteke ili koristiti kao reference u kodu.

### Primjeri upita

Evo nekoliko primjera upita koje možete isprobati. Ovi upiti pokazuju kako MCP server i Copilot mogu zajedno pružiti brzu, kontekstualno relevantnu dokumentaciju i reference bez napuštanja VS Code-a:

- "Pokaži mi kako koristiti Azure Functions okidače."
- "Umetni poveznicu na službenu dokumentaciju za Azure Key Vault."
- "Koje su najbolje prakse za osiguranje Azure resursa?"
- "Pronađi quickstart za Azure AI usluge."

Ovi upiti demonstriraju kako MCP server i Copilot mogu raditi zajedno i omogućiti trenutačnu, kontekstualno osviještenu dokumentaciju i reference unutar VS Code-a.

---

**Odricanje od odgovornosti**:  
Ovaj dokument preveden je korištenjem AI usluge prevođenja [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za važne informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakve nesporazume ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.