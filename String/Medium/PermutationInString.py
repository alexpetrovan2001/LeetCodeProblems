class Solution:
    # Beats 80 percent time and 20 memory. Sliding window approach
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or not s2:
            return False
        freq = {}
        for c in s1:
            if c not in freq:
                freq[c] = 1
            else:
                freq[c] += 1
        left, right = 0, 0
        n = len(s2)
        m = len(s1)
        while right < n:
            if s2[left] in freq:
                while right < n and s2[right] in freq and freq[s2[right]] > 0:
                    freq[s2[right]] -= 1
                    right += 1
                if right - left == m:
                    return True
                else:
                    freq[s2[left]] += 1
                    left += 1
            else:
                left += 1
                right += 1
        return False

sol = Solution()
sol.checkInclusion("ab", "eidboaoo")



