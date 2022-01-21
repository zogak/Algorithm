'''
약수 구하는 방법
'''

#첫 번째 방법
def getDivisors(n):
    res = list()
    for i in range(1, n+1):
        if (n % i) == 0:
            res.append(i)
    return res

#두 번째 방법
def getDivisors2(n):
    res = list()
    for i in range(1, int(n**0.5)+1):
        if (n % i) == 0:
            res.append(i)
            if i != (n//i):
                res.append(n//i)
    return res

print(getDivisors(12))
print(getDivisors2(20))