import os  
from os import system
import connection as c 
import mysql.connector
from mysql.connector import Error

# mydb = conn

system('cls')

conn = c.returnConnection()

# Prints just a single row
###########################
# selector = conn.cursor()

# selector.execute("SELECT product_make FROM products")

# dbresult = selector.fetchall()  # you can use the following: fetchone() , fetchmany() , and fetchall()

# for row in dbresult:
#     print(row)

# prints the whole table {fetchone} or prints whole table with total rows [fetchall()] -> pretty much the same thing
###########################

# def query_with_fetchone():
#     conn = c.returnConnection()
#     try:
#         cursor = conn.cursor()
#         cursor.execute("SELECT product_make FROM products") # * will pull all / product_make will pull the cars
        
#         row = cursor.fetchone()

#         # have only 4 rows active for all
#         # rows = cursor.fetchall()
#         # print('Total Row(s):', cursor.rowcount) # works with fetchall(), next 3 lines
#         # for row in rows:
#         #     print(row)

#         while row is not None:
#             print(f'{row}')
#             row = cursor.fetchone()

#     except Error as e:
#         print(e)

#     finally:
#         cursor.close()
#         conn.close()


# if __name__ == '__main__':
#     query_with_fetchone()

# top contender here: gives the date in the order i want
#############################

# cursor = conn.cursor()

# try:
#     sql_select_Query = "SELECT * FROM products"
#     cursor.execute(sql_select_Query)
#     # get all records
#     records = cursor.fetchall()

#     print("\nHere are your options to choose from:")
#     for row in records:
#         print("Id = ", row[0], )
#         print("Name = ", row[1])
#         print("Price  = ", row[2])
#         print("Purchase date  = ", row[3], "\n")

# except mysql.connector.Error as e:
#     print("Error reading data from MySQL table", e)
# finally:
#     cursor.close()
#     conn.close()

# creates a cursor that returns rows as dictionaries so we can access using column name
#############################

# cursor = conn.cursor(dictionary=True)

# try:
#     sql_select_Query = "SELECT * FROM products"
#     #creates a cursor that returns rows as dictionaries
#     #cursor = connection.cursor(dictionary=True)
#     cursor.execute(sql_select_Query)
#     records = cursor.fetchall()
    
#     print("Here are your options to choose from:")
#     for row in records:
#         id = row["product_make"]
#         print()
#         name = row["product_model"]
#         price = row["product_year"]
#         purchase_date = row["product_color"]
#         purchase_date1 = row["product_price"]
#         print(id, name, price, purchase_date, purchase_date1)

# except Error as e:
#     print("Error reading data from MySQL table", e)
# finally:
#      cursor.close()
#      conn.close()

#############################

cursor = conn.cursor()

try:
    # sql_Query = "SELECT product_price FROM products where product_id =%s"
    # product_id = (1,)
    # cursor.execute(sql_Query, product_id)
    
    #aother way?
    sql_select_query = "SELECT product_price FROM products where product_id =%s"
    product_id = int ( input ("Enter laptop Id") )
    cursor.execute(sql_select_query, (product_id,))
    
    record = cursor.fetchone()

    # selecting column value into variable
    price = float(record[0])
    print("Laptop price is : ", price)

except mysql.connector.Error as error:
    print("Failed to get record from database: {}".format(error))
finally:
     cursor.close()
     conn.close()