from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        minRows = 1000000000
        minCols = 1000000000
        if not ops:
            return m * n
        for i in ops:
            minRows = min(i[0], minRows)
            minCols = min(i[1], minCols)
        return minCols*minRows



sol = Solution()
sol.maxCount(26,17,[[20,10],[26,11],[2,11],[4,16],[2,3],[23,13],[7,15],[11,11],[25,13],[11,13],[13,11],[13,16],[26,17]])