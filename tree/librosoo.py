n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
move_rule = [map(int, input().split()) for _ in range(m)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
degac_x = [-1,-1,1,1]
degac_y = [-1,1,1,-1]
move_info = {1:(dx[1],dy[1]), 2:(degac_x[1],degac_y[1]), 3:(dx[0],dy[0]),
4:(degac_x[0],degac_y[0]),5:(dx[2],dy[2]),6:(degac_x[3],degac_y[3]),7:(dx[2],dy[2]),
8:(degac_x[2],degac_y[2])}
res = 0
med_pos = [(n-2,0),(n-2,1),(n-1,0),(n-1,1)]

def out_bound(x,y):
    return x<0 or y<0 or x>=n or y>=n

def med_move(year):
    global med_pos
    d, p = move_rule[year]
    dir_x, dir_y = move_info[d]
    for i,med in enumerate(med_pos):
        x,y = med

        for k in range(p):
            nx = x + dir_x
            ny = y + dir_y

            if nx<0: nx = nx+n
            if ny<0: ny = ny+n
            if nx>=n: nx = nx-n
            if ny>=n: ny = ny-n

            x,y = nx,ny
            
        med_pos[i] = (x,y)
    
def grow():
    global graph
    for med in med_pos:
        x,y = med
        graph[x][y] += 1
        # cnt = 0
        # for k in range(4):
        #     nx = x + degac_x[k]
        #     ny = y + degac_y[k]

        #     if out_bound(nx,ny):
        #         continue
        #     if graph[nx][ny] >= 1:
        #         cnt += 1
        # graph[x][y] += cnt

def degac_grow():
    global graph
    

def cut_med():
    global graph
    global med_pos
    new_med = []
    for i in range(n):
        for j in range(n):
            #영양제 맞은 땅이면
            if (i,j) in med_pos:
                continue
            
            if graph[i][j] >= 2:
                graph[i][j] -= 2
                new_med.append((i,j))
    
    med_pos = new_med


for year in range(m):
    med_move(year)
    grow()
    cut_med()

for i in range(n):
    res += sum(graph[i])
print(res)

