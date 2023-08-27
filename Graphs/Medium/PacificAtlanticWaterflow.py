from typing import List

class Solution:
    # Beats 84% time but very poor memory - 10%
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        m = len(heights)
        n = len(heights[0])

        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c, reachable):
            reachable.add((r,c))
            for dirRow, dirCol in dir:
                newRow, newCol = r + dirRow, c + dirCol
                if 0 <= newRow < m and 0 <= newCol < n and (newRow, newCol) not in reachable and heights[r][c] <= heights[newRow][newCol]:
                    dfs(newRow, newCol, reachable)

        reachAtlantic = set()
        reachPacific = set()

        for col in range(n):
            dfs(0, col, reachPacific)
        for row in range(m):
            dfs(row, 0, reachPacific)

        for col in range(n):
            dfs(m-1, col, reachAtlantic)
        for row in range(m):
            dfs(row, n-1, reachAtlantic)

        return reachAtlantic.intersection(reachPacific)

sol = Solution()
sol.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])

