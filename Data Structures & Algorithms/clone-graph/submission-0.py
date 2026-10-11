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

        # Map from original node to its clone
        clones = {}

        # Create the clone for the root
        #root_clone = Node(node.val)
        #clones[node] = root_clone

        def dfs(node):
            if node in clones:
                return clones[node]
            clone = Node(node.val)
            clones[node] = clone
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone
        return dfs(node) if node else None
    """
        # BFS
        queue = deque([node])
        while queue:
            cur = queue.popleft()
            cur_clone = clones[cur]

            for nei in cur.neighbors:
                if nei not in clones:
                    # Create clone for neighbor on demand
                    nei_clone = Node(nei.val)
                    clones[nei] = nei_clone
                    queue.append(nei)
                # Link the clone of the neighbor to the current clone
                cur_clone.neighbors.append(clones[nei])

        return root_clone
        """