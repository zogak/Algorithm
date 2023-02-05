a, b = map(int, input().split())
n, m = map(int, input().split())
check = [[0]*(a+1) for _ in range(b+1)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
robots = []
res = []
for i in range(n):
    robot = input().split()
    x, y, dir = b-int(robot[1])+1, int(robot[0]), robot[2]
    robots.append([x, y, dir])
    check[x][y] = i+1

for _ in range(m):
    flag = -1
    command = input().split()
    robotNum, direction, howMany = int(command[0]), command[1], int(command[2])

    x, y, dir = robots[robotNum-1][0], robots[robotNum-1][1], robots[robotNum-1][2]
    if dir == 'N':
        dirIndex = 0
    elif dir == 'E':
        dirIndex = 1
    elif dir == 'S':
        dirIndex = 2
    elif dir == 'W':
        dirIndex = 3

    for _ in range(howMany):
        if direction == 'F':
            x = x + dx[dirIndex]
            y = y + dy[dirIndex]

            if x < 0 or y < 0 or x >= b or y >= a:
                flag = 0
                res.append('Robot {} crashes into the wall'.format(robotNum))
                break

            if check[x][y] != 0:
                flag = check[x][y]
                res.append('Robot {} crashes into robot {}'.format(robotNum, flag))
                break
        
        elif direction == 'L':
            dirIndex = (dirIndex-1)%4

        elif direction == 'R':
            dirIndex = (dirIndex+1)%4

if flag == -1:
    print('OK')
else:
    print(res[0])

    
