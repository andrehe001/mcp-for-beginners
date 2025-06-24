<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "36de9fae488d6de554d969fe8e0801a8",
  "translation_date": "2025-06-20T19:22:50+00:00",
  "source_file": "09-CaseStudy/apimsample.md",
  "language_code": "id"
}
-->
# Studi Kasus: Mengekspos REST API di API Management sebagai server MCP

Azure API Management adalah layanan yang menyediakan Gateway di atas Endpoint API Anda. Cara kerjanya adalah Azure API Management bertindak seperti proxy di depan API Anda dan dapat menentukan apa yang harus dilakukan dengan permintaan yang masuk.

Dengan menggunakannya, Anda menambahkan berbagai fitur seperti:

- **Keamanan**, Anda dapat menggunakan segala sesuatu mulai dari API keys, JWT hingga managed identity.
- **Pembatasan kecepatan (rate limiting)**, fitur hebat yang memungkinkan Anda menentukan berapa banyak panggilan yang diperbolehkan dalam satuan waktu tertentu. Ini membantu memastikan semua pengguna mendapatkan pengalaman yang baik dan juga agar layanan Anda tidak kewalahan dengan permintaan.
- **Skalabilitas & Load balancing**. Anda dapat mengatur sejumlah endpoint untuk menyeimbangkan beban dan juga dapat menentukan bagaimana "load balance" dilakukan.
- **Fitur AI seperti semantic caching**, batas token dan pemantauan token, dan lainnya. Ini adalah fitur hebat yang meningkatkan responsivitas serta membantu Anda mengontrol pengeluaran token. [Baca selengkapnya di sini](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Mengapa MCP + Azure API Management?

Model Context Protocol dengan cepat menjadi standar untuk aplikasi AI agentik dan cara mengekspos alat serta data secara konsisten. Azure API Management adalah pilihan alami ketika Anda perlu "mengelola" API. Server MCP sering terintegrasi dengan API lain untuk menyelesaikan permintaan ke sebuah alat, misalnya. Oleh karena itu menggabungkan Azure API Management dan MCP sangat masuk akal.

## Gambaran Umum

Dalam kasus penggunaan khusus ini, kita akan belajar mengekspos endpoint API sebagai server MCP. Dengan melakukan ini, kita dapat dengan mudah menjadikan endpoint ini bagian dari aplikasi agentik sekaligus memanfaatkan fitur dari Azure API Management.

## Fitur Utama

- Anda memilih metode endpoint yang ingin diekspos sebagai alat.
- Fitur tambahan yang Anda dapatkan tergantung pada apa yang Anda konfigurasi di bagian kebijakan untuk API Anda. Namun di sini kami akan menunjukkan cara menambahkan pembatasan kecepatan.

## Langkah awal: impor API

Jika Anda sudah memiliki API di Azure API Management, bagus, Anda bisa melewati langkah ini. Jika belum, lihat tautan ini, [mengimpor API ke Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Mengekspos API sebagai Server MCP

Untuk mengekspos endpoint API, ikuti langkah-langkah berikut:

1. Buka Azure Portal dan alamat berikut <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
   Arahkan ke instance API Management Anda.

1. Di menu kiri, pilih APIs > MCP Servers > + Create new MCP Server.

1. Pada bagian API, pilih REST API yang akan diekspos sebagai server MCP.

1. Pilih satu atau lebih Operasi API yang akan diekspos sebagai alat. Anda bisa memilih semua operasi atau hanya operasi tertentu.

    ![Pilih metode yang akan diekspos](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Pilih **Create**.

1. Arahkan ke menu **APIs** dan **MCP Servers**, Anda akan melihat seperti berikut:

    ![Lihat MCP Server di panel utama](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    Server MCP telah dibuat dan operasi API diekspos sebagai alat. Server MCP tercantum di panel MCP Servers. Kolom URL menunjukkan endpoint server MCP yang dapat Anda panggil untuk pengujian atau dalam aplikasi klien.

## Opsional: Konfigurasi kebijakan

Azure API Management memiliki konsep inti kebijakan di mana Anda mengatur aturan berbeda untuk endpoint Anda, seperti pembatasan kecepatan atau semantic caching. Kebijakan ini ditulis dalam format XML.

Berikut cara mengatur kebijakan untuk membatasi kecepatan server MCP Anda:

1. Di portal, di bawah APIs, pilih **MCP Servers**.

1. Pilih server MCP yang telah Anda buat.

1. Di menu kiri, di bawah MCP, pilih **Policies**.

1. Di editor kebijakan, tambahkan atau edit kebijakan yang ingin diterapkan pada alat server MCP. Kebijakan didefinisikan dalam format XML. Misalnya, Anda dapat menambahkan kebijakan untuk membatasi panggilan ke alat server MCP (dalam contoh ini, 5 panggilan per 30 detik per alamat IP klien). Berikut XML yang akan menyebabkan pembatasan kecepatan:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Berikut gambar editor kebijakan:

    ![Editor kebijakan](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Coba

Mari pastikan server MCP kita berfungsi sebagaimana mestinya.

Untuk ini, kita akan menggunakan Visual Studio Code dan GitHub Copilot dengan mode Agent-nya. Kita akan menambahkan server MCP ke *mcp.json*. Dengan cara ini, Visual Studio Code akan bertindak sebagai klien dengan kemampuan agentik dan pengguna akhir dapat mengetik prompt dan berinteraksi dengan server tersebut.

Berikut cara menambahkan server MCP di Visual Studio Code:

1. Gunakan perintah MCP: **Add Server dari Command Palette**.

1. Saat diminta, pilih tipe server: **HTTP (HTTP atau Server Sent Events)**.

1. Masukkan URL server MCP di API Management. Contoh: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (untuk endpoint SSE) atau **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (untuk endpoint MCP), perhatikan perbedaan antara transport adalah `/sse` or `/mcp`.

1. Masukkan ID server sesuai pilihan Anda. Ini bukan nilai penting tetapi membantu Anda mengingat instance server ini.

1. Pilih apakah ingin menyimpan konfigurasi ke pengaturan workspace atau pengaturan pengguna.

  - **Workspace settings** - Konfigurasi server disimpan ke file .vscode/mcp.json yang hanya tersedia di workspace saat ini.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    atau jika Anda memilih streaming HTTP sebagai transport, konfigurasinya sedikit berbeda:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **User settings** - Konfigurasi server ditambahkan ke file *settings.json* global Anda dan tersedia di semua workspace. Konfigurasinya terlihat seperti berikut:

    ![Pengaturan pengguna](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Anda juga perlu menambahkan konfigurasi, sebuah header untuk memastikan autentikasi yang benar ke Azure API Management. Ini menggunakan header bernama **Ocp-Apim-Subscription-Key**.

    - Berikut cara menambahkannya ke pengaturan:

    ![Menambahkan header untuk autentikasi](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), ini akan memunculkan prompt untuk memasukkan nilai API key yang dapat Anda temukan di Azure Portal untuk instance Azure API Management Anda.

   - Untuk menambahkannya ke *mcp.json* sebagai gantinya, Anda bisa menambahkannya seperti ini:

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

### Gunakan mode Agent

Sekarang semuanya sudah siap baik di pengaturan atau di *.vscode/mcp.json*. Mari kita coba.

Seharusnya ada ikon Tools seperti ini, di mana alat yang diekspos dari server Anda terdaftar:

![Alat dari server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Klik ikon tools dan Anda akan melihat daftar alat seperti ini:

    ![Alat](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Masukkan prompt di chat untuk memanggil alat tersebut. Misalnya, jika Anda memilih alat untuk mendapatkan informasi tentang sebuah pesanan, Anda bisa bertanya pada agen tentang pesanan tersebut. Berikut contoh prompt:

    ```text
    get information from order 2
    ```

    Anda sekarang akan melihat ikon tools yang meminta Anda untuk melanjutkan pemanggilan alat. Pilih untuk melanjutkan menjalankan alat, Anda akan melihat output seperti ini:

    ![Hasil dari prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **apa yang Anda lihat di atas tergantung pada alat yang telah Anda siapkan, tapi idenya adalah Anda mendapatkan respons teks seperti di atas**

## Referensi

Berikut cara Anda dapat mempelajari lebih lanjut:

- [Tutorial tentang Azure API Management dan MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Contoh Python: Amankan server MCP jarak jauh menggunakan Azure API Management (eksperimental)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Lab otorisasi klien MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Gunakan ekstensi Azure API Management untuk VS Code untuk mengimpor dan mengelola API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Daftarkan dan temukan server MCP jarak jauh di Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Repo hebat yang menunjukkan banyak kemampuan AI dengan Azure API Management
- [Workshop AI Gateway](https://azure-samples.github.io/AI-Gateway/) Berisi workshop menggunakan Azure Portal, cara yang bagus untuk mulai mengevaluasi kemampuan AI.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk mencapai akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.