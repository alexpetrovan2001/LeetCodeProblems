from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Beats 98% time and 90% memory
        noFound = dict()
        for i in range(len(numbers)):
            if numbers[i] not in noFound:
                noFound[numbers[i]] = i+1
            if target-numbers[i] in noFound:
                index1 = i + 1
                index2 = noFound[target-numbers[i]]
                if index1 != index2:
                    if index1 > index2:
                        return [index2, index1]
                    else:
                        return [index1, index2]

sol = Solution()
sol.twoSum([2,3,4], 6)