# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0
        self.total = 0
        self.result = 0
        
    def get_total(self, node):
        if not node:
            return
        self.total += node.val
        self.count += 1
        self.get_total(node.left)
        self.get_total(node.right)
        
    
    def depth_first_search(self, node):
        if not node:
           return
        self.count = 0
        self.total = 0
        
        self.get_total(node)
        if self.total // self.count == node.val:
            self.result += 1
        self.depth_first_search(node.left)
        self.depth_first_search(node.right)
        
    
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.depth_first_search(root)
        return self.result
        
            
            