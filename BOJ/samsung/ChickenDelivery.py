from itertools import combinations

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

chickenHouse = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            chickenHouse.append((i,j))

chickenHouseNum = len(chickenHouse)
chickenDist = {i:[] for i in range(chickenHouseNum)}

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            for k , chicken in enumerate(chickenHouse):
                chickenDist[k].append(abs(i-chicken[0]) + abs(j-chicken[1]))

combi = list(combinations(chickenDist.keys(), m))
print(combi)

answer = 0