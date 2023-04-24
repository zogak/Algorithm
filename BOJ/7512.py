import heapq
def getPrimes():
    check = [True] * 10000001
    for i in range(2, int(10000001**0.5)):
        if check[i]:
            for j in range(i+i, 10000001, i):
                check[j] = False
    
    primes = []
    for i in range(2, 10000001):
        if check[i]:
            primes.append(i)
    
    return check, primes

def slidingWindow(sumOfPart, start, end):
    i = start
    for j in range(end+1, 10000001):
        sumOfPart += primes[j]
        sumOfPart -= primes[i]
        i += 1

        if primeTable[sumOfPart]:
            return [sumOfPart, i, j]

primeTable, primes = getPrimes()
T = int(input())
for tc in range(1, T+1):
    res = 0
    m = int(input())
    nums = list(map(int, input().split()))

    ###
    q = []
    for n in nums:
        i, j = 0, n-1
        sumOfSection = sum(primes[i:j+1])
        if primeTable[sumOfSection]:
            heapq.heappush(q, [sumOfSection, i, j])
        else:
            heapq.heappush(q, slidingWindow(sumOfSection, i, j))
    

    while len(set(list(map(list, zip(*q)))[0])) != 1:
        sumOfSection, start, end = heapq.heappop(q)
        heapq.heappush(q, slidingWindow(sumOfSection, start, end))

    res = q[0][0]
    ###
    
    print(f'Scenario {tc}:')
    print(res)
    print()