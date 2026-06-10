import psycopg2

try:
    conn = psycopg2.connect(
        database="opportunity_intelligence_db",
        user="postgres",
        password="1234567890",  # Replace with your password
        host="localhost",
        port="5432"
    )

    print("Database Connected Successfully!")

    conn.close()

except Exception as e:
    print("Connection Error:")
    print(e)