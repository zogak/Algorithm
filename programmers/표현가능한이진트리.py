import sys
sys.setrecursionlimit(10**6)
def solution(numbers):
    def convertToBinary(decimalNumber):
        binaryNumber = bin(decimalNumber)[2:]
        length = len(binaryNumber)
        h = 1
        while 2**h-1 < length:
            h += 1
        
        zeroNeeded = (2**h-1)-length
        binaryNumber = '0'*zeroNeeded + binaryNumber

        return binaryNumber

    def dfs(subtree):
        l, r = 0, len(subtree)-1
        if l==r :
            return subtree[l]
        mid = (l+r)//2
        left = dfs(subtree[:mid])
        right = dfs(subtree[mid+1:])

        if subtree[mid] == '0' and (left=='1' or right=='1'):
            return False
        
        return True
    
    answer = []
    for number in numbers:
        #1. 이진수로 변환 및 자리수 맞추기
        #2. 가능한 이진트리인지 확인
        binaryNumber = convertToBinary(number)
        print(binaryNumber)
        if dfs(binaryNumber):
            answer.append(1)
        else:
            answer.append(0)

    return answer


print(solution([63, 111, 95]))
#print(solution([7, 42, 5]))