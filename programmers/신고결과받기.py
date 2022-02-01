id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reportHistory = dict()
    for id in id_list:
        reportHistory[id] = list()
    reportedNum = [0] * len(id_list)
    
    for item in report:
        accuser, accused = item.split()
        if accused in reportHistory[accuser]:
            continue
        reportHistory[accuser].append(accused)
        reportedNum[id_list.index(accused)] += 1
    
    stopped = list()
    for i, num in enumerate(reportedNum):
        if num >= k:
            stopped.append(id_list[i])
    
    for stop in stopped:
        for key in reportHistory:
            if stop in reportHistory[key]:
                answer[id_list.index(key)] += 1
    
    return answer

ans = solution(id_list, report, k)
print(ans)