from typing import List


class Solution:

    # Beats 95 % runtime and 81 % memory

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                result[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return result

sol = Solution()
sol.dailyTemperatures([73,74,75,71,69,72,76,73])
