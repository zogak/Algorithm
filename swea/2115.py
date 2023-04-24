from itertools import combinations, combinations_with_replacement
t = int(input())
def getHoney(tong):
    # ret = 0
    # for i in range(1<<M):
    #     tmp = []
    #     tmpRet = 0
    #     for j in range(M):
    #         if i & (1<<j):
    #             tmp.append(tong[j])
    #     if sum(tmp) <= C:
    #         for item in tmp:
    #             tmpRet += (item*item)
    #         if tmpRet > ret:
    #             ret = tmpRet
    # return ret
    ret = 0
    for i in range(1, len(tong)+1):
        combi = list(combinations(tong, i))
        for com in combi:
            tmpRet = 0
            if sum(com) > C: continue
            for item in com:
                tmpRet += (item*item)
            if tmpRet > ret:
                ret = tmpRet
    return ret
for test_case in range(1, t+1):
    res = 0
    N,M,C = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    #벌통 선택
    if N >= M*2:
        rowCombination = list(combinations_with_replacement([i for i in range(N)], 2))
    else:
        rowCombination = list(combinations([i for i in range(N)], 2))

    for row1, row2 in rowCombination:
        if row1 == row2:
            colStartIndexNominees = [i for i in range(0, N, M)]
        elif row1 != row2:
            colStartIndexNominees = [i for i in range(0, N-M+1)]

        if len(colStartIndexNominees) == 1:
            colCombination = [(colStartIndexNominees+colStartIndexNominees)]
        else: colCombination = list(combinations(colStartIndexNominees, 2))

        for col1, col2 in colCombination:
            honey1 = board[row1][col1 : col1+M]
            honey2 = board[row2][col2 : col2+M]

            # honey1.sort(reverse=True)
            # honey2.sort(reverse=True)

            # print(honey1, honey2)
            # tmpRes = 0
            # honey1Limit, honey2Limit = 0,0
            # for honey in honey1:
            #     honey1Limit += honey
            #     if honey1Limit <= C:
            #         tmpRes += honey*honey
            # for honey in honey2:
            #     honey2Limit += honey
            #     if honey2Limit <= C:
            #         tmpRes += honey*honey

            tmpRes = 0
            tmpRes += getHoney(honey1)
            tmpRes += getHoney(honey2)
            
            if res < tmpRes:
                print(honey1, honey2)
                res = tmpRes


    print(f'#{test_case} {res}')

'''
1
3 3 10
7 2 9
6 6 6
5 5 7
'''

'''
1
8 3 12
9 1 6 7 5 4 6 7
9 5 1 8 8 3 5 8
5 2 6 8 6 9 2 1
9 2 1 8 7 5 2 3
6 5 5 1 4 5 7 2
1 7 1 8 1 9 5 5
6 2 2 9 2 5 1 4
7 1 1 2 5 9 5 7
'''