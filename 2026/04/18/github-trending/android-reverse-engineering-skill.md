# android-reverse-engineering-skill — Claude Code용 Android 리버스 엔지니어링 스킬

- **GitHub**: [SimoneAvogadro/android-reverse-engineering-skill](https://github.com/SimoneAvogadro/android-reverse-engineering-skill)
- **스타**: ⭐ 2,718 | **언어**: Shell
- **태그**: `#Android` `#리버스엔지니어링` `#ClaudeCode` `#보안`

## 요약

APK/XAPK/JAR/AAR 파일을 디컴파일하고 **앱이 사용하는 HTTP API를 자동 추출**하는 Claude Code 스킬이다.

### 주요 기능

- jadx와 Fernflower/Vineflower로 **디컴파일** (단일 또는 비교 모드)
- **API 추출·문서화**: Retrofit 엔드포인트, OkHttp 호출, 하드코딩 URL, 인증 헤더/토큰
- **호출 흐름 추적**: Activity/Fragment → ViewModel → Repository → HTTP 호출
- **앱 구조 분석**: 매니페스트, 패키지, 아키텍처 패턴
- **난독화 코드 처리**: ProGuard/R8 출력 탐색 전략

### 설치

```bash
/plugin marketplace add SimoneAvogadro/android-reverse-engineering-skill
/plugin install android-reverse-engineering@android-reverse-engineering-skill
```

### 사용법

```bash
/decompile path/to/app.apk
```

## Soo에게 의미 있는 이유

Agent Skills의 실전 활용 사례. 특정 도메인(Android 보안 분석)에 특화된 스킬이 어떻게 설계되는지 참고할 수 있다.
