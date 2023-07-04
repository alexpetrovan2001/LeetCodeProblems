from typing import List


class Solution:
    # Beats 92 % runtime and 93% memory
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.generateParenthesisRec(n, n, "", result)
        return result

    def generateParenthesisRec(self, left: int, right: int, current: str, result: List[str]):
        if left == 0 and right == 0:
            result.append(current)
            return

        if left > 0:
            self.generateParenthesisRec(left - 1, right, current + "(", result)

        if right > left:
            self.generateParenthesisRec(left, right - 1, current + ")", result)

    def generateParenthesisWithStack(self, n: int) -> List[str]:

        # Stack implementation

        results = []
        stack = [("(", n - 1, n)]

        while stack:
            current, openings, closings = stack.pop()

            if openings == 0 and closings == 0:
                results.append(current)
            if openings > 0:
                stack.append((current + "(", openings - 1, closings))
            if closings > openings:
                stack.append((current + ")", openings, closings - 1))

        return results


sol = Solution()
print(sol.generateParenthesisWithStack(3))