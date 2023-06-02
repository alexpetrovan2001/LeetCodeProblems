from typing import List

def removeDuplicates(nums: List[int]) -> int:
    lastNr = None
    index = 0
    while index < len(nums):
        if nums[index] == lastNr:
            lastNr = nums[index]
            nums.pop(index)
        else:
            lastNr = nums[index]
            index+=1
    return nums

print(removeDuplicates([1,1,2,2,3,3,4]))