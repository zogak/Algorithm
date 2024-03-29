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

def candidate(wheel_num,dir):
    left_num = wheel_num
    right_num = wheel_num
    left = dir
    right = dir
    to_left = []
    to_right = []

    #좌 인접
    while (left_num-1) > 0:
        if wheel[left_num][WEST] == wheel[left_num-1][EAST]:
            break
        else:
            to_left.append((left_num, -left))
            left = -left
            left_num -= 1
            
    
    #우 인접
    while (right_num+1) < 4:
        if wheel[right_num][EAST] == wheel[right_num+1][WEST]:
            break
        else:
            to_right.append((right_num, -right))
            right = -right
            right_num += 1
    
    return to_left, to_right


def rotate(wheel_num, dir, l, r):
    
    # 자기 자신
    wheel[wheel_num-1] = rotateEachWheel(wheel[wheel_num-1], dir)

    for item_num, item_dir in l:
        wheel[item_num] = rotateEachWheel(wheel[item_num], item_dir)

    for item_num, item_dir in r:
        wheel[item_num] = rotateEachWheel(wheel[item_num], item_dir)

for i in range(k):
    wheel_num, dir = map(int, input().split())
    l, r = candidate(wheel_num-1, dir)
    print(i,'-> ', 'l', l, 'r', r)
    rotate(wheel_num, dir, l, r)
    print(wheel)

res = 0
for i, w in enumerate(wheel):
    if w[0] == 1:
        res += 2**i

print(res)