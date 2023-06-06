from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq = dict()
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = i
            else:
                if abs(i-freq[nums[i]]) <= k:
                    return True
                else:
                    freq[nums[i]] = i
        return False