from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        set_nums = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in nums:
                result.append(i)
        return result
