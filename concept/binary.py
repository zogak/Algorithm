'''
Decimal -> Binary 
'''
# Decimal -> Binary 1
def getBinaryFromDecimal(n):
    answer = []
    while n > 0:
        answer.append(n%2)
        n = n//2
    answer.reverse()
    return answer

print(getBinaryFromDecimal(5))

# Decimal -> Binary 2
n = 5
ans1 = bin(n)[2:]
print(ans1)
ans1 = bin(n)[2:].zfill(8)
print(ans1)

# Decimal -> Binary 3
ans2 = format(n, 'b')
print(ans2)
ans2 = format(n, 'b').zfill(8)
print(ans2)

'''
Binary -> Decimal
'''
ans = int('101', 2)
print(ans)