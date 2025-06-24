<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "36de9fae488d6de554d969fe8e0801a8",
  "translation_date": "2025-06-20T19:20:03+00:00",
  "source_file": "09-CaseStudy/apimsample.md",
  "language_code": "el"
}
-->
# Μελέτη Περίπτωσης: Έκθεση REST API στο API Management ως MCP server

Το Azure API Management είναι μια υπηρεσία που παρέχει μια Πύλη πάνω από τα API Endpoints σας. Ο τρόπος λειτουργίας είναι ότι το Azure API Management λειτουργεί ως μεσολαβητής (proxy) μπροστά από τα APIs σας και μπορεί να αποφασίσει τι θα κάνει με τα εισερχόμενα αιτήματα.

Χρησιμοποιώντας το, προσθέτετε μια σειρά από δυνατότητες όπως:

- **Ασφάλεια**, μπορείτε να χρησιμοποιήσετε από API keys, JWT έως managed identity.
- **Περιορισμός ρυθμού κλήσεων (Rate limiting)**, μια εξαιρετική δυνατότητα που σας επιτρέπει να ορίσετε πόσες κλήσεις επιτρέπονται ανά μονάδα χρόνου. Αυτό βοηθά να διασφαλιστεί ότι όλοι οι χρήστες έχουν μια καλή εμπειρία και ότι η υπηρεσία σας δεν κατακλύζεται από αιτήματα.
- **Κλιμάκωση & Ισορροπία φορτίου (Load balancing)**. Μπορείτε να ρυθμίσετε πολλαπλά endpoints για να κατανείμετε το φορτίο και να αποφασίσετε πώς θα γίνει αυτή η κατανομή.
- **Δυνατότητες AI όπως semantic caching**, όριο tokens και παρακολούθηση tokens και άλλα. Αυτές είναι εξαιρετικές λειτουργίες που βελτιώνουν την απόκριση και βοηθούν να έχετε έλεγχο στην κατανάλωση των tokens σας. [Διαβάστε περισσότερα εδώ](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Γιατί MCP + Azure API Management;

Το Model Context Protocol γίνεται γρήγορα ένα πρότυπο για agentic AI εφαρμογές και για το πώς να εκθέτεις εργαλεία και δεδομένα με συνεπή τρόπο. Το Azure API Management είναι η φυσική επιλογή όταν χρειάζεστε να «διαχειριστείτε» APIs. Οι MCP Servers συχνά ενσωματώνονται με άλλα APIs για να επιλύουν αιτήματα προς ένα εργαλείο, για παράδειγμα. Επομένως, ο συνδυασμός Azure API Management και MCP έχει πολύ νόημα.

## Επισκόπηση

Σε αυτή τη συγκεκριμένη περίπτωση χρήσης θα μάθουμε πώς να εκθέτουμε API endpoints ως MCP Server. Με αυτόν τον τρόπο, μπορούμε εύκολα να ενσωματώσουμε αυτά τα endpoints σε μια agentic εφαρμογή ενώ παράλληλα αξιοποιούμε τις δυνατότητες του Azure API Management.

## Κύρια Χαρακτηριστικά

- Επιλέγετε τις μεθόδους του endpoint που θέλετε να εκθέσετε ως εργαλεία.
- Οι επιπλέον δυνατότητες που λαμβάνετε εξαρτώνται από το τι ρυθμίζετε στην ενότητα πολιτικών (policy) για το API σας. Εδώ θα δείξουμε πώς μπορείτε να προσθέσετε περιορισμό ρυθμού κλήσεων.

## Προαπαιτούμενο βήμα: εισαγωγή ενός API

Αν έχετε ήδη ένα API στο Azure API Management, πολύ καλά, τότε μπορείτε να παραλείψετε αυτό το βήμα. Αν όχι, δείτε αυτόν τον σύνδεσμο, [εισαγωγή API στο Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Έκθεση API ως MCP Server

Για να εκθέσουμε τα API endpoints, ακολουθούμε τα παρακάτω βήματα:

1. Μεταβείτε στο Azure Portal στη διεύθυνση <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
   Μεταβείτε στην περίπτωση API Management σας.

1. Στο αριστερό μενού, επιλέξτε APIs > MCP Servers > + Δημιουργία νέου MCP Server.

1. Στο API, επιλέξτε ένα REST API για έκθεση ως MCP server.

1. Επιλέξτε μία ή περισσότερες API Operations για έκθεση ως εργαλεία. Μπορείτε να επιλέξετε όλες τις λειτουργίες ή μόνο συγκεκριμένες.

    ![Επιλογή μεθόδων προς έκθεση](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Επιλέξτε **Create**.

1. Μεταβείτε στην επιλογή μενού **APIs** και **MCP Servers**, θα δείτε το εξής:

    ![Δείτε τον MCP Server στο κύριο παράθυρο](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    Ο MCP server έχει δημιουργηθεί και οι API operations εκτίθενται ως εργαλεία. Ο MCP server εμφανίζεται στον πίνακα MCP Servers. Η στήλη URL δείχνει το endpoint του MCP server που μπορείτε να καλέσετε για δοκιμές ή μέσα σε εφαρμογή πελάτη.

## Προαιρετικό: Διαμόρφωση πολιτικών

Το Azure API Management έχει την βασική έννοια των πολιτικών (policies) όπου ορίζετε διαφορετικούς κανόνες για τα endpoints σας, όπως για παράδειγμα περιορισμό ρυθμού ή semantic caching. Αυτές οι πολιτικές γράφονται σε XML.

Ακολουθεί πώς να ορίσετε μια πολιτική για περιορισμό ρυθμού κλήσεων στο MCP Server σας:

1. Στο portal, κάτω από APIs, επιλέξτε **MCP Servers**.

1. Επιλέξτε τον MCP server που δημιουργήσατε.

1. Στο αριστερό μενού, κάτω από MCP, επιλέξτε **Policies**.

1. Στον επεξεργαστή πολιτικών, προσθέστε ή επεξεργαστείτε τις πολιτικές που θέλετε να εφαρμόσετε στα εργαλεία του MCP server. Οι πολιτικές ορίζονται σε XML. Για παράδειγμα, μπορείτε να προσθέσετε μια πολιτική για να περιορίσετε τις κλήσεις στα εργαλεία του MCP server (σε αυτό το παράδειγμα, 5 κλήσεις ανά 30 δευτερόλεπτα ανά IP πελάτη). Ακολουθεί το XML που θα προκαλέσει τον περιορισμό:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Εικόνα του επεξεργαστή πολιτικών:

    ![Επεξεργαστής πολιτικών](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)

## Δοκιμάστε το

Ας βεβαιωθούμε ότι ο MCP Server λειτουργεί όπως αναμένεται.

Για αυτό, θα χρησιμοποιήσουμε το Visual Studio Code και το GitHub Copilot στη λειτουργία Agent. Θα προσθέσουμε τον MCP server σε ένα αρχείο *mcp.json*. Με αυτόν τον τρόπο, το Visual Studio Code θα λειτουργεί ως πελάτης με agentic δυνατότητες και οι τελικοί χρήστες θα μπορούν να πληκτρολογούν ένα prompt και να αλληλεπιδρούν με τον server.

Ας δούμε πώς να προσθέσουμε τον MCP server στο Visual Studio Code:

1. Χρησιμοποιήστε την εντολή MCP: **Add Server από το Command Palette**.

1. Όταν σας ζητηθεί, επιλέξτε τον τύπο server: **HTTP (HTTP ή Server Sent Events)**.

1. Εισάγετε το URL του MCP server στο API Management. Παράδειγμα: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (για το SSE endpoint) ή **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (για το MCP endpoint), σημειώστε τη διαφορά ανάμεσα στα transports `/sse` or `/mcp`.

1. Εισάγετε ένα αναγνωριστικό server (server ID) της επιλογής σας. Δεν είναι κρίσιμη τιμή αλλά θα σας βοηθήσει να θυμάστε ποια είναι αυτή η περίπτωση server.

1. Επιλέξτε αν θέλετε να αποθηκεύσετε τη διαμόρφωση στα workspace settings ή στα user settings.

  - **Workspace settings** - Η διαμόρφωση του server αποθηκεύεται σε αρχείο .vscode/mcp.json και είναι διαθέσιμη μόνο στο τρέχον workspace.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    ή αν επιλέξετε streaming HTTP ως transport, θα είναι λίγο διαφορετικό:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **User settings** - Η διαμόρφωση του server προστίθεται στο παγκόσμιο αρχείο *settings.json* και είναι διαθέσιμη σε όλα τα workspaces. Η διαμόρφωση μοιάζει με την παρακάτω:

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Πρέπει επίσης να προσθέσετε διαμόρφωση, μια κεφαλίδα (header) για να βεβαιωθείτε ότι γίνεται σωστή αυθεντικοποίηση προς το Azure API Management. Χρησιμοποιεί μια κεφαλίδα με όνομα **Ocp-Apim-Subscription-Key**.

    - Δείτε πώς μπορείτε να την προσθέσετε στα settings:

    ![Προσθήκη κεφαλίδας για αυθεντικοποίηση](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), αυτό θα εμφανίσει ένα prompt για να εισάγετε την τιμή του API key που μπορείτε να βρείτε στο Azure Portal για την περίπτωση Azure API Management σας.

   - Για να την προσθέσετε στο *mcp.json* αντί αυτού, μπορείτε να την προσθέσετε ως εξής:

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

### Χρήση λειτουργίας Agent

Τώρα που έχουμε ρυθμίσει είτε στα settings είτε στο *.vscode/mcp.json*, ας το δοκιμάσουμε.

Θα πρέπει να υπάρχει ένα εικονίδιο Tools όπως το παρακάτω, όπου εμφανίζονται τα εκτεθειμένα εργαλεία από τον server σας:

![Εργαλεία από τον server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Κάντε κλικ στο εικονίδιο εργαλείων και θα δείτε μια λίστα εργαλείων όπως:

    ![Εργαλεία](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Πληκτρολογήστε ένα prompt στη συνομιλία για να καλέσετε το εργαλείο. Για παράδειγμα, αν επιλέξατε ένα εργαλείο για να λάβετε πληροφορίες για μια παραγγελία, μπορείτε να ρωτήσετε τον agent για μια παραγγελία. Ακολουθεί παράδειγμα prompt:

    ```text
    get information from order 2
    ```

    Τώρα θα εμφανιστεί ένα εικονίδιο εργαλείων που σας ζητά να συνεχίσετε με την κλήση του εργαλείου. Επιλέξτε να συνεχίσετε την εκτέλεση του εργαλείου, θα δείτε μια έξοδο όπως η παρακάτω:

    ![Αποτέλεσμα από το prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **Αυτό που βλέπετε παραπάνω εξαρτάται από τα εργαλεία που έχετε ρυθμίσει, αλλά η ιδέα είναι ότι λαμβάνετε μια κειμενική απάντηση όπως παραπάνω**

## Αναφορές

Δείτε πώς μπορείτε να μάθετε περισσότερα:

- [Οδηγός για Azure API Management και MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Παράδειγμα Python: Ασφαλείς απομακρυσμένοι MCP servers με χρήση Azure API Management (πειραματικό)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Εργαστήριο εξουσιοδότησης MCP client](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Χρήση της επέκτασης Azure API Management για VS Code για εισαγωγή και διαχείριση APIs](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Εγγραφή και ανεύρεση απομακρυσμένων MCP servers στο Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Εξαιρετικό αποθετήριο που παρουσιάζει πολλές δυνατότητες AI με Azure API Management
- [Εργαστήρια AI Gateway](https://azure-samples.github.io/AI-Gateway/) Περιέχει εργαστήρια με χρήση Azure Portal, ένας εξαιρετικός τρόπος για να ξεκινήσετε την αξιολόγηση δυνατοτήτων AI.

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας την υπηρεσία αυτόματης μετάφρασης AI [Co-op Translator](https://github.com/Azure/co-op-translator). Παρόλο που προσπαθούμε για ακρίβεια, παρακαλούμε να λάβετε υπόψη ότι οι αυτόματες μεταφράσεις μπορεί να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στην αρχική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.