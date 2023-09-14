from typing import Optional, List
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Good starting sol - beats 70% time and 44% memory
        if not lists:
            return None
        elems = []
        while lists:
            to_remove = []
            for idx, head in enumerate(lists):
                if head:
                    heapq.heappush(elems, head.val)
                    lists[idx] = head.next if head.next else to_remove.append(idx)
                else:
                    to_remove.append(idx)
            while to_remove:
                lists.pop(to_remove.pop())
        if elems:
            result = ListNode(heapq.heappop(elems))
        else:
            return None
        cur_node = result
        while elems:
            new_node = ListNode(heapq.heappop(elems))
            cur_node.next = new_node
            cur_node = cur_node.next
        return result


    def mergeKLists2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Excellent improvement -> 97% time and 53% memory
        if not lists:
            return None
        elems = []
        n = len(lists)
        while lists:
            appended = False
            for i in range(n):
                if lists[i]:
                    # If we use elems as heap from the start and push using heapq.heappush -> 76% time and 99% memory
                    elems.append(lists[i].val)
                    appended = True
                    lists[i] = lists[i].next
            if not appended:
                break
        # If we use heapify instead of sort -> 76% time and 88% memory
        elems = sorted(elems)
        if elems:
            result = ListNode(elems.pop(0))
        else:
            return None
        cur_node = result
        while elems:
            new_node = ListNode(elems.pop(0))
            cur_node.next = new_node
            cur_node = cur_node.next
        return result



list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))

lists = [list1, list2, list3]
sol = Solution()
sol.mergeKLists(lists)