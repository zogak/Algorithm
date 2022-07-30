from itertools import combinations

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

combi = list(combinations(numbers, m))

for item in combi:
    for i in item:
        print(i, end= ' ')
    print()