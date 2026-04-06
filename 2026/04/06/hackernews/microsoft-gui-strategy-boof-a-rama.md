# Microsoft는 Petzold 이후 일관된 GUI 전략을 가진 적이 없다

- **출처**: [Jeffrey Snover's Blog](https://www.jsnover.com/blog/2026/03/13/microsoft-hasnt-had-a-coherent-gui-strategy-since-petzold/)
- **HN 토론**: [Hacker News](https://news.ycombinator.com/item?id=47651703) (502 points, 326 comments)
- **태그**: `#Microsoft` `#GUI` `#플랫폼전략` `#역사`

## 요약

Jeffrey Snover(PowerShell 창시자, Microsoft 전 기술 펠로우)가 Microsoft의 30년에 걸친 GUI 프레임워크 혼란사를 회고하는 글이다.

### 핵심 논점

**Petzold 시대의 명확성 (1988)**
- Charles Petzold의 *Programming Windows*가 Win16/Win32 API 기반의 단일하고 명확한 답을 제공했던 시절
- "플랫폼이 'UI를 어떻게 만들어야 하나요?'라는 질문에 10초 안에 답하지 못하면, 그 플랫폼은 개발자를 실패시킨 것" — 핵심 테제

**객체지향 열풍 (1992-2000)**
- MFC, OLE, COM, ActiveX가 난립하면서 인지적 복잡성이 급증
- "기술 프리미티브를 팔면서 개발자에게 스토리를 알아서 만들라고 한 것"

**PDC 2003과 Longhorn의 붕괴**
- WPF(Avalon)의 비전은 훌륭했으나, 2004년 완전한 개발 리셋
- Windows 팀의 .NET에 대한 조직적 반감이 시작 → **13년간의 내전**

**Silverlight의 배신 (2007-2010)**
- 기술적으로는 성공했으나 비즈니스 전략 변경으로 개발자 통보 없이 폐기
- 개발자들이 컨퍼런스 Q&A에서 자신의 플랫폼이 폐기됨을 알게 된 사건

**Metro/UWP의 실패 (2012-현재)**
- Windows 팀과 .NET 팀이 서로 다른 건물에서 서로 다른 로드맵을 추진
- 17개의 GUI 기술이 공존하는 현재의 "boof-a-rama" (혼란) 상태

### 현재 Windows GUI 기술 목록 (17개)

Microsoft 네이티브: Win32, MFC, WinForms, WPF, WinUI 3, MAUI
하이브리드: Blazor Hybrid, WebView2
서드파티: Electron, Flutter, Tauri, Qt, React Native, Avalonia, Uno Platform, Delphi, Java Swing/JavaFX

### 저자의 교훈

모든 실패한 GUI 이니셔티브는 3가지 원인 중 하나로 귀결된다: 내부 팀 정치, 컨퍼런스 발표가 주도한 섣부른 플랫폼 베팅, 개발자에게 사전 경고 없는 비즈니스 전략 전환.

## Soo에게 의미 있는 이유

플랫폼 전략의 실패 사례로서 AInD 컨설팅에 시사점이 크다. 현재 AI 에이전트 프레임워크 시장도 비슷한 파편화 위험이 있으며, "하나의 명확한 답"을 제시하는 것의 중요성을 잘 보여준다. 컨설팅 클라이언트에게 기술 선택의 위험성을 설명할 때 좋은 역사적 사례가 된다.
