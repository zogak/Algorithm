'''
3. 숫자 카드 게임

3 3
3 1 2
4 1 4
2 2 2

2 4
7 3 1 8
3 3 3 4
'''

n, m = map(int, input().split())
cards = [list(map(int, input().split())) for _ in range(n)]

for row in cards:
    row.sort()

print(cards)

leastNumInRows = list(zip(*cards))[0]
print(leastNumInRows)

answer = max(leastNumInRows)
print(answer)