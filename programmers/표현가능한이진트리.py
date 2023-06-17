def solution(numbers):
    def convertToBinary(decimalNumber):
        binaryNumber = bin(decimalNumber)[2:]
        length = len(binaryNumber)
        h = 0
        while 2**h-1 < length:
            h += 1
        
        zeroNeeded = h-length
        binaryNumber = '0'*zeroNeeded + binaryNumber

        return binaryNumber

    def dfs(subtree, depth):
        if depth == 0 and len(subtree) == 1:
            return True
        l, r = 0, len(subtree)-1
        if l == r : #리프노드
            if subtree[l] == '0': return True
            return False
        
        root = (l+r)//2
        if subtree[root] == '0':
            print(subtree[:root], subtree[root+1:])
            if dfs(subtree[:root], depth+1) and dfs(subtree[root+1:], depth+1):
                return True
            return False
        
        return True
    
    answer = []
    for number in numbers:
        #1. 이진수로 변환 및 자리수 맞추기
        #2. 가능한 이진트리인지 확인
        binaryNumber = convertToBinary(number)
        print(binaryNumber)
        if dfs(binaryNumber, 0):
            answer.append(1)
        else:
            answer.append(0)

    return answer


print(solution([63, 111, 95]))