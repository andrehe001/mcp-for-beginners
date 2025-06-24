<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6940b1e931e51821b219aa9dcfe8c4ee",
  "translation_date": "2025-06-23T11:08:09+00:00",
  "source_file": "09-CaseStudy/README.md",
  "language_code": "tr"
}
-->
# MCP Uygulamada: Gerçek Dünya Vaka Çalışmaları

Model Context Protocol (MCP), yapay zeka uygulamalarının veri, araçlar ve hizmetlerle etkileşim şeklini dönüştürüyor. Bu bölüm, MCP’nin çeşitli kurumsal senaryolarda pratik uygulamalarını gösteren gerçek dünya vaka çalışmalarını sunar.

## Genel Bakış

Bu bölüm, MCP uygulamalarına dair somut örnekler sunarak, kuruluşların bu protokolü karmaşık iş problemlerini çözmek için nasıl kullandığını vurgular. Bu vaka çalışmalarını inceleyerek, MCP’nin gerçek dünya senaryolarındaki çok yönlülüğü, ölçeklenebilirliği ve pratik faydaları hakkında fikir sahibi olacaksınız.

## Temel Öğrenme Hedefleri

Bu vaka çalışmalarını keşfederek:

- MCP’nin belirli iş problemlerini çözmek için nasıl uygulanabileceğini anlayacaksınız
- Farklı entegrasyon desenleri ve mimari yaklaşımlar hakkında bilgi edineceksiniz
- Kurumsal ortamlarda MCP uygularken en iyi uygulamaları tanıyacaksınız
- Gerçek dünya uygulamalarında karşılaşılan zorluklar ve çözümler hakkında içgörü kazanacaksınız
- Kendi projelerinizde benzer desenleri uygulama fırsatlarını belirleyeceksiniz

## Öne Çıkan Vaka Çalışmaları

### 1. [Azure AI Seyahat Acenteleri – Referans Uygulama](./travelagentsample.md)

Bu vaka çalışması, Microsoft’un MCP, Azure OpenAI ve Azure AI Search kullanarak çoklu ajanlı, yapay zeka destekli seyahat planlama uygulaması geliştirmeyi gösteren kapsamlı referans çözümünü inceliyor. Proje şunları sunuyor:

- MCP üzerinden çoklu ajan orkestrasyonu
- Azure AI Search ile kurumsal veri entegrasyonu
- Azure servisleri kullanılarak güvenli ve ölçeklenebilir mimari
- Yeniden kullanılabilir MCP bileşenleriyle genişletilebilir araçlar
- Azure OpenAI destekli konuşma tabanlı kullanıcı deneyimi

Mimari ve uygulama detayları, MCP’nin koordinasyon katmanı olarak kullanıldığı karmaşık çoklu ajan sistemleri inşa etme konusunda değerli bilgiler sağlıyor.

### 2. [YouTube Verilerinden Azure DevOps Öğelerini Güncelleme](./UpdateADOItemsFromYT.md)

Bu vaka çalışması, iş akışı süreçlerini otomatikleştirmek için MCP’nin pratik bir uygulamasını gösteriyor. MCP araçlarının nasıl kullanılabileceğini anlatıyor:

- Çevrimiçi platformlardan (YouTube) veri çekme
- Azure DevOps sistemlerindeki iş öğelerini güncelleme
- Tekrarlanabilir otomasyon iş akışları oluşturma
- Farklı sistemler arasında veri entegrasyonu sağlama

Bu örnek, nispeten basit MCP uygulamalarının rutin görevleri otomatikleştirerek ve sistemler arası veri tutarlılığını artırarak önemli verimlilik kazançları sağlayabileceğini gösteriyor.

### 3. [MCP ile Gerçek Zamanlı Dokümantasyon Erişimi](./docs-mcp/README.md)

Bu vaka çalışması, Python konsol istemcisini bir Model Context Protocol (MCP) sunucusuna bağlayarak gerçek zamanlı, bağlam farkındalıklı Microsoft dokümantasyonunu nasıl alıp kaydedebileceğinizi adım adım anlatıyor. Şunları öğreneceksiniz:

- Python istemci ve resmi MCP SDK kullanarak MCP sunucusuna bağlanma
- Verimli, gerçek zamanlı veri alımı için streaming HTTP istemcileri kullanma
- Sunucudaki dokümantasyon araçlarını çağırma ve yanıtları doğrudan konsola kaydetme
- Güncel Microsoft dokümantasyonunu terminalden çıkmadan iş akışınıza entegre etme

Bölüm, uygulamalı bir görev, minimal çalışan kod örneği ve daha derin öğrenme için ek kaynaklar içerir. MCP’nin konsol tabanlı ortamlarda dokümantasyon erişimini ve geliştirici verimliliğini nasıl dönüştürebileceğini anlamak için bağlantılı bölüme ve koda göz atabilirsiniz.

### 4. [MCP ile Etkileşimli Çalışma Planı Üretici Web Uygulaması](./docs-mcp/README.md)

