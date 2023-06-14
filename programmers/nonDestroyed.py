# def solution(board, skill):
#     res = 0
#     for tp, r1, c1, r2, c2, degree in skill:
#         if tp == 1:
#             for i in range(r1, r2+1):
#                 for j in range(c1, c2+1):
#                     board[i][j] -= degree
#         else:
#              for i in range(r1, r2+1):
#                 for j in range(c1, c2+1):
#                     board[i][j] += degree
    

#     n = len(board)
#     m = len(board[0])
#     for i in range(n):
#         for j in range(m):
#             if board[i][j] > 0:
#                 res += 1
                
#     return res

    
def solution(board, skill):
    res = 0
    n = len(board)
    m = len(board[0])
    
    check = [[0]*(m+1) for _ in range(n+1)]
    for tp, r1, c1, r2, c2, degree in skill:
        if tp==2:
            check[r1][c1] += degree
            check[r1][c2+1] -= degree
            check[r2+1][c1] -= degree
            check[r2+1][c2+1] += degree
        else:
            check[r1][c1] -= degree
            check[r1][c2+1] += degree
            check[r2+1][c1] += degree
            check[r2+1][c2+1] -= degree          
    
    #print(check)
    for i in range(n+1):
        for j in range(m):
            check[i][j+1] += check[i][j]
    
    
    for j in range(m+1):
        for i in range(n):
            check[i+1][j] += check[i][j]

    
    for i in range(n):
        for j in range(m):
            board[i][j] += check[i][j]
            if board[i][j] > 0:
                res += 1
    
                
    return res


# board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
# skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
board = [[1,2,3],[4,5,6],[7,8,9]]
skill = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
print(solution(board, skill))


[[-2, 0, 2, 0], 
 [0, -4, 0, 4], 
 [102, -100, -2, 0],
 [-100, 104, 0, -4]]

[[-2, -2, 0, 0], 
 [0, -4, -4, 0], 
 [102, 2, 0, 0], 
 [-100, 4, 4, 0]]

[[-2, -2, 0, 0], 
 [-2, -6, -4, 0], 
 [100, -4, -4, 0], 
 [0, 0, 0, 0]]