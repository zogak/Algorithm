from collections import deque
N, M = map(int, input().split())
# 보드입력
board = []
for i in range(N):
    tmp = list(input())
    for j in range(M):
        if tmp[j] == '0': #minsik 출발 위치
            minsikX, minsikY = i, j
    board.append(tmp)

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(i, j, c):
    res = int(1e9)
    q = deque()
    visited = [[0]*M for _ in range(N)]
    q.append((i,j,c,1<<6))
    visited[i][j] = 1<<6

    while q:
        x, y, cnt, keys = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #이동 불가능한 경우들
            #out of bound
            if nx<0 or ny<0 or nx>=N or ny>=M: continue
            #walked more
            if cnt > res: continue
            #exit
            if board[nx][ny] == '1': #탈출구 여러개인 경우 처리방법
                res = min(res, cnt+1)
                continue
            #already visited with same condition
            if visited[nx][ny] == keys: continue
            #wall
            if board[nx][ny] == '#': continue
            #door and no key
            if board[nx][ny].isupper():
                idx = ord(board[nx][ny]) - ord('A')
                if (1<<idx) & (keys-(1<<6) if (keys&(1<<6)) != 0 else keys) == 0: continue

            #이동 가능한 경우들
            #get new key
            if board[nx][ny].islower():
                idx = ord(board[nx][ny]) - ord('a')
                keys = (1<<idx) | keys

            visited[nx][ny] = keys
            q.append((nx,ny,cnt+1,keys))

    return res if res != int(1e9) else -1

print(bfs(minsikX, minsikY, 0))

'''
4 4
..F1
...#
f...
.0..
'''