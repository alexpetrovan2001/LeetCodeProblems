from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Similar solution to BTLevelOrderTraversal - Beats 66% time and 40% memory
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []

        levels = self.levelOrder(root)
        for level in levels:
            result.append(levels[-1])

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Average sol, beats 65% time and 66% memory
        q, sq, res, ans = [root], [], [], []

        while q:
            for node in q:
                res.append(node.val)
                if node.left:
                    sq.append(node.left)
                if node.right:
                    sq.append(node.right)
            ans.append(res)
            q = sq

        return ans
