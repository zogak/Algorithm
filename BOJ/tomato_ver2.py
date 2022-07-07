from collections import deque

m, n, h = map(int, input().split())

box = [list(list(map(int, input().split())) for _ in range(n)) for _ in range(h)]
visited = [list([0]*m for _ in range(n)) for _ in range(h)]
dx = [-1,0,1,0,0,0]
dy = [0,1,0,-1,0,0]
dz = [0,0,0,0,-1,1]

def bfs():
    while q:
        z, x, y = q.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx<0 or ny<0 or nz<0 or nx>=n or ny>=m or nz>=h:
                continue

            if box[nz][nx][ny] == 0 and visited[nz][nx][ny] == 0:
                visited[nz][nx][ny] = 1
                q.append((nz, nx,ny))
                box[nz][nx][ny] = box[z][x][y] + 1

q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                visited[i][j][k] = 1
                q.append((i,j,k))
bfs()

flag = False
res = -2
for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 0:
                flag = True
            res = max(res, box[i][j][k])

if flag:
    print(-1)
else:
    print(res - 1)