n = 9
table_piece = []
table_wall_x = []
table_wall_y = []
for i in range(n):
    x = []
    for j in range(n):
        x.append(0)
    table_piece.append(x)
table_piece[0][4] = 1
table_piece[8][4] = 2

for i in range(n-1):
    x = []
    for j in range(n-1):
        x.append(0)
    table_wall_x.append(x)
    table_wall_y.append(x)

def check_number_wall(x, table_wall):
    ans = 0
    for i in range(n-1):
        for j in range(n-1):
            if(table_wall[i][j] == x):
                ans += 1
    return ans

def do_something(x):
    print("1-> move \n2-> place wall \nchoose : ")
    s = input()
    if(s == '1'): print(0)
    else: print(1)



























































































































































    




























    




























    




























    




























    




























    




























    




























    




























    




























    




























    




























    




























    




























    




























    




























    




























    




























    




























    




























    




























    




























    




























    




























    




























    




























    




























    




























    




























print('Hi player! \nWelcome to Quoridor!')

import json
import re
import uuid
from rich import print

def checkEmail(Email):
    pattern = re.compile(r'[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}')

    matches = list(pattern.finditer(Email))

    if not matches:
        print('Email address invalid.')
        Email = input("Enter the email again: ")
        checkEmail(Email)

def checkPassword(Password):
    if len(Password)<=8:
        print("Please make the password more than 8 characters")
        Password = input("Enter the password again")
        checkPassword(Password)


username = input('Enter username: ')
password = input('Enter password: ')
email = input('Enter Email: ')

checkEmail(email)
checkPassword(password)
def registerInformation(username,password,email):
    user_data = {
        'user': username,
        'password': password,
        'Email': email
    }

    with open("Players.json", "w") as outfile:
        json.dump(user_data, outfile, indent=4)

    print("[bold yellow]Data has been saved to Players.json.[/bold yellow]")