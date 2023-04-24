n = int(input())
balloons = list(map(int, input().split()))
res = [1]
num = balloons [0]
balloons[0] = 0
curIndex = 0

while len(res) < n:
    while abs(num) > 0:
        if num > 0:
            curIndex = (curIndex+1)%n
            if balloons[curIndex] == 0:
                continue
            
            num -= 1

        elif num < 0:
            curIndex = (curIndex-1)%n
            if balloons[curIndex] == 0:
                continue
            
            num += 1
    res.append(curIndex+1)
    num = balloons[curIndex]
    balloons[curIndex] = 0

print(' '.join(map(str, res)))