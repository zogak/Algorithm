'''
랜선 자르기
'''

k, n = map(int, input().split())
lines = list(int(input()) for _ in range(k))
lines.sort(reverse=True)

answer = 0
l, r = 1, lines[0]
while l <= r:
    m = (l+r)//2
    cnt = 0
    for line in lines:
        cnt += line//m

    if cnt < n:
        r = m - 1

    else:
        l = m + 1
        answer = m
print(answer)