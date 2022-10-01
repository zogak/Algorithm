import sys
input = sys.stdin.readline
N = int(input())
dx = [0,-1,0,1]
dy = [1,0,-1,0]
graph = [[0]*101 for _ in range(101)]

for _ in range(N):
    y,x,d,g = map(int, input().split())
    graph[x][y] = 1

    curve = [d]
    temp = [d]

    for gen in range(g+1):
        for t in temp:
            x += dx[t]
            y += dy[t]
            graph[x][y] = 1
        
        temp = [(c+1)%4 for c in curve]
        temp.reverse()
        curve += temp

cnt = 0
for i in range(100):
    for j in range(100):
        if graph[i][j]==1 and graph[i+1][j]==1 and graph[i+1][j+1]==1 and graph[i][j+1]==1:
            cnt += 1

print(cnt)