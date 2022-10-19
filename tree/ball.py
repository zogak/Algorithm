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

def move(teamInfo):
    global graph
    for i, info in enumerate(teamInfo):
        if teamDir[i] == True:
            teamInfo[i][0] = (teamInfo[i][0]-1)%len(teams[i])
            teamInfo[i][1] = (teamInfo[i][1]-1)%len(teams[i])
        else:
            teamInfo[i][0] = (teamInfo[i][0]+1)%len(teams[i])
            teamInfo[i][1] = (teamInfo[i][1]+1)%len(teams[i])
    
    for i in range(m):
        for person in teams[i]:
            if person == teamInfo[i][0]: #head
                graph[person[0]][person[1]] = 1
            elif person == teamInfo[i][1]: #tail
                graph[person[0]][person[1]] = 3




# main
# 팀 정보 저장
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

#print(teams)
#print(teamInfo)
for i, info in enumerate(teamInfo):
    h = teams[i].index(teamInfo[i][0])
    t = teams[i].index(teamInfo[i][1])
    teamInfo[i] = [h,t]

# 라운드 시작
for round in range(k):
    pass