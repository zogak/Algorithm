'''
2606. 바이러스
'''

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

'''
-----
graph
-----
[[],
 [2, 5],
 [1, 3, 5], 
 [2], 
 [7], 
 [1, 2, 6], 
 [5], 
 [4]]
'''
cnt = 0
visited = [0] * (n+1)
def dfs(start):
    global cnt
    visited[start] = 1
    for item in graph[start]:
        if visited[item] == 0:
            cnt += 1
            dfs(item)

dfs(1)
print(cnt)