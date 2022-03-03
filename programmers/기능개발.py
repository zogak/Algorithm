progresses = [93, 30, 55]
speeds = [1, 30, 5]

import collections
def solution(progresses, speeds):
    answer = []
    days = collections.deque()
    for i, progress in enumerate(progresses):
        progressLeft = 100 - progress
        if progressLeft % speeds[i] == 0:
            days.append(progressLeft // speeds[i])
        else:
            days.append(progressLeft // speeds[i] + 1)
    
    current = days.popleft()
    cnt = 1
    
    # while days:
    #     if current >= days[0]:
    #         current = days.popleft()
    #         cnt += 1
    #     else:
    #         answer.append(cnt)
    #         cnt = 1
    #         current = days.popleft()
    # answer.append(cnt)
    # return answer

print(solution(progresses, speeds))