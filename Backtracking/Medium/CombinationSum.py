from typing import List

class Solution:
    # Beats 98% time and 64% memory.
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backTrack(start, target, path, res):
            if target == 0:
                res.append(path)
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                backTrack(i, target - candidates[i], path + [candidates[i]], res)

        candidates.sort()
        res = []
        backTrack(0, target, [], res)
        print(res)
        return res

sol = Solution()
sol.combinationSum([2,3,4,5], 7)