m, n = map(int, input().split())
snack = list(map(int, input().split()))

max_snack = max(snack)

l, r = 1, max_snack
answer = 0
while l <= r :
    mid = (l+r)//2
    cnt = 0

    for s in snack:
        cnt += s//mid
    
    if cnt >= m:
        answer = max(answer,mid)
        l = mid+1
    else:
        r = mid-1

print(answer)