n, m = map(int, input().split())
r, c, d = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

#북동남서
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def rotate(current_dir):
    # ver1
    '''
    if current_dir - 1 < 0:
        return 3
    return current_dir - 1
    '''
    # ver2
    return (current_dir+3) % 4
    

flag = False
start_flag = False
cnt = 0
answer = 1
visited[r][c] = 1

while True:
    # rotate to left
    d = rotate(d)

    nr = r + dir[d][0]
    nc = c + dir[d][1]

    # wall | already visited
    if graph[nr][nc]==1 or visited[nr][nc]==1:
        print('case 1')
        # first time in succession
        if not start_flag:
            start_flag = True
            flag = True
            cnt += 1

        else:
            if flag:
                cnt += 1

    # not cleaned yet
    if graph[nr][nc]==0 and visited[nr][nc]==0:
        print('case 2')
        # update current pos
        r = nr
        c = nc
        visited[r][c] = 1
        answer += 1

        flag = False
        
    if cnt == 4:
        cnt = 0
        start_flag = False
        flag = False

        # wall behind
        behind_d = (d+2)%4
        nr = r + dir[behind_d][0]
        nc = c + dir[behind_d][1]
        if graph[nr][nc]==1:
            break

        else:
            # go back
            r = nr
            c = nc
    
print(answer)

'''
4 4
1 2 0
1 1 1 1
1 0 0 1
1 0 0 1
1 1 1 1
'''