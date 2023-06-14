import heapq
def solution(n, paths, gates, summits):
    info = {i : [] for i in range(1, n+1)}
    for s, e, c in paths:
        info[s].append((e, c))
        info[e].append((s, c))
    
    def dijkstra(node):
        distance = [int(1e9)]*(n+1)
        distance[node] = 0
        q = []
        heapq.heappush(q, (0, node))
        
        while q:
            curCost, curNode = heapq.heappop(q)
            if distance[curNode] < curCost : continue
            
            for nextNode, nextCost in info[curNode]:
                cost = distance[curNode] + nextCost
                if cost < distance[nextNode]:
                    distance[nextNode] = cost
                    heapq.heappush(q, (cost, nextNode))
        
        return distance
    
    resSummit, resIntensity = 0, int(1e9)
    for gate in gates:
        for summit in summits:
            distance = dijkstra(gate)
            dist1 = distance[summit]
            print(dist1)
            distance = dijkstra(summit)
            dist2 = distance[gate]
            print(dist2)
            
            if dist1 + dist2 < resIntensity:
                resIntensity = dist1 + dist2
                resSummit = summit
    
    return [resSummit, resIntensity]

n = 6
paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
gates = [1, 3]
summits = [5]
print(solution(n, paths, gates, summits))