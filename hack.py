import mysql.connector
from mysql.connector import Error


def create_connection(host_name, username, password, db_name):
    connection = None 
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=username,
            passwd=password,
            database=db_name
        )
        print("Connection to MySql db successful!")
    except Error as e:
        print(str(e))
    
    return connection


def PartThreeShowTable():
    # create a connection to the db.
    host = "myncidatabase.ctyygtd4hi1r.us-east-1.rds.amazonaws.com"
    username = "adminw"
    password = "Yoni547941"
    dbname = "MyDatabase1"
    conn = create_connection(host, username, password, dbname)

    show_table_query = "SELECT * FROM seller"

    cursor = conn.cursor()
    table = None
    try:
        table = cursor.execute(show_table_query)
    except Error as e:
        print(str(e))
    
    print(table)


if __name__ == "__main__":
    PartThreeShowTable()




