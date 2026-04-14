# 🔥 forrestchang/andrej-karpathy-skills — Karpathy 영감 Claude Code 가이드라인

- **레포**: [github.com/forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills)
- **태그**: #ClaudeCode #CLAUDE.md #프롬프트엔지니어링 #BestPractice
- 🔥 2일 이상 연속 트렌딩

## 상세 요약

Andrej Karpathy의 LLM 코딩 함정 관찰에서 파생된 단일 `CLAUDE.md` 파일로, Claude Code의 코딩 행동을 개선하기 위한 4가지 원칙을 정의한다.

**Karpathy가 지적한 문제들:**
- 모델이 사용자 대신 잘못된 가정을 하고 확인 없이 진행
- 코드를 과도하게 복잡화, 추상화 남용, 데드 코드 방치
- 이해하지 못하는 코드/주석을 부수효과로 변경/삭제

**4가지 원칙:**
1. **Think Before Coding**: 가정을 명시적으로 밝히고, 모호하면 질문하고, 더 간단한 접근이 있으면 제안
2. **Simplicity First**: 요청받지 않은 기능, 일회용 코드의 추상화, 불가능한 시나리오의 에러 핸들링 금지. 200줄이 50줄로 가능하면 재작성
3. **Surgical Changes**: 필요한 것만 수정. 이해하지 못하는 기존 코드에 손대지 않음
4. **Goal-Driven Execution**: 테스트 우선, 검증 가능한 성공 기준 설정

## Soo에게 의미 있는 이유

AI 코딩 에이전트의 품질을 CLAUDE.md 같은 지시 파일로 개선하는 패턴이 표준화되고 있다. 이 원칙들은 R2-D2에게도 적용 가능하며, AInD 프로젝트에서 코딩 에이전트 품질 관리 가이드라인으로 참고할 만하다.
