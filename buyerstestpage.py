import connection as c 
import mysql.connector

# mydb = conn

conn = c.returnConnection()

selector = conn.cursor()

selector.execute("SELECT * FROM products")

dbresult = selector.fetchone()

for row in dbresult:
    print(row)