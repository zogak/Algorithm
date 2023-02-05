a, b = map(int, input().split())
n, m = map(int, input().split())
dx = [-1,0,1,0]
dy = [0,1,0,-1]
flag = -1
res = []
check = [[0]*(a+1) for _ in range(b+1)]
robots = [[]]
for i in range(n):
    robot = input().split()
    y, x, dir = int(robot[0]), b-int(robot[1])+1, robot[2]
    check[x][y] = i+1
    robots.append([x,y,dir])

for _ in range(m):
    command = input().split()
    robotNum, where, howMany = int(command[0]), command[1], int(command[2])
    curX, curY, curDir = robots[robotNum]
    if curDir == 'N': curIndex = 0
    elif curDir == 'E': curIndex = 1
    elif curDir == 'S': curIndex = 2
    elif curDir == 'W': curIndex = 3

    if where == 'F':
        for i in range(howMany):
            curX = curX + dx[curIndex]
            curY = curY + dy[curIndex]
            
            if curX<0 or curY<0 or curX>=b or curY>=a:
                flag = 0
                res.append('Robot {} crashes into the wall'.format(robotNum))
                break
            
            if check[curX][curY] != 0:
                flag = check[curX][curY]
                res.append('Robot {} crashes into robot {}'.format(robotNum, flag))
                break

    elif where == 'L':
        curIndex = (curIndex-howMany)%4

    elif where == 'R':
        curIndex = (curIndex+howMany)%4

if flag == -1:
    print('OK')
else:
    print(res[0])