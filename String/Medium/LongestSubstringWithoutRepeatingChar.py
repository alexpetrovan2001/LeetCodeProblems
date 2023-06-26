class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Rudimentary sol
        n = len(s)
        i = 0
        result = 0
        while i < n:
            my_dict = {}
            j = i
            while j < n and s[j] not in my_dict:
                my_dict[s[j]] = j
                j+=1
            result = max(result, (j-i))
            if j == n:
                return result
            else:
                i = my_dict[s[j]] + 1
        return result

    def lengthOfLongestSubstring2(self, s: str) -> int:
        # Excellent time, bad memory
        n = len(s)
        chars = set()
        maxLen = 0
        i = 0
        j = 0
        while j < n and i < n:
            if s[j] not in chars:
                chars.add(s[j])
                maxLen = max(maxLen, j-i+1)
            else:
                while s[j] in chars:
                    chars.remove(s[i])
                    i+=1
                chars.add(s[j])
            j+=1
        return maxLen

    def lengthOfLongestSubstring3(self, s: str) -> int:
        # Medium time, excellent memory
        if not s:
            return 0
        ans = 1
        temp = ''

        for right in range(len(s)):
            while s[right] in temp:
                temp = temp[1:]

            temp += s[right]
            ans = max(ans, len(temp))

        return ans


sol = Solution()
print(sol.lengthOfLongestSubstring2("abcabcbb"))