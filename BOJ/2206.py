from collections import deque
N, M = map(int, input().split()) # 세로, 가로
board = [list(map(int, input())) for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def bfs(i,j,wall):
    q = deque()
    visited = [[0]*M for _ in range(N)]
    q.append((i,j,wall))
    visited[i][j] = 1

    while q:
        x, y, wallCnt = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or ny<0 or nx>=N or ny>=M: continue
            if visited[nx][ny] != 0: continue
            if wallCnt+board[nx][ny] > 1: continue

            visited[nx][ny] = visited[x][y] + 1
            q.append((nx,ny,wallCnt+board[nx][ny]))

    return (visited[N-1][M-1] if visited[N-1][M-1] !=0 else -1)

print(bfs(0,0,0))
