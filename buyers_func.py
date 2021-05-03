import connection as c 
import mysql.connector
from products import Products
from colorama import Fore,Style


def readProductInfo():
    conn = c.returnConnection()
    all_cars=[]
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products where product_status = 'A' " )
        for row in cursor:
            car_product = Products()
            car_product.setId(row[0])
            car_product.setMake(row[1])
            car_product.setModel(row[2])
            car_product.setYear(row[3])
            car_product.setColor(row[4])
            car_product.setPrice(row[5])
            all_cars.append(car_product)

            
        cursor.close()
        conn.close()
        return all_cars
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error)



def insertProductInfo(make, model, year, color, price, status):
    conn = c.returnConnection()
    try:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO products (product_make, product_model, product_year, product_color, product_price, product_status) VALUES ('{make}', '{model}', {year}, '{color}','{price}','{status}')")
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

def getCarMake():
    conn = c.returnConnection()
    all_cars=[]
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT distinct product_make FROM products where product_status = 'A' " )
        counter = 1
        for row in cursor:
            print(f'{counter}.{row[0]}')
            counter  += 1


            
        cursor.close()
        conn.close()
        return all_cars
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error)

def carDetails(inputCarMake):
    conn = c.returnConnection()
    all_cars=[]
    try:
        cursor = conn.cursor()
        cursor.execute(f" SELECT * FROM products where product_status = 'A' and product_make = '{inputCarMake}' " )
        for row in cursor:
            car_product = Products()
            car_product.setId(row[0])
            car_product.setMake(row[1])
            car_product.setModel(row[2])
            car_product.setYear(row[3])
            car_product.setColor(row[4])
            car_product.setPrice(row[5])
            all_cars.append(car_product)

            
        cursor.close()
        conn.close()
        return all_cars
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error)

def  carSold(inputId,notes, discountedprice, taxpercentage, taxamount,totalamount,customer_id):
    conn = c.returnConnection()
    all_cars=[]
    try:
        cursor = conn.cursor()
        cursor.execute(f" UPDATE products set product_status = 'S' where product_id = {inputId} " )
        cursor.execute(f" INSERT INTO orders (customer_id, product_id, order_notes, order_discountedprice, order_taxpercentage, order_taxamount,order_totalprice) VALUES ('{customer_id}','{inputId}', '{notes}', '{discountedprice}','{taxpercentage}','{taxamount}','{totalamount}')" )

        conn.commit()
        cursor.execute(f" SELECT * FROM products where product_id = '{inputId}' " )
        for row in cursor:
            car_product = Products()
            car_product.setId(row[0])
            car_product.setMake(row[1])
            car_product.setModel(row[2])
            car_product.setYear(row[3])
            car_product.setColor(row[4])
            car_product.setPrice(row[5])
            all_cars.append(car_product)

            
        cursor.close()
        conn.close()
        return all_cars
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error)

def selectedCarDetails(inputId):
    conn = c.returnConnection()
    car_product = Products()
    try:
        cursor = conn.cursor()
        cursor.execute(f" SELECT * FROM products where product_id = '{inputId}' " )
        for row in cursor:
            car_product.setId(row[0])
            car_product.setMake(row[1])
            car_product.setModel(row[2])
            car_product.setYear(row[3])
            car_product.setColor(row[4])
            car_product.setPrice(row[5])

            
        cursor.close()
        conn.close()
        return car_product
    except (Exception, mysql.connector.Error) as error:
        print('Error while fetching data from mySQL', error)