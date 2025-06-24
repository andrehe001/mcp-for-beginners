<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:29:50+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "tr"
}
-->
# Chainlit & Microsoft Learn Docs MCP ile Çalışma Planı Oluşturucu

## Gereksinimler

- Python 3.8 veya üzeri
- pip (Python paket yöneticisi)
- Microsoft Learn Docs MCP sunucusuna bağlanmak için internet erişimi

## Kurulum

1. Bu depoyu klonlayın veya proje dosyalarını indirin.
2. Gerekli bağımlılıkları yükleyin:

   ```bash
   pip install -r requirements.txt
   ```

## Kullanım

### Senaryo 1: Docs MCP’ye Basit Sorgu
Docs MCP sunucusuna bağlanan, sorgu gönderen ve sonucu yazdıran bir komut satırı istemcisi.

1. Scripti çalıştırın:
   ```bash
   python scenario1.py
   ```
2. İstekte dokümantasyon sorunuz yazın.

### Senaryo 2: Çalışma Planı Oluşturucu (Chainlit Web Uygulaması)
Kullanıcıların herhangi bir teknik konu için kişiselleştirilmiş, haftalık çalışma planı oluşturmasını sağlayan web tabanlı bir arayüz (Chainlit kullanılarak).

1. Chainlit uygulamasını başlatın:
   ```bash
   chainlit run scenario2.py
   ```
2. Terminalde verilen yerel URL’yi (örneğin, http://localhost:8000) tarayıcınızda açın.
3. Sohbet penceresine çalışma konunuzu ve çalışmak istediğiniz hafta sayısını girin (örneğin, "AI-900 sertifikası, 8 hafta").
4. Uygulama, ilgili Microsoft Learn dokümantasyon bağlantılarıyla birlikte haftalık çalışma planını size sunacaktır.

**Gerekli Ortam Değişkenleri:**

Senaryo 2’yi (Azure OpenAI ile Chainlit web uygulaması) kullanmak için `.env` file in the `python` dizininde aşağıdaki ortam değişkenlerini ayarlamalısınız:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

Uygulamayı çalıştırmadan önce bu değerleri Azure OpenAI kaynak bilgilerinizle doldurun.

> **İpucu:** Kendi modellerinizi kolayca [Azure AI Foundry](https://ai.azure.com/) kullanarak dağıtabilirsiniz.

### Senaryo 3: VS Code’da MCP Sunucusu ile Editör İçi Dokümantasyon

Tarayıcı sekmeleri arasında geçiş yapmadan Microsoft Learn Docs’u doğrudan VS Code içinde kullanabilirsiniz. Bu sayede:
- Kodlama ortamınızı terk etmeden VS Code içinde doküman arayıp okuyabilirsiniz.
- Dokümantasyona referans verip, README veya ders dosyalarınıza doğrudan bağlantılar ekleyebilirsiniz.
- GitHub Copilot ile MCP’yi birlikte kullanarak kesintisiz, yapay zekâ destekli bir dokümantasyon iş akışı sağlayabilirsiniz.

**Örnek Kullanım Senaryoları:**
- Bir kurs veya proje dokümantasyonu yazarken README’ye hızlıca referans bağlantıları eklemek.
- Copilot ile kod üretirken, MCP ile ilgili dokümanları anında bulup referans göstermek.
- Editörünüzde odaklanarak verimliliği artırmak.

> [!IMPORTANT]
> Geçerli bir [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

## Why Chainlit for Scenario 2?

Chainlit is a modern open-source framework for building conversational web applications. It makes it easy to create chat-based user interfaces that connect to backend services like the Microsoft Learn Docs MCP server. This project uses Chainlit to provide a simple, interactive way to generate personalized study plans in real time. By leveraging Chainlit, you can quickly build and deploy chat-based tools that enhance productivity and learning.

## What This Does

This app allows users to create a personalized study plan by simply entering a topic and a duration. The app parses your input, queries the Microsoft Learn Docs MCP server for relevant content, and organizes the results into a structured, week-by-week plan. Each week’s recommendations are displayed in the chat, making it easy to follow and track your progress. The integration ensures you always get the latest, most relevant learning resources.

## Sample Queries

Try these queries in the chat window to see how the app responds:

- `AI-900 sertifikası, 8 hafta`
- `Learn Azure Functions, 4 hafta`
- `Azure DevOps, 6 hafta`
- `Azure üzerinde Veri Mühendisliği, 10 hafta`
- `Microsoft güvenlik temelleri, 5 hafta`
- `Power Platform, 7 hafta`
- `Azure AI servisleri, 12 hafta`
- `Bulut mimarisi, 9 hafta`

Bu örnekler, uygulamanın farklı öğrenme hedefleri ve süreleri için esnekliğini göstermektedir.

## Referanslar

- [Chainlit Dokümantasyonu](https://docs.chainlit.io/)
- [MCP Dokümantasyonu](https://github.com/MicrosoftDocs/mcp)

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.