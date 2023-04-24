from itertools import combinations
from collections import deque

N, M = map(int, input().split())
board = {i : [] for i in range(1, N+1)}
for i in range(M):
    a, b = map(int, input().split())
    board[a].append(b)
    board[b].append(a)

chickenHouses = list(combinations([i for i in range(1, N+1)], 2))
distance = int(1e9)

def bfs(c1, c2):
    dist = 0
    q = deque()
    q.append(c1)
    visited = [0]*(N+1)
    visited[c1] = 1

    while q:
        cur = q.popleft()
        for house in board[q]:
            if visited[house] == 1: continue
            if house == c2: continue

            visited[house] = 1
            dist += 1
            q.append(house)
    
    return dist            
        
for house1, house2 in chickenHouses:
    tmpDistance = 0
    tmpDistance += bfs(house1)
    tmpDistance += bfs(house2)

    