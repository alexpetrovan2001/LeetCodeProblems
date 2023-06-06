from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) == 1:
            return nums[0]
        index = 0
        n = len(nums)
        while index < n//2:
            if n % 2 == 0 and nums[index] == nums[(n//2) + index]:
                return nums[index]
            else :
                while nums[index+1] == nums[index]:
                    index+=1
                index+=1
        return nums[n//2]


"""
list = [2,2,1] -> sort -> [1,2,2]
list = [2,1,2,1,2,3,2] -> sort -> [1,1,2,2,2,2,2,3]
"""


sol = Solution()
print(sol.majorityElement([2,2,1,1,1,2,2]))