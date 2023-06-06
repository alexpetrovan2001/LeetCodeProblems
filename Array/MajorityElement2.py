from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        numbers = dict()
        result = []
        n = len(nums)
        for i in nums:
            if i in numbers and i not in result:
                numbers[i] += 1
            else:
                if i not in result:
                    numbers[i] = 1
            if numbers[i] > n // 3 and i not in result:
                result.append(i)
        return result

    def majorityElementMemoryMoreEfficient(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        target = n//3
        i = 0
        if len(nums) == 1:
            return nums
        if len(nums) == 2:
            return nums if nums[0] != nums[1] else nums[:1]
        while i < n:
            if i+target < n and nums[i+target] == nums[i]:
                while i+1 < n and nums[i+1] == nums[i]:
                    nums.pop(i)
                    n-=1
                i+=1
            else:
                nums.pop(i)
                n-=1
        return nums
