<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "36de9fae488d6de554d969fe8e0801a8",
  "translation_date": "2025-06-20T19:25:25+00:00",
  "source_file": "09-CaseStudy/apimsample.md",
  "language_code": "bg"
}
-->
# Case Study: Излагане на REST API в API Management като MCP сървър

Azure API Management е услуга, която предоставя шлюз над вашите API крайни точки. Как работи: Azure API Management действа като прокси пред вашите API-та и може да решава какво да прави с входящите заявки.

Като го използвате, добавяте множество функции като:

- **Сигурност** – можете да използвате всичко от API ключове, JWT до управлявана идентичност.
- **Ограничаване на честотата на заявките** – страхотна функция, която позволява да решите колко заявки да преминават за определен период от време. Това гарантира, че всички потребители имат добро изживяване и че вашата услуга не се претоварва с заявки.
- **Мащабиране и балансиране на натоварването** – можете да настроите няколко крайни точки, за да разпределите натоварването, както и да изберете как да се извършва балансирането.
- **AI функции като семантично кеширане**, ограничение и мониторинг на токени и други. Тези функции подобряват отзивчивостта и ви помагат да следите разхода на токени. [Прочетете повече тук](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Защо MCP + Azure API Management?

Model Context Protocol бързо се превръща в стандарт за агентски AI приложения и за това как да се изложат инструменти и данни по последователен начин. Azure API Management е естественият избор, когато трябва да "управлявате" API-та. MCP сървърите често се интегрират с други API-та, за да обработват заявки към инструменти, например. Затова съчетаването на Azure API Management и MCP има много смисъл.

## Преглед

В този конкретен случай ще научим как да изложим API крайни точки като MCP сървър. По този начин можем лесно да направим тези крайни точки част от агентско приложение, като същевременно използваме функциите на Azure API Management.

## Основни функции

- Избирате методите на крайна точка, които искате да изложите като инструменти.
- Допълнителните функции зависят от това какво конфигурирате в секцията с политики за вашия API. Тук ще ви покажем как да добавите ограничение на честотата на заявките.

## Предварителна стъпка: импортиране на API

Ако вече имате API в Azure API Management, чудесно – можете да пропуснете тази стъпка. Ако не, разгледайте този линк: [импортиране на API в Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Излагане на API като MCP сървър

За да изложите API крайни точки, следвайте следните стъпки:

1. Отидете в Azure Portal на адрес <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
Навигирайте до вашия API Management инстанция.

1. В лявото меню изберете APIs > MCP Servers > + Create new MCP Server.

1. В API изберете REST API, който искате да изложите като MCP сървър.

1. Изберете една или повече API операции, които да изложите като инструменти. Можете да изберете всички операции или само конкретни.

    ![Select methods to expose](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Изберете **Create**.

1. Навигирайте до менюто **APIs** и **MCP Servers**, трябва да видите следното:

    ![See the MCP Server in the main pane](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP сървърът е създаден и API операциите са изложени като инструменти. MCP сървърът се показва в панела MCP Servers. В колоната URL е показан крайният адрес на MCP сървъра, който можете да използвате за тестове или в клиентско приложение.

## По желание: Конфигуриране на политики

Azure API Management има основната концепция за политики, където задавате различни правила за вашите крайни точки, като например ограничаване на честотата на заявките или семантично кеширане. Тези политики се пишат в XML.

Ето как да настроите политика за ограничаване на честотата на вашия MCP сървър:

1. В портала, под APIs, изберете **MCP Servers**.

1. Изберете създадения MCP сървър.

1. В лявото меню, под MCP, изберете **Policies**.

1. В редактора на политики добавете или редактирайте политиките, които искате да приложите към инструментите на MCP сървъра. Политиките са дефинирани в XML формат. Например, можете да добавите политика, която ограничава обажданията към инструментите на MCP сървъра (в този пример, 5 обаждания на 30 секунди за клиентски IP адрес). Ето XML, който ще ограничи честотата:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Ето и изображение на редактора на политики:

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## Изпробвайте го

Нека се уверим, че MCP сървърът работи както трябва.

За целта ще използваме Visual Studio Code и GitHub Copilot в Agent режим. Ще добавим MCP сървъра в *mcp.json* файл. По този начин Visual Studio Code ще действа като клиент с агентски възможности, а крайните потребители ще могат да въвеждат заявки и да взаимодействат със сървъра.

Ето как да добавите MCP сървъра във Visual Studio Code:

1. Използвайте командата MCP: **Add Server от Command Palette**.

1. Когато бъдете подканени, изберете тип сървър: **HTTP (HTTP или Server Sent Events)**.

1. Въведете URL на MCP сървъра в API Management. Пример: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (за SSE крайна точка) или **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (за MCP крайна точка), обърнете внимание на разликата в транспорта `/sse` or `/mcp`.

1. Въведете ID на сървъра по ваш избор. Това не е критична стойност, но ще ви помогне да запомните коя е тази инстанция на сървъра.

1. Изберете дали да запазите конфигурацията в настройките на работното пространство или в потребителските настройки.

  - **Workspace settings** – Конфигурацията на сървъра се запазва във файл .vscode/mcp.json, който е достъпен само в текущото работно пространство.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    или ако изберете streaming HTTP като транспорт, конфигурацията ще изглежда малко по-различно:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **User settings** – Конфигурацията на сървъра се добавя към глобалния ви *settings.json* файл и е достъпна във всички работни пространства. Конфигурацията изглежда подобно на следното:

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Трябва също да добавите конфигурация – заглавка, за да се удостоверите правилно към Azure API Management. Използва се заглавка с име **Ocp-Apim-Subscription-Key**.

    - Ето как да я добавите в настройките:

    ![Adding header for authentication](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), това ще предизвика появата на подканващ прозорец, който ще ви поиска стойността на API ключа, който можете да намерите в Azure Portal за вашия Azure API Management инстанция.

    - За да го добавите в *mcp.json*, можете да го направите по следния начин:

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

### Използване на Agent режим

Сега, след като всичко е настроено или в настройките, или в *.vscode/mcp.json*, нека го изпробваме.

Трябва да има иконка Tools, както е показано, където са изброени изложените инструменти от вашия сървър:

![Tools from the server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Кликнете на иконката Tools и ще видите списък с инструменти, както е показано:

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Въведете заявка в чата, за да извикате инструмента. Например, ако сте избрали инструмент за получаване на информация за поръчка, можете да попитате агента за поръчка. Ето примерна заявка:

    ```text
    get information from order 2
    ```

    Сега ще видите иконка за инструменти, която ще ви подкани да продължите с извикването на инструмента. Изберете да продължите, и трябва да видите резултат като този:

    ![Result from prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **Какво виждате зависи от инструментите, които сте настроили, но идеята е да получите текстов отговор като показания по-горе.**

## Референции

Ето къде можете да научите повече:

- [Урок за Azure API Management и MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python пример: Защитени отдалечени MCP сървъри с Azure API Management (експериментално)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)
- [Лаборатория за MCP клиентска авторизация](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)
- [Използване на Azure API Management разширението за VS Code за импорт и управление на API-та](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)
- [Регистриране и откриване на отдалечени MCP сървъри в Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Отлично хранилище, което показва много AI възможности с Azure API Management
- [AI Gateway работилници](https://azure-samples.github.io/AI-Gateway/) Съдържа работилници с използване на Azure Portal, което е чудесен начин да започнете да оценявате AI възможностите.

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за никакви недоразумения или неправилни тълкувания, произтичащи от използването на този превод.