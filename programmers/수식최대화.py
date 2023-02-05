from itertools import permutations
from collections import deque

def solution(expression):

    def calculate(operand, num1, num2):
        res = 0
        if operand == '+':
            res = num1+num2
        elif operand == '-':
            res = num1-num2
        elif operand == '*':
            res = num1*num2
        elif operand == '/':
            res = num1/num2
        return res

    #숫자와 기호를 분리, 전체를 리스트로 만들기
    nums, operands= [],[]
    whole = deque()
    
    temp = ''
    for char in expression:
        if char.isnumeric():
            temp += char
        else:
            nums.append(int(temp))
            whole.append(int(temp))
            operands.append(char)
            whole.append(char)
            temp = ''
    nums.append(int(temp))
    whole.append(int(temp))
    print('num', nums)
    print('operands', operands)
    print('whole', whole)
            
    #기호 우선순위 후보들
    operands_set = list(set(operands))
    permu = permutations(operands_set, len(operands_set))

    answer = -1e9
    for per in permu:
        stack = []
        for item in per:
            print('item', item)
            while whole:
                curr = whole.popleft()
                if curr == item:
                    stack.append(calculate(item, stack.pop(), whole.popleft()))
                    print(stack)
                else:
                    stack.append(curr)
                    print(stack)
            print(stack)
            print(whole)

            if len(stack)==1:
                answer = max(answer, stack[0])
                print('answer', answer)
            

    return answer

print(solution("50*6-3*2"))