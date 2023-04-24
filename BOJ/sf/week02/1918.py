sentence = input()
stack = []
for s in sentence:
    if s.isalpha():
        print(s, end = '')
    elif s == "(":
        stack.append(s)
    elif s == "*" or s == "/":
        while stack and stack[-1] != "(" and stack[-1] != "+" and stack[-1] != "-":
            print(stack.pop(), end='')
        stack.append(s)
    elif s == "+" or s == "-":
        while stack and stack[-1] != "(":
            print(stack.pop(), end='')
        stack.append(s)
    elif s == ")":
        while stack and stack[-1] != "(":
            print(stack.pop(), end='')
        stack.pop()

if stack:
    while stack:
        print(stack.pop(), end='')