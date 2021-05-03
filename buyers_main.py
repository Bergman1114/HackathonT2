import os  
from os import system 
from colorama import Fore,Style
import functionsb1 as fn
import buyers_func as dbfun
from products import Products
import buyers_calculation as buyers_calculation
import decimal as decimal

system('cls')

product_opt = []

def BuyOperation1():
    return dbfun.readProductInfo()



def addInventory():
    numberOfEntries = int(input('Enter number of car you want to sell >> '))
    print()
    for entry in range(numberOfEntries):
        print(f'------CAR # {entry + 1} -----')
        carProduct = Products()
        carMake = input('What is the make of car? >> ')
        carProduct.setMake(carMake)
        carModel= input('What is the model of car? >> ')
        carProduct.setModel(carModel)
        carYear = input('What is the year of car? >> ')
        carProduct.setYear(carYear)
        carColor = input('What is the color of car? >> ')
        carProduct.setColor(carColor)
        carPrice = input('What is the price of car? >> ')
        carProduct.setPrice(carPrice)
        product_opt.append(carProduct)

    for abc in product_opt:
        dbfun.insertProductInfo(abc.getMake(),  abc.getModel(), abc.getYear(), abc.getColor(), abc.getPrice(), abc.getStatus())
        print()
        print('Congratulations! Your car has been approved for the trading offer!')
        print()
        print('Your credit has been issued to your account. Thank You!')

print()
print(Fore.RED,f'*******************************************************')
print('                                                        ')
print('-------------  WELCOME TO Shwetas AUTO ----------------')
print('                                                          ')
print('*********************************************************')
print()
print(Style.RESET_ALL)
print('Cars that fit your budget!')   
print()    
print('Sell or trade your car at the best offer!')
print()
print('Please lOGIN to start selling or trading')

print()
print(Fore.YELLOW,f'******************************************')
print('               LOG-IN                       ')
print('******************************************')
print()
print(Style.RESET_ALL)

 
fn.LoginPage()
print()
print(Fore.CYAN,f'******************************************')
print('           BUYING OR TRADING                       ')
print('******************************************')
print()
print(Style.RESET_ALL)
print('These are type of services we provide:')

buyorsellList = ['Buy', 'Trade']

counter = 1

print('Would you like to Buy or Trade?: ')

for buyorsell in buyorsellList :
    print(f'{counter}. {buyorsell}')
    counter += 1
choice = int(input('Select one from above choices[1-2] >> '))


if (choice == 1):

    dbfun.getCarMake()
    car_make = input('Enter the car make you want to select >> ')

    print('Below are the cars available')
    all_cars = dbfun.carDetails(car_make)
    


    for i in range(len(all_cars)):
        car = all_cars[i]
        print(f' {car.make} {car.model} {car.year} {car.color} ${car.price} To Purchase Enter - {car.id} >> ')
        print()
    selectedCarId = int(input('Please enter Your selection >> '))
        
    isBuyerVeteran = input('Are you a veteran (y/n) >> ')
    tax_percent = decimal.Decimal(0.08) 
    
    selectedCarDetails = dbfun.selectedCarDetails(selectedCarId)
    #print(selectedCarDetails.price)
    print('Great Selection!You have selected the best car')
    print('Lets proceed to checkout')

    carPriceDetails = buyers_calculation.calculatePrice(selectedCarDetails.price, selectedCarDetails.color, isBuyerVeteran, tax_percent)

    customer_id = 1

    carSold = dbfun.carSold(selectedCarId, carPriceDetails.notes, carPriceDetails.disc_amount, 0.08, carPriceDetails.tax_amount,  carPriceDetails.final_price, customer_id)
    print()
    print(Fore.CYAN,f'*********************************************')
    print('            ORDER SUMMARY                    ')
    print('******************************************')
    print(Style.RESET_ALL)
    print(f'''
    MRP:...................            $ {selectedCarDetails.price} 
    Discounted Price:................. $ {carPriceDetails.disc_amount}  
    Bonus:..................... -      $ {carPriceDetails.bonus}   
    Taxes @ 8%:.....................   $ {round(carPriceDetails.tax_amount, 2)}     
    GrandTotal:................        $ {round(carPriceDetails.final_price, 2)}
    ''')


elif (choice == 2):
    print()
    print(Fore.MAGENTA,f'******************************************')
    print('             TRADING                      ')
    print('******************************************')
    print()
    print(Style.RESET_ALL)

    addInventory()

else:
    print('We are stealing your info!!')
    

print()
print(Fore.YELLOW,f'********************************************')
print('             APPRECIATION                    ')
print('******************************************')
print(Style.RESET_ALL)
print()
print('Thank You For Your Business.')
print()
print('Your Order Was Completed Successfully.')
print()
print('An email receipt including the details about your order has been')
print()
print('sent to your email address provided. Please keep it for your records. ')
print()
print(Fore.RED,f'***********************************************************************')
print('-------------- Thank You Again! We hope to see again soon!  -------')
print('***********************************************************************')
