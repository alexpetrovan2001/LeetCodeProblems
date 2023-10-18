import queue
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Beats 47% time and 21% memory -> this is compared with result that are not in O(log(m+n))
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x, y = len(nums1), len(nums2)
        low, high = 0, x

        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX

            leftMaxX = nums1[partitionX - 1] if partitionX != 0 else float('-inf')
            rightMinX = nums1[partitionX] if partitionX != x else float('inf')

            leftMaxY = nums2[partitionY - 1] if partitionY != 0 else float('-inf')
            rightMinY = nums2[partitionY] if partitionY != y else float('inf')

            if leftMaxX <= rightMinY and leftMaxY <= rightMinX:
                if (x + y) % 2 == 0:
                    return (max(leftMaxY, leftMaxX) + min(rightMinY, rightMinX)) / 2
                else:
                    return max(leftMaxY, leftMaxX)
            elif leftMaxX > rightMinY:
                high = partitionX - 1
            else:
                low = partitionX + 1

    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        # Beats 32% time and 99.54% memory but not in o(log(m+n))
        arr = []

        while True:
            if nums1 and nums2:
                if nums1[0] < nums2[0]:
                    arr.append(nums1.pop(0))
                else:
                    arr.append(nums2.pop(0))
            elif nums2:
                while nums2:
                    arr.append(nums2.pop(0))
            elif nums1:
                while nums1:
                    arr.append(nums1.pop(0))
            else:
                break

        n = len(arr)
        if n % 2 == 0:
            return (arr[n//2] + arr[(n//2) - 1]) / 2
        else:
            return arr[n//2]


sol = Solution()
print(sol.findMedianSortedArrays([1, 8], [2, 6, 9]))