'''
samsung 3190. 뱀
'''
# import collections
# info = {
#     'snake' : 1,
#     'apple' : 2
# }
# # snakeDir = {
# #     'E' : {'L' : [0, -1, 'N'], 'D' : [1, 0, 'S']},
# #     'S' : {'L' : [0, 1, 'E'], 'D' : [0, -1, 'W']},
# #     'W' : {'L' : [1, 0, 'S'], 'D' : [-1, 0, 'N']},
# #     'N' : {'L' : [0, -1, 'W'], 'D' : [0, 1, 'E']}
# # }
# snakeDir = {
#     'E' : {'L' : 'N', 'D' : 'S'},
#     'S' : {'L' : 'E', 'D' : 'W'},
#     'W' : {'L' : 'S', 'D' : 'N'},
#     'N' : {'L' : 'W', 'D' : 'E'}
# }
# snakeDirForStraight = {
#     'E' : [0, 1],
#     'S' : [1, 0],
#     'W' : [0, -1],
#     'N' : [-1, 0]
# }
# #NESW
# dirX = [-1, 0, 1, 0]
# dirY = [0, 1, 0, -1]
# n = int(input())
# board = [[0]*n for _ in range(n)]
# board[0][0] = info['snake']
# headX, headY, tailX, tailY = 0, 0, 0, 0
# currentSnakeDir = 'E'

# k = int(input())
# for _ in range(k):
#     appleX, appleY = map(int, input().split())
#     board[appleX][appleY] = info['apple']

# L = int(input())
# rotatingInfo = []
# for _ in range(L):
#     timeToRotate, dir = input().split()
#     rotatingInfo.append([timeToRotate, dir])
# rotatingInfo = collections.deque(rotatingInfo)

# time = 0
# isApple = False

# while True:
#     time += 1

#     print('time:{}, go'.format(time))
#     x = headX + snakeDirForStraight[currentSnakeDir][0]
#     y = headY + snakeDirForStraight[currentSnakeDir][1]
#     if board[x][y] == info['apple']:
#         isApple = True
#     board[x][y] = info['snake']
#     headX, headY = x, y
#     print('snake:{},{}', headX, headY)

#     #회전하는 경우
#     if rotatingInfo and time == int(rotatingInfo[0][0]):
#         print('rotate')
#         tmp = rotatingInfo.popleft()
#         currentSnakeDir = snakeDir[currentSnakeDir][tmp[1]]

#     #사과 있는 경우 pass
#     #사과 없는 경우
#     if not isApple:
#         board[tailX][tailY] = 0
#         for i in range(4):
#             if board[tailX + dirX[i]][tailY + dirY[i]] == info['snake']:
#                 tailX = tailX + dirX[i]
#                 tailY = tailY + dirY[i]
#                 isApple = False
#                 break
    
#     #머리가 벽에 부딪히거나 몸에 부딪히면 끝
#     frontOfHeadX = headX + snakeDirForStraight[currentSnakeDir][0]
#     frontOfHeadY = headY + snakeDirForStraight[currentSnakeDir][1]
#     if frontOfHeadX < 0 or frontOfHeadX >= n or frontOfHeadY < 0 or frontOfHeadY >=n:
#        time += 1
#        break
#     if board[frontOfHeadX][frontOfHeadY] == info['snake']:
#        time += 1
#        break
    
# print(time)

import collections

#apple : 2
#snake : 1
n = int(input())
k = int(input())
board = [[0]*(n+1) for _ in range(n+1)]
for _ in range(k):
    a, b = map(int, input().split())
    board[a][b] = 2

rotatingInfo = collections.deque()
L = int(input())
for _ in range(L):
    x, c = input().split()
    rotatingInfo.append([int(x), c])

#ESWN
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def rotate(direction, c):
    if c == "L":
        direction = (direction-1)%4
    else:
        direction = (direction+1)%4
    return direction

def simulate():
    headX, headY = 1, 1
    board[headX][headY] = 1
    direction = 0
    time = 0
    snake = collections.deque()
    snake.append([headX, headY])
    
    while True:
        time += 1
        nx = headX + dx[direction]
        ny = headY + dy[direction]

        if nx >= 1 and ny >= 1 and nx <=  n and ny <= n and board[nx][ny] != 1:
            # no apple
            if board[nx][ny] == 0:
                board[nx][ny] = 1
                snake.append([nx, ny])
                tail = snake.popleft()
                tailX, tailY = tail[0], tail[1]
                board[tailX][tailY] = 0
            
            # apple
            elif board[nx][ny] == 2:
                board[nx][ny] = 1
                snake.append((nx, ny))
            
        else:
            break

        headX, headY = nx, ny
        
        if rotatingInfo and time == rotatingInfo[0][0]:
            direction = rotate(direction, rotatingInfo[0][1])
            rotatingInfo.popleft()
    return time

print(simulate())