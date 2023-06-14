from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        left = 0
        right = len(height)-1
        while left < right:
            curLine = min(height[left], height[right])
            result = max(result, curLine*(right-left))
            if height[left] > height[right]:
                right-=1
            else:
                left+=1
        return result

sol = Solution()
sol.maxArea([1,8,6,2,5,4,8,3,7])