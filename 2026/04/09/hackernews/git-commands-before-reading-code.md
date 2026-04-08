# 코드를 읽기 전에 실행하는 Git 명령어 5가지

- **출처:** [piechowski.io](https://piechowski.io/post/git-commands-before-reading-code/)
- **HN 토론:** [Hacker News](https://news.ycombinator.com/item?id=47687273) (1,692 points / 365 comments)
- **태그:** `#Git` `#코드리뷰` `#개발생산성` `#코드베이스분석`

## 상세 요약

새로운 코드베이스를 접할 때, 코드를 열기 전에 터미널에서 Git 명령어 5개만 돌리면 프로젝트의 건강 상태를 진단할 수 있다는 실전 가이드.

### 1. 가장 많이 변경된 파일 (Churn Hotspots)
```bash
git log --format=format: --name-only --since="1 year ago" | sort | uniq -c | sort -nr | head -20
```
지난 1년간 가장 많이 수정된 파일 20개. 최상위 파일은 거의 항상 "아, 그 파일... 다들 건드리기 무서워하는 파일"이다. 2005년 Microsoft Research 연구에 따르면 churn 기반 메트릭이 복잡도 메트릭보다 결함 예측에 더 신뢰도가 높다.

### 2. 누가 이것을 만들었나 (Bus Factor)
```bash
git shortlog -sn --no-merges
```
한 사람이 커밋의 60% 이상을 차지하면 bus factor 문제. 6개월 전에 떠났다면 위기.

### 3. 버그가 어디에 모이나 (Bug Clusters)
```bash
git log -i -E --grep="fix|bug|broken" --name-only --format='' | sort | uniq -c | sort -nr | head -20
```
churn 핫스팟과 교차 대조해서 양쪽 모두에 나타나는 파일이 최고 위험 코드.

### 4. 프로젝트가 가속 중인가 사망 중인가
```bash
git log --format='%ad' --date=format:'%Y-%m' | sort | uniq -c
```
월별 커밋 수 추이. 한 달 만에 반으로 줄면 보통 누군가 떠난 것.

### 5. 팀이 얼마나 자주 긴급 대응하는가
```bash
git log --oneline --since="1 year ago" | grep -iE 'revert|hotfix|emergency|rollback'
```
revert/hotfix 빈도가 주 단위면 배포 프로세스를 신뢰하지 못한다는 의미.

## Soo에게 의미 있는 이유
AInD 컨설팅에서 클라이언트 코드베이스를 빠르게 진단할 때 즉시 활용 가능한 실전 기법. AI 에이전트에게 코드베이스 분석을 시킬 때도 이 5가지 명령어를 기본 도구로 장착시킬 수 있다.
