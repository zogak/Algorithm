'''
벽을 1개까지 깨도 되긴 하지만, 일단 벽이 없는 곳을 '우선적'으로 가야한다.
'''
import heapq
N, M = map(int, input().split()) # 세로, 가로
board = [list(map(int, input())) for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]
def bfs(i,j,wall):
    q = []
    visited = [[int(1e9)]*M for _ in range(N)]
    heapq.heappush(q, (wall, i, j))
    visited[i][j] = 1

    while q:
        wallCnt, x, y = heapq.heappop(q)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or ny<0 or nx>=N or ny>=M: continue
            if visited[nx][ny] != int(1e9): continue
            
            cost = wallCnt + board[nx][ny]
            if cost > 1: continue

            visited[nx][ny] = visited[x][y] + 1
            heapq.heappush(q, (cost, nx, ny))

    return (visited[N-1][M-1] if visited[N-1][M-1] !=int(1e9) else -1)

print(bfs(0,0,0))
'''
4 4
0000
0100
1111
0000
'''