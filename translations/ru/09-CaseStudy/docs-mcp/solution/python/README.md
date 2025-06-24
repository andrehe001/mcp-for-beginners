<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:26:31+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "ru"
}
-->
# Генератор учебного плана с Chainlit и Microsoft Learn Docs MCP

## Требования

- Python 3.8 или выше  
- pip (менеджер пакетов Python)  
- Доступ в интернет для подключения к серверу Microsoft Learn Docs MCP  

## Установка

1. Клонируйте этот репозиторий или скачайте файлы проекта.  
2. Установите необходимые зависимости:  

   ```bash
   pip install -r requirements.txt
   ```

## Использование

### Сценарий 1: Простой запрос к Docs MCP  
Клиент командной строки, который подключается к серверу Docs MCP, отправляет запрос и выводит результат.

1. Запустите скрипт:  
   ```bash
   python scenario1.py
   ```  
2. Введите ваш вопрос по документации в появившейся строке ввода.

### Сценарий 2: Генератор учебного плана (веб-приложение Chainlit)  
Веб-интерфейс (на базе Chainlit), позволяющий пользователям создавать персонализированный учебный план на каждую неделю по любой технической теме.

1. Запустите приложение Chainlit:  
   ```bash
   chainlit run scenario2.py
   ```  
2. Откройте локальный URL, указанный в терминале (например, http://localhost:8000), в вашем браузере.  
3. В окне чата введите тему для изучения и количество недель (например, "AI-900 certification, 8 weeks").  
4. Приложение ответит учебным планом по неделям с ссылками на соответствующую документацию Microsoft Learn.

**Необходимые переменные окружения:**  

Для использования сценария 2 (веб-приложения Chainlit с Azure OpenAI) необходимо задать следующие переменные окружения в файле `.env` file in the `python`:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Заполните эти значения данными вашего ресурса Azure OpenAI перед запуском приложения.

> **Tip:** Вы можете легко развернуть свои модели с помощью [Azure AI Foundry](https://ai.azure.com/).

### Сценарий 3: Документация в редакторе с MCP сервером в VS Code

Вместо переключения между вкладками браузера для поиска документации вы можете интегрировать Microsoft Learn Docs прямо в VS Code с помощью MCP сервера. Это позволит вам:  
- Искать и читать документацию внутри VS Code, не покидая рабочее пространство.  
- Вставлять ссылки на документацию прямо в README или файлы курса.  
- Использовать GitHub Copilot и MCP вместе для удобной работы с документацией на базе ИИ.

**Примеры использования:**  
- Быстро добавлять ссылки на документацию в README при написании курсов или проектов.  
- Использовать Copilot для генерации кода и MCP для мгновенного поиска и цитирования нужной документации.  
- Оставаться сосредоточенным в редакторе и повышать продуктивность.

> [!IMPORTANT]  
> Убедитесь, что у вас есть корректный файл [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

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

Эти примеры демонстрируют гибкость приложения для разных целей обучения и временных рамок.

## Ссылки

- [Chainlit Documentation](https://docs.chainlit.io/)  
- [MCP Documentation](https://github.com/MicrosoftDocs/mcp)

**Отказ от ответственности**:  
Этот документ был переведен с помощью сервиса автоматического перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, просим учитывать, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для критически важной информации рекомендуется профессиональный перевод человеком. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.