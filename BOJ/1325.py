from collections import deque
N, M = map(int, input().split())
board = {i:[] for i in range(1, N+1)}
for _ in range(M):
    b, a = map(int, input().split())
    board[a].append(b)

res = []
maxCnt = -1

def bfs(i):
    global res, maxCnt    
    q = deque()
    visited = [0]*(N+1)
    q.append(i)
    visited[i] = 1
    cnt = 0

    while q:
        x = q.popleft()
        cnt += 1

        for item in board[x]:
            if visited[item] == 1: continue

            q.append(item)
            visited[item] = 1
    
    if cnt >= maxCnt:
        res.append(i)
        maxCnt = cnt

for i in range(1, N+1):
    bfs(i)

print(*res)