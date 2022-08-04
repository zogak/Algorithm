import sys
from itertools import permutations
n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split())) #map하고 []로 그냥 씌우지 말것!!!!!!!
operations = list(map(int, sys.stdin.readline().split()))

res = []

PLUS, MINUS, MULTIPLY, DIVISION = 0,1,2,3

#풀어헤치기
operation_series = []
for i, value in enumerate(operations):
    operation_series += [i]*value


permu = list(permutations(operation_series, n-1))

for per in permu:
    tmp = numbers[0]
    for i in range(n-1):
        if per[i] == PLUS:
            tmp += numbers[i+1]
        elif per[i] == MINUS:
            tmp -= numbers[i+1]
        elif per[i] == MULTIPLY:
            tmp *= numbers[i+1]
        elif per[i] == DIVISION:
            if tmp < 0:
                tmp = -((-tmp)//numbers[i+1])
            else:
                tmp = tmp//numbers[i+1]
    res.append(tmp)

print(max(res))
print(min(res))
