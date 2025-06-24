<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5384bbb2a92d00d5d7e66274dbe0331d",
  "translation_date": "2025-06-20T18:47:06+00:00",
  "source_file": "04-PracticalImplementation/README.md",
  "language_code": "hr"
}
-->
# Praktična implementacija

Praktična implementacija je mjesto gdje snaga Model Context Protocola (MCP) postaje opipljiva. Iako je važno razumjeti teoriju i arhitekturu MCP-a, prava vrijednost dolazi kada primijenite te koncepte za izgradnju, testiranje i implementaciju rješenja koja rješavaju stvarne probleme. Ovo poglavlje premošćuje jaz između konceptualnog znanja i praktičnog razvoja, vodeći vas kroz proces stvaranja aplikacija temeljenih na MCP-u.

Bilo da razvijate inteligentne asistente, integrirate AI u poslovne tokove rada ili gradite prilagođene alate za obradu podataka, MCP pruža fleksibilnu osnovu. Njegov dizajn neovisan o jeziku i službeni SDK-ovi za popularne programske jezike čine ga dostupnim širokom spektru programera. Korištenjem ovih SDK-ova možete brzo napraviti prototip, iterirati i skalirati svoja rješenja na različitim platformama i okruženjima.

U sljedećim odjeljcima pronaći ćete praktične primjere, uzorke koda i strategije implementacije koje pokazuju kako primijeniti MCP u C#, Javi, TypeScriptu, JavaScriptu i Pythonu. Također ćete naučiti kako otklanjati pogreške i testirati MCP servere, upravljati API-jima i implementirati rješenja u oblaku koristeći Azure. Ovi praktični resursi osmišljeni su da ubrzaju vaše učenje i pomognu vam samopouzdano izgraditi robusne, spremne za produkciju MCP aplikacije.

## Pregled

Ova lekcija fokusira se na praktične aspekte implementacije MCP-a u više programskih jezika. Istražit ćemo kako koristiti MCP SDK-ove u C#, Javi, TypeScriptu, JavaScriptu i Pythonu za izgradnju robusnih aplikacija, otklanjanje pogrešaka i testiranje MCP servera te kreiranje višekratno upotrebljivih resursa, promptova i alata.

## Ciljevi učenja

Do kraja ove lekcije moći ćete:
- Implementirati MCP rješenja koristeći službene SDK-ove u različitim programskim jezicima
- Sustavno otklanjati pogreške i testirati MCP servere
- Kreirati i koristiti značajke servera (Resurse, Prompte i Alate)
- Dizajnirati učinkovite MCP tokove rada za složene zadatke
- Optimizirati MCP implementacije za performanse i pouzdanost

## Službeni SDK resursi

Model Context Protocol nudi službene SDK-ove za više jezika:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

## Rad s MCP SDK-ovima

Ovaj odjeljak pruža praktične primjere implementacije MCP-a u različitim programskim jezicima. Uzorke koda možete pronaći u direktoriju `samples` organiziranom po jezicima.

### Dostupni uzorci

Repozitorij uključuje [primjere implementacija](../../../04-PracticalImplementation/samples) na sljedećim jezicima:

