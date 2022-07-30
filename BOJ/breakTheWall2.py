from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(startX, startY, group):
    cnt = 1
    q = deque()
    q.append((startX, startY))
    graph[startX][startY] = group
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
                graph[nx][ny] = group
                visited[nx][ny] = 1
                cnt += 1
    
    return cnt

group = -1
zeroCnt = {}

#zeroCnt 만들기
visited = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and visited[i][j] == 0:
            zeroCnt[group] = bfs(i,j,group)
            group -= 1

groupNum = len(zeroCnt.keys())

res = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            groupVisited = []
            cnt = 1
            
            for k in range(4):
                ni = i +dx[k]
                nj = j +dy[k]

                if ni<0 or nj<0 or ni>=n or nj>=m:
                    continue
                if graph[ni][nj] < 0 and graph[ni][nj] not in groupVisited:
                    cnt += zeroCnt[graph[ni][nj]]
                    groupVisited.append(graph[ni][nj])

            res[i][j] = cnt%10

for r in res:
    print(''.join(map(str, r)))