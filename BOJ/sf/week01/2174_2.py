a, b = map(int, input().split())
n, m = map(int, input().split())
dx = [-1,0,1,0]
dy = [0,1,0,-1]
dirInfo = ['N','E','S','W']
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
            
            if curX<=0 or curY<=0 or curX>b or curY>a:
                print('Robot {} crashes into the wall'.format(robotNum))
                exit(0)
            
            if check[curX][curY] != 0:
                print('Robot {} crashes into robot {}'.format(robotNum, check[curX][curY]))
                exit(0)

    elif where == 'L':
        curDir = (curDir-howMany)%4

    elif where == 'R':
        curDir = (curDir+howMany)%4

    check[robots[robotNum][0]][robots[robotNum][1]] = 0
    robots[robotNum] = [curX, curY, curDir]
    check[curX][curY] = robotNum

print('OK')