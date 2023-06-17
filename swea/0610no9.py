from collections import deque
T = int(input())
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]

def outOfBound(x, y):
    if x<0 or y<0 or x>=N or y>=N : return True
    return False

def bfs(startX, startY):
    global visited
    q = deque()
    visited[startX][startY] = 1
    q.append((startX, startY))

    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if outOfBound(nx,ny) : continue
            if visited[nx][ny] != 0 : continue

            visited[nx][ny] = 1
            if board[nx][ny] == 0:
                q.append((nx,ny))

for tc in range(1, T+1):
    N = int(input())
    board = [list(input()) for _ in range(N)]

    #1. 숫자로 바꾸기
    zeroPos = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == '*' : continue

            bomb = 0
            for k in range(8):
                ni = i + dx[k]
                nj = j + dy[k]

                if outOfBound(ni, nj) : continue
                if board[ni][nj] == '*' : bomb += 1
            
            board[i][j] = bomb
            if bomb == 0:
                zeroPos.append((i,j))

    #2. 0 위치들로 bfs => 0으로 한 번에 터뜨릴 수 있는 곳 터뜨리고 개수 세기
    res = 0
    visited = [[0]*N for _ in range(N)]
    for x, y in zeroPos:
        if visited[x][y] == 0:
            bfs(x, y)
            res += 1

    #3. 나머지 클릭
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and board[i][j] != '*':
                res += 1


    print(f'#{tc} {res}')
