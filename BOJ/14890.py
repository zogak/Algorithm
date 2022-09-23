from collections import deque


N, L = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

def isPossible(road):
    slope = [0]*N
    for i in range(N-1):
        if road[i] == road[i+1]:
            continue

        if abs(road[i] - road[i+1]) >= 2:
            return False

        # 한 칸 작아졌을 때
        if road[i] > road[i+1]:
            temp = road[i+1]
            for j in range(i+1, i+1+L):
                if 0 <= j < N:
                    if road[j] != temp:
                        return False
                    if slope[j] == 1:
                        return False
                    slope[j] = 1
                else:
                    return False

        # 한 칸 커졌을 때
        elif road[i] < road[i+1]:
            temp = road[i]
            for j in range(i, i-L, -1):
                if 0 <= j < N:
                    if road[j] != road[i]:
                        return False
                    if slope[j] == 1:
                        return False
                    slope[j] = 1
                else:
                    return False

    return True
    
cnt = 0
for g in graph:
    if isPossible(g):
        cnt += 1

for i in range(N):
    temp = []
    for j in range(N):
        temp.append(graph[j][i])
    if isPossible(temp):
        cnt += 1

print(cnt)