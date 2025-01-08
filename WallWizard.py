
import os
import time
############################# ساختن وسایل اولیه
n = 9
table_piece = []
table_wall_x = []
table_wall_y = []
table_wall_points = []
walls_for_1 = 10
walls_for_2 = 10
def make_starter():
    global table_wall_points
    global table_wall_x
    global table_wall_y
    global walls_for_1
    global walls_for_2
    global table_piece
    table_piece = [[0 for _ in range(n)] for _ in range(n)]
    table_piece[0][4] = 1
    table_piece[8][4] = 2
    table_wall_x = [[0 for _ in range(n)] for _ in range(n-1)]
    table_wall_y = [[0 for _ in range(n-1)] for _ in range(n)]
    table_wall_points = [[0 for _ in range(n-1)] for _ in range(n-1)]
    walls_for_1 = 10
    walls_for_2 = 10
    return
############################## تابع پیدا کردن مهره x
def find_piece(x):
    for i in range(n):
        for j in range(n):
            if(table_piece[i][j] == x):
                return([i, j])
############################## تابع چک کردن حرکت مهره x
def check_move(x):
    available = [False, True, False, True, "Player", True, False, True, False]
    place = find_piece(x)
    a = place[0]
    b = place[1]
############### (333)
    if(b == 0):
        available[3] = False
    else:
        if(table_wall_y[a][b-1] == 1): available[3] = False
        if(table_piece[a][b-1] != 0):
            if(b-1 == 0):
                available[3] = False
            elif(table_wall_y[a][b-2] == 1): available[3] = False
############### (555)
    if(b == n-1):
        available[5] = False
    else:
        if(table_wall_y[a][b] == 1): available[5] = False
        if(table_piece[a][b+1] != 0):
            if(b+1 == n-1):
                available[5] = False
            elif(table_wall_y[a][b+1] == 1): available[5] = False
############### (111)    
    if(a == 0):
        available[1] = False
    else:
        if(table_wall_x[a-1][b] == 1): available[1] = False
        if(table_piece[a-1][b] != 0):
            if(a-1 == 0):
                available[1] = False
            elif(table_wall_x[a-2][b] == 1): available[1] = False
############### (777)
    if(a == n-1):
        available[7] = False
    else:
        if(table_wall_x[a][b] == 1): available[7] = False
        if(table_piece[a+1][b] != 0):
            if(a+1 == n-1):
                available[7] = False
            elif(table_wall_x[a+1][b] == 1): available[7] = False
############### (000)
    if(b!=0)and(a!=0):   
        if(table_piece[a][b-1] != 0) and (table_wall_y[a][b-1] == 0):
            if(b-1 == 0):
                if table_wall_x[a-1][b-1]==0:
                    available[0]=True
            elif(table_wall_y[a][b-2] == 1):
                if table_wall_x[a-1][b-1]==0:
                    available[0]=True
        elif(table_piece[a-1][b] != 0) and (table_wall_x[a-1][b] == 0):
            if(a-1 == 0):
                if table_wall_y[a-1][b-1]==0:
                    available[0]=True
            elif(table_wall_x[a-2][b] == 1):
                if table_wall_y[a-1][b-1]==0:
                    available[0]=True
############### (222)
    if(b!=n-1)and(a!=0):     
        if(table_piece[a][b+1] != 0) and (table_wall_y[a][b] == 0):
            if(b+1 == n-1):
                if table_wall_x[a-1][b+1]==0:
                    available[2]=True
            elif(table_wall_y[a][b+1] == 1):
                if table_wall_x[a-1][b+1]==0:
                    available[2]=True
        elif(table_piece[a-1][b] != 0) and (table_wall_x[a-1][b] == 0):
            if(a-1 == 0):
                if table_wall_y[a-1][b]==0:
                    available[2]=True
            elif(table_wall_x[a-2][b] == 1):
                if table_wall_y[a-1][b]==0:
                    available[2]=True
############### (666)
    if(b!=0)and(a!=n-1):     
        if(table_piece[a][b-1] != 0) and (table_wall_y[a][b-1] == 0):
            if(b-1 == 0):
                if table_wall_x[a][b-1]==0:
                    available[6]=True
            elif(table_wall_y[a][b-2] == 1):
                if table_wall_x[a][b-1]==0:
                    available[6]=True
        elif(table_piece[a+1][b] != 0) and (table_wall_x[a][b] == 0):
            if(a+1 == n-1):
                if table_wall_y[a+1][b-1]==0:
                    available[6]=True
            elif(table_wall_x[a+1][b] == 1):
                if table_wall_y[a+1][b-1]==0:
                    available[6]=True
