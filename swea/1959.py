#길이의 차이

n, m = int(input().split())
if n<=m:
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    diff = m-n
    ans = 0
    for d in range(diff+1):
        total = 0
        for i in range(n):
            total += a[d+i]*b[d+i]

        if total > ans:
            ans = total
    
else:
    b = list(map(int, input().split()))
    a = list(map(int, input().split()))

    diff = n-m
    ans = 0
    for d in range(diff+1):
        total = 0
        for i in range(m):
            total += a[d+i]*b[d+i]

        if total > ans:
            ans = total

print(ans)