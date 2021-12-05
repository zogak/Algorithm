'''
Cheapest Flights Within K Stops
'''
n = 3
edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
src = 0
dst = 2
K = 0


import collections
import heapq

def findCheapestPrice():
    graph = collections.defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v,w))

    Q = [(0, src, K)]
    while Q:
        price, node, k = heapq.heappop(Q)
        
        # arrived
        if node == dst:
            return price
        
        if k >= 0:
            for v, w in graph[node]:
                alt = price + w
                heapq.heappush(Q, (alt, v, k-1))
    return -1
    
