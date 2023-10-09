from typing import List
import heapq
from queue import PriorityQueue

class Solution:
    # Average solution with heap, beats 5% time and 99.6% memory
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        while k > 0:
            num = nums.pop(0)
            heapq.heappush(min_heap, num)
            k -= 1
        for num in nums:
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)
        return min_heap[0]

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        # Improved version, beats 45% time and 89% memory
        min_heap = []
        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            else:
                if num > min_heap[0]:
                    heapq.heappushpop(min_heap, num)
        return min_heap[0]



sol = Solution()
sol.findKthLargest2([1,2,3,4,5], 2)