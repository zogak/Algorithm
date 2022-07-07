from collections import deque

m, n, h = map(int, input().split())
box = []

#input
box = [list(list(map(int, input().split())) for _ in range(n)) for _ in range(h)]

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    while q:
        z, x, y = q.popleft()
        day = visited[z][x][y]

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx<0 or ny<0 or nz<0 or nx>=n or ny>=m or nz>=h:
                continue
            if visited[nz][nx][ny] == 1:
                continue
            if box[nz][nx][ny] == -1:
                continue
            
            visited[nz][nx][ny] = visited[z][x][y] + 1
            
            # not rippen
            if box[nz][nx][ny] == 0:
                box[nz][nx][ny] = 1
                q.append((nz,nx,ny))
    return day
    
visited = [[[0]*m for _ in range(n)] for _ in range(h)]
q = deque()
for z in range(h):
    for x in range(n):
        for y in range(m):
            if visited[z][x][y] == 0 and box[z][x][y] == 1:
                visited[z][x][y] = 1
                q.append((z, x, y))
day = bfs()

flag = 0
for z in range(h):
    for x in range(n):
        for y in range(m):
            if box[z][x][y] == 0:
                flag = 1

if flag == 1:
    print(-1)