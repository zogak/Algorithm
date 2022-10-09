n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def dfs(i,j):
    global cnt, value

    if cnt == 4:
        return True

    for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]

        if ni<0 or nj<0 or ni>=n or nj>=n:
            continue

        if visited[ni][nj] == 1:
            continue
        
        cnt += 1
        value += graph[ni][nj]
        dfs(ni,nj)
        visited[ni][nj] = 0
        value -= graph[ni][nj]


visited = [[0]*m for _ in range(n)]
res = 0
for i in range(n):
    for j in range(m):
        value = graph[i][j]
        cnt = 1
        visited[i][j] = 1
        if dfs(i,j):
            res = max(res, value)
            visited[i][j] = 0
        print(res)
   
        
        #res = max(res, tetro(i,j))

#가로
#위아래 다
for i in range(1,n-1):
    for j in range(1,m-1):
        res = max(res, graph[i][j-1]+graph[i][j]+graph[i][j+1]+graph[i-1][j])
        res = max(res, graph[i][j-1]+graph[i][j]+graph[i][j+1]+graph[i+1][j])
#맨위
for j in range(1, m-1):
    res = max(res, graph[0][j-1]+graph[0][j]+graph[0][j+1]+graph[1][j])
#맨아래
for j in range(1, m-1):
    res = max(res, graph[n-1][j-1]+graph[n-1][j]+graph[n-1][j+1]+graph[n-2][j])

#세로
#양옆 다
for i in range(1,m-1):
    for j in range(1,n-1):
        res = max(res, graph[j-1][i]+graph[j][i]+graph[j+1][i]+graph[j][i-1])
        res = max(res, graph[j-1][i]+graph[j][i]+graph[j+1][i]+graph[j][i+1])
#맨 왼쪽
for i in range(1,n-1):
    res = max(res, graph[i-1][0]+graph[i][0]+graph[i+1][0]+graph[i][1])
#맨 오른
for i in range(1, n-1):
    res = max(res, graph[i-1][m-1]+graph[i][m-1]+graph[i+1][m-1]+graph[i][m-2])

print(res)