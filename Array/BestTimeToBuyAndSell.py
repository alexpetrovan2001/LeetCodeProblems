from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min = 10000
        for i in range(len(prices)):
            if prices[i] < min:
                min = prices[i]
            if prices[i]-min > profit:
                profit = prices[i]-min
        return profit

sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))




