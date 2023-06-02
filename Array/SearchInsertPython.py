from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    start=0
    end=len(nums)-1
    lastPos=0
    pos=0
    if target>nums[end]:
        return end+1
    if target<nums[0]:
        return 0
    while True:
        lastPos=pos
        pos=(end+start)//2
        if lastPos+1 == pos and nums[lastPos]<target and nums[pos]>target:
            return pos
        if nums[pos] == target or pos==target-1:
            return pos
        elif nums[pos] < target:
            start=pos+1
        else :
            end=pos

print(searchInsert([1,2,4,7], 3))
