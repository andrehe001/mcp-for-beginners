<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:29:30+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "pl"
}
-->
# Generator planu nauki z Chainlit i Microsoft Learn Docs MCP

## Wymagania wstępne

- Python 3.8 lub nowszy
- pip (menedżer pakietów Pythona)
- Dostęp do internetu, aby połączyć się z serwerem Microsoft Learn Docs MCP

## Instalacja

1. Sklonuj to repozytorium lub pobierz pliki projektu.
2. Zainstaluj wymagane zależności:

   ```bash
   pip install -r requirements.txt
   ```

## Użytkowanie

### Scenariusz 1: Proste zapytanie do Docs MCP  
Klient wiersza poleceń, który łączy się z serwerem Docs MCP, wysyła zapytanie i wyświetla wynik.

1. Uruchom skrypt:  
   ```bash
   python scenario1.py
   ```  
2. Wpisz swoje pytanie dotyczące dokumentacji, gdy pojawi się zachęta.

### Scenariusz 2: Generator planu nauki (aplikacja webowa Chainlit)  
Interfejs webowy (oparty na Chainlit), który pozwala użytkownikom wygenerować spersonalizowany, tygodniowy plan nauki dla dowolnego tematu technicznego.

1. Uruchom aplikację Chainlit:  
   ```bash
   chainlit run scenario2.py
   ```  
2. Otwórz lokalny adres URL podany w terminalu (np. http://localhost:8000) w przeglądarce.  
3. W oknie czatu wpisz temat nauki oraz liczbę tygodni, które chcesz poświęcić (np. "AI-900 certification, 8 weeks").  
4. Aplikacja odpowie planem nauki rozpisanym na tygodnie, zawierającym linki do odpowiedniej dokumentacji Microsoft Learn.

**Wymagane zmienne środowiskowe:**  

Aby korzystać ze Scenariusza 2 (aplikacji Chainlit z Azure OpenAI), musisz ustawić następujące zmienne środowiskowe w katalogu `.env` file in the `python`:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Uzupełnij te wartości swoimi danymi zasobu Azure OpenAI przed uruchomieniem aplikacji.

> **Wskazówka:** Łatwo możesz wdrożyć własne modele korzystając z [Azure AI Foundry](https://ai.azure.com/).

### Scenariusz 3: Dokumentacja w edytorze z serwerem MCP w VS Code

Zamiast przełączać się między kartami przeglądarki, aby szukać dokumentacji, możesz mieć Microsoft Learn Docs bezpośrednio w VS Code dzięki serwerowi MCP. Umożliwia to:  
- Wyszukiwanie i czytanie dokumentacji w VS Code bez wychodzenia z środowiska kodowania.  
- Odwoływanie się do dokumentacji i wstawianie linków bezpośrednio do plików README lub materiałów kursu.  
- Korzystanie jednocześnie z GitHub Copilot i MCP, tworząc płynny, wspomagany AI workflow dokumentacyjny.

**Przykładowe zastosowania:**  
- Szybkie dodawanie linków referencyjnych do README podczas pisania dokumentacji kursu lub projektu.  
- Wykorzystanie Copilota do generowania kodu oraz MCP do natychmiastowego znajdowania i cytowania odpowiednich materiałów.  
- Skupienie się na edytorze i zwiększenie produktywności.

> [!IMPORTANT]  
> Upewnij się, że posiadasz ważny plik [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

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

Te przykłady pokazują elastyczność aplikacji w zależności od celów nauki i dostępnego czasu.

## Źródła

- [Chainlit Documentation](https://docs.chainlit.io/)  
- [MCP Documentation](https://github.com/MicrosoftDocs/mcp)

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczeń AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dążymy do jak największej dokładności, prosimy mieć na uwadze, że tłumaczenia automatyczne mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy traktować jako źródło autorytatywne. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.