# n개의 화살을 몇 번 과녁에 맞출지 뽑기
# 즉, 과녁의 숫자인 0-11 중에서 n개를 뽑으면 된다
# 같은 번호의 과녁에 여러 번 맞출 수 있기 때문에 중복 조합

from itertools import combinations_with_replacement

def solution(n, info):
    answer = [-1]
    max_gap = -1
    combi = combinations_with_replacement(range(11), n)

    for com in combi:
        info2 = [0]*11

        for c in com:
            info2[10-c] += 1
        
        apeach, lion = 0,0
        for i in range(11):
            if info[i] == info2[i] == 0:
                continue
            if info[i] >= info2[i]:
                apeach += 10-i
            else:
                lion += 10-i
    
        if lion > apeach:
            gap = lion - apeach
            if gap > max_gap:
                max_gap = gap
                answer = info2

    return answer