import heapq
M, N = map(int, input().split()) #가로, 세로
board = [list(map(int, input())) for _ in range(N)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(i,j):
    q = []
    walls = [[int(1e9)]*M for _ in range(N)]
    heapq.heappush(q, (0, i, j))
    walls[0][0] = 0

    while q:
        wall, x, y = heapq.heappop(q)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or ny<0 or nx>=N or ny>=M: continue
            if walls[nx][ny] < wall: continue

            cost = wall + board[nx][ny]
            if cost < walls[nx][ny] : 
                walls[nx][ny] = cost
                heapq.heappush(q, (cost,nx,ny))
    
    return walls[N-1][M-1]

print(bfs(0,0))
