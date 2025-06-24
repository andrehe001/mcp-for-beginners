<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:30:51+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "fi"
}
-->
# Opintosuunnitelman generaattori Chainlitin ja Microsoft Learn Docs MCP:n avulla

## Esivaatimukset

- Python 3.8 tai uudempi
- pip (Python-pakettien hallintaohjelma)
- Internet-yhteys Microsoft Learn Docs MCP -palvelimeen yhdistämistä varten

## Asennus

1. Kloonaa tämä repositorio tai lataa projektin tiedostot.
2. Asenna tarvittavat riippuvuudet:

   ```bash
   pip install -r requirements.txt
   ```

## Käyttö

### Tilanne 1: Yksinkertainen kysely Docs MCP:lle
Komentoriviasiakas, joka yhdistää Docs MCP -palvelimeen, lähettää kyselyn ja tulostaa tuloksen.

1. Suorita skripti:
   ```bash
   python scenario1.py
   ```
2. Kirjoita dokumentaatiokysymyksesi kehotteeseen.

### Tilanne 2: Opintosuunnitelman generaattori (Chainlit-verkkosovellus)
Verkkopohjainen käyttöliittymä (Chainlitin avulla), jonka kautta käyttäjät voivat luoda henkilökohtaisen, viikko kerrallaan etenevän opintosuunnitelman mille tahansa tekniselle aiheelle.

1. Käynnistä Chainlit-sovellus:
   ```bash
   chainlit run scenario2.py
   ```
2. Avaa terminaalissa näkyvä paikallinen URL-osoite (esim. http://localhost:8000) selaimessasi.
3. Kirjoita chat-ikkunaan opiskeluaiheesi ja haluamiesi viikkojen määrä (esim. "AI-900 certification, 8 weeks").
4. Sovellus vastaa viikko kerrallaan etenevällä opintosuunnitelmalla, joka sisältää linkkejä asiaankuuluviin Microsoft Learn -dokumentaatiosivuihin.

**Vaaditut ympäristömuuttujat:**

Käyttääksesi tilannetta 2 (Chainlit-verkkosovellus Azure OpenAI:n kanssa), sinun tulee määrittää seuraavat ympäristömuuttujat `.env` file in the `python`-hakemistossa:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Täytä nämä tiedot omien Azure OpenAI -resurssiesi tiedoilla ennen sovelluksen käynnistämistä.

> **Vinkki:** Voit helposti ottaa käyttöön omia mallejasi käyttämällä [Azure AI Foundryä](https://ai.azure.com/).

### Tilanne 3: Dokumentaatio MCP-palvelimella suoraan VS Codessa

Sen sijaan, että vaihtaisit selaimen välilehteä dokumentaation hakemiseksi, voit tuoda Microsoft Learn Docs -sisällön suoraan VS Codeen MCP-palvelimen avulla. Tämä mahdollistaa:
- Dokumentaation hakemisen ja lukemisen VS Codessa ilman, että sinun tarvitsee poistua koodausympäristöstäsi.
- Dokumentaation viittausten lisäämisen ja linkkien upottamisen suoraan README- tai kurssitiedostoihin.
- GitHub Copilotin ja MCP:n yhteiskäytön sujuvan, tekoälyä hyödyntävän dokumentaatiotyönkulun luomiseksi.

**Esimerkkikäyttötapaukset:**
- Lisää nopeasti viittauslinkkejä README-tiedostoon kurssin tai projektin dokumentaatiota kirjoittaessasi.
- Käytä Copilotia koodin luomiseen ja MCP:tä löytämään ja lainaamaan relevantteja dokumentaatiosivuja välittömästi.
- Pysy keskittyneenä editorissasi ja lisää tuottavuutta.

> [!IMPORTANT]
> Varmista, että sinulla on voimassa oleva [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

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

Nämä esimerkit osoittavat sovelluksen joustavuuden erilaisiin oppimistavoitteisiin ja aikatauluihin.

## Viitteet

- [Chainlit Documentation](https://docs.chainlit.io/)
- [MCP Documentation](https://github.com/MicrosoftDocs/mcp)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Pyrimme tarkkuuteen, mutta huomioithan, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäinen asiakirja sen alkuperäiskielellä tulee katsoa auktoriteettiseksi lähteeksi. Tärkeiden tietojen osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinymmärryksistä tai tulkinnoista.