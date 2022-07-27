from collections import deque
import sys

n, m, k, x = map(int, sys.stdin.readline().split())
graph = {i:[] for i in range(1,n+1)}
for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

visited = [-1]*(n+1)

res = []
def bfs(node):
    q = deque()
    q.append(node)
    visited[node] = 0
    dist = 0

    while q:
        length = len(q)
        for i in range(length):
            curr = q.popleft()
            for item in graph[curr]:
                if visited[item] == -1:
                    q.append(item)
                    visited[item] = dist + 1
                    if visited[item] == k:
                        res.append(item)
        dist += 1

bfs(x)
if len(res)==0:
    print(-1)
else:
    res.sort()
    for r in res:
        print(r)