from collections import deque

N, L = map(int, input().split())
positions = []
for i in range(N):
    positions.append(int(input()))

def getDistAndPos(curr_pos, temp):
    res = []
    for item in temp:
        dist = abs(curr_pos - item[1])
        res.append((dist, item[1]))
    res.sort(key = lambda x : (x[0], x[1]))
    return deque(res)

#dp = [0]*(len(positions))
dp = [0]*1001

info = []
for position in positions:
    info.append((abs(L-position), position))
info.sort(key = lambda x : (x[0], x[1]))
info = deque(info)
dist, curr_pos = info.popleft()
dp[0] = dist

for i in range(1, N):
    info = getDistAndPos(curr_pos, info)
    dist, curr_pos = info.popleft()
    dp[i] = dp[i-1] + dist

print(sum(dp))
