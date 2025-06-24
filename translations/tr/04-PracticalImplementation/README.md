<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5384bbb2a92d00d5d7e66274dbe0331d",
  "translation_date": "2025-06-20T18:35:05+00:00",
  "source_file": "04-PracticalImplementation/README.md",
  "language_code": "tr"
}
-->
# Pratik Uygulama

Pratik uygulama, Model Context Protocol’ün (MCP) gücünün somutlaştığı yerdir. MCP’nin teori ve mimarisini anlamak önemli olsa da, gerçek değer bu kavramları kullanarak gerçek dünya problemlerini çözen çözümler geliştirdiğinizde ortaya çıkar. Bu bölüm, kavramsal bilgi ile uygulamalı geliştirme arasındaki boşluğu kapatarak, MCP tabanlı uygulamaların hayata geçirilme sürecinde size rehberlik eder.

İster akıllı asistanlar geliştiriyor, ister yapay zekayı iş süreçlerinize entegre ediyor ya da veri işleme için özel araçlar oluşturuyor olun, MCP esnek bir temel sunar. Dil bağımsız tasarımı ve popüler programlama dilleri için resmi SDK’ları sayesinde geniş bir geliştirici kitlesi tarafından erişilebilir. Bu SDK’ları kullanarak çözümlerinizi farklı platformlar ve ortamlar arasında hızla prototipleyebilir, yineleyebilir ve ölçeklendirebilirsiniz.

Aşağıdaki bölümlerde, MCP’nin C#, Java, TypeScript, JavaScript ve Python’da nasıl uygulanacağını gösteren pratik örnekler, örnek kodlar ve dağıtım stratejileri bulacaksınız. Ayrıca MCP sunucularınızı nasıl hata ayıklayıp test edeceğinizi, API’leri nasıl yöneteceğinizi ve çözümleri Azure kullanarak buluta nasıl dağıtacağınızı öğreneceksiniz. Bu uygulamalı kaynaklar, öğrenme sürecinizi hızlandırmak ve sağlam, üretime hazır MCP uygulamaları oluşturmanızı sağlamak için tasarlanmıştır.

## Genel Bakış

Bu ders, MCP uygulamasının birden çok programlama dilinde pratik yönlerine odaklanır. C#, Java, TypeScript, JavaScript ve Python’da MCP SDK’larının nasıl kullanılacağını, sağlam uygulamalar geliştirip MCP sunucularını nasıl hata ayıklayıp test edeceğinizi ve yeniden kullanılabilir kaynaklar, promptlar ve araçlar oluşturmayı keşfedeceğiz.

## Öğrenme Hedefleri

Bu dersin sonunda şunları yapabileceksiniz:
- Resmi SDK’ları kullanarak farklı programlama dillerinde MCP çözümleri geliştirmek
- MCP sunucularını sistematik olarak hata ayıklamak ve test etmek
- Sunucu özellikleri (Kaynaklar, Promptlar ve Araçlar) oluşturup kullanmak
- Karmaşık görevler için etkili MCP iş akışları tasarlamak
- MCP uygulamalarını performans ve güvenilirlik açısından optimize etmek

## Resmi SDK Kaynakları

Model Context Protocol, birden çok dil için resmi SDK’lar sunar:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk)
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

## MCP SDK’ları ile Çalışmak

Bu bölüm, MCP’nin birden çok programlama dilinde nasıl uygulanacağına dair pratik örnekler sunar. Örnek kodları dil bazında düzenlenmiş `samples` dizininde bulabilirsiniz.

### Mevcut Örnekler

Depoda aşağıdaki dillerde [örnek uygulamalar](../../../04-PracticalImplementation/samples) bulunmaktadır:

