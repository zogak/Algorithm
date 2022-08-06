from itertools import combinations
def solution(expression):

    def calculate(operand, num1, num2):
        if operand == '+':
            res = num1+num2
        elif operand == '-':
            res = num1-num2
        elif operand == '*':
            res = num1*num2
        elif operand == '/':
            res = num1/num2
        return res

    #숫자와 기호를 분리
    nums, operands = [],[]
    
    temp = ''
    for char in expression:
        if char.isnumeric():
            print(char)
            temp += char
        else:
            nums.append(int(temp))
            operands.append(char)
            temp = ''
            
    #기호 우선순위 후보들
    operands_set = list(set(operands))
    combi = combinations(operands_set, len(operands_set))

    answer = -1e9
    for com in combi:
        for item in com:
            operands_tmp = operands
            nums_tmp = nums
            for i, op in enumerate(operands_tmp):
                if op == item:
                    op_idx = i*2+1
                    new_num = calculate(op, nums_tmp[op_idx-1], nums_tmp[op_idx+1])
                    
                    # nums_tmp.insert(op_idx+2, new_num)
                    # nums_tmp.pop(op_idx-1)
                    # nums_tmp.pop(op_idx+1)
                    # operands.pop(op_idx)
        answer = max(answer, abs(operands[0]))
    return answer

print(solution("50*6-3*2"))