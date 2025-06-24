<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5384bbb2a92d00d5d7e66274dbe0331d",
  "translation_date": "2025-06-20T18:41:47+00:00",
  "source_file": "04-PracticalImplementation/README.md",
  "language_code": "ms"
}
-->
# Pelaksanaan Praktikal

Pelaksanaan praktikal adalah di mana kekuatan Model Context Protocol (MCP) menjadi nyata. Walaupun memahami teori dan seni bina di sebalik MCP adalah penting, nilai sebenar muncul apabila anda menggunakan konsep ini untuk membina, menguji, dan melaksanakan penyelesaian yang menyelesaikan masalah dunia sebenar. Bab ini menghubungkan jurang antara pengetahuan konseptual dan pembangunan praktikal, membimbing anda melalui proses membawa aplikasi berasaskan MCP ke kehidupan sebenar.

Sama ada anda membangunkan pembantu pintar, mengintegrasikan AI ke dalam aliran kerja perniagaan, atau membina alat tersuai untuk pemprosesan data, MCP menyediakan asas yang fleksibel. Reka bentuk yang tidak bergantung pada bahasa dan SDK rasmi untuk bahasa pengaturcaraan popular menjadikannya mudah diakses oleh pelbagai pembangun. Dengan memanfaatkan SDK ini, anda boleh dengan cepat membuat prototaip, ulang kaji, dan skala penyelesaian anda merentasi platform dan persekitaran yang berbeza.

Dalam bahagian berikut, anda akan menemui contoh praktikal, kod sampel, dan strategi pelaksanaan yang menunjukkan cara melaksanakan MCP dalam C#, Java, TypeScript, JavaScript, dan Python. Anda juga akan belajar cara untuk debug dan menguji server MCP anda, mengurus API, dan melaksanakan penyelesaian ke awan menggunakan Azure. Sumber praktikal ini direka untuk mempercepatkan pembelajaran anda dan membantu anda membina aplikasi MCP yang kukuh dan sedia untuk pengeluaran dengan yakin.

## Gambaran Keseluruhan

Pelajaran ini menumpukan pada aspek praktikal pelaksanaan MCP merentasi pelbagai bahasa pengaturcaraan. Kita akan meneroka cara menggunakan MCP SDK dalam C#, Java, TypeScript, JavaScript, dan Python untuk membina aplikasi yang kukuh, debug dan uji server MCP, serta mencipta sumber, prompt, dan alat yang boleh digunakan semula.

## Objektif Pembelajaran

Menjelang akhir pelajaran ini, anda akan dapat:
- Melaksanakan penyelesaian MCP menggunakan SDK rasmi dalam pelbagai bahasa pengaturcaraan
- Debug dan uji server MCP secara sistematik
- Cipta dan gunakan ciri server (Sumber, Prompt, dan Alat)
- Reka aliran kerja MCP yang berkesan untuk tugasan kompleks
- Optimumkan pelaksanaan MCP untuk prestasi dan kebolehpercayaan

## Sumber SDK Rasmi

Model Context Protocol menawarkan SDK rasmi untuk pelbagai bahasa:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) 
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

## Bekerja dengan MCP SDK

Bahagian ini menyediakan contoh praktikal pelaksanaan MCP merentasi pelbagai bahasa pengaturcaraan. Anda boleh menemui kod sampel dalam direktori `samples` yang disusun mengikut bahasa.

### Sampel Tersedia

Repositori ini termasuk [pelaksanaan sampel](../../../04-PracticalImplementation/samples) dalam bahasa berikut:

