# src/db_test.py
# this is just a test file to check if the connection to the database is working
import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="mydb",
        user="postgres",
        password="postgres"
    )
    cur = conn.cursor()
    cur.execute("SELECT version();")
    version = cur.fetchone()
    print("Connected to:", version[0])
    cur.close()
    conn.close()
except Exception as e:
    print("Connection failed:", e)