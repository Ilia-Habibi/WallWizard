############################# ساختن وسایل اولیه
n = 9
table_piece = []
table_wall_x = []
table_wall_y = []
def make_starter():
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
############################## تابع ساختن گراف جدول
def make_gragh():
    adj = []
    for i in range(n):
        for j in range(n):
            adj.append([])
    
    for i in range(1, n-1):
        for j in range(1, n-1):
            x = []
            if(table_wall_x[i-1][j] == 0):
                x.append((i-1)*n + j)
            if(table_wall_x[i][j] == 0):
                x.append((i+1)*n + j)
            if(table_wall_y[i][j-1] == 0):
                x.append(i*n + (j-1))
            if(table_wall_y[i][j] == 0):
                x.append(i*n + (j+1))
            adj[i*n + j].append(x)
    for j in range(1, n-1):
        x = []
        if(table_wall_x[0][j] == 0):
            x.append(n + j)
        if(table_wall_y[0][j-1] == 0):
            x.append(j-1)
        if(table_wall_y[0][j] == 0):
            x.append(j+1)
        adj[j].append(x)
    for j in range(1, n-1):
            x = []
            if(table_wall_x[n-2][j] == 0):
                x.append((n-2)*n + j)
            if(table_wall_y[n-1][j-1] == 0):
                x.append((n-1)*n + (j-1))
            if(table_wall_y[n-1][j] == 0):
                x.append((n-1)*n + (j+1))
            adj[(n-1)*n + j].append(x)
    for i in range(1, n-1):
            x = []
            if(table_wall_x[i-1][0] == 0):
                x.append((i-1)*n)
            if(table_wall_x[i][0] == 0):
                x.append((i+1)*n)
            if(table_wall_y[i][0] == 0):
                x.append(i*n + (1))
            adj[i*n].append(x)
    for i in range(1, n-1):
            x = []
            if(table_wall_x[i-1][n-1] == 0):
                x.append((i-1)*n + n-1)
            if(table_wall_x[i][n-1] == 0):
                x.append((i+1)*n + n-1)
            if(table_wall_y[i][n-2] == 0):
                x.append(i*n + (n-2))
            adj[i*n + n-1].append(x)
    fake_1 = []
    if(table_wall_x[0][0] == 0): fake_1.append(n)
    if(table_wall_y[0][0] == 0): fake_1.append(1)
    adj[0].append(fake_1)
    fake_2 = []
    if(table_wall_x[0][n-1] == 0): fake_2.append(2*n - 1)
    if(table_wall_y[0][n-2] == 0): fake_2.append(n-2)
    adj[n-1].append(fake_2)
    fake_3 = []
    if(table_wall_x[n-2][0] == 0): fake_3.append((n-2)*n)
    if(table_wall_y[n-1][0] == 0): fake_3.append((n-1)*n + 1)
    adj[(n-1)*n].append(fake_3)
    fake_4 = []
    if(table_wall_x[n-2][n-1] == 0): fake_4.append((n-2)*n + n-1)
    if(table_wall_y[n-1][n-2] == 0): fake_4.append((n-1)*n + n-2)
    adj[(n-1)*n + n-1].append(fake_4)
  
    return adj
############################## تابع چک کردن وجود مسیر بعد از گذاشتن دیوار (a, b) در راستای x
def check_pull_wall(a, b, x):
    # در راستی ایکس میشه صفر و در راستای وای میشه 1
    if(x == 0):
        table_wall_x[a][b] = 1
    else:
        table_wall_y[a][b] = 1

    place = find_piece(1)
    gragh = make_gragh()
    print(gragh)
    return      

make_starter()
for i in range(0, n):
    for j in range(0, n):
        print(table_piece[i][j], end = " ")
    print()

#check_pull_wall(0, 0, 0)
a =make_gragh()
for i in a:
    print(i)