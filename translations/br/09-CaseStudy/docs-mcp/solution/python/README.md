<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:29:15+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "br"
}
-->
# Gerador de Plano de Estudo com Chainlit & Microsoft Learn Docs MCP

## Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)
- Acesso à internet para conectar ao servidor Microsoft Learn Docs MCP

## Instalação

1. Clone este repositório ou baixe os arquivos do projeto.
2. Instale as dependências necessárias:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

### Cenário 1: Consulta Simples ao Docs MCP
Um cliente de linha de comando que se conecta ao servidor Docs MCP, envia uma consulta e exibe o resultado.

1. Execute o script:
   ```bash
   python scenario1.py
   ```
2. Digite sua pergunta sobre a documentação no prompt.

### Cenário 2: Gerador de Plano de Estudo (Aplicativo Web Chainlit)
Uma interface web (usando Chainlit) que permite aos usuários gerar um plano de estudo personalizado, semana a semana, para qualquer tema técnico.

1. Inicie o app Chainlit:
   ```bash
   chainlit run scenario2.py
   ```
2. Abra a URL local fornecida no seu terminal (exemplo: http://localhost:8000) no navegador.
3. Na janela de chat, informe o tema de estudo e o número de semanas que deseja estudar (exemplo: "certificação AI-900, 8 semanas").
4. O app responderá com um plano de estudo detalhado por semana, incluindo links para a documentação relevante do Microsoft Learn.

**Variáveis de Ambiente Necessárias:**

Para usar o Cenário 2 (app web Chainlit com Azure OpenAI), você deve configurar as seguintes variáveis de ambiente em um diretório `.env` file in the `python`:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Preencha esses valores com os detalhes do seu recurso Azure OpenAI antes de executar o app.

> **Dica:** Você pode facilmente implantar seus próprios modelos usando o [Azure AI Foundry](https://ai.azure.com/).

### Cenário 3: Docs no Editor com MCP Server no VS Code

Ao invés de alternar entre abas do navegador para buscar documentação, você pode trazer o Microsoft Learn Docs diretamente para o VS Code usando o servidor MCP. Isso permite que você:
- Pesquise e leia a documentação dentro do VS Code sem sair do ambiente de desenvolvimento.
- Referencie documentação e insira links diretamente em seus arquivos README ou de curso.
- Use o GitHub Copilot junto com o MCP para um fluxo de trabalho integrado e com suporte de IA para documentação.

**Exemplos de Uso:**
- Adicione rapidamente links de referência em um README enquanto escreve a documentação de um curso ou projeto.
- Use o Copilot para gerar código e o MCP para encontrar e citar documentos relevantes instantaneamente.
- Mantenha o foco no editor e aumente sua produtividade.

> [!IMPORTANT]
> Certifique-se de ter um arquivo válido [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

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

Estes exemplos mostram a flexibilidade do app para diferentes objetivos e prazos de aprendizado.

## Referências

- [Documentação Chainlit](https://docs.chainlit.io/)
- [Documentação MCP](https://github.com/MicrosoftDocs/mcp)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.