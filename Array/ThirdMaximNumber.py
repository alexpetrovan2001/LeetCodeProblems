from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(set(nums), reverse=True)
        if len(nums) <= 2:
            return nums[0]
        return nums[2]

    def thirdMax2(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        max0, max1, max2 = -100000000000, -100000000000, -100000000000
        for i in nums:
            if i > max0:
                max2 = max1
                max1 = max0
                max0 = i
            elif i > max1 and i != max0:
                max2 = max1
                max1 = i
            elif i > max2 and i != max1:
                max2 = i

        return max2

    def thirdMax3(self, nums: List[int]) -> int:
        # The best so far
        max0, max1, max2 = -100000000000, -100000000000, -100000000000
        for i in nums:
            if i >= max0:
                if i!=max0:
                    max2 = max1
                    max1 = max0
                max0 = i
            elif i>=max1:
                if i != max1:
                    max2=max1
                max1 = i
            elif i>max2:
                max2 = i
        return max2 if max2 != -100000000000 else max0


sol = Solution()
sol.thirdMax3([3,2,2,1])