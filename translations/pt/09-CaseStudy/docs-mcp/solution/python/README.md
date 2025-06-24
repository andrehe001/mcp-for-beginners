<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:29:06+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "pt"
}
-->
# Gerador de Plano de Estudo com Chainlit & Microsoft Learn Docs MCP

## Pré-requisitos

- Python 3.8 ou superior
- pip (gestor de pacotes Python)
- Acesso à Internet para conectar ao servidor Microsoft Learn Docs MCP

## Instalação

1. Clone este repositório ou faça o download dos ficheiros do projeto.
2. Instale as dependências necessárias:

   ```bash
   pip install -r requirements.txt
   ```

## Utilização

### Cenário 1: Consulta Simples ao Docs MCP  
Um cliente de linha de comando que se conecta ao servidor Docs MCP, envia uma consulta e imprime o resultado.

1. Execute o script:  
   ```bash
   python scenario1.py
   ```  
2. Insira a sua pergunta sobre a documentação no prompt.

### Cenário 2: Gerador de Plano de Estudo (Aplicação Web Chainlit)  
Uma interface web (usando Chainlit) que permite aos utilizadores gerar um plano de estudo personalizado, semana a semana, para qualquer tema técnico.

1. Inicie a aplicação Chainlit:  
   ```bash
   chainlit run scenario2.py
   ```  
2. Abra a URL local fornecida no terminal (ex.: http://localhost:8000) no seu navegador.  
3. Na janela de chat, escreva o tema que pretende estudar e o número de semanas (ex.: "Certificação AI-900, 8 semanas").  
4. A aplicação responderá com um plano de estudo detalhado por semanas, incluindo links para a documentação relevante da Microsoft Learn.

**Variáveis de Ambiente Necessárias:**

Para usar o Cenário 2 (a aplicação web Chainlit com Azure OpenAI), deve definir as seguintes variáveis de ambiente numa diretoria `.env` file in the `python`:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Preencha estes valores com os detalhes do seu recurso Azure OpenAI antes de executar a aplicação.

> **Dica:** Pode facilmente implementar os seus próprios modelos usando o [Azure AI Foundry](https://ai.azure.com/).

### Cenário 3: Documentação no Editor com o Servidor MCP no VS Code

Em vez de mudar de separador no navegador para pesquisar documentação, pode trazer a documentação Microsoft Learn diretamente para o seu VS Code usando o servidor MCP. Isto permite-lhe:  
- Pesquisar e ler documentação dentro do VS Code sem sair do ambiente de programação.  
- Referenciar documentação e inserir links diretamente nos seus ficheiros README ou de curso.  
- Usar o GitHub Copilot e o MCP em conjunto para um fluxo de trabalho de documentação assistido por IA sem interrupções.

**Exemplos de Utilização:**  
- Adicionar rapidamente links de referência a um README enquanto escreve documentação de um curso ou projeto.  
- Usar o Copilot para gerar código e o MCP para encontrar e citar documentação relevante de imediato.  
- Manter o foco no editor e aumentar a produtividade.

> [!IMPORTANT]  
> Certifique-se de que possui um ficheiro válido [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

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

Estes exemplos demonstram a flexibilidade da aplicação para diferentes objetivos de aprendizagem e prazos.

## Referências

- [Documentação Chainlit](https://docs.chainlit.io/)  
- [Documentação MCP](https://github.com/MicrosoftDocs/mcp)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em atenção que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional realizada por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.