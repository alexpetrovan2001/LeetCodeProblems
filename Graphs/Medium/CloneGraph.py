
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    # Beats 75% in time and 25% in memory
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        node_map = {}

        def dfs(original_node: 'Node'):
            if original_node in node_map:
                return node_map[original_node]

            cloned_node = Node(original_node.val)
            node_map[original_node] = cloned_node

            for neighbor in original_node.neighbors:
                cloned_neighbor = dfs(neighbor)
                cloned_node.neighbors.append(cloned_neighbor)

            return cloned_node

        return dfs(node)

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.neighbors = [node2, node3]
node2.neighbors = [node1, node3]
node3.neighbors = [node1, node2]

sol = Solution()
print(sol.cloneGraph(node1))
