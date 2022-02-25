'''
p.92 큰 수의 법칙

5 8 3
2 4 5 4 6
'''

n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))
answer = 0
numbers.sort(reverse = True)

