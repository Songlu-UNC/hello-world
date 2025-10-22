import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host="localhost",
    database="CHIP-690-WEB",
    user="postgres",
    password="",
    port="5432"  # Default is 5432 if not specified
)

cur = conn.cursor()
cur.execute("SELECT * FROM accounts")
rows = cur.fetchall()
for row in rows:
    print(row)