Bu vaka çalışması, Chainlit ve Model Context Protocol (MCP) kullanarak herhangi bir konu için kişiselleştirilmiş çalışma planları oluşturabilen etkileşimli bir web uygulamasının nasıl geliştirileceğini gösteriyor. Kullanıcılar bir konu (örneğin "AI-900 sertifikası") ve çalışma süresi (örneğin 8 hafta) belirtebilir ve uygulama haftalık önerilen içerik dökümünü sağlar. Chainlit, sohbet tabanlı bir arayüz sunarak deneyimi etkileşimli ve uyarlanabilir hale getirir.

- Chainlit destekli konuşma tabanlı web uygulaması
- Konu ve süre için kullanıcı tarafından yönlendirilen istemler
- MCP kullanarak haftalık içerik önerileri
- Sohbet arayüzünde gerçek zamanlı, uyarlanabilir yanıtlar

Proje, konuşma tabanlı yapay zeka ile MCP’nin modern web ortamlarında dinamik, kullanıcı odaklı eğitim araçları yaratmak için nasıl birleştirilebileceğini gösteriyor.

### 5. [VS Code İçinde MCP Sunucusu ile Düzenleyici İçi Dokümantasyon](./docs-mcp/README.md)

Bu vaka çalışması, MCP sunucusu kullanarak Microsoft Learn Dokümanlarını doğrudan VS Code ortamınıza getirmenin yollarını gösteriyor—tarayıcı sekmeleri arasında geçiş yapmaya son! Şunları göreceksiniz:

- MCP paneli veya komut paleti kullanarak VS Code içinde anında doküman arama ve okuma
- Dokümantasyon referanslarını README veya kurs markdown dosyalarınıza doğrudan bağlantı olarak ekleme
- GitHub Copilot ve MCP’yi birlikte kullanarak kesintisiz, yapay zeka destekli dokümantasyon ve kod iş akışları sağlama
- Gerçek zamanlı geri bildirim ve Microsoft kaynaklı doğrulukla dokümantasyonunuzu doğrulama ve geliştirme
- Sürekli dokümantasyon doğrulaması için MCP’nin GitHub iş akışlarına entegrasyonu

Uygulama şunları içerir:
- Kolay kurulum için örnek `.vscode/mcp.json` yapılandırması
- Düzenleyici içi deneyimin ekran görüntüleriyle anlatımı
- Maksimum verimlilik için Copilot ve MCP’nin birlikte kullanımına dair ipuçları

Bu senaryo, kurs yazarları, dokümantasyon yazarları ve doküman, Copilot ve doğrulama araçlarıyla çalışırken editörlerinde odaklanmak isteyen geliştiriciler için idealdir; tümü MCP tarafından desteklenir.

### 6. [APIM MCP Sunucusu Oluşturma](./apimsample.md)

Bu vaka çalışması, Azure API Management (APIM) kullanarak MCP sunucusunun nasıl oluşturulacağına dair adım adım rehber sunar. İçerik:

- Azure API Management içinde MCP sunucusu kurulumu
- API işlemlerinin MCP araçları olarak açılması
- Hız sınırlama ve güvenlik politikalarının yapılandırılması
- MCP sunucusunun Visual Studio Code ve GitHub Copilot ile test edilmesi

Bu örnek, Azure’un sunduğu imkanları kullanarak sağlam bir MCP sunucusu oluşturmayı ve bu sunucunun çeşitli uygulamalarda yapay zeka sistemlerinin kurumsal API’lerle entegrasyonunu nasıl geliştirdiğini gösterir.

## Sonuç

Bu vaka çalışmaları, Model Context Protocol’ün gerçek dünya senaryolarındaki çok yönlülüğünü ve pratik uygulamalarını ortaya koyuyor. Karmaşık çoklu ajan sistemlerinden hedeflenmiş otomasyon iş akışlarına kadar MCP, yapay zeka sistemlerini ihtiyaç duydukları araçlar ve verilerle standart bir şekilde bağlamanın yolunu sunuyor.

Bu uygulamaları inceleyerek, kendi MCP projelerinizde kullanabileceğiniz mimari desenler, uygulama stratejileri ve en iyi uygulamalar hakkında bilgi edinebilirsiniz. Örnekler, MCP’nin sadece teorik bir çerçeve olmadığını, gerçek iş problemlerine pratik bir çözüm sunduğunu gösteriyor.

## Ek Kaynaklar

- [Azure AI Seyahat Acenteleri GitHub Deposu](https://github.com/Azure-Samples/azure-ai-travel-agents)
- [Azure DevOps MCP Aracı](https://github.com/microsoft/azure-devops-mcp)
- [Playwright MCP Aracı](https://github.com/microsoft/playwright-mcp)
- [Microsoft Docs MCP Sunucusu](https://github.com/MicrosoftDocs/mcp)
- [MCP Topluluk Örnekleri](https://github.com/microsoft/mcp)

**Feragatname**:  
Bu belge, AI çeviri servisi [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucunda ortaya çıkabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.