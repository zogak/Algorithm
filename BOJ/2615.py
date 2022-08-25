graph = list(map(int, input().split()) for _ in range(19))

diagonal_dx = [-1,-1,1,1]
diagonal_dy = [-1,1,1,-1]
dx = [-1,0,1,0]
dy = [0,1,0,-1]

for i in range(19):
    for j in range(19):
        isBlack = False
        isWhite = False
        if graph[i][j] == 1:
            if not isBlack:
                startPos = (i,j)
                isBlack = True
                


