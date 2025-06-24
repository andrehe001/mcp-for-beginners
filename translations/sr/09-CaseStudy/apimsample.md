<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "36de9fae488d6de554d969fe8e0801a8",
  "translation_date": "2025-06-20T19:25:54+00:00",
  "source_file": "09-CaseStudy/apimsample.md",
  "language_code": "sr"
}
-->
# Студија случаја: Изложите REST API у API Management као MCP сервер

Azure API Management је услуга која пружа Gateway изнад ваших API Endpoint-а. Начин рада је тај што Azure API Management делује као прокси испред ваших API-ја и може одлучити шта ће радити са долазним захтевима.

Коришћењем ове услуге добијате читав низ функција као што су:

- **Безбедност**, можете користити све од API кључева, JWT-а до managed identity.
- **Ограничење броја позива (rate limiting)**, одлична функција која вам омогућава да одлучите колико позива може проћи у одређеном временском интервалу. Ово помаже да сви корисници имају одлично искуство и да ваша услуга не буде преоптерећена захтевима.
- **Скалирање и балансирање оптерећења**. Можете подесити више endpoint-а да расподеле оптерећење и можете одлучити како ће се вршити „load balance“.
- **AI функције као што су семантичко кеширање**, ограничење токена и праћење токена и још много тога. Ове одличне функције побољшавају одзивност и помажу вам да пратите трошкове везане за токене. [Прочитајте више овде](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Зашто MCP + Azure API Management?

Model Context Protocol брзо постаје стандард за agentic AI апликације и начин излагања алата и података на доследан начин. Azure API Management је природан избор када треба да „управљате“ API-јима. MCP сервери често интегришу друге API-је да би решавали захтеве ка алату, на пример. Због тога је комбинација Azure API Management и MCP-а логична.

## Преглед

У овом конкретном случају користи ћемо да научимо како да изложимо API endpoint-е као MCP сервер. На овај начин лако можемо учинити ове endpoint-е делом agentic апликације, а такође користити све предности Azure API Management-а.

## Кључне функције

- Изаберете методе endpoint-а које желите да изложите као алате.
- Додатне функције које добијате зависе од тога шта конфигуришете у policy делу за ваш API. Овде ћемо показати како да додате rate limiting.

## Претходни корак: увоз API-ја

Ако већ имате API у Azure API Management-у, одлично, можете прескочити овај корак. Ако не, погледајте овај линк, [увоз API-ја у Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Изложите API као MCP сервер

Да бисмо изложили API endpoint-е, пратимо следеће кораке:

1. Идите на Azure портал на адресу <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
   Отворите вашу Azure API Management инстанцу.

1. У левом менију изаберите APIs > MCP Servers > + Create new MCP Server.

1. У API делу изаберите REST API који желите да изложите као MCP сервер.

1. Изаберите једну или више API операција које желите да изложите као алате. Можете изабрати све операције или само одређене.

    ![Изаберите методе које ћете изложити](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Изаберите **Create**.

1. Идите у мени опцију **APIs** и **MCP Servers**, требало би да видите следеће:

    ![Погледајте MCP сервер у главном прозору](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP сервер је креиран и API операције су изложене као алати. MCP сервер је наведен у MCP Servers панелу. Колона URL приказује endpoint MCP сервера који можете позвати за тестирање или у оквиру клијент апликације.

## Опционо: Конфигуришите политике

Azure API Management има основни концепт политика у којима подешавате различита правила за ваше endpoint-е, као што су ограничење броја позива или семантичко кеширање. Ове политике се пишу у XML формату.

Ево како можете подесити политику за ограничење броја позива на вашем MCP серверу:

1. У порталу, под APIs изаберите **MCP Servers**.

1. Изаберите MCP сервер који сте креирали.

1. У левом менију, под MCP, изаберите **Policies**.

1. У уређивачу политика додајте или измените политике које желите да примените на алате MCP сервера. Политике су дефинисане у XML формату. На пример, можете додати политику која ограничава позиве алатима MCP сервера (у овом примеру, 5 позива на 30 секунди по IP адреси клијента). Ево XML-а који ће то омогућити:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Ево слике уређивача политика:

    ![Уређивач политика](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## Испробајте

Хајде да проверимо да ли наш MCP сервер ради како треба.

За ово ћемо користити Visual Studio Code и GitHub Copilot у Agent режиму. Додаћемо MCP сервер у *mcp.json* датотеку. На овај начин, Visual Studio Code ће деловати као клијент са agentic могућностима, а крајњи корисници ће моћи да укуцају упит и интерагују са сервером.

Ево како да додате MCP сервер у Visual Studio Code:

1. Користите MCP: **Add Server команду из Command Palette**.

1. Када се затражи, изаберите тип сервера: **HTTP (HTTP или Server Sent Events)**.

1. Унесите URL MCP сервера у API Management-у. Пример: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (за SSE endpoint) или **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (за MCP endpoint), приметите разлику у транспорту која је у `/sse` or `/mcp`.

1. Унесите ID сервера по вашем избору. Ова вредност није пресудна, али ће вам помоћи да запамтите о којој инстанци сервера је реч.

1. Изаберите да ли желите да конфигурацију сачувате у workspace settings или user settings.

  - **Workspace settings** - Конфигурација сервера се чува у .vscode/mcp.json фајлу који је доступан само у тренутном workspace-у.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    или ако одаберете streaming HTTP као транспорт, биће нешто другачије:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **User settings** - Конфигурација сервера се додаје у глобални *settings.json* фајл и доступна је у свим workspace-има. Конфигурација изгледа слично као следеће:

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Потребно је додати и конфигурацију хедера како би аутентификација према Azure API Management радила исправно. Користи се хедер под називом **Ocp-Apim-Subscription-Key**.

    - Ево како да га додате у settings:

    ![Додавање хедера за аутентификацију](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), што ће приказати упит за унос вредности API кључа коју можете пронаћи у Azure порталу за вашу Azure API Management инстанцу.

    - Да бисте га додали у *mcp.json*, урадите то овако:

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

### Користите Agent режим

Сада смо све подесили било у settings или у *.vscode/mcp.json*. Хајде да пробамо.

Требало би да видите иконицу Tools као ову, где су наведени изложени алати са вашег сервера:

![Алатке са сервера](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Кликните на иконицу алата и требало би да видите листу алата овако:

    ![Алатке](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Унесите упит у ћаскање да покренете алат. На пример, ако сте изабрали алат за добијање информација о поруџбини, можете питати агента о поруџбини. Ево примера упита:

    ```text
    get information from order 2
    ```

    Сада ће вам бити приказана иконица алата која тражи да наставите са позивањем алата. Изаберите да наставите са покретањем алата, требало би да видите излаз као овде:

    ![Резултат упита](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **оно што видите зависи од тога које алате сте подесили, али идеја је да добијете текстуални одговор као горе**

## Референце

Ево како можете сазнати више:

- [Туторијал за Azure API Management и MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Python пример: Безбедни удаљени MCP сервери користећи Azure API Management (експериментално)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [MCP client authorization lab](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Користите Azure API Management екстензију за VS Code за увоз и управљање API-јима](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Региструјте и откријте удаљене MCP сервере у Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Одличан репозиторијум који приказује многе AI могућности са Azure API Management
- [AI Gateway радионице](https://azure-samples.github.io/AI-Gateway/) Садржи радионице коришћењем Azure портала, што је одличан начин за почетак процене AI могућности.

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем AI сервиса за превођење [Co-op Translator](https://github.com/Azure/co-op-translator). Иако тежимо прецизности, молимо имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Изворни документ на његовом оригиналном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било какве неспоразуме или погрешне тумачења која произилазе из коришћења овог превода.