n = int(input())
m = int(input())
vips = []
for _ in range(m):
    vips.append(int(input()))

dp = [0]*41
dp[0] = 1
dp[1] = 1
dp[2] = 2
for i in range(3, 41):
    dp[i] = dp[i-2] + dp[i-1]

if vips:
    res = 1
    temp = [0] + vips + [n+1]

    for i in range(len(temp)-1):
        num = (temp[i+1] - temp[i] - 1)
        res *= dp[num]

else:
    res = dp[n]
print(res)