from collections import deque
n = int(input())
graph = []
shark_x, shark_y = 0,0
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] == 9:
            shark_x = i
            shark_y = j
    graph.append(temp)

time = 0
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(start_x, start_y, shark_size):
    visited = [[0]*n for _ in range(n)]
    q = deque()
    q.append((start_x, start_y))
    visited[start_x][start_y] = 1
    eatable = []
    while q:
        x, y = q.popleft()
        for i in range(4):
            
            nx = x + dx[i]
            ny = y + dy[i]

            # 못 지나감
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue

            if graph[nx][ny] > shark_size:
                continue
            
            # 지나감
            if visited[nx][ny]==0:
                if graph[nx][ny] != 0:
                    #작은 물고기 (먹을 수 있음)
                    if graph[nx][ny] < shark_size:
                        q.append((nx,ny))
                        eatable.append((nx,ny))
                    #같은 물고기 (먹을 수 없고 지나가기만)
                    else:
                        q.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1
                else:
                    q.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1
    if not eatable:
        print('no')
        return 0, start_x, start_y
    if len(eatable) == 1:
        print('one')
        eatable_x, eatable_y = eatable[0][0], eatable[0][1]
        time = visited[eatable_x][eatable_y] - 1
        return time, eatable_x, eatable_y
    
    else:
        nominee = []
        for eat in eatable:
            nominee.append((visited[eat[0]][eat[1]]-1, eat[0], eat[1])) #(dist,x,y)
        
        nominee.sort(key = lambda x : (x[0], x[1], x[2]))
        print('many', len(nominee))
        return nominee[0]

shark_size = 2
res, cnt = 0, 0
while True:
    time, shark_x, shark_y = bfs(shark_x, shark_y, shark_size)
    if time == 0:
        break
    else:
        res += time
        graph[shark_x][shark_y] = 0
        cnt += 1
        if cnt == shark_size:
            shark_size += 1
            cnt = 0
            
print(res)