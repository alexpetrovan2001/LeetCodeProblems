from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            result = [[1]]
            return result
        elif numRows >= 2:
            result = [[1], [1, 1]]
            while len(result) < numRows:
                listToAppend = result[len(result) - 1].copy()
                result.append(self.modifyList(listToAppend))
            return result

    def modifyList(self, listToModify: List[int]) -> List[int]:
        lengthOfList = len(listToModify)
        nrAppended = False
        if lengthOfList % 2 != 0:
            nrAppended = True
            listToModify.insert(lengthOfList//2, listToModify[lengthOfList//2])
            lengthOfList+=1
        startIndex = lengthOfList // 2 - 1
        endIndex = lengthOfList // 2
        if not nrAppended:
            endIndex = lengthOfList // 2 + 1
            listToModify.insert(startIndex + 1, listToModify[startIndex + 1] + listToModify[startIndex])
            lengthOfList += 1
        while endIndex < (lengthOfList - 1) and startIndex > 0:
            listToModify[endIndex] = listToModify[endIndex] + listToModify[endIndex + 1]
            endIndex += 1
            listToModify[startIndex] = listToModify[startIndex] + listToModify[startIndex - 1]
            startIndex -= 1
        return listToModify


"""
list = [1,2,1] -> [1,3,3,1]
list = [1,3,3,1] -> [1,4,6,4,1]
list = [1,4,6,4,1] -> [1,5,10,10,5,1]
"""

sol = Solution()
print(sol.generate(10))
