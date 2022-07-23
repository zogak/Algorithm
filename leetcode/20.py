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


class Solution:
    def isValid(self, s: str) -> bool:
        info = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        
        stack = []
        #info의 키이면 넣고 아니면 빼서 비교
        for item in s:
            if info.get(item) is not None: #왼쪽 괄호
                stack.append(item)
            else: #오른쪽 괄호
                if not stack:#오른쪽이 더 많음
                    return False
                
                else:
                    tmp = stack.pop()
                    if info[tmp] != item:
                        return False
        return len(stack)==0 #0이면 정상 아니면 왼쪽이 많음
                    
        # (){ 왼쪽이 많은 경우 -> 절대 비지 않고 뭔가 남아 있음
        # []] 오른쪽이 많은 경우 -> empty인데 빼야함
        # ({]) 짝이 안맞는 경우