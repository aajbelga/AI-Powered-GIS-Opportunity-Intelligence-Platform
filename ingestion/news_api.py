import feedparser
import pandas as pd
from urllib.parse import quote

query = "infrastructure projects india"

rss_url = (
    f"https://news.google.com/rss/search?q={quote(query)}"
)

print("Fetching:", rss_url)

feed = feedparser.parse(rss_url)

print("Articles found:", len(feed.entries))

articles = []

for entry in feed.entries:

    articles.append({
        "title": entry.title,
        "link": entry.link
    })

df = pd.DataFrame(articles)

df.to_csv(
    "data/live_news.csv",
    index=False
)

print(df.head())
print(f"\nCollected {len(df)} articles")