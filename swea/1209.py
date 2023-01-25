'''
Sum
'''

t = int(input())
for _ in range(t):
    test = int(input())
    graph = [list(map(int, input().split())) for _ in range(100)]

    # maxRow = 0
    # for row in graph:
    #     s = sum(row)
    #     if s > maxRow:
    #         maxRow = s
    
    # maxCol = 0
    # newGraph = list(map(list, zip(*graph)))
    # for col in graph:
    #     s = sum(col)
    #     if s > maxCol:
    #         maxCol = s

    # maxDiagonal = 0
    # left, right = 0, 0
    # for i in range(0, 100):
    #     left += graph[i][i]
    #     right += graph[99-i][i]
    # maxDiagonal = max(left, right)

    # ans = max(maxRow, maxCol, maxDiagonal)

    maxRow = 0
    for i in range(100):
        s = 0
        for j in range(100):
            s += graph[i][j]
        if s > maxRow:
            maxRow = s

    maxCol = 0
    for i in range(100):
        s = 0
        for j in range(100):
            s += graph[j][i]
        if s > maxCol:
            maxCol = s

    maxDiagonal = 0
    left, right = 0, 0
    for i in range(0, 100):
        left += graph[i][i]
        right += graph[99-i][i]
    maxDiagonal = max(left, right)

    ans = max(maxRow, maxCol, maxDiagonal)

    print('#{} {}'.format(test, ans))
