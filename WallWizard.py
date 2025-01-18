import json
import re
import uuid
import pyfiglet
import os
from rich import print
from rich.console import Console
import bcrypt
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
        print(" ", end="")
        for j in range(n):
            if table_piece[i][j]==1:
                print("[bold light_green]1[/bold light_green]", end=" ")
            elif table_piece[i][j]==2:
                print("[bold red]2[/bold red]", end=" ")
            else:
                print(table_piece[i][j], end = " ")
            if j<8:
                print("[bold #FFA500]|[/bold #FFA500]" if table_wall_y[i][j]==1 else "|", end=" ")
        if(i == 0): 
            print(f"  [bold yellow]>>[/bold yellow] [bold light_green]{p1} walls : {walls_for_1}[/bold light_green]")
        elif(i == 1):
            print(f"  [bold yellow]>>[/bold yellow] [bold red]{p2} walls : {walls_for_2}[/bold red]")
        else:
            print()
        if i<8:
            for j in range(n):
                print("[bold #FFA500]---[/bold #FFA500]" if table_wall_x[i][j]==1 else "---", end="")
                if j<8:
                    print("[bold #FFA500]+[/bold #FFA500]" if table_wall_points[i][j]==1 else "+", end="")
        print()
    return
############################## تابع حرکت مهره x
def move_piece(x):
    while(True):
        os.system('cls')
        if x==1:
            print(f"[yellow]{p1}'s TURN[/yellow]\n")
        elif x==2:
            print(f"[yellow]{p2}'s TURN[/yellow]\n")
        print_table()
        print("\nEnter number to move piece:[#FFD580] \n0 1 2\n3 [white]P[/white] 5\n6 7 8[/#FFD580]")
        formatted_print("\nB", "Back\n")
        s = input("Enter your choice: ")
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
                time.sleep(2)
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
                time.sleep(2)
        elif(s == '2'):
            if(check[2] == True):
                table_piece[a][b] = 0
                table_piece[a-1][b+1] = x
                return 1
            else:
                print("You cannot move in this direction :)")
                time.sleep(2)
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
                time.sleep(2)
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
                time.sleep(2)
        elif(s == '6'):
            if(check[6] == True):
                table_piece[a][b] = 0
                table_piece[a+1][b-1] = x
                return 1
            else:
                print("You cannot move in this direction :)")
                time.sleep(2)
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
                time.sleep(2)
        elif(s == '8'):
            if(check[8] == True):
                table_piece[a][b] = 0
                table_piece[a+1][b+1] = x
                return 1
            else:
                print("You cannot move in this direction :)")
                time.sleep(2)
        elif(s == 'B'):
            return 0
        else:
            print("[bold red]Invalid Choice[/bold red]")
            time.sleep(1.5)
