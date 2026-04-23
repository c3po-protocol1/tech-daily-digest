# kumo — Go로 작성된 경량 AWS 서비스 에뮬레이터

> **출처:** [github.com/sivchari/kumo](https://github.com/sivchari/kumo)
> **GeekNews:** [토론](https://news.hada.io/topic?id=28793) (18 points)
> **태그:** `#AWS` `#DevTools` `#Go` `#Testing`

## 요약

**kumo**는 Go로 작성된 경량 AWS 서비스 에뮬레이터로, 로컬 개발 및 CI/CD 테스트에서 실제 AWS 없이 빠르게 호환 환경을 구성할 수 있게 해준다. ⭐ 969 stars.

### 주요 특징
- **인증 불필요** — CI 환경에 최적
- **단일 바이너리** — 배포와 설치 간편
- **Docker 지원** — 컨테이너로 실행 가능
- **경량** — 빠른 시작, 최소 리소스 사용
- **AWS SDK v2 호환** — Go AWS SDK v2와 완벽 호환
- **선택적 데이터 지속성** — `KUMO_DATA_DIR`로 재시작 시에도 데이터 유지

### 지원 서비스: 76개
S3, DynamoDB, SQS, SNS, Lambda, IAM, CloudFormation 등 주요 서비스를 포함하여 76개 AWS 서비스를 에뮬레이션한다.

### LocalStack과의 차이
LocalStack이 Python 기반의 무거운 솔루션인 반면, kumo는 Go 단일 바이너리로 시작 시간과 리소스 사용량에서 크게 유리하다. 특히 CI/CD 파이프라인에서 매 테스트마다 빠르게 시작/종료해야 하는 시나리오에 적합하다.

### 설치
```bash
go install github.com/sivchari/kumo/cmd/kumo@latest
# 또는 Docker
docker-compose up
```

## Soo에게 의미 있는 이유

AWS 기반 프로젝트의 로컬 개발 및 테스트 환경 구축은 항상 고통스럽다. kumo는 LocalStack 대안으로서 가벼움과 빠른 시작을 강점으로 내세운다. AInD 프로젝트에서 AWS 서비스를 사용하는 에이전트를 개발할 때 테스트 환경으로 활용 가능하다.
