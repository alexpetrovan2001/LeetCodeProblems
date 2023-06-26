from collections import Counter
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        # 320/322 tests passed (time limit exceeded)
        result = 0
        i = 0
        n = len(height)
        while i < n - 2:
            j = i + 1
            water = 0
            while j < n and height[i]>height[j]:
                water += height[i] - height[j]
                j += 1
            if j == n:
                if height[j-1] >= height[i]:
                    result+=water
                    return result
                else:
                    height[i] -= 1
            elif height[i]<=height[j] and water>0:
                result+=water
                i = j
            else:
                i+=1
        return result

    """
    Correct solution
    def trap(self, height: List[int]) -> int:
        sum = 0
        n = len(height)
        back = [0] * n
        back[n - 1] = height[n - 1]
        for i in reversed(range(n-1)):
            back[i] = max(back[i+1],height[i])
        leftmax = height[0]
        for i in range(1, n-1):
            leftmax = max(leftmax, height[i])
            diff = min(leftmax, back[i]) - height[i]
            sum += diff
        return sum
    """
sol = Solution()
sol.trap([4,2,3])
