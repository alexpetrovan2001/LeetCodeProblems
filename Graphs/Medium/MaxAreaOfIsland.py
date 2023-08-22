from typing import List

class Solution:
    # Incredible solution. Beats 99.8% time and 70% memory
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0

        if not grid:
            return result

        m =  len(grid)
        n = len(grid[0])

        def dfs(row, col):
            grid[row][col] = 0
            area = 1
            if row < m-1 and grid[row+1][col] == 1:
                area += dfs(row+1, col)
            if row > 0 and grid[row-1][col] == 1:
                area += dfs(row-1, col)
            if col < n-1 and grid[row][col+1] == 1:
                area += dfs(row, col+1)
            if col > 0 and grid[row][col-1] == 1:
                area += dfs(row, col-1)
            return area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = dfs(i, j)
                    result = max(area, result)

        return result

sol = Solution()
sol.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],
                     [0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]])