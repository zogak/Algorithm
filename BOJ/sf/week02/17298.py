n = int(input())
numbers = list(map(int, input().split()))
stack = []
res = [-1]*n

for i, number in enumerate(numbers):
    while stack and stack[-1][1] < number:
        res[stack.pop()[0]] = number

    stack.append((i, number))

print(*res)