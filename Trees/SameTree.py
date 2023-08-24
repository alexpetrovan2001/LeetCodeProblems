# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Recurrsive solution - beats 99% time and 55% memory
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.checkTree(p, q)

    def checkTree(self, p, q):
        if not p and q:
            return False
        if not q and p:
            return False
        if not p and not q:
            return True
        if p.val != q.val:
            return False
        return self.checkTree(p.left, q.left) and self.checkTree(p.right, q.right)


sol = Solution()

leftChild1 = TreeNode(2, None, None)
rightChild1 = TreeNode(1, None, None)
firstHead = TreeNode(1, leftChild1, rightChild1)

leftChild2 = TreeNode(1, None, None)
rightChild2 = TreeNode(2, None, None)
secondHead = TreeNode(1, leftChild2, rightChild2)

sol.isSameTree(firstHead, secondHead)
