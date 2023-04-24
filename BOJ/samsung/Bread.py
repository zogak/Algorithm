from collections import deque
n, m = map(int, input().split())
'''
보드 입력받기
베이스 캠프 -> int(1e9)
지나가지 못하는 곳 -> -int(1e9)
편의점 -> -1, -2, ..
'''
baseCamps = [] #베이스 캠프 위치
board = [[0]*(n+1)]
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] == 1: #베이스캠프
            baseCamps.append([i,j])
            tmp[j] = int(1e9)
    board.append([0]+tmp)

#편의점 위치
stores = [[0,0]]
for _ in range(m):
    stores.append(list(map(int, input().split())))

#편의점 보드에 기록
for i in range(1, len(stores)):
    x, y = stores[i]
    board[x][y] = -i

#각 편의점에서 가까운 베이스캠프 순으로 정보 저장
store_camp_info = {i:[] for i in range(1, len(stores))}
def getDistance(sx,sy,bx,by):
    return abs(sx-bx)+abs(sy-by)

for i in range(1, len(stores)):
    sortedBaseCamps = [] #x, y, 편의점으로부터 거리
    for baseCamp in baseCamps:
        tmp = baseCamp + [getDistance(stores[i][0], stores[i][1], baseCamp[0], baseCamp[1])]
        sortedBaseCamps.append(tmp)
    
    sortedBaseCamps.sort(key = lambda x : (x[2], x[0], x[1])) #거리,행,열 순서
    store_camp_info[i] = sortedBaseCamps

# 원하는 편의점 ~ 사람 위치 가는 최단 거리 수 작성하기
dx = [-1,0,0,1]
dy = [0,-1,1,0] #위 왼 오 아래
def bfs(px,py,sx,sy):
    q = deque()
    visited = [[int(1e9)]*(n+1) for _ in range(n+1)]
    q.append([sx, sy])
    visited[sx][sy] = 1

    while q:
        x, y = q.popleft()
        if x==px and y==py: break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=n: continue
            if visited[nx][ny] != int(1e9): continue
            if board[nx][ny] == -int(1e9): continue

            visited[nx][ny]= visited[x][y] + 1
            q.append([nx,ny])

    return visited

# def backBfs(px,py,sx,sy,visited):
#     q = deque()
#     q.append([sx,sy])
#     visited[sx][sy] = -visited[sx][sy]
#     while q:
#         x,y = q.popleft()
#         if x==px and y==py: break
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if nx<0 or ny<0 or nx>=n or ny>=n: continue
#             if visited[nx][ny] < 0: continue
#             if board[nx][ny] == -int(1e9): continue

#             if visited[nx][ny] == -visited[x][y] - 1:
#                 visited[nx][ny] = -visited[nx][ny]
#                 q.append([nx,ny])
#     return visited


#main
t = 0 #시간
peopleOnTheBoard = [] #번호,x,y
arrivedPeopleCnt = 0
while arrivedPeopleCnt < m:
    t += 1
    if peopleOnTheBoard: #격자 위에 사람 있으면
        peopleToRemove = set() #지울 사람 인덱스
        # 1. 사람 편의점 방향으로 1칸 이동
        for i in range(len(peopleOnTheBoard)):
            peopleNum, peopleX, peopleY = peopleOnTheBoard[i]
            routeBoard = bfs(peopleX,peopleY,stores[peopleNum][0],stores[peopleNum][1])

            moveNominees = []
            dist = int(1e9)

            #이동할 곳 하나 구하기
            for k in range(4):
                nx = peopleX + dx[k]
                ny = peopleY + dy[k]

                if nx<0 or ny<0 or nx>=n or ny>=n: continue
                
                if routeBoard[nx][ny] <= dist:
                    dist = routeBoard[nx][ny]
                    moveNominees.append([nx,ny])
            print(moveNominees)
            #이동
            targetX, targetY = moveNominees[0]
            peopleOnTheBoard[i] = [peopleNum,targetX, targetY]

            # 2. 편의점 도착한 사람 수 세어주기
            if board[targetX][targetY] == -peopleNum: #편의점 도착
                arrivedPeopleCnt += 1
                peopleToRemove.add(i)
                board[targetX][targetY] = -int(1e9) #막기
                break

        # 편의점에 도착한 사람은 peopleOnTheboard에서 삭제
        for item in peopleToRemove: del peopleOnTheBoard[item]
        
    #3. 가고 싶은 편의점과 가장 가까운 베이스 캠프 들어가기
    if t<=m:
        for baseCamp in store_camp_info[t]:
            if board[baseCamp[0]][baseCamp[1]] == -int(1e9): continue #막힌 곳
            peopleOnTheBoard.append([t, baseCamp[0], baseCamp[1]]) #들어가고
            board[baseCamp[0]][baseCamp[1]] = -int(1e9) #막기

    # if arrivedPeopleCnt == m: #모두 편의점 도착
    #     break

print(t)