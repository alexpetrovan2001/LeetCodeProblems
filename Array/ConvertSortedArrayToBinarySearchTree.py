from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        length = len(nums)
        if length == 1:
            head = TreeNode(nums[0])
            return head
        elif length == 0:
            return None
        else:
            middleNr = nums[length // 2]
            head = TreeNode(middleNr)
            if length // 2 - 1 >= 0:
                head.left = self.sortedArrayToBST(nums[:length // 2])
            if length // 2 + 1 < length:
                head.right = self.sortedArrayToBST(nums[(length // 2) + 1:])
            return head

sol = Solution()
sol.sortedArrayToBST([5,9])

"""
[1,2,3,4] -> len = 4, len/2=2, nums[len/2]=3
-> left = [1,2] = nums[:len/2], right=[4] = nums[len/2+1:]

[1,2,3,4,5] -> len = 5, len/2=2, nums[len/2]=3
-> left = [1,2] = nums[:len/2]

"""