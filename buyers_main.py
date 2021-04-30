import os  
from os import system 
import mysql.connector
import buyers_Ops as dbops
#import connection as c

system('cls')

# conn = c.returnConnection()
# cursor = conn.cursor()

buyorsellList = ['Buy', 'Sell']

counter = 1

# cursor.execute('SELECT * FROM products')
# dbresult = conn.fetchone()

# for row in dbresult:
#     print(row)

print('Would you like to Buy or Sell?: ')
for buyorsell in buyorsellList :
    print(f'{counter}. {buyorsell}')
    counter += 1
choice = int(input('Select one above Dude >> '))

if (choice == 1):
    dbops.BuyOperation1()     ########## make def
elif (choice == 2):
    dbops.SellOperation1()   ########## make def
else:
    print('We are stealing your info, muhahahahaaha')
