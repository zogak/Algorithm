from collections import deque

n = int(input())
info = {}

for i in range(n*n):
    temp = list(map(int, input().split()))
    info[temp[0]] = temp[1:]

graph = [[0]*(n+1) for _ in range(n+1)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

# def dfs(startX, startY, student):
#     temp = []
#     q = deque()
#     visited = [[0]*(n+1) for _ in range(n+1)]

#     q.append((startX, startY))
#     visited[startX][startY] = 1

#     while q:
#         likeCnt, emptyCnt = 0, 0
#         x, y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx<=0 or ny<=0 or nx>n or ny>n:
#                 continue
#             if visited[nx][ny] == 0:
#                 visited[nx][ny] = 1
                
#                 if graph[nx][ny] in info[student]:
#                     likeCnt +=1
#                 elif graph[nx][ny] == 0:
#                     emptyCnt += 1
                
#                 q.append((nx,ny))
#         temp.append((likeCnt, emptyCnt, x, y))

#     temp.sort(key = lambda x : (x[0],x[1],x[2],x[3]), reverse=True)
#     print(temp)
#     graph[temp[0][2]][temp[0][3]] = student

def setPosition(student):
    temp = []
    for x in range(1, n+1):
        for y in range(1, n+1):
            likeCnt, emptyCnt = 0,0
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if nx<=0 or ny<=0 or nx>n or ny>n:
                    continue
                
                if graph[nx][ny] in info[student]:
                    likeCnt +=1
                elif graph[nx][ny] == 0:
                    emptyCnt += 1
            temp.append((likeCnt, emptyCnt, x, y))
    temp.sort(key = lambda x : (x[0],x[1],x[2],x[3]), reverse=True)
    
    for t in temp:
        if graph[t[2]][t[3]] != 0:
            continue
        else:
            graph[t[2]][t[3]] = student
            break


for item in info.keys():
    #dfs(1,1,item)
    #print(item)
    setPosition(item)

#print(graph)

res = 0
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] != 0:
            cnt = 0
            for k in range(4): 
                ni = i + dx[k]
                nj = j + dy[k]

                if ni<=0 or nj<=0 or ni>n or nj>n:
                    continue
                if graph[ni][nj] in info[graph[i][j]]:
                    cnt += 1
            if cnt == 1:
                res += 1
            elif cnt == 2:
                res += 10
            elif cnt == 3:
                res += 100
            elif cnt == 4:
                res += 1000

print(res)