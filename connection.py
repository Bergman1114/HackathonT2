import mysql.connector, os
from os import getenv
from dotenv import load_dotenv
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

# def returnConnection():
#     conn = connect(
#         host = environ.get('DB_URL'),
#         user = environ.get('DB_USER'),
#         password = environ.get('DB_PASSWORD'),
#         database = environ.get('DB_NAME')
#     )
#     return conn