############### (888)
    if(b!=n-1)and(a!=n-1):     
        if(table_piece[a][b+1] != 0) and (table_wall_y[a][b] == 0):
            if(b+1 == n-1):
                if table_wall_x[a][b+1]==0:
                    available[8]=True
            elif(table_wall_y[a][b+1] == 1):
                if table_wall_x[a][b+1]==0:
                    available[8]=True
        elif(table_piece[a+1][b] != 0) and (table_wall_x[a][b] == 0):
            if(a+1 == n-1):
                if table_wall_y[a+1][b]==0:
                    available[8]=True
            elif(table_wall_x[a+1][b] == 1):
                if table_wall_y[a+1][b]==0:
                    available[8]=True
    return available
############################## تابع نمایش جدول
def print_table():
    for i in range(n):
        for j in range(n):
            print(table_piece[i][j], end = " ")
        if(i == 0): 
            print(f"  >> player 1 walls : {walls_for_1}")
        elif(i == 1):
            print(f"  >> player 2 walls : {walls_for_2}")
        else:
            print()
    return
############################## تابع حرکت مهره x
def move_piece(x):
    while(True):
        os.system('cls')
        print(f"PLAYER {x}")
        print_table()
        print("choose: \n0 1 2\n3 P 5\n6 7 8")
        print("E -> EXIT")
        print("\nCHOOSE >>> ", end = "")
        s = input()
        place = find_piece(x)
        check = check_move(x)
        a = place[0]
        b = place[1]
        if(s == '0'):
            if(check[0] == True):
                table_piece[a][b] = 0
                table_piece[a-1][b-1] = x
                return 1
            else:
                print("You cannot move in this direction :)")
                time.sleep(3)
        elif(s == '1'):
            if(check[1] == True):
                if(table_piece[a-1][b] == 0):
                    table_piece[a][b] = 0
                    table_piece[a-1][b] = x
                else:
                    table_piece[a][b] = 0
                    table_piece[a-2][b] = x
                return 1
            else:
                print("You cannot move in this direction :)")
                time.sleep(3)
        elif(s == '2'):
            if(check[2] == True):
                table_piece[a][b] = 0
                table_piece[a-1][b+1] = x
                return 1
            else:
                print("You cannot move in this direction :)")
                time.sleep(3)
        elif(s == '3'):
            if(check[3] == True):
                if(table_piece[a][b-1] == 0):
                    table_piece[a][b] = 0
                    table_piece[a][b-1] = x
                else:
                    table_piece[a][b] = 0
                    table_piece[a][b-2] = x
                return 1
            else:
                print("You cannot move in this direction :)")
                time.sleep(3)
        elif(s == '5'):
            if(check[5] == True):
                if(table_piece[a][b+1] == 0):
                    table_piece[a][b] = 0
                    table_piece[a][b+1] = x
                else:
                    table_piece[a][b] = 0
                    table_piece[a][b+2] = x
                return 1
            else:
                print("You cannot move in this direction :)")
                time.sleep(3)
        elif(s == '6'):
            if(check[6] == True):
                table_piece[a][b] = 0
                table_piece[a+1][b-1] = x
                return 1
            else:
                print("You cannot move in this direction :)")
                time.sleep(3)
        elif(s == '7'):
            if(check[7] == True):
                if(table_piece[a+1][b] == 0):
                    table_piece[a][b] = 0
                    table_piece[a+1][b] = x
                else:
                    table_piece[a][b] = 0
                    table_piece[a+2][b] = x
                return 1
            else:
                print("You cannot move in this direction :)")
                time.sleep(3)
        elif(s == '8'):
            if(check[8] == True):
                table_piece[a][b] = 0
                table_piece[a+1][b+1] = x
                return 1
            else:
                print("You cannot move in this direction :)")
                time.sleep(3)
        elif(s == 'E'):
            return 0
        else:
            print("ERROR")
            time.sleep(3)
    return
