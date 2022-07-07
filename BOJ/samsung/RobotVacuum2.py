n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[0]*m for _ in range(n)]
answer = 1
cnt = 0
visited[r][c] = 1

# 북동남서
dir = [(-1,0), (0,1), (1,0), (0,-1)]

while True:
    # rotate to left
    d = (d+3)%4

    nr = r + dir[d][0]
    nc = c + dir[d][1]

    if graph[nr][nc]==0 and visited[nr][nc]==0:
        # update pos
        r = nr
        c = nc

        #clean
        answer += 1
        visited[r][c] = 1
        cnt = 0
    
    else:
        cnt += 1
    
    if cnt==4:
        cnt = 0

        behind_dir = (d+2)%4
        nr = r + dir[behind_dir][0]
        nc = c + dir[behind_dir][1]

        if graph[nr][nc] == 1:
            break
        
        else:
            r = nr
            c = nc

print(answer)