'''
20. Valid Parentheses
'''

input = '()[]'

table = {
    ')':'(',
    ']':'['
}

def isValid(input):
    stack = []
    for char in input:
        if char not in table:
            print('first')
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            print('second')
            return False
        print('stack->', stack)
    return len(stack) == 0

print(isValid(input))