############################## تابع دیوارگذاری
def place_wall(x):
    while(True):
        os.system('cls')
        print(f"PLAYER {x}")
        print_table()
        print("choose axis: x or y")
        print("E -> EXIT")
        print("\nCHOOSE >>> ", end = "")
        s = input()
        place = find_piece(x)
        a = place[0]
        b = place[1]
        if(s == 'E'):
            return 0
        elif(s == 'x'):
            while(True):
                os.system('cls')
                print(f"PLAYER {x}")
                print_table()
                print("choose the line: 1 to 8 (up to down)")
                print("E -> EXIT")
                print("\nCHOOSE >>> ", end = "")
                l = input()
                if l == 'E':
                    return 0
                elif l=='1' or l=='2' or l=='3' or l=='4' or l=='5' or l=='6' or l=='7' or l=='8':
                    l=int(l)-1
                    while(True):
                        os.system('cls')
                        print(f"PLAYER {x}")
                        print_table()
                        print("choose the start of the wall: 1 to 8 (left to right)")
                        print("E -> EXIT")
                        print("\nCHOOSE >>> ", end = "")
                        w = input()
                        if w=='E':
                            return 0
                        elif w=='1' or w=='2' or w=='3' or w=='4' or w=='5' or w=='6' or w=='7' or w=='8':
                            w=int(w)-1
                            if table_wall_x[l][w]==0 and table_wall_x[l][w+1]==0 and table_wall_points[l][w]==0:
                                table_wall_x[l][w]=1
                                if check_pull_wall(l,w+1,0):
                                    table_wall_x[l][w+1]=1
                                    table_wall_points[l][w]=1
                                    return 1
                                else:
                                    table_wall_x[l][w]=0
                                    print("You can't place a wall here :)")
                                    time.sleep(3)
                            else:
                                print("You can't place a wall here :)")
                                time.sleep(3)
                        else:
                            print("ERROR")
                            time.sleep(3)
                else:
                    print("ERROR")
                    time.sleep(3)
        elif(s == 'y'):
            while(True):
                os.system('cls')
                print(f"PLAYER {x}")
                print_table()
                print("choose the column: 1 to 8 (left to right)")
                print("E -> EXIT")
                print("\nCHOOSE >>> ", end = "")
                l = input()
                if l == 'E':
                    return 0
                elif l=='1' or l=='2' or l=='3' or l=='4' or l=='5' or l=='6' or l=='7' or l=='8':
                    l=int(l)-1
                    while(True):
                        os.system('cls')
                        print(f"PLAYER {x}")
                        print_table()
                        print("choose the start of the wall: 1 to 8 (up to down)")
                        print("E -> EXIT")
                        print("\nCHOOSE >>> ", end = "")
                        w = input()
                        if w=='E':
                            return 0
                        elif w=='1' or w=='2' or w=='3' or w=='4' or w=='5' or w=='6' or w=='7' or w=='8':
                            
                            w=int(w)-1
                            if table_wall_y[w][l]==0 and table_wall_y[w+1][l]==0 and table_wall_points[w][l]==0:
                                table_wall_y[w][l]=1
                                if check_pull_wall(w+1,l,1):
                                    table_wall_y[w+1][l]=1
                                    table_wall_points[w][l]=1
                                    return 1
                                else:
                                    table_wall_y[w][l]=0
                                    print("You can't place a wall here :)")
                                    time.sleep(3)
                            else:
                                print("You can't place a wall here :)")
                                time.sleep(3)
                        else:
                            print("ERROR")
                            time.sleep(3)
                else:
                    print("ERROR")
                    time.sleep(3)
        else:
            print("ERROR")
            time.sleep(3)
