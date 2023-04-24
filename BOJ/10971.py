N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

def dfs(start, node, cost, cnt):
    global visited, res
    visited[node] = 1
    cnt += 1

    if cnt == N-1:
        cost += board[node][start]
        if cost < res:
            res = cost
        return
    
    tmp = int(1e9)
    for i in range(N):
        if i==node : continue
        if visited[i] : continue

        if board[node][i] < tmp :
            nextIdx = i
            tmp = board[node][i]

    dfs(start, i, cost+tmp, cnt+1)
    return

res = int(1e9)
for i in range(N):
    visited = [0]*N
    dfs(i,i,0,0)
    print(res)

print(res)
    