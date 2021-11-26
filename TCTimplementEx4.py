n, m = map(int, input().split())
a, b, d = map(int, input().split())

v = [[0]*m for _ in range(n)]
map = []
for _ in range(n):
    map.append(list(map(int, input().split())))

map[a][b] = 1

# n e s w
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

