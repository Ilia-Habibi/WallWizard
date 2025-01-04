import os
import time
############################# ساختن وسایل اولیه
n = 9
m = 10
table_piece = []
table_wall_x = []
table_wall_y = []
table_wall_points = []
def make_starter():
    global table_wall_points
    global table_wall_x
    global table_wall_y
    table_piece = [[0 for _ in range(n)] for _ in range(n)]
    table_piece[0][4] = 1
    table_piece[8][4] = 2
    table_wall_x = [[0 for _ in range(n)] for _ in range(n-1)]
    table_wall_y = [[0 for _ in range(n-1)] for _ in range(n)]
    table_wall_points = [[0 for _ in range(n-1)] for _ in range(n-1)]
    return
############################## تابع چک کردن تعداد دیوار های بازیکن x
def check_number_wall(x, table_wall):
    ans = 0
    for i in range(n-1):
        for j in range(n-1):
            if(table_wall[i][j] == x):
                ans += 1
    return ans
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
            cnt = m - check_number_wall(1, table_wall_x) - check_number_wall(1, table_wall_y)
            print(f"  >> player 1 walls : {cnt}")
        elif(i == 1):
            cnt = m - check_number_wall(2, table_wall_x) - check_number_wall(2, table_wall_y)
            print(f"  >> player 2 walls : {cnt}")
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
            return 1
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
for i in range(0, n):
    for j in range(0, n):
        print(table_piece[i][j], end = " ")
    print()
print()
do_game()