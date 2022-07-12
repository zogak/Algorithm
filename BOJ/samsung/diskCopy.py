def Rotate(array):
    # 1. 원판을 회전시키는 함수
    x, d, k = map(int, sys.stdin.readline().split())
    
    if d == 0: # 시계 방향
        for i in range(x, n+1, x):
            array[i] = [array[i][(j-k)%m] for j in range(m)]

    else: # 반시계 방향
        for i in range(x, n+1, x):
            array[i] = [array[i][(j+k)%m] for j in range(m)]

def Find_adjacent_number(array):
    # 2. 인접한 동일한 숫자를 찾는 함수
    adjacent_same_number = []
    total = 0
    count = 0
    for i in range(1, n+1):
        for j in range(m):
            if array[i][j]:
                # 원판 내 인접한 숫자 찾기
                if array[i][j] == array[i][(j+1)%m]:
                    adjacent_same_number.append([i, (j+1)%m])
                if array[i][j] == array[i][(j-1)%m]:
                    adjacent_same_number.append([i, (j-1)%m])
                
                # 원판 간의 인접한 숫자 찾기
                if 1 <= i - 1 and array[i][j] == array[i-1][j]:
                    adjacent_same_number.append([i-1, j])
                if i + 1 <= n and array[i][j] == array[i+1][j]:
                    adjacent_same_number.append([i+1, j])
                
                total += array[i][j]
                count += 1
    
    if adjacent_same_number: # 인접한 숫자가 있다면
        for i, j in adjacent_same_number:
            array[i][j] = 0

    else: # 인접한 숫자가 없다면 평균 값으로 1을 더하거나 뺀다.
        if count:
            average = total / count
            for i in range(1, n+1):
                for j in range(m):
                    if array[i][j]:
                        if array[i][j] > average:
                            array[i][j] -= 1
                        elif array[i][j] < average:
                            array[i][j] += 1
    
import sys
n, m, t = map(int, sys.stdin.readline().split())
array = [[]]
for _ in range(n):
    array.append(list(map(int, sys.stdin.readline().split()))) # array[원판 번호][원판 내 숫자 인덱스]

for rot in range(t):
    Rotate(array)
    print('array after rotate', array)
    Find_adjacent_number(array)
    print('array after erase', array)

result = 0
for i in range(1, n+1):
    for j in range(m):
        result += array[i][j]

print(result)