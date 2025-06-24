<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "db532b1ec386c9ce38c791653dc3c881",
  "translation_date": "2025-06-21T14:42:00+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/scenario3/README.md",
  "language_code": "id"
}
-->
# Skenario 3: Dokumentasi Dalam Editor dengan MCP Server di VS Code

## Ikhtisar

Dalam skenario ini, Anda akan mempelajari cara menghadirkan Microsoft Learn Docs langsung ke dalam lingkungan Visual Studio Code menggunakan server MCP. Alih-alih terus-menerus berpindah tab browser untuk mencari dokumentasi, Anda dapat mengakses, mencari, dan merujuk dokumen resmi langsung di dalam editor Anda. Pendekatan ini memperlancar alur kerja Anda, menjaga fokus, dan memungkinkan integrasi mulus dengan alat seperti GitHub Copilot.

- Cari dan baca dokumentasi di dalam VS Code tanpa meninggalkan lingkungan pengkodean Anda.
- Referensikan dokumentasi dan sisipkan tautan langsung ke README atau file kursus Anda.
- Gunakan GitHub Copilot dan MCP bersama-sama untuk alur kerja dokumentasi yang mulus dan didukung AI.

## Tujuan Pembelajaran

Pada akhir bab ini, Anda akan memahami cara mengatur dan menggunakan server MCP di dalam VS Code untuk meningkatkan alur kerja dokumentasi dan pengembangan Anda. Anda akan mampu:

- Mengonfigurasi workspace untuk menggunakan server MCP dalam pencarian dokumentasi.
- Mencari dan menyisipkan dokumentasi langsung dari dalam VS Code.
- Menggabungkan kekuatan GitHub Copilot dan MCP untuk alur kerja yang lebih produktif dan didukung AI.

Keterampilan ini akan membantu Anda tetap fokus, meningkatkan kualitas dokumentasi, dan meningkatkan produktivitas sebagai pengembang atau penulis teknis.

## Solusi

Untuk mendapatkan akses dokumentasi dalam editor, Anda akan mengikuti serangkaian langkah yang mengintegrasikan server MCP dengan VS Code dan GitHub Copilot. Solusi ini sangat cocok untuk penulis kursus, penulis dokumentasi, dan pengembang yang ingin tetap fokus di editor saat bekerja dengan dokumen dan Copilot.

- Tambahkan tautan referensi ke README dengan cepat saat menulis dokumentasi kursus atau proyek.
- Gunakan Copilot untuk menghasilkan kode dan MCP untuk langsung menemukan dan mengutip dokumen yang relevan.
- Tetap fokus di editor dan tingkatkan produktivitas.

### Panduan Langkah demi Langkah

Untuk memulai, ikuti langkah-langkah berikut. Untuk setiap langkah, Anda dapat menambahkan tangkapan layar dari folder assets untuk menggambarkan proses secara visual.

