from typing import List


class Solution:

    # Beats 75% time and 70% memory

    def search(self, nums: List[int], target: int) -> int:
        pos = -1
        output = -1
        while nums:
            mid = len(nums) // 2
            if nums[mid] == target:
                if output == -1:
                    output = mid
                else:
                    output += mid
                pos = output
                break
            elif nums[mid] < target:
                output = mid + 1 if output == -1 else output + mid + 1
                nums = nums[mid + 1:]
            else:
                nums = nums[:mid]

        return pos

sol = Solution()
print(sol.search([-1,0,3,5,9,12], 12))