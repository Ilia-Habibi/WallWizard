
























































































































































































































































































































































































































































































































print('Hi player! \nWelcome to Quoridor!')

import json
import re
import uuid
from rich import print

def checkEmail(Email):
    pattern = re.compile(r'[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}')
    matches = list(pattern.finditer(Email))

    if not matches:
        print("[bold red]Email address invalid.[/bold red]")
        Email = input("Enter the email again: ")
        checkEmail(Email)
    return Email

def checkPassword(Password):
    if len(Password)<=8:
        print("[bold red]Please make the password more than 8 characters[/bold red]")
        Password = input("Enter the password again: ")
        checkPassword(Password)
    return Password

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


    print("[bold green]Data has been saved to Players.json.[/bold green]")

username = input('Enter username: ')
idUser = uuid.uuid4()
password = input('Enter password: ')
ConfirmedPassword = checkPassword(password)
email = input('Enter Email: ')
ConfirmedEmail = checkEmail(email)
registerInformation(idUser,username,ConfirmedPassword,ConfirmedEmail)