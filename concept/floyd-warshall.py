graph = {
    1: [(2,1), (3,1)],
    2: [(3,1), (4,1)],
    3: [(4,1)],
    4: [],
    5: [(1,1)]
}

inf = int(1e9)
distance = [[inf]*6 for _ in range(6)]

# 처음 입력받은 간선,노드 정보에 의해 바로 연결된 두 노드 사이의 거리는 1로 업데이트
for key in graph.keys():
    for item in graph[key]:
        distance[key][item[0]] = 1

# 자기 자신 거리 0
for i in range(1, 6):
    distance[i][i] = 0

for k in range(1, 6): #거쳐갈 노드 설정
    for i in range(1, 6):
        for j in range(1, 6):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

print(distance)