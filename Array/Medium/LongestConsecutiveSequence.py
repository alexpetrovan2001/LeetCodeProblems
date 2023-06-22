from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Beats 57% time and 13% mem
        noEntries = dict()
        for i in nums:
            if i not in noEntries:
                noEntries[i] = True
        result = 1
        for i in nums:
            cur = 1
            left = i
            right = i
            if i in noEntries:
                del (noEntries[i])
            while right+1 in noEntries:
                cur+=1
                right=right+1
                del(noEntries[right])
            while left-1 in noEntries:
                cur+=1
                left -=1
                del(noEntries[left])
            result = max(result,cur)
            if len(noEntries) == 0:
                return result
        return result

sol = Solution()
sol.longestConsecutive2([0,3,7,2,5,8,4,6,0,1])