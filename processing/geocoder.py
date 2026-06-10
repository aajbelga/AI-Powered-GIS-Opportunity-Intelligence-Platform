from geopy.geocoders import Nominatim
import psycopg2
import time

geolocator = Nominatim(user_agent="gis_opportunity_platform")

conn = psycopg2.connect(
    database="opportunity_intelligence_db",
    user="postgres",
    password="1234567890",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

cur.execute("""
SELECT id, location
FROM opportunities
WHERE latitude IS NULL
""")

rows = cur.fetchall()

for row in rows:
    record_id = row[0]
    location_name = row[1]

    try:
        location = geolocator.geocode(location_name)

        if location:
            lat = location.latitude
            lon = location.longitude

            cur.execute("""
            UPDATE opportunities
            SET latitude=%s,
                longitude=%s
            WHERE id=%s
            """, (lat, lon, record_id))

            print(f"{location_name} -> {lat}, {lon}")

        time.sleep(1)

    except Exception as e:
        print(location_name, e)

conn.commit()

cur.close()
conn.close()

print("\nGeocoding Completed!")