############################## تابع ساختن گراف جدول
def make_gragh():
    adj = []
    for i in range(n):
        for j in range(n):
            adj.append([])
    
    for i in range(1, n-1):
        for j in range(1, n-1):
            if(table_wall_x[i-1][j] == 0):
                adj[i*n + j].append((i-1)*n + j)
            if(table_wall_x[i][j] == 0):
                adj[i*n + j].append((i+1)*n + j)
            if(table_wall_y[i][j-1] == 0):
                adj[i*n + j].append(i*n + (j-1))
            if(table_wall_y[i][j] == 0):
                adj[i*n + j].append(i*n + (j+1))
    for j in range(1, n-1):
        if(table_wall_x[0][j] == 0):
            adj[j].append(n + j)
        if(table_wall_y[0][j-1] == 0):
            adj[j].append(j-1)
        if(table_wall_y[0][j] == 0):
            adj[j].append(j+1)
    for j in range(1, n-1):
            if(table_wall_x[n-2][j] == 0):
                adj[(n-1)*n + j].append((n-2)*n + j)
            if(table_wall_y[n-1][j-1] == 0):
                adj[(n-1)*n + j].append((n-1)*n + (j-1))
            if(table_wall_y[n-1][j] == 0):
                adj[(n-1)*n + j].append((n-1)*n + (j+1))
    for i in range(1, n-1):
            if(table_wall_x[i-1][0] == 0):
                adj[i*n].append((i-1)*n)
            if(table_wall_x[i][0] == 0):
                adj[i*n].append((i+1)*n)
            if(table_wall_y[i][0] == 0):
                adj[i*n].append(i*n + (1))
    for i in range(1, n-1):
            if(table_wall_x[i-1][n-1] == 0):
                adj[i*n + n-1].append((i-1)*n + n-1)
            if(table_wall_x[i][n-1] == 0):
                adj[i*n + n-1].append((i+1)*n + n-1)
            if(table_wall_y[i][n-2] == 0):
                adj[i*n + n-1].append(i*n + (n-2))
    if(table_wall_x[0][0] == 0): adj[0].append(n)
    if(table_wall_y[0][0] == 0): adj[0].append(1)
    if(table_wall_x[0][n-1] == 0): adj[n-1].append(2*n - 1)
    if(table_wall_y[0][n-2] == 0): adj[n-1].append(n-2)
    if(table_wall_x[n-2][0] == 0): adj[(n-1)*n].append((n-2)*n)
    if(table_wall_y[n-1][0] == 0): adj[(n-1)*n].append((n-1)*n + 1)
    if(table_wall_x[n-2][n-1] == 0): adj[(n-1)*n + n-1].append((n-2)*n + n-1)
    if(table_wall_y[n-1][n-2] == 0): adj[(n-1)*n + n-1].append((n-1)*n + n-2)  
    return adj
############################## تابع دی اف اس روی جدول
def dfs(root, seen, gragh):
    seen[root] = 1
    for i in gragh[root]:
        if(seen[i] == 0): dfs(i, seen, gragh)
    return
############################## تابع چک کردن وجود مسیر بعد از گذاشتن دیوار (a, b) در راستای x
def check_pull_wall(a, b, x):
    # در راستی ایکس میشه صفر و در راستای وای میشه 1
    if(x == 0):
        table_wall_x[a][b] = 1
    else:
        table_wall_y[a][b] = 1

    gragh = make_gragh()

    seen_1 = []
    place_1 = find_piece(1)
    for i in range(n*n): seen_1.append(0)
    dfs(place_1[0]*n + place_1[1], seen_1, gragh)
    bool_1 = False
    for i in range(n):
        if(seen_1[(n-1)*n + i] == 1): bool_1 = True

    seen_2 = []
    place_2 = find_piece(2)
    for i in range(n*n): seen_2.append(0)
    dfs(place_2[0]*n + place_2[1], seen_2, gragh)
    bool_2 = False
    for i in range(n):
        if(seen_2[i] == 1): bool_2 = True

    if(x == 0):
        table_wall_x[a][b] = 0
    else:
        table_wall_y[a][b] = 0
    if(bool_1 == True and bool_2 == True): return True
    else: return False    
############################## تابع نوبت بازیکن x
def player_turn(x):
    global walls_for_1
    global walls_for_2
    while(True):
        os.system('cls')
        print(f"PLAYER {x}")
        print_table()
        print("\nSelect the move:")
        print("1-> Move piece")
        print("2-> Put a wall")
        print("3-> Exit game")
        print("\nCHOOSE >>> ", end = "")
        s = input()
        if(s == '1'): 
            bool = move_piece(x)
            if(bool == 1): return 1
        elif(s == '2'):
            if x==1:
                if walls_for_1>0:
                    if (place_wall(x)==1): 
                        walls_for_1-=1
                        return 1
                else:
                    print("You don't have any walls left!")
                    time.sleep(3)
                    continue
            else:
                if walls_for_2>0:
                    if (place_wall(x)==1): 
                        walls_for_2-=1
                        return 1 
                else:
                    print("You don't have any walls left!")
                    time.sleep(3)
                    continue
        elif(s == '3'):
            return 0
        else:
            print("EROOR")
            time.sleep(3)
    return
############################## تابع چک کردن اتمام بازی و خروجی برنده
def check_end_game():
    bool_1 = False
    bool_2 = False
    for i in range(n):
        if(table_piece[n-1][i] == 1):
            bool_1 = True
    for i in range(n):
        if(table_piece[0][i] == 2):
            bool_2 = True
    if(bool_1 == True):
        return 1
    elif(bool_2 == True):
        return 2
    else:
        return 0
    return
############################## تابع خروجی برنده و آپشن ادامه و خروج
def print_end_game(x):
    while(True):
        os.system('cls')
        print(f"PLAYER {x} WIIIIN :)")
        print("1-> New Game")
        print("2-> Exit Game")
        print("\nCHOOSE >>> ", end = "")
        s = input()
        if(s == '1'): return 1
        elif(s == '2'): return 2
        else:
            print("ERROR") 
            time.sleep(3)
    return
