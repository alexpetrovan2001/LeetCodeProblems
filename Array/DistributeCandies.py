from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        if not candyType:
            return 0
        n = len(candyType)
        candyType = set(candyType)
        m = len(candyType)
        return m if m < n//2 else n//2