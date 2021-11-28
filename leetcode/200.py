'''
200. Number of Islands
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            if x < 0 or y < 0 or x >=n or y >=m:
                return
            if grid[x][y] == '1':
                grid[x][y] = '0'

                dfs(x-1, y)
                dfs(x, y+1)
                dfs(x+1, y)
                dfs(x, y-1)
            return
    
        n = len(grid)
        m = len(grid[0])
        
        count = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count
        