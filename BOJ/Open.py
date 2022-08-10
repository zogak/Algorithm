from itertools import combinations

n, m = map(int, input().split())
size = list(map(int, input().split()))

dp = [1e9]*(n+1)

#제일 작은 사이즈의 웍보다 작은 짜장면은 만들 수 없음
min_wok = min(size)
for i in range(min_wok):
    dp[i] = -1

#1개 사용
for s in size:
    dp[s] = 1

#2개 사용
combi = list(combinations(size,2))
for com in combi:
    wok_size = sum(com)
    dp[wok_size] = min(dp[wok_size], 1)


for i in range(min_wok, n+1): #dp를 채울건데
    #i를 쪼개서
    for p in range(int(i//2)+1):
        if dp[p] == -1:
            continue
        a, b = p, i-p
        if dp[a]==-1 or dp[b]==-1:
            continue
        dp[i] = min(dp[i], dp[a]+dp[b])

print(dp[-1])