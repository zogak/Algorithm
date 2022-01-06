n = int(input())
graph = [[]for _ in range(n+1)]
for _ in range(n):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

visited = [0]*(n+1)
cnt = 0
ans = list()

def dfs(start):
	global cnt
	#cnt += 1
	#ans.append(start)
	visited[start] = 1
	for item in graph[start]:
		if visited[item] == 0:
			dfs(item)
			cnt += 1

dfs(1)
print(cnt)
print(visited)
for v in visited:
    if v==1:
        print(visited.index(v), end = ' ')