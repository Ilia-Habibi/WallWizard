




































































































































































































































































































































































































































































































































































































































































































































































































































































import json
import re
import uuid
import pyfiglet
import os
from rich import print
from rich.console import Console
import bcrypt



ascii_art = pyfiglet.figlet_format("QUORIDOR", font="epic")
console = Console()
print(f"[bold yellow]{ascii_art}[/bold yellow]")
print(f"[bold violet]Hi players! \nWelcome to Quoridor! \n[bold violet]")



# signup FUNCTIONS

def repetitiveUsername(username):
    with open('Players.json', 'r') as file:
        inforamtion = json.load(file)
    for i in inforamtion:
        if inforamtion[i]["user"] == username:
            print("[bold red]username already exists.[/bold red]")
            username = input("Enter a unique username: ")
            return repetitiveUsername(username)
    return username

def checkEmail(Email):
    pattern = re.compile(r'[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}')
    matches = list(pattern.finditer(Email))

    if not matches:
        print("[bold red]Email address invalid.[/bold red]")
        Email = input("Enter the email again: ")
        return checkEmail(Email)
    return Email

def repetitiveEmail(Email):
    with open('Players.json', 'r') as file:
        inforamtion = json.load(file)
    for i in inforamtion:
        if inforamtion[i]["Email"] == Email:
            print("[bold red]Email already exists.[/bold red]")
            Email = input("Enter a unique Email: ")
            return repetitiveEmail(Email)
    return Email
    

def checkPassword(Password):
    if len(Password)<=8:
        print("[bold red]Please make the password more than 8 characters[/bold red]")
        Password = input("Enter the password again: ")
        checkPassword(Password)
    return Password

def hashedPassword(password):
    hash = password.encode('utf-8')
    hashed = bcrypt.hashpw(hash, bcrypt.gensalt())
    hashedSaved = hashed.decode('utf-8')
    return hashedSaved

def registerInformation(id,username,password,email):
    with open("Players.json", 'r') as file:
        data = json.load(file)
    
    data[str(id)] = {
        "user": username,
        "password": password,
        "Email": email
    }
    with open("Players.json", 'w') as file:
        json.dump(data,file,indent=4)

    print('[bold green]signup is complete.[/bold green]')



################################################################################

# MENU OPTIONS FUNCTIONS

def check_json(file_path): #موقت
    return os.path.getsize(file_path) == 0


    # option showcase format
def formatted_print(input1, input2):

    print(f"{input1} ==> {input2}")

    # quit game
def quit():
    print("\n[bold cyan]Thank you for playing Quoridor![/bold cyan]")
    print("-" * 60)
    exit()

def login():
    print("[bold green]Login selected[/bold green]") #موقت

def register():
    username = input('Enter username: ')
    confirmedUsername = repetitiveUsername(username)
    idUser = uuid.uuid4()
    password = input('Enter password: ')
    confirmedPassword = checkPassword(password)
    hashPassword = hashedPassword(confirmedPassword)
    email = input('Enter Email: ')
    confirmedEmail = checkEmail(email)
    confirmedEmail = repetitiveEmail(confirmedEmail)
    registerInformation(idUser,confirmedUsername,hashPassword,confirmedEmail)

def leaderboard():
    exit() #موقت

def start_menu():
    if check_json("Players.json"):
        formatted_print("L", "Login")
    formatted_print("R", "Register")
    formatted_print("B", "Leaderboard")
    formatted_print("E", "Exit")
    print("\n")
    ss = input("Enter your choice: ")
    if ss == "E":
        quit()
    elif ss == "R":
        print("\n")
        print("-" * 60)
        register()#موقت
    elif ss == "L":
        login()
    elif ss == "B":
        leaderboard()


def main_game():



########################################################################################



start_menu()
main_game()

####################################################################################
#login
def usernameLogin():
    username = input("Username: ")
    with open("Players.json", 'r')as file:
        inforamtion = json.load(file)
    for i in inforamtion:
        if inforamtion[i]["user"] == username:
            print("[bold green]username is correct.[/bold green]")
            return
    print("[bold red]username is incorrect.[/bold red]")
    return usernameLogin()

def passwordLogin():
    password = input("Password: ")
    with open("Players.json", 'r') as file:
        information = json.load(file)
    for i in information:
        if information[i]["password"] == password:
            print("[bold green]You are logged in to your account[/bold green]")
            return
    print("[bold red]Password is incorrect.[/bold red]")
    return passwordLogin()