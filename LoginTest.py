import csv
from os import system

#way #1 
def main():
    with open("userslog.txt","r") as file:
        file_reader = csv.reader(file)
        user_find(file_reader)
        file.close()
 
def user_find(file):
    user = input("Enter your username: ")
    for row in file:
        if row[0] == user:
            print("username found", user)
            user_found = [row[0],row[1]]
            pass_check(user_found)
            break
        else:
            print("not found")
 
def pass_check(user_found):
    user = input("enter your password: ")
    if user_found[1] == user:
        print("password match")
    else:
        print("password not match")
        user_find(file_reader)
 
main()


########################
#way #2

class User:

    def identity(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.loggedIn = True


def home(user):
    print("Login, Register")
    a = input("What would you like to do: ")
    if(a == "register" or a == "Register"):
        register()
    elif(a == "Login" or a == "login"):
        login(user)
    else:
        print("Choose a valid option")
        home('')

def register():
    n = input("Name: ")
    u = input("Username: ")
    p = input("Password: ")
    u = User(n, u, p)
    print("Welcome, " + u.name)
    home(u)


def login(user):
    l = input("Username: ")
    l2 = input("Password")
    if(l2 == user.password):
        print("Welcome, " + user.name)
    else:
        print("Incorrect username or password")
        login(user)
    home('')

home('')