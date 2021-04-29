import connection as c 
import mysql.connector
import os, datetime
from os import system
from datetime import *

system('cls')

def LoginPage(user):
    print('''
    THESE ARE THE OPTIONS:
    1. Exsiting Customer
    2. New Customer
    3. Exsisting Seller
    4. New Seller
    ''')
    choice = int(input('Select an option >> '))
        if( choice == 1 ):
            LoginEC()
        elif( choice == 2 ):
            NewCusAct()
        elif( choice == 3 ):
            login(user)
        elif( choice == 4 ):
            login(user)   
        else:
            print("Choose a valid option")
            LoginPage('')

def LoginEC():
    EUN = input("Enter The Username: ")
    PWD = input("Enter The Password: ")
        if( PWD == user.password):
            print("Welcome, you are logged in and fully authenticated : " + user.name)
        else:
            print("The username and password you used does not match our records")
            login(user)
        LoginPage('')

def NewCusAct():
    for u in range(New_user_info):
        userdata = {}
        print()
        print(f'ENTER TEXT HERE {counter}: ')
        username = input('Enter your user name >> ')
        userdata['UserName'] = username
        password = input('Enter your password >> ')
        userdata['Password'] = password
        Email = int(input('Enter your Email >> '))
        userdata['Email'] = Email
        userinfo.append(userdata)
        counter += 1
        print()

LoginPage('')

# username = 'Kite'
# password = 'pass'
# path = './HackathonT2/logs.txt'

# user = input('Please enter your username : ')
# passwd = input('Please enter your password : ')

# def UserLogYN(message):
#     if (message == 'Welcome'):
#         with open(path, 'a') as log:
#             log.write(f'\nUser {user} tried to log in on {datetime.now()} - Result: {message}')
#             log.close()
#     else:
#         with open(path, 'a') as log:
#             log.write(f'\nUser {user} tried to log in on {datetime.now()} - Result: {message}')
#             log.close()

# if(user == username and passwd == password):
#     print(f'Hello {user}, you are logged in and fully authenticated')
#     UserLogYN('Welcome')
# else:
#     print('The username and password you used does not match our records')
#     UserLogYN('Denied')