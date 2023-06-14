N = int(input())
#소수 리스트 만들기
def getPrimes():
    n = 4000001
    check = [True]*n
    for i in range(2, int(n**0.5)):
        if check[i]:
            for j in range(i+i, n, i):
                check[j] = False

    primes = []
    for i in range(2, n):
        if check[i]:
            primes.append(i)

    return primes

primes = getPrimes()

if N == 1:
    res = 0

else:
    #투 포인터
    j = 0
    sum_ = 0
    res = 0
    
    for i in range(len(primes)):
        while sum_ < N and j < len(primes):
            sum_ += primes[j]
            j += 1
        
        if sum_ == N:
            res += 1

        sum_ -= primes[i]

print(res)