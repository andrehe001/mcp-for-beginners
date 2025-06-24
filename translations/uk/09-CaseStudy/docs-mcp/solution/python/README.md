<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:33:41+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "uk"
}
-->
# Генератор плану навчання з Chainlit та Microsoft Learn Docs MCP

## Вимоги

- Python 3.8 або новіша версія
- pip (менеджер пакетів Python)
- Доступ до Інтернету для підключення до сервера Microsoft Learn Docs MCP

## Встановлення

1. Клонуйте цей репозиторій або завантажте файли проекту.
2. Встановіть необхідні залежності:

   ```bash
   pip install -r requirements.txt
   ```

## Використання

### Сценарій 1: Простий запит до Docs MCP
Клієнт командного рядка, який підключається до сервера Docs MCP, надсилає запит і виводить результат.

1. Запустіть скрипт:
   ```bash
   python scenario1.py
   ```
2. Введіть своє запитання до документації у запиті.

### Сценарій 2: Генератор плану навчання (веб-додаток Chainlit)
Веб-інтерфейс (на базі Chainlit), який дозволяє користувачам створювати персоналізований покроковий план навчання на будь-яку технічну тему.

1. Запустіть додаток Chainlit:
   ```bash
   chainlit run scenario2.py
   ```
2. Відкрийте локальну URL-адресу, що з’явиться у вашому терміналі (наприклад, http://localhost:8000), у браузері.
3. У вікні чату введіть тему для навчання та кількість тижнів, протягом яких плануєте вчитися (наприклад, "AI-900 certification, 8 weeks").
4. Додаток надасть покроковий план на тиждень, включно з посиланнями на відповідну документацію Microsoft Learn.

**Необхідні змінні середовища:**

Щоб використовувати сценарій 2 (веб-додаток Chainlit з Azure OpenAI), потрібно встановити такі змінні середовища у файлі `.env` file in the `python`:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Заповніть ці значення відповідно до даних вашого ресурсу Azure OpenAI перед запуском додатка.

> **Порада:** Ви можете легко розгорнути власні моделі за допомогою [Azure AI Foundry](https://ai.azure.com/).

### Сценарій 3: Документація в редакторі з MCP сервером у VS Code

Замість того, щоб перемикатися між вкладками браузера для пошуку документації, ви можете інтегрувати Microsoft Learn Docs безпосередньо у VS Code за допомогою MCP сервера. Це дозволяє:
- Шукати та читати документацію у VS Code, не виходячи з робочого середовища.
- Посилатися на документацію та вставляти посилання безпосередньо у README або файли курсу.
- Використовувати GitHub Copilot разом із MCP для безперебійної роботи з документацією на основі ШІ.

**Приклади використання:**
- Швидко додавати посилання на документацію у README під час написання курсу або проектної документації.
- Використовувати Copilot для генерації коду та MCP для миттєвого пошуку і цитування релевантної документації.
- Залишатися зосередженим у редакторі та підвищувати продуктивність.

> [!IMPORTANT]
> Переконайтеся, що у вас є дійсний [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

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

Ці приклади демонструють гнучкість додатка для різних навчальних цілей і термінів.

## Джерела

- [Chainlit Documentation](https://docs.chainlit.io/)
- [MCP Documentation](https://github.com/MicrosoftDocs/mcp)

**Відмова від відповідальності**:  
Цей документ було перекладено за допомогою сервісу автоматичного перекладу [Co-op Translator](https://github.com/Azure/co-op-translator). Хоча ми прагнемо до точності, будь ласка, майте на увазі, що автоматичні переклади можуть містити помилки або неточності. Оригінальний документ рідною мовою слід вважати авторитетним джерелом. Для критично важливої інформації рекомендується професійний переклад людиною. Ми не несемо відповідальності за будь-які непорозуміння чи неправильні тлумачення, що виникли внаслідок використання цього перекладу.