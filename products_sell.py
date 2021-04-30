import os 
import proSqlOps as prosql 
from os import system 
from product import Product

products = []
def insertProductOperation():
    numberOfEntries = int(input('Enter number of records >> '))
    for entry in range(numberOfEntries):
        print(f'--- Product # {entry + 1} ---')
        product = Product()
        product = input('What is the make of car? >> ')
        make.setMake(make)
        model= int(input('What is the model of car? >> '))
        product.setModel(model)
        year = input('What is the year of car? >> ')
        product.setYear(year)
        color = input('What is the color of car? >> ')
        product.setPhone(color)
        products.append(product)
        print()
    for product in products:
        prosql.insertProductInfo(product.getMake(), product.getYear(), product.getModel(), product.getColor())