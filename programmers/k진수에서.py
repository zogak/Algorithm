def solution(n, k):

    def isPrime(n):
        if n==1 : return False
        for i in range(2, int(n**0.5)+1):
            if n%i==0:
                return False
        return True
    
    #1. n을 k 진수로 바꾸기
    def convert(n, k):
        stack = []
        while n > 0:
            stack.append(n%k)
            n = n//k
    
        stack.reverse()
        return ''.join(map(str,stack))
    
    num = convert(n, k)
    
    #2. 조건에 맞는 수 찾기
    nominees = num.split('0')

    res = 0
    for nominee in nominees:
        if nominee == '': continue
        if isPrime(int(nominee)):
            res += 1
    
    return res

print(solution(883438, 3))