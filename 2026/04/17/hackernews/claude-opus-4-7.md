# Claude Opus 4.7 출시

- **출처**: [Anthropic 공식 블로그](https://www.anthropic.com/news/claude-opus-4-7)
- **HN 토론**: [Hacker News](https://news.ycombinator.com/item?id=47793411) (1326 points)
- **태그**: `#AI` `#LLM` `#Anthropic` `#Claude`

## 상세 요약

Anthropic이 최신 모델 Claude Opus 4.7을 정식 출시했다. Opus 4.6의 직접 업그레이드 버전으로, 특히 **고급 소프트웨어 엔지니어링**에서 눈에 띄는 개선을 보인다. 사용자들은 이전에는 밀착 감독이 필요했던 가장 어려운 코딩 작업을 Opus 4.7에 자신 있게 맡길 수 있다고 보고한다.

### 핵심 개선 사항
- **지시사항 준수력 대폭 향상**: 이전 모델이 느슨하게 해석하거나 건너뛰던 지시를 Opus 4.7은 문자 그대로 따름. 기존 프롬프트 재조정 필요
- **멀티모달 지원 강화**: 최대 2,576px 장변(~3.75 메가픽셀) 고해상도 이미지 지원. 이전 모델 대비 3배 이상 높은 해상도
- **새 effort 레벨 `xhigh`**: high와 max 사이의 세밀한 제어. Claude Code 기본값이 xhigh로 상향
- **메모리 활용 개선**: 파일시스템 기반 메모리를 더 잘 활용, 장기 멀티세션 작업에서 중요 메모를 기억
- **사이버 보안 세이프가드**: Mythos Preview의 제한 출시에 따른 사이버 공격 자동 감지/차단 시스템 탑재
- **`/ultrareview` 명령어**: 변경사항을 전용 리뷰 세션으로 읽고 버그와 설계 이슈를 플래그
- **Auto Mode**: Max 사용자에게 확대. Claude가 권한 결정을 대신해 장시간 작업을 더 적은 중단으로 실행

### 벤치마크 성과
- SWE-bench Verified에서 Opus 4.6 대비 유의미한 향상
- Finance Agent 평가에서 SOTA
- GDPval-AA(경제적 가치 있는 지식 작업 평가)에서 SOTA
- CursorBench: 70% (Opus 4.6: 58%)
- Terminal-Bench 2.0에서 이전 모델 대비 우수
- XBOW 시각 정밀도 벤치마크: 98.5% (Opus 4.6: 54.5%)

### 주의점
- 토크나이저 업데이트로 동일 입력이 1.0~1.35배 더 많은 토큰 소비 가능
- 높은 effort 레벨에서 더 많은 출력 토큰 생성
- 가격: 입력 $5/M 토큰, 출력 $25/M 토큰 (Opus 4.6과 동일)

## Soo에게 의미 있는 이유
AInD 컨설팅에서 코딩 에이전트의 자율성과 신뢰성이 핵심인데, Opus 4.7의 장시간 자율 코딩 능력 향상과 지시사항 준수력은 에이전트 기반 개발 워크플로우의 실질적 생산성 향상을 의미한다. 특히 xhigh effort 레벨과 /ultrareview 같은 기능은 코드 품질 관리에 직접적으로 도움이 된다.
