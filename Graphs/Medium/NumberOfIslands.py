import queue
from typing import List


class Solution:
    # Beats 95% time and 90% memory
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        m = len(grid)
        n = len(grid[0])

        def dfs(row, col):
            rows = len(grid)
            cols = len(grid[0])

            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == '0':
                return

            grid[row][col] = '0'

            dfs(row, col - 1)
            dfs(row, col + 1)
            dfs(row - 1, col)
            dfs(row + 1, col)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    island_count += 1
                    dfs(i, j)

        return island_count

sol = Solution()
print(sol.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","1","1","0"]
]))
