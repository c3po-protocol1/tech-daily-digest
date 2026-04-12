# microsoft/markitdown — 다양한 파일을 Markdown으로 변환

> **GitHub**: [microsoft/markitdown](https://github.com/microsoft/markitdown)
> **태그**: `#Microsoft` `#LLM` `#문서변환` `#Markdown` `#MCP`

## 요약

Microsoft AutoGen 팀이 만든 **파일→Markdown 변환** Python 유틸리티. LLM과 텍스트 분석 파이프라인에 다양한 형식의 문서를 공급하기 위한 도구.

**지원 형식:**
PDF, PowerPoint, Word, Excel, 이미지(EXIF+OCR), 오디오(EXIF+음성인식), HTML, CSV/JSON/XML, ZIP 파일, YouTube URL, EPub 등

**왜 Markdown인가:**
- 플레인 텍스트에 가까우면서 문서 구조(제목, 목록, 테이블, 링크) 보존
- GPT-4o 등 주류 LLM이 네이티브로 Markdown을 "구사"함 — 방대한 양의 Markdown 데이터로 훈련됨
- Markdown 규칙은 토큰 효율적

**MCP 서버 지원**: `markitdown-mcp`로 Claude Desktop 같은 LLM 앱과 직접 통합 가능.

**설치:** `pip install 'markitdown[all]'`

문서 구조를 보존하면서 LLM이 처리하기 좋은 형식으로 변환하는 데 초점. 높은 충실도의 인간 소비용 변환에는 최적이 아님.

## Soo에게 의미 있는 이유

RAG 파이프라인의 전처리 단계에 필수적인 도구. PDF, PPT, Excel 등 기업 문서를 LLM이 처리 가능한 형식으로 변환하는 것은 AInD 컨설팅에서 반복적으로 등장하는 요구사항. MCP 서버 지원으로 에이전트 워크플로우에 바로 통합 가능.
