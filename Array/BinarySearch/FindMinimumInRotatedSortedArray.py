from typing import List

class Solution:
    # Beats 67% time and 81% memory.
    # Can improve time by returning nums[0] if nums[0] < nums[-1]
    # but increases memory significantly: (81% -> 12%) and time (67% -> 87%)
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        # if n == 1 or nums[0] < nums[-1]:
        #     return nums[0]
        left = nums[:n//2]
        right = nums[n//2:]
        leftMin = min(left[0], left[-1])
        rightMin = min(right[0], right[-1])
        return self.findMin(left) if leftMin < rightMin else self.findMin(right)


sol = Solution()
print(sol.findMin([3,4,5,1,2]))