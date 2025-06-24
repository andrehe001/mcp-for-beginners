<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "db532b1ec386c9ce38c791653dc3c881",
  "translation_date": "2025-06-21T14:36:50+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/scenario3/README.md",
  "language_code": "ko"
}
-->
# 시나리오 3: VS Code에서 MCP 서버를 활용한 에디터 내 문서

## 개요

이 시나리오에서는 MCP 서버를 사용해 Microsoft Learn Docs를 Visual Studio Code 환경 안으로 직접 불러오는 방법을 배웁니다. 문서 검색을 위해 브라우저 탭을 계속 전환하는 대신, 에디터 내에서 공식 문서를 검색하고 참고할 수 있습니다. 이 방식은 작업 흐름을 간소화하고 집중력을 유지하게 해주며, GitHub Copilot과 같은 도구와도 원활하게 통합됩니다.

- 코딩 환경을 벗어나지 않고 VS Code 내에서 문서를 검색하고 읽기
- README나 강의 자료에 문서 링크를 바로 삽입하여 참고
- GitHub Copilot과 MCP를 함께 사용해 AI 기반 문서 작업 흐름 구현

## 학습 목표

이 장을 마치면 VS Code 내에서 MCP 서버를 설정하고 활용해 문서와 개발 작업 흐름을 향상시키는 방법을 알게 됩니다. 다음을 할 수 있습니다:

- MCP 서버를 문서 조회용으로 워크스페이스에 구성하기
- VS Code 내에서 문서를 검색하고 바로 삽입하기
- GitHub Copilot과 MCP를 결합해 생산성 높은 AI 지원 작업 흐름 구축하기

이 기술들은 개발자나 기술 문서 작성자가 집중력을 유지하고 문서 품질을 높이며 생산성을 향상하는 데 도움을 줄 것입니다.

## 솔루션

에디터 내 문서 접근을 위해 MCP 서버를 VS Code와 GitHub Copilot과 통합하는 일련의 단계를 따라갑니다. 이 솔루션은 강의 저자, 문서 작성자, 개발자가 에디터에 집중하면서 문서와 Copilot을 함께 활용하기에 이상적입니다.

- 강의나 프로젝트 문서 작성 중 README에 참고 링크를 빠르게 추가
- Copilot으로 코드를 생성하고 MCP로 관련 문서를 즉시 찾아 인용
- 에디터 내 집중력을 유지하며 생산성 향상

### 단계별 가이드

시작하려면 다음 단계를 따르세요. 각 단계별로 assets 폴더에 있는 스크린샷을 추가해 과정을 시각적으로 보여줄 수 있습니다.

