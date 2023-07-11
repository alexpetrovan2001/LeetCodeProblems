# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Iterative solution
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        newHead = ListNode(head.val)
        while head.next is not None:
            newHead = ListNode(head.next.val, newHead)
            head = head.next
        return newHead

    def reverseListRecurisvely(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Recursive solution
        if head is None:
            return None
        if head.next is None:
            return head
        newHead = self.reverseListRecurisvely(head.next)
        head.next.next = head
        head.next = None
        return newHead

sol = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(sol.reverseListRecurisvely(head))