<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6940b1e931e51821b219aa9dcfe8c4ee",
  "translation_date": "2025-06-23T11:07:37+00:00",
  "source_file": "09-CaseStudy/README.md",
  "language_code": "pl"
}
-->
# MCP w praktyce: studia przypadków z życia

Model Context Protocol (MCP) zmienia sposób, w jaki aplikacje AI współpracują z danymi, narzędziami i usługami. Ta sekcja prezentuje studia przypadków z życia, które pokazują praktyczne zastosowania MCP w różnych scenariuszach biznesowych.

## Przegląd

W tej sekcji znajdziesz konkretne przykłady implementacji MCP, ukazujące, jak organizacje wykorzystują ten protokół do rozwiązywania złożonych problemów biznesowych. Analizując te studia przypadków, zdobędziesz wiedzę na temat wszechstronności, skalowalności i praktycznych korzyści MCP w rzeczywistych zastosowaniach.

## Kluczowe cele nauki

Analizując te studia przypadków, będziesz mógł:

- Zrozumieć, jak MCP można zastosować do rozwiązywania konkretnych problemów biznesowych
- Poznać różne wzorce integracji i podejścia architektoniczne
- Rozpoznać najlepsze praktyki wdrażania MCP w środowiskach korporacyjnych
- Zdobyć wiedzę o wyzwaniach i rozwiązaniach napotkanych podczas rzeczywistych implementacji
- Zidentyfikować możliwości wykorzystania podobnych wzorców w swoich projektach

## Prezentowane studia przypadków

### 1. [Azure AI Travel Agents – Implementacja referencyjna](./travelagentsample.md)

To studium przypadku przedstawia kompleksowe rozwiązanie referencyjne Microsoftu, które pokazuje, jak zbudować wieloagentową, opartą na AI aplikację do planowania podróży, wykorzystując MCP, Azure OpenAI i Azure AI Search. Projekt demonstruje:

- Orkiestrację wielu agentów za pomocą MCP
- Integrację danych korporacyjnych z Azure AI Search
- Bezpieczną, skalowalną architekturę opartą na usługach Azure
- Rozszerzalne narzędzia z wielokrotnego użytku komponentami MCP
- Konwersacyjne doświadczenie użytkownika napędzane przez Azure OpenAI

Architektura i szczegóły implementacji dostarczają cennych wskazówek dotyczących budowy złożonych systemów wieloagentowych z MCP jako warstwą koordynacyjną.

### 2. [Aktualizacja elementów Azure DevOps na podstawie danych z YouTube](./UpdateADOItemsFromYT.md)

To studium przypadku pokazuje praktyczne zastosowanie MCP do automatyzacji procesów roboczych. Przedstawia, jak narzędzia MCP mogą być użyte do:

- Pobierania danych z platform internetowych (YouTube)
- Aktualizacji elementów pracy w systemach Azure DevOps
- Tworzenia powtarzalnych automatycznych procesów
- Integracji danych między różnymi systemami

Ten przykład ilustruje, jak nawet stosunkowo proste implementacje MCP mogą znacząco zwiększyć efektywność, automatyzując rutynowe zadania i poprawiając spójność danych między systemami.

### 3. [Pobieranie dokumentacji w czasie rzeczywistym z MCP](./docs-mcp/README.md)

To studium przypadku pokazuje, jak połączyć klienta konsolowego Python z serwerem Model Context Protocol (MCP), aby pobierać i zapisywać w logu aktualną, kontekstową dokumentację Microsoft. Nauczysz się:

- Łączyć się z serwerem MCP za pomocą klienta Python i oficjalnego SDK MCP
- Korzystać ze strumieniowych klientów HTTP do efektywnego pobierania danych w czasie rzeczywistym
- Wywoływać narzędzia dokumentacyjne na serwerze i logować odpowiedzi bezpośrednio do konsoli
- Integracji aktualnej dokumentacji Microsoft z workflow bez opuszczania terminala

Rozdział zawiera praktyczne zadanie, minimalny działający przykład kodu oraz linki do dodatkowych materiałów do pogłębionej nauki. Zobacz pełne omówienie i kod w powiązanym rozdziale, aby zrozumieć, jak MCP może zmienić dostęp do dokumentacji i produktywność deweloperów w środowiskach konsolowych.

### 4. [Interaktywny generator planu nauki w aplikacji webowej z MCP](./docs-mcp/README.md)

