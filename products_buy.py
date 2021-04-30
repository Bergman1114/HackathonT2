import os 
import proSqlOps as prosql 
from os import system 
from product import Product

system('cls')

#func.readUserInfo()
products = []
# fieldList = ['Make', 'Model', 'Year', 'Color']


def readProductOperation():
    prosql.readProductInfo()



# def insertProductOperation():
#     numberOfEntries = int(input('Enter number of records >> '))
#     for entry in range(numberOfEntries):
#         print(f'--- Product # {entry + 1} ---')
#         product = Product()
#         product = input('What is the make of car? >> ')
#         make.setMake(make)
#         model= int(input('What is the model of car? >> '))
#         product.setModel(model)
#         year = input('What is the year of car? >> ')
#         product.setYear(year)
#         color = input('What is the color of car? >> ')
#         product.setPhone(color)
#         products.append(product)
#         print()
#     for user in users:
#         prosql.insertProductInfo(product.getMake(), product.getYear(), product.getModel(), product.getColor())

# def updateProductOperation():
#     counter = 1
#     prosql.readProductInfo()
#     ProductId = int(input('what is the id of the user of which field you want to update? >> '))
    
#     while True:
#         print(f'There are the fields that you update for the userId : {productId}')
#         for field in fieldList:
#             print(f'{counter}. {field}')
#             counter += 1
    
#         selection = int(input('Select 1 option above >> '))
#         if (selection == 1):
#             newValue = input('What is the new value for Make? >> ')
#             prosql.updateUser('product_make', productId, newValue)
#         elif (selection == 2) :
#             newValue = input('What is the new value for Model? >> ')
#             prosql.updateUser('product_model', productId, newValue)
#         elif (selection == 3) :
#             newValue = input('What is the new value for Year? >> ')
#             prosql.updateUser('product_year', productId, newValue)
#         elif (selection == 4) :
#             newValue = input('What is the new value color? >> ')
#             proql.updateUser('product_color', productId, newValue)
#         else :
#             print("Please enter the correct value")

             
#         updateMore = input('Do you want to update any more field (Enter y) ')

#         if (updateMore == 'y' or updateMore == 'Y'):
#             counter = 1
#             continue
#         else :
#             break
    

# def deleteProductOperation():
#     prosql.readProductInfo()
#     productId = int(input('which productid do you want to delete? >> '))
#     prosql.deleteProduct(productId)