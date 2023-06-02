from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            result = [1,1]
            while rowIndex >= len(result):
                self.modifyList(result)
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

sol = Solution()
sol.getRow(3)