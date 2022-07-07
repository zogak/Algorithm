from collections import deque
n = int(input())

graph = []
shark_size = 2
edible = 0
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 9:
            shark = (i,j)
        elif temp[j] != 0 or temp[j] < shark_size:
            edible += 1
    graph.append(temp)

visited = [[0]*n for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
time = 0

def bfs(i,j):
    
    q = deque()
    q.append((i,j))
    
    while q:
        x, y = q.popleft()
        visited[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=n or visited[nx][ny] == 1:
                continue

            q.append((nx,ny))


while True:
    if edible > 0:
        bfs(shark[0], shark[1])
    else:
        break

print(time)