from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    index1=0
    index2=0
    zeros_out = n
    while zeros_out > 0:
        nums1.pop()
        zeros_out-=1
    while index1<m and index2<n:
        if nums1[index1] > nums2[index2]:
            nums1.insert(index1, nums2[index2])
            index2+=1
            index1+=1
            m+=1
        else:
            index1+=1

    while index2<n:
        nums1.append(nums2[index2])
        index2+=1
    print(nums1)

merge([4,0,0,0,0], 1, [1,2,3,5], 4)