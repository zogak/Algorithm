def isInRange(nx, ny):
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        return False
    return True

loc = input()
x, y = int(loc[1]), ord(loc[0])-96

#NESW
dx = [-2, 0, 2, 0]
dy = [0, 2, 0, -2]

#NS
upDownX = [-1, 1]
upDownY = [0, 0]

#EW
rightLeftX = [0, 0]
rightLeftY = [1, -1]


res = 0

for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if not isInRange(nx, ny):
        continue
    
    #N or S
    if i%2 == 0:
        for j in range(2):
            ex = nx + rightLeftX[j]
            ey = ny + rightLeftY[j]

            if isInRange(ex, ey):
                res += 1
    
    else:
        for j in range(2):
            ex = nx + upDownX[j]
            ey = ny + upDownY[j]

            if isInRange(ex, ey):
                res += 1

print(res)