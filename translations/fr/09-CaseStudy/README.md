<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6940b1e931e51821b219aa9dcfe8c4ee",
  "translation_date": "2025-06-23T10:56:46+00:00",
  "source_file": "09-CaseStudy/README.md",
  "language_code": "fr"
}
-->
# MCP en action : études de cas concrètes

Le Model Context Protocol (MCP) transforme la manière dont les applications d’IA interagissent avec les données, les outils et les services. Cette section présente des études de cas réelles qui illustrent les applications pratiques du MCP dans divers contextes d’entreprise.

## Aperçu

Cette section met en avant des exemples concrets d’implémentations MCP, soulignant comment les organisations utilisent ce protocole pour résoudre des problématiques métier complexes. En explorant ces études de cas, vous découvrirez la polyvalence, la scalabilité et les bénéfices concrets du MCP dans des situations réelles.

## Objectifs d’apprentissage clés

En parcourant ces études de cas, vous allez :

- Comprendre comment appliquer MCP pour résoudre des problèmes métier spécifiques
- Découvrir différents modèles d’intégration et approches architecturales
- Identifier les bonnes pratiques pour implémenter MCP en environnement entreprise
- Appréhender les défis rencontrés et les solutions mises en œuvre dans des cas réels
- Repérer des opportunités pour appliquer des schémas similaires dans vos propres projets

## Études de cas présentées

### 1. [Azure AI Travel Agents – Implémentation de référence](./travelagentsample.md)

Cette étude de cas analyse la solution de référence complète de Microsoft qui montre comment construire une application de planification de voyages multi-agents et alimentée par l’IA, en utilisant MCP, Azure OpenAI et Azure AI Search. Le projet met en avant :

- L’orchestration multi-agents via MCP
- L’intégration des données d’entreprise avec Azure AI Search
- Une architecture sécurisée et scalable basée sur les services Azure
- Des outils extensibles grâce à des composants MCP réutilisables
- Une expérience utilisateur conversationnelle propulsée par Azure OpenAI

Les détails d’architecture et d’implémentation offrent un aperçu précieux pour concevoir des systèmes multi-agents complexes avec MCP comme couche de coordination.

### 2. [Mise à jour des éléments Azure DevOps à partir des données YouTube](./UpdateADOItemsFromYT.md)

Cette étude de cas illustre une application pratique du MCP pour automatiser des processus de travail. Elle montre comment utiliser les outils MCP pour :

- Extraire des données depuis des plateformes en ligne (YouTube)
- Mettre à jour des éléments de travail dans Azure DevOps
- Créer des workflows d’automatisation reproductibles
- Intégrer des données issues de systèmes disparates

Cet exemple démontre comment des implémentations MCP relativement simples peuvent générer d’importants gains d’efficacité en automatisant les tâches répétitives et en améliorant la cohérence des données entre systèmes.

### 3. [Récupération documentaire en temps réel avec MCP](./docs-mcp/README.md)

Cette étude de cas vous guide pour connecter un client console Python à un serveur Model Context Protocol (MCP) afin de récupérer et enregistrer en temps réel une documentation Microsoft contextuelle. Vous apprendrez à :

- Vous connecter à un serveur MCP via un client Python utilisant le SDK officiel MCP
- Utiliser des clients HTTP en streaming pour une récupération efficace et en temps réel des données
- Appeler les outils de documentation sur le serveur et consigner les réponses directement dans la console
- Intégrer la documentation Microsoft à jour dans votre flux de travail sans quitter le terminal

Le chapitre comprend un exercice pratique, un exemple de code minimal fonctionnel, ainsi que des liens vers des ressources complémentaires pour approfondir. Consultez le guide complet et le code associé pour comprendre comment MCP peut révolutionner l’accès à la documentation et la productivité des développeurs en environnement console.

### 4. [Application web génératrice de plans d’étude interactifs avec MCP](./docs-mcp/README.md)

