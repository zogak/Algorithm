'''
#메모리초과
from itertools import combinations
N = int(input())
firstLine = [i for i in range(1, N+1)]
secondLine = [0] + list(int(input()) for _ in range(N))

for i in range(N, 0, -1):
    combinationList = list(combinations(firstLine, i))
    for combination in combinationList:
        setForSecondLine = set()
        for num in combination:
            setForSecondLine.add(secondLine[num])
        if set(combination) == setForSecondLine:
            cnt = len(combination)
            res = list(combination)
            print(cnt)
            for item in res:
                print(item)
            exit(0)

'''
import sys
sys.setrecursionlimit(10**6)
N = int(input())
firstLine = [i for i in range(N+1)]
secondLine = [0] + list(int(input()) for _ in range(N))

def combination(idx, cnt):
    global visited, temp, setForSecondLine
    if cnt == r:
        for item in temp:
            setForSecondLine.add(secondLine[item])
        
        if set(temp) == setForSecondLine:
            print(r)
            for t in temp:
                print(t)
            exit(0)
    else:
        for i in range(idx, N+1):
            if visited[i] : continue
            temp[cnt] = firstLine[i]
            visited[i] = 1
            combination(i, cnt+1)
            visited[i] = 0

for r in range(N, 0, -1):
    temp = [0]*r
    visited = [0]*(N+1)
    setForSecondLine = set()
    combination(1,0)