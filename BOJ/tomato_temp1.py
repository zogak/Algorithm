import sys
from collections import deque

m, n, h = map(int, input().split())
big_box = []
rippen = 0
empty = 0
total = m*n*h
day = 0

#input
for i in range(h):
    small_box = []
    for j in range(n):
        temp = list(map(int, sys.stdin.readline().split()))
        for k in range(m):
            if temp[k] == 1:
                rippen += 1
            elif temp[k] == -1:
                empty += 1
        small_box.append(temp)
    big_box.append(small_box)
    
dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs(z,x,y):
    global rippen
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
            if big_box[nz][nx][ny] == -1:
                continue
            
            visited[nz][nx][ny] = visited[z][x][y] + 1
            
            # not rippen
            if big_box[nz][nx][ny] == 0:
                big_box[nz][nx][ny] = 1
                rippen += 1
                q.append((nz,nx,ny))
    
    return day

while True:
    # 처음부터 다 익은 상태
    if rippen + empty == total:
        print(0)
        break

    visited = [[[0]*m for _ in range(n)] for _ in range(h)]
    q = deque()
    for z in range(h):
        for x in range(n):
            for y in range(m):
                if visited[z][x][y] == 0 and big_box[z][x][y] == 1:
                    visited[z][x][y] = 1
                    q.append((z, x, y))
    day = bfs(z,x,y)

    # 다 익히지 못하는 상태
    if rippen + empty != total:
        print(-1)
        break
    # 다 익힌 상태
    else:
        print(day - 1)
        break