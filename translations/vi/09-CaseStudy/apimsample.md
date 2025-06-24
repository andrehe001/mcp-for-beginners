<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "36de9fae488d6de554d969fe8e0801a8",
  "translation_date": "2025-06-20T19:22:34+00:00",
  "source_file": "09-CaseStudy/apimsample.md",
  "language_code": "vi"
}
-->
# Case Study: Phơi bày REST API trong API Management dưới dạng MCP server

Azure API Management là một dịch vụ cung cấp Gateway trên các API Endpoints của bạn. Cách hoạt động là Azure API Management đóng vai trò như một proxy đứng trước các API của bạn và có thể quyết định cách xử lý các yêu cầu đến.

Khi sử dụng dịch vụ này, bạn sẽ được bổ sung rất nhiều tính năng như:

- **Bảo mật**, bạn có thể sử dụng từ API keys, JWT đến managed identity.
- **Giới hạn tần suất gọi (Rate limiting)**, một tính năng tuyệt vời cho phép bạn quyết định số lượng cuộc gọi được phép qua trong một đơn vị thời gian nhất định. Điều này giúp đảm bảo tất cả người dùng đều có trải nghiệm tốt và dịch vụ của bạn không bị quá tải bởi các yêu cầu.
- **Mở rộng & Cân bằng tải**. Bạn có thể thiết lập nhiều endpoints để phân phối tải và cũng có thể quyết định cách thức "cân bằng tải".
- **Các tính năng AI như semantic caching**, giới hạn token và giám sát token, và nhiều hơn nữa. Đây là những tính năng tuyệt vời giúp cải thiện khả năng phản hồi cũng như giúp bạn kiểm soát chi tiêu token. [Tìm hiểu thêm tại đây](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities).

## Tại sao lại chọn MCP + Azure API Management?

Model Context Protocol đang nhanh chóng trở thành tiêu chuẩn cho các ứng dụng AI agentic và cách phơi bày công cụ, dữ liệu một cách nhất quán. Azure API Management là lựa chọn tự nhiên khi bạn cần "quản lý" các API. MCP Servers thường tích hợp với các API khác để xử lý các yêu cầu tới một công cụ, ví dụ. Vì vậy, việc kết hợp Azure API Management và MCP là rất hợp lý.

## Tổng quan

Trong trường hợp sử dụng cụ thể này, chúng ta sẽ học cách phơi bày các API endpoints dưới dạng MCP Server. Bằng cách này, chúng ta có thể dễ dàng biến các endpoint này thành một phần của ứng dụng agentic đồng thời tận dụng các tính năng từ Azure API Management.

## Các tính năng chính

- Bạn chọn các phương thức endpoint muốn phơi bày dưới dạng công cụ.
- Các tính năng bổ sung bạn nhận được phụ thuộc vào cách bạn cấu hình trong phần policy cho API. Ở đây chúng ta sẽ hướng dẫn cách thêm tính năng giới hạn tần suất gọi.

## Bước chuẩn bị: nhập API

Nếu bạn đã có API trong Azure API Management rồi thì rất tốt, bạn có thể bỏ qua bước này. Nếu chưa, hãy xem liên kết này, [nhập API vào Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api).

## Phơi bày API dưới dạng MCP Server

Để phơi bày các API endpoints, hãy làm theo các bước sau:

1. Truy cập Azure Portal tại địa chỉ <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
Đi tới instance API Management của bạn.

1. Trong menu bên trái, chọn APIs > MCP Servers > + Create new MCP Server.

1. Trong phần API, chọn một REST API để phơi bày dưới dạng MCP server.

