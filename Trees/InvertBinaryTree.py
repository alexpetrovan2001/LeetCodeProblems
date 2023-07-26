# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Beats 55% time and 72% memory
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            child1 = root.left
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(child1)
        return root