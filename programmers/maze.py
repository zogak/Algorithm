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

    def dfs(i, j, cnt, direction, visited):
        nonlocal res, flag
        if flag : return
        #k안으로 어차피 못갈 바에 return
        if abs(r-i)+abs(c-j)+cnt > k: return

        #도착했으면 flag로 막아주기
        if cnt == k and i == r and j == c:
            res = visited
            flag = True

        for i in range(4):
            di = i + dx[i]
            dj = j + dy[j]

            if di <=0 or dj <=0 or di>n or dj>m: continue
            visited += direction
            dfs(di, dj, cnt+1, info[i], visited)
            visited = visited[:-1]

        
    dfs(x, y, 0, "", "")
    return res

print(solution(3, 4, 2, 3, 3, 1, 5))

#https://dingdingcrong.tistory.com/163