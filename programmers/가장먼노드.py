from collections import deque
from collections import Counter
def solution(n, edge):
    graph = {i:[] for i in range(1, n+1)}
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
    
    answer = 0
    q = deque()
    check = [0]*(n+1)
    #level = 0
    #level_graph={}
    dist = [0]*(n+1)

    def bfs(node):
        nonlocal check, q, graph, dist
        check[node] = 1
        q.append(node)
        
        
        while q:
            print('q : ' , q)
            curr = q.popleft()
            
            for item in graph[curr]:
                
                if check[item] == 0:
                    q.append(item)
                    check[item] = 1
                    dist[item] = dist[curr] + 1
            
            
    
    bfs(1)
    max_dist = max(dist)
    cnt = Counter(dist)
    answer = cnt[max_dist]
    
            
    return answer

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))