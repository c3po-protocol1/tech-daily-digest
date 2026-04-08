# Anthropic의 Claude Mythos, Project Glasswing으로 제한 배포 — 보안 연구용 초강력 모델

- **출처:** [simonwillison.net](https://simonwillison.net/2026/Apr/7/project-glasswing/)
- **GeekNews:** [topic?id=28293](https://news.hada.io/topic?id=28293) (6 points)
- **태그:** `#Anthropic` `#보안` `#AI안전` `#취약점연구` `#ClaudeMythos`

## 상세 요약

Anthropic이 최신 모델 Claude Mythos를 일반 공개 대신, **Project Glasswing**이라는 제한적 프리뷰 프로그램으로 보안 연구자에게만 배포하기로 결정했다.

### Claude Mythos의 사이버보안 능력
- Firefox 147 JS 엔진 취약점에 대해: Opus 4.6은 수백 번 시도 중 2회 익스플로잇 성공 → **Mythos는 181회 성공, 29회 추가 레지스터 제어**
- 4개 취약점을 체인한 웹 브라우저 익스플로잇 작성 (JIT 힙 스프레이로 렌더러+OS 샌드박스 탈출)
- Linux 등에서 레이스 컨디션+KASLR 바이패스로 자율적 권한 상승 익스플로잇
- FreeBSD NFS 서버에 20개 가젯 ROP 체인으로 원격 코드 실행 (root 권한)

### Project Glasswing
Amazon, Apple, Google, Microsoft 등 참여. 파트너사에 Claude Mythos를 제공해 **자사 핵심 시스템의 취약점을 선제적으로 발견·수정**하게 하는 프로그램.

### 업계 반응 (Simon Willison 정리)
- **Greg Kroah-Hartman (Linux 커널):** "한 달 전 세계가 바뀌었다. 이제 AI로 만든 보안 보고서가 진짜이고 좋다"
- **Daniel Stenberg (curl):** "AI 슬럼 쓰나미에서 보안 보고서 쓰나미로 전환. 하루에 몇 시간씩 이것에 쓰고 있다"
- **Thomas Ptacek:** "Vulnerability Research Is Cooked" (취약점 연구는 끝장났다)

### "너무 위험해서 공개 안 한다"?
마케팅으로 볼 수도 있지만, Simon Willison은 이번에는 실제로 그 주의가 타당하다고 평가.

## Soo에게 의미 있는 이유
AI 안전 논의가 추상적 단계를 넘어 **구체적 사이버보안 위협**으로 진입한 전환점. AInD 컨설팅에서 보안 측면을 반드시 다뤄야 하며, AI가 공격과 방어 양쪽을 동시에 변화시키고 있음을 인지해야 한다.
