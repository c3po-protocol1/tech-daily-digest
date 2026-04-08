# AutoBe vs Claude Code — 3세대 코딩 에이전트 개발자의 소스코드 분석

- **출처:** [dev.to/samchon](https://dev.to/samchon/autobe-vs-claude-code-3rd-gen-coding-agent-developers-review-of-the-leaked-source-code-313b)
- **GeekNews:** [topic?id=28315](https://news.hada.io/topic?id=28315) (4 points)
- **태그:** `#ClaudeCode` `#코딩에이전트` `#아키텍처분석` `#AutoBe` `#FunctionCalling`

## 상세 요약

백엔드 코딩 에이전트 AutoBe 개발자가 유출된 Claude Code 소스코드 512,000줄을 분석하고 자신의 3세대 접근법과 비교한 기술 분석 글.

### Claude Code 내부 아키텍처 (유출 기반)
- **while(true) + 40개 도구 자율 선택:** 7가지 복구 경로를 가진 무한 루프 기반 에이전트
- **4단계 컨텍스트 압축:** 토큰 소비 최적화
- **23가지 보안 체크 카테고리:** BashTool만 400KB 이상의 보안 코드
- **2세대 패러다임:** 사람이 주도, AI가 보조

### AutoBe의 3세대 접근법
- **4개 AST × 4단계 컴파일러 × 자가 수정 루프:** Function Calling Harness 기법
- **"AI가 생성, 컴파일러가 검증":** 3세대 패러다임
- **작은 모델도 대형 모델 수준:** qwen3.5-35b-a3b로도 100% 컴파일 성공

### 핵심 통찰
- **0.95^400 ≈ 0%:** 400개 도구 각각 95% 성공률이면 전체 파이프라인 성공 확률은 사실상 0%. 3세대로의 전환은 모델 성능이 아니라 아키텍처 문제
- **독립적으로 같은 결론:** "선택지를 줄이고, 작업자에게 자족적 컨텍스트를 제공하라"
- **공존 미래:** AutoBe가 초기 빌드, Claude Code가 유지보수 담당

## Soo에게 의미 있는 이유
코딩 에이전트 아키텍처의 세대론을 이해하는 핵심 자료. "도구 수 × 성공률 = 전체 실패율" 공식은 에이전트 시스템 설계의 근본 원칙.
