import psycopg2

try:
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="1234567890",  # Replace with your password
        host="localhost",
        port="5432"
    )

    # Enable autocommit for CREATE DATABASE
    conn.autocommit = True

    cur = conn.cursor()

    # Create database
    cur.execute("""
        CREATE DATABASE opportunity_intelligence_db;
    """)

    print("Database Created Successfully!")

    cur.close()
    conn.close()

except Exception as e:
    print("Error:")
    print(e)