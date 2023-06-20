import sys
sys.setrecursionlimit(10**6)
def solution(info, edges):
    #1. 트리 구성
    tree = {i:[] for i in range(len(info))}
    movable = [0]
    for parent, child in edges:
        tree[parent].append(child)
        if parent == 0 : movable.append(child)

    res = 0
    visited = [0]*len(info)
    def dfs(sheep, wolf, cur, movable):
        nonlocal res, visited

        sheep += (info[cur]^1)
        wolf += info[cur]
        
        if sheep <= wolf:
            return
        
        res = max(res, sheep)

        for node in movable:
            if visited[node] : continue
            visited[node] = 1
            dfs(sheep, wolf, node, movable+tree[node])
            visited[node] = 0

    visited[0] = 1
    dfs(0, 0, 0, movable)
    return res

print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))