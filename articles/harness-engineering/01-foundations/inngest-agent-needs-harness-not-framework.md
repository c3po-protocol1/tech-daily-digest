# Your Agent Needs a Harness, Not a Framework

- **출처:** [Inngest](https://www.inngest.com/blog/your-agent-needs-a-harness-not-a-framework)
- **저자:** Dan Farrelly
- **날짜:** 2026년 3월 3일
- **코드:** [Utah (UTAH = Universally Triggered Agent Harness)](https://github.com/inngest/utah)
- **태그:** `#Inngest` `#Infrastructure` `#Durability` `#EventDriven` `#Steps`

---

## 핵심 비유: Harness의 보편적 정의

모든 엔지니어링 분야에서 harness는 같은 것: **구성 요소를 연결하고, 보호하고, 오케스트레이션하는 레이어 — 작업 자체를 수행하지 않으면서.**

- **와이어링 harness**: 엔진, 센서, 대시보드 간에 신호를 라우팅
- **테스트 harness**: 코드를 반복 가능하고 관찰 가능하게 만드는 스캐폴딩
- **안전 harness**: 떨어질 때 잡아줌

에이전트 런타임도 같은 것이 필요하다: LLM = 엔진, 도구 = 주변 장치, 메모리 = 저장소. 하지만 **무엇이 이것들을 연결하는가?** 5번째 반복에서 LLM이 타임아웃되면 무엇이 실패를 잡는가? 두 메시지가 충돌하지 않도록 무엇이 방지하는가?

> "모든 에이전트 프레임워크가 이것을 처음부터 만들고 있다 — 자체 재시도 로직, 자체 상태 영속성, 자체 작업 큐, 자체 이벤트 라우팅. **내구성 있는 이벤트 드리븐 인프라가 이미 이것을 해결한다.**"

## 핵심 통찰: Step = 독립적으로 재시도 가능한 작업 단위

모든 LLM 호출이나 도구 호출이 **step**이 된다 — 독립적으로 재시도 가능한 작업 단위. 프로세스가 5번째 반복에서 죽으면, **1~4번째 반복은 이미 영속화**되어 있다.

```typescript
while (!done && iterations < config.loop.maxIterations) {
  iterations++;
  
  // Think: LLM 호출 (각 호출이 하나의 step)
  const llmResponse = await step.run("think", async () => {
    return await callLLM(systemPrompt, messages, tools);
  });

  if (toolCalls.length > 0) {
    // Act: 각 도구 실행이 별도의 step
    for (const tc of toolCalls) {
      const result = await step.run(`tool-${tc.name}`, async () => {
        return await executeTool(tc.id, tc.name, tc.arguments);
      });
      // Observe: 결과를 메시지에 피드백
      messages.push(toolResultMessage(tc, result));
    }
  }
}
```

**핵심 메커니즘들:**
- `step.run("think")`를 10번 호출하면 Inngest가 내부적으로 `think:0`, `think:1` 등으로 추적 → 고유 ID 관리 불필요
- **각 step이 독립적으로 재시도 가능** — 3번째 반복에서 LLM API가 500을 반환하면, 해당 step만 재시도. 1~2번째 결과는 이미 영속화되어 재실행 안 함
- 이것이 **내구성 있는 실행(durable execution)**이 에이전트 루프에 적용된 것

## Utah: 참조 구현

Inngest가 이 원칙을 증명하기 위해 만든 **UTAH (Universally Triggered Agent Harness)**: Telegram/Slack 대화형 에이전트. 도구, 메모리, 서브에이전트 위임, 완전한 내구성 포함. 최소한의 TypeScript, 프레임워크 없음.

> **"내구성 있는, 클라우드 준비된 OpenClaw로 생각하라."**

**"Universally Triggered"의 의미:**
- Telegram/Slack 웹훅, cron 스케줄, 서브에이전트 호출, 함수 간 이벤트
- 에이전트는 **어떻게 활성화되었는지 알지 못하고 신경 쓰지 않음**
- 트리거가 작업에서 **분리됨(decoupled)**
- 내일 Slack 봇을 추가해도 에이전트 루프는 변하지 않음. Harness가 라우팅.

## OpenClaw와의 차이점

OpenClaw과 pi-coding-agent 라이브러리는 프로세스 내 이벤트를 사용하여 이벤트와 오케스트레이션을 메모리에서 처리. Inngest는 이벤트 드리븐 오케스트레이션 레이어로, **실행을 오케스트레이션에서 분리(decouple)**.

이것이 harness에 가져다주는 것:
- **관측성** — 트레이스와 step 레벨 검사
- **신뢰성** — 내구성 있는 실행과 재시도
- **분산 오케스트레이션** — 멀티 에이전트 분산 오케스트레이션의 기반
- **감사 추적** — 시스템 내에서 무슨 일이 일어났는지의 이벤트 히스토리
- **스케줄링** — cron이나 지연된 함수가 내장

> "이 모든 문제는 **인프라 문제이지 AI 문제가 아니다.**"

## 서브에이전트 위임 (delegate_task)

서브에이전트 위임을 위한 `delegate_task` 도구:

```typescript
const delegateTaskTool = {
  name: "delegate_task",
  description: "Delegate a task to a sub-agent that runs in its own context",
  parameters: { task: "string", context: "string" }
};
```

메인 에이전트가 서브에이전트에게 작업을 위임하면:
- 서브에이전트는 **자체 컨텍스트 윈도우**에서 실행
- 결과만 메인 에이전트에 반환
- 메인 에이전트의 컨텍스트가 중간 노이즈로 오염되지 않음
- Inngest 이벤트를 통해 비동기적으로 조정

## 메모리와 도구

Utah는 pi-coding-agent의 도구를 활용:
- `read`, `write`, `edit` — 파일 작업 (이미지 지원, 바이너리 감지, 스마트 절단)
- `bash` — 셸 실행 (설정 가능한 타임아웃, 출력 절단)
- `grep`, `find`, `ls` — `.gitignore`를 존중하는 검색/탐색
- `remember` — 일일 로그에 메모 영속화 (커스텀)
- `web_fetch` — 웹 콘텐츠 가져오기 (커스텀)
- `delegate_task` — 서브에이전트 위임 (커스텀)

## 프레임워크가 놓치는 것 vs Harness가 해결하는 것

| 문제 | 프레임워크의 접근 | Harness의 접근 |
|------|----------------|--------------|
| LLM 호출 실패 | 앱 레벨 try/catch | **step 레벨 자동 재시도** (지수 백오프) |
| 프로세스 크래시 | 처음부터 다시 | **마지막 완료된 step에서 재개** |
| 동시 메시지 | 경쟁 조건 | **동시성 제어** (큐잉, 잠금) |
| 디버깅 | 로그 파싱 | **step 레벨 트레이스** (타임라인) |
| 장기 실행 | 메모리 내 상태 | **영속화된 상태** (프로세스 독립) |

## Soo에게 의미 있는 이유

이 글은 **harness 엔지니어링을 인프라 관점**에서 접근한다. 대부분의 harness 논의가 프롬프트와 도구에 집중하는 반면, Inngest는 **상태 관리, 재시도, 관측성, 내구성**이라는 프로덕션 인프라 레이어를 강조한다.

**AInD 컨설팅 핵심:**
1. **"인프라 문제이지 AI 문제가 아니다"** — 에이전트 실패의 많은 부분이 LLM이 아닌 인프라에서 발생
2. **Step = 독립적 재시도 단위** — 에이전트 루프를 내구성 있게 만드는 구체적 패턴
3. **이벤트 드리븐 분리** — 트리거와 작업의 분리로 확장성 확보
4. **Holocron과의 연관** — Inngest의 step 레벨 트레이스가 Holocron이 보여주려는 것과 정확히 같은 목적 (에이전트가 무엇을 하고 있는지 관찰)
