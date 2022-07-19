EAST = 2
WEST = 6
CLOCK = 1
COUNTER_CLOCK = -1
wheel = [list(map(int, input())) for _ in range(4)]
k = int(input())
command = [list(map(int, input().split())) for _ in range(k)]

def getCandidates(wheel_num, dir):
    leftCandidates = []
    rightCandidates = []
    wheel_num_left = wheel_num
    wheel_num_right = wheel_num

    while wheel_num_left-1 > 0:
        if wheel[wheel_num_left][WEST] == wheel[wheel_num_left-1][EAST]:
            break
        else:
            leftCandidates.append((wheel_num_left-1, -dir))
            dir = -dir
            wheel_num_left -= 1

    while wheel_num_right+1 < 4:
        if wheel[wheel_num_right][EAST] == wheel[wheel_num_right+1][WEST]:
            break
        else:
            rightCandidates.append((wheel_num_right+1, -dir))
            dir = -dir
            wheel_num_right += 1
    
    return leftCandidates, rightCandidates

def rotateEach(wheelArray, dir):
    res = [0]*8
    if dir == CLOCK:
        for i in range(8):
            res[(i+1)%8] = wheelArray[i]
    elif dir == COUNTER_CLOCK:
        for i in range(8):
            res[(i-1)%8] = wheelArray[i] 
    return res

def rotate(wheel_num, dir, left, right):
    wheel[wheel_num] = rotateEach(wheel[wheel_num], dir)
    for num, d in left:
        wheel[num] = rotateEach(wheel[num], d)
    
    for num, d in right:
        wheel[num] = rotateEach(wheel[num], d)

for wheel_num, dir in command:
    wheel_num -= 1
    left, right = getCandidates(wheel_num, dir)
    print('left', left)
    print('right', right)
    rotate(wheel_num, dir, left, right)
    print('after rotate', wheel)

res = 0
for i, w in enumerate(wheel):
    if w[0] == 1:
        res += 2**i

print(res)