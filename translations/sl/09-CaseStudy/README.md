<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6940b1e931e51821b219aa9dcfe8c4ee",
  "translation_date": "2025-06-23T11:19:30+00:00",
  "source_file": "09-CaseStudy/README.md",
  "language_code": "sl"
}
-->
# MCP v praksi: primeri iz resničnega sveta

Model Context Protocol (MCP) spreminja način, kako AI aplikacije komunicirajo s podatki, orodji in storitvami. Ta razdelek predstavlja primere iz resničnega sveta, ki prikazujejo praktične uporabe MCP v različnih poslovnih okoljih.

## Pregled

V tem razdelku so predstavljeni konkretni primeri implementacij MCP, ki poudarjajo, kako organizacije izkoriščajo ta protokol za reševanje zahtevnih poslovnih izzivov. Z analizo teh primerov boste pridobili vpogled v vsestranskost, razširljivost in praktične koristi MCP v resničnih situacijah.

## Ključni cilji učenja

Z raziskovanjem teh primerov boste:

- razumeli, kako se MCP lahko uporabi za reševanje specifičnih poslovnih problemov
- spoznali različne vzorce integracije in arhitekturne pristope
- prepoznali najboljše prakse za implementacijo MCP v poslovnih okoljih
- pridobili vpogled v izzive in rešitve, s katerimi se srečujejo pri implementacijah v resničnem svetu
- odkrili priložnosti za uporabo podobnih vzorcev v svojih projektih

## Izbrani primeri

### 1. [Azure AI Travel Agents – referenčna implementacija](./travelagentsample.md)

Ta primer raziskuje Microsoftovo celovito referenčno rešitev, ki prikazuje, kako z uporabo MCP, Azure OpenAI in Azure AI Search zgraditi večagentno aplikacijo za načrtovanje potovanj, podprto z umetno inteligenco. Projekt prikazuje:

- večagentno orkestracijo prek MCP
- integracijo poslovnih podatkov z Azure AI Search
- varno in razširljivo arhitekturo z uporabo Azure storitev
- razširljive pripomočke z znova uporabnimi MCP komponentami
- pogovorno uporabniško izkušnjo, ki jo poganja Azure OpenAI

Arhitektura in podrobnosti implementacije nudijo dragocene vpoglede v gradnjo zapletenih večagentnih sistemov z MCP kot koordinacijsko plastjo.

### 2. [Posodabljanje Azure DevOps elementov z YouTube podatki](./UpdateADOItemsFromYT.md)

Ta primer prikazuje praktično uporabo MCP za avtomatizacijo delovnih procesov. Prikazuje, kako lahko MCP orodja uporabimo za:

- pridobivanje podatkov z spletnih platform (YouTube)
- posodabljanje delovnih elementov v sistemih Azure DevOps
- ustvarjanje ponovljivih avtomatiziranih delovnih tokov
- integracijo podatkov med različnimi sistemi

Primer kaže, kako lahko že razmeroma preproste implementacije MCP prinesejo pomembne izboljšave učinkovitosti z avtomatizacijo rutinskih opravil in izboljšanjem konsistence podatkov med sistemi.

### 3. [Pridobivanje dokumentacije v realnem času z MCP](./docs-mcp/README.md)

Ta primer vas vodi skozi povezavo Python konzolnega odjemalca z MCP strežnikom za pridobivanje in beleženje Microsoftove dokumentacije v realnem času, prilagojene kontekstu. Naučili se boste, kako:

- se povezati z MCP strežnikom z uporabo Python odjemalca in uradnega MCP SDK
- uporabljati pretočne HTTP odjemalce za učinkovito pridobivanje podatkov v realnem času
- klicati orodja za dokumentacijo na strežniku in neposredno beležiti odzive v konzolo
- vključiti najnovejšo Microsoftovo dokumentacijo v svoj delovni tok brez zapuščanja terminala

Poglavje vsebuje praktično nalogo, minimalen delujoč primer kode in povezave do dodatnih virov za poglobljeno učenje. Oglejte si celoten vodič in kodo v povezanem poglavju, da razumete, kako lahko MCP spremeni dostop do dokumentacije in produktivnost razvijalcev v konzolnem okolju.

### 4. [Interaktivna spletna aplikacija za generiranje študijskega načrta z MCP](./docs-mcp/README.md)

