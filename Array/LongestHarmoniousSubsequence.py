from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        noApp = dict()
        for i in nums:
            if i in noApp:
                noApp[i] += 1
            else:
                noApp[i] = 1
        result = 0
        for i in noApp:
            if i + 1 in noApp:
                result = max(result, noApp[i] + noApp[i + 1])
        return result


sol = Solution()
sol.findLHS([-3,-1,-1,-1,-3,-2])
