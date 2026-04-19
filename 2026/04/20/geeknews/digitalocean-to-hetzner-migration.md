# DigitalOcean에서 Hetzner로 마이그레이션: 월 $1,432 → $233, 다운타임 제로

- **출처**: [isayeter.com](https://isayeter.com/posts/digitalocean-to-hetzner-migration/)
- **GeekNews 토론**: [GeekNews](https://news.hada.io/topic?id=28671)
- **포인트**: 11점
- **태그**: `#DevOps` `#마이그레이션` `#인프라` `#비용절감`

## 요약

터키 소프트웨어 회사가 DigitalOcean에서 Hetzner 전용 서버로 프로덕션 인프라를 무중단 마이그레이션한 실전 사례.

**비용 비교:**
| | DigitalOcean | Hetzner AX162-R |
|---|---|---|
| CPU | 32 vCPU | AMD EPYC 9454P (48코어/96스레드) |
| RAM | 192GB | 256GB DDR5 |
| 디스크 | 600GB SSD + 2×1TB | 1.92TB NVMe Gen4 RAID1 |
| 월 비용 | **$1,432** | **$233** |
| 연 절감 | — | **$14,388** |

**마이그레이션 대상:** 30개 MySQL DB (248GB), 34개 Nginx 사이트, GitLab EE, Neo4J, 수십만 사용자의 모바일 앱 트래픽. OS도 CentOS 7 → AlmaLinux 9.7로 전환.

**6단계 무중단 전략:**
1. 신규 서버에 전체 스택 설치
2. rsync로 웹 파일 복제 (65GB, 150만 파일)
3. MySQL 마스터-슬레이브 복제 (mydumper로 병렬 덤프 → 수일→수시간 단축)
4. DNS TTL 300초로 사전 축소
5. 구서버 Nginx를 리버스 프록시로 전환 (Python 스크립트 자동화)
6. DNS 전환 및 구서버 해제

## Soo에게 의미 있는 이유

클라우드 vs 전용 서버의 비용 효율성을 실증적으로 보여주는 사례. AI 인프라 비용이 급증하는 시대에, 워크로드 특성에 따른 인프라 선택 전략이 중요하다.
