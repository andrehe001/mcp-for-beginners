<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "36de9fae488d6de554d969fe8e0801a8",
  "translation_date": "2025-06-20T19:23:05+00:00",
  "source_file": "09-CaseStudy/apimsample.md",
  "language_code": "ms"
}
-->
# Kajian Kes: Dedahkan REST API dalam Pengurusan API sebagai pelayan MCP

Azure API Management ialah perkhidmatan yang menyediakan Gateway di atas Titik Akhir API anda. Cara kerjanya ialah Azure API Management bertindak seperti proksi di hadapan API anda dan boleh memutuskan apa yang perlu dilakukan dengan permintaan yang masuk.

Dengan menggunakannya, anda menambah pelbagai ciri seperti:

- **Keselamatan**, anda boleh menggunakan segala-galanya daripada kekunci API, JWT hingga identiti terurus.
- **Had kadar**, ciri hebat ialah keupayaan untuk menentukan berapa banyak panggilan yang dibenarkan dalam satu unit masa tertentu. Ini membantu memastikan semua pengguna mendapat pengalaman yang baik dan juga perkhidmatan anda tidak dibebani dengan permintaan.
- **Skala & Pengimbangan beban**. Anda boleh menyediakan beberapa titik akhir untuk mengimbangkan beban dan juga boleh menentukan cara untuk "mengimbangkan beban".
- **Ciri AI seperti caching semantik**, had token dan pemantauan token dan banyak lagi. Ini adalah ciri hebat yang meningkatkan kepekaan serta membantu anda mengawal perbelanjaan token anda. [Baca lebih lanjut di sini](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Kenapa MCP + Azure API Management?

Model Context Protocol dengan pantas menjadi piawaian untuk aplikasi AI agen dan cara mendedahkan alat serta data secara konsisten. Azure API Management adalah pilihan semula jadi apabila anda perlu "mengurus" API. Pelayan MCP sering diintegrasikan dengan API lain untuk menyelesaikan permintaan kepada alat sebagai contoh. Oleh itu, menggabungkan Azure API Management dan MCP adalah sangat logik.

## Gambaran Keseluruhan

Dalam kes penggunaan khusus ini, kita akan belajar untuk mendedahkan titik akhir API sebagai Pelayan MCP. Dengan melakukan ini, kita boleh dengan mudah menjadikan titik akhir ini sebahagian daripada aplikasi agen sambil juga memanfaatkan ciri daripada Azure API Management.

## Ciri Utama

- Anda memilih kaedah titik akhir yang ingin didedahkan sebagai alat.
- Ciri tambahan yang anda peroleh bergantung pada apa yang anda konfigurasikan dalam bahagian polisi untuk API anda. Tetapi di sini kami akan tunjukkan bagaimana anda boleh menambah had kadar.

## Langkah awal: import API

Jika anda sudah mempunyai API dalam Azure API Management, bagus, anda boleh langkau langkah ini. Jika tidak, lihat pautan ini, [mengimport API ke Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Dedahkan API sebagai Pelayan MCP

Untuk mendedahkan titik akhir API, ikuti langkah berikut:

1. Pergi ke Azure Portal dan alamat berikut <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
Pergi ke instans Pengurusan API anda.

1. Dalam menu kiri, pilih APIs > MCP Servers > + Create new MCP Server.

1. Dalam API, pilih REST API untuk didedahkan sebagai pelayan MCP.

1. Pilih satu atau lebih Operasi API untuk didedahkan sebagai alat. Anda boleh pilih semua operasi atau hanya operasi tertentu.

    ![Pilih kaedah untuk didedahkan](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Pilih **Create**.

1. Pergi ke pilihan menu **APIs** dan **MCP Servers**, anda akan melihat seperti berikut:

    ![Lihat Pelayan MCP dalam panel utama](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    Pelayan MCP telah dibuat dan operasi API didedahkan sebagai alat. Pelayan MCP disenaraikan dalam panel MCP Servers. Lajur URL menunjukkan titik akhir pelayan MCP yang boleh anda panggil untuk ujian atau dalam aplikasi klien.

## Pilihan: Konfigurasikan polisi

Azure API Management mempunyai konsep teras polisi di mana anda menetapkan peraturan berbeza untuk titik akhir anda seperti contohnya had kadar atau caching semantik. Polisi ini ditulis dalam format XML.

Berikut cara anda boleh menyediakan polisi untuk had kadar Pelayan MCP anda:

1. Dalam portal, di bawah APIs, pilih **MCP Servers**.

1. Pilih pelayan MCP yang anda buat.

1. Dalam menu kiri, di bawah MCP, pilih **Policies**.

1. Dalam penyunting polisi, tambah atau sunting polisi yang ingin anda gunakan pada alat pelayan MCP. Polisi ditakrifkan dalam format XML. Sebagai contoh, anda boleh tambah polisi untuk mengehadkan panggilan ke alat pelayan MCP (dalam contoh ini, 5 panggilan setiap 30 saat bagi setiap alamat IP klien). Berikut XML yang akan menyebabkan had kadar:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Berikut adalah imej penyunting polisi:

    ![Penyunting polisi](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Cuba ia

Mari pastikan Pelayan MCP kita berfungsi seperti yang diingini.

Untuk ini, kita akan menggunakan Visual Studio Code dan GitHub Copilot serta mod Agennya. Kita akan tambah pelayan MCP ke *mcp.json*. Dengan berbuat demikian, Visual Studio Code akan bertindak sebagai klien dengan keupayaan agen dan pengguna akhir boleh menaip arahan dan berinteraksi dengan pelayan tersebut.

Mari lihat cara menambah pelayan MCP dalam Visual Studio Code:

1. Gunakan perintah MCP: **Add Server dari Command Palette**.

1. Apabila diminta, pilih jenis pelayan: **HTTP (HTTP atau Server Sent Events)**.

1. Masukkan URL pelayan MCP dalam Pengurusan API. Contoh: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (untuk titik akhir SSE) atau **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (untuk titik akhir MCP), perhatikan perbezaan antara pengangkutan adalah `/sse` or `/mcp`.

1. Masukkan ID pelayan pilihan anda. Ini bukan nilai penting tetapi membantu anda mengingati instans pelayan ini.

1. Pilih sama ada untuk menyimpan konfigurasi ke tetapan ruang kerja atau tetapan pengguna.

  - **Tetapan ruang kerja** - Konfigurasi pelayan disimpan ke fail .vscode/mcp.json yang hanya tersedia dalam ruang kerja semasa.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    atau jika anda memilih HTTP streaming sebagai pengangkutan ia sedikit berbeza:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **Tetapan pengguna** - Konfigurasi pelayan ditambah ke fail *settings.json* global anda dan tersedia di semua ruang kerja. Konfigurasi kelihatan seperti berikut:

    ![Tetapan pengguna](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Anda juga perlu menambah konfigurasi, satu header untuk memastikan ia mengesahkan dengan betul ke arah Azure API Management. Ia menggunakan header yang dipanggil **Ocp-Apim-Subscription-Key**. 

    - Berikut cara anda boleh menambahkannya ke tetapan:

    ![Menambah header untuk pengesahan](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), ini akan menyebabkan arahan muncul untuk meminta nilai kekunci API yang boleh anda dapati dalam Azure Portal untuk instans Azure API Management anda.

   - Untuk menambahkannya ke *mcp.json* pula, anda boleh tambah seperti berikut:

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

### Gunakan mod Agen

Kini semuanya sudah disediakan sama ada dalam tetapan atau dalam *.vscode/mcp.json*. Mari cuba.

Harus ada ikon Alat seperti ini, di mana alat yang didedahkan dari pelayan anda disenaraikan:

![Alat dari pelayan](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Klik ikon alat dan anda akan melihat senarai alat seperti berikut:

    ![Alat](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Masukkan arahan dalam chat untuk menggunakan alat tersebut. Contohnya, jika anda memilih alat untuk mendapatkan maklumat tentang pesanan, anda boleh bertanya kepada agen mengenai pesanan itu. Berikut contoh arahan:

    ```text
    get information from order 2
    ```

    Anda kini akan dipaparkan ikon alat yang meminta anda untuk meneruskan memanggil alat tersebut. Pilih untuk terus menjalankan alat, anda akan melihat output seperti berikut:

    ![Keputusan dari arahan](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **apa yang anda lihat di atas bergantung pada alat yang telah anda sediakan, tetapi idenya adalah anda mendapat respons berbentuk teks seperti di atas**

## Rujukan

Berikut cara anda boleh belajar lebih lanjut:

- [Tutorial mengenai Azure API Management dan MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Contoh Python: Amankan pelayan MCP jauh menggunakan Azure API Management (eksperimen)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Makmal kebenaran klien MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Gunakan sambungan Azure API Management untuk VS Code bagi mengimport dan mengurus API](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Daftar dan temui pelayan MCP jauh dalam Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Repositori hebat yang menunjukkan banyak keupayaan AI dengan Azure API Management
- [Bengkel AI Gateway](https://azure-samples.github.io/AI-Gateway/) Mengandungi bengkel menggunakan Azure Portal, yang merupakan cara terbaik untuk mula menilai keupayaan AI.

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.