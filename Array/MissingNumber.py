from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        mySum = 0
        for i in nums:
            mySum += i
        return (len(nums) * (len(nums) + 1) // 2) - mySum
