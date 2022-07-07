from cmath import inf
from itertools import combinations

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

chicken, house = [], []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i+1,j+1))
        elif graph[i][j] == 2:
            chicken.append((i+1,j+1))

#print('chicken', chicken)
#print('house', house)
chickenNum = len(chicken)
combi = list(combinations([i for i in range(chickenNum)], m))
#print('combi', combi)

def getDistance(a,b,c,d):
    return abs(a-c) + abs(b-d)


finalDist = inf
for c in combi: #0 번 이랑 1번 치킨 집, 2번 치킨 집 3개만 남길거야
    #print('c', c)
    tempDist = 0
    for h in house: # 집들마다 돌면서
        chickenDistOfHouse = inf
        for k in range(m): 
            chickenDistOfHouse = min(chickenDistOfHouse, getDistance(h[0], h[1], chicken[c[k]][0], chicken[c[k]][1]))
        #print('chickenDist', chickenDistOfHouse)
        tempDist += chickenDistOfHouse
        #print('tempDist', tempDist)
    finalDist = min(finalDist, tempDist)
        
print(finalDist)
