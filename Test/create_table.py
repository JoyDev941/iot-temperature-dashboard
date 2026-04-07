import psycopg2

conn = psycopg2.connect(
    host = "localhost",
    database="x",#
    user="x",#
    password="x"#
)

cur = conn.cursor()

# Create a table (example for temperature readings)
cur.execute("""
    CREATE TABLE IF NOT EXISTS temperature_data (
    id SERIAL PRIMARY KEY,
    temperature INTEGER NOT NULL,
    humidity INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

# Commit changes and close
conn.commit()
cur.close()
conn.close()

print("Table 'temperature_data' created successfully!")