from itertools import combinations
from collections import deque

n, m = map(int, input().split())
graph = {i:[] for i in range(1,n+1)}

def getDist(a,b):
    dist = 0
    visited = [0]*(n+1)
    q = deque()
    q.append(a)
    visited[a] = 1

    while q:
        length = len(q)
        for _ in range(length):
            node = q.popleft()
            if node == b:
                break
            for item in graph[node]:
                if visited[item] == 0:
                    q.append(item)
                    visited[item] = 1
        dist += 1
    return dist

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
   
nominee = []

combi = combinations([i for i in range(1,n+1)], 2)
for com in combi:
    chicken1, chicken2 = com[0], com[1]
    dist = [0]*(n+1)
    total = 0

    #치킨 집으로부터의 거리 구하기
    for key in graph.keys():
        if key == chicken1 or key == chicken2:
            dist[key] = 0
            continue
        
        dist[key] = min(getDist(key, chicken1), getDist(key, chicken2))

    total = sum(dist)*2
    nominee.append((chicken1, chicken2, total))
    
nominee.sort(key = lambda x : (x[2], x[0], x[1]))

for item in nominee[0]:
    print(item, end = ' ')