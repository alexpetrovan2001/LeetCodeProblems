class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Beats 62% time and 79% memory
        left = 0
        right = len(s)-1
        s = s.lower()
        while left < right:
            while left<=right and not s[left].isalnum():
                left+=1
            while right>=left and not s[right].isalnum():
                right-=1
            if left<right and s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True

sol = Solution()
sol.isPalindrome(" ")