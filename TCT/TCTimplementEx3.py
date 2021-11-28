# solution 1
row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

pos = input()
x =  int(row.index(pos[0]) + 1)
y = int(pos[1])

horizontalX = [0, 0]
horizontalY = [2, -2]
verticalX = [-2, 2]
verticalY = [0, 0]

upDownX = [-1, 1]
upDoxnY = [0, 0]
leftRightX = [0, 0]
leftRightY = [-1, 1]

count = 0

for i in range(2):
    nx = x + horizontalX[i]
    ny = y + horizontalY[i]

    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    
    for j in range(2):
        nnx = nx + upDownX[j]
        nny = ny + upDoxnY[j]

        if nnx < 1 or nny < 1 or nnx > 8 or nny > 8:
            continue
        count += 1

for i in range(2):
    nx = x + verticalX[i]
    ny = y + verticalY[i]

    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    
    for j in range(2):
        nnx = nx + leftRightX[j]
        nny = ny + leftRightY[j]

        if nnx < 1 or nny < 1 or nnx > 8 or nny > 8:
            continue
        count += 1

print(count)

# solution 2