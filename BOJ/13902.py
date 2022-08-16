from itertools import combinations

n, m = map(int, input().split())
size = list(map(int, input().split()))

#index : 그릇 수, value : 요리 횟수
dp = [1e9]*(2*n+1)

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
    curr = i
    if dp[i] == 1:
        continue
    #i를 몇 개로 쪼갤 것인지
    
    
    if dp[i] == 1e9:
        dp[i] = -1
print(dp[n])