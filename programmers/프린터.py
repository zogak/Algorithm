priorities = [1, 1, 9, 1, 1, 1]
location = 0
import collections
def solution(priorities, location):
    answer = 0
    d = collections.deque()
    # 1. idx 와 priorities를 deque로 만들기
    for i, p in enumerate(priorities):
        d.append([p, i])
    
    while d:
        val = d.popleft()
        # priority 큰 값이 있는 경우
        if d and val[0] < max(d)[0]:
            # 맨 뒤로 이동
            d.append(val)
        
        # 프린트할 경우(priority 제일 큼)이거나, val이 d의 마지막 값인 경우
        else:
            answer += 1
            if val[1] == location:
                break
    
    return answer

print(solution(priorities, location))