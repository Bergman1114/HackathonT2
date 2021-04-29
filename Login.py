import os, datetime
from os import system
from datetime import *
system('cls')

username = 'Kite'
password = 'pass'
path = './HackathonT2/logs.txt'

user = input('Please enter your username : ')
passwd = input('Please enter your password : ')

def logopt():
    print("Which would you like to access >> \n 1. Exsiting Customer \n 2. New Customer \n 3. Exsisting Seller \n 4. New Seller")
    choice = input()
    if choice == "1":
        UserLogYN()
    if chocie == "2":
        logopt()
    if chocie == "3":
        logopt()
    if chocie == "4":
        logopt()

def UserLogYN(message):
    if (message == 'Welcome'):
        with open(path, 'a') as log:
            log.write(f'\nUser {user} tried to log in on {datetime.now()} - Result: {message}')
            log.close()
    else:
        with open(path, 'a') as log:
            log.write(f'\nUser {user} tried to log in on {datetime.now()} - Result: {message}')
            log.close()

if(user == username and passwd == password):
    print(f'Hello {user}, you are logged in and fully authenticated')
    UserLogYN('Welcome')
else:
    print('The username and password you used does not match our records')
    UserLogYN('Denied')