- [C#](./samples/csharp/README.md)
- [Java](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Svaki primjer prikazuje ključne MCP koncepte i obrasce implementacije za određeni jezik i ekosustav.

## Osnovne značajke servera

MCP serveri mogu implementirati bilo koju kombinaciju ovih značajki:

### Resursi
Resursi pružaju kontekst i podatke koje korisnik ili AI model mogu koristiti:
- Repozitoriji dokumenata
- Baze znanja
- Strukturirani izvori podataka
- Datotečni sustavi

### Prompti
Prompti su predlošci poruka i tokova rada za korisnike:
- Unaprijed definirani predlošci razgovora
- Vođeni obrasci interakcije
- Specijalizirane strukture dijaloga

### Alati
Alati su funkcije koje AI model može izvršavati:
- Alati za obradu podataka
- Integracije s vanjskim API-jima
- Računalne mogućnosti
- Funkcionalnost pretraživanja

## Primjeri implementacije: C#

Službeni C# SDK repozitorij sadrži nekoliko primjera implementacija koji demonstriraju različite aspekte MCP-a:

- **Osnovni MCP klijent**: Jednostavan primjer kako kreirati MCP klijenta i pozivati alate
- **Osnovni MCP server**: Minimalna implementacija servera s osnovnom registracijom alata
- **Napredni MCP server**: Potpuno opremljen server s registracijom alata, autentikacijom i rukovanjem pogreškama
- **Integracija s ASP.NET-om**: Primjeri integracije s ASP.NET Core
- **Obrasci implementacije alata**: Razni obrasci za implementaciju alata različitih razina složenosti

MCP C# SDK je u preview fazi i API-ji se mogu mijenjati. Ovaj blog ćemo kontinuirano ažurirati kako SDK bude evoluirao.

### Ključne značajke
- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)

- Izgradnja vašeg [prvog MCP servera](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

Za potpune primjere implementacije u C#, posjetite [službeni repozitorij C# SDK primjera](https://github.com/modelcontextprotocol/csharp-sdk)

## Primjer implementacije: Java implementacija

Java SDK nudi robusne opcije implementacije MCP-a s enterprise razinom značajki.

### Ključne značajke

- Integracija sa Spring Frameworkom
- Snažna tipna sigurnost
- Podrška za reaktivno programiranje
- Sveobuhvatno rukovanje pogreškama

Za potpuni primjer implementacije u Javi pogledajte [Java primjer](samples/java/containerapp/README.md) u direktoriju primjera.

## Primjer implementacije: JavaScript implementacija

JavaScript SDK pruža lagan i fleksibilan pristup implementaciji MCP-a.

### Ključne značajke

- Podrška za Node.js i preglednike
- API zasnovan na Promise objektima
- Jednostavna integracija s Expressom i drugim frameworkovima
- Podrška za WebSocket za streaming

Za potpuni primjer implementacije u JavaScriptu pogledajte [JavaScript primjer](samples/javascript/README.md) u direktoriju primjera.

## Primjer implementacije: Python implementacija

Python SDK nudi pitonski pristup implementaciji MCP-a s izvrsnom integracijom ML frameworka.

### Ključne značajke

- Podrška za async/await s asyncio
- Integracija s Flaskom i FastAPI-jem
- Jednostavna registracija alata
- Izvorna integracija s popularnim ML bibliotekama

Za potpuni primjer implementacije u Pythonu pogledajte [Python primjer](samples/python/README.md) u direktoriju primjera.

## Upravljanje API-jima

Azure API Management je izvrsno rješenje za osiguranje MCP servera. Ideja je postaviti Azure API Management instancu ispred vašeg MCP servera i dopustiti joj da upravlja značajkama koje će vam vjerojatno trebati, poput:

- ograničavanja brzine (rate limiting)
- upravljanja tokenima
- nadzora
- balansiranja opterećenja
- sigurnosti

### Azure primjer

Evo Azure primjera koji radi upravo to, tj. [kreira MCP server i osigurava ga Azure API Managementom](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Pogledajte kako autorizacijski tok izgleda na donjoj slici:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

Na slici se događa sljedeće:

- Autentikacija/Autorizacija odvija se pomoću Microsoft Entra.
- Azure API Management djeluje kao gateway i koristi politike za usmjeravanje i upravljanje prometom.
- Azure Monitor bilježi sve zahtjeve za daljnju analizu.

#### Autorizacijski tok

Pogledajmo autorizacijski tok detaljnije:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP specifikacija autorizacije

Saznajte više o [MCP Authorization specifikaciji](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization#2-10-third-party-authorization-flow)

## Implementacija udaljenog MCP servera na Azure

Pogledajmo možemo li implementirati ranije spomenuti primjer:

1. Klonirajte repozitorij

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

2. Registrirajte `Microsoft.App` pomoću naredbe

    ` resource provider.
    * If you are using Azure CLI, run `az provider register --namespace Microsoft.App --wait`.
    * If you are using Azure PowerShell, run `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Then run `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState

    nakon nekog vremena provjerite je li registracija završena.

3. Pokrenite ovu [azd](https://aka.ms/azd) naredbu za postavljanje API Management servisa, funkcijske aplikacije (s kodom) i svih ostalih potrebnih Azure resursa

    ```shell
    azd up
    ```

    Ova naredba trebala bi implementirati sve cloud resurse na Azureu

### Testiranje vašeg servera s MCP Inspectorom

1. U **novom terminal prozoru**, instalirajte i pokrenite MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Trebali biste vidjeti sučelje slično:

    ![Connect to Node inspector](../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.hr.png)

2. CTRL klikom učitajte MCP Inspector web aplikaciju s URL-a koji aplikacija prikazuje (npr. http://127.0.0.1:6274/#resources)
3. Postavite transportni tip na `SSE`
1. Set the URL to your running API Management SSE endpoint displayed after `azd up` i **Povežite se**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

5. **Popis alata**. Kliknite na alat i **Pokreni alat**.

Ako su svi koraci uspjeli, sada ste povezani s MCP serverom i uspjeli ste pozvati alat.

## MCP serveri za Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Ovaj set repozitorija je predložak za brzo pokretanje za izgradnju i implementaciju prilagođenih udaljenih MCP (Model Context Protocol) servera koristeći Azure Functions s Python, C# .NET ili Node/TypeScript.

Primjeri pružaju kompletno rješenje koje omogućava programerima da:

- Izgrade i pokrenu lokalno: razvijaju i otklanjaju pogreške MCP servera na lokalnom računalu
- Implementiraju na Azure: lako implementiraju u oblak jednostavnom naredbom azd up
- Povežu se s klijentima: povežu se s MCP serverom iz raznih klijenata uključujući VS Code-ov Copilot agent mode i MCP Inspector alat

### Ključne značajke:

- Sigurnost po dizajnu: MCP server je osiguran pomoću ključeva i HTTPS-a
- Opcije autentikacije: podržava OAuth koristeći ugrađenu autentikaciju i/ili API Management
- Izolacija mreže: omogućuje mrežnu izolaciju koristeći Azure Virtual Networks (VNET)
- Serverless arhitektura: koristi Azure Functions za skalabilno, događajima vođeno izvršavanje
- Lokalni razvoj: sveobuhvatna podrška za lokalni razvoj i otklanjanje pogrešaka
- Jednostavna implementacija: pojednostavljeni proces implementacije na Azure

Repozitorij uključuje sve potrebne konfiguracijske datoteke, izvorni kod i definicije infrastrukture za brzo pokretanje MCP servera spremnog za produkciju.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Primjer implementacije MCP-a koristeći Azure Functions s Python-om

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Primjer implementacije MCP-a koristeći Azure Functions s C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Primjer implementacije MCP-a koristeći Azure Functions s Node/TypeScript.

## Ključne spoznaje

- MCP SDK-ovi pružaju jezično specifične alate za implementaciju robusnih MCP rješenja
- Proces otklanjanja pogrešaka i testiranja je ključan za pouzdane MCP aplikacije
- Višekratno upotrebljivi predlošci promptova omogućuju dosljedne AI interakcije
- Dobro dizajnirani tokovi rada mogu orkestrirati složene zadatke koristeći više alata
- Implementacija MCP rješenja zahtijeva razmatranje sigurnosti, performansi i rukovanja pogreškama

## Vježba

Dizajnirajte praktični MCP tok rada koji rješava stvarni problem u vašem području:

1. Identificirajte 3-4 alata koji bi bili korisni za rješavanje tog problema
2. Kreirajte dijagram toka rada koji prikazuje kako ti alati međusobno djeluju
3. Implementirajte osnovnu verziju jednog od alata koristeći svoj omiljeni jezik
4. Kreirajte predložak prompta koji će pomoći modelu da učinkovito koristi vaš alat

## Dodatni resursi


---

Sljedeće: [Napredne teme](../05-AdvancedTopics/README.md)

**Odricanje od odgovornosti**:  
Ovaj dokument preveden je pomoću AI usluge za prevođenje [Co-op Translator](https://github.com/Azure/co-op-translator). Iako nastojimo postići točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati službenim i autoritativnim izvorom. Za važne informacije preporučuje se profesionalni ljudski prijevod. Ne odgovaramo za bilo kakve nesporazume ili pogrešne interpretacije koje proizlaze iz korištenja ovog prijevoda.