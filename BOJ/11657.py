import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
edge = []

for _ in range(m):
    a, b, cost = map(int, input().split())
    edge.append((a, b, cost))

distance = [INF]*(n+1)

def bellman_ford(start):
    distance[start] = 0
    for i in range(n):
        for j in range(m):
            cur, next, cost = edge[j][0], edge[j][1], edge[j][2]
            if distance[cur] != INF and distance[next] > distance[cur] + cost:
                distance[next] = distance[cur] + cost
                if i == n-1:
                    return True
    
    return False

negative_cycle = bellman_ford(1)

if negative_cycle:
    print("-1")
else:
    for i in range(2, n+1):
        if distance[i] == INF:
            print("-1")
        else:
            print(distance[i])
    