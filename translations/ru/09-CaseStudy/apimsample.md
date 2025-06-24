<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "36de9fae488d6de554d969fe8e0801a8",
  "translation_date": "2025-06-20T19:13:29+00:00",
  "source_file": "09-CaseStudy/apimsample.md",
  "language_code": "ru"
}
-->
# Кейc: Открытие REST API в Azure API Management как MCP сервер

Azure API Management — это сервис, который предоставляет шлюз поверх ваших API-эндпоинтов. Принцип работы таков: Azure API Management выступает в роли прокси перед вашими API и может управлять входящими запросами.

Используя этот сервис, вы получаете множество возможностей, таких как:

- **Безопасность**: можно использовать всё — от API ключей и JWT до управляемой идентификации.
- **Ограничение частоты запросов**: удобная функция, позволяющая контролировать, сколько вызовов проходит за определённый промежуток времени. Это помогает обеспечить хороший опыт для всех пользователей и не перегружать ваш сервис.
- **Масштабирование и балансировка нагрузки**: можно настроить несколько эндпоинтов для распределения нагрузки и выбрать способ балансировки.
- **AI-функции, такие как семантическое кеширование, ограничение и мониторинг токенов и другие**. Эти возможности улучшают отзывчивость и помогают контролировать расход токенов. [Подробнее здесь](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Почему MCP + Azure API Management?

Model Context Protocol быстро становится стандартом для агентных AI-приложений и способа последовательного предоставления инструментов и данных. Azure API Management — естественный выбор, когда нужно «управлять» API. MCP серверы часто интегрируются с другими API для обработки запросов к инструментам, например. Поэтому сочетание Azure API Management и MCP выглядит логичным.

## Обзор

В этом конкретном примере мы научимся открывать API-эндпоинты как MCP сервер. Это позволит легко использовать эти эндпоинты в агентном приложении, одновременно используя возможности Azure API Management.

## Основные возможности

- Вы выбираете методы эндпоинта, которые хотите открыть как инструменты.
- Дополнительные возможности зависят от того, что вы настроите в разделе политики для вашего API. Здесь мы покажем, как добавить ограничение частоты запросов.

## Предварительный шаг: импорт API

Если у вас уже есть API в Azure API Management, отлично — этот шаг можно пропустить. Если нет, ознакомьтесь с инструкцией по [импорту API в Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Открытие API как MCP сервер

Чтобы открыть API-эндпоинты, выполните следующие шаги:

1. Перейдите в Azure Portal по адресу <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp> и откройте ваш экземпляр API Management.

1. В левом меню выберите APIs > MCP Servers > + Создать новый MCP сервер.

1. В разделе API выберите REST API, который хотите открыть как MCP сервер.

1. Выберите одну или несколько операций API, которые хотите открыть как инструменты. Можно выбрать все операции или только определённые.

    ![Выбор методов для открытия](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Нажмите **Создать**.

1. Перейдите в меню **APIs** и **MCP Servers**, вы увидите следующее:

    ![MCP сервер в основном окне](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP сервер создан, а операции API открыты как инструменты. MCP сервер отображается в панели MCP Servers. В столбце URL показан эндпоинт MCP сервера, который можно использовать для тестирования или в клиентском приложении.

## Дополнительно: настройка политик

В Azure API Management есть ключевая концепция политик — правил, которые применяются к эндпоинтам, например, ограничение частоты запросов или семантическое кеширование. Политики задаются в формате XML.

Вот как можно настроить политику для ограничения частоты запросов к вашему MCP серверу:

1. В портале, в разделе APIs выберите **MCP Servers**.

1. Выберите созданный MCP сервер.

1. В левом меню, под MCP, выберите **Policies**.

1. В редакторе политик добавьте или отредактируйте политики, которые хотите применить к инструментам MCP сервера. Политики описываются в XML. Например, можно добавить политику, ограничивающую количество вызовов инструментов MCP сервера (в этом примере — 5 вызовов за 30 секунд с одного IP-адреса клиента). Вот XML, который задаёт такое ограничение:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Вот изображение редактора политик:

    ![Редактор политик](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Попробуйте

Давайте убедимся, что MCP сервер работает как задумано.

Для этого мы воспользуемся Visual Studio Code и GitHub Copilot в режиме агента. Мы добавим MCP сервер в файл *mcp.json*. Таким образом Visual Studio Code будет выступать клиентом с агентными возможностями, а конечные пользователи смогут вводить запросы и взаимодействовать с сервером.

Вот как добавить MCP сервер в Visual Studio Code:

1. Используйте команду MCP: **Add Server** из палитры команд.

1. При появлении запроса выберите тип сервера: **HTTP (HTTP или Server Sent Events)**.

1. Введите URL MCP сервера в Azure API Management. Например: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (для SSE эндпоинта) или **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (для MCP эндпоинта). Обратите внимание, что разница в транспортах — `/sse` or `/mcp`.

1. Введите ID сервера на ваш выбор. Это не критичное значение, но поможет запомнить, что это за сервер.

1. Выберите, сохранить ли конфигурацию в настройках рабочего пространства или в пользовательских настройках.

  - **Настройки рабочего пространства** — конфигурация сохраняется в файле .vscode/mcp.json и доступна только в текущем рабочем пространстве.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    Если выбран транспорт HTTP потоковой передачи, конфигурация будет немного другой:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Пользовательские настройки** — конфигурация добавляется в глобальный файл *settings.json* и доступна во всех рабочих пространствах. Конфигурация выглядит примерно так:

    ![Пользовательские настройки](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Также нужно добавить конфигурацию — заголовок для корректной аутентификации в Azure API Management. Используется заголовок **Ocp-Apim-Subscription-Key**.

    - Вот как его можно добавить в настройки:

    ![Добавление заголовка для аутентификации](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png). После этого появится запрос на ввод значения API ключа, который можно найти в Azure Portal для вашего экземпляра Azure API Management.

   - Чтобы добавить его в *mcp.json*, используйте следующий пример:

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

### Использование режима агента

Теперь, когда всё настроено — либо в настройках, либо в *.vscode/mcp.json*, давайте попробуем.

Должна появиться иконка Инструментов, где отображаются открытые инструменты вашего сервера:

![Инструменты сервера](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Нажмите на иконку инструментов, и вы увидите список инструментов:

    ![Инструменты](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Введите запрос в чат, чтобы вызвать инструмент. Например, если вы выбрали инструмент для получения информации о заказе, можно задать вопрос агенту по заказу. Вот пример запроса:

    ```text
    get information from order 2
    ```

    Вам будет показана иконка инструментов с запросом подтвердить вызов инструмента. Подтвердите выполнение, и вы увидите результат, похожий на этот:

    ![Результат запроса](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **То, что вы видите, зависит от настроенных инструментов, но суть в том, что вы получаете текстовый ответ, как показано выше.**

## Ссылки

Вот где можно узнать больше:

- [Учебник по Azure API Management и MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Пример на Python: Безопасные удалённые MCP серверы с использованием Azure API Management (экспериментально)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Лаборатория по авторизации клиентов MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Использование расширения Azure API Management для VS Code для импорта и управления API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Регистрация и обнаружение удалённых MCP серверов в Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Отличный репозиторий с множеством AI возможностей в Azure API Management
- [Мастер-классы AI Gateway](https://azure-samples.github.io/AI-Gateway/) Содержит мастер-классы с использованием Azure Portal — отличный способ начать изучать AI возможности.

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, имейте в виду, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его родном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.