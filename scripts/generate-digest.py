#!/usr/bin/env python3
"""Tech Daily Digest - Fetch from HN, GeekNews, GitHub Trending"""

import json
import os
import sys
import subprocess
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
import concurrent.futures
import urllib.request

REPO_DIR = "/Users/c-3po/.openclaw/workspace-yoda/tech-daily-digest"
SEEN_FILE = os.path.join(REPO_DIR, "scripts", ".seen_urls")

def load_seen():
    if os.path.exists(SEEN_FILE):
        with open(SEEN_FILE) as f:
            return set(line.strip() for line in f if line.strip())
    return set()

def save_seen(seen):
    with open(SEEN_FILE, 'w') as f:
        urls = list(seen)[-2000:]
        f.write('\n'.join(urls) + '\n')

def fetch_url(url, timeout=10):
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode('utf-8', errors='replace')
    except Exception as e:
        print(f"  Warning: Failed {url}: {e}", file=sys.stderr)
        return None

def fetch_url_curl(url):
    """Fallback using curl for sites that block urllib"""
    try:
        result = subprocess.run(
            ['curl', '-sL', url, '-H', 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'],
            capture_output=True, text=True, timeout=15
        )
        return result.stdout if result.returncode == 0 else None
    except Exception as e:
        print(f"  Warning: curl failed {url}: {e}", file=sys.stderr)
        return None

def fetch_hn_item(item_id):
    data = fetch_url(f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json", timeout=5)
    if data:
        return json.loads(data)
    return None

def fetch_hacker_news(seen):
    print("=== Fetching Hacker News ===", file=sys.stderr)
    data = fetch_url("https://hacker-news.firebaseio.com/v0/topstories.json")
    if not data:
        return []
    
    ids = json.loads(data)[:30]
    items = []
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(fetch_hn_item, id_): id_ for id_ in ids}
        for future in concurrent.futures.as_completed(futures):
            item = future.result()
            if item and item.get('url') and item['url'] not in seen:
                items.append({
                    'title': item.get('title', ''),
                    'url': item['url'],
                    'score': item.get('score', 0),
                    'comments': item.get('descendants', 0),
                    'source': 'hackernews'
                })
                seen.add(item['url'])
    
    items.sort(key=lambda x: x['score'], reverse=True)
    return items

def fetch_geeknews(seen):
    print("=== Fetching GeekNews ===", file=sys.stderr)
    # Use curl as GeekNews blocks urllib
    data = fetch_url_curl("https://news.hada.io/rss/news")
    if not data:
        return []
    
    items = []
    try:
        ns = {'atom': 'http://www.w3.org/2005/Atom'}
        root = ET.fromstring(data)
        
        for entry in root.findall('atom:entry', ns):
            title_el = entry.find('atom:title', ns)
            link_el = entry.find('atom:link[@rel="alternate"]', ns)
            content_el = entry.find('atom:content', ns)
            
            if title_el is not None and link_el is not None:
                url = link_el.get('href', '')
                if url and url not in seen:
                    # Clean CDATA from title
                    title = title_el.text.strip() if title_el.text else ''
                    desc = ''
                    if content_el is not None and content_el.text:
                        # Strip HTML tags for summary
                        import re
                        desc = re.sub(r'<[^>]+>', '', content_el.text)[:300].strip()
                    
                    items.append({
                        'title': title,
                        'url': url,
                        'description': desc,
                        'source': 'geeknews'
                    })
                    seen.add(url)
    except ET.ParseError as e:
        print(f"  Warning: GeekNews parse error: {e}", file=sys.stderr)
    
    return items

def fetch_github_trending(seen):
    print("=== Fetching GitHub Trending ===", file=sys.stderr)
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    url = f"https://api.github.com/search/repositories?q=created:>{yesterday}&sort=stars&order=desc&per_page=15"
    data = fetch_url(url)
    if not data:
        return []
    
    items = []
    try:
        repos = json.loads(data)
        for repo in repos.get('items', [])[:15]:
            repo_url = repo.get('html_url', '')
            if repo_url and repo_url not in seen:
                items.append({
                    'name': repo.get('full_name', ''),
                    'url': repo_url,
                    'description': (repo.get('description', '') or '')[:200],
                    'stars': repo.get('stargazers_count', 0),
                    'language': repo.get('language') or 'Unknown',
                    'source': 'github_trending'
                })
                seen.add(repo_url)
    except json.JSONDecodeError:
        pass
    
    return items

def main():
    seen = load_seen()
    
    hn = fetch_hacker_news(seen)
    gn = fetch_geeknews(seen)
    gh = fetch_github_trending(seen)
    
    save_seen(seen)
    
    output = {
        'date': datetime.now().strftime('%Y-%m-%d'),
        'year': datetime.now().strftime('%Y'),
        'month': datetime.now().strftime('%m'),
        'hacker_news': hn,
        'geeknews': gn,
        'github_trending': gh
    }
    
    print(json.dumps(output, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
