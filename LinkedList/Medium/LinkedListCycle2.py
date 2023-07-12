# Definition for singly-linked list.

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # Floyd's Tortoise and Hare algorithm (62% time and 69% memory)
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return None
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        if fast is None or fast.next is None:
            return None
        else:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow

    def detectCycle2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Improved first algorithm (96% time and 91% memory)
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:  # Cycle detected
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow  # Node where the cycle begins

        return None  # No cycle found
