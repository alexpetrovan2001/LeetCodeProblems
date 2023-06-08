from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        result = 0
        for i in range(len(timeSeries) - 1):
            if timeSeries[i] + duration - 1 < timeSeries[i + 1]:
                result += duration
            else:
                result += timeSeries[i + 1] - timeSeries[i]
        return result + duration

    def findPoisonedDuration2(self, timeSeries: List[int], duration: int) -> int:
        # More memory efficient
        return duration + sum(min(timeSeries[i + 1] - timeSeries[i], duration) for i in range(len(timeSeries) - 1))