# Tech Daily Digest — 2026년 4월 15일 (화)

## 🌟 오늘의 하이라이트

1. **Claude Code Routines 출시** — 스케줄/API/GitHub 이벤트로 클라우드에서 자동 실행되는 AI 코딩 자동화. CI/CD와 AI 에이전트의 경계가 허물어진다. [→ 상세](hackernews/claude-code-routines.md)
2. **Django Pre-Auth DoS (CVE-2026-33033)** — 2.5MB 요청 하나로 86GB 메모리 복사 유발. Claude Code + Codex로 발견된 20년 묵은 취약점. [→ 상세](geeknews/django-cve-dos.md)
3. **Gemma 4 로컬 코딩 에이전트 실전 테스트** — 도구 호출 성공률 6.6% → 86.4%. 로컬 AI 코딩이 실용화 단계 진입. [→ 상세](geeknews/gemma4-codex-local.md)
4. **Wheel Next: `pip install torch` 한 줄의 미래** — NVIDIA+Astral+Quansight 연합이 Python 패키징 혁신 추진. 900MB → 250MB. [→ 상세](geeknews/pip-install-torch-wheel-next.md)
5. **Steve Blank: "AI 시대에 2년 이상 된 스타트업은 사실상 사망"** — 소프트웨어-as-결과 패러다임, MVP → MPO 전환. [→ 상세](geeknews/startup-dead-on-arrival.md)

---

## 📰 Hacker News Top 5

| # | 제목 | Points | Comments |
|---|------|--------|----------|
| 1 | [Flock Safety 프라이버시 옵트아웃 거부](hackernews/flock-privacy-opt-out.md) | 425 | 179 |
| 2 | [Claude Code Routines](hackernews/claude-code-routines.md) | 317 | 203 |
| 3 | [우주 화장실 이야기](hackernews/space-toilets.md) | 111 | 40 |
| 4 | [5NF와 데이터베이스 설계](hackernews/5nf-database-design.md) | 108 | 45 |
| 5 | [Chrome Skills — AI 프롬프트를 원클릭 도구로](hackernews/chrome-skills.md) | 69 | 37 |

## 🇰🇷 GeekNews Top 10

| # | 제목 | Points |
|---|------|--------|
| 1 | [월 $20 스택으로 월매출 $10K 회사 운영법](geeknews/20-dollar-stack-10k-mrr.md) | 46 |
| 2 | [damn-my-slow-kt — KT SLA 자동 측정 도구](geeknews/damn-my-slow-kt.md) | 40 |
| 3 | [홈랩 2026 — 월 €7 셀프호스팅](geeknews/homelab-2026.md) | 29 |
| 4 | [Gemma 4를 Codex CLI에서 로컬 실행](geeknews/gemma4-codex-local.md) | 27 |
| 5 | [Happy — Claude Code/Codex 모바일 클라이언트](geeknews/happy-mobile-client.md) | 18 |
| 6 | [pip install torch 혁신 — Wheel Next](geeknews/pip-install-torch-wheel-next.md) | 18 |
| 7 | [소프트웨어 팀의 경제학](geeknews/software-team-economics.md) | 14 |
| 8 | [스타트업 사망 선고 — Steve Blank](geeknews/startup-dead-on-arrival.md) | 10 |
| 9 | [Django DoS 취약점 CVE-2026-33033](geeknews/django-cve-dos.md) | 6 |
| 10 | [CASK — KV 캐시 구조적 압축](geeknews/cask-kv-compression.md) | 3 |

## 🔥 GitHub Trending Top 10

| # | 레포 | 설명 | 연속 |
|---|------|------|------|
| 1 | 🔥 [forrestchang/andrej-karpathy-skills](github-trending/andrej-karpathy-skills.md) | Karpathy 영감 Claude Code 가이드라인 | 2일+ |
| 2 | 🔥 [thedotmack/claude-mem](github-trending/claude-mem.md) | Claude Code 영속 메모리 압축 시스템 | 2일+ |
| 3 | 🔥 [jamiepine/voicebox](github-trending/voicebox.md) | 오픈소스 음성 합성 스튜디오 | 2일+ |
| 4 | [pascalorg/editor](github-trending/pascal-editor.md) | 3D 건축 에디터 (React Three Fiber + WebGPU) | NEW |
| 5 | 🔥 [obra/superpowers](github-trending/superpowers.md) | 에이전틱 코딩 스킬 프레임워크 | 2일+ |
| 6 | 🔥 [virattt/ai-hedge-fund](github-trending/ai-hedge-fund.md) | AI 헤지펀드 PoC (19개 에이전트) | 2일+ |
| 7 | 🔥 [shiyu-coder/Kronos](github-trending/kronos-financial-model.md) | 금융 시장 파운데이션 모델 | 2일+ |
| 8 | 🔥 [NousResearch/hermes-agent](github-trending/hermes-agent.md) | 자기 개선 AI 에이전트 | 2일+ |
| 9 | [tw93/Mole](github-trending/mole-mac-cleaner.md) | macOS 딥 클린 & 최적화 도구 | NEW |
| 10 | 🔥 [shanraisshan/claude-code-best-practice](github-trending/claude-code-best-practice.md) | Claude Code 베스트 프랙티스 종합 | 2일+ |

---

## 🔑 오늘의 키워드

**AI 코딩 에이전트 생태계 폭발**: Claude Code Routines, Superpowers 프레임워크, Happy 모바일 클라이언트, Karpathy Skills, claude-mem 등 AI 코딩 도구/프레임워크가 동시다발적으로 트렌딩. "에이전틱 엔지니어링"이 별도의 생태계를 형성 중.

**로컬 AI의 실용화**: Gemma 4의 도구 호출 86.4% 성공률, 월 $20 스택에서 로컬 GPU로 AI 비용 제로화 등 로컬 AI가 "실험"에서 "실전"으로 전환.

**보안 + AI**: Django 20년 묵은 취약점을 AI가 발견. AI 기반 보안 감사의 새로운 가능성.
