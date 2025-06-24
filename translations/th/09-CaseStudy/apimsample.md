<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "36de9fae488d6de554d969fe8e0801a8",
  "translation_date": "2025-06-20T19:20:25+00:00",
  "source_file": "09-CaseStudy/apimsample.md",
  "language_code": "th"
}
-->
# กรณีศึกษา: การเปิดเผย REST API ใน API Management เป็น MCP server

Azure API Management เป็นบริการที่ให้ Gateway อยู่บน API Endpoints ของคุณ วิธีการทำงานคือ Azure API Management ทำหน้าที่เป็นพร็อกซีอยู่หน้าของ API ของคุณและสามารถตัดสินใจว่าจะทำอย่างไรกับคำขอที่เข้ามา

เมื่อใช้บริการนี้ คุณจะได้ฟีเจอร์มากมาย เช่น:

- **ความปลอดภัย** คุณสามารถใช้ทุกอย่างตั้งแต่ API keys, JWT ไปจนถึง managed identity
- **การจำกัดอัตราการเรียกใช้งาน** ฟีเจอร์ที่ดีมากคือการกำหนดจำนวนการเรียกใช้งานที่ผ่านได้ในช่วงเวลาหนึ่ง ซึ่งช่วยให้ผู้ใช้ทุกคนได้รับประสบการณ์ที่ดีและยังช่วยให้บริการของคุณไม่ถูกคำขอท่วมท้น
- **การปรับขนาดและการกระจายโหลด** คุณสามารถตั้งค่า endpoints หลายตัวเพื่อกระจายโหลด และยังเลือกวิธีการ "load balance" ได้อีกด้วย
- **ฟีเจอร์ AI เช่น semantic caching, การจำกัดโทเค็น และการตรวจสอบโทเค็น** ฟีเจอร์เหล่านี้ช่วยเพิ่มความตอบสนองและช่วยให้คุณควบคุมการใช้โทเค็นได้ดีขึ้น [อ่านเพิ่มเติมที่นี่](https://learn.microsoft.com/en-us/azure/api-management/genai-gateway-capabilities)

## ทำไมต้อง MCP + Azure API Management?

Model Context Protocol กำลังกลายเป็นมาตรฐานสำหรับแอป AI ที่มีความสามารถแบบ agentic และวิธีการเปิดเผยเครื่องมือและข้อมูลในรูปแบบที่สม่ำเสมอ Azure API Management เป็นตัวเลือกที่เหมาะสมเมื่อคุณต้องการ "จัดการ" APIs MCP Servers มักจะผสานรวมกับ APIs อื่นๆ เพื่อแก้ไขคำขอไปยังเครื่องมือบางอย่าง ดังนั้นการรวม Azure API Management กับ MCP จึงสมเหตุสมผลมาก

## ภาพรวม

ในกรณีการใช้งานนี้ เราจะเรียนรู้วิธีเปิดเผย API endpoints เป็น MCP Server โดยการทำเช่นนี้ เราสามารถทำให้ endpoints เหล่านี้เป็นส่วนหนึ่งของแอป agentic ได้อย่างง่ายดาย พร้อมกับใช้ประโยชน์จากฟีเจอร์ของ Azure API Management

## ฟีเจอร์หลัก

- คุณเลือกวิธีการของ endpoint ที่ต้องการเปิดเผยเป็นเครื่องมือ
- ฟีเจอร์เพิ่มเติมที่คุณได้รับขึ้นอยู่กับการตั้งค่าในส่วน policy สำหรับ API ของคุณ แต่ที่นี่เราจะแสดงวิธีเพิ่มการจำกัดอัตราการเรียกใช้งาน

## ขั้นตอนเบื้องต้น: นำเข้า API

ถ้าคุณมี API ใน Azure API Management อยู่แล้ว ยอดเยี่ยม คุณสามารถข้ามขั้นตอนนี้ได้เลย หากยังไม่มี ลองดูลิงก์นี้ [การนำเข้า API ไปยัง Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish#import-and-publish-a-backend-api)

## การเปิดเผย API เป็น MCP Server

เพื่อเปิดเผย API endpoints ให้ทำตามขั้นตอนนี้:

1. ไปที่ Azure Portal ที่ <https://portal.azure.com/?Microsoft_Azure_ApiManagement=mcp>  
ไปยัง API Management instance ของคุณ

1. ในเมนูด้านซ้าย เลือก APIs > MCP Servers > + Create new MCP Server

1. ใน API ให้เลือก REST API ที่ต้องการเปิดเผยเป็น MCP server

1. เลือก API Operations หนึ่งหรือหลายรายการที่จะเปิดเผยเป็นเครื่องมือ คุณสามารถเลือกทั้งหมดหรือเลือกเฉพาะบางรายการได้

    ![เลือกวิธีการที่จะเปิดเผย](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/create-mcp-server-small.png)

1. เลือก **Create**

1. ไปที่เมนู **APIs** และ **MCP Servers** คุณจะเห็นดังนี้:

    ![ดู MCP Server ในหน้าหลัก](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-list.png)

    MCP server ถูกสร้างขึ้นและ API operations ถูกเปิดเผยเป็นเครื่องมือ MCP server จะแสดงในแผง MCP Servers คอลัมน์ URL แสดง endpoint ของ MCP server ที่คุณสามารถเรียกใช้งานเพื่อทดสอบหรือภายในแอปพลิเคชันของลูกค้าได้

## ตัวเลือก: การตั้งค่า policies

Azure API Management มีแนวคิดหลักคือ policies ซึ่งคุณสามารถตั้งกฎต่างๆ สำหรับ endpoints ของคุณ เช่น การจำกัดอัตราการเรียกใช้งาน หรือ semantic caching โดย policies เหล่านี้เขียนในรูปแบบ XML

นี่คือวิธีตั้งค่า policy เพื่อจำกัดอัตราการเรียกใช้งาน MCP Server ของคุณ:

1. ในพอร์ทัล ภายใต้ APIs ให้เลือก **MCP Servers**

1. เลือก MCP server ที่คุณสร้างขึ้น

1. ในเมนูด้านซ้าย ภายใต้ MCP ให้เลือก **Policies**

1. ในตัวแก้ไข policy ให้เพิ่มหรือแก้ไข policies ที่ต้องการใช้กับเครื่องมือของ MCP server policies จะถูกกำหนดในรูปแบบ XML เช่น คุณสามารถเพิ่ม policy เพื่อจำกัดการเรียกใช้งานเครื่องมือของ MCP server (ในตัวอย่างนี้ 5 ครั้งต่อ 30 วินาที ต่อที่อยู่ IP ของลูกค้า) ตัวอย่าง XML ที่จะตั้งค่า rate limit:

    ```xml
     <rate-limit-by-key calls="5" 
       renewal-period="30" 
       counter-key="@(context.Request.IpAddress)" 
       remaining-calls-variable-name="remainingCallsPerIP" 
    />
    ```

    นี่คือตัวอย่างภาพของตัวแก้ไข policy:

    ![ตัวแก้ไข policy](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-policies-small.png)
 
## ทดลองใช้งาน

มาทดสอบว่า MCP Server ของเราทำงานได้ตามที่ตั้งใจไว้

สำหรับการนี้ เราจะใช้ Visual Studio Code และ GitHub Copilot ในโหมด Agent เราจะเพิ่ม MCP server ลงในไฟล์ *mcp.json* ด้วยวิธีนี้ Visual Studio Code จะทำหน้าที่เป็นไคลเอนต์ที่มีความสามารถแบบ agentic และผู้ใช้จะสามารถพิมพ์คำสั่งเพื่อโต้ตอบกับเซิร์ฟเวอร์ดังกล่าวได้

มาดูวิธีเพิ่ม MCP server ใน Visual Studio Code:

1. ใช้คำสั่ง MCP: **Add Server จาก Command Palette**

1. เมื่อได้รับแจ้ง ให้เลือกประเภทเซิร์ฟเวอร์: **HTTP (HTTP หรือ Server Sent Events)**

1. ใส่ URL ของ MCP server ใน API Management ตัวอย่าง: **https://<apim-service-name>.azure-api.net/<api-name>-mcp/sse** (สำหรับ SSE endpoint) หรือ **https://<apim-service-name>.azure-api.net/<api-name>-mcp/mcp** (สำหรับ MCP endpoint) สังเกตความแตกต่างของการส่งข้อมูลคือ `/sse` or `/mcp`

1. ใส่ server ID ตามที่คุณต้องการ ค่านี้ไม่สำคัญมาก แต่จะช่วยให้คุณจำได้ว่า instance นี้คืออะไร

1. เลือกว่าจะบันทึกการตั้งค่าไว้ที่ workspace settings หรือ user settings

  - **Workspace settings** - การตั้งค่าเซิร์ฟเวอร์จะถูกบันทึกในไฟล์ .vscode/mcp.json ซึ่งใช้ได้เฉพาะใน workspace ปัจจุบัน

    *mcp.json*

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "sse",
            "url": "url-to-mcp-server/sse"
        }
    }
    ```

    หรือถ้าเลือกใช้ streaming HTTP เป็นการส่งข้อมูล จะมีความแตกต่างเล็กน้อย:

    ```json
    "servers": {
        "APIM petstore" : {
            "type": "http",
            "url": "url-to-mcp-server/mcp"
        }
    }
    ```

  - **User settings** - การตั้งค่าเซิร์ฟเวอร์จะถูกเพิ่มในไฟล์ *settings.json* ทั่วไปของคุณและจะใช้ได้ในทุก workspace การตั้งค่าจะมีลักษณะดังนี้:

    ![User setting](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-servers-visual-studio-code.png)

1. คุณยังต้องเพิ่มการตั้งค่า header เพื่อให้แน่ใจว่าการยืนยันตัวตนกับ Azure API Management ถูกต้อง โดยใช้ header ชื่อ **Ocp-Apim-Subscription-Key**

    - นี่คือตัวอย่างการเพิ่ม header ในการตั้งค่า:

    ![เพิ่ม header สำหรับการยืนยันตัวตน](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/mcp-server-with-header-visual-studio-code.png) ซึ่งจะทำให้มีหน้าต่างแจ้งให้คุณกรอกค่า API key ซึ่งคุณสามารถหาได้ใน Azure Portal สำหรับ Azure API Management instance ของคุณ

    - หากต้องการเพิ่มใน *mcp.json* แทน คุณสามารถเพิ่มได้ดังนี้:

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

### ใช้งานโหมด Agent

ตอนนี้เราตั้งค่าทุกอย่างเสร็จแล้ว ไม่ว่าจะใน settings หรือใน *.vscode/mcp.json* ลองทดสอบกันเลย

จะมีไอคอน Tools แบบนี้ ซึ่งแสดงเครื่องมือที่เปิดเผยจากเซิร์ฟเวอร์ของคุณ:

![เครื่องมือจากเซิร์ฟเวอร์](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/tools-button-visual-studio-code.png)

1. คลิกไอคอน tools แล้วคุณจะเห็นรายการเครื่องมือดังนี้:

    ![เครื่องมือ](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/select-tools-visual-studio-code.png)

1. พิมพ์คำสั่งในแชทเพื่อเรียกใช้เครื่องมือ เช่น หากคุณเลือกเครื่องมือสำหรับดูข้อมูลคำสั่งซื้อ คุณสามารถถามเอเจนต์เกี่ยวกับคำสั่งซื้อได้ ตัวอย่างคำสั่ง:

    ```text
    get information from order 2
    ```

    คุณจะเห็นไอคอนเครื่องมือขึ้นมาให้กดเพื่อเรียกใช้เครื่องมือ เลือกเพื่อดำเนินการต่อและคุณจะเห็นผลลัพธ์ดังนี้:

    ![ผลลัพธ์จากคำสั่ง](https://learn.microsoft.com/en-us/azure/api-management/media/export-rest-mcp-server/chat-results-visual-studio-code.png)

    **สิ่งที่คุณเห็นด้านบนขึ้นอยู่กับเครื่องมือที่คุณตั้งค่าไว้ แต่แนวคิดคือคุณจะได้รับการตอบกลับเป็นข้อความเหมือนตัวอย่าง**

## เอกสารอ้างอิง

นี่คือแหล่งข้อมูลเพิ่มเติม:

- [บทเรียนเกี่ยวกับ Azure API Management และ MCP](https://learn.microsoft.com/en-us/azure/api-management/export-rest-mcp-server)
- [ตัวอย่าง Python: การรักษาความปลอดภัย MCP servers ระยะไกลโดยใช้ Azure API Management (ทดลอง)](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

- [ห้องปฏิบัติการการอนุญาต MCP client](https://github.com/Azure-Samples/AI-Gateway/tree/main/labs/mcp-client-authorization)

- [ใช้ส่วนขยาย Azure API Management สำหรับ VS Code เพื่อนำเข้าและจัดการ APIs](https://learn.microsoft.com/en-us/azure/api-management/visual-studio-code-tutorial)

- [ลงทะเบียนและค้นหา MCP servers ระยะไกลใน Azure API Center](https://learn.microsoft.com/en-us/azure/api-center/register-discover-mcp-server)
- [AI Gateway](https://github.com/Azure-Samples/AI-Gateway) รีโปที่ยอดเยี่ยมซึ่งแสดงความสามารถ AI มากมายร่วมกับ Azure API Management
- [เวิร์กช็อป AI Gateway](https://azure-samples.github.io/AI-Gateway/) มีเวิร์กช็อปผ่าน Azure Portal ซึ่งเป็นวิธีที่ดีในการเริ่มต้นประเมินความสามารถ AI

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาด้วย AI [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้ความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้อง เอกสารต้นฉบับในภาษาดั้งเดิมถือเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญมนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดใด ๆ ที่เกิดจากการใช้การแปลนี้