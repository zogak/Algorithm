n = int(input())

graph = [list(map(int, input())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dfs(i,j):
    global cnt
    visited[i][j] = 1
    cnt += 1
    for k in range(4):
        ni = i+dx[k]
        nj = j+dy[k]

        if ni<0 or nj<0 or ni>=n or nj>=n:
            continue
        if visited[ni][nj] == 1:
            continue

        if graph[ni][nj] == 1:
            dfs(ni,nj)
    return cnt

total = 0
houses = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j]==0:
            cnt = 0
            houses.append(dfs(i,j))
            total += 1

print(total)
houses.sort()
for house in houses:
    print(house)