n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

# dx = [0,1]
# dy = [1,0]

for i in range(n):
    for j in range(n):
        # if i==n-1 and j==n-1:
        #     break

        jump = graph[i][j]
        
        east = [i, j+jump]
        south = [i+jump, j]

        if 0<= east[1] <n:
            dp[east[0]][east[1]] += dp[i][j]
        
        if 0<= south[0] <n:
            dp[south[0]][south[1]] += dp[i][j]

        # for k in range(2):
        #     nx = i + dx[k]*jump
        #     ny = j + dy[k]*jump
            
        #     if nx<0 or ny<0 or nx>=n or ny>=n:
        #         continue
        
        #     dp[nx][ny] = dp[nx][ny] + 1
        print(dp)

print(dp[n-1][n-1])