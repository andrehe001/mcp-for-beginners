<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:30:13+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "th"
}
-->
# ตัวสร้างแผนการเรียนรู้ด้วย Chainlit & Microsoft Learn Docs MCP

## สิ่งที่ต้องเตรียมก่อน

- Python 3.8 ขึ้นไป
- pip (ตัวจัดการแพ็กเกจของ Python)
- การเชื่อมต่ออินเทอร์เน็ตเพื่อเข้าถึงเซิร์ฟเวอร์ Microsoft Learn Docs MCP

## การติดตั้ง

1. โคลนที่เก็บโค้ดนี้หรือติดตั้งไฟล์โปรเจกต์
2. ติดตั้ง dependencies ที่จำเป็น:

   ```bash
   pip install -r requirements.txt
   ```

## วิธีใช้งาน

### กรณีที่ 1: คำถามง่ายๆ ไปยัง Docs MCP  
ไคลเอนต์บนคอมมานด์ไลน์ที่เชื่อมต่อกับเซิร์ฟเวอร์ Docs MCP ส่งคำถามและแสดงผลลัพธ์

1. รันสคริปต์:
   ```bash
   python scenario1.py
   ```
2. พิมพ์คำถามเกี่ยวกับเอกสารที่ต้องการในพรอมต์

### กรณีที่ 2: ตัวสร้างแผนการเรียนรู้ (แอปเว็บ Chainlit)  
อินเทอร์เฟซบนเว็บ (ใช้ Chainlit) ที่ช่วยให้ผู้ใช้สร้างแผนการเรียนรู้รายสัปดาห์แบบส่วนตัวสำหรับหัวข้อทางเทคนิคใดก็ได้

1. เริ่มแอป Chainlit:
   ```bash
   chainlit run scenario2.py
   ```
2. เปิด URL ที่แสดงในเทอร์มินัลของคุณ (เช่น http://localhost:8000) บนเว็บเบราว์เซอร์
3. ในหน้าต่างแชท พิมพ์หัวข้อที่ต้องการเรียนและจำนวนสัปดาห์ที่ต้องการศึกษา (เช่น "AI-900 certification, 8 weeks")
4. แอปจะแสดงแผนการเรียนรายสัปดาห์ พร้อมลิงก์ไปยังเอกสาร Microsoft Learn ที่เกี่ยวข้อง

**ตัวแปรสภาพแวดล้อมที่ต้องตั้งค่า:**

เพื่อใช้งานกรณีที่ 2 (แอปเว็บ Chainlit ร่วมกับ Azure OpenAI) คุณต้องตั้งค่าตัวแปรสภาพแวดล้อมในไดเรกทอรี `.env` file in the `python` ดังนี้:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

กรอกข้อมูลของ Azure OpenAI ของคุณก่อนรันแอป

> **Tip:** คุณสามารถปรับใช้โมเดลของตัวเองได้ง่าย ๆ ด้วย [Azure AI Foundry](https://ai.azure.com/)

### กรณีที่ 3: ดูเอกสารในตัวแก้ไขด้วย MCP Server บน VS Code

แทนที่จะสลับแท็บเบราว์เซอร์เพื่อค้นหาเอกสาร คุณสามารถนำ Microsoft Learn Docs เข้ามาใน VS Code ได้โดยตรงผ่าน MCP server ซึ่งช่วยให้คุณ:  
- ค้นหาและอ่านเอกสารใน VS Code โดยไม่ต้องออกจากสภาพแวดล้อมการเขียนโค้ด  
- อ้างอิงเอกสารและแทรกลิงก์เข้าไปใน README หรือไฟล์คอร์สได้ทันที  
- ใช้ GitHub Copilot ร่วมกับ MCP เพื่อการทำงานเอกสารด้วย AI ที่ราบรื่น

**ตัวอย่างการใช้งาน:**  
- เพิ่มลิงก์อ้างอิงใน README ได้อย่างรวดเร็วขณะเขียนเอกสารคอร์สหรือโปรเจกต์  
- ใช้ Copilot สร้างโค้ดและ MCP ค้นหาเอกสารที่เกี่ยวข้องทันที  
- โฟกัสกับตัวแก้ไขและเพิ่มประสิทธิภาพการทำงาน

> [!IMPORTANT]  
> ตรวจสอบให้แน่ใจว่าคุณมีไฟล์ [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

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

ตัวอย่างเหล่านี้แสดงให้เห็นถึงความยืดหยุ่นของแอปสำหรับเป้าหมายการเรียนรู้และระยะเวลาที่หลากหลาย

## แหล่งอ้างอิง

- [Chainlit Documentation](https://docs.chainlit.io/)
- [MCP Documentation](https://github.com/MicrosoftDocs/mcp)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้มีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาต้นฉบับถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้การแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดขึ้นจากการใช้การแปลนี้