<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:31:39+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "ms"
}
-->
# Penjana Pelan Belajar dengan Chainlit & Microsoft Learn Docs MCP

## Prasyarat

- Python 3.8 atau lebih tinggi  
- pip (pengurus pakej Python)  
- Akses internet untuk menyambung ke pelayan Microsoft Learn Docs MCP  

## Pemasangan

1. Klon repositori ini atau muat turun fail projek.  
2. Pasang kebergantungan yang diperlukan:  

   ```bash
   pip install -r requirements.txt
   ```  

## Penggunaan

### Senario 1: Pertanyaan Mudah ke Docs MCP  
Klien baris perintah yang menyambung ke pelayan Docs MCP, menghantar pertanyaan, dan memaparkan hasilnya.  

1. Jalankan skrip:  
   ```bash
   python scenario1.py
   ```  
2. Masukkan soalan dokumentasi anda pada arahan yang diberikan.  

### Senario 2: Penjana Pelan Belajar (Aplikasi Web Chainlit)  
Antara muka berasaskan web (menggunakan Chainlit) yang membolehkan pengguna menghasilkan pelan belajar peribadi, minggu demi minggu, untuk sebarang topik teknikal.  

1. Mulakan aplikasi Chainlit:  
   ```bash
   chainlit run scenario2.py
   ```  
2. Buka URL tempatan yang dipaparkan dalam terminal anda (contoh: http://localhost:8000) di pelayar anda.  
3. Dalam tetingkap chat, masukkan topik belajar dan bilangan minggu yang anda ingin belajar (contoh: "AI-900 certification, 8 weeks").  
4. Aplikasi akan memberi pelan belajar minggu demi minggu, termasuk pautan ke dokumentasi Microsoft Learn yang berkaitan.  

**Pembolehubah Persekitaran Diperlukan:**  

Untuk menggunakan Senario 2 (aplikasi web Chainlit dengan Azure OpenAI), anda mesti tetapkan pembolehubah persekitaran berikut dalam direktori `.env` file in the `python`:  

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```  

Isikan nilai ini dengan maklumat sumber Azure OpenAI anda sebelum menjalankan aplikasi.  

> **Tip:** Anda boleh dengan mudah menghos model anda sendiri menggunakan [Azure AI Foundry](https://ai.azure.com/).  

### Senario 3: Dokumentasi Dalam Editor dengan Pelayan MCP dalam VS Code  

Daripada menukar tab pelayar untuk mencari dokumentasi, anda boleh membawa Microsoft Learn Docs terus ke dalam VS Code menggunakan pelayan MCP. Ini membolehkan anda:  
- Mencari dan membaca dokumen dalam VS Code tanpa meninggalkan persekitaran pengekodan anda.  
- Merujuk dokumentasi dan menyisipkan pautan terus ke dalam fail README atau kursus anda.  
- Menggunakan GitHub Copilot dan MCP bersama-sama untuk aliran kerja dokumentasi berkuasa AI yang lancar.  

**Contoh Kegunaan:**  
- Tambah pautan rujukan dengan cepat ke README semasa menulis dokumentasi kursus atau projek.  
- Gunakan Copilot untuk menjana kod dan MCP untuk mencari serta memetik dokumen yang relevan dengan segera.  
- Kekal fokus dalam editor dan tingkatkan produktiviti.  

> [!IMPORTANT]  
> Pastikan anda mempunyai fail [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

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
- `Cloud architecture, 9 weeks` yang sah.  

Contoh-contoh ini menunjukkan fleksibiliti aplikasi untuk pelbagai matlamat pembelajaran dan tempoh masa.  

## Rujukan

- [Dokumentasi Chainlit](https://docs.chainlit.io/)  
- [Dokumentasi MCP](https://github.com/MicrosoftDocs/mcp)

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan AI [Co-op Translator](https://github.com/Azure/co-op-translator). Walaupun kami berusaha untuk ketepatan, sila ambil maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang sahih. Untuk maklumat penting, terjemahan profesional oleh manusia adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.