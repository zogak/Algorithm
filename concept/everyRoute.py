'''
BACK TRACIKING
'''
n, m = map(int, input().split())
graph = {i:[] for i in range(1, n+1)}

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

visited = [0]*(n+1)

def dfs(node):
    if node == n:
        ans = '-'.join(map(str, path))
        print(ans)

    else:
        for item in graph[node]:
            if visited[item] == 1:
                continue
            
            #print('node :', node , ' item:', item)
            visited[item] = 1
            path.append(item)
            dfs(item)
            #print('finished')
            path.pop()
            visited[item] = 0
        

visited[1] = 1
path = [1]
dfs(1)

'''
5 6
1 2
2 3
2 4
2 5
3 4
4 5
'''