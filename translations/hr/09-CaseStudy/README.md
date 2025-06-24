<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6940b1e931e51821b219aa9dcfe8c4ee",
  "translation_date": "2025-06-23T11:18:58+00:00",
  "source_file": "09-CaseStudy/README.md",
  "language_code": "hr"
}
-->
# MCP u praksi: Studije slučaja iz stvarnog svijeta

Model Context Protocol (MCP) mijenja način na koji AI aplikacije komuniciraju s podacima, alatima i uslugama. Ovaj odjeljak prikazuje stvarne primjere koji ilustriraju praktične primjene MCP-a u različitim poslovnim scenarijima.

## Pregled

Ovdje su prikazani konkretni primjeri implementacija MCP-a, naglašavajući kako organizacije koriste ovaj protokol za rješavanje složenih poslovnih izazova. Analizom ovih studija slučaja dobit ćete uvid u svestranost, skalabilnost i praktične prednosti MCP-a u stvarnim uvjetima.

## Ključni ciljevi učenja

Istražujući ove studije slučaja, naučit ćete:

- Kako se MCP može primijeniti za rješavanje specifičnih poslovnih problema
- Različite obrasce integracije i arhitektonske pristupe
- Najbolje prakse za implementaciju MCP-a u poslovnim okruženjima
- Izazove i rješenja s kojima se susreću stvarne implementacije
- Prilike za primjenu sličnih obrazaca u vlastitim projektima

## Istaknute studije slučaja

### 1. [Azure AI Travel Agents – Referentna implementacija](./travelagentsample.md)

Ova studija slučaja analizira Microsoftovo sveobuhvatno referentno rješenje koje pokazuje kako izgraditi aplikaciju za planiranje putovanja s više agenata, pokretanu AI-jem, koristeći MCP, Azure OpenAI i Azure AI Search. Projekt prikazuje:

- Orkestraciju više agenata putem MCP-a
- Integraciju podataka poduzeća s Azure AI Search
- Sigurnu i skalabilnu arhitekturu koristeći Azure usluge
- Proširive alate s ponovo upotrebljivim MCP komponentama
- Konverzacijsko korisničko iskustvo potpomognuto Azure OpenAI-em

Arhitektura i detalji implementacije pružaju vrijedne uvide u izgradnju složenih sustava s više agenata gdje MCP služi kao sloj koordinacije.

### 2. [Ažuriranje Azure DevOps stavki podacima s YouTubea](./UpdateADOItemsFromYT.md)

Ova studija slučaja prikazuje praktičnu primjenu MCP-a za automatizaciju radnih procesa. Pokazuje kako se MCP alati mogu koristiti za:

- Izvlačenje podataka s online platformi (YouTube)
- Ažuriranje radnih stavki u Azure DevOps sustavima
- Kreiranje ponovljivih automatiziranih tijekova rada
- Integraciju podataka između različitih sustava

Ovaj primjer ilustrira kako čak i relativno jednostavne implementacije MCP-a mogu donijeti značajna poboljšanja u učinkovitosti automatizacijom rutinskih zadataka i poboljšanjem dosljednosti podataka.

### 3. [Preuzimanje dokumentacije u stvarnom vremenu s MCP-om](./docs-mcp/README.md)

Ova studija slučaja vodi vas kroz povezivanje Python konzolnog klijenta s Model Context Protocol (MCP) serverom za dohvat i zapisivanje Microsoftove dokumentacije u stvarnom vremenu, prilagođene kontekstu. Naučit ćete kako:

- Povezati se na MCP server koristeći Python klijent i službeni MCP SDK
- Koristiti streaming HTTP klijente za učinkovito dohvaćanje podataka u stvarnom vremenu
- Pozivati alate za dokumentaciju na serveru i zapisivati odgovore direktno u konzolu
- Integrirati najnoviju Microsoftovu dokumentaciju u svoj radni tijek bez napuštanja terminala

Poglavlje uključuje praktični zadatak, minimalni radni primjer koda i poveznice na dodatne resurse za dublje učenje. Pogledajte cijeli vodič i kod u povezanom poglavlju kako biste razumjeli kako MCP može transformirati pristup dokumentaciji i produktivnost developera u konzolnim okruženjima.

### 4. [Interaktivna web aplikacija za generiranje plana učenja s MCP-om](./docs-mcp/README.md)

