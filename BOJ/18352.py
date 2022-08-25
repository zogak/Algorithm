import sys
import heapq

input = sys.stdin.readline
n, m, k, x = map(int, input().split())
graph = {i:[] for i in range(1, n+1)}
distance = [1e9]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b,1))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for item in graph[node]:
            cost = dist + item[1]
            if cost < distance[item[0]]:
                distance[item[0]] = cost
                heapq.heappush(q, (cost, item[0]))

dijkstra(x)
flag = False
for i, d in enumerate(distance):
    if d == k:
        flag = True
        print(i)

if not flag:
    print(-1)
