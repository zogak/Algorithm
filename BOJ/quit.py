n = int(input())
dp = [0]*(n+2)
graph = [list(map(int, input().split())) for _ in range(n)]
graph = [[0,0]] + graph

for i in range(n, 0, -1):
    t, p = graph[i][0], graph[i][1]
    if i + t > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[i+t] + p)

print(dp)