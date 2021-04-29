import os, datetime
from os import system
from datetime import *
system('cls')

username = 'Kite'
password = 'pass'
path = './HackathonT2/logs.txt'

user = input('What is your username? >> ')
passwd = input('What is your password? >> ')

def printSuccessOrNot(message):
    if (message == 'You'):
        with open(path, 'a') as log:
            log.write(f'\nUser {user} tried to log in on {datetime.now()} - Result: {message}')
            log.close()
    else:
        with open(path, 'a') as log:
            log.write(f'\nUser {user} tried to log in on {datetime.now()} - Result: {message}')
            log.close()

if(user == username and passwd == password):
    print(f'Hello {user}, you are fully authenticated')
    printSuccessOrNot('Success')
else:
    print('The combination of the username and password you used does not match our records')
    printSuccessOrNot('Failed')

    # testing for push