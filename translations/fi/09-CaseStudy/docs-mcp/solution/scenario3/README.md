<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "db532b1ec386c9ce38c791653dc3c881",
  "translation_date": "2025-06-21T14:41:01+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/scenario3/README.md",
  "language_code": "fi"
}
-->
# Scenario 3: In-Editor Docs with MCP Server in VS Code

## Yleiskatsaus

Tässä skenaariossa opit, miten voit tuoda Microsoft Learn -dokumentaation suoraan Visual Studio Code -ympäristöösi MCP-palvelimen avulla. Sen sijaan, että vaihtaisit jatkuvasti selaimen välilehtiä dokumentaatiota etsiessäsi, voit käyttää, hakea ja viitata virallisiin dokumentteihin suoraan editorissasi. Tämä tapa tehostaa työskentelyäsi, auttaa sinua pysymään keskittyneenä ja mahdollistaa saumattoman integraation esimerkiksi GitHub Copilotin kanssa.

- Hae ja lue dokumentaatiota VS Codessa ilman, että poistut koodausympäristöstäsi.
- Viittaa dokumentaatioon ja lisää linkkejä suoraan README- tai kurssitiedostoihisi.
- Käytä GitHub Copilotia ja MCP:tä yhdessä sujuvaan, tekoälyavusteiseen dokumentaatiotyöskentelyyn.

## Oppimistavoitteet

Tämän luvun lopussa osaat ottaa MCP-palvelimen käyttöön VS Codessa ja hyödyntää sitä dokumentaatio- ja kehitysprosessissasi. Osaat:

- Määrittää työtilasi käyttämään MCP-palvelinta dokumentaation hakemiseen.
- Hakea ja lisätä dokumentaatiota suoraan VS Codesta.
- Yhdistää GitHub Copilotin ja MCP:n voimat tehokkaampaan, tekoälyavusteiseen työnkulkuun.

Nämä taidot auttavat sinua pysymään keskittyneenä, parantamaan dokumentaation laatua ja lisäämään tuottavuuttasi kehittäjänä tai teknisenä kirjoittajana.

## Ratkaisu

Saavuttaaksesi editorissa tapahtuvan dokumentaation käytön, seuraat sarjaa vaiheita, jotka yhdistävät MCP-palvelimen VS Coden ja GitHub Copilotin kanssa. Tämä ratkaisu sopii erinomaisesti kurssien tekijöille, dokumentaation kirjoittajille ja kehittäjille, jotka haluavat pysyä keskittyneinä editorissa työskennellessään dokumentaation ja Copilotin kanssa.

- Lisää nopeasti viittauslinkkejä README-tiedostoon kirjoittaessasi kurssia tai projektidokumentaatiota.
- Käytä Copilotia koodin generointiin ja MCP:tä löytääksesi ja viitataksesi relevantteihin dokumentteihin välittömästi.
- Pysy keskittyneenä editorissasi ja lisää tuottavuuttasi.

### Vaihe vaiheelta -opas

Aloittaaksesi seuraa näitä ohjeita. Voit lisätä kuhunkin vaiheeseen kuvakaappauksen assets-kansiosta havainnollistamaan prosessia.

