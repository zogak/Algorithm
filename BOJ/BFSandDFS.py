'''
런타임 에러(key error)!!!!
e.g.
-----
5 1 2
3 4
-----

시작점에 연결된 간선이 하나도 없을 때
key error
'''
from collections import deque

n, m, v = map(int, input().split())

graph = {}
for i in range(m):
    a, b = map(int, input().split())
    if graph.get(a) is None:
        graph[a] = []
    if graph.get(b) is None:
        graph[b] = []
    graph[a].append(b)
    graph[b].append(a)

for key in graph.keys():
    graph[key].sort()

#print('graph', graph)

visited = [0]*(n+1)

def dfs(start):
    visited[start] = 1
    print(start, end=' ')
    for item in graph[start]:
        if visited[item] == 0:
            dfs(item)

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        curr = q.popleft()
        print(curr, end=' ')
        for item in graph[curr]:
            if visited[item] == 0:
                q.append(item)
                visited[item] = 1

dfs(v)

visited = [0]*(n+1)
print()

bfs(v)