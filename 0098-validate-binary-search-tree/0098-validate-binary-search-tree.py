# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.nodes = []
    
    def dfs(self, root):
        if not root:
            return
        self.isValidBST(root.left)
        self.nodes.append(root.val)
        self.isValidBST(root.right)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.dfs(root)
        
        if len(self.nodes) < 2:
            return True
        
        for i in range(1, len(self.nodes)):
            if self.nodes[i] <= self.nodes[i - 1]:
                return False
        return True
        
    
    
        
        