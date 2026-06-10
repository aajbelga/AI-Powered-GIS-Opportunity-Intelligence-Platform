import requests
import pandas as pd

API_KEY = "df5af46417ce4bb9b8ded893e2c2031c"

query = '''
("infrastructure project")
OR ("metro project")
OR ("highway project")
OR ("railway project")
OR ("solar park")
OR ("industrial corridor")
OR ("smart city")
'''

url = "https://newsapi.org/v2/everything"

params = {
    "q": query,
    "language": "en",
    "sortBy": "publishedAt",
    "pageSize": 50,
    "apiKey": API_KEY
}

response = requests.get(url, params=params)

data = response.json()

articles = []

for article in data.get("articles", []):
    articles.append({
        "title": article["title"],
        "source": article["source"]["name"],
        "published": article["publishedAt"],
        "description": article["description"]
    })

df = pd.DataFrame(articles)

print(df.head())

df.to_csv("data/live_news.csv", index=False)

print(f"\nCollected {len(df)} articles")