############################## تابع دیوارگذاری
def place_wall(x):
    while(True):
        os.system('cls')
        if x==1:
            print(f"[yellow]{p1}'s TURN[/yellow]\n")
        elif x==2:
            print(f"[yellow]{p2}'s TURN[/yellow]\n")
        print_table()
        print("\nChoose Axis: X or Y")
        formatted_print("B", "Back\n")
        s = input("Enter your choice: ")
        place = find_piece(x)
        a = place[0]
        b = place[1]
        if(s == 'B'):
            return 0
        elif(s == 'X'):
            while(True):
                os.system('cls')
                if x==1:
                    print(f"[yellow]{p1}'s TURN[/yellow]\n")
                elif x==2:
                    print(f"[yellow]{p2}'s TURN[/yellow]\n")
                print_table()
                print("Choose The Line: 1 to 8 (Up to Down)")
                formatted_print("B", "Back\n")
                l = input("Enter your choice: ")
                if l == 'B':
                    return 0
                elif l=='1' or l=='2' or l=='3' or l=='4' or l=='5' or l=='6' or l=='7' or l=='8':
                    l=int(l)-1
                    while(True):
                        os.system('cls')
                        if x==1:
                            print(f"[yellow]{p1}'s TURN[/yellow]\n")
                        elif x==2:
                            print(f"[yellow]{p2}'s TURN[/yellow]\n")
                        print_table()
                        print("\nChoose The Start Of The Wall: 1 to 8 (Left to Right)")
                        formatted_print("B", "Back\n")
                        w = input("Enter your choice: ")
                        if w=='B':
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
                            print("[bold red]Invalid Choice[/bold red]")
                            time.sleep(3)
                else:
                    print("[bold red]Invalid Choice[/bold red]")
                    time.sleep(3)
        elif(s == 'Y'):
            while(True):
                os.system('cls')
                if x==1:
                    print(f"[yellow]{p1}'s TURN[/yellow]\n")
                elif x==2:
                    print(f"[yellow]{p2}'s TURN[/yellow]\n")
                print_table()
                print("Choose The Column: 1 to 8 (Left to Right)")
                formatted_print("B", "Back\n")
                l = input("Enter your choice: ")
                if l == 'B':
                    return 0
                elif l=='1' or l=='2' or l=='3' or l=='4' or l=='5' or l=='6' or l=='7' or l=='8':
                    l=int(l)-1
                    while(True):
                        os.system('cls')
                        if x==1:
                            print(f"[yellow]{p1}'s TURN[/yellow]\n")
                        elif x==2:
                            print(f"[yellow]{p2}'s TURN[/yellow]\n")
                        print_table()
                        print("choose the start of the wall: 1 to 8 (up to down)")
                        formatted_print("B", "Back\n")
                        w = input("Enter your choice: ")
                        if w=='B':
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
                            print("[bold red]Invalid Choice[/bold red]")
                            time.sleep(3)
                else:
                    print("[bold red]Invalid Choice[/bold red]")
                    time.sleep(3)
        else:
            print("[bold red]Invalid Choice[/bold red]")
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
        if x==1:
            print(f"[yellow]{p1}'s TURN[/yellow]\n")
        elif x==2:
            print(f"[yellow]{p2}'s TURN[/yellow]\n")
        print_table()
        formatted_print("\nM", "Move Piece")
        formatted_print("P", "Place Wall")
        formatted_print("B", "Back")
        formatted_print("E", "Exit\n")
        s = input("Enter your choice: ")
        if(s == 'M'): 
            bool = move_piece(x)
            if(bool == 1): return 1
        elif(s == 'P'):
            if x==1:
                if walls_for_1>0:
                    if (place_wall(x)==1): 
                        walls_for_1-=1
                        return 1
                else:
                    print("[bold red]You don't have any walls left![/bold red]")
                    time.sleep(2)
                    continue
            else:
                if walls_for_2>0:
                    if (place_wall(x)==1): 
                        walls_for_2-=1
                        return 1 
                else:
                    print("[bold red]You don't have any walls left![/bold red]")
                    time.sleep(2)
                    continue
        elif(s == 'B'):
            return 0
        elif(s == 'E'):
            quit()
        else:
            print("[bold red]Invalid Choice[/bold red]")
            time.sleep(2)
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
############################## تابع خروجی برنده و آپشن ادامه و خروج
def print_end_game(x):
    with open("Players.json", 'r') as file:
        information = json.load(file)
    while(True):
        os.system('cls')
        if x == 1:
            print(f"[bold #FFA500]{p1}[/bold #FFA500] WIIIINS :)\n")
            for i in information:
                if p1 == information[i]["user"]:
                    information[i]["win"]+=1
                    with open("Players.json", 'w') as file:
                        json.dump(information,file,indent=4)
                    historyOfGame(p1 + ": winner", p2)
        elif x == 2:
            print(f"[bold #FFA500]{p2}[/bold #FFA500] WIIIINS :)\n")
            for i in information:
                if p2 == information[i]["user"]:
                    information[i]["win"]+=1
                    with open("Players.json", 'w') as file:
                        json.dump(information,file,indent=4)
                    historyOfGame(p1, p2 + ": winner")
        formatted_print("R", "Rematch")
        formatted_print("E", "Exit\n")
        s = input("Enter your choice: ")
        if(s == 'R'): return 1
        elif(s == 'E'): quit()
        else:
            print("[bold red]Invalid Choice[/bold red]") 
            time.sleep(2)
############################## تابع انجام بازی نوبتی
def do_game():
    while(True):
        os.system('cls')
        make_starter()
        print("[hot_pink]Who starts first?[/hot_pink]")
        print()
        formatted_print("1", f"[yellow]{p1}[/yellow]")
        formatted_print("2", f"[yellow]{p2}[/yellow]")
        formatted_print("B", "Back")
        formatted_print("E", "Exit\n")
        s = input("Enter your choice: ")
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
        elif(s == 'B'):
            players.pop(1)
            back()
        elif s == 'E':
            quit()
        else:
            print("[bold red]Invalid Choice[/bold red]")
            time.sleep(1.5)



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


# MENU OPTIONS FUNCTIONS

def formatted_print(input1, input2):
    print(f"{input1} ==> {input2}")

def menu_split():
    print("[bold purple]-[/bold purple]"* 60)


