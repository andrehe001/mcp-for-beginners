<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5384bbb2a92d00d5d7e66274dbe0331d",
  "translation_date": "2025-06-20T18:41:24+00:00",
  "source_file": "04-PracticalImplementation/README.md",
  "language_code": "id"
}
-->
# Implementasi Praktis

Implementasi praktis adalah saat kekuatan Model Context Protocol (MCP) menjadi nyata. Meskipun memahami teori dan arsitektur di balik MCP penting, nilai sebenarnya muncul ketika Anda menerapkan konsep-konsep ini untuk membangun, menguji, dan menerapkan solusi yang menyelesaikan masalah dunia nyata. Bab ini menjembatani kesenjangan antara pengetahuan konseptual dan pengembangan langsung, membimbing Anda melalui proses menghidupkan aplikasi berbasis MCP.

Baik Anda mengembangkan asisten cerdas, mengintegrasikan AI ke dalam alur kerja bisnis, atau membangun alat khusus untuk pemrosesan data, MCP menyediakan fondasi yang fleksibel. Desainnya yang tidak bergantung pada bahasa pemrograman dan SDK resmi untuk bahasa pemrograman populer membuatnya dapat diakses oleh berbagai pengembang. Dengan memanfaatkan SDK ini, Anda dapat dengan cepat membuat prototipe, melakukan iterasi, dan mengembangkan solusi Anda di berbagai platform dan lingkungan.

Di bagian berikut, Anda akan menemukan contoh praktis, kode sampel, dan strategi penerapan yang menunjukkan cara mengimplementasikan MCP dalam C#, Java, TypeScript, JavaScript, dan Python. Anda juga akan belajar bagaimana melakukan debug dan pengujian server MCP, mengelola API, dan menerapkan solusi ke cloud menggunakan Azure. Sumber daya praktis ini dirancang untuk mempercepat pembelajaran Anda dan membantu Anda membangun aplikasi MCP yang kuat dan siap produksi dengan percaya diri.

## Ikhtisar

Pelajaran ini berfokus pada aspek praktis implementasi MCP di berbagai bahasa pemrograman. Kita akan menjelajahi cara menggunakan SDK MCP di C#, Java, TypeScript, JavaScript, dan Python untuk membangun aplikasi yang tangguh, melakukan debug dan pengujian server MCP, serta membuat sumber daya, prompt, dan alat yang dapat digunakan ulang.

## Tujuan Pembelajaran

Pada akhir pelajaran ini, Anda akan mampu:
- Mengimplementasikan solusi MCP menggunakan SDK resmi dalam berbagai bahasa pemrograman
- Melakukan debug dan pengujian server MCP secara sistematis
- Membuat dan menggunakan fitur server (Resources, Prompts, dan Tools)
- Merancang alur kerja MCP yang efektif untuk tugas-tugas kompleks
- Mengoptimalkan implementasi MCP untuk performa dan keandalan

## Sumber SDK Resmi

Model Context Protocol menyediakan SDK resmi untuk beberapa bahasa:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) 
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

## Bekerja dengan SDK MCP

Bagian ini memberikan contoh praktis implementasi MCP di berbagai bahasa pemrograman. Anda dapat menemukan kode sampel di direktori `samples` yang diorganisir berdasarkan bahasa.

### Sampel yang Tersedia

Repositori ini mencakup [implementasi sampel](../../../04-PracticalImplementation/samples) dalam bahasa-bahasa berikut:

