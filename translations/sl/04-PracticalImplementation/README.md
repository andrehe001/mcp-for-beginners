<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5384bbb2a92d00d5d7e66274dbe0331d",
  "translation_date": "2025-06-20T18:47:30+00:00",
  "source_file": "04-PracticalImplementation/README.md",
  "language_code": "sl"
}
-->
# Praktična izvedba

Praktična izvedba je tisti del, kjer moč Model Context Protocol (MCP) postane otipljiva. Medtem ko je razumevanje teorije in arhitekture MCP pomembno, se prava vrednost pokaže, ko te koncepte uporabite za izdelavo, testiranje in uvajanje rešitev, ki rešujejo dejanske probleme. Ta poglavje premošča vrzel med konceptualnim znanjem in praktičnim razvojem ter vas vodi skozi proces oživljanja aplikacij na osnovi MCP.

Ne glede na to, ali razvijate inteligentne asistente, integrirate AI v poslovne procese ali ustvarjate prilagojena orodja za obdelavo podatkov, MCP ponuja prilagodljivo osnovo. Njegova jezikovno neodvisna zasnova in uradni SDK-ji za priljubljene programske jezike omogočajo dostop širokemu krogu razvijalcev. Z uporabo teh SDK-jev lahko hitro izdelate prototipe, iterirate in skalirate svoje rešitve na različnih platformah in okoljih.

V naslednjih razdelkih boste našli praktične primere, vzorčne kode in strategije uvajanja, ki prikazujejo, kako implementirati MCP v C#, Javi, TypeScriptu, JavaScriptu in Pythonu. Naučili se boste tudi, kako odpravljati napake in testirati MCP strežnike, upravljati API-je ter uvajati rešitve v oblak z uporabo Azure. Ti praktični viri so zasnovani tako, da pospešijo vaše učenje in vam pomagajo samozavestno graditi robustne, produkcijsko pripravljene MCP aplikacije.

## Pregled

Ta lekcija se osredotoča na praktične vidike implementacije MCP v več programskih jezikih. Raziskali bomo, kako uporabljati MCP SDK-je v C#, Javi, TypeScriptu, JavaScriptu in Pythonu za izdelavo robustnih aplikacij, odpravljanje napak in testiranje MCP strežnikov ter ustvarjanje ponovno uporabnih virov, pozivov in orodij.

## Cilji učenja

Na koncu te lekcije boste znali:
- Implementirati MCP rešitve z uporabo uradnih SDK-jev v različnih programskih jezikih
- Sistematično odpravljati napake in testirati MCP strežnike
- Ustvarjati in uporabljati strežniške funkcionalnosti (Viri, Pozivi in Orodja)
- Oblikovati učinkovite MCP delovne tokove za kompleksne naloge
- Optimizirati MCP implementacije za zmogljivost in zanesljivost

## Uradni SDK viri

Model Context Protocol ponuja uradne SDK-je za več jezikov:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) 
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

## Delo z MCP SDK-ji

Ta razdelek ponuja praktične primere implementacije MCP v več programskih jezikih. V mapi `samples` najdete vzorčne kode razporejene po jezikih.

### Na voljo vzorci

V repozitoriju so [vzorec implementacij](../../../04-PracticalImplementation/samples) v naslednjih jezikih:

