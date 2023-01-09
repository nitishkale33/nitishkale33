import psycopg2

def connection():
    connection = psycopg2.connect(
        user="postgres",
        password="Nitish",
        host="localhost",
        port="5432",
        database="postgres")
    return connection