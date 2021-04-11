#CodeUp 1162 당신의 사주를 봐 드립니다 1
y, m, d = input().split()
y = int(y)
m = int(m)
d = int(d)

temp = y-m+d
if temp%10 == 0 :
    print("대박")
else:
    print("그럭저럭")