- [C#](./samples/csharp/README.md)
- [Java](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Her örnek, ilgili dil ve ekosistem için temel MCP kavramlarını ve uygulama kalıplarını gösterir.

## Temel Sunucu Özellikleri

MCP sunucuları aşağıdaki özelliklerin herhangi bir kombinasyonunu uygulayabilir:

### Kaynaklar  
Kaynaklar, kullanıcı veya yapay zeka modelinin kullanması için bağlam ve veri sağlar:
- Doküman depoları
- Bilgi tabanları
- Yapılandırılmış veri kaynakları
- Dosya sistemleri

### Promptlar  
Promptlar, kullanıcılar için şablonlanmış mesajlar ve iş akışlarıdır:
- Önceden tanımlanmış sohbet şablonları
- Yönlendirilmiş etkileşim desenleri
- Özelleşmiş diyalog yapıları

### Araçlar  
Araçlar, yapay zeka modelinin çalıştırabileceği fonksiyonlardır:
- Veri işleme araçları
- Harici API entegrasyonları
- Hesaplama yetenekleri
- Arama fonksiyonları

## Örnek Uygulamalar: C#

Resmi C# SDK deposu, MCP’nin farklı yönlerini gösteren birkaç örnek uygulama içerir:

- **Temel MCP İstemcisi**: MCP istemcisi oluşturmayı ve araçları çağırmayı gösteren basit örnek
- **Temel MCP Sunucusu**: Temel araç kaydı ile minimal sunucu uygulaması
- **Gelişmiş MCP Sunucusu**: Araç kaydı, kimlik doğrulama ve hata yönetimi içeren tam özellikli sunucu
- **ASP.NET Entegrasyonu**: ASP.NET Core ile entegrasyonu gösteren örnekler
- **Araç Uygulama Kalıpları**: Farklı karmaşıklık seviyelerinde araç uygulama kalıpları

MCP C# SDK önizlemededir ve API’lerde değişiklik olabilir. SDK geliştikçe bu blogu sürekli güncelleyeceğiz.

### Öne Çıkan Özellikler  
- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)

- [İlk MCP Sunucunuzu oluşturma](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

Tam C# uygulama örnekleri için [resmi C# SDK örnek deposunu](https://github.com/modelcontextprotocol/csharp-sdk) ziyaret edin.

## Örnek uygulama: Java Uygulaması

Java SDK, kurumsal sınıf özelliklerle güçlü MCP uygulama seçenekleri sunar.

### Öne Çıkan Özellikler

- Spring Framework entegrasyonu
- Güçlü tür güvenliği
- Reaktif programlama desteği
- Kapsamlı hata yönetimi

Tam Java uygulama örneği için örnekler dizinindeki [Java örneğine](samples/java/containerapp/README.md) bakabilirsiniz.

## Örnek uygulama: JavaScript Uygulaması

JavaScript SDK, MCP uygulaması için hafif ve esnek bir yaklaşım sunar.

### Öne Çıkan Özellikler

- Node.js ve tarayıcı desteği
- Promise tabanlı API
- Express ve diğer frameworklerle kolay entegrasyon
- Akış için WebSocket desteği

Tam JavaScript uygulama örneği için örnekler dizinindeki [JavaScript örneğine](samples/javascript/README.md) bakabilirsiniz.

## Örnek uygulama: Python Uygulaması

Python SDK, MCP uygulaması için Python’a özgü ve güçlü ML framework entegrasyonları sunar.

### Öne Çıkan Özellikler

- Async/await desteği ve asyncio ile uyumlu
- Flask ve FastAPI entegrasyonu
- Basit araç kaydı
- Popüler ML kütüphaneleri ile yerel entegrasyon

Tam Python uygulama örneği için örnekler dizinindeki [Python örneğine](samples/python/README.md) bakabilirsiniz.

## API yönetimi

Azure API Management, MCP Sunucularını nasıl güvence altına alabileceğimiz için harika bir çözümdür. Fikir, MCP Sunucunuzun önüne bir Azure API Management örneği koymak ve aşağıdaki gibi istediğiniz özellikleri onun yönetmesine izin vermektir:

- hız sınırlandırma
- token yönetimi
- izleme
- yük dengeleme
- güvenlik

### Azure Örneği

İşte tam olarak bunu yapan bir Azure Örneği, yani [bir MCP Sunucusu oluşturup Azure API Management ile güvence altına alma](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Yetkilendirme akışının aşağıdaki resimde nasıl gerçekleştiğine bakın:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true)

Yukarıdaki görselde şu işlemler gerçekleşir:

- Kimlik doğrulama/Yetkilendirme Microsoft Entra kullanılarak yapılır.
- Azure API Management bir ağ geçidi olarak görev yapar ve trafiği yönlendirmek ve yönetmek için politikalar kullanır.
- Azure Monitor, tüm istekleri daha sonra analiz için kaydeder.

#### Yetkilendirme akışı

Yetkilendirme akışına daha yakından bakalım:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### MCP yetkilendirme spesifikasyonu

[MCP Yetkilendirme spesifikasyonu](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization#2-10-third-party-authorization-flow) hakkında daha fazla bilgi edinin.

## Uzaktan MCP Sunucusunu Azure’a Dağıtma

Daha önce bahsettiğimiz örneği dağıtıp dağıtamayacağımıza bakalım:

1. Depoyu klonlayın

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

2. `Microsoft.App` sağlayıcısını kaydedin

    ` resource provider.
    * If you are using Azure CLI, run `az provider register --namespace Microsoft.App --wait`.
    * If you are using Azure PowerShell, run `  
    `. Then run `Register-AzResourceProvider -ProviderNamespace Microsoft.App`. Then run `  
    Kayıt işleminin tamamlanıp tamamlanmadığını kontrol etmek için bir süre sonra `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` komutunu çalıştırabilirsiniz.

3. Bu [azd](https://aka.ms/azd) komutunu çalıştırarak API Management servisini, function app’i (kod dahil) ve diğer gerekli Azure kaynaklarını oluşturun

    ```shell
    azd up
    ```

    Bu komut, Azure üzerinde tüm bulut kaynaklarını dağıtmalıdır.

### MCP Inspector ile sunucunuzu test etme

1. **Yeni bir terminal penceresinde**, MCP Inspector’ı kurup çalıştırın

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Aşağıdaki gibi bir arayüz görmelisiniz:

    ![Connect to Node inspector](../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.tr.png)

2. Uygulamanın gösterdiği URL’den (örneğin http://127.0.0.1:6274/#resources) MCP Inspector web uygulamasını CTRL tıklayarak açın
3. Taşıma türünü `SSE`
1. Set the URL to your running API Management SSE endpoint displayed after `azd up` olarak ayarlayın ve **Bağlan**a tıklayın:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

5. **Araçları Listele**. Bir araca tıklayın ve **Aracı Çalıştır**a basın.

Eğer tüm adımlar başarılı olduysa, artık MCP sunucusuna bağlısınız ve bir aracı çağırabilmişsiniz demektir.

## Azure için MCP sunucuları

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Bu depo seti, Python, C# .NET veya Node/TypeScript kullanarak Azure Functions ile özel uzak MCP (Model Context Protocol) sunucuları oluşturup dağıtmak için hızlı başlangıç şablonlarıdır.

Örnekler, geliştiricilere tam bir çözüm sunar:

- Yerel olarak oluşturma ve çalıştırma: MCP sunucusunu yerel makinede geliştirin ve hata ayıklayın
- Azure’a dağıtma: Basit bir azd up komutuyla buluta kolayca dağıtım yapın
- İstemcilerden bağlanma: VS Code’un Copilot agent modu ve MCP Inspector aracı dahil çeşitli istemcilerden MCP sunucusuna bağlanın

### Öne Çıkan Özellikler:

- Tasarım gereği güvenlik: MCP sunucusu anahtarlar ve HTTPS ile güvence altına alınmıştır
- Kimlik doğrulama seçenekleri: Dahili kimlik doğrulama ve/veya API Management ile OAuth desteği
- Ağ izolasyonu: Azure Sanal Ağları (VNET) kullanarak ağ izolasyonu sağlar
- Sunucusuz mimari: Ölçeklenebilir, olay odaklı yürütme için Azure Functions kullanır
- Yerel geliştirme: Kapsamlı yerel geliştirme ve hata ayıklama desteği
- Basit dağıtım: Azure’a kolaylaştırılmış dağıtım süreci

Depo, üretime hazır bir MCP sunucu uygulamasıyla hızlı başlamanız için gerekli tüm yapılandırma dosyalarını, kaynak kodu ve altyapı tanımlarını içerir.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Azure Functions ile Python kullanarak MCP örnek uygulaması
- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Azure Functions ile C# .NET kullanarak MCP örnek uygulaması
- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Azure Functions ile Node/TypeScript kullanarak MCP örnek uygulaması

## Temel Çıkarımlar

- MCP SDK’ları, sağlam MCP çözümleri geliştirmek için dil bazlı araçlar sağlar
- Hata ayıklama ve test süreci, güvenilir MCP uygulamaları için kritiktir
- Yeniden kullanılabilir prompt şablonları, tutarlı yapay zeka etkileşimleri sağlar
- İyi tasarlanmış iş akışları, birden fazla araç kullanarak karmaşık görevleri koordine edebilir
- MCP çözümleri geliştirirken güvenlik, performans ve hata yönetimi göz önünde bulundurulmalıdır

## Alıştırma

Alanınızdaki gerçek bir problemi ele alan pratik bir MCP iş akışı tasarlayın:

1. Bu problemi çözmek için faydalı olabilecek 3-4 araç belirleyin
2. Bu araçların nasıl etkileşime girdiğini gösteren bir iş akışı diyagramı oluşturun
3. Tercih ettiğiniz dilde araçlardan birinin temel bir sürümünü uygulayın
4. Modelin aracınızı etkili kullanmasına yardımcı olacak bir prompt şablonu oluşturun

## Ek Kaynaklar


---

Sonraki: [Gelişmiş Konular](../05-AdvancedTopics/README.md)

**Feragatname**:  
Bu belge, AI çeviri hizmeti [Co-op Translator](https://github.com/Azure/co-op-translator) kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hatalar veya yanlışlıklar içerebileceğini lütfen unutmayınız. Orijinal belge, kendi ana dilindeki haliyle yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımı sonucu oluşabilecek yanlış anlamalar veya yorum hatalarından sorumlu değiliz.