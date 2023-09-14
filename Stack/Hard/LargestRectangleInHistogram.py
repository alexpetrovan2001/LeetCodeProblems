from typing import List
import heapq

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Excellent solution for hard problem, 92% time and 62% memory
        stack = []
        max_area = 0
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                height = heights[stack.pop(-1)]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, width * height)
            stack.append(i)
        while stack:
            height = heights[stack.pop(-1)]
            width = len(heights) if not stack else len(heights) - stack[-1] - 1
            max_area = max(max_area, width * height)
        return max_area


sol = Solution()
heights = [4,3,2,6,7]
print(sol.largestRectangleArea(heights))