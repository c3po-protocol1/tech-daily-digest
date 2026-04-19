# Claude Opus 4.6 → 4.7 시스템 프롬프트 변경사항 분석

- **출처**: [Simon Willison's Weblog](https://simonwillison.net/2026/Apr/18/opus-system-prompt/)
- **HN 토론**: [Hacker News](https://news.ycombinator.com/item?id=47823270)
- **HN 점수**: ⭐ 152점
- **태그**: `#AI` `#Anthropic` `#Claude` `#시스템프롬프트`

## 요약

Simon Willison이 Anthropic의 공개된 시스템 프롬프트 아카이브를 기반으로, Claude Opus 4.6(2026년 2월 5일)에서 4.7(2026년 4월 16일)로의 시스템 프롬프트 변경사항을 상세히 분석한 글이다.

**주요 변경사항:**
1. **"개발자 플랫폼" → "Claude Platform"으로 명칭 변경**
2. **새 도구 추가**: Claude in Chrome(브라우징 에이전트), Claude in Excel(스프레드시트 에이전트), **Claude in Powerpoint**(슬라이드 에이전트) 추가. Claude Cowork가 이들을 도구로 사용 가능
3. **아동 안전 섹션 대폭 확장**: 한 번 거부한 요청에 대해 이후 대화 전체에서 극도의 주의 적용
4. **덜 끈질기게(Less pushy)**: 사용자가 대화를 끝내겠다고 하면 머물기를 요청하지 않도록 지시
5. **모호함은 도구로 해결**: 세부사항이 불명확할 때 사용자에게 묻기보다 **tool_search**를 먼저 호출하여 해결 시도
6. **간결한 응답 권장**: 길고 압도적인 응답 대신 핵심에 집중
7. **이모트/특정 단어 사용 금지 제거**: "genuinely", "honestly" 등의 금지어 제거 (모델 자체가 개선됨)
8. **식이장애 관련 새 섹션**: 구체적인 수치/목표 제공 금지
9. **예/아니오 강요 방어**: 복잡한 이슈에 대해 단순 답변 거부 가능
10. **트럼프 대통령 관련 문구 삭제**: 모델의 지식 컷오프가 업데이트되어 불필요해짐

**Claude 도구 목록 (총 23개):**
`ask_user_input_v0`, `bash_tool`, `conversation_search`, `create_file`, `fetch_sports_data`, `image_search`, `message_compose_v1`, `places_map_display_v0`, `places_search`, `present_files`, `recent_chats`, `recipe_display_v0`, `recommend_claude_apps`, `search_mcp_registry`, `str_replace`, `suggest_connectors`, `view`, `weather_fetch`, `web_fetch`, `web_search`, `tool_search`, `visualize:read_me`, `visualize:show_widget`

## Soo에게 의미 있는 이유

시스템 프롬프트 엔지니어링의 실전 사례로, Anthropic이 모델 행동을 어떻게 제어하는지 보여준다. 특히 "도구로 모호함 해결" 패턴은 에이전트 설계에 직접 적용 가능한 인사이트이다. AInD에서 프롬프트 설계 가이드라인 수립 시 참고 필수.