Ta primer prikazuje, kako z uporabo Chainlit in Model Context Protocol (MCP) zgraditi interaktivno spletno aplikacijo za ustvarjanje personaliziranih študijskih načrtov za katerokoli temo. Uporabniki lahko določijo predmet (npr. "certifikat AI-900") in čas trajanja študija (npr. 8 tednov), aplikacija pa nato ponudi tedenski pregled priporočene vsebine. Chainlit omogoča pogovorni klepet, zaradi česar je izkušnja zanimiva in prilagodljiva.

- pogovorna spletna aplikacija, ki jo poganja Chainlit
- uporabniški pozivi za izbiro teme in trajanja
- tedenske priporočene vsebine z uporabo MCP
- odzivi v realnem času v klepetalnem vmesniku

Projekt prikazuje, kako lahko združimo pogovorno AI in MCP za ustvarjanje dinamičnih, uporabniško usmerjenih izobraževalnih orodij v sodobnem spletnem okolju.

### 5. [Dokumentacija v urejevalniku z MCP strežnikom v VS Code](./docs-mcp/README.md)

Ta primer prikazuje, kako lahko Microsoft Learn Docs neposredno vključite v okolje VS Code z uporabo MCP strežnika – brez preklapljanja med zavihki brskalnika! Videli boste, kako:

- takoj iskati in brati dokumentacijo znotraj VS Code preko MCP panela ali ukazne palete
- sklicevati se na dokumentacijo in vstavljati povezave neposredno v README ali markdown datoteke tečajev
- uporabljati GitHub Copilot in MCP skupaj za nemotene delovne tokove z dokumentacijo in kodo, podprte z AI
- preverjati in izboljševati dokumentacijo z realnočasovnim povratnim informacijam in Microsoftovo natančnostjo
- integrirati MCP z GitHub delovnimi tokovi za kontinuirano validacijo dokumentacije

Implementacija vključuje:
- primer `.vscode/mcp.json` konfiguracije za enostavno nastavitev
- prikaze zaslona za vodenje skozi izkušnjo znotraj urejevalnika
- nasvete za kombiniranje Copilota in MCP za največjo produktivnost

Ta scenarij je idealen za avtorje tečajev, pisce dokumentacije in razvijalce, ki želijo ostati osredotočeni v urejevalniku med delom z dokumentacijo, Copilotom in orodji za validacijo – vse podprto z MCP.

### 6. [Ustvarjanje MCP strežnika z APIM](./apimsample.md)

Ta primer ponuja korak za korakom vodič, kako ustvariti MCP strežnik z uporabo Azure API Management (APIM). Pokriva:

- postavitev MCP strežnika v Azure API Management
- izpostavljanje API operacij kot MCP orodij
- konfiguracijo pravil za omejevanje hitrosti in varnost
- testiranje MCP strežnika z uporabo Visual Studio Code in GitHub Copilot

Primer prikazuje, kako izkoristiti zmogljivosti Azure za ustvarjanje robustnega MCP strežnika, ki ga je mogoče uporabiti v različnih aplikacijah in izboljšati integracijo AI sistemov z API-ji podjetij.

## Zaključek

Ti primeri izpostavljajo vsestranskost in praktične uporabe Model Context Protocol v resničnih scenarijih. Od zapletenih večagentnih sistemov do ciljno usmerjenih avtomatiziranih delovnih tokov, MCP zagotavlja standardiziran način povezovanja AI sistemov z orodji in podatki, ki jih potrebujejo za ustvarjanje vrednosti.

S preučevanjem teh implementacij lahko pridobite vpoglede v arhitekturne vzorce, strategije izvedbe in najboljše prakse, ki jih lahko uporabite v svojih MCP projektih. Primeri dokazujejo, da MCP ni le teoretični okvir, temveč praktična rešitev za resnične poslovne izzive.

## Dodatni viri

- [Azure AI Travel Agents GitHub repozitorij](https://github.com/Azure-Samples/azure-ai-travel-agents)
- [Azure DevOps MCP orodje](https://github.com/microsoft/azure-devops-mcp)
- [Playwright MCP orodje](https://github.com/microsoft/playwright-mcp)
- [Microsoft Docs MCP strežnik](https://github.com/MicrosoftDocs/mcp)
- [MCP skupnostni primeri](https://github.com/microsoft/mcp)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za pomembne informacije priporočamo strokovni človeški prevod. Za kakršne koli nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda, ne odgovarjamo.