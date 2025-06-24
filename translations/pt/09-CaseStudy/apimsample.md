<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "36de9fae488d6de554d969fe8e0801a8",
  "translation_date": "2025-06-20T19:18:26+00:00",
  "source_file": "09-CaseStudy/apimsample.md",
  "language_code": "pt"
}
-->
# Estudo de Caso: Expor REST API no API Management como um servidor MCP

Azure API Management é um serviço que fornece um Gateway sobre os seus endpoints de API. O seu funcionamento baseia-se no facto de o Azure API Management atuar como um proxy à frente das suas APIs, podendo decidir o que fazer com os pedidos recebidos.

Ao utilizá-lo, adiciona uma série de funcionalidades, tais como:

- **Segurança**, pode usar desde chaves de API, JWT até identidade gerida.
- **Limitação de taxa**, uma funcionalidade excelente que permite decidir quantas chamadas são permitidas por unidade de tempo. Isto ajuda a garantir que todos os utilizadores têm uma boa experiência e que o seu serviço não fica sobrecarregado com pedidos.
- **Escalabilidade e balanceamento de carga**. Pode configurar vários endpoints para distribuir a carga e também decidir como fazer o "balanceamento de carga".
- **Funcionalidades de IA como caching semântico**, limite de tokens, monitorização de tokens e mais. São funcionalidades ótimas que melhoram a capacidade de resposta e ajudam a controlar os gastos com tokens. [Leia mais aqui](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Porquê MCP + Azure API Management?

O Model Context Protocol está rapidamente a tornar-se um padrão para aplicações de IA agentiva e para expor ferramentas e dados de forma consistente. O Azure API Management é uma escolha natural quando precisa de "gerir" APIs. Os servidores MCP frequentemente se integram com outras APIs para resolver pedidos a uma ferramenta, por exemplo. Portanto, combinar Azure API Management e MCP faz muito sentido.

## Visão Geral

Neste caso de uso específico, vamos aprender a expor endpoints de API como um Servidor MCP. Ao fazer isto, podemos facilmente tornar estes endpoints parte de uma aplicação agentiva, aproveitando também as funcionalidades do Azure API Management.

## Funcionalidades Principais

- Seleciona os métodos do endpoint que quer expor como ferramentas.
- As funcionalidades adicionais que obtém dependem do que configurar na secção de políticas para a sua API. Aqui vamos mostrar como adicionar limitação de taxa.

## Passo prévio: importar uma API

Se já tem uma API no Azure API Management, ótimo, pode saltar este passo. Caso contrário, consulte este link, [importar uma API para o Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Expor API como Servidor MCP

Para expor os endpoints da API, siga estes passos:

1. Navegue até ao Portal Azure e ao endereço <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
   Aceda à sua instância do API Management.

1. No menu lateral, selecione APIs > MCP Servers > + Criar novo Servidor MCP.

1. Em API, selecione uma REST API para expor como servidor MCP.

1. Selecione uma ou mais operações da API para expor como ferramentas. Pode selecionar todas as operações ou apenas operações específicas.

    ![Selecionar métodos para expor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Selecione **Criar**.

1. Navegue para a opção de menu **APIs** e **MCP Servers**, deverá ver o seguinte:

    ![Ver o Servidor MCP no painel principal](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    O servidor MCP está criado e as operações da API estão expostas como ferramentas. O servidor MCP aparece listado no painel MCP Servers. A coluna URL mostra o endpoint do servidor MCP que pode usar para testes ou dentro de uma aplicação cliente.

## Opcional: Configurar políticas

O Azure API Management tem o conceito central de políticas, onde define regras diferentes para os seus endpoints, como por exemplo limitação de taxa ou caching semântico. Estas políticas são escritas em XML.

Veja como configurar uma política para limitar a taxa do seu Servidor MCP:

1. No portal, em APIs, selecione **MCP Servers**.

1. Selecione o servidor MCP que criou.

1. No menu lateral, sob MCP, selecione **Policies**.

1. No editor de políticas, adicione ou edite as políticas que quer aplicar às ferramentas do servidor MCP. As políticas são definidas em formato XML. Por exemplo, pode adicionar uma política para limitar as chamadas às ferramentas do servidor MCP (neste exemplo, 5 chamadas por 30 segundos por endereço IP do cliente). Este é o XML que irá aplicar a limitação de taxa:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Aqui está uma imagem do editor de políticas:

    ![Editor de políticas](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Experimente

Vamos garantir que o nosso Servidor MCP está a funcionar como esperado.

Para isso, vamos usar o Visual Studio Code e o GitHub Copilot no modo Agent. Vamos adicionar o servidor MCP a um *mcp.json*. Desta forma, o Visual Studio Code atuará como um cliente com capacidades agentivas e os utilizadores finais poderão escrever um prompt e interagir com esse servidor.

Veja como adicionar o servidor MCP no Visual Studio Code:

1. Use o comando MCP: **Add Server a partir do Command Palette**.

1. Quando solicitado, selecione o tipo de servidor: **HTTP (HTTP ou Server Sent Events)**.

1. Introduza a URL do servidor MCP no API Management. Exemplo: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (para endpoint SSE) ou **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (para endpoint MCP), note a diferença entre os transportes que é `/sse` or `/mcp`.

1. Introduza um ID para o servidor à sua escolha. Este valor não é crítico, mas ajuda a lembrar qual é esta instância do servidor.

1. Selecione se quer guardar a configuração nas definições do workspace ou nas definições do utilizador.

  - **Definições do workspace** - A configuração do servidor é guardada num ficheiro .vscode/mcp.json disponível apenas no workspace atual.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    ou, se escolher o transporte HTTP em streaming, será ligeiramente diferente:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Definições do utilizador** - A configuração do servidor é adicionada ao ficheiro global *settings.json* e está disponível em todos os workspaces. A configuração é semelhante à seguinte:

    ![Definição do utilizador](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Também precisa de adicionar uma configuração, um header para garantir que a autenticação funciona corretamente com o Azure API Management. Usa um header chamado **Ocp-Apim-Subscription-Key**.

    - Veja como pode adicioná-lo às definições:

    ![Adicionar header para autenticação](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), isto fará com que apareça um prompt a pedir o valor da chave API, que pode encontrar no Portal Azure para a sua instância do Azure API Management.

   - Para adicionar ao *mcp.json* em vez disso, pode fazê-lo assim:

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

### Usar modo Agent

Agora que está tudo configurado, seja nas definições ou no *.vscode/mcp.json*, vamos experimentar.

Deve existir um ícone de Ferramentas assim, onde as ferramentas expostas pelo seu servidor estão listadas:

![Ferramentas do servidor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Clique no ícone das ferramentas e deverá ver uma lista de ferramentas assim:

    ![Ferramentas](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Introduza um prompt no chat para invocar a ferramenta. Por exemplo, se selecionou uma ferramenta para obter informação sobre uma encomenda, pode perguntar ao agente sobre uma encomenda. Aqui está um exemplo de prompt:

    ```text
    get information from order 2
    ```

    Agora será apresentado um ícone de ferramentas a pedir para continuar a chamada da ferramenta. Selecione para continuar a executar a ferramenta, deverá ver uma saída assim:

    ![Resultado do prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **o que vê acima depende das ferramentas que configurou, mas a ideia é que obtenha uma resposta textual como a mostrada**

## Referências

Aqui pode aprender mais:

- [Tutorial sobre Azure API Management e MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Exemplo em Python: Servidores MCP remotos seguros usando Azure API Management (experimental)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Laboratório de autorização de cliente MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Use a extensão Azure API Management para VS Code para importar e gerir APIs](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Registar e descobrir servidores MCP remotos no Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Repositório excelente que mostra muitas capacidades de IA com Azure API Management
- [Workshops AI Gateway](https://azure-samples.github.io/AI-Gateway/) Contém workshops usando o Portal Azure, uma ótima forma de começar a avaliar capacidades de IA.

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em atenção que traduções automáticas podem conter erros ou imprecisões. O documento original no seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.