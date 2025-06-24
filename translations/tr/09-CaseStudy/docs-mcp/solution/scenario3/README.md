<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "db532b1ec386c9ce38c791653dc3c881",
  "translation_date": "2025-06-21T14:39:32+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/scenario3/README.md",
  "language_code": "tr"
}
-->
# Senaryo 3: VS Code’da MCP Sunucusu ile Editör İçi Dokümanlar

## Genel Bakış

Bu senaryoda, Microsoft Learn Dokümanlarını doğrudan Visual Studio Code ortamınıza MCP sunucusu kullanarak nasıl getireceğinizi öğreneceksiniz. Sürekli tarayıcı sekmeleri arasında doküman aramak yerine, resmi dokümanlara doğrudan editörünüzden erişebilir, arama yapabilir ve referans verebilirsiniz. Bu yaklaşım iş akışınızı hızlandırır, odaklanmanızı sağlar ve GitHub Copilot gibi araçlarla sorunsuz entegrasyon imkanı sunar.

- Kodlama ortamınızı terk etmeden VS Code içinde doküman arayın ve okuyun.
- Dokümantasyona referans verin ve bağlantıları doğrudan README veya ders dosyalarınıza ekleyin.
- GitHub Copilot ve MCP’yi birlikte kullanarak yapay zekâ destekli kesintisiz dokümantasyon iş akışı oluşturun.

## Öğrenme Hedefleri

Bu bölümün sonunda, VS Code içinde MCP sunucusunu nasıl kurup kullanacağınızı anlayacak ve dokümantasyon ile geliştirme iş akışınızı nasıl geliştireceğinizi öğreneceksiniz. Şunları yapabileceksiniz:

- Çalışma alanınızı MCP sunucusunu doküman araması için kullanacak şekilde yapılandırmak.
- VS Code içinden doğrudan doküman aramak ve eklemek.
- Daha verimli, yapay zekâ destekli bir iş akışı için GitHub Copilot ve MCP’nin gücünü birleştirmek.

Bu beceriler, odaklanmanızı artırmanıza, dokümantasyon kalitenizi iyileştirmenize ve geliştirici ya da teknik yazar olarak verimliliğinizi yükseltmenize yardımcı olacak.

## Çözüm

Editör içinde dokümantasyon erişimi sağlamak için, MCP sunucusunu VS Code ve GitHub Copilot ile entegre eden bir dizi adımı takip edeceksiniz. Bu çözüm, ders yazanlar, dokümantasyon yazarları ve dokümanlar ile Copilot’u kullanırken odaklarını editörde tutmak isteyen geliştiriciler için idealdir.

- Ders ya da proje dokümantasyonu yazarken README dosyasına hızlıca referans bağlantıları ekleyin.
- Copilot ile kod üretirken MCP ile ilgili dokümanları anında bulun ve alıntı yapın.
- Editörde odaklanın ve verimliliğinizi artırın.

### Adım Adım Rehber

Başlamak için şu adımları izleyin. Her adım için, süreci görsel olarak göstermek amacıyla assets klasöründen bir ekran görüntüsü ekleyebilirsiniz.

