n, m = map(int, input().split())
simsa = [int(input()) for _ in range(n)]

left, right = 0, max(simsa)*m
res = 0
while left<=right:
    mid = (left+right) // 2
    total = 0

    for item in simsa:
        total += mid//item
    
    if total >= m:
        right = mid - 1
        res = mid
    
    elif total < m:
        left = mid + 1

print(res)