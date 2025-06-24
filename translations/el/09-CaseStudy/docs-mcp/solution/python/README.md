<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:30:01+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "el"
}
-->
# Δημιουργός Σχεδίου Μελέτης με Chainlit & Microsoft Learn Docs MCP

## Προαπαιτούμενα

- Python 3.8 ή νεότερη έκδοση  
- pip (διαχειριστής πακέτων Python)  
- Πρόσβαση στο διαδίκτυο για σύνδεση με τον διακομιστή Microsoft Learn Docs MCP  

## Εγκατάσταση

1. Κλωνοποιήστε αυτό το αποθετήριο ή κατεβάστε τα αρχεία του έργου.  
2. Εγκαταστήστε τις απαραίτητες εξαρτήσεις:  

   ```bash
   pip install -r requirements.txt
   ```

## Χρήση

### Σενάριο 1: Απλή Ερώτηση προς Docs MCP  
Ένας πελάτης γραμμής εντολών που συνδέεται με τον διακομιστή Docs MCP, στέλνει μια ερώτηση και εμφανίζει το αποτέλεσμα.

1. Εκτελέστε το σενάριο:  
   ```bash
   python scenario1.py
   ```  
2. Πληκτρολογήστε την ερώτηση τεκμηρίωσης στο προτροπή.

### Σενάριο 2: Δημιουργός Σχεδίου Μελέτης (Chainlit Web App)  
Μια διαδικτυακή διεπαφή (με χρήση Chainlit) που επιτρέπει στους χρήστες να δημιουργήσουν ένα εξατομικευμένο, εβδομαδιαίο σχέδιο μελέτης για οποιοδήποτε τεχνικό θέμα.

1. Εκκινήστε την εφαρμογή Chainlit:  
   ```bash
   chainlit run scenario2.py
   ```  
2. Ανοίξτε το τοπικό URL που εμφανίζεται στο τερματικό σας (π.χ., http://localhost:8000) στον περιηγητή σας.  
3. Στο παράθυρο συνομιλίας, εισάγετε το θέμα μελέτης και τον αριθμό εβδομάδων που θέλετε να μελετήσετε (π.χ., "AI-900 certification, 8 weeks").  
4. Η εφαρμογή θα απαντήσει με ένα εβδομαδιαίο σχέδιο μελέτης, περιλαμβάνοντας συνδέσμους σε σχετική τεκμηρίωση Microsoft Learn.

**Απαιτούμενες Μεταβλητές Περιβάλλοντος:**

Για να χρησιμοποιήσετε το Σενάριο 2 (την εφαρμογή Chainlit με Azure OpenAI), πρέπει να ορίσετε τις ακόλουθες μεταβλητές περιβάλλοντος σε έναν φάκελο `.env` file in the `python`:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Συμπληρώστε αυτές τις τιμές με τα στοιχεία του πόρου Azure OpenAI πριν εκτελέσετε την εφαρμογή.

> **Tip:** Μπορείτε εύκολα να αναπτύξετε τα δικά σας μοντέλα χρησιμοποιώντας το [Azure AI Foundry](https://ai.azure.com/).

### Σενάριο 3: Τεκμηρίωση εντός Επεξεργαστή με MCP Server στο VS Code

Αντί να αλλάζετε καρτέλες στον περιηγητή για να αναζητήσετε τεκμηρίωση, μπορείτε να φέρετε το Microsoft Learn Docs απευθείας στο VS Code σας μέσω του MCP server. Αυτό σας επιτρέπει να:  
- Αναζητάτε και διαβάζετε τεκμηρίωση μέσα στο VS Code χωρίς να βγαίνετε από το περιβάλλον προγραμματισμού σας.  
- Αναφέρετε τεκμηρίωση και εισάγετε συνδέσμους απευθείας στα αρχεία README ή μαθήματός σας.  
- Χρησιμοποιείτε το GitHub Copilot και το MCP μαζί για μια ομαλή ροή εργασίας με τεχνητή νοημοσύνη στην τεκμηρίωση.

**Παραδείγματα Χρήσης:**  
- Προσθέστε γρήγορα συνδέσμους αναφοράς σε ένα README ενώ γράφετε τεκμηρίωση μαθήματος ή έργου.  
- Χρησιμοποιήστε το Copilot για να δημιουργήσετε κώδικα και το MCP για να βρείτε και να παραθέσετε άμεσα σχετική τεκμηρίωση.  
- Παραμείνετε συγκεντρωμένοι στον επεξεργαστή σας και αυξήστε την παραγωγικότητα.

> [!IMPORTANT]  
> Βεβαιωθείτε ότι έχετε ένα έγκυρο [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

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

Αυτά τα παραδείγματα δείχνουν την ευελιξία της εφαρμογής για διαφορετικούς στόχους μάθησης και χρονικά πλαίσια.

## Αναφορές

- [Chainlit Documentation](https://docs.chainlit.io/)  
- [MCP Documentation](https://github.com/MicrosoftDocs/mcp)

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που προσπαθούμε για ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν σφάλματα ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες συνιστάται η επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.