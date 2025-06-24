<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5384bbb2a92d00d5d7e66274dbe0331d",
  "translation_date": "2025-06-20T18:34:41+00:00",
  "source_file": "04-PracticalImplementation/README.md",
  "language_code": "pl"
}
-->
# Praktyczna Implementacja

Praktyczna implementacja to moment, w którym moc Model Context Protocol (MCP) staje się namacalna. Choć zrozumienie teorii i architektury MCP jest ważne, prawdziwa wartość pojawia się, gdy zastosujesz te koncepcje do tworzenia, testowania i wdrażania rozwiązań rozwiązujących realne problemy. Ten rozdział łączy wiedzę teoretyczną z praktycznym rozwojem, prowadząc Cię przez proces tworzenia aplikacji opartych na MCP.

Niezależnie od tego, czy tworzysz inteligentnych asystentów, integrujesz AI w procesy biznesowe, czy budujesz niestandardowe narzędzia do przetwarzania danych, MCP zapewnia elastyczną podstawę. Jego językowo-neutralna konstrukcja oraz oficjalne SDK dla popularnych języków programowania sprawiają, że jest dostępny dla szerokiego grona deweloperów. Wykorzystując te SDK, możesz szybko prototypować, iterować i skalować swoje rozwiązania na różnych platformach i środowiskach.

W kolejnych sekcjach znajdziesz praktyczne przykłady, przykładowy kod i strategie wdrażania, które pokazują, jak implementować MCP w C#, Java, TypeScript, JavaScript i Python. Dowiesz się również, jak debugować i testować serwery MCP, zarządzać API oraz wdrażać rozwiązania w chmurze za pomocą Azure. Te praktyczne materiały mają na celu przyspieszenie nauki i pomóc Ci zbudować solidne, gotowe do produkcji aplikacje MCP.

## Przegląd

Ta lekcja koncentruje się na praktycznych aspektach implementacji MCP w różnych językach programowania. Poznasz, jak korzystać z SDK MCP w C#, Java, TypeScript, JavaScript i Python, aby tworzyć solidne aplikacje, debugować i testować serwery MCP oraz tworzyć wielokrotnego użytku zasoby, prompt’y i narzędzia.

## Cele Nauki

Po ukończeniu tej lekcji będziesz potrafił:
- Implementować rozwiązania MCP przy użyciu oficjalnych SDK w różnych językach programowania
- Systematycznie debugować i testować serwery MCP
- Tworzyć i wykorzystywać funkcje serwera (Resources, Prompts i Tools)
- Projektować efektywne workflow MCP dla złożonych zadań
- Optymalizować implementacje MCP pod kątem wydajności i niezawodności

## Oficjalne SDK

Model Context Protocol oferuje oficjalne SDK dla wielu języków:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) 
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

## Praca z SDK MCP

Ta sekcja zawiera praktyczne przykłady implementacji MCP w różnych językach programowania. Przykładowy kod znajdziesz w katalogu `samples`, zorganizowanym według języków.

### Dostępne Przykłady

Repozytorium zawiera [przykładowe implementacje](../../../04-PracticalImplementation/samples) w następujących językach:

