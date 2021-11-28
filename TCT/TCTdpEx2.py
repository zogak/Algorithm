n = int(input())
food = list(map(int, input().split()))

dp = [0] * 100

dp[0] = food[0]
dp[1] = max(dp[0], food[1])

for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2]+food[i])

print(dp[n-1])