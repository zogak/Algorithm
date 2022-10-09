import sys
input = sys.stdin.readline

n,m,k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[0]*n for _ in range(n)]
teams = []
teamInfo = []
teamDir = [True]*m

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def saveTeam(i,j):
    global temp, visited, info

    for k in range(4):
        ni = i + dx[k]
        nj = j + dy[k]
        if ni<0 or nj<0 or ni>=n or nj>=n:
            continue
        if graph[ni][nj] == 0:
            continue
        
        if visited[ni][nj] == 0:
            visited[ni][nj] = 1
            temp.append((graph[ni][nj], ni, nj))
            if graph[ni][nj] == 1:
                info[0] = (ni,nj)
            if graph[ni][nj] == 3:
                info[1] = (ni,nj)

            saveTeam(ni,nj)
    return

def move():
    pass

# main
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0 and visited[i][j] == 0:
            visited[i][j] = 1
            temp = [(graph[i][j], i, j)]
            if graph[i][j] == 1:
                info = [(i,j),0]
            elif graph[i][j] == 3:
                info = [0,(i,j)]
            else:
                info = [0,0]
            saveTeam(i,j)
            temp.sort(key = lambda x : x[0])
            team = []
            for t in temp:
                team.append((t[1], t[2]))
            teams.append(team)
            teamInfo.append(info)


