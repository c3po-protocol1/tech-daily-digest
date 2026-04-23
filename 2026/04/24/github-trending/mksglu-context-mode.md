# mksglu/context-mode — AI 코딩 에이전트의 컨텍스트 윈도우 최적화

> **GitHub:** [mksglu/context-mode](https://github.com/mksglu/context-mode)
> ⭐ 9.4k stars | 🍴 654 forks
> **태그:** `#AI` `#Context` `#Agent` `#Optimization`

## 요약

AI 코딩 에이전트의 컨텍스트 윈도우를 최적화하는 도구. 도구 출력을 샌드박싱하여 **98% 감소** 효과를 달성한다. 12개 플랫폼 지원.

### 핵심 메커니즘
AI 코딩 에이전트(Claude Code, Cursor, Windsurf 등)가 도구(shell, file read 등)를 실행할 때, 도구 출력이 컨텍스트 윈도우를 대량 소비한다. context-mode는 이 출력을 샌드박싱하여:
- **원본 출력 보존** (필요시 접근 가능)
- **컨텍스트에는 요약만 포함** (98% 토큰 절감)
- 에이전트가 "더 자세히 보고 싶다"면 원본에 접근 가능

### 지원 플랫폼
Claude Code, Cursor, Windsurf, Cline, OpenClaw, Pi 등 12개 코딩 에이전트 플랫폼과 호환.

### 성능 영향
- 토큰 사용량 98% 감소 (도구 출력 부분)
- 더 긴 세션 유지 가능
- 컨텍스트 윈도우 소진으로 인한 품질 저하 방지
- 비용 절감 효과

### 설치
플러그인 형태로 각 플랫폼에 설치. Claude Code의 경우 `.claude-plugin/` 디렉토리에 설정.

## Soo에게 의미 있는 이유

"토큰 효율성"은 AInD 컨설팅에서 비용 최적화의 핵심이다. 98% 감소라는 수치는 고객에게 매우 인상적인 데모 포인트가 된다. OpenClaw도 지원 플랫폼 목록에 포함되어 있다는 점이 흥미롭다.