To studium przypadku pokazuje, jak zbudować interaktywną aplikację webową wykorzystującą Chainlit i Model Context Protocol (MCP) do tworzenia spersonalizowanych planów nauki na dowolny temat. Użytkownicy mogą określić temat (np. "certyfikacja AI-900") oraz czas nauki (np. 8 tygodni), a aplikacja zaproponuje tygodniowy podział zalecanych materiałów. Chainlit umożliwia konwersacyjny interfejs czatu, co sprawia, że doświadczenie jest angażujące i elastyczne.

- Konwersacyjna aplikacja webowa napędzana przez Chainlit
- Prompty sterowane przez użytkownika dotyczące tematu i czasu trwania
- Tygodniowe rekomendacje treści z wykorzystaniem MCP
- Adaptacyjne odpowiedzi w czasie rzeczywistym w interfejsie czatu

Projekt pokazuje, jak AI konwersacyjne i MCP mogą współpracować, tworząc dynamiczne, sterowane przez użytkownika narzędzia edukacyjne w nowoczesnym środowisku webowym.

### 5. [Dokumentacja w edytorze z serwerem MCP w VS Code](./docs-mcp/README.md)

To studium przypadku pokazuje, jak wprowadzić Microsoft Learn Docs bezpośrednio do środowiska VS Code za pomocą serwera MCP — koniec z przełączaniem się między kartami przeglądarki! Zobaczysz, jak:

- Natychmiast wyszukiwać i czytać dokumentację w VS Code, korzystając z panelu MCP lub palety poleceń
- Odnosić się do dokumentacji i wstawiać linki bezpośrednio do plików README lub kursów w formacie markdown
- Korzystać z GitHub Copilot i MCP razem, aby uzyskać płynne, wspomagane AI przepływy pracy z dokumentacją i kodem
- Weryfikować i ulepszać dokumentację dzięki informacji zwrotnej w czasie rzeczywistym i dokładności pochodzącej od Microsoft
- Integracja MCP z workflow GitHub dla ciągłej weryfikacji dokumentacji

Implementacja obejmuje:
- Przykładową konfigurację `.vscode/mcp.json` dla łatwego uruchomienia
- Przewodniki oparte na zrzutach ekranu pokazujące doświadczenie w edytorze
- Wskazówki dotyczące łączenia Copilot i MCP dla maksymalnej produktywności

Scenariusz idealny dla autorów kursów, twórców dokumentacji i programistów, którzy chcą pozostać skupieni w edytorze, pracując z dokumentacją, Copilotem i narzędziami walidacyjnymi — wszystko napędzane przez MCP.

### 6. [Tworzenie serwera MCP w APIM](./apimsample.md)

To studium przypadku przedstawia krok po kroku, jak stworzyć serwer MCP za pomocą Azure API Management (APIM). Obejmuje:

- Konfigurację serwera MCP w Azure API Management
- Udostępnianie operacji API jako narzędzi MCP
- Konfigurację polityk ograniczania liczby żądań i zabezpieczeń
- Testowanie serwera MCP za pomocą Visual Studio Code i GitHub Copilot

Przykład pokazuje, jak wykorzystać możliwości Azure do stworzenia solidnego serwera MCP, który może być używany w różnych aplikacjach, zwiększając integrację systemów AI z korporacyjnymi API.

## Podsumowanie

Te studia przypadków podkreślają wszechstronność i praktyczne zastosowania Model Context Protocol w rzeczywistych scenariuszach. Od złożonych systemów wieloagentowych po ukierunkowane automatyzacje procesów, MCP oferuje ustandaryzowany sposób łączenia systemów AI z narzędziami i danymi potrzebnymi do dostarczania wartości.

Analizując te implementacje, zdobędziesz wiedzę na temat wzorców architektonicznych, strategii wdrożeniowych i najlepszych praktyk, które możesz zastosować we własnych projektach MCP. Przykłady pokazują, że MCP to nie tylko teoria, ale praktyczne rozwiązanie rzeczywistych wyzwań biznesowych.

## Dodatkowe zasoby

- [Azure AI Travel Agents GitHub Repository](https://github.com/Azure-Samples/azure-ai-travel-agents)
- [Azure DevOps MCP Tool](https://github.com/microsoft/azure-devops-mcp)
- [Playwright MCP Tool](https://github.com/microsoft/playwright-mcp)
- [Microsoft Docs MCP Server](https://github.com/MicrosoftDocs/mcp)
- [MCP Community Examples](https://github.com/microsoft/mcp)

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony za pomocą usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym powinien być uważany za źródło autorytatywne. W przypadku informacji o kluczowym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.