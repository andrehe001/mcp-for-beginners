<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "db532b1ec386c9ce38c791653dc3c881",
  "translation_date": "2025-06-21T14:42:12+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/scenario3/README.md",
  "language_code": "ms"
}
-->
# Senario 3: Dokumen Dalam Editor dengan MCP Server dalam VS Code

## Gambaran Keseluruhan

Dalam senario ini, anda akan belajar cara membawa Microsoft Learn Docs terus ke dalam persekitaran Visual Studio Code anda menggunakan MCP server. Daripada sentiasa menukar tab pelayar untuk mencari dokumentasi, anda boleh mengakses, mencari, dan merujuk dokumen rasmi terus di dalam editor anda. Pendekatan ini mempermudah aliran kerja anda, mengekalkan fokus, dan membolehkan integrasi lancar dengan alat seperti GitHub Copilot.

- Cari dan baca dokumen dalam VS Code tanpa meninggalkan persekitaran pengkodan anda.
- Rujuk dokumentasi dan masukkan pautan terus ke dalam fail README atau kursus anda.
- Gunakan GitHub Copilot dan MCP bersama-sama untuk aliran kerja dokumentasi berkuasa AI yang lancar.

## Objektif Pembelajaran

Menjelang akhir bab ini, anda akan memahami cara menyediakan dan menggunakan MCP server dalam VS Code untuk meningkatkan aliran kerja dokumentasi dan pembangunan anda. Anda akan dapat:

- Konfigurasikan ruang kerja anda untuk menggunakan MCP server bagi carian dokumentasi.
- Cari dan masukkan dokumentasi terus dari dalam VS Code.
- Gabungkan kuasa GitHub Copilot dan MCP untuk aliran kerja yang lebih produktif dan dipertingkatkan AI.

Kemahiran ini akan membantu anda kekal fokus, meningkatkan kualiti dokumentasi, dan meningkatkan produktiviti anda sebagai pembangun atau penulis teknikal.

## Penyelesaian

Untuk mencapai akses dokumentasi dalam editor, anda akan mengikuti beberapa langkah yang mengintegrasikan MCP server dengan VS Code dan GitHub Copilot. Penyelesaian ini sesuai untuk pengarang kursus, penulis dokumentasi, dan pembangun yang mahu mengekalkan fokus dalam editor sambil bekerja dengan dokumen dan Copilot.

- Tambah pautan rujukan dengan cepat ke README semasa menulis dokumentasi kursus atau projek.
- Gunakan Copilot untuk menjana kod dan MCP untuk mencari serta memetik dokumen yang relevan dengan segera.
- Kekal fokus dalam editor anda dan tingkatkan produktiviti.

### Panduan Langkah demi Langkah

Untuk memulakan, ikut langkah-langkah berikut. Untuk setiap langkah, anda boleh menambah tangkapan skrin dari folder aset untuk menggambarkan proses secara visual.

