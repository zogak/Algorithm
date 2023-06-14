import heapq
N, M = map(int, input().split())
check = [0]*1001 #idx:학급번호, val:해당 학급 포인터
arr = [] #각 학급별 능력치 리스트를 모두 모아둘 리스트
maxAbility = 0
q = []
for i in range(N):
    ability = list(map(int, input().split()))
    ability.sort()
    maxAbility = max(maxAbility, ability[0])

    heapq.heappush(q, [ability[0], i]) #능력치, 학급번호
    arr.append(ability)

res = int(1e9)
while q:
    minAbility, classNum = heapq.heappop(q)
    res = min(res, maxAbility - minAbility)

    idx = check[classNum]
    if idx == M-1: break #이 풀이는 학급번호를 0번부터 시작하였다.
    heapq.heappush(q, [arr[classNum][idx+1], classNum])
    maxAbility = max(maxAbility, arr[classNum][idx+1])
    check[classNum] += 1

print(res)