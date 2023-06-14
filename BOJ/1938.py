from collections import deque
n = int(input())
board = []
bPos = []
ePos = []
#board 입력
for i in range(n):
    tmp = input()
    for j in range(n):
        if tmp[j] == 'B':
            bPos.append([i,j])
        elif tmp[j] == 'E':
            ePos.append([i,j])

    board.append(tmp)

# 가로(0) 세로(1) 판단 
def garoSero(pos):
    if len(set(list(zip(*pos))[0])) == 1:
        return 0
    return 1

bDir = garoSero(bPos)
eDir = garoSero(ePos)

dx = [-1,0,1,1]
dy = [0,1,0,-1]

garoToSeroDx = [-1,0,1]
garoToSeroDy = [1,0,-1]
seroToGaroDx = [1,0,-1]
seroToGaroDy = [1,0,-1]

def outOfBound(x1,y1,x2,y2,x3,y3):
    if x1<0 or y1<0 or x2<0 or y2<0 or x3<0 or y3<0 or \
    x1>=n  or x1>=n or x2>=n or y2>=n or x3>=n or y3>=n:
        return True

    return False
        

def bfs():
    cnt = 0
    q = deque
    visited = [list([0]*n for _ in range(n)) for _ in range(2)]
    q.append(bPos, bDir)
    mid = bPos[1]
    visited[bDir][mid[0]][mid[1]] = 1

    while q:
        x1,y1,x2,y2,x3,y3,dir,cnt = q.popleft()
        if x1==ePos[0][0] and y1==ePos[0][1] and\
            x2==ePos[1][0] and y2==ePos[1][1] and\
            x3==ePos[2][0] and y2==ePos[2][1]:
            return cnt        

        for i in range(5):
            if i == 4:
                if dir==0:
                    if board[x1-1][y1]==1 or board[x2-1][y2]==1 or board[x3-1][y3]==1 or\
                    board[x1+1][y1]==1 or board[x2+1][y2]==1 or board[x3+1][y3]==1:
                        continue
                    
                    nx1 = x1+garoToSeroDx[0]
                    nx2 = x2+garoToSeroDx[1]
                    nx3 = x3+garoToSeroDx[2]
                    ny1 = y1+garoToSeroDy[0]
                    ny2 = y2+garoToSeroDy[1]
                    ny3 = y3+garoToSeroDy[2]
                    
            
            else:
                nx1 = x1 + dx[i]
                ny1 = y1+ dy[i]
                nx2 = x2 + dx[i]
                ny2 = y2 + dy[i]
                nx3 = x3 + dx[i]
                ny3 = y3 + dy[i]

                if outOfBound(nx1,ny1,nx2,ny2,nx3,ny3): continue
                if board[nx1][ny1]==1 or board[nx2][ny2]==1 or board[nx3][ny3]==1 : continue
                if visited[dir][nx2][ny2] == 1: continue

                visited[dir][nx2][ny2] == 1 #방문처리
                q.append([nx1,ny1,nx2,ny2,nx3,ny3],dir,cnt+1)

