# Karpathy-Inspired Claude Code Guidelines (andrej-karpathy-skills)

- **리포**: [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills)
- **⭐ Today**: 7,939 stars
- **태그**: `#ClaudeCode` `#CLAUDE.md` `#Karpathy` `#프롬프트엔지니어링`

## 상세 요약

Andrej Karpathy가 X에서 지적한 LLM 코딩의 핵심 문제점들을 해결하기 위한 **단일 CLAUDE.md ���일**. Claude Code의 행동을 개선하는 4가지 원칙을 제시한다.

### Karpathy가 지적한 문제
- "모델이 당신을 대신해 잘못된 가정을 하고 확인 없이 진행"
- "혼란을 관리하지 않고, 명확화를 구하지 않고, 불일치를 드러내지 않음"
- "코드와 API를 과도하게 복잡하게 만들고, 추상화를 비대화"
- "이해하지 못하는 코드와 주석을 부작용으로 변경/삭제"

### 4가지 원칙
1. **Think Before Coding**: 가정을 명시, 다중 해석 제시, 불확실하면 물어보기
2. **Simplicity First**: 요청받지 않은 기능/추상화/유연성 없이 최소 코드. "200줄이 50줄이 될 수 있다면 다시 작성"
3. **Surgical Changes**: 요청과 직접 관련된 줄만 변경. 인접 코드 "개선" 금지
4. **Goal-Driven Execution**: 성공 기준 정의, 검증될 때까지 반복

### 작성자
Forrest Chang, 새 프로젝트 [Multica](https://github.com/multica-ai/multica)(코딩 에이전트 실행/관리 오픈소스 플랫폼)도 공개.

## Soo에게 의미 있�� 이유
Claude Code를 실제 업무에서 사용할 때 코드 품질을 높이는 실용적인 가이드라인. CLAUDE.md 하나로 에이전트의 코딩 습관을 크게 개선할 수 있다는 점이 AInD 컨설팅에서 바로 적용 가능한 팁이다.
