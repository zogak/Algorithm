import sys
input = sys.stdin.readline
from collections import deque
n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dir = [(-1,0), (0,1), (1,0), (0,-1)] #북동남서

def bfs(i, j):
    q = deque()
    q.append((i,j))

    union_pos = []
    union_pos.append((i,j))

    sum = graph[i][j]
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dir[i][0]
            ny = y + dir[i][1]

            if nx<0 or ny<0 or nx>=n or ny>=n or visited[nx][ny] == 1:
                continue

            if l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                visited[nx][ny] = 1
                q.append((nx,ny))
                union_pos.append((nx,ny))
                sum += graph[nx][ny]
    
    return union_pos, sum



res = 0
while True:
    visited = [[0]*n for _ in range(n)]
    flag = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                country, total = bfs(i,j)
                #print('country', country)
                #print('total', total)

                if len(country) > 1:
                    flag = 1
                    divided_population = total // len(country)
                    #print('divided', divided_population)
                    for cx, cy in country:
                        graph[cx][cy] = divided_population
    
    if flag == 0:
        break
    
    res += 1

print(res)