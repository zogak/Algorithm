import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())
graph = list(list(map(int, input().split())) for _ in range(r))
machine = []
for i in range(r):
    temp = graph[i]
    for j, item in enumerate(temp):
        if item == -1:
            machine.append((i,j))

def solve(input_board):
    board = [[0]*c for _ in range(r)]
    for m in machine:
        board[m[0]][m[1]] = -1

    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    # 먼지 퍼지기
    for i in range(r):
        for j in range(c):
            if input_board[i][j] == 0 or input_board[i][j] == -1:
                continue
            
            if input_board[i][j] < 5:
                board[i][j] += input_board[i][j]
                continue

            spread = []
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]

                if ni<0 or nj<0 or ni>=r or nj>=c:
                    continue
                
                if input_board[ni][nj] == -1:
                    continue

                spread.append((ni,nj))
            
            amount = input_board[i][j] // 5
            
            for item in spread:
                board[item[0]][item[1]] += amount
            
            board[i][j] += (input_board[i][j] - (amount*len(spread)))

    
    
    # 공기청정기
    m1_x, m1_y = machine[0]
    for i in range(m1_x-1, -1, -1):
        if i==0:
            board[i][0] = board[i][1]
        else:
            board[i][0] = board[i-1][0]
    
    for i in range(1, c):
        if i == c-1:
            board[0][i] = board[1][i]
        else:
            board[0][i] = board[0][i+1]
    
    for i in range(1, m1_x+1):
        if i == m1_x:
            board[i][c-1] = board[i][c-2]
        else:
            board[i][c-1] = board[i+1][c-1]

    for i in range(c-1, 1, -1):
        board[m1_x][i] = board[m1_x][i-1]
    board[m1_x][1] = 0


    m2_x, m2_y = machine[1]
    for i in range(m2_x+1, r):
        if i == r-1:
            board[i][0] = board[i][1]
        else:
            board[i][0] = board[i+1][0]
        
    for i in range(1, c):
        if i == c-1:
            board[r-1][i] = board[r-2][i]
        else:
            board[r-1][i] = board[r-1][i+1]

    for i in range(r-2, m2_x-1, -1):
        if i == m2_x:
            board[i][c-1] = board[i][c-2]
        else:
            board[i][c-1] = board[i-1][c-1]

    for i in range(c-2, 1, -1):
        board[m2_x][i] = board[m2_x][i-1]
    board[m2_x][1] = 0

    return board

res = 0
board=0
for i in range(t):
    if i==0:
        board = solve(graph)
        
    else:
        board = solve(board)

for i in range(r):
    for j in range(c):
        if board[i][j] == -1 or board[i][j] == 0:
            continue
        res += board[i][j]

print(res)

'''
[[0, 0, 0, 0, 0, 0, 1, 8], 
[0, 0, 1, 0, 3, 0, 5, 6], 
[-1, 2, 1, 1, 0, 4, 6, 5], 
[-1, 5, 2, 0, 0, 2, 12, 0], 
[0, 1, 1, 0, 5, 10, 13, 8], 
[0, 1, 9, 4, 3, 5, 12, 0], 
[0, 8, 17, 8, 3, 4, 8, 4]]

[[0, 0, 0, 0, 0, 1, 8, 6], 
[0, 0, 1, 0, 3, 0, 5, 5], 
[-1, 0, 2, 1, 1, 0, 4, 6], 
[-1, 0, 5, 2, 0, 0, 2, 12], 
[0, 1, 1, 0, 5, 10, 13, 0], 
[0, 1, 9, 4, 3, 5, 12, 8], 
[8, 17, 8, 3, 4, 8, 4, 4]]

'''