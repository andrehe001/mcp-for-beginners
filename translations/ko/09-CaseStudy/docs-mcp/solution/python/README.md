<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a05fb941810e539147fec53aaadbb6fd",
  "translation_date": "2025-06-21T14:27:54+00:00",
  "source_file": "09-CaseStudy/docs-mcp/solution/python/README.md",
  "language_code": "ko"
}
-->
# Chainlit 및 Microsoft Learn Docs MCP를 활용한 학습 계획 생성기

## 사전 준비 사항

- Python 3.8 이상
- pip (파이썬 패키지 관리자)
- Microsoft Learn Docs MCP 서버에 연결할 수 있는 인터넷 접속

## 설치

1. 이 저장소를 클론하거나 프로젝트 파일을 다운로드하세요.
2. 필요한 의존성을 설치하세요:

   ```bash
   pip install -r requirements.txt
   ```

## 사용법

### 시나리오 1: Docs MCP에 간단한 쿼리 보내기
Docs MCP 서버에 연결하여 쿼리를 전송하고 결과를 출력하는 커맨드라인 클라이언트입니다.

1. 스크립트를 실행하세요:
   ```bash
   python scenario1.py
   ```
2. 프롬프트에 문서 관련 질문을 입력하세요.

### 시나리오 2: 학습 계획 생성기 (Chainlit 웹 앱)
Chainlit을 사용한 웹 기반 인터페이스로, 사용자가 기술 주제에 대해 주차별 맞춤 학습 계획을 생성할 수 있습니다.

1. Chainlit 앱을 시작하세요:
   ```bash
   chainlit run scenario2.py
   ```
2. 터미널에 표시된 로컬 URL(예: http://localhost:8000)을 브라우저에서 열어주세요.
3. 채팅창에 학습 주제와 원하는 학습 기간(예: "AI-900 certification, 8 weeks")을 입력하세요.
4. 앱이 주차별 학습 계획과 관련된 Microsoft Learn 문서 링크를 응답합니다.

**필요한 환경 변수:**

시나리오 2 (Azure OpenAI와 함께하는 Chainlit 웹 앱)를 사용하려면 `.env` file in the `python` 디렉터리에 다음 환경 변수를 설정해야 합니다:

```
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME=
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_VERSION=
```

앱 실행 전에 Azure OpenAI 리소스 정보를 해당 값에 채워 넣으세요.

> **팁:** [Azure AI Foundry](https://ai.azure.com/)를 사용하면 자신만의 모델을 쉽게 배포할 수 있습니다.

### 시나리오 3: VS Code 내에서 MCP 서버를 활용한 문서 편집기

브라우저 탭을 전환하지 않고도 Microsoft Learn Docs를 VS Code 안에서 직접 사용할 수 있습니다. 이를 통해:
- 코딩 환경을 벗어나지 않고도 VS Code 내에서 문서를 검색하고 읽을 수 있습니다.
- 문서 참조 및 링크를 README나 강의 파일에 바로 삽입할 수 있습니다.
- GitHub Copilot과 MCP를 함께 사용하여 AI 기반 문서 작업 흐름을 원활하게 할 수 있습니다.

**활용 예시:**
- 강의나 프로젝트 문서를 작성하면서 README에 참고 링크를 빠르게 추가할 때
- Copilot으로 코드를 생성하고 MCP로 관련 문서를 즉시 찾아 인용할 때
- 에디터 내에서 집중력을 유지하며 생산성을 높이고 싶을 때

> [!IMPORTANT]
> 유효한 [`mcp.json`](../../../../../../09-CaseStudy/docs-mcp/solution/scenario3/mcp.json) configuration in your workspace (location is `.vscode/mcp.json`).

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

이 예시들은 다양한 학습 목표와 기간에 맞춘 앱의 유연성을 보여줍니다.

## 참고 자료

- [Chainlit Documentation](https://docs.chainlit.io/)
- [MCP Documentation](https://github.com/MicrosoftDocs/mcp)

**면책 조항**:  
이 문서는 AI 번역 서비스 [Co-op Translator](https://github.com/Azure/co-op-translator)를 사용하여 번역되었습니다. 정확성을 위해 최선을 다하고 있으나, 자동 번역은 오류나 부정확한 부분이 있을 수 있음을 양지해 주시기 바랍니다. 원문 문서가 권위 있는 출처로 간주되어야 합니다. 중요한 정보의 경우, 전문적인 인간 번역을 권장합니다. 본 번역 사용으로 인해 발생하는 오해나 잘못된 해석에 대해 당사는 책임을 지지 않습니다.