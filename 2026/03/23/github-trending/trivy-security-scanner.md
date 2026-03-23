# Trivy — 컨테이너/클라우드 종합 보안 스캐너

- **출처:** [github.com/aquasecurity/trivy](https://github.com/aquasecurity/trivy) ⭐ 33,600+ (+249/일)
- **태그:** `#DevSecOps` `#ContainerSecurity` `#Kubernetes` `#Vulnerability` `#SBOM`

---

## 핵심 요약

Aqua Security가 개발한 오픈소스 종합 보안 스캐너 Trivy가 33,600+ 스타의 성숙한 프로젝트로 계속 성장하며 하루 249 스타를 기록하고 있다. Trivy는 **컨테이너 이미지, Kubernetes 매니페스트, IaC(Infrastructure as Code) 파일, 코드 저장소, 클라우드 환경** 등 현대적 소프트웨어 인프라의 거의 모든 계층에서 보안 문제를 탐지하는 올인원 스캐너이다.

Trivy가 탐지하는 보안 문제의 범위는 다섯 가지 카테고리에 걸친다. 첫째, **취약점(Vulnerabilities)** — 알려진 CVE(Common Vulnerabilities and Exposures)에 등록된 소프트웨어 취약점을 탐지한다. OS 패키지(apt, yum 등)와 언어별 의존성(npm, pip, Maven 등) 모두를 분석한다. 둘째, **잘못된 설정(Misconfigurations)** — Kubernetes, Docker, Terraform, CloudFormation 등의 설정 파일에서 보안 모범 사례에 어긋나는 설정을 찾아낸다. 예를 들어 "컨테이너가 root로 실행되고 있다", "S3 버킷이 공개되어 있다" 같은 문제를 탐지한다.

셋째, **시크릿(Secrets)** — 코드에 하드코딩된 API 키, 비밀번호, 토큰 등을 탐지한다. 넷째, **라이선스(Licenses)** — 사용 중인 오픈소스 라이브러리의 라이선스가 조직의 정책과 호환되는지 확인한다. 다섯째, **SBOM(Software Bill of Materials)** — 소프트웨어에 포함된 모든 구성 요소의 목록을 생성하여 공급망 보안을 지원한다.

DevSecOps 파이프라인에서 Trivy의 위치는 **CI/CD의 게이트 역할**이다. 코드가 커밋되면 자동으로 Trivy 스캔이 실행되고, 심각한 취약점이 발견되면 빌드/배포를 차단한다. GitHub Actions, GitLab CI, Jenkins 등 주요 CI/CD 도구와의 통합이 공식 지원되며, 설치부터 첫 스캔까지 단 몇 분이면 설정 가능한 사용 편의성도 큰 장점이다.

AI 에이전트 시대에서 Trivy의 중요성은 더욱 커진다. AI 에이전트가 생성한 코드나 인프라 설정에 보안 문제가 포함될 수 있으며, Trivy 같은 자동화된 보안 스캐너가 **에이전트의 출력물에 대한 보안 검증 게이트**로 기능할 수 있다. "에이전트가 만든 코드도 반드시 보안 스캔을 통과해야 한다"는 원칙을 자동으로 강제하는 도구이다.

## Soo에게 의미 있는 이유

AInD 컨설팅에서 AI 에이전트의 코드 생성 파이프라인을 설계할 때, 보안 스캔은 필수 게이트이다. Trivy 같은 도구를 에이전트 워크플로에 통합하는 패턴은 기업 보안팀의 신뢰를 얻는 데 핵심적이다.
