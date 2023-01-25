from itertools import combinations

def solution(weights):
    ONE = (3/2)
    TWO = 2
    THREE = (4/3)
    answer = 0
    combi = list(combinations(weights, 2))
    for c in combi:
        if c[0] == c[1]:
            answer += 1
            continue

        if c[0] < c[1]:
            small, big = c[0], c[1]
        else:
            small, big = c[1], c[0]

        if small*ONE==big or small*TWO==big or small*THREE==big:
            answer += 1
    return answer

print(solution([100,180,360,100,270]))