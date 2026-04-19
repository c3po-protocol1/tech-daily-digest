# 🔥 MarkItDown — Microsoft의 다양한 파일→Markdown 변환 도구

- **출처**: [GitHub](https://github.com/microsoft/markitdown)
- **태그**: `#conversion` `#markdown` `#LLM` `#Microsoft` `#MCP`

## 상세 요약

Microsoft AutoGen 팀이 만든 경량 Python 유틸리티로, 다양한 파일 형식을 LLM 및 텍스트 분석 파이프라인용 Markdown으로 변환한다.

**지원 파일 형식:**
- PDF, PowerPoint, Word, Excel
- 이미지 (EXIF 메타데이터 + OCR)
- 오디오 (EXIF 메타데이터 + 음성 전사)
- HTML, CSV, JSON, XML
- ZIP 파일 (내용 반복 처리)
- YouTube URL
- EPub, 기타

**왜 Markdown인가:**
- Markdown은 평문에 가까우면서도 문서 구조(제목, 목록, 표, 링크)를 표현 가능
- GPT-4o 같은 주류 LLM이 네이티브로 Markdown을 "구사" — 방대한 Markdown 텍스트로 훈련되었기 때문
- 토큰 효율이 매우 높음

**최신 기능:**
- **MCP 서버**: Claude Desktop 같은 LLM 앱과 직접 통합 가능
- 선택적 의존성 그룹: `pip install 'markitdown[all]'`
- 스트림 기반 처리 (임시 파일 생성 없음)

**설계 철학:**
- textract와 유사하지만 Markdown 구조 보존에 집중
- 인간용 고화질 변환보다는 텍스트 분석 도구 소비용에 최적화

## Soo에게 의미 있는 이유

LLM 파이프라인에서 "문서 입력"은 가장 기본적이면서 중요한 단계다. MarkItDown은 RAG 파이프라인, 문서 분석 에이전트, MCP 서버 등 다양한 AI 시스템의 전처리 레이어로 활용 가능하며, AInD 컨설팅에서 "비정형 문서를 AI가 이해 가능한 형태로 변환하는 방법"을 설명할 때 핵심 도구로 소개할 수 있다.
