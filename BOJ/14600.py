k = int(input()) #한 변의 길이가 2^k가 되는 것
n = 2**k
board = [[0]*n for _ in range(n)]

holeY, holeX = map(int, input().split())
holeY = n-holeY
holeX = n-holeX

board[holeX][holeY] = -1