menu_history =[]

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
            time.sleep(2)
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
        time.sleep(2)
    else:
        return register()

def LeaderBoard():
    os.system('cls')
    print("[hot_pink]WallWizard League Ranking:[/hot_pink]\n")
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
                print(f'[bold bright_yellow]({i+1}) {point[i][j]} : {point[i][j+1]}[/bold bright_yellow]')
            elif i == 1:
                print(f'[bold #C0C0C0]({i+1}) {point[i][j]} : {point[i][j+1]}[/bold #C0C0C0]')
            elif i == 2:
                print(f'[bold #CD7F32]({i+1}) {point[i][j]} : {point[i][j+1]}[/bold #CD7F32]')
            else:
                print(f' [bright_white]{i+1}. {point[i][j]} : {point[i][j+1]}[/bright_white]')
    print()
    menu_split()
    formatted_print("B", "Back")
    formatted_print("E", "Exit\n")
    jj = input("Enter your choice: ")
    if jj == "B":
        back()
    elif jj == "E":
        quit()


def historyOfGame(player1, player2):
    playerInGame = [player1,player2]
    with open("history.json", 'r') as file:
        information = json.load(file)
    information.append(playerInGame)
    with open("history.json", 'w') as file:
        json.dump(information,file,indent=4)

def printHistoryGame():
    os.system('cls')
    print("[hot_pink]HISTORY OF GAMES:[/hot_pink]\n")
    with open("history.json", 'r') as file:
        information = json.load(file)
    for i in range(len(information)):
        print(f"[#00FFFF]Game {i+1}[/#00FFFF] [bold]>>>   [/bold]" + f"[bold yellow]{information[i][0]}[/bold yellow] vs [bold yellow]{information[i][1]}[/bold yellow]")
    print()
    menu_split()
    formatted_print("B", "Back")
    formatted_print("E", "Exit\n")
    jj = input("Enter your choice: ")
    if jj == "B":
        back()
    elif jj == "E":
        quit()
    else:
        print("[bold red]Invalid Choice[/bold red]")
        time.sleep(1.5)
        return printHistoryGame()


def initial_menu():
    os.system('cls')
    ascii_art = pyfiglet.figlet_format("QUORIDOR", font="epic")
    print(f"[bold #00FFFF]{ascii_art}[/bold #00FFFF]")
    print(f"[bold yellow]Hi players! \nWelcome to QUORIDOR! \nA WallWizard Project[bold yellow]")
    menu_split()
    print("[hot_pink]MAIN MENU:[/hot_pink]\n")
    formatted_print("L", "Login")
    formatted_print("R", "Register")
    formatted_print("P", "Leaderboard")
    formatted_print("H", "History")
    formatted_print("E", "Exit\n")
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
        navigate(LeaderBoard)
    elif ss == "H":
        navigate(printHistoryGame) 
    else:
        print("[bold red]Invalid Choice[/bold red]")
        time.sleep(1.5)
        return initial_menu()


def second_player():
    os.system('cls')
    print("[hot_pink]REGISTER OR LOGIN SECOND PLAYER:[/hot_pink]\n")
    formatted_print("L", "Login")
    formatted_print("R", "Register")
    formatted_print("B", "Back")
    formatted_print("E", "Exit\n")
    jj = input("Enter your choice: ")
    if jj == "R":
        register()
        name_select()
        navigate(do_game)
    elif jj == "L":
        print()
        menu_split()
        usernameLogin()
        passwordLogin()
        name_select()
        navigate(do_game)
    elif jj == "B":
        back()
    elif jj == "E":
        quit()
    else:
        print("[bold red]Invalid Choice[/bold red]")
        time.sleep(1)
        return second_player()


def start_menu():
    os.system('cls')
    formatted_print("\nN", "New Game")
    formatted_print("B", "Back")
    formatted_print("E", "Exit\n")
    ff = input("Enter your choice: ")
    if ff == "N":
        navigate(second_player)
    elif ff == "B":
        print("\n")
        menu_split()
        players.clear()
        back()
    elif ff == "E":
        quit()
    else:
        print("[bold red]Invalid Choice[/bold red]")
        time.sleep(1)
        return start_menu()
    


def name_select():
    global p1
    global p2
    os.system('cls')
    print("[hot_pink]ENTER IN-GAME NAMES:[/hot_pink]\n")
    with open("Players.json", 'r') as file:
        information = json.load(file)
    for i in information:
        if i == players[0]:
            p1 = information[i]["user"]
        elif i == players[1]:
            p2 = information[i]["user"]
    navigate(do_game)




########################################################################################



initial_menu()

























































