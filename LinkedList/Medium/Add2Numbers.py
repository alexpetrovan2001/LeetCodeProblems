from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Good solution, beats 92% time and 62% memory
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        digits = []
        carry = 0
        while l1 and l2:
            carry, sum = divmod(l1.val + l2.val + carry, 10)
            digits.append(sum)
            l1, l2 = l1.next, l2.next
        while l1:
            carry, sum = divmod(l1.val + carry, 10)
            digits.append(sum)
            l1 = l1.next
        while l2:
            carry, sum = divmod(l2.val + carry, 10)
            digits.append(sum)
            l2 = l2.next
        digits.append(carry) if carry else None
        result = ListNode(digits.pop(0), None)
        cur_node = result
        while digits:
            new_node = ListNode(digits.pop(0), None)
            cur_node.next = new_node
            cur_node = cur_node.next
        return result


    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Best solution (improvement from sol1) which beats 99% time and 99.5% memory !!!
        carry, sum = divmod(l1.val + l2.val, 10)
        result = ListNode(sum, None)
        cur_node = result
        l1, l2 = l1.next, l2.next
        while l1 and l2:
            carry, sum = divmod(l1.val + l2.val + carry, 10)
            cur_node.next = ListNode(sum)
            l1, l2, cur_node = l1.next, l2.next, cur_node.next
        while l1:
            carry, sum = divmod(l1.val + carry, 10)
            cur_node.next = ListNode(sum)
            l1 , cur_node = l1.next, cur_node.next
        while l2:
            carry, sum = divmod(l2.val + carry, 10)
            cur_node.next = ListNode(sum)
            l2, cur_node = l2.next, cur_node.next
        cur_node.next = ListNode(carry, None) if carry else None
        return result


list1 = ListNode(9, ListNode(9, ListNode(9, None)))
list2 = ListNode(9, ListNode(9, None))
sol = Solution()
print(sol.addTwoNumbers2(list1, list2))
