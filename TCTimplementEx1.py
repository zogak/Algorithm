x = 1
y = 1
n = int(input())
movement = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
moveType = ['L', 'R', 'U', 'D']

for move in movement:
    for i in range(4):
        if move == moveType[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    
    x, y = nx, ny

print(x, y)

'''
5
R R R U D D
'''