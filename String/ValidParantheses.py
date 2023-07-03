import collections

class Solution:
    # Beats 93% in time but only 15 % in memory
    def isValid(self, s: str) -> bool:
        stackToClose = collections.deque()
        for i in s:
            if i == "(":
                stackToClose.append(")")
            elif i == "{":
                stackToClose.append("}")
            elif i == "[":
                stackToClose.append("]")
            else:
                if not stackToClose or stackToClose.pop() != i:
                    return False
        return True if not stackToClose else False

sol = Solution()
sol.isValid("()[]{}")
