import pandas as pd
import psycopg2

excel_file = "data.xlsx"  

df = pd.read_excel(excel_file)

print("Excel Data Loaded:")
print(df)

try:
    connection = psycopg2.connect(
        host="localhost",
        port="5432",
        database="demo",
        user="postgres",
        password="yourpassword"
    )
    cursor = connection.cursor()
    print("\nConnected to PostgreSQL")
except Exception as e:
    print("Error connecting:", e)
    exit()

try:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS excel_data (
            id SERIAL PRIMARY KEY,
            column1 VARCHAR(255),
            column2 VARCHAR(255),
            column3 VARCHAR(255)
        );
    """)
    connection.commit()
    print("Table ready")
except Exception as e:
    print("Error creating table:", e)

try:
    for index, row in df.iterrows():
        cursor.execute("""
            INSERT INTO excel_data (column1, column2, column3)
            VALUES (%s, %s, %s);
        """, (row[0], row[1], row[2]))

    connection.commit()
    print("Data inserted successfully!")
except Exception as e:
    print("Error inserting:", e)

cursor.close()
connection.close()
print("Done.")
