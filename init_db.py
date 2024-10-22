import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import os

load_dotenv()
dbname = os.getenv("PG_dbname")
user = os.getenv("PG_user")
pw = os.getenv("PG_pw")
host = os.getenv("PG_host")
port = os.getenv("PG_port")
new_dbname = os.getenv("PG_new_dbname")

connect = psycopg2.connect(dbname=dbname, user=user, password=pw, host=host, port=port)
connect.autocommit = True

try:
    cursor = connect.cursor()
    cursor.execute(sql.SQL("SELECT 1 FROM pg_database WHERE datname = %s"),[new_dbname])
    exists = cursor.fetchone()
    
    if not exists:
        cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(new_dbname)))
        print(f"database {new_dbname} created.")
    
    connect.close()
    connect = psycopg2.connect(dbname=new_dbname, user=user, password=pw, host=host, port=port)
    cursor = connect.cursor()
    cursor.execute("CREATE EXTENSION IF NOT EXISTS vector")
    print(f"Vector plugin enabled on database {new_dbname}")
finally:
    cursor.close()
    connect.close()