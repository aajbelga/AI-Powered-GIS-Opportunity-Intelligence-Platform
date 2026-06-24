import pandas as pd
import psycopg2

# Read extracted locations
df = pd.read_csv("data/location_news.csv")

# Location Importance
location_scores = {
    "Delhi": 25,
    "Mumbai": 25,
    "Bengaluru": 20,
    "Chennai": 20,
    "Hyderabad": 20,
    "Gujarat": 20,
    "Maharashtra": 20,
    "Kerala": 15,
    "Odisha": 15,
    "Kolkata": 15,
    "Sikkim": 10,
    "Cuddalore": 10
}

# Infrastructure Project Types
project_keywords = {
    "metro": 25,
    "airport": 25,
    "railway": 22,
    "highway": 20,
    "port": 20,
    "solar": 18,
    "industrial corridor": 25,
    "smart city": 20,
    "infrastructure": 15,
    "road": 15
}

# Investment / Scale Keywords
scale_keywords = {
    "crore": 10,
    "billion": 20,
    "million": 15,
    "investment": 15,
    "expansion": 10,
    "approved": 10,
    "launches": 10,
    "foundation stone": 10,
    "development project": 15
}

# Frequency of locations
location_frequency = (
    df["location"]
    .value_counts()
    .to_dict()
)

conn = psycopg2.connect(
    database="opportunity_intelligence_db",
    user="postgres",
    password="1234567890",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

cur.execute("TRUNCATE TABLE opportunities RESTART IDENTITY")

for _, row in df.iterrows():

    project_name = row["article"]
    location = row["location"]

    score = 0

    # ------------------
    # Location Score
    # ------------------
    score += location_scores.get(location, 10)

    # ------------------
    # Project Type Score
    # ------------------
    title_lower = project_name.lower()

    for keyword, value in project_keywords.items():

        if keyword in title_lower:
            score += value

    # ------------------
    # Scale Score
    # ------------------
    for keyword, value in scale_keywords.items():

        if keyword in title_lower:
            score += value

    # ------------------
    # Frequency Score
    # ------------------
    freq = location_frequency.get(location, 1)

    frequency_score = min(freq * 5, 25)

    score += frequency_score

    # Cap score
    score = min(score, 100)

    cur.execute("""
    INSERT INTO opportunities
    (
        project_name,
        location,
        score
    )
    VALUES (%s,%s,%s)
    """,
    (
        project_name,
        location,
        score
    ))

conn.commit()

print("Opportunity scoring completed successfully!")

cur.close()
conn.close()