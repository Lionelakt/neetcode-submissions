from typing import Optional
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if node is None:
            return None
        clones = {}

        queue = deque([node])
        clone_node = Node(val = node.val)
        clones[node] = clone_node
        
        while queue:
            cur = queue.popleft()
            cur_clone = clones[cur]

            for nei in cur.neighbors:
                if nei not in clones:
                    queue.append(nei)
                    nei_clone = Node(nei.val)
                    clones[nei] = nei_clone
                cur_clone.neighbors.append(clones[nei])
        return clone_node


