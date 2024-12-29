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