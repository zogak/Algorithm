C, N = map(int, input().split())
graph = list(tuple(map(int, input().split())) for _ in range(N))

dp = [1e9]*(C+100)
dp[0] = 0

# #채울 수 있는 dp 채우기
# for money, people in graph:
#     dp[people] = money

#     if people != 1:
#         for i in range(1, C//people+1):
#             dp[people*i] = min(money*i, dp[people*i])

# for i in range(1, C+1):
#     dp[i] = min(dp[i-1]+1, dp[i])

# print(dp[C]

for money, people in graph:
    for i in range(people, C+100):
        dp[i] = min(dp[i], dp[i-people]+money)

print(min(dp[C:]))

    