<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:32:42+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "ro"
}
-->
# Generator de Plan de Studiu cu Chainlit & Microsoft Learn Docs MCP

## Cerințe preliminare

- Python 3.8 sau versiune superioară
- pip (managerul de pachete Python)
- Acces la internet pentru conectarea la serverul Microsoft Learn Docs MCP

## Instalare

1. Clonează acest depozit sau descarcă fișierele proiectului.
2. Instalează dependențele necesare:

   ```bash
   pip install -r requirements.txt
   ```

## Utilizare

### Scenariul 1: Interogare simplă către Docs MCP  
Un client în linie de comandă care se conectează la serverul Docs MCP, trimite o interogare și afișează rezultatul.

1. Rulează scriptul:  
   ```bash
   python scenario1.py
   ```  
2. Introdu întrebarea ta legată de documentație la prompt.

### Scenariul 2: Generator de plan de studiu (aplicație web Chainlit)  
O interfață web (folosind Chainlit) care permite utilizatorilor să genereze un plan de studiu personalizat, săptămână cu săptămână, pentru orice subiect tehnic.

1. Pornește aplicația Chainlit:  
   ```bash
   chainlit run scenario2.py
   ```  
2. Deschide în browser URL-ul local afișat în terminal (ex: http://localhost:8000).  
3. În fereastra de chat, introdu subiectul de studiu și numărul de săptămâni pentru care vrei să studiezi (ex: „certificare AI-900, 8 săptămâni”).  
4. Aplicația va răspunde cu un plan de studiu săptămânal, inclusiv linkuri către documentația relevantă Microsoft Learn.

**Variabile de mediu necesare:**  

Pentru a folosi Scenariul 2 (aplicația web Chainlit cu Azure OpenAI), trebuie să setezi următoarele variabile de mediu într-un fișier `.env` file in the `python`:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Completează aceste valori cu detaliile resursei tale Azure OpenAI înainte de a rula aplicația.

> **Tip:** Poți să-ți implementezi cu ușurință propriile modele folosind [Azure AI Foundry](https://ai.azure.com/).

### Scenariul 3: Documentație în editor cu server MCP în VS Code

În loc să schimbi taburile din browser pentru a căuta documentație, poți aduce Microsoft Learn Docs direct în VS Code folosind serverul MCP. Astfel poți:  
- Căuta și citi documentația direct în VS Code, fără să părăsești mediul de lucru.  
- Referenția documentația și insera linkuri direct în fișiere README sau cursuri.  
- Folosi GitHub Copilot și MCP împreună pentru un flux de lucru AI integrat și eficient.

**Exemple de utilizare:**  
- Adaugă rapid linkuri de referință într-un README în timp ce scrii documentația unui curs sau proiect.  
- Folosește Copilot pentru generarea codului și MCP pentru a găsi și cita imediat documentația relevantă.  
- Rămâi concentrat în editor și crește-ți productivitatea.

> [!IMPORTANT]  
> Asigură-te că ai un fișier valid [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

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

Aceste exemple demonstrează flexibilitatea aplicației pentru diverse obiective de învățare și durate.

## Referințe

- [Documentația Chainlit](https://docs.chainlit.io/)  
- [Documentația MCP](https://github.com/MicrosoftDocs/mcp)

**Declinare de responsabilitate**:  
Acest document a fost tradus folosind serviciul de traducere AI [Co-op Translator](https://github.com/Azure/co-op-translator). Deși ne străduim pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autorizată. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.