# SQLite로 실제 쇼핑몰을 운영하며 배운 것들

> **출처**: [ultrathink.art](https://ultrathink.art/blog/sqlite-in-production-lessons) | [GeekNews 토론](https://news.hada.io/topic?id=28377)
> **점수**: 27점 | **댓글**: 4개
> **태그**: `#SQLite` `#프로덕션` `#Rails` `#인프라` `#AI운영`

## 요약

AI 에이전트가 자율적으로 운영하는 이커머스 쇼핑몰 ultrathink.art가 **SQLite를 프로덕션에서 사용하며 배운 교훈**을 공유한다.

**설정:**
Rails 8 + SQLite, 4개 DB (primary, cache, queue, cable)가 하나의 Docker 볼륨에 위치. WAL(Write-Ahead Logging) 모드로 동시 읽기/쓰기 처리.

**주문 2건이 사라진 날:**
2월 4일, 2시간 동안 11번의 커밋을 main에 푸시. Kamal의 blue-green 배포로 인해 컨테이너 교체 구간이 겹치기 시작. 3개의 프로세스가 동시에 WAL 파일을 열고 쓰기를 시도.

결과: Stripe에서는 결제 성공, **DB에는 주문 레코드 미기록**. `sqlite_sequence`에서 seq=17이지만 실제 행은 15개 — 2건의 주문이 WAL 충돌로 유실.

**교훈:**
- 빠른 연속 배포 금지 — AI 에이전트의 CLAUDE.md에 규칙 추가
- SQLite의 WAL은 단일 프로세스에서는 훌륭하지만, 다중 컨테이너 동시 접근에서 데이터 유실 위험
- `timeout: 5000`(5초 대기)는 일반 운영에서 충분하지만, 배포 겹침에는 무력

**근본 원인:** 컨테이너 기반 배포에서 SQLite 파일을 공유 볼륨으로 마운트하면, 배포 시 여러 프로세스가 동시에 WAL에 쓰면서 경합 발생.

## Soo에게 의미 있는 이유

AI 에이전트가 운영하는 서비스의 실제 프로덕션 사고 보고서. SQLite의 한계를 정확히 이해하는 것은 바이브 코딩으로 빠르게 서비스를 만들 때 필수적이다. "빠르게 배포하되, 데이터 무결성은 타협하지 말라"는 교훈.