- [C#](./samples/csharp/README.md)
- [Java](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Każdy przykład demonstruje kluczowe koncepcje MCP i wzorce implementacji specyficzne dla danego języka i ekosystemu.

## Główne Funkcje Serwera

Serwery MCP mogą implementować dowolne połączenie poniższych funkcji:

### Resources
Resources dostarczają kontekst i dane do wykorzystania przez użytkownika lub model AI:
- Repozytoria dokumentów
- Bazy wiedzy
- Strukturalne źródła danych
- Systemy plików

### Prompts
Prompts to szablonowe wiadomości i workflow dla użytkowników:
- Wstępnie zdefiniowane szablony konwersacji
- Wzorce interakcji prowadzonej
- Specjalistyczne struktury dialogowe

### Tools
Tools to funkcje, które model AI może wykonać:
- Narzędzia do przetwarzania danych
- Integracje z zewnętrznymi API
- Możliwości obliczeniowe
- Funkcje wyszukiwania

## Przykładowe Implementacje: C#

Oficjalne repozytorium C# SDK zawiera kilka przykładów implementacji pokazujących różne aspekty MCP:

- **Podstawowy klient MCP**: Prosty przykład pokazujący, jak stworzyć klienta MCP i wywołać narzędzia
- **Podstawowy serwer MCP**: Minimalna implementacja serwera z podstawową rejestracją narzędzi
- **Zaawansowany serwer MCP**: Pełna implementacja serwera z rejestracją narzędzi, uwierzytelnianiem i obsługą błędów
- **Integracja z ASP.NET**: Przykłady integracji z ASP.NET Core
- **Wzorce implementacji narzędzi**: Różne wzorce implementacji narzędzi o różnym stopniu złożoności

SDK MCP dla C# jest w fazie preview i API mogą się zmieniać. Będziemy na bieżąco aktualizować ten blog wraz z rozwojem SDK.

### Kluczowe Funkcje 
- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)

- Tworzenie [pierwszego serwera MCP](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

Pełne przykłady implementacji w C# znajdziesz w [oficjalnym repozytorium przykładów C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Przykładowa implementacja: Java

Java SDK oferuje solidne opcje implementacji MCP z funkcjami na poziomie enterprise.

### Kluczowe Funkcje

- Integracja ze Spring Framework
- Silna typizacja
- Wsparcie dla programowania reaktywnego
- Kompleksowa obsługa błędów

Pełny przykład implementacji w Javie znajdziesz w [Java sample](samples/java/containerapp/README.md) w katalogu z przykładami.

## Przykładowa implementacja: JavaScript

JavaScript SDK oferuje lekkie i elastyczne podejście do implementacji MCP.

### Kluczowe Funkcje

- Wsparcie dla Node.js i przeglądarek
- API oparte na Promise
- Łatwa integracja z Express i innymi frameworkami
- Wsparcie WebSocket do streamingu

Pełny przykład implementacji w JavaScript znajdziesz w [JavaScript sample](samples/javascript/README.md) w katalogu z przykładami.

## Przykładowa implementacja: Python

Python SDK oferuje „pythoniczne” podejście do implementacji MCP z doskonałą integracją z frameworkami ML.

### Kluczowe Funkcje

- Wsparcie async/await z asyncio
- Integracja z Flask i FastAPI
- Prosta rejestracja narzędzi
- Natychmiastowa integracja z popularnymi bibliotekami ML

Pełny przykład implementacji w Pythonie znajdziesz w [Python sample](samples/python/README.md) w katalogu z przykładami.

## Zarządzanie API 

Azure API Management to świetne rozwiązanie, które pozwala zabezpieczyć serwery MCP. Pomysł polega na umieszczeniu instancji Azure API Management przed Twoim serwerem MCP, która zajmie się funkcjami, które mogą Ci się przydać, takimi jak:

- ograniczanie liczby żądań (rate limiting)
- zarządzanie tokenami
- monitorowanie
- równoważenie obciążenia
- bezpieczeństwo

### Przykład Azure

Oto przykład Azure, który robi dokładnie to, czyli [tworzy serwer MCP i zabezpiecza go za pomocą Azure API Management](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Zobacz, jak przebiega proces autoryzacji na poniższym obrazku:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true) 

Na powyższym obrazku dzieje się:

- Uwierzytelnianie/autoryzacja odbywa się za pomocą Microsoft Entra.
- Azure API Management działa jako brama i używa polityk do kierowania i zarządzania ruchem.
- Azure Monitor rejestruje wszystkie żądania do dalszej analizy.

#### Przebieg autoryzacji

Przyjrzyjmy się dokładniej przebiegowi autoryzacji:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### Specyfikacja autoryzacji MCP

Dowiedz się więcej o [specyfikacji autoryzacji MCP](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization#2-10-third-party-authorization-flow)

## Wdrażanie zdalnego serwera MCP na Azure

Sprawdźmy, czy możemy wdrożyć wspomniany wcześniej przykład:

1. Sklonuj repozytorium

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

2. Zarejestruj `Microsoft.App` resource provider.
    * If you are using Azure CLI, run `az provider register --namespace Microsoft.App --wait`.
    * If you are using Azure PowerShell, run `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Then run `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` i po chwili sprawdź, czy rejestracja jest zakończona.

3. Uruchom to polecenie [azd](https://aka.ms/azd), aby utworzyć usługę zarządzania API, aplikację funkcji (z kodem) oraz wszystkie inne potrzebne zasoby Azure

    ```shell
    azd up
    ```

    To polecenie powinno wdrożyć wszystkie zasoby w chmurze Azure

### Testowanie serwera za pomocą MCP Inspector

1. W **nowym oknie terminala** zainstaluj i uruchom MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Powinieneś zobaczyć interfejs podobny do:

    ![Connect to Node inspector](../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.pl.png) 

2. Kliknij CTRL i otwórz aplikację webową MCP Inspector z adresu URL wyświetlonego przez aplikację (np. http://127.0.0.1:6274/#resources)
3. Ustaw typ transportu na `SSE`
1. Set the URL to your running API Management SSE endpoint displayed after `azd up` i **Połącz**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

5. **Wyświetl listę narzędzi**. Kliknij na narzędzie i **Uruchom narzędzie**.  

Jeśli wszystkie kroki zostały wykonane poprawnie, powinieneś być teraz połączony z serwerem MCP i móc wywołać narzędzie.

## Serwery MCP dla Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Ten zestaw repozytoriów to szablony szybkiego startu do budowy i wdrażania niestandardowych zdalnych serwerów MCP (Model Context Protocol) z użyciem Azure Functions w Pythonie, C# .NET lub Node/TypeScript.

Przykłady oferują kompletne rozwiązanie, które pozwala deweloperom:

- Budować i uruchamiać lokalnie: rozwijać i debugować serwer MCP na lokalnej maszynie
- Wdrażać na Azure: łatwo wdrażać w chmurze za pomocą prostego polecenia azd up
- Łączyć się z klientami: łączyć się z serwerem MCP z różnych klientów, w tym trybu agenta Copilot w VS Code oraz narzędzia MCP Inspector

### Kluczowe Funkcje:

- Bezpieczeństwo wbudowane: serwer MCP jest zabezpieczony przy użyciu kluczy i HTTPS
- Opcje uwierzytelniania: obsługuje OAuth z wbudowanym uwierzytelnianiem i/lub API Management
- Izolacja sieci: umożliwia izolację sieciową za pomocą Azure Virtual Networks (VNET)
- Architektura bezserwerowa: wykorzystuje Azure Functions do skalowalnego, zdarzeniowego wykonania
- Lokalny rozwój: kompleksowe wsparcie lokalnego rozwoju i debugowania
- Proste wdrażanie: uproszczony proces wdrażania na Azure

Repozytorium zawiera wszystkie niezbędne pliki konfiguracyjne, kod źródłowy i definicje infrastruktury, aby szybko rozpocząć pracę z produkcyjną implementacją serwera MCP.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Przykładowa implementacja MCP z użyciem Azure Functions w Pythonie

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Przykładowa implementacja MCP z użyciem Azure Functions w C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Przykładowa implementacja MCP z użyciem Azure Functions w Node/TypeScript.

## Najważniejsze wnioski

- SDK MCP dostarczają narzędzia specyficzne dla języków do tworzenia solidnych rozwiązań MCP
- Proces debugowania i testowania jest kluczowy dla niezawodnych aplikacji MCP
- Wielokrotnego użytku szablony promptów umożliwiają spójne interakcje z AI
- Dobrze zaprojektowane workflow mogą orkiestruje złożone zadania z użyciem wielu narzędzi
- Implementacja rozwiązań MCP wymaga uwzględnienia bezpieczeństwa, wydajności i obsługi błędów

## Ćwiczenie

Zaprojektuj praktyczny workflow MCP, który rozwiązuje realny problem w Twojej dziedzinie:

1. Wybierz 3-4 narzędzia, które byłyby przydatne do rozwiązania tego problemu
2. Stwórz diagram workflow pokazujący, jak te narzędzia współpracują
3. Zaimplementuj podstawową wersję jednego z narzędzi w wybranym języku
4. Stwórz szablon promptu, który pomoże modelowi skutecznie korzystać z Twojego narzędzia

## Dodatkowe zasoby


---

Następny: [Zaawansowane tematy](../05-AdvancedTopics/README.md)

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu automatycznej usługi tłumaczeniowej AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mimo że dokładamy starań, aby tłumaczenie było jak najbardziej precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w języku źródłowym należy traktować jako źródło wiążące. W przypadku informacji krytycznych zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.