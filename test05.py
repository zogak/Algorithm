n = int(input())

#map = list()
#for _ in range(n):
#	map.append(list(map(int, input().split())))
map = [list(map(int, input().split())) for _ in range(n)]
plusMap = [[0 for _ in range(n)] for _ in range(n)]

mid = n // 2
isPlus = False
isX = False

# +
for i in range(n):
	if map[i][mid] == 1:
		plusMap[i][mid] = 2
	if map[mid][i] == 1:
		plusMap[mid][i] = 2

plusCnt = 0	#n+n-1 => 2n - 1
for i in range(n):
	for j in range(n):
		if plusMap[i][j] == 2:
			plusCnt += 1

if plusCnt == 2*n - 1:
	isPlus = True
	
# X
for i in range(n):
	if map[i][i] == 1:
		map[i][i] = 3
	if map[i][n-i-1] == 1:
		map[i][n-i-1] = 3

xCnt = 0
for i in range(n):
	for j in range(n):
		if map[i][j] == 3:
			xCnt += 1

if xCnt == 2*n - 1:
	isX = True
	
if isPlus == True and isX == False:
	print(0)
elif isPlus == False and isX == True:
	print(1)
else:
	print(2)