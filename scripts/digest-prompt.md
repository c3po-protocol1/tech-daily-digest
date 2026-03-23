# Daily Digest Generation Standard

## Sources & Counts
- **Hacker News**: Top 5 stories by score
- **GeekNews**: Top 10 stories (tech-focused, Korean community)
- **GitHub Trending**: Top 10 repositories by daily stars

## Folder Structure
```
YYYY/MM/DD/
├── README.md                     ← Index with links to all articles
├── hackernews/{slug}.md          ← 5 individual files
├── geeknews/{slug}.md            ← 10 individual files
└── github-trending/{slug}.md     ← 10 individual files
```

## Individual Article Format
Each .md file must contain (minimum 15 lines of content):

```markdown
# {Title}

- **출처:** [{domain}]({url})
- **HN/GN 토론:** [{discussion-url}]({url}) · ⬆️ {score}
- **태그:** `#Tag1` `#Tag2` `#Tag3`

---

## 핵심 요약

{Detailed summary - minimum 10 paragraphs covering:
- What it is and why it matters
- Technical details and architecture
- Community reaction and debate
- Broader industry implications}

## Soo에게 의미 있는 이유

{1-2 paragraphs connecting to AInD consulting, developer trends, or Soo's work}
```

## Rules
1. Write summaries in Korean
2. Each article file must be minimum 15 lines (content area)
3. Include source links, discussion links, and tags
4. Always include "Soo에게 의미 있는 이유" section
5. For items trending 2+ consecutive days, mark with 🔥 and compare growth
6. README.md serves as index linking to all individual files
7. Remove any old single-file digest.md format
8. Slug format: lowercase-english-with-dashes (no dates in filename)

## Schedule
Run daily at 08:00 KST. Data collection → File creation → README index → Git commit.
