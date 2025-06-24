<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "5384bbb2a92d00d5d7e66274dbe0331d",
  "translation_date": "2025-06-20T18:36:33+00:00",
  "source_file": "04-PracticalImplementation/README.md",
  "language_code": "th"
}
-->
# การใช้งานจริง

การใช้งานจริงคือจุดที่พลังของ Model Context Protocol (MCP) กลายเป็นสิ่งที่จับต้องได้ แม้ว่าการเข้าใจทฤษฎีและสถาปัตยกรรมเบื้องหลัง MCP จะมีความสำคัญ แต่คุณค่าที่แท้จริงจะเกิดขึ้นเมื่อคุณนำแนวคิดเหล่านี้ไปใช้ในการสร้าง ทดสอบ และนำโซลูชันไปใช้งานจริงเพื่อแก้ปัญหาในโลกแห่งความเป็นจริง บทนี้จะเชื่อมช่องว่างระหว่างความรู้เชิงแนวคิดกับการพัฒนาจริง โดยแนะนำขั้นตอนในการสร้างแอปพลิเคชันที่ใช้ MCP ให้เกิดขึ้นได้

ไม่ว่าคุณจะกำลังพัฒนาผู้ช่วยอัจฉริยะ การผสาน AI เข้ากับเวิร์กโฟลว์ธุรกิจ หรือสร้างเครื่องมือเฉพาะสำหรับการประมวลผลข้อมูล MCP มอบพื้นฐานที่ยืดหยุ่น การออกแบบที่ไม่ขึ้นกับภาษาโปรแกรมและ SDK อย่างเป็นทางการสำหรับภาษายอดนิยมช่วยให้เข้าถึงได้สำหรับนักพัฒนาหลากหลายกลุ่ม ด้วยการใช้ SDK เหล่านี้ คุณสามารถสร้างต้นแบบ ทดสอบ และขยายโซลูชันของคุณได้อย่างรวดเร็วในแพลตฟอร์มและสภาพแวดล้อมที่แตกต่างกัน

ในส่วนถัดไป คุณจะพบตัวอย่างการใช้งานจริง โค้ดตัวอย่าง และกลยุทธ์การนำไปใช้งานที่แสดงให้เห็นวิธีการใช้งาน MCP ใน C#, Java, TypeScript, JavaScript และ Python คุณจะได้เรียนรู้วิธีการดีบักและทดสอบเซิร์ฟเวอร์ MCP การจัดการ API และการนำโซลูชันขึ้นคลาวด์ด้วย Azure ทรัพยากรเหล่านี้ถูกออกแบบมาเพื่อเร่งการเรียนรู้ของคุณและช่วยให้คุณสร้างแอป MCP ที่มั่นคงและพร้อมใช้งานจริงได้อย่างมั่นใจ

## ภาพรวม

บทเรียนนี้เน้นไปที่แง่มุมการใช้งานจริงของ MCP ในหลายภาษาโปรแกรม เราจะสำรวจวิธีการใช้ MCP SDK ใน C#, Java, TypeScript, JavaScript และ Python เพื่อสร้างแอปพลิเคชันที่มั่นคง ดีบักและทดสอบเซิร์ฟเวอร์ MCP รวมถึงการสร้างทรัพยากร, prompts และเครื่องมือที่นำกลับมาใช้ใหม่ได้

## วัตถุประสงค์การเรียนรู้

เมื่อจบบทเรียนนี้ คุณจะสามารถ:
- นำโซลูชัน MCP ไปใช้งานโดยใช้ SDK อย่างเป็นทางการในหลายภาษาโปรแกรม
- ดีบักและทดสอบเซิร์ฟเวอร์ MCP อย่างเป็นระบบ
- สร้างและใช้งานฟีเจอร์ของเซิร์ฟเวอร์ (Resources, Prompts และ Tools)
- ออกแบบเวิร์กโฟลว์ MCP ที่มีประสิทธิภาพสำหรับงานที่ซับซ้อน
- ปรับแต่งการใช้งาน MCP เพื่อประสิทธิภาพและความน่าเชื่อถือ

