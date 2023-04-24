n = int(input())
m = int(input())

distance = [[int(1e9)]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, cost = map(int, input().split())
    distance[a][b] = min(distance[a][b], cost)

for i in range(1, n+1):
    distance[i][i] = 0

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            distance[i][j] = min(distance[i][k]+distance[k][j], distance[i][j])

for i in range(1, n+1):
    print(*distance[i][1:])