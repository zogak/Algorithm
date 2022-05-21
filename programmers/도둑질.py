def solution(money):
    n = len(money)
    dp = [0]*n
    
    dp[0] = money[0]
    for i in range(1,n-1):
        dp[i] = max(dp[i-1], dp[i-2]+money[i])
    
    last = [0]*n
    last[1] = money[1]
    for i in range(2, n):
        last[i] = max(last[i-1], last[i-2]+money[i])
    
    return max(max(dp), max(last))