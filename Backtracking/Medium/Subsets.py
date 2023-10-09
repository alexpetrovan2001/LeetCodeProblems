from typing import List

class Solution:
    # Avg solution, 94% time and 63% memory - depending on the examples
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            result.append(path[:])
            for i in range(start, len(nums)):
                backtrack(i + 1, path + [nums[i]])

        result = []
        backtrack(0, [])
        return result


sol = Solution()
sol.subsets([1,2,3,4,5,6,7])
