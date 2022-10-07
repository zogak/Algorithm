n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def tetro(x,y):
    ret = 0
    cnt = 0
    visited = set()

    while True:
        cnt += 1
        ret += graph[x][y]
        visited.add((x,y))

        if cnt == 4:
            return ret

        temp = []
        for k in range(4):
            nx = x+ dx[k]
            ny = y + dy[k]

            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue

            if (nx,ny) in visited:
                continue

            temp.append((graph[nx][ny], nx, ny))
        temp.sort(key = lambda x : x[0], reverse=True)
        x,y = temp[0][1], temp[0][2]


res = 0
for i in range(n):
    for j in range(m):
        res = max(res, tetro(i,j))

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