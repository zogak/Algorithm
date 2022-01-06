'''
4949. 균형잡힌 세상
'''
table = {
    ')' : '(',
    ']' : '['
}

def isBalanced(sentence):
    stack = list()
    for char in sentence:
        if char == '(' or char == '[':
            stack.append(char)
        if char == ')' or char == ']':
            if not stack or table[char] != stack.pop():
                return False
    return len(stack) == 0

while True:
    sentence = input()
    if sentence == '.':
        break

    if isBalanced(sentence):
        print('yes')
    else:
        print('no')