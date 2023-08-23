# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    # Beats 76% time and 93% memory :)
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copyMap = {}
        def getFromMap(node):
            if not node:
                return None
            elif node not in copyMap:
                newNode = Node(node.val)
                copyMap[node] = newNode
            return copyMap[node]

        newHead = getFromMap(head)

        while head:
            curNewNode = getFromMap(head)
            newNext = getFromMap(head.next)
            newRandom = getFromMap(head.random)
            curNewNode.next = newNext
            curNewNode.random = newRandom
            head = head.next

        return newHead

sol = Solution()
node5 = Node(1, None)
node4 = Node(10, node5, random=node5)
node3 = Node(11, node4, random=node5)
node2 = Node(13, node3, random=node4)
node1 = Node(7, node2, random=node3)

sol.copyRandomList(node1)
