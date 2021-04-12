#수 나열하기 1

def solution(a,d,n):
    return a + d * (n - 1)

a, d, n = input().split()
a = int(a)
d = int(d)
n = int(n)

print(solution(a,d,n))