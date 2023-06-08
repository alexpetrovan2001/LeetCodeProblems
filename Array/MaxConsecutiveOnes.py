from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxSeq = 0
        curSeq = 0
        for i in nums:
            if i == 1:
                curSeq += 1
            else :
                maxSeq = max(curSeq, maxSeq)
                curSeq = 0
        maxSeq = max(curSeq, maxSeq)
        return maxSeq


sol = Solution()
sol.findMaxConsecutiveOnes([1,1,0,1,1,1])