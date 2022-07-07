from collections import deque

m, n = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs():
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue

            if box[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx,ny))
                box[nx][ny] = box[x][y] + 1

q = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            visited[i][j] = 1
            q.append((i,j))
bfs()

flag = False
res = -2
for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            flag = True
        res = max(res, box[i][j])

if flag:
    print(-1)
else:
    print(res - 1)