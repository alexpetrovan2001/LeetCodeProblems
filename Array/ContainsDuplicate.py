from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return False
        return True

    def containsDuplicate2(self, nums: List[int]) -> bool:
        freq = dict()
        for i in nums:
            if i in freq:
                return True
            else: freq[i] = True
        return False

sol = Solution()
sol.containsDuplicate2([1,2,3,1])
