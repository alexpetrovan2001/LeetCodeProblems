from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Improved version of permute2 -> 94% time and 48% memory
        def backtrack(nums, path, res):
            if not nums:
                res.append(path)
                return
            for i in range(0, len(nums)):
                #temp_nums = [num for num in nums]
                #temp_nums.pop(i)
                if nums:
                    backtrack(nums[:i] + nums[i+1:], path + [nums[i]], res)

        res = []
        backtrack(nums, [], res)
        return res

    def permute2(self, nums: List[int]) -> List[List[int]]:
        # First version of the problem -> 76% time and 48% memory
        def backtrack(nums, path, res):
            if not nums:
                res.append(path)
                return
            for i in range(0, len(nums)):
                temp_nums = [num for num in nums]
                temp_nums.pop(i)
                backtrack(temp_nums, path + [nums[i]], res)

        res = []
        backtrack(nums, [], res)
        return res

sol = Solution()
print(sol.permute([1,2,3]))