from typing import List
import queue

class Solution:
    # Poor solution with 18% time and 87% memory
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])

        result = 0
        fresh = 0
        to_visit = queue.Queue()

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 2:
                    to_visit.put((row, col, 0))
                if grid[row][col] == 1:
                    fresh += 1

        while not to_visit.empty():
            row, col, time = to_visit.get()
            result = max(result, time)  # Update the result with the current time

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2
                    fresh -= 1
                    to_visit.put((new_row, new_col, time + 1))

        return result if fresh == 0 else -1

sol = Solution()
sol.orangesRotting([[2,1,1],[1,1,1],[0,1,2]])
