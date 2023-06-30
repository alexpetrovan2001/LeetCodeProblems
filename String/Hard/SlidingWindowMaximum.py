from typing import List

class Solution:
    # Beats 95 % time and 11.5 % memory
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q, res = deque(), []  # save index in q (decreasing order)
        for r in range(len(nums)):
            # remove from the right side all items less than current
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            # while window not full (size =k) do nothing
            if r + 1 < k: continue
            # if most left index out of window [r+1-k, r] we need remove it
            if q[0] < r + 1 - k:
                q.popleft()
            # because deque is decreasing the left value is highest
            res.append(nums[q[0]])

        return res

sol = Solution()
print(sol.maxSlidingWindow([1, -1], 1))

