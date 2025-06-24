<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "6940b1e931e51821b219aa9dcfe8c4ee",
  "translation_date": "2025-06-23T11:12:59+00:00",
  "source_file": "09-CaseStudy/README.md",
  "language_code": "vi"
}
-->
# MCP trong Thực Tiễn: Các Nghiên Cứu Trường Hợp Thực Tế

Model Context Protocol (MCP) đang thay đổi cách các ứng dụng AI tương tác với dữ liệu, công cụ và dịch vụ. Phần này trình bày các nghiên cứu trường hợp thực tế minh họa các ứng dụng thực tiễn của MCP trong nhiều kịch bản doanh nghiệp khác nhau.

## Tổng Quan

Phần này giới thiệu các ví dụ cụ thể về việc triển khai MCP, làm nổi bật cách các tổ chức tận dụng giao thức này để giải quyết các thách thức kinh doanh phức tạp. Qua việc xem xét những nghiên cứu trường hợp này, bạn sẽ hiểu rõ hơn về tính linh hoạt, khả năng mở rộng và lợi ích thực tiễn của MCP trong các tình huống thực tế.

## Mục Tiêu Học Tập Chính

Khi khám phá các nghiên cứu trường hợp này, bạn sẽ:

- Hiểu cách MCP được áp dụng để giải quyết các vấn đề kinh doanh cụ thể
- Tìm hiểu về các mẫu tích hợp và cách tiếp cận kiến trúc khác nhau
- Nhận biết các thực hành tốt nhất khi triển khai MCP trong môi trường doanh nghiệp
- Nắm bắt các thách thức và giải pháp đã gặp phải trong các triển khai thực tế
- Xác định cơ hội áp dụng các mẫu tương tự vào dự án của riêng bạn

## Các Nghiên Cứu Trường Hợp Tiêu Biểu

### 1. [Azure AI Travel Agents – Triển Khai Tham Chiếu](./travelagentsample.md)

Nghiên cứu trường hợp này phân tích giải pháp tham chiếu toàn diện của Microsoft, thể hiện cách xây dựng ứng dụng lập kế hoạch du lịch đa tác nhân, được hỗ trợ bởi AI, sử dụng MCP, Azure OpenAI và Azure AI Search. Dự án trình bày:

- Điều phối đa tác nhân thông qua MCP
- Tích hợp dữ liệu doanh nghiệp với Azure AI Search
- Kiến trúc bảo mật và có khả năng mở rộng sử dụng dịch vụ Azure
- Công cụ mở rộng với các thành phần MCP có thể tái sử dụng
- Trải nghiệm người dùng đàm thoại được hỗ trợ bởi Azure OpenAI

Chi tiết kiến trúc và triển khai cung cấp cái nhìn sâu sắc về cách xây dựng hệ thống đa tác nhân phức tạp với MCP làm lớp điều phối.

### 2. [Cập Nhật Mục Azure DevOps từ Dữ Liệu YouTube](./UpdateADOItemsFromYT.md)

Nghiên cứu trường hợp này trình bày ứng dụng thực tế của MCP để tự động hóa quy trình làm việc. Nó cho thấy cách sử dụng các công cụ MCP để:

- Trích xuất dữ liệu từ các nền tảng trực tuyến (YouTube)
- Cập nhật các mục công việc trong hệ thống Azure DevOps
- Tạo các quy trình tự động hóa có thể lặp lại
- Tích hợp dữ liệu giữa các hệ thống khác nhau

Ví dụ này minh họa cách các triển khai MCP tương đối đơn giản cũng có thể mang lại hiệu quả đáng kể bằng cách tự động hóa các tác vụ thường xuyên và cải thiện tính nhất quán dữ liệu giữa các hệ thống.

### 3. [Truy Xuất Tài Liệu Thời Gian Thực với MCP](./docs-mcp/README.md)

Nghiên cứu trường hợp này hướng dẫn bạn kết nối một client Python console với máy chủ Model Context Protocol (MCP) để truy xuất và ghi lại tài liệu Microsoft theo ngữ cảnh, thời gian thực. Bạn sẽ học cách:

- Kết nối với máy chủ MCP sử dụng client Python và SDK MCP chính thức
- Sử dụng client HTTP streaming để truy xuất dữ liệu hiệu quả, thời gian thực
- Gọi các công cụ tài liệu trên máy chủ và ghi phản hồi trực tiếp vào console
- Tích hợp tài liệu Microsoft cập nhật vào quy trình làm việc mà không cần rời khỏi terminal

Chương này bao gồm bài tập thực hành, mẫu mã nguồn tối giản và liên kết đến các tài nguyên bổ sung để học sâu hơn. Xem hướng dẫn chi tiết và mã nguồn trong chương liên kết để hiểu cách MCP có thể thay đổi việc truy cập tài liệu và năng suất của nhà phát triển trong môi trường console.

### 4. [Ứng Dụng Web Tạo Kế Hoạch Học Tương Tác với MCP](./docs-mcp/README.md)

