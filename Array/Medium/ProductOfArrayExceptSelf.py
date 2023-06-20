from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
    # Best solution I could ever find : beats 95% memory and time. 
         product = 1
         zeroPos = []
         n = len(nums)
         for i in range(n):
             if nums[i] == 0:
                 zeroPos.append(i)
             else:
                 product *= nums[i]
         if len(zeroPos) >= 2:
             return [0] * n
         elif len(zeroPos) == 1:
             nums = [0] * (n-1)
             nums.insert(zeroPos[0], product)
             return nums
         else:
            for i in range(n):
                nums[i] = product // nums[i]
            return nums

sol = Solution()
sol.productExceptSelf([-1,1,2,-3,3])