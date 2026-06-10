import folium
import psycopg2

conn = psycopg2.connect(
    database="opportunity_intelligence_db",
    user="postgres",
    password="1234567890",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

cur.execute("""
SELECT project_name,
       location,
       latitude,
       longitude,
       score
FROM opportunities
""")

rows = cur.fetchall()

# India centered map
india_map = folium.Map(
    location=[22.5, 78.9],
    zoom_start=5
)

for row in rows:

    project_name = row[0]
    location = row[1]
    latitude = row[2]
    longitude = row[3]
    score = row[4]

    folium.Marker(
        [latitude, longitude],
        popup=f"""
        <b>{project_name}</b><br>
        Location: {location}<br>
        Score: {score}
        """,
        tooltip=project_name
    ).add_to(india_map)

india_map.save("maps/opportunity_map.html")

print("Map generated successfully!")
print("Saved as maps/opportunity_map.html")

cur.close()
conn.close()