import itertools
def solution(numbers):
    answer = 0
    pieces = []
    for number in numbers:
        pieces.append(number)
    
    p = []
    for i in range(1, len(numbers)+1):
        p += map(list,itertools.permutations(pieces, i))
    print(p)
    
    joined = []
    for item in p:
        joined.append(int(''.join(item)))
    print(joined)
    joined = list(set(joined))
    print(joined)
    
    for num in joined:
        isPrime = True
        if num < 2:
            continue
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                isPrime = False
                break
        if isPrime:
            print(num)
            answer += 1

    return answer

print(solution("011"))