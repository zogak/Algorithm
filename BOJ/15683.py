'''
경우의 수(dfs) + bfs
'''

import copy
n, m = map(int, input().split())
graph = []
cctvs = []
for i in range(n):
    temp = map(int, input().split())
    for j in range(m):
        if temp[j] !=0 and temp[j] !=6:
            cctvs.append((temp[j], (i,j)))

    graph.append(temp)

dx = [-1,0,1,0]
dy = [0,1,0,-1]

# dir = {
#     "N" : 0,
#     "E" : 1,
#     "S" : 2,
#     "W" : 3
# }

# info = {
#     "1" : ["N","E","S","W"],
#     "2" : [("N","S"), ("E","W")],
#     "3" : [("N","E"),("E","S"),("S","W"),("W","N")],
#     "4" : [("N","E","S"),("E","S","W"),("S","W","N"),("W","N","E")],
#     "5" : [("N","E","S","W")]
# }

info = {
    "1" : [0,1,2,3],
    "2" : [(0,2), (1,3)],
    "3" : [(0,1),(1,2),(2,3),(3,4)],
    "4" : [(0,1,2),(1,2,3),(2,3,0),(3,0,1)],
    "5" : [(0,1,2,3)]
}

def watch(arr,dir,x,y):
    for d in dir:
        nx = x + dx[d]
        ny = y + dy[d]

        if nx<0 or ny<0 or nx>=n or ny>=m:
            continue
        if arr[nx][ny] != 6:
            if arr[nx][ny] == 0:
                arr[nx][ny] = -1
            nx += dx[d]
            ny += dy[d]

def dfs(depth, arr):
    if depth == len(cctvs):
        cnt = 0
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 0:
                    cnt += 1
        res = min(res, cnt)
        return

    else:
        temp = copy.deepcopy(arr)
        cctv_num,x,y = cctvs[depth]
        for item in info[cctv_num]:
            watch(temp,item,x,y)
            dfs(depth+1, temp)
            temp = copy.deepcopy(arr)

res = int(1e9)
dfs(0, graph)
print(res)