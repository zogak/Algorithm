M, N = map(int, input().split()) #세로, 가로
board = [list(map(int, input().split())) for _ in range(M)]

visited = [[0]*N for _ in range(N)]
check = [[0]*N for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dfs(x, y):
    global visited, check
    visited[x][y] = 1

    if nx==M-1 and ny==N-1: return 1
    

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx<0 or ny<0 or nx>=M or ny>=N : continue
        if board[nx][ny] >= board[x][y] : continue
        if visited[nx][ny] : continue

        check[nx][ny] = dfs(nx,ny)
            
