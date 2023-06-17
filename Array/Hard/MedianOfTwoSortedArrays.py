import queue
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0
        j = 0
        m = len(nums1)
        n = len(nums2)


        if not nums1:
            return nums2[(n-1)//2] if n % 2 == 1 else (nums2[(n-1)//2] + nums2[n//2]) / 2

        if not nums2:
            return nums1[(m-1)//2] if m % 2 == 1 else (nums1[(m-1)//2] + nums1[m//2]) / 2

        q = queue.LifoQueue()

        while i < m and j < n and i + j <= (m + n) // 2:
            if nums1[i] < nums2[j]:
                q.put(nums1[i])
                i += 1
            else:
                q.put(nums2[j])
                j += 1
        if i+j <= (m+n) // 2:
            if i < m:
                while i + j <= (m+n) // 2:
                    q.put(nums1[i])
                    i+=1
            elif j < n:
                while i + j <= (m+n) // 2:
                    q.put(nums2[j])
                    j+=1
        if (m+n) % 2 == 0:
            return (q.get()+q.get()) / 2
        else :
            return q.get()


sol = Solution()
print(sol.findMedianSortedArrays([1,2], [3,4]))
