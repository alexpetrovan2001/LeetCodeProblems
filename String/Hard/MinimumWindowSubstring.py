class Solution:
    # Beats 99.3 percent in time and 25.47 in memory
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        freq = {}
        for c in t:
            if c not in freq:
                freq[c] = 1
            else:
                freq[c] += 1
        if n < m:
            return ""
        elif n == m:
            for i in s:
                if i not in freq or freq[i] == 0:
                    return ""
                else:
                    freq[i] -= 1
            return s

        left, right = 0, 0
        minLeft, minRight = 0, n
        lettersFound = 0
        while right < n:
            while lettersFound < m and right < n:
                if s[right] in freq:
                    if freq[s[right]] > 0:
                        lettersFound += 1
                    freq[s[right]] -= 1
                    right+=1
                else:
                    right+=1
            while lettersFound == m:
                if s[left] in freq:
                    if freq[s[left]] == 0:
                        if right - left - 1 < minRight - minLeft:
                            minLeft, minRight = left, right - 1
                        lettersFound -= 1
                    freq[s[left]] += 1
                left+=1
        return s[minLeft:minRight] if (minRight != n or minLeft != 0) else ""



sol = Solution()
sol.minWindow("ab", "A")


