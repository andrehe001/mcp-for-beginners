<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5384bbb2a92d00d5d7e66274dbe0331d",
  "translation_date": "2025-06-20T18:42:43+00:00",
  "source_file": "04-PracticalImplementation/README.md",
  "language_code": "sw"
}
-->
# Utekelezaji wa Kivitendo

Utekelezaji wa kivitendo ndio sehemu ambapo nguvu ya Model Context Protocol (MCP) inakuwa dhahiri. Ingawa kuelewa nadharia na usanifu wa MCP ni muhimu, thamani halisi hujitokeza unapotekeleza dhana hizi kujenga, kujaribu, na kupeleka suluhisho zinazotatua matatizo halisi. Sura hii inavuka pengo kati ya maarifa ya dhana na maendeleo ya vitendo, ikikuongoza kupitia mchakato wa kuleta programu zinazotumia MCP kuwa halisi.

Iwe unatengeneza wasaidizi wa akili, kuingiza AI katika mtiririko wa kazi wa biashara, au kujenga zana maalum za usindikaji data, MCP hutoa msingi rahisi kubadilika. Muundo wake usioegemea lugha yoyote na SDK rasmi kwa lugha maarufu za programu hufanya iwe rahisi kwa watengenezaji wengi. Kwa kutumia SDK hizi, unaweza haraka kutengeneza mfano, kuendelea kuboresha, na kupanua suluhisho zako katika majukwaa na mazingira tofauti.

Katika sehemu zinazofuata, utapata mifano ya vitendo, nambari za sampuli, na mikakati ya upeleaji inayonyesha jinsi ya kutekeleza MCP katika C#, Java, TypeScript, JavaScript, na Python. Pia utajifunza jinsi ya kufuatilia makosa na kujaribu seva zako za MCP, kusimamia APIs, na kupeleka suluhisho katika wingu kwa kutumia Azure. Vifaa hivi vya vitendo vimeundwa kukuongezea kasi ya kujifunza na kukusaidia kujenga kwa kujiamini programu thabiti, tayari kwa uzalishaji za MCP.

## Muhtasari

Somo hili linazingatia nyanja za vitendo za utekelezaji wa MCP katika lugha mbalimbali za programu. Tutachunguza jinsi ya kutumia MCP SDKs katika C#, Java, TypeScript, JavaScript, na Python kujenga programu thabiti, kufuatilia makosa na kujaribu seva za MCP, na kuunda rasilimali, maelekezo, na zana zinazoweza kutumika tena.

## Malengo ya Kujifunza

Mwisho wa somo hili, utaweza:
- Kutekeleza suluhisho za MCP kwa kutumia SDK rasmi katika lugha mbalimbali za programu
- Kufuatilia makosa na kujaribu seva za MCP kwa mfumo mzuri
- Kuunda na kutumia vipengele vya seva (Rasilimali, Maelekezo, na Zana)
- Kubuni mtiririko mzuri wa MCP kwa kazi tata
- Kuboresha utekelezaji wa MCP kwa ajili ya utendaji na uaminifu

## Rasilimali Rasmi za SDK

Model Context Protocol hutoa SDK rasmi kwa lugha nyingi:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) 
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

## Kufanya kazi na MCP SDKs

Sehemu hii inatoa mifano ya vitendo ya utekelezaji wa MCP katika lugha mbalimbali za programu. Unaweza kupata nambari za sampuli katika saraka ya `samples` iliyopangwa kwa lugha.

### Sampuli Zinazopatikana

Hifadhi ina [utekelezaji wa sampuli](../../../04-PracticalImplementation/samples) katika lugha zifuatazo:

