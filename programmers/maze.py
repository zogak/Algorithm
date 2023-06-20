import sys
sys.setrecursionlimit(10**6)
def solution(n, m, x, y, r, c, k):
    dx = [1, 0, 0, -1] #남서동북
    dy = [0, -1, 1, 0]
    
    info = {
        0 : 'd',
        1 : 'l',
        2 : 'r',
        3 : 'u'
    }
    res = "impossible"
    flag = False
    visited = []

    def dfs(i, j, cnt):
        nonlocal res, flag, visited
        print(visited)
        if flag : return
        #k안으로 어차피 못갈 바에 return
        if abs(r-i)+abs(c-j)+cnt > k: 
            return

        #도착했으면 flag로 막아주기
        if cnt == k and i == r and j == c:
            res = ''.join(visited)
            flag = True
            return
        
        for p in range(4):
            di = i + dx[p]
            dj = j + dy[p]

            if di <=0 or dj <=0 or di>n or dj>m: continue
            visited.append(info[p])
            dfs(di, dj, cnt+1)
            visited.pop()

    dist = abs(x-r) + abs(y-c)
    if dist <= k and (k-dist)%2 == 0:
        dfs(x, y, 0)
    return res

print(solution(3, 4, 2, 3, 3, 1, 5))

#https://dingdingcrong.tistory.com/163