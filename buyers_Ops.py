import os 
import buyers_func as dbfun
from os import system 
from products import Products
import connection as c 
import mysql.connector

system('cls')

# buyorsell_records = []

def BuyOperation1():
    dbfun.readProductInfo()

product_opt = []

def SellOperation1():
    numberOfEntries = int(input('What are you doing?!? >> '))
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
        product_opt.append(product)
        print()
    for product in product_opt:
        prosql.insertProductInfo(product.getMake(), product.getYear(), product.getModel(), product.getColor())