- [C#](./samples/csharp/README.md)
- [Java](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Kila sampuli inaonyesha dhana kuu za MCP na mifumo ya utekelezaji kwa lugha na mfumo husika.

## Vipengele vya Msingi vya Seva

Seva za MCP zinaweza kutekeleza mchanganyiko wowote wa vipengele hivi:

### Rasilimali
Rasilimali hutoa muktadha na data kwa mtumiaji au mfano wa AI kutumia:
- Hifadhi za nyaraka
- Misingi ya maarifa
- Vyanzo vya data vilivyopangwa
- Mifumo ya faili

### Maelekezo
Maelekezo ni ujumbe wa templeti na mtiririko wa kazi kwa watumiaji:
- Templeti za mazungumzo zilizotanguliwa
- Mifumo ya maingiliano iliyoongozwa
- Miundo maalum ya mazungumzo

### Zana
Zana ni kazi za mfano wa AI kutekeleza:
- Zana za usindikaji data
- Muunganisho wa API za nje
- Uwezo wa kihesabu
- Kazi za utafutaji

## Mifano ya Utekelezaji: C#

Hifadhi rasmi ya SDK ya C# ina mifano kadhaa inayoonyesha nyanja tofauti za MCP:

- **Mteja wa MCP wa Msingi**: Mfano rahisi unaoonyesha jinsi ya kuunda mteja wa MCP na kuitisha zana
- **Seva ya MCP ya Msingi**: Utekelezaji mdogo wa seva yenye usajili wa zana za msingi
- **Seva ya MCP ya Juu**: Seva yenye vipengele kamili na usajili wa zana, uthibitishaji, na usimamizi wa makosa
- **Muunganisho wa ASP.NET**: Mifano inayoonyesha muunganisho na ASP.NET Core
- **Mifumo ya Utekelezaji wa Zana**: Mifumo mbalimbali ya kutekeleza zana zenye ngazi tofauti za ugumu

SDK ya MCP ya C# iko katika awamu ya majaribio na API zinaweza kubadilika. Tutaendelea kusasisha blogu hii kadri SDK inavyoendelea.

### Vipengele Muhimu
- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)

- Kujenga [Seva yako ya MCP ya Kwanza](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

Kwa mifano kamili ya utekelezaji wa C#, tembelea [hifadhi rasmi ya mifano ya SDK ya C#](https://github.com/modelcontextprotocol/csharp-sdk)

## Mfano wa utekelezaji: Utekelezaji wa Java

SDK ya Java inatoa chaguzi thabiti za utekelezaji wa MCP zenye vipengele vya kiwango cha biashara.

### Vipengele Muhimu

- Muunganisho wa Spring Framework
- Usalama wa aina thabiti
- Msaada wa programu ya kuhimili matukio (reactive programming)
- Usimamizi kamili wa makosa

Kwa mfano kamili wa utekelezaji wa Java, angalia [sampuli ya Java](samples/java/containerapp/README.md) katika saraka ya mifano.

## Mfano wa utekelezaji: Utekelezaji wa JavaScript

SDK ya JavaScript hutoa njia nyepesi na rahisi kubadilika kwa utekelezaji wa MCP.

### Vipengele Muhimu

- Msaada wa Node.js na kivinjari
- API inayotegemea ahadi (promise-based)
- Muunganisho rahisi na Express na mifumo mingine
- Msaada wa WebSocket kwa mtiririko wa data

Kwa mfano kamili wa utekelezaji wa JavaScript, angalia [sampuli ya JavaScript](samples/javascript/README.md) katika saraka ya mifano.

## Mfano wa utekelezaji: Utekelezaji wa Python

SDK ya Python hutoa njia ya Ki-python ya utekelezaji wa MCP yenye muunganisho mzuri na mifumo ya ML.

### Vipengele Muhimu

- Msaada wa async/await kwa asyncio
- Muunganisho wa Flask na FastAPI
- Usajili rahisi wa zana
- Muunganisho wa asili na maktaba maarufu za ML

Kwa mfano kamili wa utekelezaji wa Python, angalia [sampuli ya Python](samples/python/README.md) katika saraka ya mifano.

## Usimamizi wa API

Azure API Management ni suluhisho nzuri la jinsi tunavyoweza kulinda Seva za MCP. Wazo ni kuweka mfano wa Azure API Management mbele ya Seva yako ya MCP na kuiruhusu kusimamia vipengele unavyotaka kama:

- Kuzuia kasi ya maombi
- Usimamizi wa tokeni
- Ufuatiliaji
- Usawazishaji mzigo
- Usalama

### Sampuli ya Azure

Hii ni Sampuli ya Azure inayofanya hasa hivyo, yaani [kuunda Seva ya MCP na kuilinda kwa Azure API Management](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Angalia jinsi mtiririko wa idhini unavyotokea kwenye picha ifuatayo:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true) 

Katika picha hapo juu, yafuatayo hutokea:

- Uthibitishaji/Idhini hutokea kwa kutumia Microsoft Entra.
- Azure API Management hufanya kazi kama lango na hutumia sera kusimamia na kuelekeza trafiki.
- Azure Monitor hurekodi maombi yote kwa uchambuzi zaidi.

#### Mtiririko wa Idhini

Tuchunguze mtiririko wa idhini kwa undani zaidi:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### Maelezo ya Idhini ya MCP

Jifunze zaidi kuhusu [Maelezo ya Idhini ya MCP](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization#2-10-third-party-authorization-flow)

## Kuweka Seva ya Remote MCP Azure

Tuwe tukaangalie kama tunaweza kupeleka sampuli tulizotaja awali:

1. Fanya nakala ya repo

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. Sajili `Microsoft.App` resource provider.
    * If you are using Azure CLI, run `az provider register --namespace Microsoft.App --wait`.
    * If you are using Azure PowerShell, run `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Then run `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` baada ya muda ili kuangalia kama usajili umekamilika.

2. Endesha amri hii ya [azd](https://aka.ms/azd) ili kuanzisha huduma ya usimamizi wa API, app ya function (na nambari) na rasilimali zote za Azure zinazohitajika

    ```shell
    azd up
    ```

    Amri hizi zinapaswa kupeleka rasilimali zote za wingu kwenye Azure

### Kuangalia seva yako kwa MCP Inspector

1. Katika **dirisha jipya la terminal**, sakinisha na endesha MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Unapaswa kuona kiolesura kama hiki:

    ![Connect to Node inspector](../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.sw.png) 

1. Bonyeza CTRL ili kupakia app ya wavuti ya MCP Inspector kutoka kwenye URL inayotolewa na app (mfano http://127.0.0.1:6274/#resources)
1. Weka aina ya usafirishaji kuwa `SSE`
1. Set the URL to your running API Management SSE endpoint displayed after `azd up` na **Unganisha**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

5. **Orodhesha Zana**. Bonyeza zana na **Endesha Zana**.

Kama hatua zote zimefanikiwa, sasa unapaswa kuwa umeunganishwa na seva ya MCP na umeweza kuitisha zana.

## Seva za MCP kwa Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Seti hii ya hifadhi ni templeti ya kuanza haraka kwa kujenga na kupeleka seva za MCP za mbali (Model Context Protocol) kwa kutumia Azure Functions na Python, C# .NET au Node/TypeScript.

Mifano hutoa suluhisho kamili linalowawezesha watengenezaji:

- Kujenga na kuendesha ndani ya eneo: Tengeneza na fuatilia makosa seva ya MCP kwenye mashine ya ndani
- Kupeleka kwa Azure: Rahisi kupeleka kwenye wingu kwa amri rahisi ya azd up
- Kuungana kutoka kwa wateja: Ungana na seva ya MCP kutoka kwa wateja mbalimbali ikiwemo hali ya wakala wa Copilot wa VS Code na zana ya MCP Inspector

### Vipengele Muhimu:

- Usalama kwa muundo: Seva ya MCP inalindwa kwa kutumia funguo na HTTPS
- Chaguzi za uthibitishaji: Inasaidia OAuth kwa kutumia uthibitishaji uliyojengwa ndani na/au API Management
- Kutenganishwa kwa mtandao: Inaruhusu kutenganishwa kwa mtandao kwa kutumia Azure Virtual Networks (VNET)
- Miundombinu isiyo na seva (serverless): Inatumia Azure Functions kwa utekelezaji unaoweza kupanuka na kuendeshwa kwa matukio
- Maendeleo ya ndani: Msaada kamili wa maendeleo na kufuatilia makosa ndani ya eneo
- Upeleaji rahisi: Mchakato rahisi wa kupeleka kwa Azure

Hifadhi ina faili zote muhimu za usanidi, nambari chanzo, na maelezo ya miundombinu ili kuanza haraka na utekelezaji wa seva ya MCP tayari kwa uzalishaji.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Mfano wa utekelezaji wa MCP kwa kutumia Azure Functions na Python

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Mfano wa utekelezaji wa MCP kwa kutumia Azure Functions na C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Mfano wa utekelezaji wa MCP kwa kutumia Azure Functions na Node/TypeScript.

## Muhimu wa Kujifunza

- SDK za MCP hutoa zana maalum za lugha kwa ajili ya kutekeleza suluhisho thabiti za MCP
- Mchakato wa kufuatilia makosa na kujaribu ni muhimu kwa programu za MCP zenye uaminifu
- Templeti za maelekezo zinazoweza kutumika tena hutoa maingiliano thabiti ya AI
- Mitiririko iliyobuniwa vizuri inaweza kuratibu kazi tata kwa kutumia zana nyingi
- Kutekeleza suluhisho za MCP kunahitaji kuzingatia usalama, utendaji, na usimamizi wa makosa

## Mazoezi

Buni mtiririko wa kazi wa MCP wa kivitendo unaoshughulikia tatizo halisi katika eneo lako:

1. Tambua zana 3-4 zitakazosaidia kutatua tatizo hili
2. Tengeneza mchoro wa mtiririko unaoonyesha jinsi zana hizi zinavyoshirikiana
3. Tekeleza toleo la msingi la moja ya zana hizo kwa kutumia lugha unayopendelea
4. Unda templeti ya maelekezo itakayosaidia mfano kutumia zana yako kwa ufanisi

## Rasilimali Zaidi


---

Ifuatayo: [Mada Zinazopitia Zaidi](../05-AdvancedTopics/README.md)

**Kangisho**:  
Hati hii imetafsiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Ingawa tunajitahidi kuwa sahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au upungufu wa usahihi. Hati asili katika lugha yake ya asili inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, tafsiri ya kitaalamu inayofanywa na binadamu inapendekezwa. Hatuna wajibu kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.