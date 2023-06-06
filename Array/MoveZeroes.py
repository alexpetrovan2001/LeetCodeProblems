import queue
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroPositions = queue.Queue()
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroPositions.put(i)
            else:
                if not zeroPositions.empty():
                    index = zeroPositions.get()
                    zeroPositions.put(i)
                    nums[index] = nums[i]
                    nums[i] = 0


    def moveZeroes2(self, nums: List[int]) -> None:
        # This has the best results in terms of memory and runtime  
        noZeroes=0
        i=0
        while i < len(nums)-noZeroes:
            if nums[i] == 0:
                nums.pop(i)
                noZeroes+=1
                nums.append(0)
            else: i+=1


    def moveZeroes3(self, nums: List[int]) -> None:
        zero = nums.count(0)
        if zero == 0:
            return
        nums = list(filter(lambda a: a !=0, nums))
        while zero > 0:
            nums.append(0)
            zero-=1



sol = Solution()
sol.moveZeroes3([0,1,0,3,12])