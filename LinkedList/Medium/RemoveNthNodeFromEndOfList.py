# Definition for singly-linked list.

from typing import Optional

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Beats 94% of time complexity and 70% memory
    def removeNthFromEnd(self, head: Optional[Node], n: int) -> Optional[Node]:
        simpleList = []
        curNode = head
        while curNode:
            simpleList.append(curNode)
            curNode = curNode.next
        length = len(simpleList)
        if length == 1:
            return []
        n = length-n
        if n == length-1:
            simpleList[n-1].next = none
        elif n == 0:
            head = head.next
        else:
            simpleList[n-1].next = simpleList[n+1]
        return head

sol = Solution()
node4 = Node(4, None)
node3 = Node(3, node4)
node2 = Node(2, node3)
node1 = Node(1, node2)
sol.removeNthFromEnd(node1, 2)