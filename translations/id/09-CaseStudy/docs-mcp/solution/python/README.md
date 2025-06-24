<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:31:31+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "id"
}
-->
# Study Plan Generator dengan Chainlit & Microsoft Learn Docs MCP

## Prasyarat

- Python 3.8 atau versi lebih baru  
- pip (manajer paket Python)  
- Koneksi internet untuk terhubung ke server Microsoft Learn Docs MCP  

## Instalasi

1. Clone repositori ini atau unduh file proyeknya.  
2. Instal dependensi yang dibutuhkan:

   ```bash
   pip install -r requirements.txt
   ```

## Penggunaan

### Skenario 1: Query Sederhana ke Docs MCP  
Client command-line yang terhubung ke server Docs MCP, mengirimkan query, dan menampilkan hasilnya.

1. Jalankan skrip:  
   ```bash
   python scenario1.py
   ```  
2. Masukkan pertanyaan dokumentasi Anda pada prompt.

### Skenario 2: Study Plan Generator (Aplikasi Web Chainlit)  
Antarmuka berbasis web (menggunakan Chainlit) yang memungkinkan pengguna membuat rencana belajar pribadi mingguan untuk topik teknis apa pun.

1. Mulai aplikasi Chainlit:  
   ```bash
   chainlit run scenario2.py
   ```  
2. Buka URL lokal yang muncul di terminal Anda (misalnya, http://localhost:8000) di browser.  
3. Di jendela chat, masukkan topik belajar dan jumlah minggu yang ingin Anda pelajari (misalnya, "AI-900 certification, 8 weeks").  
4. Aplikasi akan merespon dengan rencana belajar mingguan, termasuk tautan ke dokumentasi Microsoft Learn yang relevan.

**Variabel Lingkungan yang Diperlukan:**  

Untuk menggunakan Skenario 2 (aplikasi web Chainlit dengan Azure OpenAI), Anda harus mengatur variabel lingkungan berikut di direktori `.env` file in the `python`:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Isi nilai-nilai tersebut dengan detail resource Azure OpenAI Anda sebelum menjalankan aplikasi.

> **Tip:** Anda bisa dengan mudah menerapkan model Anda sendiri menggunakan [Azure AI Foundry](https://ai.azure.com/).

### Skenario 3: Docs Dalam Editor dengan MCP Server di VS Code  

Daripada berganti tab browser untuk mencari dokumentasi, Anda dapat membawa Microsoft Learn Docs langsung ke VS Code menggunakan server MCP. Ini memungkinkan Anda untuk:  
- Mencari dan membaca dokumentasi di dalam VS Code tanpa meninggalkan lingkungan coding Anda.  
- Mereferensikan dokumentasi dan memasukkan tautan langsung ke README atau file kursus Anda.  
- Menggunakan GitHub Copilot dan MCP secara bersamaan untuk alur kerja dokumentasi berbasis AI yang mulus.

**Contoh Kasus Penggunaan:**  
- Menambahkan tautan referensi ke README dengan cepat saat menulis dokumentasi kursus atau proyek.  
- Menggunakan Copilot untuk membuat kode dan MCP untuk langsung menemukan serta mengutip dokumentasi yang relevan.  
- Tetap fokus di editor dan tingkatkan produktivitas.

> [!IMPORTANT]  
> Pastikan Anda memiliki file [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

## Why Chainlit for Scenario 2?

Chainlit is a modern open-source framework for building conversational web applications. It makes it easy to create chat-based user interfaces that connect to backend services like the Microsoft Learn Docs MCP server. This project uses Chainlit to provide a simple, interactive way to generate personalized study plans in real time. By leveraging Chainlit, you can quickly build and deploy chat-based tools that enhance productivity and learning.

## What This Does

This app allows users to create a personalized study plan by simply entering a topic and a duration. The app parses your input, queries the Microsoft Learn Docs MCP server for relevant content, and organizes the results into a structured, week-by-week plan. Each week’s recommendations are displayed in the chat, making it easy to follow and track your progress. The integration ensures you always get the latest, most relevant learning resources.

## Sample Queries

Try these queries in the chat window to see how the app responds:

- `AI-900 certification, 8 weeks`
- `Learn Azure Functions, 4 weeks`
- `Azure DevOps, 6 weeks`
- `Data engineering on Azure, 10 weeks`
- `Microsoft security fundamentals, 5 weeks`
- `Power Platform, 7 weeks`
- `Azure AI services, 12 weeks`
- `Cloud architecture, 9 weeks`] yang valid.

Contoh-contoh ini menunjukkan fleksibilitas aplikasi untuk berbagai tujuan belajar dan jangka waktu.

## Referensi

- [Chainlit Documentation](https://docs.chainlit.io/)  
- [MCP Documentation](https://github.com/MicrosoftDocs/mcp)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Meskipun kami berusaha untuk akurasi, harap diketahui bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang sahih. Untuk informasi penting, disarankan menggunakan terjemahan profesional oleh manusia. Kami tidak bertanggung jawab atas kesalahpahaman atau salah tafsir yang timbul dari penggunaan terjemahan ini.