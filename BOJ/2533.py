import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 입력받기
N = int(input())
graph = {i:[] for i in range(1, N+1)}
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0]*(N+1)
# dp[node][0] => 얼리어답터 아닌 경우
# dp[node][1] => 얼리어답터인 경우
dp = [[0,1] for _ in range(N+1)]

def dfs(node):
    global visited, dp
    visited[node] = 1

    for item in graph[node]:
        if not visited[item]:
            dfs(item)
            dp[node][0] += dp[item][1]
            dp[node][1] += min(dp[item][0], dp[item][1])

dfs(1)
print(min(dp[1]))

#참고 좋은 설명
#https://ddggblog.tistory.com/211
