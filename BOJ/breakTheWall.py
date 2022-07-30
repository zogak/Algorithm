from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(startX, startY):
    cnt = 0
    visited = [[0]*m for _ in range(n)]
    q = deque()
    q.append((startX, startY))
    visited[startX][startY] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                q.append((nx,ny))
                visited[nx][ny] = 1
                cnt += 1
    
    return cnt+1


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            print((bfs(i,j)%10), end='')
        elif graph[i][j] == 0:
            print(0, end='')
    print()

