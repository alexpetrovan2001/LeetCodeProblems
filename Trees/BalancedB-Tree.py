from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Beats 96% time and 78% space
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.checkBalance(root) != -1

    def checkBalance(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.checkBalance(root.left)
        right = self.checkBalance(root.right)

        # If any subtree is unbalanced, return -1 to indicate unbalance
        if left == -1 or right == -1 or abs(left - right) >= 2:
            return -1

        # Return the height of the current node's subtree
        return max(left, right) + 1

sol = Solution()
node3left = TreeNode(4, None, None)
node2left = TreeNode(3, None, None)
node2right = TreeNode(3, node3left, None)
node1left = TreeNode(2, None, None)
node1right = TreeNode(2, node2left, node2right)
tree = TreeNode(1, node1left, node1right)
print(sol.isBalanced(tree))
