jobs = [[0,3], [1,9], [2,6]]
import collections



'''
deprecated
'''
def solution1(jobs):
    answer = 0
    temp = []
    for start, duration in jobs:
        temp.append([duration, start])
    temp.sort()
    d = collections.deque(temp)
    print(d)
    end = d[0][1]
    while d:
        current = d.popleft()
        end = end + current[0]
        answer += (end - current[1])
    
    answer = answer // len(jobs)
    
    return answer

print(solution1(jobs))