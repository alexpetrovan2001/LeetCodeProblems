from typing import List


class Solution:
    # Beats 40% time and 47% memory
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while low < high:
            mid = (low + high) // 2
            if self.canEatAll(piles, h, mid):
                high = mid
            else:
                low = mid + 1
        return low

    def canEatAll(self, piles: List[int], h: int, value: int):
        for i in piles:
            h -= i // value
            if i % value != 0:
                h -= 1
        return h >= 0


sol = Solution()
print(sol.minEatingSpeed([3,6,7,11], 8))