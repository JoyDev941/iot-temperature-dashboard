import psycopg2
import pandas as pd

# Connect to your database
con = psycopg2.connect(
    host="localhost",
    database="tempdb",
    user="lan_serv",
    password="esptemp32"
)
cur = con.cursor()

# Fetch the first 10 rows
cur.execute("SELECT * FROM temperature_data ORDER BY created_at ASC LIMIT 10;")
rows = cur.fetchall()

# Convert to pandas DataFrame
df = pd.DataFrame(rows, columns=["id", "temperature", "humidity", "created_at"])

# Save as Feather file
df.to_feather("temperature_data_first10.feather")

cur.close()
con.close()

print("Saved first 10 readings to Feather file!")