############################## تابع انجام بازی نوبتی
def do_game():
    while(True):
        os.system('cls')
        make_starter()
        print("Who starts first?")
        print("1_PLAYER 1")
        print("2_PLAYER 2")
        print("3_EXIT")
        print("\nCHOOSE >>> ", end = "")
        s = input()
        if(s == '1'):
            x = 1
            while(True):
                cnt = check_end_game()
                if(cnt == 1 or cnt == 2):
                    check = print_end_game(cnt)
                    if(check == 1): break
                    else: return
                if(x%2 == 1):
                    cnt = player_turn(1) 
                    if(cnt == 0): break
                else: 
                    cnt = player_turn(2)
                    if(cnt == 0): break
                x += 1
        elif(s == '2'):
            x = 0
            while(True):
                cnt = check_end_game()
                if(cnt == 1 or cnt == 2):
                    check = print_end_game(cnt)
                    if(check == 1): break
                    else: return
                if(x%2 == 1): 
                    cnt = player_turn(1)
                    if(cnt == 0): break
                else: 
                    cnt = player_turn(2)
                    if(cnt == 0): break
                x += 1
        elif(s == '3'):
            return
        else:
            print("ERROR")
            time.sleep(3)
    return

make_starter()
for i in range(n):
    for j in range(n):
        print(table_piece[i][j], end = " ")
    print()
# print()
# do_game()
# =======








































































































































































































































































































































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
            if i not in players:
                players.append(i)
                print("[bold green]username is correct.[/bold green]")
                return
    print("[bold red]username is incorrect or You have already logged in with this username.[/bold red]")
    return usernameLogin()

def passwordLogin():
    password = input("Password: ")
    with open("Players.json", 'r') as file:
        information = json.load(file)
    for i in information:
        if bcrypt.checkpw(password.encode('utf-8'), information[i]["password"].encode('utf-8')):
            print("[bold green]You are logged in to your account[/bold green]")
            return
    print("[bold red]Password is incorrect.[/bold red]")
    return passwordLogin()

def register():
    print()
    menu_split()
    username = input('Enter username: ')
    if len(username)>0:
        confirmedUsername = repetitiveUsername(username)
        idUser = uuid.uuid4()
        password = input('Enter password: ')
        confirmedPassword = checkPassword(password)
        hashPassword = hashedPassword(confirmedPassword)
        email = input('Enter Email: ')
        confirmedEmail = checkEmail(email)
        confirmedEmail = repetitiveEmail(confirmedEmail)
        registerInformation(idUser,confirmedUsername,hashPassword,confirmedEmail)
    else:
        return register()

def LeaderBoard():
    print()
    menu_split()
    point = {}
    with open("Players.json", 'r') as file:
        information = json.load(file)
    for id in information:
        point[information[id]["user"]] = information[id]["win"]
    point = dict(sorted(point.items(),key=lambda item: item[1],reverse=True))
    point = list(point.items())
    for i in range(len(point)):
        for j in range(1):
            if i == 0:
                print(f'[bold bright_yellow]{i+1}. {point[i][j]} : {point[i][j+1]}[/bold bright_yellow]')
            else:
                print(f'[bold bright_white]{i+1}. {point[i][j]} : {point[i][j+1]}[/bold bright_white]')


def historyOfGame():
    playerInGame = []
    with open("Players.json", 'r') as file:
        information = json.load(file)
    for i in information:
        if i == players[0]:
            playerInGame.append(information[i]["user"])
    for i in information:
        if i == players[1]:
            playerInGame.append(information[i]["user"])
    for i in information:
        if i == players[0] or i == players[1]:
            information["History of games"].append(tuple(playerInGame))
            with open("Players.json", 'w') as file:
                json.dump(information,file,indent=4)

def printHistoryGame():
    with open("Players.json", 'r') as file:
        information = json.load(file)
    print(information["History of games"])


def initial_menu():
    menu_split()
    print("[hot_pink]MAIN MENU:[/hot_pink]\n")
#    if not check_json("Players.json"):
    formatted_print("L", "Login")
    formatted_print("R", "Register")
    formatted_print("P", "Leaderboard")
    formatted_print("H", "History")
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
        LeaderBoard()
    elif ss == "H":
        printHistoryGame() 
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
    p2 = input("Enter Second Player's Name: ")


        



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

























































