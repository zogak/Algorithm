n, m = map(int, input().split()) #학생수, 보석종류
gems = [int(input()) for _ in range(m)]
res = 0

left, right = 1, max(gems)
while left <= right:
    mid = (left+right)//2 #각 학생이 가질 보석의 개수
    cnt = 0 #각 학생이 mid개씩 보석을 가진다 했을 때 보석을 다 나누어 가지면 몇 명의 학생이 나누어 가질 수 있는지
    for gem in gems:
        if gem < mid:
            cnt += 1
        elif gem % mid == 0:
            cnt += (gem//mid)
        elif gem % mid != 0:
            cnt += (gem//mid) + 1
    
    if cnt <= n:
        right = mid - 1
        res = mid
    
    elif cnt > n:
        left = mid + 1

print(res)