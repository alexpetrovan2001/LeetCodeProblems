from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        count = 0
        for i in s:
            if len(g) > 0 and i >= g[0]:
                while len(g) > 0 and i < g[0]:
                    g.pop(0)
                if len(g) == 0:
                    return count
                else:
                    count+=1
                    g.pop(0)
            else:
                pass
        return count

    def findContentChildren2(self, g: List[int], s: List[int]) -> int:
        # The best so far
        count = 0
        g = sorted(g)
        s = sorted(s)
        i = 0
        j = 0
        if len(g) == 0 or len(s) == 0 or g[0] > s[len(s) - 1]:
            return count
        while len(s) > j and len(g) > i:
            if s[j] >= g[i]:
                count += 1
                i += 1
                j += 1
            elif s[j] <= g[i]:
                j += 1
            else:
                i += 1
        return count


sol = Solution()
sol.findContentChildren([1,2,3],[1,1])