- [C#](./samples/csharp/README.md)
- [Java](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Setiap sampel menunjukkan konsep utama MCP dan corak pelaksanaan untuk bahasa dan ekosistem tertentu itu.

## Ciri Utama Server

Server MCP boleh melaksanakan mana-mana gabungan ciri berikut:

### Sumber  
Sumber menyediakan konteks dan data untuk digunakan oleh pengguna atau model AI:  
- Repositori dokumen  
- Pangkalan pengetahuan  
- Sumber data berstruktur  
- Sistem fail  

### Prompt  
Prompt adalah mesej dan aliran kerja berformat untuk pengguna:  
- Templat perbualan yang telah ditetapkan  
- Corak interaksi berpandu  
- Struktur dialog khusus  

### Alat  
Alat adalah fungsi yang boleh dijalankan oleh model AI:  
- Utiliti pemprosesan data  
- Integrasi API luaran  
- Keupayaan pengiraan  
- Fungsi carian  

## Pelaksanaan Sampel: C#

Repositori SDK rasmi C# mengandungi beberapa pelaksanaan sampel yang menunjukkan pelbagai aspek MCP:

- **Klien MCP Asas**: Contoh mudah menunjukkan cara mencipta klien MCP dan memanggil alat  
- **Server MCP Asas**: Pelaksanaan server minimum dengan pendaftaran alat asas  
- **Server MCP Lanjutan**: Server lengkap dengan pendaftaran alat, pengesahan, dan pengendalian ralat  
- **Integrasi ASP.NET**: Contoh yang menunjukkan integrasi dengan ASP.NET Core  
- **Corak Pelaksanaan Alat**: Pelbagai corak untuk melaksanakan alat dengan tahap kerumitan berbeza  

SDK MCP C# adalah dalam pratonton dan API mungkin berubah. Kami akan sentiasa mengemas kini blog ini selaras dengan evolusi SDK.

### Ciri Utama  
- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)

- Membina [Server MCP pertama anda](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

Untuk contoh pelaksanaan C# lengkap, lawati [repositori sampel SDK C# rasmi](https://github.com/modelcontextprotocol/csharp-sdk)

## Pelaksanaan Sampel: Pelaksanaan Java

SDK Java menawarkan pilihan pelaksanaan MCP yang kukuh dengan ciri kelas perusahaan.

### Ciri Utama

- Integrasi Spring Framework  
- Keselamatan jenis yang kukuh  
- Sokongan pengaturcaraan reaktif  
- Pengendalian ralat yang menyeluruh  

Untuk contoh pelaksanaan Java lengkap, lihat [sampel Java](samples/java/containerapp/README.md) dalam direktori sampel.

## Pelaksanaan Sampel: Pelaksanaan JavaScript

SDK JavaScript menyediakan pendekatan ringan dan fleksibel untuk pelaksanaan MCP.

### Ciri Utama

- Sokongan Node.js dan pelayar  
- API berasaskan Promise  
- Integrasi mudah dengan Express dan rangka kerja lain  
- Sokongan WebSocket untuk penstriman  

Untuk contoh pelaksanaan JavaScript lengkap, lihat [sampel JavaScript](samples/javascript/README.md) dalam direktori sampel.

## Pelaksanaan Sampel: Pelaksanaan Python

SDK Python menawarkan pendekatan Pythonic untuk pelaksanaan MCP dengan integrasi rangka kerja ML yang hebat.

### Ciri Utama

- Sokongan async/await dengan asyncio  
- Integrasi Flask dan FastAPI  
- Pendaftaran alat yang mudah  
- Integrasi asli dengan perpustakaan ML popular  

Untuk contoh pelaksanaan Python lengkap, lihat [sampel Python](samples/python/README.md) dalam direktori sampel.

## Pengurusan API

Azure API Management adalah jawapan yang baik untuk bagaimana kita boleh mengamankan Server MCP. Idéanya adalah meletakkan instans Azure API Management di hadapan Server MCP anda dan membiarkannya mengendalikan ciri yang anda mungkin perlukan seperti:

- had kadar  
- pengurusan token  
- pemantauan  
- pengimbangan beban  
- keselamatan  

### Sampel Azure

Berikut adalah Sampel Azure yang melakukan perkara tersebut, iaitu [mencipta Server MCP dan mengamankannya dengan Azure API Management](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Lihat bagaimana aliran pengesahan berlaku dalam imej di bawah:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true) 

Dalam imej tersebut, perkara berikut berlaku:

- Pengesahan/Pengesahan berlaku menggunakan Microsoft Entra.  
- Azure API Management bertindak sebagai pintu masuk dan menggunakan polisi untuk mengarahkan dan mengurus trafik.  
- Azure Monitor merekod semua permintaan untuk analisis lanjut.  

#### Aliran Pengesahan

Mari kita lihat aliran pengesahan dengan lebih terperinci:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### Spesifikasi pengesahan MCP

Ketahui lebih lanjut tentang [spesifikasi Pengesahan MCP](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization#2-10-third-party-authorization-flow)

## Melaksanakan Server MCP Jauh ke Azure

Mari kita lihat jika kita boleh melaksanakan sampel yang disebutkan tadi:

1. Klon repositori

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. Daftar `Microsoft.App` resource provider.
    * If you are using Azure CLI, run `az provider register --namespace Microsoft.App --wait`.
    * If you are using Azure PowerShell, run `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Then run `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` selepas beberapa ketika untuk menyemak jika pendaftaran selesai.

2. Jalankan arahan [azd](https://aka.ms/azd) ini untuk menyediakan perkhidmatan pengurusan API, function app (dengan kod) dan semua sumber Azure lain yang diperlukan

    ```shell
    azd up
    ```

    Arahan ini akan melaksanakan semua sumber awan di Azure

### Menguji server anda dengan MCP Inspector

1. Dalam **tetingkap terminal baru**, pasang dan jalankan MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Anda sepatutnya melihat antara muka seperti berikut:

    ![Connect to Node inspector](../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.ms.png) 

1. CTRL klik untuk memuatkan aplikasi web MCP Inspector dari URL yang dipaparkan oleh aplikasi (contoh: http://127.0.0.1:6274/#resources)  
1. Tetapkan jenis pengangkutan ke `SSE`
1. Set the URL to your running API Management SSE endpoint displayed after `azd up` dan **Sambung**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

5. **Senaraikan Alat**. Klik pada alat dan **Jalankan Alat**.  

Jika semua langkah berjaya, anda kini sepatutnya disambungkan ke server MCP dan berjaya memanggil alat.

## Server MCP untuk Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Set repositori ini adalah templat permulaan pantas untuk membina dan melaksanakan server MCP jauh tersuai menggunakan Azure Functions dengan Python, C# .NET atau Node/TypeScript.

Sampel ini menyediakan penyelesaian lengkap yang membolehkan pembangun untuk:

- Bina dan jalankan secara tempatan: Bangunkan dan debug server MCP pada mesin tempatan  
- Laksanakan ke Azure: Mudah melaksanakan ke awan dengan arahan azd up yang ringkas  
- Sambung dari klien: Sambung ke server MCP dari pelbagai klien termasuk mod ejen Copilot VS Code dan alat MCP Inspector  

### Ciri Utama:

- Keselamatan secara reka bentuk: Server MCP diamankan menggunakan kunci dan HTTPS  
- Pilihan pengesahan: Menyokong OAuth menggunakan pengesahan terbina dalam dan/atau Pengurusan API  
- Pengasingan rangkaian: Membenarkan pengasingan rangkaian menggunakan Azure Virtual Networks (VNET)  
- Seni bina tanpa server: Memanfaatkan Azure Functions untuk pelaksanaan yang boleh diskala dan berasaskan acara  
- Pembangunan tempatan: Sokongan pembangunan dan debug tempatan yang menyeluruh  
- Pelaksanaan mudah: Proses pelaksanaan yang dipermudahkan ke Azure  

Repositori mengandungi semua fail konfigurasi yang diperlukan, kod sumber, dan definisi infrastruktur untuk memulakan dengan cepat pelaksanaan server MCP yang sedia untuk pengeluaran.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Pelaksanaan sampel MCP menggunakan Azure Functions dengan Python

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Pelaksanaan sampel MCP menggunakan Azure Functions dengan C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Pelaksanaan sampel MCP menggunakan Azure Functions dengan Node/TypeScript.

## Perkara Penting

- SDK MCP menyediakan alat khusus bahasa untuk melaksanakan penyelesaian MCP yang kukuh  
- Proses debug dan ujian adalah penting untuk aplikasi MCP yang boleh dipercayai  
- Templat prompt yang boleh digunakan semula membolehkan interaksi AI yang konsisten  
- Aliran kerja yang direka dengan baik boleh mengatur tugasan kompleks menggunakan pelbagai alat  
- Melaksanakan penyelesaian MCP memerlukan pertimbangan keselamatan, prestasi, dan pengendalian ralat  

## Latihan

Reka aliran kerja MCP praktikal yang menangani masalah dunia sebenar dalam domain anda:

1. Kenal pasti 3-4 alat yang berguna untuk menyelesaikan masalah ini  
2. Cipta rajah aliran kerja yang menunjukkan bagaimana alat-alat ini berinteraksi  
3. Laksanakan versi asas salah satu alat menggunakan bahasa pilihan anda  
4. Cipta templat prompt yang membantu model menggunakan alat anda dengan berkesan  

## Sumber Tambahan


---

Seterusnya: [Topik Lanjutan](../05-AdvancedTopics/README.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat yang kritikal, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.