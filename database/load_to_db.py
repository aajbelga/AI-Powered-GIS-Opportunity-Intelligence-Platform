import pandas as pd
import psycopg2

conn = psycopg2.connect(
    database="opportunity_intelligence_db",
    user="postgres",
    password="1234567890",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

df = pd.read_csv("data/news_data.csv")

for _, row in df.iterrows():
    cur.execute(
        """
        INSERT INTO news(title, location, category, source)
        VALUES (%s, %s, %s, %s)
        """,
        (
            row["title"],
            row["location"],
            row["category"],
            row["source"]
        )
    )

conn.commit()

print(f"{len(df)} records inserted successfully!")

cur.close()
conn.close()