## แหล่ง SDK อย่างเป็นทางการ

Model Context Protocol มี SDK อย่างเป็นทางการสำหรับหลายภาษา:

- [C# SDK](https://github.com/modelcontextprotocol/csharp-sdk)
- [Java SDK](https://github.com/modelcontextprotocol/java-sdk) 
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

## การใช้งาน MCP SDK

ส่วนนี้นำเสนอตัวอย่างการใช้งาน MCP ในหลายภาษาโปรแกรม คุณสามารถดูโค้ดตัวอย่างในไดเรกทอรี `samples` ที่จัดเรียงตามภาษา

### ตัวอย่างที่มีให้

รีโพสิตอรีประกอบด้วย [ตัวอย่างการใช้งาน](../../../04-PracticalImplementation/samples) ในภาษาต่อไปนี้:

- [C#](./samples/csharp/README.md)
- [Java](./samples/java/containerapp/README.md)
- [TypeScript](./samples/typescript/README.md)
- [JavaScript](./samples/javascript/README.md)
- [Python](./samples/python/README.md)

แต่ละตัวอย่างแสดงแนวคิดหลักของ MCP และรูปแบบการใช้งานสำหรับภาษานั้นๆ และระบบนิเวศของมัน

## ฟีเจอร์หลักของเซิร์ฟเวอร์

เซิร์ฟเวอร์ MCP สามารถใช้งานฟีเจอร์เหล่านี้ร่วมกันได้:

### Resources
Resources ให้บริบทและข้อมูลสำหรับผู้ใช้หรือโมเดล AI ใช้ประกอบการทำงาน:
- ที่เก็บเอกสาร
- ฐานความรู้
- แหล่งข้อมูลที่มีโครงสร้าง
- ระบบไฟล์

### Prompts
Prompts คือข้อความแม่แบบและเวิร์กโฟลว์สำหรับผู้ใช้:
- แม่แบบการสนทนาที่กำหนดไว้ล่วงหน้า
- รูปแบบการโต้ตอบที่มีการแนะนำ
- โครงสร้างบทสนทนาเฉพาะทาง

### Tools
Tools คือฟังก์ชันที่โมเดล AI สามารถเรียกใช้งานได้:
- ยูทิลิตี้ประมวลผลข้อมูล
- การเชื่อมต่อ API ภายนอก
- ความสามารถในการคำนวณ
- ฟังก์ชันการค้นหา

## ตัวอย่างการใช้งาน: C#

รีโพสิตอรี SDK C# อย่างเป็นทางการมีตัวอย่างการใช้งานหลายแบบที่แสดงแง่มุมต่างๆ ของ MCP:

- **Basic MCP Client**: ตัวอย่างง่ายๆ ที่แสดงวิธีสร้าง MCP client และเรียกใช้งานเครื่องมือ
- **Basic MCP Server**: การใช้งานเซิร์ฟเวอร์พื้นฐานที่ลงทะเบียนเครื่องมืออย่างง่าย
- **Advanced MCP Server**: เซิร์ฟเวอร์ที่มีฟีเจอร์ครบครันพร้อมการลงทะเบียนเครื่องมือ การตรวจสอบสิทธิ์ และการจัดการข้อผิดพลาด
- **ASP.NET Integration**: ตัวอย่างการผสานรวมกับ ASP.NET Core
- **Tool Implementation Patterns**: รูปแบบต่างๆ สำหรับการสร้างเครื่องมือที่มีความซับซ้อนหลากหลายระดับ

SDK MCP สำหรับ C# ยังอยู่ในช่วงพรีวิวและ API อาจมีการเปลี่ยนแปลง เราจะอัปเดตบล็อกนี้อย่างต่อเนื่องเมื่อ SDK พัฒนาไป

### ฟีเจอร์หลัก
- [C# MCP Nuget ModelContextProtocol](https://www.nuget.org/packages/ModelContextProtocol)

- การสร้าง [MCP Server แรกของคุณ](https://devblogs.microsoft.com/dotnet/build-a-model-context-protocol-mcp-server-in-csharp/)

สำหรับตัวอย่างการใช้งาน C# แบบครบถ้วน ให้เยี่ยมชม [รีโพสิตอรีตัวอย่าง C# SDK อย่างเป็นทางการ](https://github.com/modelcontextprotocol/csharp-sdk)

## ตัวอย่างการใช้งาน: Java Implementation

Java SDK มอบตัวเลือกการใช้งาน MCP ที่แข็งแกร่งพร้อมฟีเจอร์ระดับองค์กร

### ฟีเจอร์หลัก

- การผสานรวมกับ Spring Framework
- ความปลอดภัยของชนิดข้อมูลที่เข้มงวด
- รองรับโปรแกรมเชิงปฏิกิริยา (Reactive programming)
- การจัดการข้อผิดพลาดอย่างครบถ้วน

สำหรับตัวอย่างการใช้งาน Java แบบครบถ้วน ดูได้ที่ [Java sample](samples/java/containerapp/README.md) ในไดเรกทอรีตัวอย่าง

## ตัวอย่างการใช้งาน: JavaScript Implementation

JavaScript SDK มอบวิธีการใช้งาน MCP ที่เบาและยืดหยุ่น

### ฟีเจอร์หลัก

- รองรับ Node.js และเบราว์เซอร์
- API แบบ Promise
- การผสานรวมง่ายกับ Express และเฟรมเวิร์กอื่นๆ
- รองรับ WebSocket สำหรับการสตรีมข้อมูล

สำหรับตัวอย่างการใช้งาน JavaScript แบบครบถ้วน ดูได้ที่ [JavaScript sample](samples/javascript/README.md) ในไดเรกทอรีตัวอย่าง

## ตัวอย่างการใช้งาน: Python Implementation

Python SDK มอบวิธีการใช้งาน MCP ที่เป็นธรรมชาติสำหรับ Python พร้อมการผสานรวมกับเฟรมเวิร์ก ML ชั้นนำ

### ฟีเจอร์หลัก

- รองรับ async/await ด้วย asyncio
- การผสานรวมกับ Flask และ FastAPI
- การลงทะเบียนเครื่องมืออย่างง่าย
- การผสานรวมเนทีฟกับไลบรารี ML ยอดนิยม

สำหรับตัวอย่างการใช้งาน Python แบบครบถ้วน ดูได้ที่ [Python sample](samples/python/README.md) ในไดเรกทอรีตัวอย่าง

## การจัดการ API

Azure API Management เป็นคำตอบที่ดีสำหรับการรักษาความปลอดภัยของ MCP Servers แนวคิดคือการวาง Azure API Management ไว้หน้าตัว MCP Server ของคุณและให้มันจัดการฟีเจอร์ต่างๆ ที่คุณอาจต้องการ เช่น:

- การจำกัดอัตราการเรียกใช้งาน (rate limiting)
- การจัดการโทเคน
- การตรวจสอบและมอนิเตอร์
- การกระจายโหลด
- ความปลอดภัย

### ตัวอย่าง Azure

นี่คือตัวอย่าง Azure ที่ทำตามแนวทางนี้ เช่น [การสร้าง MCP Server และรักษาความปลอดภัยด้วย Azure API Management](https://github.com/Azure-Samples/remote-mcp-apim-functions-python)

ดูการไหลของการอนุญาตในภาพด้านล่าง:

![APIM-MCP](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/mcp-client-authorization.gif?raw=true) 

ในภาพนี้ เกิดเหตุการณ์ดังนี้:

- การตรวจสอบสิทธิ์และการอนุญาตเกิดขึ้นโดยใช้ Microsoft Entra
- Azure API Management ทำหน้าที่เป็นเกตเวย์และใช้โพลิซีเพื่อกำหนดทิศทางและจัดการทราฟฟิก
- Azure Monitor บันทึกคำขอทั้งหมดเพื่อนำไปวิเคราะห์เพิ่มเติม

#### การไหลของการอนุญาต

มาดูรายละเอียดการไหลของการอนุญาตกัน:

![Sequence Diagram](https://github.com/Azure-Samples/remote-mcp-apim-functions-python/blob/main/infra/app/apim-oauth/diagrams/images/mcp-client-auth.png?raw=true)

#### ข้อกำหนดการอนุญาต MCP

เรียนรู้เพิ่มเติมเกี่ยวกับ [ข้อกำหนดการอนุญาต MCP](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization#2-10-third-party-authorization-flow)

## การนำ Remote MCP Server ขึ้น Azure

มาลองดูว่าเราสามารถนำตัวอย่างที่กล่าวถึงไปใช้งานได้หรือไม่:

1. โคลนรีโพสิตอรี

    ```bash
    git clone https://github.com/Azure-Samples/remote-mcp-apim-functions-python.git
    cd remote-mcp-apim-functions-python
    ```

1. ลงทะเบียน `Microsoft.App` ด้วยคำสั่ง `az provider register --namespace Microsoft.App --wait` หรือ `Register-AzResourceProvider -ProviderNamespace Microsoft.App` และตรวจสอบสถานะการลงทะเบียนด้วย `(Get-AzResourceProvider -ProviderNamespace Microsoft.App).RegistrationState` หลังจากรอสักครู่

2. รันคำสั่ง [azd](https://aka.ms/azd) นี้เพื่อจัดเตรียมบริการ API Management, function app (พร้อมโค้ด) และทรัพยากร Azure อื่นๆ ที่จำเป็นทั้งหมด

    ```shell
    azd up
    ```

    คำสั่งนี้จะนำทรัพยากรทั้งหมดขึ้นบนคลาวด์ Azure

### การทดสอบเซิร์ฟเวอร์ด้วย MCP Inspector

1. ใน **หน้าต่างเทอร์มินัลใหม่** ให้ติดตั้งและรัน MCP Inspector

    ```shell
    npx @modelcontextprotocol/inspector
    ```

    คุณจะเห็นอินเทอร์เฟซคล้ายกับ:

    ![Connect to Node inspector](../../../translated_images/connect.141db0b2bd05f096fb1dd91273771fd8b2469d6507656c3b0c9df4b3c5473929.th.png) 

1. กด CTRL คลิกเพื่อโหลดเว็บแอป MCP Inspector จาก URL ที่แอปแสดง (เช่น http://127.0.0.1:6274/#resources)
1. ตั้งค่าประเภทการส่งข้อมูลเป็น `SSE` และ **Connect**:

    ```shell
    https://<apim-servicename-from-azd-output>.azure-api.net/mcp/sse
    ```

5. **แสดงรายการ Tools** คลิกที่เครื่องมือแล้ว **Run Tool**

ถ้าทุกขั้นตอนสำเร็จ คุณจะเชื่อมต่อกับเซิร์ฟเวอร์ MCP ได้และเรียกใช้งานเครื่องมือได้

## MCP servers สำหรับ Azure

[Remote-mcp-functions](https://github.com/Azure-Samples/remote-mcp-functions-dotnet): ชุดรีโพสิตอรีนี้เป็นเทมเพลตเริ่มต้นอย่างรวดเร็วสำหรับการสร้างและนำเซิร์ฟเวอร์ MCP ระยะไกลแบบกำหนดเองโดยใช้ Azure Functions กับ Python, C# .NET หรือ Node/TypeScript

ตัวอย่างเหล่านี้นำเสนอโซลูชันครบถ้วนที่ช่วยให้นักพัฒนาสามารถ:

- สร้างและรันบนเครื่องท้องถิ่น: พัฒนาและดีบักเซิร์ฟเวอร์ MCP บนเครื่องของคุณ
- นำขึ้น Azure: นำขึ้นคลาวด์ได้ง่ายด้วยคำสั่ง azd up เพียงคำสั่งเดียว
- เชื่อมต่อจากไคลเอนต์: เชื่อมต่อกับเซิร์ฟเวอร์ MCP จากไคลเอนต์ต่างๆ รวมถึงโหมด Copilot agent ของ VS Code และเครื่องมือ MCP Inspector

### ฟีเจอร์หลัก:

- ความปลอดภัยตั้งแต่การออกแบบ: เซิร์ฟเวอร์ MCP ปลอดภัยด้วยคีย์และ HTTPS
- ตัวเลือกการตรวจสอบสิทธิ์: รองรับ OAuth ผ่านระบบ auth ในตัวและ/หรือ API Management
- การแยกเครือข่าย: รองรับการแยกเครือข่ายด้วย Azure Virtual Networks (VNET)
- สถาปัตยกรรมแบบไร้เซิร์ฟเวอร์: ใช้ Azure Functions เพื่อประมวลผลแบบขยายตัวตามเหตุการณ์
- การพัฒนาท้องถิ่น: รองรับการพัฒนาและดีบักแบบครบวงจรบนเครื่อง
- การนำขึ้นใช้งานง่าย: กระบวนการนำขึ้นใช้งานไปยัง Azure ที่เรียบง่าย

รีโพสิตอรีมีไฟล์คอนฟิก โค้ดต้นฉบับ และคำจำกัดความโครงสร้างพื้นฐานที่จำเป็นทั้งหมด เพื่อให้คุณเริ่มต้นใช้งานเซิร์ฟเวอร์ MCP พร้อมใช้งานจริงได้อย่างรวดเร็ว

- [Azure Remote MCP Functions Python](https://github.com/Azure-Samples/remote-mcp-functions-python) - ตัวอย่างการใช้งาน MCP ด้วย Azure Functions และ Python

- [Azure Remote MCP Functions .NET](https://github.com/Azure-Samples/remote-mcp-functions-dotnet) - ตัวอย่างการใช้งาน MCP ด้วย Azure Functions และ C# .NET

- [Azure Remote MCP Functions Node/Typescript](https://github.com/Azure-Samples/remote-mcp-functions-typescript) - ตัวอย่างการใช้งาน MCP ด้วย Azure Functions และ Node/TypeScript

## สรุปประเด็นสำคัญ

- MCP SDK มอบเครื่องมือเฉพาะภาษาสำหรับการสร้างโซลูชัน MCP ที่มั่นคง
- กระบวนการดีบักและทดสอบเป็นสิ่งสำคัญสำหรับแอป MCP ที่เชื่อถือได้
- แม่แบบ prompt ที่นำกลับมาใช้ใหม่ช่วยให้การโต้ตอบกับ AI มีความสม่ำเสมอ
- เวิร์กโฟลว์ที่ออกแบบดีสามารถจัดการงานซับซ้อนได้โดยใช้เครื่องมือหลายตัว
- การใช้งาน MCP ต้องคำนึงถึงความปลอดภัย ประสิทธิภาพ และการจัดการข้อผิดพลาด

## แบบฝึกหัด

ออกแบบเวิร์กโฟลว์ MCP ที่ใช้งานได้จริงเพื่อแก้ปัญหาในโดเมนของคุณ:

1. ระบุเครื่องมือ 3-4 ตัวที่เป็นประโยชน์สำหรับการแก้ปัญหานี้
2. สร้างไดอะแกรมเวิร์กโฟลว์แสดงการทำงานร่วมกันของเครื่องมือเหล่านี้
3. พัฒนาเวอร์ชันพื้นฐานของเครื่องมือหนึ่งตัวโดยใช้ภาษาที่คุณถนัด
4. สร้างแม่แบบ prompt ที่ช่วยให้โมเดลใช้เครื่องมือของคุณได้อย่างมีประสิทธิภาพ

## แหล่งข้อมูลเพิ่มเติม


---

ถัดไป: [หัวข้อขั้นสูง](../05-AdvancedTopics/README.md)

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติ [Co-op Translator](https://github.com/Azure/co-op-translator) แม้เราจะพยายามให้มีความถูกต้องสูงสุด แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความคลาดเคลื่อนได้ เอกสารต้นฉบับในภาษาต้นทางถือเป็นแหล่งข้อมูลที่เชื่อถือได้ หากเป็นข้อมูลสำคัญ แนะนำให้ใช้บริการแปลโดยผู้เชี่ยวชาญด้านภาษามนุษย์ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความผิดที่เกิดขึ้นจากการใช้การแปลนี้