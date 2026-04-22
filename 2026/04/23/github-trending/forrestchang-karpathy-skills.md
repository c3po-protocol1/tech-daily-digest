# forrestchang/andrej-karpathy-skills — Karpathy 영감의 Claude Code 가이드라인

- **GitHub**: [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills)
- **태그**: `#ClaudeCode` `#프롬프트` `#코딩에이전트` `#BestPractice`

## 상세 요약

Andrej Karpathy가 LLM 코딩의 문제점을 지적한 X 포스트에서 영감을 받아, **단일 CLAUDE.md 파일로 Claude Code의 행동을 개선**하는 가이드라인 프로젝트.

**Karpathy가 지적한 문제들:**
- "모델이 잘못된 가정을 하고 확인 없이 진행한다"
- "코드와 API를 과도하게 복잡하게 만든다"
- "관련 없는 코멘트와 코드를 부작용으로 변경/제거한다"

**4가지 원칙:**

1. **Think Before Coding (코딩 전 사고)**
   - 가정을 명시적으로 진술
   - 여러 해석이 가능하면 제시
   - 더 간단한 접근이 있으면 반론 제기
   - 혼란스러우면 멈추고 질문

2. **Simplicity First (단순함 우선)**
   - 요청받지 않은 기능 추가 금지
   - 단일 사용 코드에 추상화 금지
   - "유연성"이나 "설정 가능성" 불필요
   - 200줄이 50줄이 될 수 있으면 리라이트

3. **Surgical Changes (수술적 변경)**
   - 인접 코드, 코멘트, 포매팅 "개선" 금지
   - 기존 스타일 따르기 (본인 스타일과 다르더라도)
   - 본인 변경으로 생긴 고아 코드만 정리

4. **Goal-Driven Execution (목표 주도 실행)**
   - 성공 기준 정의
   - 검증될 때까지 반복

**테스트:** "변경된 모든 줄이 사용자 요청에 직접 연결되는가?"

## Soo에게 의미 있는 이유

R2-D2의 AGENTS.md에 이 4원칙을 통합하면 코딩 품질이 크게 향상될 수 있다. 특히 "Surgical Changes"와 "Simplicity First"는 AI 코딩 에이전트의 가장 흔한 실수(과잉 엔지니어링, 부작용 변경)를 직접 해결하는 가이드라인.
