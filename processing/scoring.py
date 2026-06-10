import psycopg2

# Simple scoring rules
scores = {
    "Transportation": 90,
    "Energy": 85,
    "Infrastructure": 80,
    "Smart City": 75,
    "Roadways": 70
}

conn = psycopg2.connect(
    database="opportunity_intelligence_db",
    user="postgres",
    password="1234567890",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

cur.execute("""
SELECT id, title, location, category
FROM news
""")

rows = cur.fetchall()

for row in rows:
    news_id, title, location, category = row

    score = scores.get(category, 50)

    cur.execute("""
    INSERT INTO opportunities
    (project_name, location, score)
    VALUES (%s, %s, %s)
    """, (title, location, score))

conn.commit()

print("Opportunity scores generated successfully!")

cur.close()
conn.close()