1. **Tambahkan konfigurasi MCP:**
   Di root proyek Anda, buat file `.vscode/mcp.json` dan tambahkan konfigurasi berikut:
   ```json
   {
     "servers": {
       "LearnDocsMCP": {
         "url": "https://learn.microsoft.com/api/mcp"
       }
     }
   }
   ```
   Konfigurasi ini memberi tahu VS Code bagaimana cara terhubung ke [`Microsoft Learn Docs MCP server`](https://github.com/MicrosoftDocs/mcp).
   
   ![Langkah 1: Tambahkan mcp.json ke folder .vscode](../../../../../../translated_images/step1-mcp-json.c06a007fccc3edfaf0598a31903c9ec71476d9fd3ae6c1b2b4321fd38688ca4b.id.png)
    
2. **Buka panel GitHub Copilot Chat:**
   Jika Anda belum memasang ekstensi GitHub Copilot, buka tampilan Extensions di VS Code dan pasang ekstensi tersebut. Anda dapat mengunduhnya langsung dari [Visual Studio Code Marketplace](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat). Setelah itu, buka panel Copilot Chat dari sidebar.

   ![Langkah 2: Buka panel Copilot Chat](../../../../../../translated_images/step2-copilot-panel.f1cc86e9b9b8cd1a85e4df4923de8bafee4830541ab255e3c90c09777fed97db.id.png)

3. **Aktifkan mode agen dan verifikasi alat:**
   Di panel Copilot Chat, aktifkan mode agen.

   ![Langkah 3: Aktifkan mode agen dan verifikasi alat](../../../../../../translated_images/step3-agent-mode.cdc32520fd7dd1d149c3f5226763c1d85a06d3c041d4cc983447625bdbeff4d4.id.png)

   Setelah mengaktifkan mode agen, pastikan server MCP tercantum sebagai salah satu alat yang tersedia. Ini memastikan agen Copilot dapat mengakses server dokumentasi untuk mengambil informasi yang relevan.
   
   ![Langkah 3: Verifikasi alat server MCP](../../../../../../translated_images/step3-verify-mcp-tool.76096a6329cbfecd42888780f322370a0d8c8fa003ed3eeb7ccd23f0fc50c1ad.id.png)
4. **Mulai chat baru dan berikan perintah pada agen:**
   Buka chat baru di panel Copilot Chat. Sekarang Anda dapat memberikan perintah kepada agen dengan pertanyaan dokumentasi Anda. Agen akan menggunakan server MCP untuk mengambil dan menampilkan dokumentasi Microsoft Learn yang relevan langsung di editor Anda.

   - *"Saya sedang mencoba membuat rencana belajar untuk topik X. Saya akan mempelajarinya selama 8 minggu, untuk setiap minggu, sarankan konten yang harus saya pelajari."*

   ![Langkah 4: Berikan perintah pada agen di chat](../../../../../../translated_images/step4-prompt-chat.12187bb001605efc5077992b621f0fcd1df12023c5dce0464f8eb8f3d595218f.id.png)

5. **Query Langsung:**

   > Mari ambil query langsung dari bagian [#get-help](https://discord.gg/D6cRhjHWSC) di Azure AI Foundry Discord ([lihat pesan asli](https://discord.com/channels/1113626258182504448/1385498306720829572)):
   
   *"Saya mencari jawaban tentang cara menerapkan solusi multi-agen dengan agen AI yang dikembangkan di Azure AI Foundry. Saya melihat tidak ada metode penerapan langsung, seperti saluran Copilot Studio. Jadi, apa saja cara berbeda untuk melakukan penerapan ini agar pengguna perusahaan bisa berinteraksi dan menyelesaikan pekerjaan?
Ada banyak artikel/blog yang mengatakan kita bisa menggunakan layanan Azure Bot untuk melakukan pekerjaan ini yang bisa bertindak sebagai jembatan antara MS Teams dan Azure AI Foundry Agents, apakah ini akan berhasil jika saya membuat Azure bot yang terhubung ke Orchestrator Agent di Azure AI Foundry melalui Azure function untuk melakukan orkestrasi atau saya perlu membuat Azure function untuk setiap agen AI yang merupakan bagian dari solusi multi-agen untuk melakukan orkestrasi di Bot framework? Saran lain sangat disambut."*

   ![Langkah 5: Query langsung](../../../../../../translated_images/step5-live-queries.49db3e4a50bea27327e3cb18c24d263b7d134930d78e7392f9515a1c00264a7f.id.png)

   Agen akan merespon dengan tautan dokumentasi dan ringkasan yang relevan, yang kemudian dapat Anda sisipkan langsung ke dalam file markdown Anda atau gunakan sebagai referensi dalam kode Anda.
   
### Contoh Query

Berikut beberapa contoh query yang bisa Anda coba. Query ini akan menunjukkan bagaimana server MCP dan Copilot dapat bekerja sama untuk menyediakan dokumentasi dan referensi yang instan dan sesuai konteks tanpa meninggalkan VS Code:

- "Tunjukkan cara menggunakan trigger Azure Functions."
- "Sisipkan tautan ke dokumentasi resmi untuk Azure Key Vault."
- "Apa praktik terbaik untuk mengamankan sumber daya Azure?"
- "Temukan quickstart untuk layanan Azure AI."

Query-query ini akan menunjukkan bagaimana server MCP dan Copilot dapat bekerja sama untuk menyediakan dokumentasi dan referensi yang instan dan sesuai konteks tanpa meninggalkan VS Code.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berupaya untuk memberikan terjemahan yang akurat, harap diperhatikan bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang otoritatif. Untuk informasi yang penting, disarankan menggunakan jasa penerjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau penafsiran yang salah yang timbul dari penggunaan terjemahan ini.