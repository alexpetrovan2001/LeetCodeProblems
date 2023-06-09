from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sortedScores = sorted(score, reverse=True)
        map = dict()
        if len(sortedScores) >= 1:
            map[sortedScores[0]] = "Gold Medal"
            if len(sortedScores) >= 2:
                map[sortedScores[1]] = "Silver Medal"
                if len(sortedScores) >= 3:
                    map[sortedScores[2]] = "Bronze Medal"
        for i in range(3, len(sortedScores)):
            map[sortedScores[i]] = i+1
        result = []
        for i in score:
            result.append(map[i])
        return result

sol = Solution()
sol.findRelativeRanks([10,3,8,9,4])
