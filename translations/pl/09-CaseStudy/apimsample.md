<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "36de9fae488d6de554d969fe8e0801a8",
  "translation_date": "2025-06-20T19:19:20+00:00",
  "source_file": "09-CaseStudy/apimsample.md",
  "language_code": "pl"
}
-->
# Studium przypadku: Udostępnianie REST API w Azure API Management jako serwer MCP

Azure API Management to usługa, która zapewnia bramę (Gateway) nad Twoimi punktami końcowymi API. Działa ona jako proxy przed Twoimi API i decyduje, co zrobić z przychodzącymi żądaniami.

Korzystając z niej, zyskujesz wiele funkcji, takich jak:

- **Bezpieczeństwo** – możesz używać wszystkiego, od kluczy API, JWT po managed identity.
- **Ograniczanie liczby wywołań (rate limiting)** – świetna funkcja pozwalająca określić, ile wywołań może przejść w określonym czasie. Pomaga to zapewnić wszystkim użytkownikom dobrą jakość obsługi oraz chroni usługę przed przeciążeniem.
- **Skalowanie i równoważenie obciążenia** – możesz skonfigurować wiele punktów końcowych, aby rozłożyć obciążenie, a także zdecydować, jak ma działać równoważenie obciążenia.
- **Funkcje AI, takie jak semantyczne buforowanie, limit tokenów, monitorowanie tokenów i inne**. To doskonałe funkcje, które poprawiają szybkość reakcji oraz pomagają kontrolować zużycie tokenów. [Dowiedz się więcej tutaj](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Dlaczego MCP + Azure API Management?

Model Context Protocol szybko staje się standardem dla agentowych aplikacji AI oraz sposobem na spójne udostępnianie narzędzi i danych. Azure API Management jest naturalnym wyborem, gdy potrzebujesz „zarządzać” API. Serwery MCP często integrują się z innymi API, by rozwiązywać żądania do narzędzi. Dlatego połączenie Azure API Management i MCP ma dużo sensu.

## Przegląd

W tym konkretnym przypadku nauczymy się, jak udostępnić punkty końcowe API jako serwer MCP. Dzięki temu łatwo włączymy te punkty końcowe do aplikacji agentowej, jednocześnie korzystając z funkcji Azure API Management.

## Kluczowe funkcje

- Wybierasz metody endpointów, które chcesz udostępnić jako narzędzia.
- Dodatkowe funkcje zależą od konfiguracji w sekcji polityk dla Twojego API. Tutaj pokażemy, jak dodać ograniczenie liczby wywołań.

## Krok wstępny: import API

Jeśli masz już API w Azure API Management, świetnie – możesz pominąć ten krok. Jeśli nie, zapoznaj się z tym linkiem: [importowanie API do Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Udostępnianie API jako serwera MCP

Aby udostępnić punkty końcowe API, wykonaj następujące kroki:

1. Przejdź do Azure Portal pod adresem <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
   Przejdź do swojej instancji API Management.

1. W menu po lewej wybierz APIs > MCP Servers > + Create new MCP Server.

1. W sekcji API wybierz REST API, które chcesz udostępnić jako serwer MCP.

1. Wybierz jedną lub więcej operacji API, które chcesz udostępnić jako narzędzia. Możesz wybrać wszystkie operacje lub tylko wybrane.

    ![Wybierz metody do udostępnienia](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Wybierz **Create**.

1. Przejdź do menu **APIs** i **MCP Servers**, powinieneś zobaczyć coś takiego:

    ![Zobacz serwer MCP w głównym panelu](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    Serwer MCP został utworzony, a operacje API są udostępnione jako narzędzia. Serwer MCP jest widoczny na liście MCP Servers. Kolumna URL pokazuje punkt końcowy serwera MCP, który możesz wywołać do testów lub z poziomu aplikacji klienckiej.

## Opcjonalnie: Konfiguracja polityk

Azure API Management opiera się na koncepcji polityk, gdzie definiujesz różne zasady dla swoich endpointów, np. ograniczenie liczby wywołań czy semantyczne buforowanie. Polityki są definiowane w formacie XML.

Oto jak możesz ustawić politykę ograniczającą liczbę wywołań na serwerze MCP:

1. W portalu, w sekcji APIs, wybierz **MCP Servers**.

1. Wybierz utworzony serwer MCP.

1. W menu po lewej, pod MCP, wybierz **Policies**.

1. W edytorze polityk dodaj lub edytuj polityki, które chcesz zastosować do narzędzi serwera MCP. Polityki definiuje się w XML. Na przykład możesz dodać politykę ograniczającą wywołania do narzędzi serwera MCP (w tym przykładzie 5 wywołań na 30 sekund na adres IP klienta). Oto XML, który wprowadza ograniczenie:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Poniżej obrazek edytora polityk:

    ![Edytor polityk](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Wypróbuj

Sprawdźmy, czy nasz serwer MCP działa poprawnie.

Do tego użyjemy Visual Studio Code oraz GitHub Copilot w trybie agenta. Dodamy serwer MCP do pliku *mcp.json*. W ten sposób Visual Studio Code będzie działać jako klient z możliwościami agentowymi, a użytkownicy końcowi będą mogli wpisywać polecenia i wchodzić w interakcję z serwerem.

Zobaczmy, jak dodać serwer MCP w Visual Studio Code:

1. Użyj polecenia MCP: **Add Server** z Command Palette.

1. Po wyświetleniu monitu wybierz typ serwera: **HTTP (HTTP lub Server Sent Events)**.

1. Wprowadź URL serwera MCP w Azure API Management. Przykład: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (dla endpointu SSE) lub **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (dla endpointu MCP). Zwróć uwagę na różnicę w protokole: `/sse` or `/mcp`.

1. Wprowadź dowolny identyfikator serwera. Nie jest to wartość krytyczna, ale pomoże Ci zapamiętać, czym jest ta instancja serwera.

1. Wybierz, czy zapisać konfigurację w ustawieniach workspace, czy w ustawieniach użytkownika.

  - **Workspace settings** – konfiguracja serwera jest zapisywana w pliku .vscode/mcp.json dostępnym tylko w bieżącym workspace.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    lub jeśli wybierzesz streaming HTTP jako transport, będzie to wyglądało nieco inaczej:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **User settings** – konfiguracja serwera jest dodawana do globalnego pliku *settings.json* i jest dostępna we wszystkich workspace’ach. Konfiguracja wygląda mniej więcej tak:

    ![Ustawienia użytkownika](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Musisz również dodać konfigurację nagłówka, aby poprawnie uwierzytelnić się w Azure API Management. Używa on nagłówka o nazwie **Ocp-Apim-Subscription-Key**.

    - Oto jak dodać go w ustawieniach:

    ![Dodawanie nagłówka do uwierzytelniania](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png) – spowoduje to wyświetlenie monitu o wartość klucza API, który znajdziesz w Azure Portal dla swojej instancji Azure API Management.

    - Aby dodać go do *mcp.json*, możesz zrobić to tak:

    ```json
    "inputs": [
      {
        "type": "promptString",
        "id": "apim_key",
        "description": "API Key for Azure API Management",
        "password": true
      }
    ]
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp",
            "headers": {
                "Ocp-Apim-Subscription-Key": "Bearer ${input:apim_key}"
            }
        }
    }
    ```

### Użyj trybu agenta

Teraz mamy wszystko skonfigurowane, zarówno w ustawieniach, jak i w *.vscode/mcp.json*. Wypróbujmy.

Powinien pojawić się ikonka Narzędzi, gdzie będą wyświetlone udostępnione narzędzia z Twojego serwera:

![Narzędzia z serwera](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Kliknij ikonę narzędzi, powinieneś zobaczyć listę narzędzi, na przykład taką:

    ![Narzędzia](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Wpisz polecenie w czacie, aby wywołać narzędzie. Na przykład, jeśli wybrałeś narzędzie do pobierania informacji o zamówieniu, możesz zapytać agenta o szczegóły zamówienia. Oto przykładowe polecenie:

    ```text
    get information from order 2
    ```

    Zobaczysz teraz ikonę narzędzi z prośbą o kontynuację wywołania narzędzia. Wybierz, aby kontynuować, a powinieneś zobaczyć wynik podobny do tego:

    ![Wynik zapytania](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **To, co widzisz powyżej, zależy od tego, jakie narzędzia skonfigurowałeś, ale idea jest taka, że otrzymujesz tekstową odpowiedź.**

## Źródła

Oto, gdzie możesz dowiedzieć się więcej:

- [Samouczek dotyczący Azure API Management i MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Przykład w Python: Bezpieczne zdalne serwery MCP z użyciem Azure API Management (eksperymentalne)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Laboratorium autoryzacji klienta MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Użyj rozszerzenia Azure API Management dla VS Code do importu i zarządzania API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Rejestracja i odkrywanie zdalnych serwerów MCP w Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) – świetne repozytorium pokazujące wiele możliwości AI z Azure API Management
- [Warsztaty AI Gateway](https://azure-samples.github.io/AI-Gateway/) – zawiera warsztaty z użyciem Azure Portal, co jest świetnym sposobem na rozpoczęcie oceny możliwości AI.

**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczenia AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dążymy do dokładności, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w języku źródłowym powinien być uznawany za źródło autorytatywne. W przypadku informacji o krytycznym znaczeniu zalecane jest skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.