import mysql.connector, os
from os import getenv
from dotenv import load_dotenv
from mysql.connector import Error
from mysql.connector import connect

load_dotenv()

def returnConnection():
    conn = connect(
        host = getenv('DB_HOST'),
        user = getenv('DB_USER'),
        password = getenv('DB_PASSWORD'),
        database = getenv('DB_NAME')
    )
    return conn

returnConnection()

# def connect():
#     conn = None
#     try:
#         conn = mysql.connector.connect(
#             host = getenv('DB_HOST'),
#             user = getenv('DB_USER'),
#             password = getenv('DB_PASSWORD'),
#             database = getenv('DB_NAME')
#         )
#         if conn.is_connected():
#             print('Connected to MySQL database')
#     except Error as e:
#         print(e)
#     finally:
#         if conn is not None and conn.is_connected():
#             conn.close()

# if __name__ == '__main__':
#     connect()


# def returnConnection():
#     conn = connect(
#         host = environ.get('DB_URL'),
#         user = environ.get('DB_USER'),
#         password = environ.get('DB_PASSWORD'),
#         database = environ.get('DB_NAME')
#     )
#     return conn


