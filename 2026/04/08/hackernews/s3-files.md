# S3 Files: S3의 변화하는 얼굴

- **출처:** https://www.allthingsdistributed.com/2026/04/s3-files-and-the-changing-face-of-s3.html
- **HN 토론:** https://news.ycombinator.com/item?id=47680404
- **점수:** 144 points | 38 comments
- **태그:** `#AWS` `#클라우드` `#스토리지` `#인프라`

## 상세 요약

AWS가 **S3 Files**를 출시했다. Werner Vogels의 All Things Distributed 블로그에서 Andy Warfield가 설계 과정을 상세히 공유한 이 글은 6,000단어에 달하는 기술 에세이다.

S3 Files는 Amazon EFS(Elastic File System)를 S3에 통합하여 기존 S3 데이터를 네트워크 파일시스템으로 직접 접근할 수 있게 한다. EC2, 컨테이너, Lambda에서 S3 버킷을 마운트하면 일반 파일처럼 작업하고, 변경사항이 S3로 전파된다.

**설계의 핵심 통찰**: 파일과 오브젝트 시맨틱을 하나로 합치려는 시도가 반복적으로 실패했다. 결국 **"Stage and Commit"** 모델을 채택 — 파일 변경이 EFS에서 축적되고 약 60초마다 S3로 커밋되는 방식이다. 이 경계를 숨기지 않고 명시적으로 드러낸 것이 오히려 최고의 설계가 되었다.

주요 특징:
- 128KB 이하 파일은 메타데이터와 함께 즉시 가져옴 (lazy hydration)
- **Read bypass**: 순차 읽기 시 NFS 대신 S3에 직접 병렬 GET → 클라이언트당 3GB/s
- 30일 미접근 파일 데이터는 파일시스템 뷰에서 자동 퇴거 (S3에서 삭제되지 않음)
- 충돌 시 S3가 진실의 원천, 파일시스템 버전은 lost+found로 이동

에이전트 코딩 도구와의 연관성도 언급: AI 에이전트들이 데이터 작업 시 Unix 도구를 즉시 활용하려 하는데, S3 Files가 이 마찰을 제거한다.

## Soo에게 의미 있는 이유

클라우드 스토리지의 패러다임 변화를 보여준다. S3가 오브젝트 스토어에서 Tables, Vectors, Files로 확장되며 "데이터 프리미티브 플랫폼"으로 진화 중이다. AI/ML 파이프라인 설계 시 중요한 인프라 변화.
