from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Average solution, beats 37% time and 82% memory
        nums = sorted(nums)
        for idx in range(len(nums)):
            if nums[idx] == nums[idx + 1]:
                return nums[idx]

    def findDuplicate2(self, nums: List[int]) -> int:
        # Tortoise and Hare algorithm - beats 68% time and 93% memory3
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


test_list = [1,2,3,2,4]
sol = Solution()
sol.findDuplicate2(test_list)