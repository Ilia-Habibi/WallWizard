############################# ساختن وسایل اولیه
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
    for j in range(n):
        x.append(0)
    table_wall_x.append(x)
for i in range(n):
    x = []
    for j in range(n-1):
        x.append(0)
    table_wall_y.append(x)
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
    available = [True, True, True, True, "Player", True, True, True, True]
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
    return available
############################## تابع حرکت مهره x
def move_piece(x):
    print("choose: \n0 1 2\n3 P 5\n6 7 8")
    s = input()
    place = find_piece(x)
    check = check_move(x)
    a = place[0]
    b = place[1]
    if(s == '0'):
        if(check[0] == True):
            table_piece[a][b] = 0
            table_piece[a-1][b-1] = x
        else:
            print("EROOR!!!")
    if(s == '1'):
        if(check[1] == True):
            table_piece[a][b] = 0
            table_piece[a-1][b] = x
        else:
            print("EROOR!!!")
    if(s == '2'):
        if(check[2] == True):
            table_piece[a][b] = 0
            table_piece[a-1][b+1] = x
        else:
            print("EROOR!!!")
    if(s == '3'):
        if(check[3] == True):
            table_piece[a][b] = 0
            table_piece[a][b-1] = x
        else:
            print("EROOR!!!")
    if(s == '5'):
        if(check[5] == True):
            table_piece[a][b] = 0
            table_piece[a][b+1] = x
        else:
            print("EROOR!!!")
    if(s == '6'):
        if(check[6] == True):
            table_piece[a][b] = 0
            table_piece[a+1][b-1] = x
        else:
            print("EROOR!!!")
    if(s == '7'):
        if(check[7] == True):
            table_piece[a][b] = 0
            table_piece[a+1][b] = x
        else:
            print("EROOR!!!")
    if(s == '8'):
        if(check[8] == True):
            table_piece[a][b] = 0
            table_piece[a+1][b+1] = x
        else:
            print("EROOR!!!")
##############################   
def do_something(x):
    print("1-> move \n2-> place wall \nchoose : ")
    s = input()
    if(s == '1'): print(0)
    else: print(1)

move_piece(1)
for i in range(n):
    for j in range(n):
        print(table_piece[i][j], end = " ")
    print()