from typing import List

class Solution:
    # Beats 53% time and 33% memory -> avg sol
    def search(self, nums: List[int], target: int) -> int:
        # nums = [4, 5, 6, 7, 0, 1, 2]
        # nums = [5, 6, 0, 1, 2, 3, 4]
        index = 0
        while nums:
            n = len(nums)
            if n == 1 and nums[0] != target:
                return -1
            if nums[n//2] == target:
                return index + n//2
            elif target < nums[n//2]:
                if target < nums[0]:
                    if nums[0] < nums[n//2]:
                        index += n//2
                        nums = nums[n//2:]
                    else:
                        nums = nums[:n//2]
                elif target > nums[0]:
                    nums = nums[:n//2]
                else:
                    return index
            else:  # target > nums[//2]
                if target > nums[-1]:
                    if nums[-1] < nums[n//2]:
                        nums = nums[n//2:]
                        index += n//2
                    else:
                        nums = nums[:n//2]
                elif target < nums[-1]:
                    nums = nums[n//2:]
                    index += n//2
                else:
                    return index + n - 1

    def search2(self, nums: List[int], target: int) -> int:
        # Improved solution that beats 74% time and 92% memory
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1


sol = Solution()
array = [3, 1]
target = 1
print(sol.search2(array, target))