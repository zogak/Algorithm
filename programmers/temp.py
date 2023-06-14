import heapq
n = 4

# key : 출발 노드, value : (도착 노드, 가중치)
info = {
    1 : [(2, 1), (3, 4), (4, 10)],
    2 : [(3, 2)],
    3 : [(4, 1)],
    4 : []
}

def dijkstra(node): #출발 노드
    distance = [int(1e9)]*(n+1) #무한대로 초기화
    distance[node] = 0 #시작노드의 거리는 0
    q = []
    heapq.heappush(q, (0, node)) #cost, node순

    while q:
        curCost, curNode = heapq.heappop(q) #이번 케이스에 curNode까지 가는데 curCost만큼 필요함
        if distance[curNode] < curCost : continue # 이미 이번 케이스보다 더 짧게 가는게 구해진 상태면 넘어가

        for nextNode, nextCost in info[curNode]: #curNode와 연결된 것들을 돌면서
            cost = distance[curNode] + nextCost #curNode까지의 비용 + curNode에서 nextNode가는 비용
            if distance[nextNode] > cost:
                distance[nextNode] = cost
                heapq.heappush(q, (cost, nextNode))

    return distance

distance = dijkstra(1)
print(distance)