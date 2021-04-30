import connection as c 
import mysql.connector


def readProductInfo():
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM products')
        for row in cursor:
            print(f'''
            id .............. {row[0]}  
            Make ............ {row[1]}   
            Year ............ {row[2]}
            Model............ {row[3]}
            Color ........... {row[4]}  
            Price ........... {row[5]}      
            ''')
        cursor.close()
        conn.close()
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error)

def insertProductInfo(make, model, year, color, price):
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO products (product_make, product_model, product_year, product_color, product_price) VALUES ('{make}', '{model}', {year}, '{color}','{price}')")
        conn.commit()
        readProductInfo()
        cursor.close()
        conn.close()
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error) 

def updateProduct(field, id, newValue):
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute(f"UPDATE products SET {field} = '{newValue}' WHERE user_id = {id}")
        conn.commit()
        readProductInfo()
        cursor.close()
        conn.close()
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error)
    
def deleteProduct(id):
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute(f'DELETE FROM products WHERE user_id = {id}')
        conn.commit()
        readProductInfo()
        cursor.close()
        conn.close()
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error)  