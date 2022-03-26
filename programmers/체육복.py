n = 5
lost = [2, 4]
reserve = [1, 3, 5]

def solution(n, lost, reserve):
    answer = 0
    uniform = [1]*n
    for idx in lost:
        uniform[idx-1] -= 1
    for idx in reserve:
        uniform[idx-1] += 1
    
    print(uniform)
    for i, num in enumerate(uniform):
        if num==2:
            if (i-1) >=0 and uniform[i-1] == 0:
                uniform[i-1] += 1
                uniform[i] -= 1
            elif (i+1) < n and uniform[i+1] == 0:
                uniform[i+1] += 1
                uniform[i] -= 1

    print(uniform)
    for num in uniform:
        if num > 0:
            answer += 1
    return answer

print(solution(n, lost, reserve))