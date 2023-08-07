import heapq
from typing import List

class Solution:
    # Beats 79% time and 71% memory
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [stone * -1 for stone in stones]

        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            first = heapq.heappop(max_heap) * -1
            second = heapq.heappop(max_heap) * -1

            if first != second :
                heapq.heappush(max_heap, (first-second) * -1 )

        return max_heap[0] * -1 if max_heap else 0