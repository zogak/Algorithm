scoville = [1, 2, 3, 9, 10, 12]
K = 7
import collections
import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    # 제일 작은 값이 K이상이면 모든 값이 K이상인 것이므로
    while scoville[0] < K :
        # 최초 scoville의 길이는 2이상이므로 0이 되는 경우는 없음
        if len(scoville) == 1:
            return -1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new = first + second*2
        heapq.heappush(scoville, new)
        answer += 1
        
    return answer

'''
deprecated, not correct
'''
def solution1(scoville, K):
    answer = 0
    
    scoville = collections.deque(scoville)
    # scoville의 길이가 애초에 2 이상이므로 체크할 필요가 없음.
    # if len(scoville) == 1:
    #     if scoville[0] < K:
    #         return -1
    # if len(scoville) == 0 and K != 0:
    #     return -1
    while len(scoville) >= 2:
        # 모두 k 이상인 경우 break
        if all(s >= K for s in scoville):
            print('all above')
            break
        #전체 소트 넣기
        answer += 1
        cook = []
        cook.append(scoville.popleft())
        cook.append(scoville.popleft())
        cook.sort()
        #cook에 있는 2개만 sort해줄게 아니라, 전체 소트를 해주어야 함.
        new = cook[0] + cook[1] * 2
        scoville.appendleft(new)
        print(scoville)

        if len(scoville) == 1 and scoville[0] < K:
            return -1
        
    return answer

print(solution1(scoville, K))

