from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None

        hash = {}
        queue = deque([node])

        hash[node] = Node(node.val)

        while queue:
            curr_node = queue.popleft()

            for neighbor in curr_node.neighbors:
                if neighbor not in hash:
                    hash[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                
                hash[curr_node].neighbors.append(hash[neighbor])
        
        return hash[node]