# 🔄 Ralph — 자율 AI 코딩 루프

- **저장소**: [snarktank/ralph](https://github.com/snarktank/ralph)
- **태그**: `#AI코딩` `#자율에이전트` `#ClaudeCode` `#Amp`

## 상세 요약

Ralph는 AI 코딩 도구(Amp 또는 Claude Code)를 **PRD(제품 요구사항 문서)의 모든 항목이 완료될 때까지 반복 실행**하는 자율 에이전트 루프다. Geoffrey Huntley의 Ralph 패턴에 기반한다.

**핵심 원리:**
- 각 반복은 **깨끗한 컨텍스트**의 새 인스턴스
- 메모리는 git 이력, `progress.txt`, `prd.json`으로 유지
- PRD를 JSON으로 변환 → 작업 항목 추적 → 완료까지 반복

**설치 방법:** 3가지 옵션
1. 프로젝트에 스크립트 복사
2. Amp/Claude 글로벌 스킬로 설치
3. Claude Code 마켓플레이스로 설치 (`/prd`, `/ralph` 스킬)

**자동 호출:** "create a prd", "convert this prd", "turn into ralph format" 등의 자연어로 스킬 자동 감지

이 패턴은 컨텍스트 길이 제한을 우회하면서도 장기 실행 작업을 처리할 수 있다는 점에서 주목할 만하다.

## Soo에게 의미 있는 이유

"PRD → 자동 구현"이라는 패턴은 AInD의 핵심 워크플로우가 될 수 있다. R2-D2에게 SPEC을 넘기고 자율적으로 완료하게 하는 현재 방식과 유사하지만, 반복 루프와 진행 추적이 더 체계적이다.
