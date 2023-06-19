import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nrFreq = dict()

        for i in nums:
            if i not in nrFreq:
                nrFreq[i] = 0
            nrFreq[i] += 1

        sorted_dict = sorted(nrFreq.items(), key=lambda x: x[1], reverse=True)

        result = [item[0] for item in sorted_dict]

        return result[:k]

    def topKFrequentImproved(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        freq_heap = []

        for num, freq in freq.items():
            heapq.heappush(freq_heap, (freq,num))
            if len(freq_heap) > k:
                heapq.heappop(freq_heap)

        sol = [num for freq, num in freq_heap]

        return sol

sol = Solution()
print(sol.topKFrequentImproved([4,1,-1,2,-1,2,3], 2))
