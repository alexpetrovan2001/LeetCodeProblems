from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        m = len(nums1)
        n = len(nums2)
        if m == 0:
            return ans
        if n == 0:
            return ans
        firstIndexes = dict()
        for i in range(n):
            firstIndexes[nums2[i]] = i
        for i in nums1:
            j = firstIndexes[i] + 1
            while j < n and nums2[j] <= i:
                j += 1
            if j < n:
                ans.append(nums2[j])
            else:
                ans.append(-1)
        return ans

sol = Solution()
sol.nextGreaterElement([4,1,2], [1,3,4,2])
