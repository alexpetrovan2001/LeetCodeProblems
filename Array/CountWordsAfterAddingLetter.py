from typing import List


class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        s = set()

        for w in startWords:
            s.add("".join(sorted(list(w))))

        ans = 0
        for w in targetWords:
            w = sorted(list(w))
            for i in range(len(w)):
                if "".join(w[:i] + w[i + 1:]) in s:
                    ans += 1
                    break

        return ans

sol = Solution()
sol.wordCount(["g","vf","ylpuk","nyf","gdj","j","fyqzg","sizec"], ["r","am","jg","umhjo","fov","lujy","b","uz","y"])
sol.wordCount(["ant","act","tack"], ["tack","act","acti"])