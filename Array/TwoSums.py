from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    nrDict = {}
    result = []
    for i in range(len(nums)):
        curr = nums[i]
        if curr < target:
            if curr in nrDict:
                result = [nrDict[curr], i]
                return result
            else:
                nrDict[target - curr] = i


print(twoSum([3,2,4], 6))
