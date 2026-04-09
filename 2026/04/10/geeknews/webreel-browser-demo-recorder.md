# webreel — 브라우저 데모를 MP4 영상으로 자동 녹화하는 CLI

- **출처**: [GitHub](https://github.com/vercel-labs/webreel)
- **GeekNews**: [토론](https://news.hada.io/topic?id=28335) (11 points)
- **태그**: `#devtools` `#video` `#automation` `#vercel`

## 상세 요약

Vercel Labs가 만든 브라우저 데모 영상 자동 녹화 도구. JSON 설정에 클릭·타이핑·드래그 등 액션을 정의하면, 헤드리스 Chrome이 ~60fps로 캡처 후 ffmpeg으로 인코딩.

**주요 기능:** 커서 오버레이 + 키스트로크 HUD, 사운드 이펙트, 드래그 앤 드롭, 폼 필링, GIF 출력. Chrome과 ffmpeg는 첫 사용 시 `~/.webreel`에 자동 다운로드.

**사용법:** `npx webreel init --name my-video --url https://example.com` → `npx webreel record`

제품 데모, 튜토리얼, 변경 사항 소개 영상을 스크립트화하여 재현 가능하게 만드는 도구.

## Soo에게 의미 있는 이유

제품 데모 영상을 코드로 관리할 수 있게 해주는 도구. 컨설팅 프로젝트의 데모 자동화에 활용 가능.
