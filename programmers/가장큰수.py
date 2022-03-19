import itertools
def solution1(numbers):
    answer = ''
    permutation = list(map(list, itertools.permutations(numbers, len(numbers))))
    temp = []
    for p in permutation:
        p = list(map(str, p))
        temp.append(''.join(p))
    
    answer = max(temp)
    return answer

#print(solution1([6, 10, 2]))

def solution2(numbers):
    answer = ''
    for i in range(1, len(numbers)):
        temp = numbers[i]
        j = i-1
        while (str(numbers[j])+str(temp) < str(temp) + str(numbers[j])) and j > -1:
            numbers[j+1] = numbers[j]
            numbers[j] = temp
            j -= 1
    print(numbers)
    answer = str(int(''.join(map(str, numbers))))
    return answer
print(solution2([6, 10, 2]))