<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5384bbb2a92d00d5d7e66274dbe0331d",
  "translation_date": "2025-06-20T18:40:38+00:00",
  "source_file": "04-PracticalImplementation/README.md",
  "language_code": "vi"
}
-->
# Triển Khai Thực Tiễn

Triển khai thực tiễn là nơi sức mạnh của Model Context Protocol (MCP) trở nên rõ ràng. Mặc dù việc hiểu lý thuyết và kiến trúc đằng sau MCP rất quan trọng, giá trị thực sự chỉ xuất hiện khi bạn áp dụng các khái niệm này để xây dựng, kiểm thử và triển khai các giải pháp giải quyết các vấn đề thực tế. Chương này sẽ kết nối khoảng cách giữa kiến thức khái niệm và phát triển thực hành, hướng dẫn bạn từng bước đưa các ứng dụng dựa trên MCP vào cuộc sống.

Dù bạn đang phát triển trợ lý thông minh, tích hợp AI vào quy trình kinh doanh, hay xây dựng các công cụ tùy chỉnh cho xử lý dữ liệu, MCP cung cấp một nền tảng linh hoạt. Thiết kế không phụ thuộc vào ngôn ngữ cùng các SDK chính thức cho các ngôn ngữ lập trình phổ biến giúp MCP dễ tiếp cận với nhiều nhà phát triển. Bằng cách tận dụng các SDK này, bạn có thể nhanh chóng tạo mẫu, lặp lại và mở rộng giải pháp trên nhiều nền tảng và môi trường khác nhau.

Trong các phần tiếp theo, bạn sẽ tìm thấy các ví dụ thực tế, mã mẫu và chiến lược triển khai minh họa cách triển khai MCP trong C#, Java, TypeScript, JavaScript và Python. Bạn cũng sẽ học cách gỡ lỗi và kiểm thử các máy chủ MCP, quản lý API, và triển khai giải pháp lên đám mây bằng Azure. Những tài nguyên thực hành này được thiết kế để tăng tốc quá trình học tập và giúp bạn tự tin xây dựng các ứng dụng MCP mạnh mẽ, sẵn sàng cho môi trường sản xuất.

## Tổng Quan

Bài học này tập trung vào các khía cạnh thực tiễn của việc triển khai MCP trên nhiều ngôn ngữ lập trình. Chúng ta sẽ khám phá cách sử dụng các SDK MCP trong C#, Java, TypeScript, JavaScript và Python để xây dựng các ứng dụng bền vững, gỡ lỗi và kiểm thử máy chủ MCP, cũng như tạo các tài nguyên, prompt và công cụ có thể tái sử dụng.

## Mục Tiêu Học Tập

Kết thúc bài học này, bạn sẽ có khả năng:
- Triển khai các giải pháp MCP sử dụng SDK chính thức trên nhiều ngôn ngữ lập trình
- Gỡ lỗi và kiểm thử máy chủ MCP một cách có hệ thống
- Tạo và sử dụng các tính năng máy chủ (Resources, Prompts và Tools)
- Thiết kế các workflow MCP hiệu quả cho các tác vụ phức tạp
- Tối ưu hóa triển khai MCP về hiệu suất và độ tin cậy

## Tài Nguyên SDK Chính Thức

Model Context Protocol cung cấp các SDK chính thức cho nhiều ngôn ngữ:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) 
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

## Làm Việc Với MCP SDKs

Phần này cung cấp các ví dụ thực tiễn về triển khai MCP trên nhiều ngôn ngữ lập trình. Bạn có thể tìm thấy mã mẫu trong thư mục `samples` được tổ chức theo từng ngôn ngữ.

### Mẫu Có Sẵn

Kho lưu trữ bao gồm [các triển khai mẫu](../../../04-PracticalImplementation/samples) bằng các ngôn ngữ sau:

