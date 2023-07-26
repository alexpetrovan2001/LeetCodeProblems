# Definition for a binary tree node
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Beats 99.8% time and only 13% memory
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            depth = max(self.calculateDepth(root.left, 1), self.calculateDepth(root.right, 1))
            return depth
        return 0

    def calculateDepth(self, root, cur_max) -> int:
        if root:
            return max(self.calculateDepth(root.left, cur_max+1), self.calculateDepth(root.right, cur_max+1))
        return cur_max


    # Beats 80% time and 76% memory
    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        if root:
            return max(self.maxDepth2(root.left) + 1, self.maxDepth2(root.right) +1)
        return 0

sol = Solution()
node2left = TreeNode(3, None, None)
node2right = TreeNode(3, None, None)
node1left = TreeNode(2, None, None)
node1right = TreeNode(2, node2left, node2right)
tree = TreeNode(1, node1left, node1right)
print(sol.maxDepth2(tree))
