import queue
from typing import List


class Solution:
    # Basic sol, best so far
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    if i == 0:
                        result += 1
                    if i == len(grid) - 1:
                        result += 1
                    if i - 1 >= 0 and grid[i - 1][j] == 0:
                        result += 1
                    if i + 1 < len(grid) and grid[i + 1][j] == 0:
                        result += 1
                    if j == 0:
                        result += 1
                    if j == len(grid[i]) - 1:
                        result += 1
                    if j - 1 >= 0 and grid[i][j - 1] == 0:
                        result += 1
                    if j + 1 < len(grid[i]) and grid[i][j + 1] == 0:
                        result += 1
        return result

    def islandPerimeter2(self, grid: List[List[int]]) -> int:
        result = 0
        i = 0
        foundFirst = False
        islandsToVist = queue.Queue()
        while i < len(grid):
            j = 0
            while j < len(grid[i]) and not foundFirst:
                if grid[i][j] == 0:
                    j += 1
                else :
                    islandsToVist.put([i, j])
                    foundFirst = True
            if foundFirst:
                break
            i += 1
        while not islandsToVist.empty():
            i, j = islandsToVist.get()
            if grid[i][j] == 1 and [i, j]:
                if j == 0:
                    result += 1
                if j == len(grid[i]) - 1:
                    result += 1
                if j - 1 >= 0:
                    if grid[i][j - 1] == 0:
                        result += 1
                    else:
                        islandsToVist.put([i, j - 1])
                if j + 1 < len(grid[i]):
                    if grid[i][j + 1] == 0:
                        result += 1
                    else:
                        islandsToVist.put([i, j + 1])
                if i == 0:
                    result += 1
                if i == len(grid) - 1:
                    result += 1
                if i - 1 >= 0:
                    if grid[i - 1][j] == 0:
                        result += 1
                    else:
                        islandsToVist.put([i - 1, j])
                if i + 1 < len(grid):
                    if grid[i + 1][j] == 0:
                        result += 1
                    else:
                        islandsToVist.put([i + 1, j])
                grid[i][j] = 2

        return result

    def islandPerimeter3(self, grid: List[List[int]]) -> int:
        # First version time efficient
        result = 0
        foundOnRow = False
        for i in range(len(grid)):
            if foundOnRow:
                foundOnRow = False
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    foundOnRow = True
                    if j == 0:
                        result += 1
                    if j == len(grid[i]) - 1:
                        result += 1
                    if j - 1 >= 0 and grid[i][j - 1] == 0:
                        result += 1
                    if j + 1 < len(grid[i]) and grid[i][j + 1] == 0:
                        result += 1
                    if i == 0:
                        result += 1
                    if i == len(grid) - 1:
                        result += 1
                    if i - 1 >= 0 and grid[i - 1][j] == 0:
                        result += 1
                    if i + 1 < len(grid) and grid[i + 1][j] == 0:
                        result += 1
            if result != 0 and not foundOnRow:
                return result
        return result


sol = Solution()
print(sol.islandPerimeter2([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
