from collections import Counter
n = int(input())
numbers = list(map(int, input().split()))
stack = []
res = [-1]*n
F = Counter(numbers)
for i, num in enumerate(numbers):
    while stack and F[stack[-1][1]] < F[num]:
        res[stack.pop()[0]] = num
    stack.append((i,num))

print(*res)