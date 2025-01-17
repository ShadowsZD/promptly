import psycopg2
import pandas as pd
from psycopg2 import sql

HOST = "localhost"
PORT = 5432
USER = "test_user"
PASSWORD = "test_pass"
DB_NAME = "test_db"

def create_connection(db_name: str):
    """
        Creates a connection to postgresql DB and returns it.
    """

    conn = psycopg2.connect(
            dbname=db_name,
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD
        )
    conn.autocommit = True
    return conn

def create_db(db_name: str):
    """
        Creates a new database with provided name
    """

    #create connection on default database to create new db
    conn = create_connection("postgres")

    try:
        cursor = conn.cursor()

        cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))
        print(f"Database '{db_name}' created successfully.")

    except psycopg2.Error as e:
        print(f"Error: {e}")

    finally:
        if cursor:
            cursor.close()
        conn.close()

def create_table(db_name:str, query_location: str):
    conn = create_connection(db_name)

    with open(query_location, 'r') as file:
        create_table_sql = file.read()

    try:
        cursor = conn.cursor()

        cursor.execute(create_table_sql)
        print(f"Table from {query_location} created successfully.")

    except psycopg2.Error as e:
        print(f"Error: {e}")

    finally:
        if cursor:
            cursor.close()
        conn.close()


def insert_csv(db_name:str, csv_file: str, table_name: str):

    conn = create_connection(db_name)
    cursor = conn.cursor()

    df = pd.read_csv(csv_file)

    headers = list(df.columns)
    columns = ", ".join(headers)

    with open(csv_file, 'r', encoding='utf-8') as file:
        cursor.copy_expert(f"COPY {table_name} ({columns}) FROM STDIN WITH CSV HEADER", file)
        print(f"CSV data for {table_name} loaded successfully.")

def insert_sql(db_name:str, sql_file_path: str):

    conn = create_connection(db_name)
    cursor = conn.cursor()

    with open(sql_file_path, 'r') as file:
        query = file.read()

        try:
            cursor.execute(query)
            print("SQL query executed successfully and data inserted.")
        except Exception as e:
            conn.rollback()
            print(f"Error occurred: {e}")

        finally:
            cursor.close()
            conn.close()
    

def main():

    create_db(DB_NAME)

    create_table(DB_NAME, "table_creation/raw_patient.sql")
    insert_csv(DB_NAME, "patient.csv", "raw_patient")

    create_table(DB_NAME, "table_creation/fhir_patient.sql")
    #insert_sql(DB_NAME, "data_insert/fhir_patient_drop_empty.sql")
    insert_sql(DB_NAME, "data_insert/raw_to_fhir_patient.sql")


if __name__ == '__main__':
    main()
