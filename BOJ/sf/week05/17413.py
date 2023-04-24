sentence = input()
stack = []
res = ''
flag = False

for s in sentence:
    if s == '<':
        flag = True
        if stack:
            while stack:
                res += stack.pop()
        res += s

    elif s == '>':
        flag = False
        res += s    
    
    elif s == ' ':
        if stack:
            while stack:
                res += stack.pop()
        res += ' '
    
    else:
        if flag:
            res += s
        else:
            stack.append(s)

if stack:
    while stack:
        res += stack.pop()

print(res)