- [C#](./samples/csharp/README.md)
- [Java](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Vsak vzorec prikazuje ključne koncepte MCP in vzorce implementacije za določen jezik in ekosistem.

## Osnovne funkcije strežnika

MCP strežniki lahko implementirajo katerokoli kombinacijo teh funkcij:

### Viri
Viri zagotavljajo kontekst in podatke za uporabnika ali AI model:
- Repzitoriji dokumentov
- Baze znanja
- Strukturirani podatkovni viri
- Datotečni sistemi

### Pozivi
Pozivi so predloge sporočil in delovnih tokov za uporabnike:
- Vnaprej določene predloge pogovorov
- Vodeni vzorci interakcij
- Specializirane strukture dialogov

### Orodja
Orodja so funkcije, ki jih AI model izvaja:
- Orodja za obdelavo podatkov
- Integracije zunanjih API-jev
- Računske zmogljivosti
- Iskalne funkcionalnosti

## Vzorčne implementacije: C#

Uradni repozitorij C# SDK vsebuje več vzorčnih implementacij, ki prikazujejo različne vidike MCP:

- **Osnovni MCP klient**: Preprost primer, kako ustvariti MCP klienta in klicati orodja
- **Osnovni MCP strežnik**: Minimalna implementacija strežnika z osnovno registracijo orodij
- **Napredni MCP strežnik**: Polno funkcionalen strežnik z registracijo orodij, avtentikacijo in obravnavo napak
- **Integracija z ASP.NET**: Primeri integracije z ASP.NET Core
- **Vzorec implementacije orodij**: Različni vzorci za implementacijo orodij z različno zahtevnostjo

MCP C# SDK je v predogledu in API-ji se lahko spreminjajo. Ta blog bomo sproti posodabljali, ko bo SDK napredoval.

### Ključne funkcije 
- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)

- Izdelava [prvega MCP strežnika](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

Za popolne vzorce implementacij v C# obiščite [uradni repozitorij vzorcev C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)

## Vzorčna implementacija: Java

Java SDK ponuja robustne možnosti implementacije MCP z enterprise-grade funkcijami.

### Ključne funkcije

- Integracija s Spring Framework
- Močna tipna varnost
- Podpora za reaktivno programiranje
- Celovita obravnava napak

Za popoln vzorec implementacije v Javi si oglejte [Java vzorec](samples/java/containerapp/README.md) v mapi vzorcev.

## Vzorčna implementacija: JavaScript

JavaScript SDK ponuja lahkoten in prilagodljiv pristop k implementaciji MCP.

### Ključne funkcije

- Podpora za Node.js in brskalnike
- API, ki temelji na Promise-jih
- Enostavna integracija z Express in drugimi okviri
- Podpora za WebSocket za pretakanje podatkov

Za popoln vzorec implementacije v JavaScriptu si oglejte [JavaScript vzorec](samples/javascript/README.md) v mapi vzorcev.

## Vzorčna implementacija: Python

Python SDK ponuja pythonističen pristop k implementaciji MCP z odlično integracijo ML ogrodij.

### Ključne funkcije

- Podpora za async/await z asyncio
- Integracija s Flask in FastAPI
- Enostavna registracija orodij
- Nativna integracija s priljubljenimi ML knjižnicami

Za popoln vzorec implementacije v Pythonu si oglejte [Python vzorec](samples/python/README.md) v mapi vzorcev.

## Upravljanje API-jev

Azure API Management je odlična rešitev za varovanje MCP strežnikov. Ideja je, da postavite Azure API Management instanco pred vaš MCP strežnik in ji dovolite upravljati funkcije, kot so:

- omejevanje hitrosti
- upravljanje žetonov
- nadzor
- uravnoteženje obremenitve
- varnost

### Azure vzorec

Tukaj je Azure vzorec, ki točno to počne, tj. [ustvarjanje MCP strežnika in njegovo varovanje z Azure API Management](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Spodnja slika prikazuje, kako poteka avtentikacijski potek:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true) 

Na zgornji sliki potekajo naslednji procesi:

- Avtentikacija/avtorizacija poteka preko Microsoft Entra.
- Azure API Management deluje kot prehod in uporablja politike za usmerjanje in upravljanje prometa.
- Azure Monitor beleži vse zahteve za nadaljnjo analizo.

#### Potek avtorizacije

Poglejmo podrobneje potek avtorizacije:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP specifikacija avtorizacije

Več o [MCP specifikaciji avtorizacije](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization#2-10-third-party-authorization-flow)

## Uvajanje oddaljenega MCP strežnika v Azure

Poglejmo, ali lahko uvedemo prej omenjeni vzorec:

1. Klonirajte repozitorij

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

2. Registrirajte `Microsoft.App` resource provider.
    * If you are using Azure CLI, run `az provider register --namespace Microsoft.App --wait`.
    * If you are using Azure PowerShell, run `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Then run `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` in po nekaj času preverite, ali je registracija končana.

3. Zaženite ta [azd](https://aka.ms/azd) ukaz za pripravo api management storitve, funkcijske aplikacije (s kodo) in vseh drugih potrebnih Azure virov

    ```shell
    azd up
    ```

    Ta ukaz bi moral uvesti vse oblačne vire v Azure.

### Testiranje vašega strežnika z MCP Inspectorjem

1. V **novem terminalskem oknu** namestite in zaženite MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Videti bi morali vmesnik, podoben temu:

    ![Connect to Node inspector](../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.sl.png) 

2. CTRL kliknite, da naložite MCP Inspector spletno aplikacijo z URL-ja, ki ga aplikacija prikaže (npr. http://127.0.0.1:6274/#resources)
3. Nastavite tip prenosa na `SSE`
1. Set the URL to your running API Management SSE endpoint displayed after `azd up` in **Povežite se**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

5. **Seznam orodij**. Kliknite na orodje in izberite **Zaženi orodje**.

Če so bili vsi koraki uspešni, ste zdaj povezani z MCP strežnikom in ste lahko poklicali orodje.

## MCP strežniki za Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Ta niz repozitorijev je hitri začetek za gradnjo in uvajanje prilagojenih oddaljenih MCP (Model Context Protocol) strežnikov z uporabo Azure Functions v Pythonu, C# .NET ali Node/TypeScript.

Vzorec ponuja celovito rešitev, ki razvijalcem omogoča:

- Lokalni razvoj in zagon: Razvijajte in odpravljajte napake MCP strežnika na lokalnem računalniku
- Uvajanje v Azure: Enostavno uvajanje v oblak z ukazom azd up
- Povezovanje iz odjemalcev: Povežite se z MCP strežnikom iz različnih odjemalcev, vključno z VS Code v načinu Copilot agent in orodjem MCP Inspector

### Ključne funkcije:

- Varnost po zasnovi: MCP strežnik je zaščiten z ključi in HTTPS
- Možnosti avtentikacije: Podpira OAuth z vgrajeno avtentikacijo in/ali API Management
- Omrežna izolacija: Omogoča izolacijo omrežja z uporabo Azure Virtual Networks (VNET)
- Strežnik brez strežnika (serverless): Izkorišča Azure Functions za skalabilno, dogodkovno usmerjeno izvajanje
- Lokalni razvoj: Celovita podpora za lokalni razvoj in odpravljanje napak
- Enostavno uvajanje: Poenostavljen postopek uvajanja v Azure

Repozitorij vsebuje vse potrebne konfiguracijske datoteke, izvorno kodo in definicije infrastrukture, da hitro začnete z produkcijsko pripravljeno implementacijo MCP strežnika.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Vzorec implementacije MCP z uporabo Azure Functions v Pythonu

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Vzorec implementacije MCP z uporabo Azure Functions v C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Vzorec implementacije MCP z uporabo Azure Functions v Node/TypeScript.

## Ključne ugotovitve

- MCP SDK-ji nudijo jezikovno specifična orodja za implementacijo robustnih MCP rešitev
- Postopek odpravljanja napak in testiranja je ključen za zanesljive MCP aplikacije
- Ponovno uporabne predloge pozivov omogočajo dosledne interakcije z AI
- Dobro zasnovani delovni tokovi lahko orkestrirajo kompleksne naloge z uporabo več orodij
- Implementacija MCP rešitev zahteva upoštevanje varnosti, zmogljivosti in obravnave napak

## Vaja

Oblikujte praktičen MCP delovni tok, ki rešuje dejanski problem v vašem področju:

1. Izberite 3-4 orodja, ki bi bila koristna za reševanje tega problema
2. Naredite diagram delovnega toka, ki prikazuje, kako ta orodja medsebojno delujejo
3. Implementirajte osnovno različico enega od orodij v izbranem jeziku
4. Ustvarite predlogo poziva, ki bo modelu pomagala učinkovito uporabljati vaše orodje

## Dodatni viri


---

Naslednje: [Napredne teme](../05-AdvancedTopics/README.md)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitve za avtomatski prevod AI [Co-op Translator](https://github.com/Azure/co-op-translator). Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku velja za avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Nismo odgovorni za morebitna nesporazume ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.