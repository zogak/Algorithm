EAST = 2
WEST = 6
wheel = [list(map(int, input())) for _ in range(4)]
k = int(input())
def rotateEachWheel(wheel, dir):
    rotated = [0]*8
    if dir == 1: #clockwise
        for i, w in enumerate(wheel):
            rotated[(i+9)%8] = w
    elif dir == -1: #counter clockwise
        for i, w in enumerate(wheel):
            rotated[(i+7)%8] = w
    return rotated

def rotate(wheel_num, dir):
    left_num = wheel_num-1
    right_num = wheel_num-1
    left = dir
    right = dir

    #좌 인접
    while (left_num-1) > 0:
        if wheel[left_num][WEST] == wheel[left_num-1][EAST]:
            break
        else:
            print('left')
            wheel[left_num-1] = rotateEachWheel(wheel[left_num-1], -left)
            left_num -= 1
            left = -left
    
    #우 인접
    while (right_num+1) < 4:
        if wheel[right_num][EAST] == wheel[right_num+1][WEST]:
            break
        else:
            print('right')
            wheel[right_num+1] = rotateEachWheel(wheel[right_num+1], -right)
            right_num += 1
            right = -right

    #자기꺼 회전
    wheel[wheel_num-1] = rotateEachWheel(wheel[wheel_num-1], dir)

for i in range(k):
    wheel_num, dir = map(int, input().split())
    rotate(wheel_num, dir)

res = 0
for i, w in enumerate(wheel):
    if w[0] == 1:
        res += 2**i

print(res)