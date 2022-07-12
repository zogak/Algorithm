n, m, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
graph = [[]] + graph
rotate = [list(map(int, input().split())) for _ in range(t)]

def rotateDisk(d,k,m,origin):
    res = [0]*m
    if d == 0:
        for i in range(m):
            res[(i+k)%m] = origin[i]
    elif d == 1:
        for i in range(m):
            res[(i-k)%m] = origin[i]
    return res

for i in range(t):
    x, d, k = rotate[i]

    # 1. rotate multiple disks
    for i, disk in enumerate(graph):
        # fake thing
        if i == 0:
            continue
        
        # multiple
        if i%x == 0:
            #print('which disk', i)
            graph[i] = rotateDisk(d,k,m,disk) #여기서 disk에 결과값을 넣어주면 바뀌지가 않음!!

    #print('graph after rotate', graph)

    # 2  
    total_erase = []
    
    for p in range(1, n+1):
        for q in range(m):
            curr = graph[p][q]
            visited = [[0]*m for _ in range(n+1)]
            erase = []
            if curr == -1:
                continue
            
            # within same disk
            if curr == graph[p][(q+m-1)%m] and visited[p][(q+m-1)%m]==0:
                erase.append((p, (q+m-1)%m))
                visited[p][(q+m-1)%m] = 1
                
            if curr == graph[p][(q+1)%m] and visited[p][(q+1)%m]==0:
                erase.append((p, (q+1)%m))
                visited[p][(q+1)%m] = 1

            # other disk
            if p == 1:
                if curr == graph[p+1][q] and visited[p+1][q]==0:
                    erase.append((p+1, q))
                    visited[p+1][q] = 1
                    
            elif p == n:
                if curr == graph[p-1][q] and visited[p-1][q]==0:
                    erase.append((p-1, q))
                    visited[p-1][q] = 1

            else:
                if curr == graph[p+1][q] and visited[p+1][q]==0:
                    erase.append((p+1, q))
                    visited[p+1][q] = 1

                if curr == graph[p-1][q] and visited[p-1][q]==0:
                    erase.append((p-1,q))
                    visited[p-1][q] = 1
            
            if len(erase)>0 and visited[p][q] == 0:
                erase.append((p,q))
                visited[p][q] = 1
            
                for e in erase:
                    total_erase.append(e)

    #print('total erase', total_erase)
    if len(total_erase)>0:
        for p,q in total_erase:
            graph[p][q] = -1

    elif len(total_erase)==0:
        sum = 0
        cnt = 0
        for i in range(1, n+1):
            for j in range(m):
                if graph[i][j] == -1:
                    continue

                sum += graph[i][j]
                cnt += 1
        #print('sum', sum, 'cnt', cnt)

        if cnt > 0:
            avg = sum / cnt
            #print('avg', avg)

            for i in range(1, n+1):
                for j in range(m):
                    if graph[i][j] == -1:
                        continue

                    if graph[i][j] > avg:
                        graph[i][j] -= 1
                    elif graph[i][j] < avg:
                        graph[i][j] += 1

    #print('after erase', graph)

# sum of the num
res = 0
for i in range(1,n+1):
    for j in range(m):
        if graph[i][j] == -1:
            continue

        res += graph[i][j]

print(res)