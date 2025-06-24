<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:33:00+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "sr"
}
-->
# Генератор плана учења са Chainlit и Microsoft Learn Docs MCP

## Предуслови

- Python 3.8 или новији
- pip (менаџер пакета за Python)
- Интернет веза за повезивање са Microsoft Learn Docs MCP сервером

## Инсталација

1. Клонирајте овај репозиторијум или преузмите фајлове пројекта.
2. Инсталирајте потребне зависности:

   ```bash
   pip install -r requirements.txt
   ```

## Коришћење

### Сценарио 1: Једноставан упит према Docs MCP
Командно-линијски клијент који се повезује на Docs MCP сервер, шаље упит и исписује резултат.

1. Покрените скрипту:
   ```bash
   python scenario1.py
   ```
2. Унесите питање везано за документацију када вам се то затражи.

### Сценарио 2: Генератор плана учења (Chainlit веб апликација)
Веб интерфејс (користећи Chainlit) који омогућава корисницима да генеришу персонализовани, недељни план учења за било коју техничку тему.

1. Покрените Chainlit апликацију:
   ```bash
   chainlit run scenario2.py
   ```
2. Отворите локални URL који вам је дат у терминалу (нпр. http://localhost:8000) у вашем претраживачу.
3. У ћаскању унесите тему учења и број недеља колико желите да учите (нпр. "AI-900 сертификација, 8 недеља").
4. Апликација ће вам вратити недељни план учења, укључујући линкове ка релевантној Microsoft Learn документацији.

**Потребне променљиве окружења:**

Да бисте користили Сценарио 2 (Chainlit веб апликацију са Azure OpenAI), морате подесити следеће променљиве окружења у `.env` file in the `python` фолдеру:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Попуните ове вредности са детаљима вашег Azure OpenAI ресурса пре покретања апликације.

> **Савет:** Лако можете да имплементирате своје моделе користећи [Azure AI Foundry](https://ai.azure.com/).

### Сценарио 3: Документација у уређивачу са MCP сервером у VS Code

Уместо да мењате табове у претраживачу да бисте тражили документацију, можете довести Microsoft Learn Docs директно у VS Code користећи MCP сервер. Ово вам омогућава да:
- Претражујете и читате документацију унутар VS Code-а без напуштања окружења за програмирање.
- Референцирате документацију и убацујете линкове директно у README или фајлове курса.
- Користите GitHub Copilot и MCP за беспрекорну, AI-подржану радну динамику са документацијом.

**Примери коришћења:**
- Брзо додавање референци у README док пишете документацију за курс или пројекат.
- Коришћење Copilot-а за генерисање кода и MCP-а за тренутно проналажење и цитирање релевантне документације.
- Останите фокусирани у уређивачу и повећајте продуктивност.

> [!IMPORTANT]
> Проверите да ли имате валидан [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

## Why Chainlit for Scenario 2?

Chainlit is a modern open-source framework for building conversational web applications. It makes it easy to create chat-based user interfaces that connect to backend services like the Microsoft Learn Docs MCP server. This project uses Chainlit to provide a simple, interactive way to generate personalized study plans in real time. By leveraging Chainlit, you can quickly build and deploy chat-based tools that enhance productivity and learning.

## What This Does

This app allows users to create a personalized study plan by simply entering a topic and a duration. The app parses your input, queries the Microsoft Learn Docs MCP server for relevant content, and organizes the results into a structured, week-by-week plan. Each week’s recommendations are displayed in the chat, making it easy to follow and track your progress. The integration ensures you always get the latest, most relevant learning resources.

## Sample Queries

Try these queries in the chat window to see how the app responds:

- `AI-900 сертификација, 8 недеља`
- `Learn Azure Functions, 4 недеље`
- `Azure DevOps, 6 недеља`
- `Data engineering on Azure, 10 недеља`
- `Microsoft security fundamentals, 5 недеља`
- `Power Platform, 7 недеља`
- `Azure AI services, 12 недеља`
- `Cloud architecture, 9 недеља`

Ови примери показују флексибилност апликације за различите циљеве учења и временске оквире.

## Референце

- [Chainlit документација](https://docs.chainlit.io/)
- [MCP документација](https://github.com/MicrosoftDocs/mcp)

**Одрицање од одговорности**:  
Овај документ је преведен помоћу АИ преводилачке услуге [Co-op Translator](https://github.com/Azure/co-op-translator). Иако се трудимо да превод буде прецизан, молимо вас да имате у виду да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати ауторитетним извором. За критичне информације препоручује се професионални људски превод. Нисмо одговорни за било каква неспоразума или погрешне тумачења која произилазе из коришћења овог превода.