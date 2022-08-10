n = int(input())
input_list = list(int(input()) for _ in range(n))
dp = [1]*n

for i in range(len(input_list)):
    for j in range(i):
        if input_list[j] < input_list[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))