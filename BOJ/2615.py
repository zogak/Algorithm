graph = list(list(map(int, input().split())) for _ in range(19))

def left_right_diagonal(x, y, color):
    default_x, default_y = x, y
    startPos = (x,y)
    isPossible = True
    cnt = 1

    # 왼쪽 대각선 위 탐색
    while True:
        nx, ny = x-1, y-1
        
        if nx<0 or ny<0 or nx>=19 or ny>=19:
            break

        if graph[nx][ny] == color:
            startPos = (nx,ny)
            cnt += 1
            x, y = nx, ny

            if cnt == 6:
                isPossible = False
                break
        else:
            break

    # 오른쪽 대각선 아래 탐색
    x, y = default_x, default_y
    while True:
        nx, ny = x+1, y+1

        if nx<0 or ny<0 or nx>=19 or ny>=19:
            break
        if graph[nx][ny] == color:
            cnt += 1
            x, y = nx, ny

            if cnt == 6:
                break
        
        else:
            break
    
    if cnt != 5:
        isPossible = False

    return isPossible, startPos

def right_left_diagonal(x, y, color):
    default_x, default_y = x, y
    startPos = (x,y)
    isPossible = True
    cnt = 1

    # 오른쪽 대각선 위 탐색
    while True:
        nx, ny = x-1, y+1
        
        if nx<0 or ny<0 or nx>=19 or ny>=19:
            break

        if graph[nx][ny] == color:
            cnt += 1
            x, y = nx, ny

            if cnt == 6:
                isPossible = False
                break
        else:
            break

    # 왼쪽 대각선 아래 탐색
    x, y = default_x, default_y
    while True:
        nx, ny = x+1, y-1

        if nx<0 or ny<0 or nx>=19 or ny>=19:
            break
        if graph[nx][ny] == color:
            startPos = (nx,ny)
            cnt += 1
            x, y = nx, ny

            if cnt == 6:
                break
        
        else:
            break
    
    if cnt != 5:
        isPossible = False

    return isPossible, startPos

def up_down(x, y, color):
    default_x, default_y = x, y
    startPos = (x,y)
    isPossible = True
    cnt = 1

    # 위 탐색
    while True:
        nx, ny = x-1, y
        
        if nx<0 or ny<0 or nx>=19 or ny>=19:
            break

        if graph[nx][ny] == color:
            startPos = (nx,ny)
            cnt += 1
            x, y = nx, ny

            if cnt == 6:
                isPossible = False
                break
        else:
            break

    # 아래 탐색
    x, y = default_x, default_y
    while True:
        nx, ny = x+1, y

        if nx<0 or ny<0 or nx>=19 or ny>=19:
            break
        if graph[nx][ny] == color:
            cnt += 1
            x, y = nx, ny

            if cnt == 6:
                break
        
        else:
            break
    
    if cnt != 5:
        isPossible = False

    return isPossible, startPos

def left_right(x, y, color):
    default_x, default_y = x, y
    startPos = (x,y)
    isPossible = True
    cnt = 1

    # 왼쪽 탐색
    while True:
        nx, ny = x, y-1
        
        if nx<0 or ny<0 or nx>=19 or ny>=19:
            break

        if graph[nx][ny] == color:
            startPos = (nx,ny)
            cnt += 1
            x, y = nx, ny

            if cnt == 6:
                isPossible = False
                break
        else:
            break

    # 오른쪽 탐색
    x, y = default_x, default_y
    while True:
        nx, ny = x, y+1

        if nx<0 or ny<0 or nx>=19 or ny>=19:
            break
        if graph[nx][ny] == color:
            cnt += 1
            x, y = nx, ny

            if cnt == 6:
                break
    
        else:
            break
    
    if cnt != 5:
        isPossible = False

    return isPossible, startPos


def solution():
    ans = 0
    isPossible = False
    startPos = (0,0)
    for i in range(19):
        for j in range(19):
            
            if graph[i][j] == 0:
                continue
            # 검은색
            elif graph[i][j] == 1:
                ans = 1
            # 흰색
            elif graph[i][j] == 2:
                ans = 2

            isPossible, startPos = left_right_diagonal(i,j,ans)
            if isPossible:
                print(ans)
                print(startPos[0]+1, startPos[1]+1)
                return

            isPossible, startPos = right_left_diagonal(i,j,ans)
            if isPossible:
                print(ans)
                print(startPos[0]+1, startPos[1]+1)
                return

            isPossible, startPos = up_down(i,j,ans)
            if isPossible:
                print(ans)
                print(startPos[0]+1, startPos[1]+1)
                return

            isPossible, startPos = left_right(i,j,ans)
            if isPossible:
                print(ans)
                print(startPos[0]+1, startPos[1]+1)
                return

    if not isPossible:
        print(0)
        return
solution()