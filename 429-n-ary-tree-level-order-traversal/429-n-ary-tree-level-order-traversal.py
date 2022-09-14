"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root == None:
            return []
        result = []
        q = deque([root])
        
        while q:
            temp = []
            for _ in range(len(q)):
                node = q.popleft()
                temp.append(node.val)
                for child in node.children:
                    q.append(child)
            
            result.append(temp.copy())
        return result