## 시간초과 ##
def solution(topping):
    answer = 0
    length = len(topping)
    for i in range(1, length-1):
        chul, bro = topping[0:i], topping[i:length]
        if len(set(chul)) == len(set(bro)):
            answer += 1
    
    return answer

a = {1:2, 3:0}
print(a)
a.pop(3)
print(a)

## 정답 코드 ##
from collections import Counter
def solution(topping):
    answer = 0
    topping_counter = Counter(topping)
    topping_set = set()
    for top in topping:
        topping_counter[top] -= 1
        topping_set.add(top)
        if topping_counter[top] == 0:
            topping_counter.pop(top)
        if len(topping_counter) == len(topping_set):
            answer += 1
    
    return answer