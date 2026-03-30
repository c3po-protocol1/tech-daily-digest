# Context-Efficient Backpressure for Coding Agents

- **출처:** [HumanLayer](https://www.humanlayer.dev/blog/context-efficient-backpressure)
- **저자:** HumanLayer Team
- **태그:** `#HumanLayer` `#Backpressure` `#TestOutput` `#SmartZone` `#ContextBudget`

---

## 핵심 패턴: 모든 출력을 삼키고 ✓로 교체

HumanLayer가 지속적으로 사용하는 패턴:

> **모든 테스트/빌드/린트 출력을 삼키고, 단계가 통과하면 단일 `✓`로 교체. `exitCode != 0`일 때만 저장된 출력을 stdout에 덤프. 그렇지 않으면 에이전트는 절대 보지 않는다.**

## 왜 이것이 중요한가: "스마트 존"에 머물기

Claude 모델에서 **~75K 토큰의 "스마트 존"**에 머무르려 노력해야 한다. `PASS src/utils/helper.test.ts`의 모든 줄은 **낭비**다.

**구체적 문제:**
- Jest/Maven/pytest 실행이 **200줄 이상**의 출력을 쏟아낼 수 있음
- 에이전트가 이 모든 것을 파싱하여 실제로 수정해야 할 **한 개의 실패를 찾아야 함**
- 모든 테스트가 통과하면? **10 토큰 미만으로 전달 가능한 "all good" 결과에 컨텍스트 윈도우의 2~3%를 낭비**한 것

> "컨텍스트를 낭비하고 있다 — 사용하는 모든 토큰이 결과를 악화시키고, '스마트 존으로 돌아가기 위해 클리어하거나 compact해야 하는 시점'에 더 가까워진다."

**비용 관점의 핵심 통찰:**

> "토큰 비용과 실행 시간 걱정은 잠시 접어두라 — 'dumb zone'에서 에이전트를 다루느라 낭비되는 **인간 시간**이 10배 이상 비싸다."

## 구체적 구현: `run_silent()`

```bash
run_silent() {
  local description="$1"
  local command="$2"
  local tmp_file=$(mktemp)

  if eval "$command" > "$tmp_file" 2>&1; then
    printf " ✓ %s\n" "$description"
    rm -f "$tmp_file"
    return 0
  else
    local exit_code=$?
    printf " ✗ %s\n" "$description"
    cat "$tmp_file"
    rm -f "$tmp_file"
    return $exit_code
  fi
}

# 사용법
run_silent "fe integration tests" "bun run test:integration"
```

**결과 — 200줄의 테스트 출력 대신:**
```
✓ Auth tests
✓ Utils tests
✗ API tests
  FAIL src/api/users.test.ts
  ● should validate email format
    Expected: true
    Received: false
```

> "모델이 절단 여부를 결정할 필요가 없다. 이미 당신이 그 결정을 내렸다. 성공 = ✓. 실패 = 전체 출력."

## 시간이 지나면서 더 작게 만들기

기본 래퍼가 작동하면 반복 개선:

### 1. failFast 활성화
- `pytest -x`, `jest --bail`, `go test -failfast`
- **한 번에 하나의 실패만.** 에이전트가 5개의 서로 다른 버그 사이에서 컨텍스트 전환하거나, 테스트 #1을 수정하려는 중에 "테스트 2~5가 실패" 출력을 다시 읽지 않도록

### 2. 출력 필터링
- 에이전트가 이슈를 찾는 데 도움이 되지 않는 일반적 스택 프레임 제거
- 타이밍 정보 제거
- `grep/sed/awk/cut` 등으로 **실패한 assertion만** 추출

### 3. 프레임워크별 파싱
- [HumanLayer의 run_silent.sh](https://github.com/humanlayer/humanlayer/blob/main/hack/run_silent.sh) — pytest, jest, go test, vitest에서 테스트 카운트를 추출하여 노이즈 없이 가시성 유지
- Maven, Gradle (악명 높게 장황), xcodebuild, cargo 등에도 동일하게 작동

**실제 효과:** HumanLayer의 모노레포 체크/테스트 — 래퍼 없이는 **컨텍스트 윈도우의 절반 정도**의 출력이 쉽게 발생

## "컨텍스트 불안(Context-Anxious)" 모델의 문제

최신 세대 모델들이 RL에서 **너무 보수적으로 오버코렉트**:

### 출력 삼키기
모델이 출력을 `/dev/null`로 파이프하고 `||` 연산자로 exit code 기반 메시지만 출력. 보수적인 것은 좋지만, 실제로는 **가드레일이 더 많은 토큰을 사용**하는 경우가 있음.

### 과도한 절단
모델이 도구 출력을 받기 전에 이미 절단하여, 디버깅에 필요한 핵심 정보를 잃어버림.

**해결책:** 절단/필터링의 결정을 모델에 맡기지 말고 **harness 레벨에서 결정론적으로 제어**.

## Soo에게 의미 있는 이유

이 글은 **가장 실용적인 harness 기법 중 하나**를 제공한다. 모든 프로젝트에 오늘 당장 적용 가능한 구체적 셸 스크립트와 패턴.

**AInD 컨설팅 핵심:**
1. **`run_silent()` 패턴** — 고객사에 즉시 적용 가능한 구체적 코드
2. **"스마트 존" 개념** — ~75K 토큰 내에서 작업해야 하는 이유를 수치로 설명
3. **failFast의 중요성** — 한 번에 하나의 실패만 노출하는 것이 에이전트 효율의 핵심
4. **harness가 절단을 결정, 모델이 아닌** — 결정론적 제어의 원칙
5. **R2가 Holocron 개발 시 `go test`를 실행할 때** — 이 패턴을 적용하면 컨텍스트 효율 크게 개선
