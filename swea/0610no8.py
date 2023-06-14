T = int(input())

def parents(cur, ret):
    while arr[cur] != 0:
        ret.append(arr[cur])
        cur = arr[cur]

    return ret

def dfs(node):
    global cnt
    cnt += 1
    for item in tree[node]:
        dfs(item)

for tc in range(1, T+1):
    V, E, target1, target2 = list(map(int, input().split()))
    edges = list(map(int, input().split()))
    tree = {i:[] for i in range(1, V+1)}
    arr = [0]*(V+1)
    for i in range(0, len(edges), 2):
        parent, child = edges[i], edges[i+1]
        arr[child] = parent
        tree[parent].append(child)


    print(arr)
    print(tree)
    target1Parents = parents(target1, [])
    target2Parents = parents(target2, [])

    #target1Parents.sort(reverse=True)
    #target2Parents.sort(reverse=True)

    print(target1Parents)
    print(target2Parents)

    '''
    p, q = 0, 0
    res = 0
    while p < len(target1Parents) and q < len(target2Parents):
        if target1Parents[p] == target2Parents[q]:
            res = target1Parents[p]
            break
        elif target1Parents[p] > target2Parents[q]:
            p += 1
        elif target1Parents[p] < target2Parents[q]:
            q += 1
    '''

    res = 0
    for i in range(len(target1Parents)):
        for j in range(len(target2Parents)):
            if target1Parents[i] == target2Parents[j]:
                res = target1Parents[i]
                break

        if res != 0: break #이중 포문 끝내는 법은 flag인가?
    
    cnt = 0
    dfs(res)
    
    print(f'#{tc} {res} {cnt}')