1. **Tambah konfigurasi MCP:**
   Di akar projek anda, cipta fail `.vscode/mcp.json` dan tambah konfigurasi berikut:
   ```json
   {
     "servers": {
       "LearnDocsMCP": {
         "url": "https://learn.microsoft.com/api/mcp"
       }
     }
   }
   ```
   Konfigurasi ini memberitahu VS Code bagaimana untuk berhubung dengan [`Microsoft Learn Docs MCP server`](https://github.com/MicrosoftDocs/mcp).
   
   ![Langkah 1: Tambah mcp.json ke folder .vscode](../../../../../../translated_images/step1-mcp-json.c06a007fccc3edfaf0598a31903c9ec71476d9fd3ae6c1b2b4321fd38688ca4b.ms.png)
    
2. **Buka panel GitHub Copilot Chat:**
   Jika anda belum memasang sambungan GitHub Copilot, pergi ke paparan Extensions dalam VS Code dan pasang ia. Anda boleh muat turun terus dari [Visual Studio Code Marketplace](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat). Kemudian, buka panel Copilot Chat dari bar sisi.

   ![Langkah 2: Buka panel Copilot Chat](../../../../../../translated_images/step2-copilot-panel.f1cc86e9b9b8cd1a85e4df4923de8bafee4830541ab255e3c90c09777fed97db.ms.png)

3. **Aktifkan mod agen dan sahkan alat:**
   Dalam panel Copilot Chat, aktifkan mod agen.

   ![Langkah 3: Aktifkan mod agen dan sahkan alat](../../../../../../translated_images/step3-agent-mode.cdc32520fd7dd1d149c3f5226763c1d85a06d3c041d4cc983447625bdbeff4d4.ms.png)

   Selepas mengaktifkan mod agen, sahkan bahawa MCP server disenaraikan sebagai salah satu alat yang tersedia. Ini memastikan agen Copilot boleh mengakses server dokumentasi untuk mendapatkan maklumat yang relevan.
   
   ![Langkah 3: Sahkan alat MCP server](../../../../../../translated_images/step3-verify-mcp-tool.76096a6329cbfecd42888780f322370a0d8c8fa003ed3eeb7ccd23f0fc50c1ad.ms.png)
4. **Mulakan sembang baru dan beri arahan kepada agen:**
   Buka sembang baru dalam panel Copilot Chat. Anda kini boleh memberi arahan kepada agen dengan soalan dokumentasi anda. Agen akan menggunakan MCP server untuk mendapatkan dan memaparkan dokumentasi Microsoft Learn yang relevan terus dalam editor anda.

   - *"Saya sedang cuba menulis pelan pembelajaran untuk topik X. Saya akan belajar selama 8 minggu, untuk setiap minggu, cadangkan kandungan yang patut saya ambil."*

   ![Langkah 4: Beri arahan kepada agen dalam sembang](../../../../../../translated_images/step4-prompt-chat.12187bb001605efc5077992b621f0fcd1df12023c5dce0464f8eb8f3d595218f.ms.png)

5. **Pertanyaan Langsung:**

   > Mari ambil pertanyaan langsung dari bahagian [#get-help](https://discord.gg/D6cRhjHWSC) dalam Discord Azure AI Foundry ([lihat mesej asal](https://discord.com/channels/1113626258182504448/1385498306720829572)):
   
   *"Saya mencari jawapan tentang cara untuk melaksanakan penyelesaian multi-agen dengan agen AI yang dibangunkan di Azure AI Foundry. Saya perhatikan tiada kaedah pelaksanaan langsung, seperti saluran Copilot Studio. Jadi, apakah cara berbeza untuk melaksanakan ini supaya pengguna perusahaan dapat berinteraksi dan menyelesaikan tugasan?
Terdapat banyak artikel/blog yang mengatakan kita boleh gunakan perkhidmatan Azure Bot untuk tugasan ini yang boleh bertindak sebagai jambatan antara MS Teams dan Agen Azure AI Foundry, adakah ini akan berfungsi jika saya sediakan Azure bot yang bersambung dengan Orchestrator Agent di Azure AI Foundry melalui fungsi Azure untuk melakukan orkestrasi atau saya perlu cipta fungsi Azure untuk setiap agen AI yang merupakan sebahagian daripada penyelesaian multi-agen untuk melakukan orkestrasi pada rangka kerja Bot? Sebarang cadangan lain amat dialu-alukan."*

   ![Langkah 5: Pertanyaan langsung](../../../../../../translated_images/step5-live-queries.49db3e4a50bea27327e3cb18c24d263b7d134930d78e7392f9515a1c00264a7f.ms.png)

   Agen akan membalas dengan pautan dokumentasi dan ringkasan yang relevan, yang kemudian anda boleh masukkan terus ke dalam fail markdown anda atau gunakan sebagai rujukan dalam kod anda.
   
### Contoh Pertanyaan

Berikut adalah beberapa contoh pertanyaan yang boleh anda cuba. Pertanyaan ini akan menunjukkan bagaimana MCP server dan Copilot boleh bekerjasama untuk menyediakan dokumentasi dan rujukan yang segera dan berasaskan konteks tanpa meninggalkan VS Code:

- "Tunjukkan cara menggunakan pencetus Azure Functions."
- "Masukkan pautan ke dokumentasi rasmi untuk Azure Key Vault."
- "Apakah amalan terbaik untuk mengamankan sumber Azure?"
- "Cari panduan permulaan pantas untuk perkhidmatan Azure AI."

Pertanyaan ini akan menunjukkan bagaimana MCP server dan Copilot boleh bekerjasama untuk menyediakan dokumentasi dan rujukan yang segera dan berasaskan konteks tanpa meninggalkan VS Code.

---

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya hendaklah dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.