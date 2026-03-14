#!/bin/bash
# Tech Daily Digest Generator
# Fetches top stories from HN, GeekNews, GitHub Trending
# Deduplicates against previous digests
# Organizes into categorized MD files

set -euo pipefail

REPO_DIR="/Users/c-3po/.openclaw/workspace-yoda/tech-daily-digest"
TODAY=$(TZ=Asia/Seoul date +%Y-%m-%d)
YEAR=$(TZ=Asia/Seoul date +%Y)
MONTH=$(TZ=Asia/Seoul date +%m)
SEEN_FILE="$REPO_DIR/scripts/.seen_urls"

cd "$REPO_DIR"
git pull --rebase origin main 2>/dev/null || true

# Initialize seen file if not exists
touch "$SEEN_FILE"

#--- Hacker News (top 30 stories via API) ---
echo "=== Fetching Hacker News ==="
HN_IDS=$(curl -s "https://hacker-news.firebaseio.com/v0/topstories.json" | python3 -c "import sys,json; ids=json.load(sys.stdin)[:30]; print(' '.join(map(str,ids)))")

HN_ITEMS=""
for id in $HN_IDS; do
  ITEM=$(curl -s "https://hacker-news.firebaseio.com/v0/item/${id}.json")
  URL=$(echo "$ITEM" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('url',''))" 2>/dev/null || echo "")
  
  # Skip if already seen
  if [ -n "$URL" ] && grep -qF "$URL" "$SEEN_FILE" 2>/dev/null; then
    continue
  fi
  
  TITLE=$(echo "$ITEM" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('title',''))" 2>/dev/null || echo "")
  SCORE=$(echo "$ITEM" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('score',0))" 2>/dev/null || echo "0")
  COMMENTS=$(echo "$ITEM" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('descendants',0))" 2>/dev/null || echo "0")
  
  if [ -n "$TITLE" ] && [ -n "$URL" ]; then
    HN_ITEMS="${HN_ITEMS}|${TITLE}|||${URL}|||${SCORE}|||${COMMENTS}"
    echo "$URL" >> "$SEEN_FILE"
  fi
done

#--- GeekNews (RSS) ---
echo "=== Fetching GeekNews ==="
GEEKNEWS_FEED=$(curl -s "https://news.hada.io/rss" 2>/dev/null || echo "")
GN_ITEMS=""
if [ -n "$GEEKNEWS_FEED" ]; then
  GN_ITEMS=$(echo "$GEEKNEWS_FEED" | python3 -c "
import sys, xml.etree.ElementTree as ET
seen = set(open('$SEEN_FILE').read().splitlines())
feed = sys.stdin.read()
try:
    root = ET.fromstring(feed)
    items = root.findall('.//item')[:20]
    for item in items:
        title = item.find('title')
        link = item.find('link')
        desc = item.find('description')
        if title is not None and link is not None:
            url = link.text.strip() if link.text else ''
            if url and url not in seen:
                t = title.text.strip() if title.text else ''
                d = desc.text.strip()[:200] if desc is not None and desc.text else ''
                print(f'{t}|||{url}|||{d}')
                seen.add(url)
    with open('$SEEN_FILE', 'a') as f:
        for u in seen:
            pass  # already appended inline
except Exception as e:
    print(f'ERROR: {e}', file=sys.stderr)
" 2>/dev/null || echo "")
  
  # Add GeekNews URLs to seen
  echo "$GN_ITEMS" | while IFS='|||' read -r t u d; do
    [ -n "$u" ] && echo "$u" >> "$SEEN_FILE"
  done
fi

#--- GitHub Trending ---
echo "=== Fetching GitHub Trending ==="
GH_TRENDING=$(curl -s "https://api.github.com/search/repositories?q=created:>$(date -v-1d +%Y-%m-%d 2>/dev/null || date -d '1 day ago' +%Y-%m-%d)&sort=stars&order=desc&per_page=15" 2>/dev/null || echo "")
GH_ITEMS=""
if [ -n "$GH_TRENDING" ]; then
  GH_ITEMS=$(echo "$GH_TRENDING" | python3 -c "
import sys, json
seen = set(open('$SEEN_FILE').read().splitlines())
try:
    data = json.load(sys.stdin)
    for repo in data.get('items', [])[:15]:
        url = repo.get('html_url', '')
        if url and url not in seen:
            name = repo.get('full_name', '')
            desc = repo.get('description', '')[:150] if repo.get('description') else ''
            stars = repo.get('stargazers_count', 0)
            lang = repo.get('language', 'Unknown')
            print(f'{name}|||{url}|||{desc}|||{stars}|||{lang}')
except Exception as e:
    print(f'ERROR: {e}', file=sys.stderr)
" 2>/dev/null || echo "")
  
  echo "$GH_ITEMS" | while IFS='|||' read -r n u d s l; do
    [ -n "$u" ] && echo "$u" >> "$SEEN_FILE"
  done
fi

# Output raw data for the AI to process
echo "===RAW_DATA_START==="
echo "---HN_START---"
echo "$HN_ITEMS"
echo "---HN_END---"
echo "---GN_START---"
echo "$GN_ITEMS"
echo "---GN_END---"
echo "---GH_START---"
echo "$GH_ITEMS"
echo "---GH_END---"
echo "===RAW_DATA_END==="
echo "DATE=$TODAY YEAR=$YEAR MONTH=$MONTH"
