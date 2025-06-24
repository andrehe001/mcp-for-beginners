<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:26:06+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "fr"
}
-->
# Générateur de plan d’étude avec Chainlit & Microsoft Learn Docs MCP

## Prérequis

- Python 3.8 ou version supérieure  
- pip (gestionnaire de paquets Python)  
- Accès Internet pour se connecter au serveur Microsoft Learn Docs MCP  

## Installation

1. Clonez ce dépôt ou téléchargez les fichiers du projet.  
2. Installez les dépendances requises :  

   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

### Scénario 1 : Requête simple vers Docs MCP  
Un client en ligne de commande qui se connecte au serveur Docs MCP, envoie une requête et affiche le résultat.

1. Lancez le script :  
   ```bash
   python scenario1.py
   ```  
2. Saisissez votre question de documentation à l’invite.

### Scénario 2 : Générateur de plan d’étude (application web Chainlit)  
Une interface web (utilisant Chainlit) qui permet aux utilisateurs de créer un plan d’étude personnalisé, semaine par semaine, pour n’importe quel sujet technique.

1. Démarrez l’application Chainlit :  
   ```bash
   chainlit run scenario2.py
   ```  
2. Ouvrez l’URL locale affichée dans votre terminal (par exemple http://localhost:8000) dans votre navigateur.  
3. Dans la fenêtre de chat, saisissez votre sujet d’étude ainsi que le nombre de semaines souhaité (ex. : « AI-900 certification, 8 semaines »).  
4. L’application vous répondra avec un plan d’étude détaillé semaine par semaine, incluant des liens vers la documentation Microsoft Learn correspondante.

**Variables d’environnement requises :**

Pour utiliser le Scénario 2 (l’application web Chainlit avec Azure OpenAI), vous devez définir les variables d’environnement suivantes dans un fichier `.env` file in the `python` :

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Remplissez ces valeurs avec les informations de votre ressource Azure OpenAI avant de lancer l’application.

> **Astuce :** Vous pouvez facilement déployer vos propres modèles avec [Azure AI Foundry](https://ai.azure.com/).

### Scénario 3 : Documentation intégrée dans l’éditeur avec le serveur MCP dans VS Code

Au lieu de changer d’onglet dans le navigateur pour chercher la documentation, vous pouvez intégrer Microsoft Learn Docs directement dans VS Code grâce au serveur MCP. Cela vous permet de :  
- Rechercher et lire la documentation sans quitter votre environnement de développement.  
- Référencer la documentation et insérer des liens directement dans vos fichiers README ou cours.  
- Utiliser GitHub Copilot et MCP ensemble pour un flux de travail documentaire fluide et assisté par IA.

**Exemples d’utilisation :**  
- Ajouter rapidement des liens de référence dans un README lors de la rédaction d’un cours ou d’un projet.  
- Utiliser Copilot pour générer du code et MCP pour trouver et citer instantanément la documentation pertinente.  
- Rester concentré dans l’éditeur et gagner en productivité.

> [!IMPORTANT]  
> Assurez-vous de disposer d’un fichier valide [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

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

Ces exemples montrent la flexibilité de l’application selon différents objectifs et durées d’apprentissage.

## Références

- [Documentation Chainlit](https://docs.chainlit.io/)  
- [Documentation MCP](https://github.com/MicrosoftDocs/mcp)

**Avertissement** :  
Ce document a été traduit à l'aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.