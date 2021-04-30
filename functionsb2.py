# import connection as c 
# import mysql.connector
import os, datetime
from os import system
from datetime import *
import logging

system('cls')

def LoginPage():
    print('''
    THESE ARE THE OPTIONS:
    1. Exsiting User
    2. New User
    3. Exit
    ''')
    choice = int(input('Select an option >> '))
    if( choice == 1 ):
        LoginEC() #login
    elif( choice == 2 ):
        NewCusAct()  #newuser 
    elif( choice == 3 ):
        print("Now Stealing your DATA...")
        sleep(2)
        exit()
    else:
        print("Choose a valid option")
        LoginPage('')


#####################################

# def LoginEC():
#     conn = c.returnConnection()
#     while True:
#         EUN = input("Enter The Username: ")
#         PWD = input("Enter The Password: ")
#         cursor = conn.cursor()
#         select_user = ("SELECT * FROM useract WHERE Username = ? AND Password = ?")
#         cursor.execute("SELECT user_password FROM useract WHERE username=%s", '{username}')
#         row = cursor.fetchone()
#         cursor.close()
#         conn.close()
#         break

# LoginPage()

######################################

# def LoginEC():
#     EUN = input("Enter The Username: ")
#     PWD = input("Enter The Password: ")
#     if( PWD == user.password):
#         print("Access, you are logged in and fully authenticated : " + user.name)
#     else:
#         print("The username and password you used does not match our records")
#         login(user)
#     LoginPage('')

# LoginPage('')


########################################


def LoginEC():
    logging.basicConfig(filename='logs.txt', level=logging.INFO)
    
    user = input('Please enter your username : ')
    passwd = input('Please enter your password : ')

    logging.info(f"Attempt to login: User name : {user} | Password : {passwd}")

    # path = './HackathonT2/logs.txt'
    # path = './HackathonT2/logs.txt'
    path = 'logs.txt'
    username = 'Kite' #['Kite', 'Shweta']
    password = 'pass1' #['pass1', 'pass2']



    def printAccessOrNot(message):
        if (message == 'Access'):
            with open(path, 'a') as log:
                log.write(f'\nUser {user} tried to log in on {datetime.now()} - Result: {message}')
                log.close()
        else:
            with open(path, 'a') as log:
                log.write(f'\nUser {user} tried to log in on {datetime.now()} - Result: {message}')
                log.close()

    with open('userslog.txt') as ud:
        c = False
        for i in ud.readlines():
            if not len(i.split(",")) == 2:
                continue
            username, password = i.split(",")
            username = username.strip()
            password = password.replace("\n", '')
            user = user.strip()
            passwd = passwd.replace("\n", '')
            # print(passwd.encode(), password.encode() ,  passwd == password)
            if(user == username and passwd == password):
                print(f'Hello {user}, you are logged in and fully authenticated')

                logging.info(f"Login successfull: User name : {user} | Password : {passwd}")

                c = True
                printAccessOrNot('Access')

            # else:
            #     # print('The username and password you used does not match our records')

            #     # printAccessOrNot('Denied')
    
    if not c:
        logging.info(f"Login unsuccessfull: User name : {user} | Password : {passwd}")

        printAccessOrNot('Denied')


def NewCusAct():
    logging.basicConfig(filename='logs.txt', level=logging.INFO)
    
    with open("userslog.txt") as usedata:
        usedata = usedata.readlines()
    
    userdata_sep = []

    for u in usedata:
        u = u.split(",")
        userdata_sep.append(u)

    # print(userdata_sep)

    with open("userslog.txt", 'w') as ud:

        print()
        # print(f'ENTER TEXT HERE {counter}: ')
        print(f'ENTER TEXT HERE : ')
        nusername = input('Enter your user name >> ')
        # userdata['UserName'] = nusername
        npassword = input('Enter your password >> ')
        # userdata['Password'] = npassword
        Email = input('Enter your Email >> ')
        # userdata['Email'] = Email

        userdata_sep.append([nusername, npassword])
        # print(userdata_sep)



        for u in userdata_sep:
            if len(u) == 2: 
                print(f'{u[0]},{u[1]}', file=ud)       

        logging.info(f"New User Added : User name : {u[0]} | Password : {u[1]}")

        print()

LoginPage()