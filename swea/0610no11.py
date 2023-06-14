T = int(input())
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def outOfBound(x, y):
    if x<0 or y<0 or x>=N or y>=N:
        return True
    return False

def dfs(cnt, length, connectCnt):
    global res, board, maxConnectCnt 
    if connectCnt > maxConnectCnt:
        maxConnectCnt = connectCnt
        res = length
    elif connectCnt == maxConnectCnt:
        res = min(res, length)

    if cnt == coreCnt:
        return

    if length > res:
        return
    
    x, y = corePos[cnt]
    for i in range(4):
        nx = x
        ny = y
        thisLength = 0
        isPossible = True
        visitList = []
        while True:
            nx += dx[i]
            ny += dy[i]

            if outOfBound(nx,ny):
                break
            if board[nx][ny] != 0 : #다른 코어가 있거나 전선이 있으면
                isPossible = False
                break
            thisLength += 1
            visitList.append((nx,ny))

        if isPossible:
            for itemX, itemY in visitList:
                board[itemX][itemY] = 2

            dfs(cnt+1, length+thisLength, connectCnt+1)
            for itemX, itemY in visitList:
                board[itemX][itemY] = 0
        
    dfs(cnt+1, length, connectCnt) #연결할 수 있는데 안하고도 해봐야함
      

for tc in range(1, T+1):
    res = int(1e9)
    N = int(input())
    corePos = []
    board = []
    for i in range(N):
        temp = list(map(int, input().split()))
        for j in range(N):
            if temp[j] == 1:
                corePos.append([i, j])
        board.append(temp)

    coreCnt = len(corePos)
    maxConnectCnt = 0

    dfs(0, 0, 0)

    print(f'#{tc} {res}')

'''
1
7    
0 0 1 0 0 0 0
0 0 1 0 0 0 0
0 0 0 0 0 1 0
0 0 0 0 0 0 0
1 1 0 1 0 0 0
0 1 0 0 0 0 0
0 0 0 0 0 0 0
'''