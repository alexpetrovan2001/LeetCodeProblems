# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # First solution, beats 64% time and 23% memory, without using BST property
        pathToP = self.pathToNode(root, p, [])
        pathToQ = self.pathToNode(root, q, [])

        if p in pathToQ:
            return p

        if q in pathToP:
            return q

        while len(pathToP) > len(pathToQ):
            node = pathToP.pop()
            if node == q:
                return node
        while len(pathToP) < len(pathToQ):
            node = pathToQ.pop()
            if node == p:
                return node
        while pathToP and pathToQ:
            parentP = pathToP.pop()
            parentQ = pathToQ.pop()

            if parentP == parentQ:
                return parentP

    def pathToNode(self, root, node, path):
        if root:
            path += [root]
            if root.val == node.val:
                return path
            if root.left:
                result = self.pathToNode(root.left, node, path)
                if result:
                    return result
                else:
                    path.pop()
            if root.right:
                result = self.pathToNode(root.right, node, path)
                if result:
                    return result
                else:
                    path.pop()
        return []

        def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            # Beats 53% time and 58% memory without using BST property
            def findPath(node, target):
                if not node:
                    return None
                if node == target:
                    return [node]

                left_path = findPath(node.left, target)
                if left_path:
                    left_path.insert(0, node)
                    return left_path

                right_path = findPath(node.right, target)
                if right_path:
                    right_path.insert(0, node)
                    return right_path

                return None

            path_to_p = findPath(root, p)
            path_to_q = findPath(root, q)

            ancestor = None

            for node_p, node_q in zip(path_to_p, path_to_q):
                if node_p == node_q:
                    ancestor = node_p
                else:
                    break

            return ancestor

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Beats 91% time and 89% memory but uses BST property
        if not root:
            return None

        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root



sol = Solution()

root = TreeNode(6)
p = TreeNode(2)
root.left = p
root.right = TreeNode(8)
root.left.left = TreeNode(0)
q = TreeNode(4)
root.left.right = q
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)

print(sol.lowestCommonAncestor(root, p, q).val)



