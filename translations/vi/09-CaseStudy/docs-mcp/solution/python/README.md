<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:31:22+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "vi"
}
-->
# Trình Tạo Kế Hoạch Học Tập với Chainlit & Microsoft Learn Docs MCP

## Yêu cầu trước

- Python 3.8 trở lên  
- pip (trình quản lý gói Python)  
- Kết nối Internet để truy cập máy chủ Microsoft Learn Docs MCP  

## Cài đặt

1. Sao chép kho lưu trữ này hoặc tải xuống các tệp dự án.  
2. Cài đặt các phụ thuộc cần thiết:  

   ```bash
   pip install -r requirements.txt
   ```  

## Cách sử dụng

### Tình huống 1: Truy vấn đơn giản đến Docs MCP  
Một ứng dụng dòng lệnh kết nối đến máy chủ Docs MCP, gửi câu hỏi và in kết quả ra màn hình.

1. Chạy script:  
   ```bash
   python scenario1.py
   ```  
2. Nhập câu hỏi về tài liệu của bạn tại dấu nhắc.

### Tình huống 2: Trình tạo kế hoạch học tập (ứng dụng web Chainlit)  
Giao diện web (sử dụng Chainlit) cho phép người dùng tạo kế hoạch học tập cá nhân theo tuần cho bất kỳ chủ đề kỹ thuật nào.

1. Khởi động ứng dụng Chainlit:  
   ```bash
   chainlit run scenario2.py
   ```  
2. Mở URL địa phương được cung cấp trong terminal (ví dụ: http://localhost:8000) trên trình duyệt của bạn.  
3. Trong cửa sổ chat, nhập chủ đề học và số tuần bạn muốn học (ví dụ: "Chứng chỉ AI-900, 8 tuần").  
4. Ứng dụng sẽ phản hồi với kế hoạch học tập từng tuần, bao gồm các liên kết đến tài liệu Microsoft Learn liên quan.

**Biến môi trường cần thiết:**  

Để sử dụng Tình huống 2 (ứng dụng web Chainlit với Azure OpenAI), bạn phải thiết lập các biến môi trường sau trong thư mục `.env` file in the `python`:  

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```  

Điền các giá trị này theo thông tin tài nguyên Azure OpenAI của bạn trước khi chạy ứng dụng.

> **Mẹo:** Bạn có thể dễ dàng triển khai mô hình riêng của mình bằng cách sử dụng [Azure AI Foundry](https://ai.azure.com/).

### Tình huống 3: Tài liệu trong trình soạn thảo với MCP Server trên VS Code

Thay vì chuyển tab trình duyệt để tìm kiếm tài liệu, bạn có thể đưa Microsoft Learn Docs trực tiếp vào VS Code bằng MCP server. Điều này cho phép bạn:  
- Tìm kiếm và đọc tài liệu ngay trong VS Code mà không cần rời môi trường lập trình.  
- Tham khảo tài liệu và chèn liên kết trực tiếp vào README hoặc các tệp khóa học.  
- Sử dụng GitHub Copilot kết hợp với MCP để có quy trình làm việc tài liệu AI liền mạch.

**Ví dụ về cách sử dụng:**  
- Nhanh chóng thêm liên kết tham khảo vào README khi viết tài liệu khóa học hoặc dự án.  
- Dùng Copilot để tạo mã và MCP để tìm và trích dẫn tài liệu liên quan ngay lập tức.  
- Giữ tập trung trong trình soạn thảo và tăng năng suất.

> [!IMPORTANT]  
> Đảm bảo bạn có một file [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

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
- `Cloud architecture, 9 weeks`

Các ví dụ này minh họa sự linh hoạt của ứng dụng cho các mục tiêu và khung thời gian học tập khác nhau.

## Tài liệu tham khảo

- [Chainlit Documentation](https://docs.chainlit.io/)  
- [MCP Documentation](https://github.com/MicrosoftDocs/mcp)

**Tuyên bố từ chối trách nhiệm**:  
Tài liệu này đã được dịch bằng dịch vụ dịch thuật AI [Co-op Translator](https://github.com/Azure/co-op-translator). Mặc dù chúng tôi cố gắng đảm bảo độ chính xác, xin lưu ý rằng các bản dịch tự động có thể chứa lỗi hoặc không chính xác. Tài liệu gốc bằng ngôn ngữ gốc của nó nên được xem là nguồn chính xác và có thẩm quyền. Đối với thông tin quan trọng, khuyến nghị sử dụng dịch vụ dịch thuật chuyên nghiệp do con người thực hiện. Chúng tôi không chịu trách nhiệm về bất kỳ sự hiểu lầm hoặc giải thích sai nào phát sinh từ việc sử dụng bản dịch này.