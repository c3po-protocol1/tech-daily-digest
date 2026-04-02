# MiniStack — 무료 오픈소스 로컬 AWS 에뮬레이터

- **출처:** https://ministack.org/
- **GeekNews:** https://news.hada.io/topic?id=28106
- **점수:** 15 points
- **태그:** #aws #localstack #dev-tools #open-source #docker

## 상세 요약

LocalStack이 유료화된 이후, 무료 대체재로 등장한 MiniStack은 34개 AWS 서비스를 단일 포트(4566)에서 제공하는 MIT 라이선스 오픈소스 에뮬레이터다.

**핵심 차별점:**
- **실제 데이터베이스:** RDS는 진짜 PostgreSQL/MySQL 컨테이너를, ElastiCache는 진짜 Redis/Memcached 컨테이너를 실행
- **실제 Docker 컨테이너:** ECS RunTask가 실제 컨테이너를 시작
- **실제 SQL 실행:** Athena가 DuckDB를 통해 실제 SQL을 실행 (선택사항)
- **가벼운 스펙:** ~2초 시작, ~30MB RAM(유휴), 150MB Docker 이미지

**지원 서비스 (34개):** S3, SQS, SNS, DynamoDB, Lambda(실제 Python 실행), IAM, STS, Secrets Manager, CloudWatch Logs/Metrics, SSM, EventBridge, Kinesis, SES, Step Functions, API Gateway v1/v2, RDS, ElastiCache, ECS, Glue, Athena, Firehose, Route53, Cognito, EC2, EMR, EBS, EFS, ALB/ELBv2, ACM, SES v2, WAF v2, CloudFormation.

특히 EMR, EBS, EFS, ALB, WAF 등은 LocalStack에서 Pro(유료) 전용인 서비스를 MiniStack은 무료로 제공한다. 812개 테스트 통과, 계정/라이선스키/텔레메트리 없이 사용 가능.

## Soo에게 의미 있는 이유

로컬 개발 및 CI/CD 환경에서 AWS 서비스를 에뮬레이션할 필요가 있는 프로젝트에서 비용 절감의 직접적 대안이다. 컨설팅 고객사가 AWS를 사용하는 경우, 개발 환경 효율화 방안으로 추천할 수 있다.
