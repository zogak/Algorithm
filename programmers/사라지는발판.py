import sys
sys.setrecursionlimit(10**6)
def solution(board, aloc, bloc):
    n = len(board)
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    def outOfBound(x, y):
        if x<0 or y<0 or x>=n or y>=n: return True
        return False

    def dfs(whoseTurn, cnt, aloc, bloc):
        nonlocal res, flag
        print(f'turn : {whoseTurn}, cnt : {cnt}, aloc : {aloc}, bloc : {bloc}')
        if flag: return
        
        if aloc == bloc : 
            if cnt[whoseTurn] > max(res):
                res = cnt
            print(f'here, {res}')
            flag = True
        else: flag = False

        if whoseTurn == 0:
            cnt[whoseTurn] += 1
            x, y = aloc
        elif whoseTurn == 1:
            cnt[whoseTurn] += 1
            x, y = bloc

        outOfBoundCnt, wallCnt = 0, 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if outOfBound(nx,ny) : 
                outOfBoundCnt += 1
                continue
            if board[nx][ny] == 0: 
                wallCnt += 1
                continue

            dfs(whoseTurn^1, cnt, [nx,ny] if whoseTurn==0 else aloc, [nx,ny] if whoseTurn==1 else bloc)

        if outOfBoundCnt == 4 or wallCnt == 4:
            if cnt[whoseTurn] > max(res):
                res = cnt
            print(f'here, {res}')
            flag = True

    res = [0,0]
    flag = False

    if aloc == bloc :
        res = 1
    
    else:
        dfs(0, [0,0], aloc, bloc)
    
    return sum(res)

print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1,0], [1,2]))