"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def __init__(self):
        self.visited = {}

    def dfs(self, node):
        if node in self.visited:
            return self.visited[node]
        copy_node = Node(node.val)
        self.visited[node] = copy_node
        for neigh in node.neighbors:
            copy_node.neighbors.append(self.dfs(neigh))
        return copy_node

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return self.dfs(node) if node else None
