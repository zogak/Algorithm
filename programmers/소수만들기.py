from itertools import combinations
def solution(nums):
    res = 0
    combi = combinations(nums, 3)
    def isPrime(num):
        check = [0]*(num+1)
        for i in range(2, int(num**0.5)+1):
            if check[i] == 0:
                for j in range(i+i, num+1, i):
                    check[j] = 1
        return check[num]==0
    
    for c in combi:
        if isPrime(sum(c)):
            res += 1
    return res