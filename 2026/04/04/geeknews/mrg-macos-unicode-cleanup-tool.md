# mrg — macOS에서 자모 분리 현상을 해결하고 메타데이터 파일을 제거하는 CLI 도구

- **출처**: [https://github.com/ilotoki0804/mrg](https://github.com/ilotoki0804/mrg)
- **GeekNews**: [https://news.hada.io/topic?id=28176](https://news.hada.io/topic?id=28176)
- **점수**: 1 point
- **태그**: `macos` `unicode` `korean` `cli` `developer-tools`

## 상세 요약

mrg("멕레기" — macOS + 쓰레기의 합성어)는 macOS에서 발생하는 한글 자모 분리 현상과 각종 잡다한 메타데이터 파일을 정리하는 Python CLI 유틸리티이다.

### 핵심 기능
- **유니코드 NFC 정규화(`--bad-unicode`)**: macOS의 NFD 유니코드로 인한 한글 자모 분리(ㅎㅏㄴㄱㅡㄹ) 문제를 NFC로 정규화하여 해결
- **.DS_Store 삭제(`--ds-store`)**: Finder가 폴더를 열 때 생성하는 .DS_Store 파일 제거
- **._* 파일 삭제(`--dot`)**: macOS가 메타데이터/인덱싱용으로 생성하는 ._* 파일 제거
- **`--all` 플래그**: 위 세 가지 정리를 한번에 수행
- **ANSI 컬러 지원**: 터미널에서 직관적 상태 표시 (NO_COLOR 환경 변수로 비활성화 가능)
- **분석 리포트**: 스캔/정리 결과를 예쁜 리포트 또는 JSON 형식으로 제공
- **Python API**: 파이썬 모듈로도 사용 가능
- **외부 의존성 없음**: 표준 라이브러리만 사용

### 설치
```bash
brew tap ilotoki0804/homebrew-mrg && brew install mrg
# 또는
uvx mrg
```

### 안전 모드
인자 없이 실행하면 스캔 모드(파일 변경 없음)로 디렉토리 상태만 조사.

## Soo에게 의미 있는 이유

한국어 macOS 사용자의 오래된 고통인 자모 분리 문제를 CLI로 깔끔하게 해결하는 도구. 크로스 플랫폼 파일 공유 시 유니코드 정규화는 필수이며, 특히 Git 저장소에서 한글 파일명 문제를 방지할 수 있다.
