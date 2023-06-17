T = int(input())

def lca(a, b):
    while depthInfo[a] != depthInfo[b]:
        if depthInfo[a] > depthInfo[b] :
            a = parentInfo[a]
        else:
            b = parentInfo[b]

    while a != b:
        a = parentInfo[a]
        b = parentInfo[b]
    
    return a


def dfs(node):
    global cnt
    cnt += 1
    for item in tree[node]:
        dfs(item)

def getDepth(node, depth):
    global depthInfo

    depthInfo[node] = depth

    for item in tree[node]:
        if depthInfo[item] != 0: continue
        getDepth(item, depth+1)

for tc in range(1, T+1):
    V, E, target1, target2 = list(map(int, input().split()))
    edges = list(map(int, input().split()))
    parentInfo = [0]*(V+1) #idx : 자식, value : 부모
    tree = {i:[] for i in range(1, V+1)} 
    for i in range(0, len(edges), 2):
        parent, child = edges[i], edges[i+1]
        parentInfo[child] = parent
        tree[parent].append(child)

    depthInfo = [0]*(V+1)
    getDepth(1, 0)

    res = lca(target1, target2)
    
    cnt = 0
    dfs(res)
    
    print(f'#{tc} {res} {cnt}')



'''
1
13 12 8 13
1 2 1 3 2 4 3 5 3 6 4 7 7 12 5 9 5 8 6 10 6 11 11 13
'''