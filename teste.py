import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()



try:
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    print("Connection successful!")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if 'conn' in locals():
        conn.close()
