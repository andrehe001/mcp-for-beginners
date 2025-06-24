<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "36de9fae488d6de554d969fe8e0801a8",
  "translation_date": "2025-06-20T19:27:12+00:00",
  "source_file": "09-CaseStudy/apimsample.md",
  "language_code": "uk"
}
-->
# Case Study: Відкриття REST API в API Management як MCP сервер

Azure API Management — це сервіс, який надає шлюз поверх ваших API кінцевих точок. Принцип його роботи полягає в тому, що Azure API Management виступає як проксі перед вашими API і може визначати, що робити з вхідними запитами.

Використовуючи його, ви отримуєте цілий ряд функцій, таких як:

- **Безпека** — можна застосовувати все: від API ключів, JWT до керованої ідентичності.
- **Обмеження частоти викликів** — чудова можливість контролювати, скільки запитів проходить за певний проміжок часу. Це допомагає забезпечити відмінний досвід для всіх користувачів і запобігти перевантаженню вашого сервісу.
- **Масштабування та балансування навантаження**. Ви можете налаштувати кілька кінцевих точок для розподілу навантаження і вибрати спосіб балансування.
- **Штучний інтелект, як-от семантичне кешування**, обмеження токенів, моніторинг токенів та інше. Ці функції підвищують швидкодію та допомагають контролювати витрати на токени. [Детальніше тут](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Чому MCP + Azure API Management?

Model Context Protocol швидко стає стандартом для агентських AI-додатків і способу послідовного надання інструментів та даних. Azure API Management — природний вибір, коли потрібно "керувати" API. MCP сервери часто інтегруються з іншими API для обробки запитів до інструментів, наприклад. Тому поєднання Azure API Management і MCP має сенс.

## Огляд

У цьому конкретному випадку ми навчимося відкривати API кінцеві точки як MCP сервер. Це дозволить легко включати ці кінцеві точки до агентських додатків, одночасно використовуючи можливості Azure API Management.

## Ключові особливості

- Ви обираєте методи кінцевих точок, які хочете відкрити як інструменти.
- Додаткові функції залежать від налаштувань у розділі політик для вашого API. Тут ми покажемо, як додати обмеження частоти викликів.

## Попередній крок: імпорт API

Якщо у вас вже є API в Azure API Management — чудово, цей крок можна пропустити. Якщо ні, перегляньте цей посилання: [імпорт API в Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Відкриття API як MCP Server

Щоб відкрити кінцеві точки API, виконайте наступні кроки:

1. Перейдіть до Azure Portal за адресою <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
   Відкрийте ваш екземпляр API Management.

1. У лівому меню оберіть APIs > MCP Servers > + Create new MCP Server.

1. В API оберіть REST API, який хочете відкрити як MCP сервер.

1. Оберіть одну або кілька операцій API, які хочете відкрити як інструменти. Можна вибрати всі операції або лише певні.

    ![Select methods to expose](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Натисніть **Create**.

1. Перейдіть у меню **APIs** та **MCP Servers**, ви побачите наступне:

    ![See the MCP Server in the main pane](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP сервер створено, а операції API відкриті як інструменти. MCP сервер відображається у панелі MCP Servers. У стовпці URL показано кінцеву точку MCP сервера, яку можна викликати для тестування або у клієнтському додатку.

## За бажанням: налаштування політик

Azure API Management базується на концепції політик, де ви задаєте різні правила для кінцевих точок, наприклад обмеження частоти викликів або семантичне кешування. Ці політики описуються у форматі XML.

Ось як можна налаштувати політику для обмеження частоти викликів MCP сервера:

1. У порталі, в розділі APIs, оберіть **MCP Servers**.

1. Виберіть створений MCP сервер.

1. У лівому меню, під MCP, оберіть **Policies**.

1. У редакторі політик додайте або змініть політики, які хочете застосувати до інструментів MCP сервера. Політики визначаються у форматі XML. Наприклад, можна додати політику, яка обмежить кількість викликів інструментів MCP сервера (у цьому прикладі — 5 викликів на 30 секунд з однієї IP-адреси клієнта). Ось XML, який реалізує це обмеження:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Ось зображення редактора політик:

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## Спробуйте

Переконаємося, що наш MCP сервер працює як слід.

Для цього використаємо Visual Studio Code та GitHub Copilot у режимі агента. Ми додамо MCP сервер у *mcp.json*. Таким чином Visual Studio Code виступатиме клієнтом з агентськими можливостями, а кінцеві користувачі зможуть вводити запити і взаємодіяти з сервером.

Як додати MCP сервер у Visual Studio Code:

1. Використайте команду MCP: **Add Server** з Command Palette.

1. Коли з’явиться запит, оберіть тип сервера: **HTTP (HTTP or Server Sent Events)**.

1. Введіть URL MCP сервера в API Management. Приклад: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (для SSE кінцевої точки) або **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (для MCP кінцевої точки). Зверніть увагу на різницю у транспорті — `/sse` or `/mcp`.

1. Введіть ідентифікатор сервера на свій розсуд. Це не критичне значення, але допоможе вам пам’ятати, що це за сервер.

1. Оберіть, де зберегти конфігурацію — у налаштуваннях робочої області або користувача.

  - **Workspace settings** — конфігурація сервера зберігається у файлі .vscode/mcp.json, доступному лише в поточній робочій області.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    Якщо ви оберете стрімінговий HTTP транспорт, конфігурація буде трохи іншою:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **User settings** — конфігурація додається у глобальний файл *settings.json* і доступна у всіх робочих областях. Конфігурація виглядає приблизно так:

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Також потрібно додати конфігурацію заголовка для автентифікації в Azure API Management. Використовується заголовок **Ocp-Apim-Subscription-Key**.

    - Ось як додати його у налаштування:

    ![Adding header for authentication](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), це викличе запит на введення значення API ключа, який можна знайти в Azure Portal для вашого екземпляру Azure API Management.

   - Щоб додати у *mcp.json*, використайте такий формат:

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

### Використання режиму агента

Тепер ми готові — налаштування є або в налаштуваннях, або у *.vscode/mcp.json*. Спробуємо.

Повинна з’явитися іконка Інструментів, де будуть перераховані відкриті інструменти вашого сервера:

![Tools from the server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Натисніть на іконку інструментів, ви побачите список інструментів:

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Введіть запит у чат, щоб викликати інструмент. Наприклад, якщо ви обрали інструмент для отримання інформації про замовлення, можна запитати агента про замовлення. Ось приклад запиту:

    ```text
    get information from order 2
    ```

    Тепер з’явиться іконка інструментів із пропозицією продовжити виклик інструменту. Оберіть продовження, і ви побачите результат, схожий на цей:

    ![Result from prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **те, що ви бачите, залежить від налаштованих інструментів, але ідея полягає в отриманні текстової відповіді, як на зображенні вище**

## Посилання

Ось де можна дізнатися більше:

- [Покрокове керівництво по Azure API Management та MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Приклад на Python: Захищені віддалені MCP сервери з Azure API Management (експериментальний)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Лабораторія авторизації MCP клієнтів](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Використання розширення Azure API Management для VS Code для імпорту та керування API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Реєстрація та виявлення віддалених MCP серверів в Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Відмінний репозиторій, який демонструє багато можливостей AI з Azure API Management
- [Майстер-класи AI Gateway](https://azure-samples.github.io/AI-Gateway/) Містить майстер-класи з використання Azure Portal — чудовий спосіб почати оцінювати можливості AI.

**Відмова від відповідальності**:  
Цей документ був перекладений за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується звертатися до професійного людського перекладу. Ми не несемо відповідальності за будь-які непорозуміння чи неправильні тлумачення, що виникли внаслідок використання цього перекладу.