<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:32:50+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "bg"
}
-->
# Генератор на учебен план с Chainlit и Microsoft Learn Docs MCP

## Изисквания

- Python 3.8 или по-нова версия  
- pip (мениджър на Python пакети)  
- Интернет връзка за свързване със сървъра на Microsoft Learn Docs MCP  

## Инсталация

1. Клонирайте това хранилище или изтеглете файловете на проекта.  
2. Инсталирайте необходимите зависимости:  

   ```bash
   pip install -r requirements.txt
   ```

## Употреба

### Сценарий 1: Просто запитване към Docs MCP  
Клиент от командния ред, който се свързва със сървъра на Docs MCP, изпраща запитване и отпечатва резултата.

1. Стартирайте скрипта:  
   ```bash
   python scenario1.py
   ```  
2. Въведете вашия въпрос за документацията в подканата.

### Сценарий 2: Генератор на учебен план (уеб приложение Chainlit)  
Уеб интерфейс (използващ Chainlit), който позволява на потребителите да генерират персонализиран, седмичен учебен план за всяка техническа тема.

1. Стартирайте Chainlit приложението:  
   ```bash
   chainlit run scenario2.py
   ```  
2. Отворете локалния URL, който се показва в терминала ви (например http://localhost:8000), в браузъра си.  
3. В чат прозореца въведете темата за учене и броя седмици, които искате да учите (например "AI-900 certification, 8 weeks").  
4. Приложението ще ви отговори със седмичен учебен план, включително връзки към съответната документация на Microsoft Learn.

**Необходими променливи на средата:**

За да използвате Сценарий 2 (уеб приложението Chainlit с Azure OpenAI), трябва да зададете следните променливи на средата в `.env` file in the `python` директорията:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Попълнете тези стойности с детайлите на вашия Azure OpenAI ресурс преди да стартирате приложението.

> **Tip:** Лесно можете да разположите свои модели чрез [Azure AI Foundry](https://ai.azure.com/).

### Сценарий 3: Документация в редактора с MCP сървър във VS Code

Вместо да сменяте раздели в браузъра, за да търсите документация, можете да интегрирате Microsoft Learn Docs директно във VS Code чрез MCP сървъра. Това ви позволява:  
- Да търсите и четете документация в VS Code без да напускате средата за програмиране.  
- Да добавяте препратки към документация и връзки директно в README или учебните файлове.  
- Да използвате GitHub Copilot и MCP за безпроблемна AI-поддържана работа с документация.

**Примери за употреба:**  
- Бързо добавяне на препратки в README, докато пишете курс или проектна документация.  
- Използване на Copilot за генериране на код и MCP за незабавно намиране и цитиране на подходяща документация.  
- Оставате фокусирани в редактора и повишавате продуктивността си.

> [!IMPORTANT]  
> Уверете се, че имате валиден [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

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

Тези примери показват гъвкавостта на приложението за различни учебни цели и времеви рамки.

## Референции

- [Chainlit Documentation](https://docs.chainlit.io/)  
- [MCP Documentation](https://github.com/MicrosoftDocs/mcp)

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за каквито и да е недоразумения или неправилни тълкувания, произтичащи от използването на този превод.