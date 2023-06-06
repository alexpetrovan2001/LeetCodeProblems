from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        i = 0;
        result=[]
        if nums[0] + len(nums) -1 == nums[len(nums)-1] and len(nums) > 1:
            string = str(nums[0])+ "->" + str(nums[len(nums)-1])
            result.append(string)
            return result
        while i < len(nums):
            string=str(nums[i])
            isRange = False
            while i+1 < len(nums) and nums[i+1] == nums[i]+1:
                isRange = True
                i+=1
            if isRange == True:
                string = string + "->" + str(nums[i])
            result.append(string)
            i+=1
        return result