- [C#](./samples/csharp/README.md)
- [Java](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

Mỗi mẫu minh họa các khái niệm chính và mẫu triển khai MCP cho ngôn ngữ và hệ sinh thái cụ thể đó.

## Tính Năng Cốt Lõi Của Máy Chủ

Các máy chủ MCP có thể triển khai bất kỳ sự kết hợp nào của các tính năng sau:

### Resources  
Resources cung cấp ngữ cảnh và dữ liệu cho người dùng hoặc mô hình AI sử dụng:
- Kho lưu trữ tài liệu
- Cơ sở tri thức
- Nguồn dữ liệu có cấu trúc
- Hệ thống tập tin

### Prompts  
Prompts là các thông điệp mẫu và quy trình làm việc dành cho người dùng:
- Mẫu hội thoại được định nghĩa sẵn
- Các mẫu tương tác hướng dẫn
- Cấu trúc đối thoại chuyên biệt

### Tools  
Tools là các hàm cho mô hình AI thực thi:
- Tiện ích xử lý dữ liệu
- Tích hợp API bên ngoài
- Khả năng tính toán
- Chức năng tìm kiếm

## Triển Khai Mẫu: C#

Kho SDK C# chính thức chứa nhiều ví dụ mẫu minh họa các khía cạnh khác nhau của MCP:

- **Basic MCP Client**: Ví dụ đơn giản cho thấy cách tạo một client MCP và gọi các công cụ
- **Basic MCP Server**: Triển khai máy chủ tối giản với đăng ký công cụ cơ bản
- **Advanced MCP Server**: Máy chủ đầy đủ tính năng với đăng ký công cụ, xác thực và xử lý lỗi
- **ASP.NET Integration**: Ví dụ minh họa tích hợp với ASP.NET Core
- **Tool Implementation Patterns**: Các mẫu khác nhau để triển khai công cụ với mức độ phức tạp khác nhau

SDK MCP C# đang trong giai đoạn xem trước và API có thể thay đổi. Chúng tôi sẽ liên tục cập nhật blog này khi SDK phát triển.

### Tính Năng Chính  
- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)

- Xây dựng [Máy Chủ MCP đầu tiên của bạn](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/).

Để xem toàn bộ các ví dụ triển khai C#, truy cập kho mẫu SDK C# chính thức [tại đây](https://github.com/modelcontextprotocol/csharp-sdk)

## Triển Khai Mẫu: Java

SDK Java cung cấp các tùy chọn triển khai MCP mạnh mẽ với các tính năng cấp doanh nghiệp.

### Tính Năng Chính

- Tích hợp Spring Framework
- An toàn kiểu dữ liệu cao
- Hỗ trợ lập trình phản ứng (reactive programming)
- Xử lý lỗi toàn diện

Để xem ví dụ triển khai Java đầy đủ, tham khảo [Java sample](samples/java/containerapp/README.md) trong thư mục mẫu.

## Triển Khai Mẫu: JavaScript

SDK JavaScript cung cấp cách tiếp cận nhẹ nhàng và linh hoạt cho việc triển khai MCP.

### Tính Năng Chính

- Hỗ trợ Node.js và trình duyệt
- API dựa trên Promise
- Dễ dàng tích hợp với Express và các framework khác
- Hỗ trợ WebSocket cho streaming

Để xem ví dụ triển khai JavaScript đầy đủ, tham khảo [JavaScript sample](samples/javascript/README.md) trong thư mục mẫu.

## Triển Khai Mẫu: Python

SDK Python mang đến cách triển khai MCP theo phong cách Python với tích hợp xuất sắc các framework ML.

### Tính Năng Chính

- Hỗ trợ async/await với asyncio
- Tích hợp Flask và FastAPI
- Đăng ký công cụ đơn giản
- Tích hợp gốc với các thư viện ML phổ biến

Để xem ví dụ triển khai Python đầy đủ, tham khảo [Python sample](samples/python/README.md) trong thư mục mẫu.

## Quản Lý API

Azure API Management là giải pháp tuyệt vời để bảo mật các máy chủ MCP. Ý tưởng là đặt một instance Azure API Management trước máy chủ MCP của bạn và để nó xử lý các tính năng bạn có thể cần như:

- giới hạn tốc độ truy cập
- quản lý token
- giám sát
- cân bằng tải
- bảo mật

### Mẫu Azure

Dưới đây là một mẫu Azure thực hiện chính xác điều đó, tức là [tạo một MCP Server và bảo vệ nó bằng Azure API Management](https://github.com/Azure-Samples/remote-mcp-apim-functions-python).

Xem cách quy trình xác thực diễn ra trong hình dưới đây:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true) 

Trong hình trên, các bước sau diễn ra:

- Xác thực/Ủy quyền được thực hiện thông qua Microsoft Entra.
- Azure API Management hoạt động như một cổng và sử dụng các chính sách để điều hướng và quản lý lưu lượng.
- Azure Monitor ghi lại tất cả các yêu cầu để phân tích sau này.

#### Quy trình ủy quyền

Hãy xem chi tiết hơn về quy trình ủy quyền:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### Đặc tả ủy quyền MCP

Tìm hiểu thêm về [đặc tả ủy quyền MCP](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization#2-10-third-party-authorization-flow)

## Triển Khai Máy Chủ MCP Từ Xa Lên Azure

Hãy thử triển khai mẫu mà chúng ta đã đề cập trước đó:

1. Clone kho mã nguồn

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

2. Đăng ký `Microsoft.App`  
    ` resource provider.
    * If you are using Azure CLI, run `az provider register --namespace Microsoft.App --wait`.
    * If you are using Azure PowerShell, run `  
    hoặc dùng lệnh  
    Register-AzResourceProvider -ProviderNamespace Microsoft.App  
    `. Then run `  
    (Chờ một lúc rồi kiểm tra trạng thái đăng ký với lệnh (Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState)

3. Chạy lệnh [azd](https://aka.ms/azd) này để cấp phát dịch vụ quản lý API, function app (với mã nguồn) và tất cả tài nguyên Azure cần thiết

    ```shell
    azd up
    ```

    Lệnh này sẽ triển khai tất cả tài nguyên trên đám mây Azure

### Kiểm thử máy chủ với MCP Inspector

1. Trong **cửa sổ terminal mới**, cài đặt và chạy MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    Bạn sẽ thấy giao diện tương tự như:

    ![Connect to Node inspector](../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.vi.png) 

2. CTRL click để tải ứng dụng web MCP Inspector từ URL được hiển thị bởi ứng dụng (ví dụ: http://127.0.0.1:6274/#resources)
3. Đặt loại truyền tải thành `SSE`
1. Set the URL to your running API Management SSE endpoint displayed after `azd up` và **Kết nối**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

5. **Liệt kê các công cụ**. Nhấn vào một công cụ và **Chạy công cụ**.

Nếu tất cả các bước đều thành công, bạn đã kết nối được với máy chủ MCP và có thể gọi một công cụ.

## Máy Chủ MCP cho Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): Bộ kho này là mẫu khởi đầu nhanh để xây dựng và triển khai các máy chủ MCP từ xa tùy chỉnh sử dụng Azure Functions với Python, C# .NET hoặc Node/TypeScript.

Các mẫu này cung cấp giải pháp hoàn chỉnh cho phép nhà phát triển:

- Xây dựng và chạy cục bộ: Phát triển và gỡ lỗi máy chủ MCP trên máy tính cá nhân
- Triển khai lên Azure: Dễ dàng triển khai lên đám mây với lệnh azd up đơn giản
- Kết nối từ các client: Kết nối với máy chủ MCP từ nhiều client khác nhau bao gồm chế độ agent Copilot của VS Code và công cụ MCP Inspector

### Tính Năng Chính:

- Bảo mật theo thiết kế: Máy chủ MCP được bảo vệ bằng khóa và HTTPS
- Tùy chọn xác thực: Hỗ trợ OAuth với xác thực tích hợp sẵn và/hoặc API Management
- Cô lập mạng: Cho phép cô lập mạng sử dụng Azure Virtual Networks (VNET)
- Kiến trúc serverless: Tận dụng Azure Functions để thực thi theo sự kiện, dễ mở rộng
- Phát triển cục bộ: Hỗ trợ đầy đủ cho phát triển và gỡ lỗi cục bộ
- Triển khai đơn giản: Quy trình triển khai lên Azure được tối ưu hóa

Kho chứa mã bao gồm tất cả các tệp cấu hình cần thiết, mã nguồn và định nghĩa hạ tầng để bạn nhanh chóng bắt đầu với triển khai máy chủ MCP sẵn sàng cho sản xuất.

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - Mẫu triển khai MCP sử dụng Azure Functions với Python

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - Mẫu triển khai MCP sử dụng Azure Functions với C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - Mẫu triển khai MCP sử dụng Azure Functions với Node/TypeScript.

## Những Điều Cần Nhớ

- SDK MCP cung cấp công cụ chuyên biệt theo ngôn ngữ để triển khai các giải pháp MCP bền vững
- Quá trình gỡ lỗi và kiểm thử rất quan trọng để có ứng dụng MCP đáng tin cậy
- Các mẫu prompt tái sử dụng giúp tương tác AI nhất quán
- Các workflow được thiết kế tốt có thể phối hợp các tác vụ phức tạp sử dụng nhiều công cụ
- Triển khai MCP cần cân nhắc về bảo mật, hiệu suất và xử lý lỗi

## Bài Tập

Thiết kế một workflow MCP thực tiễn giải quyết một vấn đề thực tế trong lĩnh vực của bạn:

1. Xác định 3-4 công cụ hữu ích để giải quyết vấn đề này
2. Tạo sơ đồ workflow mô tả cách các công cụ này tương tác với nhau
3. Triển khai phiên bản cơ bản của một công cụ bằng ngôn ngữ bạn ưa thích
4. Tạo một mẫu prompt giúp mô hình sử dụng hiệu quả công cụ của bạn

## Tài Nguyên Bổ Sung


---

Tiếp theo: [Chủ Đề Nâng Cao](../05-AdvancedTopics/README.md)

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và có thẩm quyền. Đối với thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.