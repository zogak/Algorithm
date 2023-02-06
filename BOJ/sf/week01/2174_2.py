a, b = map(int, input().split())
n, m = map(int, input().split())
dx = [-1,0,1,0]
dy = [0,1,0,-1]
dirInfo = ['N','E','S','W']
flag = -1
check = [[0]*(a+1) for _ in range(b+1)]
robots = [[]]
for i in range(n):
    robot = input().split()
    y, x, dir = int(robot[0]), b-int(robot[1])+1, robot[2]
    check[x][y] = i+1
    robots.append([x,y,dirInfo.index(dir)])

for _ in range(m):
    command = input().split()
    robotNum, where, howMany = int(command[0]), command[1], int(command[2])
    curX, curY, curDir = robots[robotNum]

    if where == 'F':
        for i in range(howMany):
            curX = curX + dx[curDir]
            curY = curY + dy[curDir]
            
            if curX<0 or curY<0 or curX>=b or curY>=a:
                flag = 0
                print('Robot {} crashes into the wall'.format(robotNum))
                exit()
            
            if check[curX][curY] != 0:
                flag = check[curX][curY]
                print('Robot {} crashes into robot {}'.format(robotNum, flag))
                exit()

    elif where == 'L':
        curDir = (curDir-howMany)%4

    elif where == 'R':
        curDir = (curDir+howMany)%4

    robots[robotNum] = [curX, curY, curDir]

print('OK')