from collections import deque
T = int(input())

def lca(a, b):
    while depthInfo[a] != depthInfo[b]:
        if depthInfo[a] > depthInfo[b]:
            a = parents[a]
        else:
            b = parents[b]
    
    while a != b:
        a = parents[a]
        b = parents[b]

    return a

def getDepth():
    global depthInfo
    q = deque()
    visited = [0]*(N+1)
    visited[1] = 1
    q.append((1, 0)) #node, depth

    while q:
        node, depth = q.popleft()
        depthInfo[node] = depth
        for item in tree[node]:
            if visited[item] != 0: continue
            visited[item] = 1
            q.append((item, depth+1))

for tc in range(1, T+1):
    N = int(input())
    tree = {i:[] for i in range(1, N+1)}
    parents = [0, 1] + list(map(int, input().split())) #idx : child, val : parent
    #print(parents)
    for i in range(2, N+1):
        parent, child = parents[i], i
        tree[parent].append(child)

    depthInfo = [0]*(N+1)
    getDepth()

    res = 0
    q = deque()
    q.append(1)
    visited = [0]*(N+1)
    visited[1] = 1
    start = 1
    #print(tree)
    #print(depthInfo)
    while q:
        node = q.popleft()
        for end in tree[node]:
            if visited[end] != 0: continue
            visited[end] = 1
            ancestor = lca(start, end)
            #print(f'{start}와 {end}의 공통조상 : {ancestor}')
            #print(f'{ancestor}와 {start} 사이의 거리 : {abs(depthInfo[ancestor] - depthInfo[start])}')
            #print(f'{ancestor}와 {end} 사이의 거리 : {abs(depthInfo[ancestor] - depthInfo[end])}')
            res += (abs(depthInfo[ancestor] - depthInfo[start]) + abs(depthInfo[ancestor]-depthInfo[end]))
            #print(res)
            start = end
            q.append(end)

    print(f'#{tc} {res}')