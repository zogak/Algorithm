n = int(input())
cnt = 0
while True:
    if n < 0:
        cnt = -1
        break
    if n == 0:
        break

    if n % 5 == 0:
        cnt += n // 5
        n -= 5 * (n // 5)

    if n == 0:
        break

    n -= 2
    cnt += 1

print(cnt)