1. **MCP 구성 추가하기:**
   프로젝트 루트에 `.vscode/mcp.json` 파일을 만들고 다음 구성을 추가하세요:
   ```json
   {
     "servers": {
       "LearnDocsMCP": {
         "url": "https://learn.microsoft.com/api/mcp"
       }
     }
   }
   ```
   이 구성은 VS Code가 [`Microsoft Learn Docs MCP server`](https://github.com/MicrosoftDocs/mcp)에 연결하는 방법을 알려줍니다.
   
   ![Step 1: Add mcp.json to .vscode folder](../../../../../../translated_images/step1-mcp-json.c06a007fccc3edfaf0598a31903c9ec71476d9fd3ae6c1b2b4321fd38688ca4b.ko.png)
    
2. **GitHub Copilot Chat 패널 열기:**
   GitHub Copilot 확장 프로그램이 설치되어 있지 않다면 VS Code의 확장 뷰에서 설치하세요. [Visual Studio Code Marketplace](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat)에서 직접 다운로드할 수 있습니다. 이후 사이드바에서 Copilot Chat 패널을 엽니다.

   ![Step 2: Open Copilot Chat panel](../../../../../../translated_images/step2-copilot-panel.f1cc86e9b9b8cd1a85e4df4923de8bafee4830541ab255e3c90c09777fed97db.ko.png)

3. **에이전트 모드 활성화 및 도구 확인:**
   Copilot Chat 패널에서 에이전트 모드를 활성화하세요.

   ![Step 3: Enable agent mode and verify tools](../../../../../../translated_images/step3-agent-mode.cdc32520fd7dd1d149c3f5226763c1d85a06d3c041d4cc983447625bdbeff4d4.ko.png)

   에이전트 모드를 켠 후 MCP 서버가 사용 가능한 도구 목록에 있는지 확인합니다. 이렇게 하면 Copilot 에이전트가 문서 서버에 접속해 관련 정보를 가져올 수 있습니다.
   
   ![Step 3: Verify MCP server tool](../../../../../../translated_images/step3-verify-mcp-tool.76096a6329cbfecd42888780f322370a0d8c8fa003ed3eeb7ccd23f0fc50c1ad.ko.png)

4. **새 채팅 시작 및 에이전트에 질문하기:**
   Copilot Chat 패널에서 새 채팅을 열고 문서 관련 질문을 에이전트에 전달하세요. 에이전트는 MCP 서버를 이용해 Microsoft Learn 문서를 직접 에디터에 표시합니다.

   - *"주제 X에 대한 학습 계획을 작성하려고 합니다. 8주 동안 공부할 예정인데, 각 주차별로 학습할 내용을 제안해 주세요."*

   ![Step 4: Prompt the agent in chat](../../../../../../translated_images/step4-prompt-chat.12187bb001605efc5077992b621f0fcd1df12023c5dce0464f8eb8f3d595218f.ko.png)

5. **실시간 질의:**

   > Azure AI Foundry Discord의 [#get-help](https://discord.gg/D6cRhjHWSC) 섹션에서 실제 질의를 가져왔습니다 ([원본 메시지 보기](https://discord.com/channels/1113626258182504448/1385498306720829572)):
   
   *"Azure AI Foundry에서 개발된 AI 에이전트로 다중 에이전트 솔루션을 배포하는 방법에 대한 답변을 찾고 있습니다. Copilot Studio 채널 같은 직접적인 배포 방식이 없는 것 같은데, 기업 사용자가 상호작용하며 작업을 수행할 수 있도록 배포하는 다양한 방법은 무엇인가요? 여러 글에서는 Azure Bot 서비스를 MS Teams와 Azure AI Foundry 에이전트 사이의 다리 역할로 사용할 수 있다고 하는데, Azure Function을 통해 Orchestrator Agent에 연결하는 Azure Bot을 설정하는 방식이 효과적인지, 아니면 다중 에이전트 솔루션 내 각 AI 에이전트마다 Bot Framework에서 오케스트레이션을 수행하는 Azure Function을 별도로 만들어야 하는지 궁금합니다. 다른 제안도 환영합니다."*

   ![Step 5: Live queries](../../../../../../translated_images/step5-live-queries.49db3e4a50bea27327e3cb18c24d263b7d134930d78e7392f9515a1c00264a7f.ko.png)

   에이전트는 관련 문서 링크와 요약을 제공하며, 이를 마크다운 파일에 바로 삽입하거나 코드 참고 자료로 사용할 수 있습니다.

### 예제 질의

다음은 시도해볼 수 있는 몇 가지 예제 질의입니다. 이 질의들은 MCP 서버와 Copilot이 VS Code를 벗어나지 않고도 즉각적이고 문맥에 맞는 문서와 참고 자료를 제공하는 방식을 보여줍니다:

- "Azure Functions 트리거 사용 방법을 보여줘."
- "Azure Key Vault 공식 문서 링크를 삽입해줘."
- "Azure 리소스 보안 모범 사례는 무엇인가?"
- "Azure AI 서비스 빠른 시작 가이드를 찾아줘."

이 질의들은 MCP 서버와 Copilot이 함께 작동해 VS Code 내에서 즉시 문서와 참고 자료를 제공하는 과정을 시연합니다.

---

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 노력하고 있으나, 자동 번역에는 오류나 부정확한 부분이 있을 수 있음을 양지해 주시기 바랍니다. 원문 문서는 해당 언어의 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 본 번역의 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.