Ova studija slučaja pokazuje kako izgraditi interaktivnu web aplikaciju koristeći Chainlit i Model Context Protocol (MCP) za generiranje personaliziranih planova učenja za bilo koju temu. Korisnici mogu odabrati predmet (npr. "AI-900 certifikacija") i trajanje učenja (npr. 8 tjedana), a aplikacija pruža tjedni raspored preporučenog sadržaja. Chainlit omogućava konverzacijsko chat sučelje, čineći iskustvo zanimljivim i prilagodljivim.

- Konverzacijska web aplikacija pokretana Chainlit-om
- Korisnički upiti za odabir teme i trajanja
- Preporuke sadržaja po tjednima koristeći MCP
- Prilagodljivi odgovori u stvarnom vremenu kroz chat sučelje

Projekt ilustrira kako se konverzacijski AI i MCP mogu spojiti za stvaranje dinamičnih, korisnički vođenih edukativnih alata u suvremenom web okruženju.

### 5. [Dokumentacija unutar editora uz MCP server u VS Code-u](./docs-mcp/README.md)

Ova studija slučaja pokazuje kako možete integrirati Microsoft Learn Docs izravno u VS Code koristeći MCP server—bez potrebe za prebacivanjem na preglednik! Naučit ćete kako:

- Odmah pretraživati i čitati dokumentaciju unutar VS Code-a koristeći MCP panel ili naredbeni paletu
- Referencirati dokumentaciju i umetati poveznice direktno u README ili markdown datoteke tečaja
- Koristiti GitHub Copilot i MCP zajedno za besprijekorne AI-pokretane tokove rada s dokumentacijom i kodom
- Validirati i poboljšavati dokumentaciju uz povratne informacije u stvarnom vremenu i točnost iz Microsoft izvora
- Integrirati MCP s GitHub tokovima rada za kontinuiranu validaciju dokumentacije

Implementacija uključuje:
- Primjer `.vscode/mcp.json` konfiguracije za jednostavnu postavu
- Prikaze zaslona koji prikazuju iskustvo unutar editora
- Savjete za kombiniranje Copilota i MCP-a radi maksimalne produktivnosti

Ovaj scenarij idealan je za autore tečajeva, pisce dokumentacije i developere koji žele ostati fokusirani u svom editoru dok rade s dokumentacijom, Copilotom i alatima za validaciju—sve to uz podršku MCP-a.

### 6. [Izrada MCP servera u APIM-u](./apimsample.md)

Ova studija slučaja pruža korak-po-korak vodič za izradu MCP servera koristeći Azure API Management (APIM). Obuhvaća:

- Postavljanje MCP servera u Azure API Managementu
- Izlaganje API operacija kao MCP alata
- Konfiguriranje pravila za ograničavanje brzine i sigurnost
- Testiranje MCP servera koristeći Visual Studio Code i GitHub Copilot

Ovaj primjer pokazuje kako iskoristiti mogućnosti Azurea za stvaranje robusnog MCP servera koji se može koristiti u različitim aplikacijama, poboljšavajući integraciju AI sustava s poslovnim API-jima.

## Zaključak

Ove studije slučaja ističu svestranost i praktične primjene Model Context Protocola u stvarnim situacijama. Od složenih sustava s više agenata do ciljane automatizacije tijekova rada, MCP pruža standardizirani način povezivanja AI sustava s alatima i podacima potrebnima za isporuku vrijednosti.

Analizom ovih implementacija možete steći uvide u arhitektonske obrasce, strategije implementacije i najbolje prakse koje možete primijeniti u vlastitim MCP projektima. Primjeri pokazuju da MCP nije samo teorijski okvir, već praktično rješenje za stvarne poslovne izazove.

## Dodatni resursi

- [Azure AI Travel Agents GitHub repozitorij](https://github.com/Azure-Samples/azure-ai-travel-agents)
- [Azure DevOps MCP alat](https://github.com/microsoft/azure-devops-mcp)
- [Playwright MCP alat](https://github.com/microsoft/playwright-mcp)
- [Microsoft Docs MCP server](https://github.com/MicrosoftDocs/mcp)
- [MCP zajednički primjeri](https://github.com/microsoft/mcp)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako težimo točnosti, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati autoritativnim izvorom. Za kritične informacije preporučuje se profesionalni ljudski prijevod. Ne snosimo odgovornost za bilo kakva nesporazuma ili pogrešna tumačenja koja proizlaze iz korištenja ovog prijevoda.