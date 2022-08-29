import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[int(1e9)]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n+1): #k-경유할 노드
    graph[k][k] = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

# 두 개의 치킨 집 i, j
res = []
for i in range(1, n):
    for j in range(i+1, n+1):
        total = 0
        for house in range(1,n+1):
            total += min(graph[house][i], graph[house][j])*2
        res.append((i, j, total))

res.sort(key=lambda x : (x[2], x[0], x[1]))

for item in res[0]:
    print(item, end =' ')