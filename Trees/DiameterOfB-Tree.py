# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # 86% time and 76% memory
        self.max_diameter = 0

        self.calculate_depth(root)

        return self.max_diameter

    def calculate_depth(self, node: TreeNode) -> int:
        if not node:
            return 0

        left_depth = self.calculate_depth(node.left)
        right_depth = self.calculate_depth(node.right)

        current_diameter = left_depth + right_depth

        self.max_diameter = max(self.max_diameter, current_diameter)

        return max(left_depth, right_depth) + 1