1. **Lisää MCP-konfiguraatio:**
   Luo projektisi juureen `.vscode/mcp.json`-tiedosto ja lisää siihen seuraava konfiguraatio:
   ```json
   {
     "servers": {
       "LearnDocsMCP": {
         "url": "https://learn.microsoft.com/api/mcp"
       }
     }
   }
   ```
   Tämä määritys kertoo VS Codelle, miten se yhdistää [`Microsoft Learn Docs MCP serveriin`](https://github.com/MicrosoftDocs/mcp).
   
   ![Vaihe 1: Lisää mcp.json .vscode-kansioon](../../../../../../translated_images/step1-mcp-json.c06a007fccc3edfaf0598a31903c9ec71476d9fd3ae6c1b2b4321fd38688ca4b.fi.png)
    
2. **Avaa GitHub Copilot Chat -paneeli:**
   Jos sinulla ei vielä ole GitHub Copilot -laajennusta asennettuna, siirry VS Coden Extensions-näkymään ja asenna se. Voit ladata sen suoraan [Visual Studio Code Marketplacesta](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat). Avaa sitten Copilot Chat -paneeli sivupalkista.

   ![Vaihe 2: Avaa Copilot Chat -paneeli](../../../../../../translated_images/step2-copilot-panel.f1cc86e9b9b8cd1a85e4df4923de8bafee4830541ab255e3c90c09777fed97db.fi.png)

3. **Ota agenttitila käyttöön ja varmista työkalut:**
   Ota Copilot Chat -paneelissa agenttitila käyttöön.

   ![Vaihe 3: Ota agenttitila käyttöön ja varmista työkalut](../../../../../../translated_images/step3-agent-mode.cdc32520fd7dd1d149c3f5226763c1d85a06d3c041d4cc983447625bdbeff4d4.fi.png)

   Agenttitilan aktivoimisen jälkeen varmista, että MCP-palvelin näkyy käytettävissä olevien työkalujen listalla. Tämä varmistaa, että Copilot-agentti pääsee käsiksi dokumentaatiopalvelimeen hakemaan relevanttia tietoa.
   
   ![Vaihe 3: Varmista MCP-palvelintyökalu](../../../../../../translated_images/step3-verify-mcp-tool.76096a6329cbfecd42888780f322370a0d8c8fa003ed3eeb7ccd23f0fc50c1ad.fi.png)
4. **Aloita uusi keskustelu ja ohjaa agenttia:**
   Avaa uusi keskustelu Copilot Chat -paneelissa. Voit nyt esittää agentille dokumentaatiokysymyksiä. Agentti käyttää MCP-palvelinta noutaakseen ja näyttääksesi relevanttia Microsoft Learn -dokumentaatiota suoraan editorissasi.

   - *"Yritän laatia opintosuunnitelmaa aiheelle X. Opiskelen sitä 8 viikkoa, ehdota kullekin viikolle sopivaa sisältöä."*

   ![Vaihe 4: Ohjaa agenttia keskustelussa](../../../../../../translated_images/step4-prompt-chat.12187bb001605efc5077992b621f0fcd1df12023c5dce0464f8eb8f3d595218f.fi.png)

5. **Live-kysely:**

   > Otetaanpa live-kysely [#get-help](https://discord.gg/D6cRhjHWSC) -kanavalta Azure AI Foundry Discordissa ([katso alkuperäinen viesti](https://discord.com/channels/1113626258182504448/1385498306720829572)):
   
   *"Etsin vastauksia siihen, miten moniagenttiratkaisu otetaan käyttöön Azure AI Foundryssa kehitettyjen AI-agenttien kanssa. Huomaan, ettei suoraa käyttöönottoa ole, kuten Copilot Studio -kanavia. Mitkä ovat eri tavat toteuttaa käyttöönotto yrityskäyttäjille, jotta he voivat olla vuorovaikutuksessa ja saada työn tehtyä?
Useita artikkeleita/blogeja väittää, että Azure Bot -palvelua voisi käyttää siltana MS Teamsin ja Azure AI Foundryn agenttien välillä. Toimiiko tämä, jos asennan Azure-botin, joka yhdistyy Orchestrator Agenttiin Azure AI Foundryssa Azure Functionin kautta orkestrointia varten, vai täytyykö luoda Azure Function jokaiselle moniagenttiratkaisuun kuuluvalle AI-agentille orkestroinnin tekemiseksi Bot Frameworkissa? Kaikki muut ehdotukset ovat tervetulleita."*

   ![Vaihe 5: Live-kyselyt](../../../../../../translated_images/step5-live-queries.49db3e4a50bea27327e3cb18c24d263b7d134930d78e7392f9515a1c00264a7f.fi.png)

   Agentti vastaa asiaankuuluvilla dokumentaatio-linkeillä ja yhteenvetoilla, jotka voit sitten lisätä suoraan markdown-tiedostoihisi tai käyttää viitteinä koodissasi.

### Esimerkkikyselyt

Tässä muutamia esimerkkikyselyjä, joita voit kokeilla. Näiden avulla näet, miten MCP-palvelin ja Copilot toimivat yhdessä tarjoten välitöntä, kontekstin mukaista dokumentaatiota ja viitteitä ilman, että sinun tarvitsee poistua VS Codesta:

- "Näytä, miten käytetään Azure Functions -triggeröitä."
- "Lisää linkki Azure Key Vaultin viralliseen dokumentaatioon."
- "Mitkä ovat parhaat käytännöt Azure-resurssien suojaamiseen?"
- "Löydä pikaopas Azure AI -palveluihin."

Nämä kyselyt demonstroivat, miten MCP-palvelin ja Copilot voivat yhdessä tarjota välitöntä, kontekstin mukaista dokumentaatiota ja viitteitä ilman, että poistut VS Codesta.

---

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulee pitää virallisena lähteenä. Tärkeissä asioissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tästä käännöksestä aiheutuvista väärinkäsityksistä tai tulkinnoista.