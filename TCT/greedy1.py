'''
p.87 거스름돈
'''

def changes(n):
    answer = 0
    coins = [500, 100, 50, 10]

    for coin in coins:
        answer += n // coin
        n = n % coin
    return answer


print(changes(1260))