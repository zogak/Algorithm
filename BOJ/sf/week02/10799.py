bars = input()
stack = []
answer = 0
for i in range(len(bars)):
    if bars[i] == "(":
        stack.append(bars[i])

    elif bars[i] == ")":
        if bars[i-1] == "(":
            stack.pop()
            answer += len(stack)
        else:
            stack.pop()
            answer += 1

print(answer)