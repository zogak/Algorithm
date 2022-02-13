def solution(m, n, board):
    answer = 0
    newBoard = []
    for row in board:
        newBoard.append(list(row))
    
    while True:
        print('round')
        check = []
        for i in range(m-1):
            for j in range(n-1):
                if newBoard[i][j] == '-':
                    continue
                if newBoard[i][j]==newBoard[i][j+1] == newBoard[i+1][j] == newBoard[i+1][j+1]:
                    check.append((i,j))
                    check.append((i,j+1))
                    check.append((i+1,j))
                    check.append((i+1,j+1))
        
        check = set(check)
        print('check:' ,check)

        if len(check) == 0:
            break
        
        answer += len(check)
        for c in check:
            newBoard[c[0]][c[1]] = '-'
        
        columnsToBeMoved = set([c[1] for c in check])
        #print('hey',columnsToBeMoved)
        
        for column in columnsToBeMoved:
            for j in range(1, m):
                #if newBoard[j+1][column] == '-':
                #    newBoard[j+1][column] = newBoard[j][column]
                #    newBoard[j][column] = '-'
                if newBoard[j][column] == '-':
                    for e in range(j, 0, -1):
                        newBoard[e][column] = newBoard[e-1][column]
                    newBoard[0][column] = '-'
        print(newBoard)
    return answer
m = 5
n = 3
board = ["ACF", "ADA", "BBC", "BBE", "AEB"]
print(solution(m,n,board))