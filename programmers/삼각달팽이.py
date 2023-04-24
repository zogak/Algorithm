def solution(n):
    graph = [[0]*i for i in range(1, n+1)]
    
    dx = [-1,1,0]
    dy = [-1,0,1]
    dir = 1
    x,y = -1,0
    num = 0
    for i in range(n, 0, -1):
        for j in range(i):
            x += dx[dir]
            y += dy[dir]
            num += 1
            graph[x][y] = num
            
        dir = (dir+1)%3
    
    res = []
    for row in graph:
        for item in row:
            res.append(item)
    
    print(res)

solution(4)