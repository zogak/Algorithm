v, e = map(int, input().split())
parent = [i for i in range(v+1)]
graph = []

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(e):
    a,b,c = map(int, input().split())
    graph.append((c,a,b))

graph.sort()

res = 0
for c,a,b in graph:
    if find_parent(parent, a) != find_parent(parent, b): #같은 집합에 포함되지 않으면
        union_parent(parent, a, b) #합치기
        res += c
        
print(res)