Cette étude de cas montre comment créer une application web interactive utilisant Chainlit et le Model Context Protocol (MCP) pour générer des plans d’étude personnalisés sur n’importe quel sujet. Les utilisateurs peuvent spécifier un thème (comme « certification AI-900 ») et une durée d’étude (par exemple 8 semaines), et l’application fournit une répartition semaine par semaine des contenus recommandés. Chainlit offre une interface de chat conversationnelle, rendant l’expérience engageante et adaptable.

- Application web conversationnelle propulsée par Chainlit
- Saisie utilisateur pour le sujet et la durée
- Recommandations de contenu semaine par semaine via MCP
- Réponses adaptatives et en temps réel dans une interface de chat

Le projet illustre comment combiner IA conversationnelle et MCP pour créer des outils éducatifs dynamiques et centrés utilisateur dans un environnement web moderne.

### 5. [Documentation intégrée dans l’éditeur avec MCP Server dans VS Code](./docs-mcp/README.md)

Cette étude de cas montre comment intégrer directement Microsoft Learn Docs dans votre environnement VS Code grâce au serveur MCP—plus besoin de changer d’onglet de navigateur ! Vous découvrirez comment :

- Rechercher et lire instantanément la documentation dans VS Code via le panneau MCP ou la palette de commandes
- Référencer la documentation et insérer des liens directement dans vos fichiers README ou markdown de cours
- Utiliser GitHub Copilot et MCP conjointement pour des workflows documentaires et de code fluides et assistés par IA
- Valider et enrichir votre documentation avec un retour en temps réel et une précision garantie par Microsoft
- Intégrer MCP aux workflows GitHub pour une validation continue de la documentation

L’implémentation comprend :
- Une configuration `.vscode/mcp.json` pour une installation simplifiée
- Des captures d’écran illustrant l’expérience intégrée dans l’éditeur
- Des conseils pour combiner Copilot et MCP afin d’optimiser la productivité

Ce scénario est idéal pour les auteurs de cours, rédacteurs techniques et développeurs souhaitant rester concentrés dans leur éditeur tout en travaillant avec la documentation, Copilot et les outils de validation—le tout propulsé par MCP.

### 6. [Création d’un serveur APIM MCP](./apimsample.md)

Cette étude de cas propose un guide étape par étape pour créer un serveur MCP avec Azure API Management (APIM). Elle couvre :

- La mise en place d’un serveur MCP dans Azure API Management
- L’exposition des opérations API en tant qu’outils MCP
- La configuration des politiques de limitation de débit et de sécurité
- Les tests du serveur MCP via Visual Studio Code et GitHub Copilot

Cet exemple illustre comment exploiter les capacités d’Azure pour créer un serveur MCP robuste, utilisable dans diverses applications, renforçant l’intégration des systèmes d’IA avec les API d’entreprise.

## Conclusion

Ces études de cas soulignent la polyvalence et les applications concrètes du Model Context Protocol dans des contextes réels. Des systèmes multi-agents complexes aux workflows d’automatisation ciblés, MCP offre une méthode standardisée pour connecter les systèmes d’IA aux outils et données nécessaires à la création de valeur.

En étudiant ces implémentations, vous pourrez tirer des enseignements sur les modèles architecturaux, les stratégies d’implémentation et les bonnes pratiques applicables à vos propres projets MCP. Ces exemples démontrent que MCP n’est pas qu’un cadre théorique, mais une solution pragmatique face à des enjeux métier concrets.

## Ressources supplémentaires

- [Azure AI Travel Agents GitHub Repository](https://github.com/Azure-Samples/azure-ai-travel-agents)
- [Azure DevOps MCP Tool](https://github.com/microsoft/azure-devops-mcp)
- [Playwright MCP Tool](https://github.com/microsoft/playwright-mcp)
- [Microsoft Docs MCP Server](https://github.com/MicrosoftDocs/mcp)
- [MCP Community Examples](https://github.com/microsoft/mcp)

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforçons d’assurer l’exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.