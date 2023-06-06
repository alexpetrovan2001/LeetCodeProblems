from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for i in nums1:
            if i in nums2 and i not in result:
                result.append(i)
        return result

    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Best so far

        nums1 = sorted(set(nums1))
        nums2 = sorted(set(nums2))
        result = []
        if len(nums1) == 0 or len(nums2) == 0 or (nums1[len(nums1) - 1] < nums2[0]) or (
                nums1[0] > nums2[len(nums2) - 1]):
            return result
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return result

sol = Solution()
sol.intersection2([2,2],[1,2,2,1])



