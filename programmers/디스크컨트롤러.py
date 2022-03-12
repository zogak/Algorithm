jobs = [[0,3], [1,9], [2,6]]
import collections

'''
deprecated
'''
def solution1(jobs):
    answer = 0
    # temp = []
    # for start, duration in jobs:
    #     temp.append([duration, start])
    # temp.sort()

    jobs.sort(key = lambda x : x[1])
    print(jobs)
    d = collections.deque(jobs)
    print(d)
    end = d[0][1]
    while d:
        current = d.popleft()
        end = end + current[0]
        answer += (end - current[1])

    
    answer = answer // len(jobs)
    
    return answer

print(solution1(jobs))

[[0, 3], [1, 9], [2, 6]]
def solution(jobs):
    n = len(jobs)
    
    # 소요시간을 기준으로 정렬
    jobs = sorted(jobs, key=lambda x:x[1])
    
    start = 0
    answer = 0
    
    while jobs:
        for i in range(len(jobs)): # jobs의 개수만큼
            if jobs[i][0] <= start: # 기다리고 있는애라면
                start += jobs[i][1]  # 현재까지 수행된 시간
                answer += start - jobs[i][0] # 끝난시점에서 시작시간을 빼야 해당 작업의 총 걸린시간이나옴
                jobs.pop(i)
                break
            # 해당시점에 아직 작업이 들어오지 않았으면 시간 ++
            if i ==  len(jobs) - 1:
                start += 1
                
    #print(time)  
    return answer // n