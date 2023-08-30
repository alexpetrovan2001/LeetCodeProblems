from typing import Optional
import queue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Poor time results: 5% time and 98% memory
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def compareTrees(rootToVerify):
            nodesToVisit1 = queue.Queue()
            nodesToVisit2 = queue.Queue()

            if rootToVerify:
                nodesToVisit1.put(rootToVerify)
            if subRoot:
                nodesToVisit2.put(subRoot)

            while not nodesToVisit1.empty() and not nodesToVisit2.empty():
                root1 = nodesToVisit1.get()
                root2 = nodesToVisit2.get()

                if root1.val == root2.val:
                    if root2.left and root1.left:
                        nodesToVisit2.put(root2.left)
                        nodesToVisit1.put(root1.left)
                    elif not root2.left and not root1.left:
                        pass
                    else:
                        return False
                    if root2.right and root1.right:
                        nodesToVisit2.put(root2.right)
                        nodesToVisit1.put(root1.right)
                    elif not root2.right and not root1.right:
                        pass
                    else:
                        return False
                else:
                    return False

            if not nodesToVisit2.empty():
                return False
            else:
                return True

        nodesToVisit = queue.Queue()
        nodesToVisit.put(root)

        while not nodesToVisit.empty():
            currNode = nodesToVisit.get()

            if currNode.val == subRoot.val:
                if compareTrees(currNode):
                    return True

            if currNode.left:
                nodesToVisit.put(currNode.left)
            if currNode.right:
                nodesToVisit.put(currNode.right)

        return False

    def isSubtree2(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Improvement for 1: 45% time and 92% memory
        q = queue.Queue()
        q.put(root)
        visitedNodes = {}

        def checkTrees2(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val != root2.val:
                return False
            return checkTrees2(root1.left, root2.left) and checkTrees2(root1.right, root2.right)

        while not q.empty():
            curRoot = q.get()
            if curRoot.left:
                    q.put(curRoot.left)
            if curRoot.right:
                q.put(curRoot.right)
            if curRoot.val == subRoot.val:
                visitedNodes[curRoot] = True
                if checkTrees2(curRoot, subRoot):
                    return True

        return False

sol = Solution()

root = TreeNode(1)
root.left = TreeNode(1)
# root.right = TreeNode(5)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(2)

subRoot = TreeNode(1)
# subRoot.left = TreeNode(1)
# subRoot.right = TreeNode(2)

sol.isSubtree3(root, subRoot)
