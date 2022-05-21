triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

def solution(triangle):
    answer = 0
    length = len(triangle)

    #1
    '''
    dp = []
    for i in range(1, length+1):
        temp = [0]*i
        dp.append(temp)
    '''
    dp = [[0]*length for _ in range(length)]

    #2
    dp[0][0] = triangle[0][0]

    #3
    for i in range(length-1):
        for j in range(i+1):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j]+triangle[i+1][j])
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+triangle[i+1][j+1])
    
    return max(dp[-1])

print(solution(triangle))