Nghiên cứu trường hợp này trình bày cách xây dựng ứng dụng web tương tác sử dụng Chainlit và Model Context Protocol (MCP) để tạo kế hoạch học tập cá nhân hóa cho bất kỳ chủ đề nào. Người dùng có thể chỉ định một môn học (ví dụ "chứng chỉ AI-900") và thời gian học (ví dụ 8 tuần), ứng dụng sẽ cung cấp kế hoạch học từng tuần với nội dung đề xuất. Chainlit cung cấp giao diện chat đàm thoại, làm cho trải nghiệm trở nên sinh động và linh hoạt.

- Ứng dụng web đàm thoại được hỗ trợ bởi Chainlit
- Lời nhắc do người dùng điều khiển về chủ đề và thời lượng
- Đề xuất nội dung từng tuần sử dụng MCP
- Phản hồi thời gian thực, thích ứng trong giao diện chat

Dự án minh họa cách kết hợp AI đàm thoại và MCP để tạo ra công cụ giáo dục năng động, do người dùng điều khiển trong môi trường web hiện đại.

### 5. [Tài Liệu Trong Trình Soạn Thảo với MCP Server trên VS Code](./docs-mcp/README.md)

Nghiên cứu trường hợp này cho thấy cách bạn có thể đưa Microsoft Learn Docs trực tiếp vào môi trường VS Code sử dụng MCP server—không cần phải chuyển đổi tab trình duyệt nữa! Bạn sẽ thấy cách:

- Tìm kiếm và đọc tài liệu ngay trong VS Code qua bảng điều khiển MCP hoặc command palette
- Tham khảo tài liệu và chèn liên kết trực tiếp vào README hoặc các file markdown khóa học
- Sử dụng GitHub Copilot kết hợp MCP để có quy trình làm việc tài liệu và mã nguồn mượt mà, hỗ trợ AI
- Xác thực và nâng cao tài liệu với phản hồi thời gian thực và độ chính xác từ Microsoft
- Tích hợp MCP với quy trình làm việc GitHub để xác thực tài liệu liên tục

Việc triển khai bao gồm:
- Cấu hình `.vscode/mcp.json` mẫu để thiết lập dễ dàng
- Hướng dẫn dựa trên ảnh chụp màn hình về trải nghiệm trong trình soạn thảo
- Mẹo kết hợp Copilot và MCP để đạt hiệu suất tối đa

Kịch bản này phù hợp với tác giả khóa học, người viết tài liệu và nhà phát triển muốn tập trung làm việc trong trình soạn thảo khi làm việc với tài liệu, Copilot và công cụ xác thực—tất cả đều được hỗ trợ bởi MCP.

### 6. [Tạo MCP Server trên APIM](./apimsample.md)

Nghiên cứu trường hợp này cung cấp hướng dẫn từng bước cách tạo MCP server sử dụng Azure API Management (APIM). Nội dung bao gồm:
- Thiết lập MCP server trong Azure API Management
- Cung cấp các thao tác API như các công cụ MCP
- Cấu hình chính sách giới hạn tốc độ và bảo mật
- Kiểm thử MCP server bằng Visual Studio Code và GitHub Copilot

Ví dụ này minh họa cách tận dụng khả năng của Azure để tạo MCP server mạnh mẽ, có thể sử dụng trong nhiều ứng dụng, nâng cao tích hợp hệ thống AI với API doanh nghiệp.

## Kết Luận

Các nghiên cứu trường hợp này làm nổi bật tính linh hoạt và ứng dụng thực tiễn của Model Context Protocol trong các tình huống thực tế. Từ hệ thống đa tác nhân phức tạp đến các quy trình tự động hóa nhắm mục tiêu, MCP cung cấp một phương thức chuẩn hóa để kết nối hệ thống AI với công cụ và dữ liệu cần thiết nhằm tạo ra giá trị.

Qua việc nghiên cứu các triển khai này, bạn có thể nắm bắt các mẫu kiến trúc, chiến lược triển khai và thực hành tốt nhất để áp dụng vào dự án MCP của riêng bạn. Các ví dụ cho thấy MCP không chỉ là một khuôn khổ lý thuyết mà còn là giải pháp thực tiễn cho các thách thức kinh doanh thực tế.

## Tài Nguyên Bổ Sung

- [Azure AI Travel Agents GitHub Repository](https://github.com/Azure-Samples/azure-ai-travel-agents)
- [Azure DevOps MCP Tool](https://github.com/microsoft/azure-devops-mcp)
- [Playwright MCP Tool](https://github.com/microsoft/playwright-mcp)
- [Microsoft Docs MCP Server](https://github.com/MicrosoftDocs/mcp)
- [MCP Community Examples](https://github.com/microsoft/mcp)

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ nguyên bản của nó nên được coi là nguồn chính xác và đáng tin cậy. Đối với các thông tin quan trọng, nên sử dụng dịch vụ dịch thuật chuyên nghiệp bởi con người. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu nhầm hay giải thích sai nào phát sinh từ việc sử dụng bản dịch này.