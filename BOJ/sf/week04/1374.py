# 시간초과
from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
roomInfo = [list(map(int, input().split())) for _ in range(n)]
check = [0]*(n+1)

roomInfo.sort(key = lambda x : (x[2], x[1]))
roomInfo = deque(roomInfo)

res = 0
while sum(check) < n:
    flag = roomInfo.popleft()
    if check[flag[0]] : continue
    check[flag[0]] = 1
    for room in roomInfo:
        if check[room[0]] : continue
        if flag[2] <= room[1]:
            check[room[0]] = 1
    
    res += 1

print(res)