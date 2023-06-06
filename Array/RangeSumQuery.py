from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.numbers = nums

    def sumRange(self, left: int, right: int) -> int:
        # This is much better
        if left>right:
            return 0
        else:
            nums = self.numbers[left:right+1]
            return sum(nums)

    def sumRange2(self, left: int, right: int) -> int:
        sum = 0
        while left <= right:
            sum += self.numbers[left]
            left+=1
        return sum

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)