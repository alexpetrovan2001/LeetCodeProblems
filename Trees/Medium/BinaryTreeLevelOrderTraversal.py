from typing import List, Optional
from queue import Queue
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # First solution; Beats 28% time and 66% memory
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result

        q = Queue()
        q.put((root, 0))

        level_map = {}

        while not q.empty():
            cur_node, level = q.get()
            if level not in level_map:
                level_map[level] = [cur_node.val]
            else:
                level_map[level].append(cur_node.val)
            if cur_node.left:
                q.put((cur_node.left, level+1))
            if cur_node.right:
                q.put((cur_node.right, level+1))

        for value in level_map.values():
            result.append(value)

        return result

    def levelOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Better solution : beats 90% time and 18% memory
        result = []
        q = []

        if not root:
            return result

        q.append(root)
        q.append(0)
        length = 0

        while q:
            node, level = q.pop(0), q.pop(0)
            if level == length:
                length += 1
                result.append([node.val])
            else:
                result[level].append(node.val)
            if node.left:
                q.append(node.left)
                q.append(leve+1)
            if node.right:
                q.append(node.right)
                q.append(level+1)
        return result

    def levelOrder3(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Average sol, beats 65% time and 66% memory
        if not root:
            return []

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