a = input()
b = input()
a_len = len(a)
b_len = len(b)

dp = [[""]*(b_len+1) for _ in range(a_len+1)]
res = []
for i in range(1,a_len+1):
    for j in range(1,b_len+1):
        if a[i-1]==b[j-1]:
            dp[i][j] = dp[i-1][j-1]+a[i-1]
        else:
            #dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            if len(dp[i-1][j]) >= len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

res = dp[-1][-1]
print(len(res))
print(res)