- [C#](./samples/csharp/README.md)
- [Java](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Setiap sampel menunjukkan konsep utama MCP dan pola implementasi untuk bahasa dan ekosistem tersebut.

## Fitur Utama Server

Server MCP dapat mengimplementasikan kombinasi dari fitur-fitur berikut:

### Resources  
Resources menyediakan konteks dan data untuk digunakan oleh pengguna atau model AI:
- Repositori dokumen
- Basis pengetahuan
- Sumber data terstruktur
- Sistem berkas

### Prompts  
Prompts adalah pesan dan alur kerja yang sudah ditemplatkan untuk pengguna:
- Template percakapan yang sudah ditentukan
- Pola interaksi yang dipandu
- Struktur dialog khusus

### Tools  
Tools adalah fungsi yang dapat dijalankan oleh model AI:
- Utilitas pemrosesan data
- Integrasi API eksternal
- Kapabilitas komputasi
- Fungsi pencarian

## Contoh Implementasi: C#

Repositori SDK C# resmi berisi beberapa contoh implementasi yang menunjukkan berbagai aspek MCP:

- **Basic MCP Client**: Contoh sederhana yang menunjukkan cara membuat klien MCP dan memanggil tools
- **Basic MCP Server**: Implementasi server minimal dengan pendaftaran tool dasar
- **Advanced MCP Server**: Server lengkap dengan pendaftaran tool, autentikasi, dan penanganan kesalahan
- **Integrasi ASP.NET**: Contoh yang menunjukkan integrasi dengan ASP.NET Core
- **Pola Implementasi Tool**: Berbagai pola untuk mengimplementasikan tools dengan tingkat kompleksitas berbeda

SDK MCP C# masih dalam tahap preview dan API dapat berubah. Kami akan terus memperbarui blog ini seiring perkembangan SDK.

### Fitur Utama  
- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)

- Membangun [Server MCP pertama Anda](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

Untuk contoh implementasi C# lengkap, kunjungi [repositori sampel SDK C# resmi](https://github.com/modelcontextprotocol/csharp-sdk)

## Contoh Implementasi: Java

SDK Java menawarkan opsi implementasi MCP yang kuat dengan fitur kelas enterprise.

### Fitur Utama

- Integrasi Spring Framework
- Keamanan tipe yang kuat
- Dukungan pemrograman reaktif
- Penanganan kesalahan yang komprehensif

Untuk contoh implementasi Java lengkap, lihat [sampel Java](samples/java/containerapp/README.md) di direktori sampel.

## Contoh Implementasi: JavaScript

SDK JavaScript menyediakan pendekatan yang ringan dan fleksibel untuk implementasi MCP.

### Fitur Utama

- Dukungan Node.js dan browser
- API berbasis Promise
- Integrasi mudah dengan Express dan framework lain
- Dukungan WebSocket untuk streaming

Untuk contoh implementasi JavaScript lengkap, lihat [sampel JavaScript](samples/javascript/README.md) di direktori sampel.

## Contoh Implementasi: Python

SDK Python menawarkan pendekatan Pythonic untuk implementasi MCP dengan integrasi framework ML yang sangat baik.

### Fitur Utama

- Dukungan async/await dengan asyncio
- Integrasi Flask dan FastAPI
- Pendaftaran tool yang sederhana
- Integrasi native dengan pustaka ML populer

Untuk contoh implementasi Python lengkap, lihat [sampel Python](samples/python/README.md) di direktori sampel.

## Manajemen API

Azure API Management adalah solusi tepat untuk mengamankan server MCP. Ide dasarnya adalah menempatkan instance Azure API Management di depan server MCP Anda dan membiarkannya menangani fitur-fitur yang kemungkinan Anda butuhkan seperti:

- pembatasan laju (rate limiting)
- manajemen token
- pemantauan
- load balancing
- keamanan

### Contoh Azure

Berikut adalah contoh Azure yang melakukan hal tersebut, yaitu [membuat server MCP dan mengamankannya dengan Azure API Management](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Lihat bagaimana alur otorisasi berlangsung pada gambar di bawah ini:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true) 

Pada gambar tersebut terjadi hal-hal berikut:

- Autentikasi/Otorisasi dilakukan menggunakan Microsoft Entra.
- Azure API Management berperan sebagai gateway dan menggunakan kebijakan untuk mengarahkan dan mengelola trafik.
- Azure Monitor mencatat semua permintaan untuk analisis lebih lanjut.

#### Alur Otorisasi

Mari kita lihat lebih detail alur otorisasi berikut:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### Spesifikasi Otorisasi MCP

Pelajari lebih lanjut tentang [spesifikasi Otorisasi MCP](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization#2-10-third-party-authorization-flow)

## Menerapkan Remote MCP Server ke Azure

Mari kita lihat apakah kita bisa menerapkan sampel yang disebutkan sebelumnya:

1. Clone repo

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

2. Daftarkan `Microsoft.App`  
    ` resource provider.
    * If you are using Azure CLI, run `az provider register --namespace Microsoft.App --wait`.
    * If you are using Azure PowerShell, run `  
    `. Then run `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Then run `  
    Tunggu beberapa saat lalu cek apakah pendaftaran sudah selesai dengan perintah `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState`.

3. Jalankan perintah [azd](https://aka.ms/azd) ini untuk menyediakan layanan api management, function app (beserta kode), dan semua sumber daya Azure yang diperlukan

    ```shell
    azd up
    ```

    Perintah ini akan menerapkan semua sumber daya cloud di Azure

### Menguji server Anda dengan MCP Inspector

1. Di **jendela terminal baru**, instal dan jalankan MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Anda akan melihat antarmuka serupa:

    ![Connect to Node inspector](../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.id.png) 

2. Klik CTRL untuk membuka aplikasi web MCP Inspector dari URL yang ditampilkan oleh aplikasi (misalnya http://127.0.0.1:6274/#resources)
3. Setel tipe transport ke `SSE``
1. Set the URL to your running API Management SSE endpoint displayed after `azd up` dan **Connect**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

5. **List Tools**. Klik pada sebuah tool dan **Run Tool**.  

Jika semua langkah berhasil, Anda sekarang terhubung ke server MCP dan dapat memanggil sebuah tool.

## Server MCP untuk Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Kumpulan repositori ini adalah template cepat untuk membangun dan menerapkan server MCP (Model Context Protocol) jarak jauh khusus menggunakan Azure Functions dengan Python, C# .NET, atau Node/TypeScript.

Sampel ini menyediakan solusi lengkap yang memungkinkan pengembang untuk:

- Membangun dan menjalankan secara lokal: Mengembangkan dan debug server MCP di mesin lokal
- Menerapkan ke Azure: Dengan mudah menerapkan ke cloud menggunakan perintah azd up sederhana
- Terhubung dari klien: Terhubung ke server MCP dari berbagai klien termasuk mode agen Copilot di VS Code dan alat MCP Inspector

### Fitur Utama:

- Keamanan sejak desain: Server MCP diamankan menggunakan kunci dan HTTPS
- Opsi autentikasi: Mendukung OAuth menggunakan autentikasi bawaan dan/atau API Management
- Isolasi jaringan: Memungkinkan isolasi jaringan menggunakan Azure Virtual Networks (VNET)
- Arsitektur serverless: Memanfaatkan Azure Functions untuk eksekusi yang skalabel dan berbasis event
- Pengembangan lokal: Dukungan lengkap untuk pengembangan dan debug lokal
- Penerapan sederhana: Proses penerapan yang mudah ke Azure

Repositori ini mencakup semua file konfigurasi, kode sumber, dan definisi infrastruktur yang diperlukan untuk memulai dengan cepat implementasi server MCP yang siap produksi.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Contoh implementasi MCP menggunakan Azure Functions dengan Python

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Contoh implementasi MCP menggunakan Azure Functions dengan C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Contoh implementasi MCP menggunakan Azure Functions dengan Node/TypeScript.

## Poin Penting

- SDK MCP menyediakan alat spesifik bahasa untuk mengimplementasikan solusi MCP yang tangguh
- Proses debugging dan pengujian sangat penting untuk aplikasi MCP yang andal
- Template prompt yang dapat digunakan ulang memungkinkan interaksi AI yang konsisten
- Alur kerja yang dirancang dengan baik dapat mengatur tugas kompleks menggunakan banyak tools
- Mengimplementasikan solusi MCP membutuhkan perhatian pada aspek keamanan, performa, dan penanganan kesalahan

## Latihan

Rancang alur kerja MCP praktis yang menangani masalah nyata di bidang Anda:

1. Identifikasi 3-4 tools yang akan berguna untuk menyelesaikan masalah ini
2. Buat diagram alur kerja yang menunjukkan bagaimana tools ini berinteraksi
3. Implementasikan versi dasar salah satu tools menggunakan bahasa pilihan Anda
4. Buat template prompt yang membantu model menggunakan tool Anda secara efektif

## Sumber Daya Tambahan


---

Selanjutnya: [Topik Lanjutan](../05-AdvancedTopics/README.md)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.