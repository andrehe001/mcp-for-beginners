<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5384bbb2a92d00d5d7e66274dbe0331d",
  "translation_date": "2025-06-20T18:33:10+00:00",
  "source_file": "04-PracticalImplementation/README.md",
  "language_code": "pt"
}
-->
# Implementação Prática

A implementação prática é onde o poder do Model Context Protocol (MCP) se torna tangível. Embora compreender a teoria e a arquitetura por trás do MCP seja importante, o verdadeiro valor surge quando aplicamos estes conceitos para construir, testar e implementar soluções que resolvem problemas do mundo real. Este capítulo faz a ponte entre o conhecimento conceptual e o desenvolvimento prático, guiando-o no processo de dar vida a aplicações baseadas em MCP.

Quer esteja a desenvolver assistentes inteligentes, a integrar IA em fluxos de trabalho empresariais ou a criar ferramentas personalizadas para processamento de dados, o MCP oferece uma base flexível. O seu design independente da linguagem e os SDKs oficiais para linguagens de programação populares tornam-no acessível a uma vasta gama de programadores. Ao aproveitar estes SDKs, pode prototipar rapidamente, iterar e escalar as suas soluções em diferentes plataformas e ambientes.

Nas secções seguintes, encontrará exemplos práticos, código de exemplo e estratégias de implementação que demonstram como implementar MCP em C#, Java, TypeScript, JavaScript e Python. Também aprenderá como depurar e testar os seus servidores MCP, gerir APIs e implementar soluções na cloud usando Azure. Estes recursos práticos foram concebidos para acelerar a sua aprendizagem e ajudá-lo a construir com confiança aplicações MCP robustas e prontas para produção.

## Visão Geral

Esta lição foca-se nos aspetos práticos da implementação do MCP em várias linguagens de programação. Vamos explorar como usar os SDKs MCP em C#, Java, TypeScript, JavaScript e Python para construir aplicações robustas, depurar e testar servidores MCP, e criar recursos, prompts e ferramentas reutilizáveis.

## Objetivos de Aprendizagem

No final desta lição, será capaz de:
- Implementar soluções MCP usando SDKs oficiais em várias linguagens de programação
- Depurar e testar servidores MCP de forma sistemática
- Criar e usar funcionalidades do servidor (Recursos, Prompts e Ferramentas)
- Projetar fluxos de trabalho MCP eficazes para tarefas complexas
- Otimizar implementações MCP para desempenho e fiabilidade

## Recursos Oficiais dos SDKs

O Model Context Protocol oferece SDKs oficiais para várias linguagens:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) 
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

## Trabalhar com os SDKs MCP

Esta secção apresenta exemplos práticos de implementação do MCP em várias linguagens de programação. Pode encontrar código de exemplo no diretório `samples` organizado por linguagem.

### Exemplos Disponíveis

O repositório inclui [implementações de exemplo](../../../04-PracticalImplementation/samples) nas seguintes linguagens:

