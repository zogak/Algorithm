import heapq

graph = {
    1: [(2,1), (3,1)],
    2: [(3,1), (4,1)],
    3: [(4,1)],
    4: [],
    5: [(1,1)]
}

distance = [1e9]*6
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) #(거리, 노드)
    distance[start] = 0

    while q:
        dist, node = heapq.heappop(q)
        print('dist : ', dist, 'node : ', node)
        if distance[node] < dist:
            continue
        for item in graph[node]:
            print('item : ', item)
            cost = dist + item[1]
            print('cost : ', cost)
            if cost < distance[item[0]]:
                distance[item[0]] = cost
                heapq.heappush(q, (cost, item[0]))

        print('heap : ', q)

dijkstra(1)
print(distance)