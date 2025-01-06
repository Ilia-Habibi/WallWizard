




































































































































































































































































































































































































































































































































































































































































































































































































































































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
print(f"[bold red]{ascii_art}[/bold red]")
print(f"[bold yellow]Hi players! \nWelcome to QUORIDOR! \nA WallWizard Project[bold yellow]")



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
        "Email": email,
        "win" : 0
    }
    with open("Players.json", 'w') as file:
        json.dump(data,file,indent=4)
    if str(id) not in players:
        players.append(str(id))

    print('[bold green]signup is complete.[/bold green]')



################################################################################


menu_history =[]



# MENU OPTIONS FUNCTIONS

 #   def check_json(file_path):
  #      if not os.path.exists(file_path):
#         print(f"File '{file_path}' does not exist.")
#            return True
#        return os.path.getsize(file_path) == 0
#    file_path = "Players.json"



    # option showcase format
def formatted_print(input1, input2):
    print(f"{input1} ==> {input2}")

def menu_split():
    print("[bold purple]-[/bold purple]"* 60)


def navigate(menu):
    menu_history.append(menu)
    menu()

def back():
    if menu_history:
        menu_history.pop()
        if menu_history:
            menu_history[-1]()
        else:
            initial_menu()
            

    # quit game
def quit():
    print("\n[bold cyan]Thank you for playing Quoridor![/bold cyan]")
    menu_split()
    exit()


players = []
#def player_indicate():


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
        if bcrypt.checkpw(password.encode('utf-8'), information[i]["password"].encode('utf-8')):
            print("[bold green]You are logged in to your account[/bold green]")
            if i not in players:
                players.append(i)
            return
    print("[bold red]Password is incorrect.[/bold red]")
    return passwordLogin()

def register():
    print()
    menu_split()
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
    print()
    menu_split()

def initial_menu():
    menu_split()
    print("[hot_pink]MAIN MENU:[/hot_pink]\n")
#    if not check_json("Players.json"):
    formatted_print("L", "Login")
    formatted_print("R", "Register")
    formatted_print("P", "Leaderboard")
    formatted_print("E", "Exit")
    ss = input("Enter your choice: ")
    if ss == "E":
        quit()
    elif ss == "R":
        register()
        navigate(start_menu)
    elif ss == "L":
        menu_split()
        usernameLogin()
        passwordLogin()
        navigate(start_menu)
    elif ss == "P":
        leaderboard()
    else:
        print("[bold red]Invalid Choice[/bold red]")
        return initial_menu()


def second_player():
    print()
    menu_split()
    print("[hot_pink]REGISTER OR LOGIN SECOND PLAYER:[/hot_pink]\n")
    formatted_print("L", "Login")
    formatted_print("R", "Register")
    formatted_print("B", "Back")
    formatted_print("E", "Exit")
    jj = input("Enter your choice: ")
    if jj == "R":
        print()
        menu_split()
        register()
        navigate(name_select)
    elif jj == "L":
        print()
        menu_split()
        usernameLogin()
        passwordLogin()
        navigate(name_select)
    elif jj == "B":
        print()
        menu_split()
        back()
    elif jj == "E":
        quit()
    else:
        print("[bold red]Invalid Choice[/bold red]")
        return second_player()


def start_menu():
    print()
    menu_split()
    formatted_print("N", "New Game")
    formatted_print("B", "Back")
    formatted_print("E", "Exit")
    ff = input("Enter your choice: ")
    if ff == "N":
        navigate(second_player)
    elif ff == "B":
        print("\n")
        menu_split()
        back()
    elif ff == "E":
        quit()
    else:
        print("[bold red]Invalid Choice[/bold red]")
        return start_menu()
    


def name_select():
    print()
    menu_split()
    global p1
    global p2
    p1 = input("Enter First Player's Name: ")
    p1 = players[0]
    input("Enter Second Player's Name: ")


        



#  def print_table():

# def move_piece():

def main_game():
    print()
    menu_split()
    make_starter()
    do_game()




########################################################################################



initial_menu()
#main_game()

####################################################################################
#login









































































































































































































































































































































































































































































































































































































































































































































































































def LeaderBoard():
    point = {}
    with open("Players.json", 'r') as file:
        information = json.load(file)
    for id in information:
        point[information[id]["user"]] = information[id]["win"]
    point = dict(sorted(point.items(),key=lambda item: item[1],reverse=True))
    print(point)