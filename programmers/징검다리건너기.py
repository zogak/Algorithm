def solution(stones, k):
    answer = 0
    while True:
        cluster = False
        for i, stone in enumerate(stones):
            if stone == 0:
                if not cluster:
                    cluster = True
                    succession = 1
                else:
                    succession += 1
                    if succession >= k:
                        return answer
                
            else:
                if cluster:
                    cluster = False
                stones[i] -= 1
        answer += 1

    #return answer

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(stones, k))