n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

print(a)
print(b)

for i in range(k):
    if a[i] < b[n-1-i]:
        a[i], b[n-1-i] = b[n-1-i], a[i]
    else:
        continue

print(sum(a))

'''
5 3
1 2 5 4 3
5 5 6 6 5
'''