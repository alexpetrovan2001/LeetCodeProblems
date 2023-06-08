from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        firstRow = "qwertyuiop"
        secondRow = "asdfghjkl"
        thirdRow = "zxcvbnm"
        map = dict()
        for i in firstRow:
            map[i] = 1
        for i in secondRow:
            map[i] = 2
        for i in thirdRow:
            map[i] = 3
        ans = []
        for i in words:
            if len(i) == 1:
                ans.append(i)
            else:
                word = i.lower()
                for j in range(len(i)):
                    if j == len(i)-1 or map[word[j]] != map[word[j+1]]:
                        break
                if j == len(i)-1:
                    ans.append(i)
        return ans

sol = Solution()
sol.findWords(["abdfs","cccd","a","qwwewm"])