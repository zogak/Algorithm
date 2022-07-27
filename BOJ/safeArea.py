from collections import deque

n = int(input())
max_height = 0
graph = []

# 제일 높은 벽 저장하기 위해서
for i in range(n):
    tmp = list(map(int, input().split()))
    max_height = max(max_height, max(tmp))
    graph.append(tmp)

dx = [-1,0,1,0]
dy = [0,1,0,-1]

res = 1

#Q1. visit의 위치
def bfs(node, height):
    q = deque()
    q.append(node)
    visited[node[0]][node[1]] = 1
    
    while q:
        x, y = q.popleft()
        #visited[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue

            if graph[nx][ny] > height and visited[nx][ny]==0:
                q.append((nx,ny))
                visited[nx][ny] = 1 

for i in range(1, max_height):
    area = 0
    visited = [[0]*n for _ in range(n)]

    for p in range(n):
        for q in range(n):
            if visited[p][q] == 0 and graph[p][q]>i:
                bfs((p,q), i)
                area += 1

    res = max(res, area)

print(res)