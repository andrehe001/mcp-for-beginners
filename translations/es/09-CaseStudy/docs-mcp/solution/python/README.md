<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:26:15+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "es"
}
-->
# Generador de Plan de Estudio con Chainlit y Microsoft Learn Docs MCP

## Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Acceso a Internet para conectarse al servidor Microsoft Learn Docs MCP

## Instalación

1. Clona este repositorio o descarga los archivos del proyecto.
2. Instala las dependencias necesarias:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

### Escenario 1: Consulta Simple a Docs MCP
Un cliente de línea de comandos que se conecta al servidor Docs MCP, envía una consulta y muestra el resultado.

1. Ejecuta el script:
   ```bash
   python scenario1.py
   ```
2. Escribe tu pregunta sobre la documentación en el prompt.

### Escenario 2: Generador de Plan de Estudio (Aplicación Web Chainlit)
Una interfaz web (usando Chainlit) que permite a los usuarios generar un plan de estudio personalizado, semana a semana, para cualquier tema técnico.

1. Inicia la aplicación Chainlit:
   ```bash
   chainlit run scenario2.py
   ```
2. Abre la URL local que aparece en tu terminal (por ejemplo, http://localhost:8000) en tu navegador.
3. En la ventana de chat, escribe el tema que quieres estudiar y el número de semanas que deseas dedicar (por ejemplo, "Certificación AI-900, 8 semanas").
4. La aplicación responderá con un plan de estudio semanal, incluyendo enlaces a la documentación relevante de Microsoft Learn.

**Variables de Entorno Requeridas:**

Para usar el Escenario 2 (la aplicación web Chainlit con Azure OpenAI), debes configurar las siguientes variables de entorno en un directorio `.env` file in the `python`:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Completa estos valores con los detalles de tu recurso Azure OpenAI antes de ejecutar la aplicación.

> **Tip:** Puedes desplegar fácilmente tus propios modelos usando [Azure AI Foundry](https://ai.azure.com/).

### Escenario 3: Documentación en el Editor con el Servidor MCP en VS Code

En lugar de cambiar de pestaña en el navegador para buscar documentación, puedes integrar Microsoft Learn Docs directamente en VS Code usando el servidor MCP. Esto te permite:
- Buscar y leer documentación dentro de VS Code sin salir de tu entorno de codificación.
- Referenciar documentación e insertar enlaces directamente en tus archivos README o de curso.
- Usar GitHub Copilot y MCP juntos para un flujo de trabajo de documentación potenciado por IA, sin interrupciones.

**Casos de Uso Ejemplares:**
- Añadir rápidamente enlaces de referencia a un README mientras escribes la documentación de un curso o proyecto.
- Usar Copilot para generar código y MCP para encontrar y citar documentación relevante al instante.
- Mantenerte concentrado en tu editor y aumentar la productividad.

> [!IMPORTANT]
> Asegúrate de contar con un archivo válido [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

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

Estos ejemplos muestran la flexibilidad de la aplicación para diferentes objetivos de aprendizaje y períodos de tiempo.

## Referencias

- [Documentación de Chainlit](https://docs.chainlit.io/)
- [Documentación MCP](https://github.com/MicrosoftDocs/mcp)

**Aviso Legal**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por la precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o inexactitudes. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda la traducción profesional humana. No nos hacemos responsables de ningún malentendido o interpretación errónea derivada del uso de esta traducción.