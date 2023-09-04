from typing import List
import heapq

class Solution:
    # Quick solution with 94% time and 63% memory - can be improved in terms of memory, should have stored only k elements in the heap.
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        noPoints = len(points)
        if k == noPoints:
            return points

        distances = []
        mapFromDistanceToPoints = {}

        for i in range(noPoints):
            x, y = points[i]
            diff = x*x + y*y
            heapq.heappush(distances, diff)
            if diff not in mapFromDistanceToPoints:
                mapFromDistanceToPoints[diff] = [points[i]]
            else:
                mapFromDistanceToPoints[diff].append(points[i])

        ans = []

        while k > 0:
            ans.append(mapFromDistanceToPoints[heapq.heappop(distances)].pop())
            k -= 1

        return ans


