n = int(input())
position = [list(map(int, input().split())) for _ in range(n)]
board = [[0]*100 for _ in range(100)]
cnt = 0

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def check(x,y):
    global cnt
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if nx<0 or ny<0 or nx>=100 or ny>=100:
            cnt += 1
        elif board[nx][ny] == 0:
            cnt += 1

for pos in position:
    y, x = pos
    y = 100 - (y+10)

    for i in range(x, x+10):
        for j in range(y, y+10):
            board[i][j] = 1

for i in range(100):
    for j in range(100):
        if board[i][j] == 1:
            check(i,j)

print(cnt)