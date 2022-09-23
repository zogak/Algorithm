#readline으로 입력받았을 때 마지막 줄바꿈 처리하는 방법
from collections import deque

n, m = map(int, input().split())
graph = []

for i in range(n):
    temp = list(input())
    for j in range(m):
        if temp[j] == 'R':
            redPos = (i,j)
        if temp[j] == 'O':
            endPos = (i,j)
        if temp[j] == 'B':
            bluePos = (i,j)
    graph.append(temp)

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(rx_start, ry_start, bx_start, by_start):
    q = deque()
    cnt = 1
    q.append((cnt, rx_start, ry_start, bx_start, by_start))

    while q:
        cnt, rx, ry, bx, by = q.popleft()

        for i in range(4):
            nrx = rx + dx[i]
            nry = ry + dy[i]
            nbx = bx + dx[i]
            nby = by + dy[i]

            # # 벽인 경우 처리
            # if nrx==0 or nry==0 or nrx==n-1 or nry==m-1:
            #     nrx -= dx[i]
            #     nry -= dy[i]
            # if nbx==0 or nby==0 or nbx==n-1 or nby==m-1:
            #     nbx -= dx[i]
            #     nby -= dy[i]
            print(nrx,nry,nbx,nby)

            # 파란 구슬 계속 이동
            while graph[nbx][nby] != '#' and graph[nbx][nby] != 'O':
                nbx = nbx + dx[i]
                nby = nby + dy[i]
            
            # 벽이나 구멍이 아닐 경우 빨간 구슬 계속 이동 가능
            while graph[nrx][nry] != '#' and graph[nrx][nry] != 'O':
                nrx = nrx + dx[i]
                nry = nry + dy[i]
                cnt += 1

            if nrx == nbx and nry == nby :
                if abs(nrx-rx)+abs(nry-ry) > abs(nbx-bx)+abs(nby-by):
                    nrx = nrx - dx[i]
                    nry = nry - dy[i]
                else:
                    nbx = nbx - dx[i]
                    nby = nby - dy[i]

            print('움직인 후')
            print('빨간공 위치', nrx, nry)
            print('파란공 위치', nbx, nby)

            if graph[nbx][nby] == 'O':
                print('blue over')
                continue 

            if graph[nrx][nry] == 'O' and cnt <= 10:
                return cnt

            
            
            q.append((cnt+1, nrx,nry,nbx,nby))
            # if [nrx,nry,nbx,nby] not in visited:
            #     q.append((cnt+1, nrx,nry,nbx,nby))
            #     visited.append([nrx,nry,nbx,nby])

        if cnt > 10:
            return -1
    #return -1

ans = bfs(redPos[0], redPos[1], bluePos[0], bluePos[1])

print(ans)