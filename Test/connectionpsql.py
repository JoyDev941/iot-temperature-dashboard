import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="tempdb",
    user="server",
    password="esptemp32"
)
cur = conn.cursor()
cur.execute("SELECT version();")
print(cur.fetchone())
cur.close()
conn.close()