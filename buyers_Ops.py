import os 
import buyers_func as dbfun
from os import system 
from products import Products
from colorama import Fore,Style

product_opt = []
print()
print(Fore.MAGENTA,f'********************************************')
print('               BUYING                       ')
print('******************************************')
print()
print(Style.RESET_ALL)

car_make = input('Enter the car make you want to select >> ')

print('Below are the cars available')
all_cars = dbfun.carDetails(car_make)
for i in range(len(all_cars)):
    car = all_cars[i]
    print(f' {car.make} {car.model} {car.year} {car.color} ${car.price} To Purchase Enter - {car.id} >> ')
print()
selectedCar = int(input('Please enter Your selection >> '))

carSold = dbfun.carSold(selectedCar)
for i in range(len(carSold)):
    car = carSold[i]
    print(f' {car.make} {car.model} {car.year} {car.color} ${car.price} To Purchase Enter - {car.id} >> ')

