from typing import List


class Solution:

    # Beats 85% runtime and 60% memory

    def evalRPN(self, tokens: List[str]) -> int:
        nrStack = []
        for token in tokens:
            if token == "+":
                nrStack.append(nrStack.pop() + nrStack.pop())
            elif token == "-":
                op2 = int(nrStack.pop())
                op1 = int(nrStack.pop())
                nrStack.append(op1 - op2)
            elif token == "*":
                nrStack.append(nrStack.pop() * nrStack.pop())
            elif token == "/":
                op2 = int(nrStack.pop())
                op1 = int(nrStack.pop())
                nrStack.append(int(op1 / op2))
            else:
                nrStack.append(int(token))
        return nrStack[0]

sol = Solution()
print(sol.evalRPN(["4","13","5","/","+"]))