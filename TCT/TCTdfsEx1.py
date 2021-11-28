'''
음료수 얼려 먹기
'''
import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
map = []
for i in range(n):
    map.append(list(input()))
count = 0

#print(map)

def dfs(x, y):
    if x<0 or y<0 or x>=n or y>=m:
        return 
    
    if map[x][y] == '0':
        map[x][y] = '2'
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x+1, y)
        dfs(x, y-1)
    
    return 

for i in range(n):
    for j in range(m):
        if map[i][j] == '0':
            dfs(i, j)
            count += 1
    
print(count)

'''
4 5
00110
00011
11111
00000
'''