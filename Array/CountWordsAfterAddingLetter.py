from typing import List


class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        startWords = sorted(startWords, key=len)
        targetWords = sorted(targetWords, key=len)
        i, j, result = 0, 0, 0

        # iterate for every word from startWords to all words that can match len in targetWords
        while i < len(startWords) and j < len(targetWords):
            if len(startWords[i]) + 1 < len(targetWords[j]):
                i += 1
            elif len(startWords[i]) + 1 == len(targetWords[j]):
                if self.compareWords(startWords[i], targetWords[j]):
                    result += 1
                i += 1
                j += 1
            else :
                j += 1
        return result

    def compareWords(self, word1, word2):
        for i in word1:
            if i not in word2:
                return False
        return True

sol = Solution()
sol.wordCount(["ant","act","tack"], ["tack","act","acti"])