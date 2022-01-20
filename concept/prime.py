'''
에라토스테네스의 체를 이용하여 소수를 찾는 법
* 소수 (prime number): 1과 자기 자신으로만 나누어 떨어지는 수
'''

def getPrimeNumber(n):
    check = [True] * (n+1)

    m = int(n**0.5)
    for i in range(2, m+1):
        if check:
            for j in range(i+i, n+1, i):
                check[j] = False
    
    return [i for i in range(2, n+1) if check[i]]