import copy
n,m,k,c = map(int, input().split())
graph = []
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == -1:
            temp[j] = 'w'
    graph.append(temp)

res = 0

dx = [-1,0,1,0]
dy = [0,1,0,-1]
degac_x = [-1,-1,1,1]
degac_y = [-1,1,1,-1]

def grow(graph):
    for i in range(n):
        for j in range(n):
            nearTreeCnt = 0
            # 벽
            if graph[i][j] == 'w':
                continue
            # 제초제 일년 지남
            if graph[i][j] < 0 and graph[i][j] != -c:
                graph[i][j] += 1
                continue
            # 나무다
            if graph[i][j] > 0:
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]

                    if ni<0 or nj<0 or ni>=n or nj>=n:
                        continue
                    if graph[ni][nj] == 'w':
                        continue

                    # 나무다
                    if graph[ni][nj] > 0:
                        nearTreeCnt += 1
                graph[i][j] += nearTreeCnt
                
def breed(afterBreed):
    for i in range(n):
        for j in range(n):
            # 벽
            if graph[i][j] == 'w':
                continue
            # 나무다
            if graph[i][j] > 0:
                possible = []
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]

                    if ni<0 or nj<0 or ni>=n or nj>=n:
                        continue
                    if graph[ni][nj] == 'w':
                        continue
                        
                    #번식 가능 위치
                    if graph[ni][nj] == 0:
                        possible.append((ni,nj))
            
                if not possible:
                    continue
                amount = graph[i][j] // len(possible)
                for pos in possible:
                    afterBreed[pos[0]][pos[1]] += amount

def getDeathAmount(k,x,y):
    deathAmount = afterBreed[x][y]
    for p in range(4):
        nx = x + degac_x[p]
        ny = y + degac_y[p]
        if nx<0 or ny<0 or nx>=n or ny>=n:
            continue
        if afterBreed[nx][ny] == 'w':
            continue
        if afterBreed[nx][ny] <= 0:
            continue
        
        # 나무
        if afterBreed[nx][ny] > 0:
            deathAmount += afterBreed[nx][ny]
        
        i = 1
        while True:
            if i == k:
                break
            nx = nx + degac_x[p]
            ny = ny + degac_y[p]
            
            if nx<0 or ny<0 or nx>=n or ny>=n:
                i += 1
                continue
            if afterBreed[nx][ny] == 'w':
                break
            if afterBreed[nx][ny] <= 0:
                break

            # 나무
            if afterBreed[nx][ny] > 0:
                deathAmount += afterBreed[nx][ny]           
            i += 1

    return deathAmount

def pesticideCheck(k):
    temp = []
    for i in range(n):
        for j in range(n):
            if afterBreed[i][j] == 'w':
                continue
            
            temp.append((getDeathAmount(k,i,j), i,j))
    #print(temp)
    if not temp:
        return (-1,-1)
    temp.sort(key = lambda x : (-x[0],x[1],x[2]))  
    return (temp[0][1], temp[0][2])

def pesticide(x, y, afterBreed, c):
    global res
    
    if afterBreed[x][y] <= 0:
        afterBreed[x][y] = -c
        return
    if afterBreed[x][y] > 0:
        res += afterBreed[x][y]
    afterBreed[x][y] = -c

    for p in range(4):
        nx = x + degac_x[p]
        ny = y + degac_y[p]

        if nx<0 or ny<0 or nx>=n or ny>=n:
            continue
        if afterBreed[nx][ny] == 'w':
            continue
        # 빈 공간 또는 이미 제초제인 곳에 제초제 뿌려지면 거기서 스탑
        if afterBreed[nx][ny] <= 0:
            afterBreed[nx][ny] = -c
            continue
        
        if afterBreed[nx][ny] > 0:
            res += afterBreed[nx][ny]
        afterBreed[nx][ny] = -c
        
        i = 1
        while True:
            if i == k:
                break
            nx = nx + degac_x[p]
            ny = ny + degac_y[p]

            if nx<0 or ny<0 or nx>=n or ny>=n:
                i += 1
                continue
            if afterBreed[nx][ny] == 'w':
                break
            if afterBreed[nx][ny] <= 0:
                afterBreed[nx][ny] = -c
                break

            if afterBreed[nx][ny] > 0:
                res += afterBreed[nx][ny]
            afterBreed[nx][ny] = -c
            i += 1

for year in range(m):
    grow(graph)
    print(graph)
    afterBreed = copy.deepcopy(graph)
    breed(afterBreed)
    print(afterBreed)
    target_x, target_y = pesticideCheck(k)
    print(target_x, target_y)
    if target_x != -1 and target_y != -1:
        pesticide(target_x, target_y, afterBreed, c)
    print(afterBreed)
    graph = afterBreed
    print('res', res)
    print('---')

print(res)
'''
5 4 5 5
0 0 0 0 0 
0 0 0 -1 1 
0 0 5 0 0 
4 0 0 0 0 
2 0 -1 0 0
'''
