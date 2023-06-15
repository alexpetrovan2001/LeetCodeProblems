class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letterFreq = dict()
        if len(s) != len(t):
            return False
        for i in s :
            if i in letterFreq:
                letterFreq[i] += 1
            else:
                letterFreq[i] = 1
        for i in t:
            if i in letterFreq:
                letterFreq[i] -= 1
                if letterFreq[i] < 0:
                    return False
            else:
                return False
        return True