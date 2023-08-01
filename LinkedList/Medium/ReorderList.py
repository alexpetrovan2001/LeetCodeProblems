from typing import Optional

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Beats 95% time and 18% memory
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or head.next is None:
            return head

        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        prev, curr = None, slow.next
        slow.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        firstHalf, secondHalf = head, prev
        while secondHalf:
            temp1, temp2 = firstHalf.next, secondHalf.next
            firstHalf.next = secondHalf
            if secondHalf!= temp1:
                secondHalf.next = temp1
            firstHalf, secondHalf = temp1, temp2

        return None

sol = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
sol.reorderList(head)