- [C#](./samples/csharp/README.md)
- [Java](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Cada exemplo demonstra conceitos-chave do MCP e padrões de implementação para essa linguagem e ecossistema específicos.

## Funcionalidades Principais do Servidor

Os servidores MCP podem implementar qualquer combinação destas funcionalidades:

### Recursos
Os recursos fornecem contexto e dados para o utilizador ou modelo de IA usar:
- Repositórios de documentos
- Bases de conhecimento
- Fontes de dados estruturados
- Sistemas de ficheiros

### Prompts
Os prompts são mensagens e fluxos de trabalho modelados para os utilizadores:
- Templates de conversação pré-definidos
- Padrões de interação guiada
- Estruturas de diálogo especializadas

### Ferramentas
As ferramentas são funções que o modelo de IA pode executar:
- Utilitários de processamento de dados
- Integrações com APIs externas
- Capacidades computacionais
- Funcionalidade de pesquisa

## Implementações de Exemplo: C#

O repositório oficial do SDK C# contém várias implementações de exemplo que demonstram diferentes aspetos do MCP:

- **Cliente MCP Básico**: Exemplo simples que mostra como criar um cliente MCP e chamar ferramentas
- **Servidor MCP Básico**: Implementação mínima de servidor com registo básico de ferramentas
- **Servidor MCP Avançado**: Servidor completo com registo de ferramentas, autenticação e tratamento de erros
- **Integração ASP.NET**: Exemplos que demonstram integração com ASP.NET Core
- **Padrões de Implementação de Ferramentas**: Vários padrões para implementar ferramentas com diferentes níveis de complexidade

O SDK MCP C# está em pré-visualização e as APIs podem mudar. Iremos atualizar este blog continuamente à medida que o SDK evolui.

### Funcionalidades Principais 
- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)

- Construir o seu [primeiro Servidor MCP](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

Para exemplos completos de implementação em C#, visite o [repositório oficial de exemplos do SDK C#](https://github.com/modelcontextprotocol/csharp-sdk)

## Implementação de Exemplo: Java

O SDK Java oferece opções robustas de implementação MCP com funcionalidades de nível empresarial.

### Funcionalidades Principais

- Integração com Spring Framework
- Forte tipagem
- Suporte a programação reativa
- Tratamento de erros abrangente

Para um exemplo completo de implementação em Java, consulte o [exemplo Java](samples/java/containerapp/README.md) no diretório de exemplos.

## Implementação de Exemplo: JavaScript

O SDK JavaScript oferece uma abordagem leve e flexível para implementação MCP.

### Funcionalidades Principais

- Suporte para Node.js e browser
- API baseada em Promises
- Integração fácil com Express e outros frameworks
- Suporte WebSocket para streaming

Para um exemplo completo de implementação em JavaScript, consulte o [exemplo JavaScript](samples/javascript/README.md) no diretório de exemplos.

## Implementação de Exemplo: Python

O SDK Python oferece uma abordagem Pythonica para a implementação MCP com excelentes integrações com frameworks de ML.

### Funcionalidades Principais

- Suporte async/await com asyncio
- Integração com Flask e FastAPI
- Registo simples de ferramentas
- Integração nativa com bibliotecas populares de ML

Para um exemplo completo de implementação em Python, consulte o [exemplo Python](samples/python/README.md) no diretório de exemplos.

## Gestão de API

O Azure API Management é uma excelente solução para garantir a segurança dos Servidores MCP. A ideia é colocar uma instância do Azure API Management à frente do seu Servidor MCP e deixar que esta trate funcionalidades que provavelmente vai querer, como:

- limitação de taxa
- gestão de tokens
- monitorização
- balanceamento de carga
- segurança

### Exemplo Azure

Aqui está um exemplo Azure que faz exatamente isso, ou seja, [criar um Servidor MCP e protegê-lo com Azure API Management](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Veja como decorre o fluxo de autorização na imagem abaixo:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true) 

Na imagem anterior, ocorre o seguinte:

- A autenticação/autorização é feita usando Microsoft Entra.
- O Azure API Management atua como um gateway e usa políticas para direcionar e gerir o tráfego.
- O Azure Monitor regista todas as solicitações para análise posterior.

#### Fluxo de autorização

Vamos analisar o fluxo de autorização com mais detalhe:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### Especificação de autorização MCP

Saiba mais sobre a [especificação de Autorização MCP](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization#2-10-third-party-authorization-flow)

## Implementar Servidor MCP Remoto no Azure

Vamos ver se conseguimos implementar o exemplo que mencionámos anteriormente:

1. Clone o repositório

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

2. Registe `Microsoft.App` resource provider.
    * If you are using Azure CLI, run `az provider register --namespace Microsoft.App --wait`.
    * If you are using Azure PowerShell, run `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Then run `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` e, passado algum tempo, verifique se o registo está concluído.

3. Execute este comando [azd](https://aka.ms/azd) para provisionar o serviço de gestão de API, a function app (com código) e todos os outros recursos Azure necessários

    ```shell
    azd up
    ```

    Este comando deverá implementar todos os recursos na cloud Azure

### Testar o seu servidor com MCP Inspector

1. Numa **nova janela de terminal**, instale e execute o MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Deve ver uma interface semelhante a esta:

    ![Connect to Node inspector](../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.pt.png) 

2. CTRL clique para carregar a aplicação web MCP Inspector a partir da URL mostrada pela aplicação (ex. http://127.0.0.1:6274/#resources)
3. Defina o tipo de transporte para `SSE`
1. Set the URL to your running API Management SSE endpoint displayed after `azd up` e clique em **Connect**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

5. **Listar Ferramentas**. Clique numa ferramenta e **Execute a Ferramenta**.  

Se todos os passos correram bem, deverá agora estar ligado ao servidor MCP e ter conseguido chamar uma ferramenta.

## Servidores MCP para Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Este conjunto de repositórios são templates de início rápido para construir e implementar servidores MCP (Model Context Protocol) remotos personalizados usando Azure Functions com Python, C# .NET ou Node/TypeScript.

Os exemplos fornecem uma solução completa que permite aos programadores:

- Construir e executar localmente: desenvolver e depurar um servidor MCP numa máquina local
- Implementar no Azure: implementar facilmente na cloud com um simples comando azd up
- Ligar a partir de clientes: conectar ao servidor MCP a partir de vários clientes, incluindo o modo agente Copilot do VS Code e a ferramenta MCP Inspector

### Funcionalidades Principais:

- Segurança por design: o servidor MCP está protegido usando chaves e HTTPS
- Opções de autenticação: suporta OAuth usando autenticação integrada e/ou API Management
- Isolamento de rede: permite isolamento de rede usando Redes Virtuais Azure (VNET)
- Arquitetura serverless: aproveita Azure Functions para execução escalável e orientada a eventos
- Desenvolvimento local: suporte abrangente para desenvolvimento e depuração local
- Implementação simples: processo de implementação simplificado para Azure

O repositório inclui todos os ficheiros de configuração necessários, código fonte e definições de infraestrutura para começar rapidamente com uma implementação de servidor MCP pronta para produção.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Implementação de exemplo do MCP usando Azure Functions com Python

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Implementação de exemplo do MCP usando Azure Functions com C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Implementação de exemplo do MCP usando Azure Functions com Node/TypeScript.

## Principais Conclusões

- Os SDKs MCP fornecem ferramentas específicas para cada linguagem para implementar soluções MCP robustas
- O processo de depuração e teste é crítico para aplicações MCP fiáveis
- Templates de prompts reutilizáveis permitem interações consistentes com a IA
- Fluxos de trabalho bem desenhados podem orquestrar tarefas complexas usando múltiplas ferramentas
- Implementar soluções MCP requer atenção à segurança, desempenho e tratamento de erros

## Exercício

Desenhe um fluxo de trabalho MCP prático que resolva um problema real na sua área:

1. Identifique 3-4 ferramentas que seriam úteis para resolver esse problema
2. Crie um diagrama do fluxo de trabalho mostrando como estas ferramentas interagem
3. Implemente uma versão básica de uma das ferramentas na sua linguagem preferida
4. Crie um template de prompt que ajude o modelo a usar eficazmente a sua ferramenta

## Recursos Adicionais


---

Próximo: [Tópicos Avançados](../05-AdvancedTopics/README.md)

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes do uso desta tradução.