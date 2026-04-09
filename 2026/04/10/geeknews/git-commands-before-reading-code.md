# 코드를 읽기 전에 실행하는 Git 명령들

- **출처**: [piechowski.io](https://piechowski.io/post/git-commands-before-reading-code/)
- **GeekNews**: [토론](https://news.hada.io/topic?id=28324) (48 points)
- **태그**: `#git` `#development` `#codebase-audit`

## 상세 요약

새로운 코드베이스를 접할 때 코드를 열기 전 Git 히스토리로 프로젝트의 건강 상태를 진단하는 5가지 명령어를 소개한다.

1. **가장 많이 변경된 파일** (`git log --format=format: --name-only --since="1 year ago" | sort | uniq -c | sort -nr | head -20`): 높은 변동 + 소유자 없음 = 코드베이스 드래그의 핵심 신호. 2005년 Microsoft Research 연구에서 변동률 기반 지표가 복잡도보다 결함을 더 잘 예측한다고 밝힘.

2. **누가 만들었나** (`git shortlog -sn --no-merges`): 1인이 60% 이상이면 버스 팩터 위험. 최근 6개월과 전체를 비교하여 핵심 기여자 이탈 여부 확인. squash-merge 워크플로우에서는 머지한 사람만 보이는 한계.

3. **버그 클러스터** (`git log -i -E --grep="fix|bug|broken" --name-only`): 변동률 핫스팟과 교차하면 최고 위험 코드.

4. **프로젝트 가속/감속** (`git log --format='%ad' --date=format:'%Y-%m'`): 월별 커밋 수 추이. 한 달 만에 절반으로 떨어지면 대개 누군가 떠난 것. CTO에게 차트를 보여주니 "그때 두 번째 시니어 엔지니어를 잃었다"고 인식한 사례.

5. **소방 빈도** (`git log --oneline --since="1 year ago" | grep -iE 'revert|hotfix|emergency|rollback'`): 매주 리버트가 있으면 배포 프로세스 신뢰 부족.

## Soo에게 의미 있는 이유

AInD 컨설팅 초기 진단에 활용 가능한 실전 기법. 고객사 코드베이스의 건강 상태를 정량적으로 빠르게 파악하는 도구.
