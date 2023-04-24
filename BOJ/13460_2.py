from collections import deque
N, M = map(int, input().split())
board = []
exitX, exitY = 0,0
redX, redY = 0,0
blueX, blueY = 0,0
for i in range(N):
    tmp = list(input())
    for j in range(M):
        if tmp[j] == 'R':
            redX, redY = i,j
        elif tmp[j] == 'B':
            blueX, blueY = i,j
        elif tmp[j] == 'O': #탈출구
            exitX, exitY = i,j
    board.append(tmp)

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(redX, redY, blueX, blueY, exitX, exitY):
    q = deque()
    visited = set()
    q.append((redX, redY, blueX, blueY, 0))
    visited.add((redX,redY,blueX,blueY))

    while q:
        rx, ry, bx, by, cnt = q.popleft()

        if cnt > 10 :
            return -1

        if cnt <= 10 and rx==exitX and ry==exitY:
            return cnt

        for i in range(4):
            nrx, nry, nbx, nby = rx,ry,bx,by
            while nrx


            

            #
            if (nrx,nry,nbx,nby) in visited: continue

            #파란 구슬이 먼저 빠지는 상황
            if nbx == exitX and nby == exitY : continue

            #동시에 빠지는 상황
            if nbx == nrx == exitX and nby == nry == exitY : continue

            #다음 프로세스
            visited.add((nrx,nry,nbx,nby))
            q.append((nrx,nry,nbx,nby,cnt+1))

    return -1   
            
res = bfs(redX,redY,blueX,blueY,exitX,exitY)
print(res)