1. **MCP yapılandırmasını ekleyin:**  
   Proje kök dizininizde bir `.vscode/mcp.json` dosyası oluşturun ve aşağıdaki yapılandırmayı ekleyin:  
   ```json
   {
     "servers": {
       "LearnDocsMCP": {
         "url": "https://learn.microsoft.com/api/mcp"
       }
     }
   }
   ```  
   Bu yapılandırma, VS Code’a [`Microsoft Learn Docs MCP server`](https://github.com/MicrosoftDocs/mcp) ile nasıl bağlantı kurulacağını söyler.

   ![Adım 1: mcp.json dosyasını .vscode klasörüne ekleyin](../../../../../../translated_images/step1-mcp-json.c06a007fccc3edfaf0598a31903c9ec71476d9fd3ae6c1b2b4321fd38688ca4b.tr.png)

2. **GitHub Copilot Chat panelini açın:**  
   Eğer GitHub Copilot eklentisi henüz yüklü değilse, VS Code’daki Extensions görünümüne gidip yükleyin. Direkt olarak [Visual Studio Code Marketplace](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat) üzerinden indirebilirsiniz. Ardından, yan panelden Copilot Chat panelini açın.

   ![Adım 2: Copilot Chat panelini açın](../../../../../../translated_images/step2-copilot-panel.f1cc86e9b9b8cd1a85e4df4923de8bafee4830541ab255e3c90c09777fed97db.tr.png)

3. **Agent modunu etkinleştirin ve araçları doğrulayın:**  
   Copilot Chat panelinde agent modunu açın.

   ![Adım 3: Agent modunu etkinleştirin ve araçları doğrulayın](../../../../../../translated_images/step3-agent-mode.cdc32520fd7dd1d149c3f5226763c1d85a06d3c041d4cc983447625bdbeff4d4.tr.png)

   Agent modunu etkinleştirdikten sonra, MCP sunucusunun kullanılabilir araçlar arasında listelendiğinden emin olun. Bu, Copilot agent’ın dokümantasyon sunucusuna erişerek ilgili bilgileri getirebilmesini sağlar.

   ![Adım 3: MCP sunucu aracını doğrulayın](../../../../../../translated_images/step3-verify-mcp-tool.76096a6329cbfecd42888780f322370a0d8c8fa003ed3eeb7ccd23f0fc50c1ad.tr.png)

4. **Yeni bir sohbet başlatın ve agent’ı yönlendirin:**  
   Copilot Chat panelinde yeni bir sohbet açın. Artık dokümantasyon sorularınızı agent’a iletebilirsiniz. Agent, MCP sunucusunu kullanarak ilgili Microsoft Learn dokümanlarını doğrudan editörünüzde getirecek ve gösterecektir.

   - *"X konusu için bir çalışma planı hazırlamaya çalışıyorum. 8 hafta boyunca çalışacağım, her hafta için hangi içerikleri almam gerektiğini öner."*

   ![Adım 4: Agent’a sohbet içinde yönlendirme yapın](../../../../../../translated_images/step4-prompt-chat.12187bb001605efc5077992b621f0fcd1df12023c5dce0464f8eb8f3d595218f.tr.png)

5. **Canlı Sorgu:**

   > Azure AI Foundry Discord’daki [#get-help](https://discord.gg/D6cRhjHWSC) bölümünden canlı bir sorgu alalım ([orijinal mesajı görüntüle](https://discord.com/channels/1113626258182504448/1385498306720829572)):  
   
   *"Azure AI Foundry üzerinde geliştirilen AI agent’larıyla çoklu-agent çözümünü nasıl dağıtacağım hakkında cevap arıyorum. Doğrudan bir dağıtım yöntemi yok gibi, örneğin Copilot Studio kanalları gibi. Peki, kurumsal kullanıcıların etkileşimde bulunup işi yapabilmesi için bu dağıtımı yapmanın farklı yolları nelerdir?  
   MS Teams ile Azure AI Foundry Agent’ları arasında köprü görevi görecek Azure Bot servisini kullanabileceğimizi söyleyen birçok makale/blog var, peki bu işe yarar mı? Azure bot’u, Azure function üzerinden Orchestrator Agent’a bağlayarak orkestrasyon yapmak için kurarsam mı yoksa her AI agent için Bot framework üzerinde orkestrasyon yapmak üzere ayrı Azure function mı oluşturmam gerekir? Başka önerileriniz varsa memnuniyetle karşılarım."*

   ![Adım 5: Canlı sorgular](../../../../../../translated_images/step5-live-queries.49db3e4a50bea27327e3cb18c24d263b7d134930d78e7392f9515a1c00264a7f.tr.png)

   Agent, ilgili doküman bağlantıları ve özetlerle yanıt verecek; bunları markdown dosyalarınıza doğrudan ekleyebilir veya kodunuzda referans olarak kullanabilirsiniz.

### Örnek Sorgular

Deneyebileceğiniz bazı örnek sorgular şunlardır. Bu sorgular, MCP sunucusu ve Copilot’un VS Code’u terk etmeden anında, bağlama duyarlı doküman ve referans sağlayabilme yeteneğini gösterecektir:

- "Azure Functions tetikleyicilerini nasıl kullanırım?"
- "Azure Key Vault resmi dokümantasyonuna bir bağlantı ekle."
- "Azure kaynaklarını güvence altına almak için en iyi uygulamalar nelerdir?"
- "Azure AI servisleri için hızlı başlangıç rehberi bul."

Bu sorgular, MCP sunucusu ve Copilot’un birlikte nasıl çalışarak VS Code içinde anında, bağlama uygun doküman ve referans sağlayabileceğini gösterecektir.

---

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Orijinal belge, kendi dilinde yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı nedeniyle oluşabilecek yanlış anlamalar veya yanlış yorumlamalar için sorumluluk kabul edilmemektedir.