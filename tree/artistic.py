from collections import deque
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

visited = [[0]*n for _ in range(n)]
group_block_cnt = 0
group_val = 0

def out_bound(x,y):
    return x<0 or y<0 or x>=n or y>=n

def dfs(x,y):
    global group_block_cnt, visited
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if out_bound(nx,ny):
            continue

        if graph[nx][ny] == group_val and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            group_block_cnt += 1
            dfs(nx,ny)

def getGroupInfo():
    global visited, group_block_cnt, group_val
    group_num = 0
    group_info = []
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                group_num += 1
                group_block_cnt = 1
                group_val = graph[i][j]
                dfs(i,j)
                group_info.append((group_num,group_val,group_block_cnt))

    return group_info

print(getGroupInfo())

def bfs(start_x,start_y):
    global visited, group_block_cnt, group_val
    q = deque()
    q.append((start_x,start_y))
    visited[start_x][start_y] = 1

    while q:
        x,y = q.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if out_bound(nx,ny):
                continue
            if visited[nx][ny] == 0 and graph[nx][ny] == group_val:
                visited[nx][ny] = 1
                group_block_cnt += 1
                q.append((nx,ny))


def getGroupInfo():
    global visited, group_val, group_block_cnt
    group_info = []
    group_num = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                group_num += 1
                group_block_cnt = 1
                group_val = graph[i][j]
                bfs(i,j)
                group_info.append((group_num, group_val, group_block_cnt))

    return group_info

print(getGroupInfo())