1. Chọn một hoặc nhiều API Operations để phơi bày dưới dạng công cụ. Bạn có thể chọn tất cả các operation hoặc chỉ một số cụ thể.

    ![Select methods to expose](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. Chọn **Create**.

1. Truy cập menu **APIs** và **MCP Servers**, bạn sẽ thấy như sau:

    ![See the MCP Server in the main pane](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP server đã được tạo và các API operations được phơi bày dưới dạng công cụ. MCP server sẽ được liệt kê trong phần MCP Servers. Cột URL hiển thị endpoint của MCP server mà bạn có thể gọi để thử nghiệm hoặc sử dụng trong ứng dụng khách.

## Tùy chọn: Cấu hình chính sách

Azure API Management có khái niệm cốt lõi là các chính sách (policies) nơi bạn thiết lập các quy tắc khác nhau cho các endpoint như giới hạn tần suất gọi hay semantic caching. Các chính sách này được viết dưới dạng XML.

Dưới đây là cách bạn có thể thiết lập một chính sách giới hạn tần suất gọi cho MCP Server:

1. Trong portal, dưới phần APIs, chọn **MCP Servers**.

1. Chọn MCP server bạn đã tạo.

1. Trong menu bên trái, dưới MCP, chọn **Policies**.

1. Trong trình chỉnh sửa chính sách, thêm hoặc chỉnh sửa các chính sách bạn muốn áp dụng cho các công cụ của MCP server. Các chính sách được định nghĩa dưới dạng XML. Ví dụ, bạn có thể thêm chính sách giới hạn số cuộc gọi tới các công cụ của MCP server (ví dụ 5 cuộc gọi mỗi 30 giây cho mỗi địa chỉ IP client). Đây là đoạn XML để thực hiện giới hạn tần suất:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    Đây là hình ảnh trình chỉnh sửa chính sách:

    ![Policy editor](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## Thử nghiệm

Hãy đảm bảo MCP Server của chúng ta hoạt động đúng như mong đợi.

Chúng ta sẽ sử dụng Visual Studio Code và GitHub Copilot với chế độ Agent. Chúng ta sẽ thêm MCP server vào file *mcp.json*. Bằng cách này, Visual Studio Code sẽ đóng vai trò như một client với khả năng agentic và người dùng cuối có thể nhập prompt để tương tác với server đó.

Cách thêm MCP server vào Visual Studio Code:

1. Sử dụng lệnh MCP: **Add Server command from the Command Palette**.

1. Khi được yêu cầu, chọn loại server: **HTTP (HTTP hoặc Server Sent Events)**.

1. Nhập URL của MCP server trong API Management. Ví dụ: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (cho endpoint SSE) hoặc **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (cho endpoint MCP), lưu ý sự khác biệt giữa các phương thức truyền tải là `/sse` or `/mcp`.

1. Nhập một server ID theo ý bạn. Đây không phải giá trị quan trọng nhưng giúp bạn nhớ server instance này là gì.

1. Chọn lưu cấu hình vào workspace settings hoặc user settings.

  - **Workspace settings** - Cấu hình server được lưu trong file .vscode/mcp.json chỉ có trong workspace hiện tại.

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    hoặc nếu bạn chọn streaming HTTP làm phương thức truyền tải sẽ hơi khác:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **User settings** - Cấu hình server được thêm vào file *settings.json* toàn cục và có sẵn ở tất cả các workspace. Cấu hình trông giống như sau:

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. Bạn cũng cần thêm cấu hình header để xác thực đúng với Azure API Management. Nó sử dụng header tên **Ocp-Apim-Subscription-Key**.

    - Đây là cách thêm vào settings:

    ![Adding header for authentication](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png), điều này sẽ hiển thị prompt yêu cầu bạn nhập giá trị API key, bạn có thể tìm thấy trong Azure Portal của instance Azure API Management.

    - Để thêm vào *mcp.json* thay vào đó, bạn có thể thêm như sau:

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

### Sử dụng chế độ Agent

Bây giờ chúng ta đã thiết lập xong trong settings hoặc trong *.vscode/mcp.json*. Hãy thử sử dụng.

Sẽ có biểu tượng Tools như sau, nơi các công cụ được phơi bày từ server của bạn được liệt kê:

![Tools from the server](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. Nhấp vào biểu tượng tools và bạn sẽ thấy danh sách các công cụ như sau:

    ![Tools](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. Nhập prompt trong chat để gọi công cụ. Ví dụ, nếu bạn chọn công cụ lấy thông tin về một đơn hàng, bạn có thể hỏi agent về đơn hàng đó. Đây là ví dụ prompt:

    ```text
    get information from order 2
    ```

    Bạn sẽ thấy biểu tượng công cụ yêu cầu xác nhận để tiếp tục gọi công cụ. Chọn để tiếp tục chạy công cụ, bạn sẽ thấy kết quả đầu ra như sau:

    ![Result from prompt](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **Những gì bạn thấy phụ thuộc vào các công cụ bạn đã thiết lập, nhưng ý tưởng là bạn sẽ nhận được phản hồi dạng văn bản như trên.**


## Tham khảo

Bạn có thể tìm hiểu thêm qua các tài liệu sau:

- [Hướng dẫn về Azure API Management và MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [Ví dụ Python: Bảo mật MCP servers từ xa bằng Azure API Management (thử nghiệm)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [Phòng thí nghiệm ủy quyền client MCP](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [Sử dụng extension Azure API Management cho VS Code để nhập và quản lý APIs](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [Đăng ký và khám phá MCP servers từ xa trong Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) Kho lưu trữ tuyệt vời thể hiện nhiều khả năng AI với Azure API Management
- [Hội thảo AI Gateway](https://azure-samples.github.io/AI-Gateway/) Chứa các workshop sử dụng Azure Portal, đây là cách tuyệt vời để bắt đầu đánh giá các khả năng AI.

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi nỗ lực đảm bảo độ chính xác, xin lưu ý rằng bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm đối với bất kỳ sự hiểu nhầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.