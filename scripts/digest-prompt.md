You are generating the daily tech digest. You have been given raw JSON data from three sources: Hacker News, GeekNews, and GitHub Trending.

Your task:
1. Read the JSON data
2. Categorize each item into a topic (e.g., ai-ml, web-dev, devops, security, programming-languages, open-source, startups, databases, mobile, cloud, etc.)
3. Create markdown files organized as: {YEAR}/{MONTH}/{source}/{topic}/{DATE}-{slug}.md
4. Each folder must not exceed 10 files. If a topic would have more than 10, split into subtopics
5. Each MD file should contain:
   - Title as H1
   - Source link
   - Brief summary (2-3 sentences)
   - Why it matters (1 sentence)
   - Tags
6. After creating files, git add, commit, and push to origin main

Sources map:
- hackernews → "hackernews"
- geeknews → "geeknews"  
- github_trending → "github-trending"

Keep summaries concise and informative. Write in English. For GeekNews Korean titles, translate to English and keep original in parentheses.
