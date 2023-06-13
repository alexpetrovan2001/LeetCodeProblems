from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mapList1 = dict()
        result = []
        minIndex = len(list1) + len(list2)
        for i in range(len(list1)):
            mapList1[list1[i]] = i
        for i in range(len(list2)):
            if list2[i] in mapList1:
                if i + mapList1[list2[i]] < minIndex:
                    result = [list2[i]]
                    minIndex = i + mapList1[list2[i]]
                elif i + mapList1[list2[i]] == minIndex:
                    result.append(list2[i])
        return result