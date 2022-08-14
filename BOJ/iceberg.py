from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
answer = 0

def bfs(startX, startY):
    q = deque()
    q.append((startX, startY))
    visited[startX][startY] = 1

    while q:
        item = q.popleft()
        x, y = item[0], item[1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0  or nx >= n or ny >= m :
                continue
            
            if graph[nx][ny] == 0:
                melting[x][y] += 1
            
            if graph[nx][ny] > 0 and visited[nx][ny] == 0:
                q.append((nx,ny))
                visited[nx][ny] = 1

day = 0
while True:
    day += 1
    cnt = 0
    flag = False
    melting = [[0]*m for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            if graph[i][j] > 0 and visited[i][j] == 0:
                flag = True
                bfs(i,j)
                cnt += 1
    
    #print('덩어리:', cnt)
    if cnt > 1:
        answer = day - 1
        break

    if not flag:
        answer = 0
        break
    
    #녹이기 update
    for i in range(1,n):
        for j in range(1,m):
            if melting[i][j] > 0:
                if melting[i][j] > graph[i][j]:
                    graph[i][j] = 0
                else:
                    graph[i][j] -= melting[i][j]

    # print('녹인 후')
    # print(graph)

print(answer)


'''
[[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 2, 4, 1, 0, 0],
 [0, 1, 0, 1, 5, 0, 0],
 [0, 5, 4, 1, 2, 0, 0],
 [0, 0, 0, 0, 0, 0, 0]]

--------------------------

[[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 3, 0, 0, 0],
 [0, 0, 0, 0, 4, 0, 0],
 [0, 3, 2, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0]]
'''