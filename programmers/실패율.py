from collections import Counter
def solution(N, stages):
    players = len(stages)
    status = Counter(stages)
    failRate = []
    for i in range(1, N+1):
        if status.get(i) is not None:
            player = status.get(i)
            failRate.append((player/players, i))
            players -= player
        else:
            failRate.append((0, i))
    
    print(failRate)
    #앞은 내림차순, 뒤는 오름차순 정렬하는 방법?
    failRate.sort(key = lambda x : x[0], reverse=True)
    print(failRate)
    ans = []
    for num in failRate:
        ans.append(num[1])
        
    return ans
    
print(solution(5, [2,1,2,6,2,4,3,3]))