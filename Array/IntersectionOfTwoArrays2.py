from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1=sorted(nums1)
        nums2=sorted(nums2)
        i = 0
        j = 0
        result = []
        if len(nums1) == 0 or len(nums2) == 0 or (nums1[len(nums1) - 1] < nums2[0]) or (
                nums1[0] > nums2[len(nums2) - 1]):
            return result
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
        return result

    def intersect2(self, nums1: List[int], nums2: List[int]) -> List[int]:

        #This is the best so far

        numDict = dict()
        result = []
        for i in nums1:
            if i not in numDict:
                numDict[i] = 1
            else:
                numDict[i] += 1
        for j in nums2:
            if j in numDict and numDict[j] > 0:
                result.append(j)
                numDict[j] -= 1
        return result