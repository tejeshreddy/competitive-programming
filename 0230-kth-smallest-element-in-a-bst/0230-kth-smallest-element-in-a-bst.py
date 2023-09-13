# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.nodes = []
    
    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        self.nodes.append(root.val)
        self.inOrder(root.right)
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.inOrder(root)
        
        return self.nodes[k - 1]
        