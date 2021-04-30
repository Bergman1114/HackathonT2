import os 
from os import system 
import products as proops
from colorama import Fore, Back, Style 
# import price 
# from price import *


system('cls')
print(Fore.RED,f'WELCOME TO CARZONE')
print()
print(f'Cars that fit your budget!')   
print()    
print(f'Sell or trade your car at the best offer!')
print()
print(f'Please login to start selling or trading')
print()
print()
print(Fore.CYAN,f'**********************************************************************************************************************')
print(f'********************************************************************************************************************************')
print(f'                                                USER LOG -IN                                                              ')
print(f'********************************************************************************************************************************')
print(f'********************************************************************************************************************************')
print()

#login functionality-bryan
print(Fore.YELLOW,f'********************************************************************************************************************')
print(f'********************************************************************************************************************************')
print(f'                                            BUYING OR TRADING                                                                   ')
print(f'********************************************************************************************************************************')
print(f'********************************************************************************************************************************')
print('These are type of service we provide')
counter = 1
buySellOperationList = ['Buy' , 'Sell']
for buySell in buySellOperationList:
    print(f'{counter}. {buySell}')
    counter += 1

buySellChoice = int(input('Select from the options you would like to perform[1-2]:>> '))
if (buySellChoice == 1):
    print(f'We see that you want to {buySellOperationList[0]} a car')
elif (buySellChoice == 2):
    print(f'Great! We see that you want to {buySellOperationList[1]} a car')
print(f'We can provide you the best car in your budget.')







# operationsList = ['Read', 'Insert', 'Update', 'Delete']

# counter = 1

# print('These are the operations that you can perform in our database: ')
# for operation in operationsList:
#     print(f'{counter}. {operation}')
#     counter += 1
# choice = int(input('Select one above >> '))

# if (choice == 1):
#     ops.readProductOperation()
# elif (choice == 2):
#     ops.insertProductOperation()
# elif (choice == 3):
#     ops.updateProductOperation()   
# elif (choice == 4):
#     ops.deleteProductOperation()
# else:
#     print('invalid selection')