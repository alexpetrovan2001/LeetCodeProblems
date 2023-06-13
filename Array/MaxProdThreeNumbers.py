from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return nums[0]*nums[1]*nums[2]
        maxPos = sorted(nums[:3], reverse=True)
        maxNeg = sorted(nums[:3])
        if maxNeg[0] > 0:
            maxNeg = [0,0,0]
        nums = nums[3:]
        for i in nums:
            if i < 0:
                if i <= maxNeg[0]:
                    maxNeg[2] = maxNeg[1]
                    maxNeg[1] = maxNeg[0]
                    maxNeg[0] = i
                elif i <= maxNeg[1]:
                    maxNeg[2] = maxNeg[1]
                    maxNeg[1] = i
                elif i <= maxNeg[2]:
                    maxNeg[2] = i
            if i >= maxPos[0]:
                maxPos[2] = maxPos[1]
                maxPos[1] = maxPos[0]
                maxPos[0] = i
            elif i >= maxPos[1]:
                maxPos[2] = maxPos[1]
                maxPos[1] = i
            elif i >= maxPos[2]:
                maxPos[2] = i
        if maxNeg[0]*maxNeg[1] > maxPos[1]*maxPos[2] and maxPos[0] > 0:
            return maxNeg[0]*maxNeg[1]*maxPos[0]
        return maxPos[0]*maxPos[1]*maxPos[2]

    """
    Simple solution and more efficient
    
    nums.sort()
    return max(nums[0]*nums[1]*nums[-1],nums[-1]*nums[-2]*nums[-3])
    """


sol = Solution()
sol.maximumProduct([74,27,12,75,68,47,61,57,67,52])
