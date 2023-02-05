from collections import Counter
def solution(k, tangerine):
    answer = 0
    counter = Counter(tangerine)
    items = list(counter.items())
    items.sort(key = lambda x : -x[1])
    for item in items:
        answer += 1
        k -= item[1]
        if k == 0:
            break
    return answer

print(solution(2,[1, 1, 1, 1, 2, 2, 2, 3]))